---
title: "Map Algebra Compared with Python"
nav_order: 9
parent: "Language and Expressions"
---
{% raw %}
# Map Algebra Compared with Python

> **Draft.** This page compares the map calculators of Dinamica EGO 8.15.0 with map algebra written in Python using NumPy, rasterio, SciPy, pandas and Numba. Library behaviour is described for current releases of those packages; check their documentation before relying on a specific detail. A companion page, [Map Algebra Compared with GDAL](Map-Algebra-Compared-With-GDAL.html), compares the same features with `gdal raster calc`.

## Overview

Python has no single map algebra tool. The usual equivalent of [Calculate Map](functors/Calculate-Map.html) is a script that reads rasters into NumPy arrays with rasterio, computes the result with array operations, and writes it back with rasterio. SciPy provides neighbourhood filters, pandas provides table joins and Numba compiles custom loops.

The two approaches differ in where the semantics of a calculation live:

- **Calculate Map** evaluates an expression once per cell, and the semantics are built in: null propagation, error recovery, mirrored edges, neighbourhoods that skip null cells, table lookups, alignment of inputs with different extents and resolutions, tiling and parallel execution.
- **Python** evaluates whole arrays at once, and none of these semantics come for free. Each one is a choice of function, argument or helper code, and several of the obvious choices behave differently from Dinamica EGO.

As a result, every Calculate Map calculation can be reproduced in Python, and Python can compute things no calculator expression can, because it is a general-purpose language. The difference is in **how much has to be written** and in how easily the result departs from the intended semantics: a one-line Calculate Map expression typically becomes ten to twenty lines of Python.

This page compares what each approach can express and shows the Python equivalent of each Calculate Map feature, including the places where the obvious Python code gives a different result.

## At a glance

| Capability | Dinamica EGO 8.15.0 (Calculate Map) | Python (NumPy, rasterio, SciPy) |
| --- | --- | --- |
| Evaluation | Per cell | Per array: each operation runs over the whole array |
| Arithmetic, comparison and logical operators | Yes | Yes, element-wise on arrays |
| Bitwise operators | No | `&`, `\|`, `^`, `~`, `<<`, `>>` on integer arrays |
| Conditionals | `if ... then ... else`, short-circuit evaluated | `np.ma.where`, `np.select`; every branch is computed for every cell |
| Mathematical functions | Trigonometric, exp, logarithms, rounding, `clamp`, `clampMod`, `signal` | The full NumPy and SciPy libraries |
| Local variables | `let ... in` | Ordinary variables |
| Several results from one evaluation | Struct expression in [Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html), with shared `let` variables | A `dict` of arrays |
| Missing data | Abstract `null`, propagated automatically | Masked arrays (`numpy.ma`) or NaN; must be chosen and kept consistent |
| Error recovery | `EXPR ? FALLBACK` | Masked arithmetic plus `.filled()`, or `np.errstate` plus `np.where` |
| Halt on an invalid state | `abort` | `raise` |
| Multiband input | Layers are extracted and connected as separate maps | Native, as 3-D arrays |
| Grid position | `line`, `column` | `np.indices` |
| Georeferenced position | Derived from map attributes | `rasterio.transform.xy` |
| Value at another cell | `#map[line, col]`, `#map[[line, col]]`, with mirroring | Fancy indexing plus a user-written mirror function |
| Neighbourhood statistics | `nbMin`, `nbMax`, `nbSum`, `nbProd`, `nbCount`, `nbAverage`, `nbMedian`, `nbMode`, `nbVar`, `nbStdDev`, null cells skipped | `scipy.ndimage` filters and `sliding_window_view`; null cells must be handled explicitly |
| Arg-min / arg-max of a window | `nbMinRef`, `nbMaxRef` | `sliding_window_view` plus `argmin` / `argmax` |
| Convolution | `nbConvol` with any rectangular kernel from a lookup table | `scipy.ndimage.correlate` |
| User-defined window aggregation | `nbReduce` | Numba loop, Numba `@stencil` or `generic_filter` |
| Lookup tables | Exact, bounds, closest key, linear interpolation, key-exists test | `np.searchsorted`, `np.interp`, `np.isin` |
| Multi-column tables | Multi-key join, named or indexed column | `pandas` `MultiIndex` or `merge` |
| Random numbers | `rand`, `rUniform`, `rNormal`, `rPoisson` | `numpy.random.Generator` |
| Whole-map statistics in the same calculation | Through [Extract Map Attributes](functors/Extract-Map-Attributes.html) connected as a table | Any reduction over the array |
| Global operations (connected components, distance maps, iterative solvers) | Other functors in the model | `scipy.ndimage`, scikit-image and other libraries, in the same script |
| Inputs with different extent or resolution | Reconciled automatically by [image virtualization](Image-Virtualization.html) | Resampled explicitly, for example with rioxarray `reproject_match` |
| Out-of-range results | The cell becomes null | Wrap around or are cast silently unless checked |
| Large rasters | Tiled automatically | Whole arrays in memory unless Dask, xarray chunks or rasterio windows are used |
| Native compilation | Automatic with the optional native expression support package | Numba, written explicitly |
| Parallel evaluation | Automatic, on all workers, and on accelerator devices when enabled | Explicit: Numba `prange`, Dask, thread pools or GPU libraries |

## Execution model

| Aspect | Dinamica EGO | Python |
| --- | --- | --- |
| Evaluation | The expression describes the value of one cell; the functor evaluates it for every cell of the result | Each NumPy operation runs over the whole array before the next one starts |
| Binding inputs | Maps, tables and values bound to script variables, referred to as `#name`, `%name` and `$name` in the [abbreviated syntax](EGO-Script.html#calculator-functor-shorthand) | Arrays read with rasterio, tables read with pandas, values as Python numbers |
| Kinds of input | Maps, lookup tables, multi-column tables and scalar values | Any Python object |
| Precision | Always real (double precision), converted to the Cell Type at the end | The data type of the arrays involved; integer arrays use integer arithmetic |
| Alignment | Image virtualization builds a common extent at the highest resolution among the inputs; only the projection must match | Arrays must have the same shape; inputs on different grids are resampled explicitly to a grid you choose |
| Output | One map per functor, or several maps from Calculate Multiple Maps | Any number of arrays, written with rasterio |
| Out-of-range results | The cell becomes null | Integers wrap around and casts are silent unless checked |

Evaluating whole arrays has three consequences that do not exist in Calculate Map:

- **Both branches of a conditional are computed.** `np.where(b != 0, a / b, 0)` divides by zero in the cells where `b == 0` and discards the result. In Dinamica EGO, `if #b != 0 then #a / #b else 0` never evaluates the division in those cells.
- **Intermediate results take memory.** Every sub-expression produces a full array. A long expression over large rasters can need several times the memory of its inputs.
- **Per-cell logic that does not vectorize** (loops, early exits, data-dependent windows) must be written with Numba or other compiled code to run at a comparable speed.

### Inputs and outputs

In EGO Script, maps are read with [Load Map](functors/Load-Map.html) and written with [Save Map](functors/Save-Map.html). The arguments after the expression of a calculator are, in order, its Cell Type, Null Value, Result Sparsity and Result Format; see [Calculate Map](functors/Calculate-Map.html).

```
Script {{
    dem := LoadMap "dem.tif";

    scaled := # [ #dem / 1000 ] .float32 -9999 .auto .none;

    SaveMap scaled "scaled.tif";
}};
```

In Python, the examples on this page use two helpers. `read` returns the first band as a masked array, converted to `float64` because Calculate Map always computes in real numbers. `write` applies the cell type and the null value:

```python
import numpy as np
import pandas as pd
import rasterio
from scipy import ndimage

def read(path):
    with rasterio.open(path) as src:
        return src.read(1, masked=True).astype("float64"), src.profile

def write(path, data, profile, dtype, nodata):
    profile = {**profile, "count": 1, "dtype": dtype, "nodata": nodata}
    with rasterio.open(path, "w", **profile) as dst:
        dst.write(np.ma.masked_invalid(data).filled(nodata).astype(dtype), 1)

dem, profile = read("dem.tif")
write("scaled.tif", dem / 1000, profile, "float32", -9999)
```

The helpers assume that every input is on the same grid. Inputs on different grids must first be resampled, for example with rioxarray `reproject_match(reference)` or a rasterio `WarpedVRT`, choosing the reference grid and the resampling method explicitly. `write` does not reproduce the Calculate Map rule that a value outside the range of the Cell Type becomes null; check the range and mask those cells before writing.

## Feature by feature

Each section below shows a Calculate Map statement and its Python equivalent. The same statements are used on [Map Algebra Compared with GDAL](Map-Algebra-Compared-With-GDAL.html#feature-by-feature).

### Null values and errors

In Dinamica EGO, `null` is an abstract value that propagates through any arithmetic, `isNull` tests it, and `EXPR ? FALLBACK` replaces any algebraic error (division by zero, missing table key, null operand) with another expression. `abort` halts the model when the expression reaches an invalid state. See [Null Value Handling](Calculate-Functors.html#null-value-handling).

```
// Biomass per unit of area; 0 where either map is null or the area is zero
ratio := # [ (#biomass / #area) ? 0 ] .float32 .default .auto .none;
```

Masked arrays are the closest match to Dinamica EGO's null: a masked operand makes the result masked, and NumPy's masked division, square root and logarithm mask invalid results such as division by zero.

```python
ratio = (biomass / area).filled(0)
```

| Dinamica EGO | Python (masked arrays) |
| --- | --- |
| `null` | `np.ma.masked` |
| `isNull(e)` | `np.ma.getmaskarray(e)` |
| `e ? fallback` | `e.filled(fallback)`, or `np.ma.where(np.ma.getmaskarray(e), fallback, e)` when the fallback is an array |
| `if c then a else b` | `np.ma.where(c, a, b)` |
| `null(#map)` | `src.nodata` |
| `abort` | `raise` |

`np.where` (without `.ma`) **drops the mask** of its arguments and returns an ordinary array, so a null cell silently becomes the sentinel stored behind the mask. Use `np.ma.where`.

Dinamica EGO also nulls a conditional whose test is null. `np.ma.where` with a masked condition gives a masked result as well, but code that converts the condition with `.filled(False)` changes this behaviour.

### Local variables and several outputs

`let ... in` evaluates a sub-expression once per cell and names it. In Calculate Multiple Maps, the variables are shared by every output:

```
indices := #* [
    let _ndvi: (#nir - #red) / (#nir + #red) in
    { ndvi: _ndvi, vigorous: if _ndvi > 0.6 then 1 else 0 }
] .float32 .default .auto .none;
```

In Python, an intermediate result is an ordinary variable, and several results are a `dict` of arrays:

```python
ndvi = (nir - red) / (nir + red)
indices = {"ndvi": ndvi, "vigorous": np.ma.where(ndvi > 0.6, 1, 0)}
```

### Grid position and values at other cells

`line` and `column` give the 1-based position of the current cell. `#map[LINE, COL]` reads a map at a computed coordinate: coordinates outside the map are mirrored back into range, and a null target reads as 0. `#map[[LINE, COL]]` does the same but keeps the null. Because the coordinates are ordinary expressions, the cell read can depend on other maps or tables:

```
// Elevation at the cell pointed to by the row and column offsets of a flow direction
downstream := # [ #elevation[[line + #rowOffset, column + #columnOffset]] ] .float32 .default .auto .none;
```

In Python, the grid position comes from `np.indices` and the cell is read by fancy indexing. The `mirror` helper reproduces the mirror formula given in [Image Operators and Functions](Calculate-Functors.html#4-image-operators-and-functions) and returns 0-based indices:

```python
def mirror(i, n):
    """1-based coordinate -> 0-based index, mirrored like #map[LINE, COL]."""
    i = np.asarray(i)
    i = np.where(i <= 0, 1 - i, i)
    i = np.where(i > n, 2 * n + 1 - i, i)
    return i - 1

rows, cols = elevation.shape
L, C = np.indices(elevation.shape) + 1                       # line, column
offset_null = np.ma.getmaskarray(row_offset) | np.ma.getmaskarray(column_offset)
r = mirror(L + row_offset.filled(0).astype(np.int64), rows)
c = mirror(C + column_offset.filled(0).astype(np.int64), cols)
downstream = np.ma.masked_where(offset_null, elevation[r, c])  # #elevation[[...]]
# #elevation[...] would be elevation.filled(0)[r, c]
```

### Neighbourhoods

The `nbN` functions aggregate a rectangular window, skipping null cells and mirroring the cells outside the map. Because they are ordinary expressions, they can be combined with conditionals, tables and other windows in the same calculation, and the window can be anchored anywhere, not just at the current cell:

```
// Local relief, only where the cell is forest (class 3) and the 5x5 window is mostly valid
relief := # [
    if #landuse == 3 and nbCount(#dem, 5, 5) >= 20
    then nbMax(#dem, 5, 5) - nbMin(#dem, 5, 5)
    else null
] .float32 .default .auto .none;
```

`nbMinRef` and `nbMaxRef` return the position of the window minimum or maximum, mapped to a lookup table or to a second map. `nbConvol` applies any rectangular kernel stored in a lookup table.

SciPy's `mode="reflect"` extends the array by repeating the edge cell (`d c b a | a b c d`), which matches the Dinamica EGO mirror formula. The SciPy filters do not skip null cells, so the statistics that Dinamica EGO computes over non-null cells need the validity mask as a separate array:

```python
def nb_count(a, h, w):
    valid = ~np.ma.getmaskarray(a)
    return ndimage.correlate(valid.astype(float), np.ones((h, w)), mode="reflect")

def nb_sum(a, h, w):
    vals = np.where(np.ma.getmaskarray(a), 0.0, a.filled(0))
    return ndimage.correlate(vals, np.ones((h, w)), mode="reflect")

def nb_average(a, h, w):
    n = nb_count(a, h, w)
    return np.ma.masked_where(n == 0, nb_sum(a, h, w) / np.maximum(n, 1))

def nb_max(a, h, w):
    vals = np.where(np.ma.getmaskarray(a), -np.inf, a.filled(0))
    return np.ma.masked_invalid(ndimage.maximum_filter(vals, size=(h, w), mode="reflect"))

def nb_min(a, h, w):
    vals = np.where(np.ma.getmaskarray(a), np.inf, a.filled(0))
    return np.ma.masked_invalid(ndimage.minimum_filter(vals, size=(h, w), mode="reflect"))

keep = (landuse == 3).filled(False) & (nb_count(dem, 5, 5) >= 20)
relief = np.ma.masked_where(~keep, nb_max(dem, 5, 5) - nb_min(dem, 5, 5))
```

These helpers are correct for odd window sizes; see the last row of the table below for even sizes.

| Dinamica EGO | Python | Difference to handle |
| --- | --- | --- |
| `nbSum`, `nbCount`, `nbAverage` | `ndimage.correlate` of values and mask, as above | `uniform_filter` alone counts null cells |
| `nbMin`, `nbMax` | `ndimage.minimum_filter`, `maximum_filter`, as above | Fill null cells with `+inf` or `-inf` first |
| `nbProd` | `sliding_window_view` plus `np.nanprod` | — |
| `nbMedian` | `sliding_window_view` plus `np.partition` | For an even count Dinamica EGO returns the **greater** central value; `np.median` and `np.nanmedian` return the average |
| `nbMode` | `scipy.stats.mode` over `sliding_window_view` | Ties go to the lesser value in both; Dinamica EGO returns null when no value repeats |
| `nbVar`, `nbStdDev` | `np.nanvar`, `np.nanstd` over `sliding_window_view` | Both are population statistics (`ddof=0`) |
| `nbConvol` | `ndimage.correlate(vals, kernel, mode="reflect")` | Use `correlate`, not `convolve`: `convolve` flips the kernel, while `nbConvol` applies coefficient 1 to the top-left cell |
| `nbMinRef`, `nbMaxRef` | `argmin` / `argmax` over `sliding_window_view` | Fill null cells first; ties go to the first cell in both |
| Anchored window (`y`, `x` arguments) | Compute the filter, then index it at the anchor coordinates | — |
| Even-sized window | `origin=-1` along each even dimension, for example `origin=(-1, 0)` for a 4 × 3 window | With the default `origin=0`, SciPy covers 2 rows above and 1 below the centre of a 4-row window; Dinamica EGO covers 1 above and 2 below |

`sliding_window_view` builds a view, not a copy, but reductions over it allocate `rows × cols × h × w` values. For windows larger than a few cells, a Numba loop is usually faster and uses far less memory.

### User-defined window aggregation

`nbReduce` folds a window into one value with an accumulator written in the expression itself. It covers every built-in neighbourhood operator except `nbMedian` and `nbMode`, and any other aggregation that can be computed with a running accumulator. It can also read other maps at each window element:

```
// Sum of the biomass over the cells of the 5x5 window that have the same class as the centre cell
classBiomass := # [
    nbReduce(#landuse, 0,
        if not isNull(_elem) and _elem == #landuse then _acc + #biomass[_eline, _ecolumn] else _acc,
        5, 5)
] .float32 .default .auto .none;
```

In Python, `nbReduce` corresponds to a compiled loop. With `parallel=True` and `prange`, Numba distributes the rows among threads; with `@njit` and `range` alone, the loop runs on one thread. See [Parallel execution](#parallel-execution).

```python
from numba import njit, prange

@njit(inline="always")
def _mirror(i, n):
    # 0-based index mirrored like the Dinamica EGO windows
    return -i - 1 if i < 0 else (2 * n - i - 1 if i >= n else i)

@njit(parallel=True, cache=True)
def class_biomass(landuse, landuse_valid, biomass):
    rows, cols = landuse.shape
    out = np.empty((rows, cols))
    for r in prange(rows):              # rows distributed among threads
        for c in range(cols):
            acc = 0.0
            for dr in range(-2, 3):
                rr = _mirror(r + dr, rows)
                for dc in range(-2, 3):
                    cc = _mirror(c + dc, cols)
                    if landuse_valid[rr, cc] and landuse[rr, cc] == landuse[r, c]:
                        acc += biomass[rr, cc]
            out[r, c] = acc
    return out

landuse_null = np.ma.getmaskarray(landuse)
result = class_biomass(landuse.filled(0), ~landuse_null, biomass.filled(0))  # #biomass[...] reads null as 0
class_biomass_map = np.ma.masked_array(result, mask=landuse_null)          # null centre -> null result
```

`numba.set_num_threads(n)` or the `NUMBA_NUM_THREADS` environment variable sets the number of threads.

### Tables

Lookup tables give per-cell joins with exact, bound, closest-key and interpolated lookups. Multi-column tables join on several keys at once:

```
// Transition probability keyed by land-use class and elevation zone, weighted by a factor interpolated by slope
probability := # [
    %transitions[[#landuse, %zones[<= #elevation]]] * %slopeFactor[/ #slope]
] .float32 .default .auto .none;
```

In Python, a lookup table becomes a pair of sorted `keys` and `values` arrays, and a multi-column table a pandas `Series` indexed by its key columns. The helpers below reproduce the three lookups of the statement, including the null results:

```python
def lookup_le(keys, values, x):
    """tX[<= x]: value of the greatest key <= x; keys sorted."""
    i = np.searchsorted(keys, x.filled(-np.inf), side="right") - 1
    return np.ma.masked_array(values[np.maximum(i, 0)], mask=(i < 0) | np.ma.getmaskarray(x))

def lookup_interp(keys, values, x):
    """tX[/ x]: linear interpolation; null outside [keys[0], keys[-1]]."""
    xf = x.filled(np.nan)
    outside = np.ma.getmaskarray(x) | ~((xf >= keys[0]) & (xf <= keys[-1]))
    return np.ma.masked_where(outside, np.interp(xf, keys, values))

def lookup_keys(table, k1, k2):
    """tX[[k1, k2]]: table is a Series indexed by (key1, key2)."""
    k1, k2 = np.ma.asarray(k1).astype("float64"), np.ma.asarray(k2).astype("float64")
    keys = pd.MultiIndex.from_arrays([k1.filled(np.nan).ravel(), k2.filled(np.nan).ravel()])
    i = table.index.get_indexer(keys).reshape(k1.shape)
    nulls = (i < 0) | np.ma.getmaskarray(k1) | np.ma.getmaskarray(k2)
    return np.ma.masked_array(table.to_numpy()[np.maximum(i, 0)], mask=nulls)

probability = (lookup_keys(transitions, landuse, lookup_le(zone_keys, zone_ids, elevation))
               * lookup_interp(slope_keys, slope_factors, slope))
```

| Dinamica EGO | Python (sorted `keys` and matching `values` arrays) |
| --- | --- |
| `tX[e]` | `i = np.searchsorted(keys, e)`; found where `i < len(keys)` and `keys[i] == e`; mask the rest |
| `tX[<= e]` | `i = np.searchsorted(keys, e, side="right") - 1`; mask where `i < 0` |
| `tX[< e]` | `i = np.searchsorted(keys, e, side="left") - 1`; mask where `i < 0` |
| `tX[>= e]` | `i = np.searchsorted(keys, e, side="left")`; mask where `i == len(keys)` |
| `tX[> e]` | `i = np.searchsorted(keys, e, side="right")`; mask where `i == len(keys)` |
| `tX[/ e]` | `np.interp(e, keys, values)`, masked outside `[keys[0], keys[-1]]` |
| `tX[? e]` | `np.isin(e, keys)` |
| `tX[[k1, k2]]` | `pandas` `MultiIndex.get_indexer` on the flattened key arrays, or `merge` |

Two details matter. `np.interp` returns the first or last value for keys outside the table range, while `tX[/ e]` returns null there; inside the range, including at the first and last keys, both give the same values. And null cells must be filled with a value that cannot match any key before calling `np.searchsorted`: NaN sorts after every key, so a null filled with NaN would be read as the last key.

### Random numbers

`rand`, `rUniform`, `rNormal` and `rPoisson` draw one sample per cell. This allows stochastic allocation and Monte Carlo perturbation in a single calculation:

```
allocated := ## [ if rand < %probabilityByClass[#landuse] then 1 else 0 ] .uint8 .default .auto .none;
```

In Python, the samples come from a `numpy.random.Generator`, one array at a time:

```python
rng = np.random.default_rng(seed)
rng.random(shape)            # rand
rng.uniform(lo, hi, shape)   # rUniform(lo, hi)
rng.normal(mean, sd, shape)  # rNormal(mean, sd)
rng.poisson(lam, shape)      # rPoisson(lam)
```

Dinamica EGO draws only for the cells actually evaluated. NumPy draws for every cell of the array, which matters only when reproducing a sequence with a fixed seed.

## What Python expresses that Calculate Map does not

- **Multiband rasters as arrays.** `src.read()` returns a 3-D array, and operations broadcast over bands: `(a + b).mean(axis=0)` averages the band sums. Dinamica EGO computes the same results once the layers are extracted with [Extract Map Layer](functors/Extract-Map-Layer.html) and connected as separate maps, as shown in [Multiband rasters](Map-Algebra-Compared-With-GDAL.html#multiband-rasters) on the GDAL page.
- **Georeferenced coordinates.** `rasterio.transform.xy(transform, rows, cols)` gives the coordinates of the cell centres in the CRS of the raster. Dinamica EGO exposes the grid position (`line`, `column`) instead. The georeferenced position can be derived by connecting the output of [Extract Map Attributes](functors/Extract-Map-Attributes.html) as a table and combining `line` and `column` with the registration coordinate, registration cell and original cell size attributes.
<!-- TODO: confirm the registration convention (corner or centre, line direction) and add the exact formula. -->
- **Bitwise operators** on integer arrays, useful for quality-flag bands. Dinamica EGO extracts a bit with arithmetic, for example `floor(#qa / 2 ^ 3) % 2` for bit 3.
- **The full NumPy and SciPy mathematical libraries**, including hyperbolic and special functions. Dinamica EGO builds the hyperbolic functions from `exp` and `ln`, for example `(exp(#x) - exp(-#x)) / 2` for `sinh`.
- **Arbitrary control flow** inside the per-cell logic: loops with a data-dependent number of steps, early exits and recursion, through Numba or plain Python.
- **Global operations** in the same script: connected-component labelling, distance transforms, flow accumulation, iterative solvers and whole-map statistics. In Dinamica EGO these are separate functors connected in the model, and whole-map statistics reach an expression through [Extract Map Attributes](functors/Extract-Map-Attributes.html).
- **Multidimensional data**: band stacks and time series as 3-D or 4-D arrays with xarray, reduced along any dimension.
- **The Python ecosystem**: machine-learning models from scikit-learn or PyTorch applied cell by cell, and statistics from SciPy and statsmodels.

## What Calculate Map provides that Python leaves to the programmer

- **Null semantics** applied consistently to every operator, conditional, table lookup and neighbourhood, with `?` for error recovery.
- **Short-circuit conditionals** that skip work and never evaluate an invalid branch.
- **Mirrored edges and null-skipping windows** in every neighbourhood function, without choosing modes or building masks.
- **Neighbourhoods, tables and random numbers composed in one expression**, where each can depend on the others cell by cell.
- **Alignment of inputs** with different extents and resolutions.
- **Range checking**: a value outside the range of the Cell Type becomes null instead of wrapping around.
- **Scaling**: tiled, parallel evaluation, native compilation, and skipping the null cells of sparse maps when the expression allows it (see [Null-strict maps](Calculate-Functors.html#null-strict-maps)). The Python equivalent requires Dask or windowed I/O, with overlapping chunks for neighbourhoods.

## Composing calculations

In Python, a multi-step calculation is ordinary code: each step is a function call whose result is passed to the next one, and steps can be organized in functions and modules. Dask and xarray can defer the steps and evaluate them chunk by chunk when the result is written.

Dinamica EGO composes calculations through the model graph. Calculators, other functors, submodels and containers such as [Repeat](functors/Repeat.html) and [For Each](functors/For-Each.html) connect through ports, and the graph also provides iteration and control flow outside the expressions. Both approaches therefore reach multi-step results. The difference is that a single Calculate Map expression already combines neighbourhood, table and random operations cell by cell, where Python needs a separate array operation, with its own null handling, for each of them.

## Side-by-side examples

Each example below is complete: the EGO script and the Python script read the same input files and write the same result. The Python scripts use the `read` and `write` helpers from [Inputs and outputs](#inputs-and-outputs), and the second and third examples also use the neighbourhood and table helpers defined above. The same examples are shown with GDAL on [Map Algebra Compared with GDAL](Map-Algebra-Compared-With-GDAL.html#side-by-side-examples).

### Masked index

```
Script {{
    nir := LoadMap "nir.tif";
    red := LoadMap "red.tif";
    cloud := LoadMap "cloud.tif";

    ndvi := # [ if #cloud == 0 then (#nir - #red) / (#nir + #red) else null ] .float32 -9999 .auto .none;

    SaveMap ndvi "ndvi.tif";
}};
```

```python
nir, profile = read("nir.tif")
red, _ = read("red.tif")
cloud, _ = read("cloud.tif")

ndvi = np.ma.where(cloud == 0, (nir - red) / (nir + red), np.ma.masked)

write("ndvi.tif", ndvi, profile, "float32", -9999)
```

### Focal statistic where a condition holds

```
Script {{
    dem := LoadMap "dem.tif";
    landuse := LoadMap "landuse.tif";

    tpi := # [ if #landuse == 3 then #dem - nbAverage(#dem, 5, 5) else null ] .float32 -9999 .auto .none;

    SaveMap tpi "tpi.tif";
}};
```

```python
dem, profile = read("dem.tif")
landuse, _ = read("landuse.tif")

tpi = np.ma.where(landuse == 3, dem - nb_average(dem, 5, 5), np.ma.masked)

write("tpi.tif", tpi, profile, "float32", -9999)
```

### Table-driven, stochastic allocation

`probability.csv` holds the transition probability for each pair of land-use class and elevation zone, with both key columns marked with `*` in its header, and `zones.csv` maps the lower bound of each elevation range to its zone.

```
Script {{
    landuse := LoadMap "landuse.tif";
    elevation := LoadMap "elevation.tif";
    probability := LoadTable "probability.csv";
    zones := LoadLookupTable "zones.csv";

    allocated := ## [
        let _p: (%probability[[#landuse, %zones[<= #elevation]]]) ? 0 in
        if rand < _p then 1 else 0
    ] .uint8 255 .auto .none;

    SaveMap allocated "allocated.tif";
}};
```

```python
landuse, profile = read("landuse.tif")
elevation, _ = read("elevation.tif")
table = pd.read_csv("probability.csv")
probability = table.set_index(list(table.columns[:2]))[table.columns[2]]
zones = pd.read_csv("zones.csv")
zones = zones.sort_values(zones.columns[0])
zone_keys, zone_ids = zones.iloc[:, 0].to_numpy(), zones.iloc[:, 1].to_numpy()

p = lookup_keys(probability, landuse, lookup_le(zone_keys, zone_ids, elevation)).filled(0)
allocated = np.ma.masked_array((np.random.default_rng().random(landuse.shape) < p).astype("uint8"))

write("allocated.tif", allocated, profile, "uint8", 255)
```

## Parallel execution

Dinamica EGO parallelizes a map calculation without any change to the expression. The cells of the result are divided into contiguous ranges, one per task, and the tasks run on the workers described in [Parallel Execution](Parallel-Execution.html); the number of tasks follows the [granularity](Parallel-Execution.html#granularity). Each task has its own copy of the local variables. This is safe for every expression because a calculator expression only computes the value of its own cell: it reads the input maps, tables and values, but cannot write to another cell or keep state between cells.

The calculation runs on a single task when the input maps cannot be read in parallel or the result cannot be written in parallel, and when it visits only the non-null cells of a sparse null-strict map (see [Null-strict maps](Calculate-Functors.html#null-strict-maps)). When accelerator devices are enabled, an expression that is complex enough and compatible with them can run on an OpenCL device instead; expressions that use `nbReduce` are not compatible.

In Python, parallel execution is never automatic for this kind of code:

- NumPy element-wise operations run on one thread. Only linear algebra, through a multithreaded BLAS library, uses several.
- The `scipy.ndimage` filters run on one thread.
- A Numba `@njit` function runs its loops in sequence.

The program has to request parallel execution and guarantee that it is safe. The options are:

| Approach | How | Notes |
| --- | --- | --- |
| Numba parallel loops | `@njit(parallel=True)` and `prange` for the outer loop, as in [User-defined window aggregation](#user-defined-window-aggregation) | Iterations must be independent; only scalar reductions such as `total += x` are handled safely |
| Dask | `dask.array` chunks and `map_overlap(func, depth=..., boundary=...)` for neighbourhoods | Also processes rasters larger than memory; set `boundary` so the edges are mirrored as in Dinamica EGO |
| Thread pool over windows | `concurrent.futures.ThreadPoolExecutor` with rasterio windowed reads and writes | Only faster when the work releases the global interpreter lock, as NumPy, rasterio I/O and Numba with `nogil=True` do; neighbourhood windows must overlap |
| GPU | CuPy, or `numba.cuda` with one thread per cell | Data must be copied to and from the device |

With `prange`, the program asserts that the iterations of the loop are independent. In `class_biomass` this holds because each iteration writes only `out[r, c]`. A loop that writes to cells computed by other iterations, or accumulates into a shared array, produces wrong results without any error. In Dinamica EGO this guarantee comes from the expression language itself.

## Beyond expressive power

Expressive power is only one criterion. Python is a general-purpose language with a very large ecosystem for data analysis, statistics and machine learning, and it runs anywhere Python is installed. Dinamica EGO compiles expressions to native code when the optional native expression support package is installed, skips the null cells of sparse maps when the expression allows it (see [Null-strict maps](Calculate-Functors.html#null-strict-maps)), and integrates the calculation into a model with iteration, calibration and submodels.

## Using Python with a Dinamica EGO model

[Calculate Python Expression](functors/Calculate-Python-Expression.html) runs Python inside a model, but it accepts only tables, values and strings: maps cannot be passed to it. To combine Python map algebra with a model, save the maps to files with [Save Map](functors/Save-Map.html), process them in Python and load the results back with [Load Map](functors/Load-Map.html), or move the calculation into Calculate Map.

## See also

- [Map Algebra Compared with GDAL](Map-Algebra-Compared-With-GDAL.html)
- [Calculate Functors — Complete Operator Documentation](Calculate-Functors.html)
- [Calculate Map](functors/Calculate-Map.html)
- [Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html)
- [Calculate Python Expression](functors/Calculate-Python-Expression.html)
- [Image Virtualization](Image-Virtualization.html)
- [Parallel Execution](Parallel-Execution.html)
- [NumPy masked arrays](https://numpy.org/doc/stable/reference/maskedarray.html), [scipy.ndimage](https://docs.scipy.org/doc/scipy/reference/ndimage.html), [rasterio](https://rasterio.readthedocs.io/) and [Numba](https://numba.readthedocs.io/)

{% endraw %}
