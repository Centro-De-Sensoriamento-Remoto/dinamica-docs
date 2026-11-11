---
title: "Map Algebra Compared with Python"
nav_order: 6
parent: "Language and Expressions"
---
{% raw %}
# Map Algebra Compared with Python

> **Draft.** This page compares the map calculators of Dinamica EGO 8.15.0 with map algebra written in Python using NumPy, rasterio and SciPy. Library behaviour is described for current releases of those packages; check their documentation before relying on a specific detail.

## Overview

Python has no single map algebra tool. The usual equivalent of [Calculate Map](functors/Calculate-Map.html) is a script that reads rasters into NumPy arrays with rasterio, computes the result with array operations, and writes it back with rasterio. SciPy provides neighbourhood filters, pandas provides table joins and Numba compiles custom loops.

Python is a general-purpose language, so every Calculate Map expression can be reproduced in Python, and Python can compute things no calculator expression can. The difference is in **how much has to be written**:

- **Calculate Map** evaluates an expression once per cell, and the semantics are built in: null propagation, error recovery, mirrored edges, neighbourhoods that skip null cells, table lookups, alignment of inputs with different extents and resolutions, tiling and parallel execution.
- **Python** evaluates whole arrays at once, and none of these semantics come for free. Each one is a choice of function, argument or helper code, and several of the obvious choices behave differently from Dinamica EGO.

A one-line Calculate Map expression typically becomes ten to twenty lines of Python. This page shows the correspondence construct by construct, lists the places where the obvious Python code gives a different result, and compares what each approach can express.

## At a glance

| Capability | Dinamica EGO 8.15.0 (Calculate Map) | Python (NumPy, rasterio, SciPy) |
| --- | --- | --- |
| Arithmetic, comparison and logical operators | Built in | Built in, element-wise on arrays |
| Bitwise operators | No | `&`, `\|`, `^`, `~`, `<<`, `>>` on integer arrays |
| Conditionals | `if ... then ... else`, short-circuit evaluated | `np.ma.where`, `np.select`; every branch is computed for every cell |
| Local variables and several outputs | `let ... in`, struct expressions | Ordinary variables, a `dict` of arrays |
| Missing data | Abstract `null`, propagated automatically | Masked arrays (`numpy.ma`) or NaN; must be chosen and kept consistent |
| Error recovery | `EXPR ? FALLBACK` | Masked arithmetic plus `.filled()`, or `np.errstate` plus `np.where` |
| Inputs with different extent or resolution | Reconciled automatically by [image virtualization](Image-Virtualization.html) | Resampled explicitly, for example with rioxarray `reproject_match` |
| Grid position | `line`, `column` | `np.indices` |
| Value at another cell | `iX[line, col]`, `iX[[line, col]]`, with mirroring | Fancy indexing plus a user-written mirror function |
| Neighbourhood statistics | `nbMin` ... `nbStdDev`, null cells skipped | `scipy.ndimage` filters; null cells must be handled explicitly |
| Convolution | `nbConvol` | `scipy.ndimage.correlate` |
| Arg-min / arg-max of a window | `nbMinRef`, `nbMaxRef` | `sliding_window_view` plus `argmin` / `argmax` |
| User-defined window aggregation | `nbReduce` | Numba `@stencil` or `@njit` loop, or `generic_filter` |
| Lookup tables | Exact, bounds, closest key, interpolation, key-exists test | `np.searchsorted`, `np.interp`, `pandas` |
| Multi-column tables | Multi-key join | `pandas` `MultiIndex` or `merge` |
| Random numbers | `rand`, `rUniform`, `rNormal`, `rPoisson` | `numpy.random.Generator` |
| Whole-map statistics in the same calculation | Through [Extract Map Attributes](functors/Extract-Map-Attributes.html) connected as a table | Any reduction over the array |
| Global operations (connected components, distance transforms, iterative solvers) | Other functors in the model | `scipy.ndimage`, scikit-image and any other library |
| Out-of-range results | The cell becomes null | Wrap around or are cast silently unless checked |
| Large rasters | Tiled automatically | Whole arrays in memory unless Dask, xarray chunks or rasterio windows are used |
| Native compilation | Automatic with the optional native expression support package | Numba, written explicitly |
| Parallel evaluation | Automatic, on all workers, and on accelerator devices when enabled | Explicit: Numba `prange`, Dask, thread pools or GPU libraries |

## Execution model

Calculate Map is a **per-cell** language: the expression describes the value of one cell, and the functor evaluates it for every cell of the output map, in parallel, tile by tile.

NumPy is a **per-array** language: each operation runs over the whole array before the next one starts. This has three consequences:

- **Both branches of a conditional are computed.** `np.where(b != 0, a / b, 0)` divides by zero in the cells where `b == 0` and discards the result. In Dinamica EGO, `if i2 != 0 then i1 / i2 else 0` never evaluates the division in those cells.
- **Intermediate results take memory.** Every sub-expression produces a full array. A long expression over large rasters can need several times the memory of its inputs.
- **Per-cell logic that does not vectorize** (loops, early exits, data-dependent windows) must be written with Numba or other compiled code to run at a comparable speed.

## Construct-by-construct correspondence

### Reading inputs

| Dinamica EGO | Python |
| --- | --- |
| Map connected through [Number Map](functors/Number-Map.html), referenced as `iX` or `#name` | `rasterio.open(path).read(1, masked=True).astype("float64")` |
| Table connected through [Number Table](functors/Number-Table.html) | `pandas.read_csv(path)` or a `dict` |
| Value connected through [Number Value](functors/Number-Value.html) | A Python number |
| Image virtualization | `rioxarray` `reproject_match(reference)`, or a rasterio `WarpedVRT` with the target grid |

Two details matter:

- **Convert to `float64`.** Calculate Map always computes in real numbers. NumPy keeps the data type of the input, so integer arrays use integer arithmetic, overflow silently and give integer results for some operations.
- **Choose the reference grid explicitly.** Image virtualization builds a common extent at the highest resolution among the inputs. Python resamples to whatever grid you pass, with the resampling method you choose.

### Null values and errors

Masked arrays are the closest match to Dinamica EGO's null: a masked operand makes the result masked, and NumPy's masked division, square root and logarithm mask invalid results such as division by zero.

| Dinamica EGO | Python (masked arrays) |
| --- | --- |
| `null` | `np.ma.masked` |
| `isNull(e)` | `np.ma.getmaskarray(e)` |
| `e ? fallback` | `e.filled(fallback)`, or `np.ma.where(np.ma.getmaskarray(e), fallback, e)` when the fallback is an array |
| `if c then a else b` | `np.ma.where(c, a, b)` |
| `null(iX)` | `src.nodata` |

`np.where` (without `.ma`) **drops the mask** of its arguments and returns an ordinary array, so a null cell silently becomes the sentinel stored behind the mask. Use `np.ma.where`.

Dinamica EGO also nulls a conditional whose test is null. `np.ma.where` with a masked condition gives a masked result as well, but code that converts the condition with `.filled(False)` changes this behaviour. See [Null Value Handling](Calculate-Functors.html#null-value-handling) for the full Dinamica EGO rules.

### Local variables and several outputs

```
indices := #* [
    let _ndvi: (#nir - #red) / (#nir + #red) in
    { ndvi: _ndvi, vigorous: if _ndvi > 0.6 then 1 else 0 }
] .float32 .default .auto .none;
```

```python
ndvi = (nir - red) / (nir + red)
outputs = {"ndvi": ndvi, "vigorous": np.ma.where(ndvi > 0.6, 1, 0)}
```

### Grid position and values at other cells

`line` and `column` are 1-based in Dinamica EGO:

```python
L, C = np.indices(a.shape) + 1
```

`iX[LINE, COL]` mirrors coordinates outside the map back into range and reads a null target as 0. The helper below reproduces the mirror formula given in [Image Operators and Functions](Calculate-Functors.html#4-image-operators-and-functions) and returns 0-based indices:

```python
def mirror(i, n):
    """1-based coordinate -> 0-based index, mirrored like iX[LINE, COL]."""
    i = np.asarray(i)
    i = np.where(i <= 0, 1 - i, i)
    i = np.where(i > n, 2 * n + 1 - i, i)
    return i - 1

rows, cols = a.shape
at = a.filled(0)[mirror(Lexpr, rows), mirror(Cexpr, cols)]   # iX[LINE, COL]
at_nulls = a[mirror(Lexpr, rows), mirror(Cexpr, cols)]       # iX[[LINE, COL]]
```

### Neighbourhoods

SciPy's `mode="reflect"` extends the array by repeating the edge cell (`d c b a | a b c d`), which matches the Dinamica EGO mirror formula. The SciPy filters do not skip null cells, so the statistics that Dinamica EGO computes over non-null cells need the validity mask as a separate array:

```python
valid = ~np.ma.getmaskarray(a)
vals = np.where(valid, a.filled(0), 0.0)
k = np.ones((h, w))

nb_sum   = ndimage.correlate(vals, k, mode="reflect")                  # nbSum
nb_count = ndimage.correlate(valid.astype(float), k, mode="reflect")   # nbCount
nb_avg   = np.ma.masked_where(nb_count == 0, nb_sum / np.maximum(nb_count, 1))  # nbAverage
```

| Dinamica EGO | Python | Difference to handle |
| --- | --- | --- |
| `nbSum`, `nbCount`, `nbAverage` | `ndimage.correlate` of values and mask, as above | `uniform_filter` alone counts null cells |
| `nbMin`, `nbMax` | `ndimage.minimum_filter`, `maximum_filter` | Fill null cells with `+inf` or `-inf` first |
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

`nbReduce` corresponds to a compiled loop. The example below reproduces the Dinamica EGO expression `nbReduce(i1, 0, if isNull(_elem) then _acc + 10 else _acc + _elem, 3, 3)`. With `parallel=True` and `prange`, Numba distributes the rows among threads; with `@njit` and `range` alone, the loop runs on one thread. See [Parallel execution](#parallel-execution).

```python
from numba import njit, prange

@njit(inline="always")
def _mirror(i, n):
    # 0-based index mirrored like the Dinamica EGO windows
    return -i - 1 if i < 0 else (2 * n - i - 1 if i >= n else i)

@njit(parallel=True, cache=True)
def reduce_3x3(vals, valid):
    rows, cols = vals.shape
    out = np.empty((rows, cols))
    for r in prange(rows):              # rows distributed among threads
        for c in range(cols):
            acc = 0.0
            for dr in range(-1, 2):
                rr = _mirror(r + dr, rows)
                for dc in range(-1, 2):
                    cc = _mirror(c + dc, cols)
                    acc = acc + vals[rr, cc] if valid[rr, cc] else acc + 10.0
            out[r, c] = acc
    return out
```

`numba.set_num_threads(n)` or the `NUMBA_NUM_THREADS` environment variable sets the number of threads.

### Tables

| Dinamica EGO | Python (sorted `keys` and matching `values` arrays) |
| --- | --- |
| `tX[e]` | `i = np.searchsorted(keys, e)`; found where `i < len(keys)` and `keys[i] == e`; mask the rest |
| `tX[<= e]` | `i = np.searchsorted(keys, e, side="right") - 1`; mask where `i < 0` |
| `tX[< e]` | `i = np.searchsorted(keys, e, side="left") - 1`; mask where `i < 0` |
| `tX[>= e]` | `i = np.searchsorted(keys, e, side="left")`; mask where `i == len(keys)` |
| `tX[> e]` | `i = np.searchsorted(keys, e, side="right")`; mask where `i == len(keys)` |
| `tX[/ e]` | `np.ma.masked_where((e < keys[0]) \| (e > keys[-1]), np.interp(e, keys, values))` |
| `tX[? e]` | `np.isin(e, keys)` |
| `tX[[k1, k2]]` | `pandas` `MultiIndex.get_indexer` on the flattened key arrays, or `merge` |

`np.interp` returns the first or last value for keys outside the table range, while `tX[/ e]` returns null there, so the result must be masked outside `[keys[0], keys[-1]]` as shown. Inside the range, including at the first and last keys, both give the same values.

### Random numbers

```python
rng = np.random.default_rng(seed)
rng.random(shape)            # rand
rng.uniform(lo, hi, shape)   # rUniform(lo, hi)
rng.normal(mean, sd, shape)  # rNormal(mean, sd)
rng.poisson(lam, shape)      # rPoisson(lam)
```

Dinamica EGO draws only for the cells actually evaluated. NumPy draws for every cell of the array, which matters only when reproducing a sequence with a fixed seed.

### Output

| Dinamica EGO | Python |
| --- | --- |
| Cell Type | `astype(...)` before writing |
| Null Value | `filled(nodata)` and the `nodata` entry of the rasterio profile |
| Values outside the Cell Type range become null | Check the range and mask before casting; NumPy otherwise wraps integers or casts silently |
| `abort` | `raise` |

## What Python expresses that Calculate Map does not

- **Arbitrary control flow** inside the per-cell logic: loops with a data-dependent number of steps, early exits and recursion, through Numba or plain Python.
- **Bitwise operators** on integer arrays, useful for quality-flag bands.
- **Global operations** in the same script: connected-component labelling, distance transforms, flow accumulation, iterative solvers and whole-map statistics. In Dinamica EGO these are separate functors connected in the model, and whole-map statistics reach an expression through [Extract Map Attributes](functors/Extract-Map-Attributes.html).
- **Multidimensional data**: band stacks and time series as 3-D or 4-D arrays with xarray, reduced along any dimension.
- **The Python ecosystem**: machine-learning models from scikit-learn or PyTorch applied cell by cell, and statistics from SciPy and statsmodels.

## What Calculate Map provides that Python leaves to the programmer

- **Null semantics** applied consistently to every operator, conditional, table lookup and neighbourhood, with `?` for error recovery.
- **Short-circuit conditionals** that skip work and never evaluate an invalid branch.
- **Mirrored edges and null-skipping windows** in every neighbourhood function, without choosing modes or building masks.
- **Neighbourhoods, tables and random numbers composed in one expression**, where each can depend on the others cell by cell.
- **Alignment of inputs** with different extents and resolutions.
- **Scaling**: tiled, parallel evaluation, native compilation, and skipping the null cells of sparse maps when the expression allows it (see [Null-strict maps](Calculate-Functors.html#null-strict-maps)). The Python equivalent requires Dask or windowed I/O, with overlapping chunks for neighbourhoods.

## Side-by-side examples

The examples below show the calculation only. In the EGO Script statements, the input maps and tables are variables bound earlier in the script, for example with [Load Map](functors/Load-Map.html), and the arguments after the expression are, in order, the Cell Type, the Null Value, the Result Sparsity and the Result Format of [Calculate Map](functors/Calculate-Map.html). In the Python code, the inputs are masked arrays read with rasterio, as in [Reading inputs](#reading-inputs), and the cell type and null value are applied when the result is written, as in [Output](#output).

### Masked index

```
ndvi := # [ if #cloud == 0 then (#nir - #red) / (#nir + #red) else null ] .float32 .default .auto .none;
```

```python
ndvi = np.ma.where(cloud == 0, (nir - red) / (nir + red), np.ma.masked)
```

### Focal statistic where a condition holds

```
tpi := # [ if #landuse == 3 then #dem - nbAverage(#dem, 5, 5) else null ] .float32 .default .auto .none;
```

```python
valid = ~np.ma.getmaskarray(dem)
k = np.ones((5, 5))
s = ndimage.correlate(np.where(valid, dem.filled(0), 0.0), k, mode="reflect")
n = ndimage.correlate(valid.astype(float), k, mode="reflect")
mean5 = np.ma.masked_where(n == 0, s / np.maximum(n, 1))
tpi = np.ma.where(landuse == 3, dem - mean5, np.ma.masked)
```

### Table-driven, stochastic allocation

```
allocated := ## [
    let _p: (%probability[[#landuse, %zones[<= #elevation]]]) ? 0 in
    if rand < _p then 1 else 0
] .uint8 255 .auto .none;
```

```python
# zones: sorted breakpoints zone_keys -> zone_ids; probability: DataFrame indexed by (landuse, zone)
i = np.searchsorted(zone_keys, elevation.filled(np.nan), side="right") - 1
zone = np.where(i >= 0, zone_ids[np.maximum(i, 0)], -1)
idx = probability.index.get_indexer(list(zip(landuse.filled(-1).ravel(), zone.ravel())))
p = np.where(idx >= 0, probability["p"].to_numpy()[np.maximum(idx, 0)], 0.0).reshape(landuse.shape)
alloc = (rng.random(landuse.shape) < p).astype("uint8")
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

With `prange`, the program asserts that the iterations of the loop are independent. In `reduce_3x3` this holds because each iteration writes only `out[r, c]`. A loop that writes to cells computed by other iterations, or accumulates into a shared array, produces wrong results without any error. In Dinamica EGO this guarantee comes from the expression language itself.

## Using Python from a Dinamica EGO model

[Calculate Python Expression](functors/Calculate-Python-Expression.html) runs Python inside a model, but it accepts only tables, values and strings: a model that connects a [Number Map](functors/Number-Map.html) to it fails to load. To combine Python map algebra with a model, save the maps to files, process them in Python and load the results back, or move the calculation into Calculate Map.

## See also

- [Map Algebra Compared with GDAL](Map-Algebra-Compared-With-GDAL.html)
- [Calculate Functors — Complete Operator Documentation](Calculate-Functors.html)
- [Calculate Map](functors/Calculate-Map.html)
- [Calculate Python Expression](functors/Calculate-Python-Expression.html)
- [Image Virtualization](Image-Virtualization.html)
- [NumPy masked arrays](https://numpy.org/doc/stable/reference/maskedarray.html), [scipy.ndimage](https://docs.scipy.org/doc/scipy/reference/ndimage.html), [rasterio](https://rasterio.readthedocs.io/) and [Numba](https://numba.readthedocs.io/)

{% endraw %}
