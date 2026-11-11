---
title: "Map Algebra Compared with GDAL"
nav_order: 5
parent: "Language and Expressions"
---
{% raw %}
# Map Algebra Compared with GDAL

> **Draft.** This page compares the map calculators of Dinamica EGO 8.15.0 with `gdal raster calc` from GDAL 3.12. Both tools are under active development; check the release notes of each before relying on a specific detail.

## Overview

Both [Calculate Map](functors/Calculate-Map.html) and `gdal raster calc` evaluate an expression once for each cell of an output raster. The difference lies in what the expression can see while it runs:

- **`gdal raster calc`** sees the value of each input band **at the current pixel**, the pixel's georeferenced coordinates and a few constants. Anything that needs other pixels, tables or random numbers must be computed by another program or pipeline step before or after the calculation.
- **Calculate Map** sees the current cell of each input map, but it can also read **any other cell**, aggregate **windows** of cells, query **lookup tables and multi-column tables**, draw **random numbers**, bind **local variables** and catch **algebraic errors**, all inside a single expression.

As a result, every calculation that `gdal raster calc` can express has a Calculate Map equivalent, with one minor exception (georeferenced coordinates, which Dinamica EGO can derive; see [Coordinates](#coordinates)). The reverse is not true: neighbourhood, table, random-access and stochastic expressions have no equivalent inside a GDAL expression.

This page compares **expressive power**, meaning what a single expression can compute. It does not rank the two tools as products. GDAL is a data-processing library with a very broad set of formats and utilities, and Dinamica EGO reads and writes maps through GDAL.

## At a glance

| Capability | Dinamica EGO 8.15.0 (Calculate Map) | GDAL 3.12 (`gdal raster calc`) |
| --- | --- | --- |
| Arithmetic, comparison and logical operators | Yes | Yes |
| Conditionals | `if ... then ... else` | `cond ? a : b` |
| Mathematical functions | Trigonometric, exp, logarithms, rounding, `clamp`, `clampMod`, `signal` | Trigonometric and hyperbolic, exp, logarithms, rounding, `sign` |
| Local variables | `let ... in` | No |
| Several results from one evaluation | Struct expression in [Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html), with shared `let` variables | Several `--calc` expressions, each evaluated independently |
| Multiband input | Layers are extracted and connected as separate maps | Native, with automatic band broadcasting |
| Value at another cell | `iX[line, col]`, `iX[[line, col]]` | No |
| Neighbourhood statistics | `nbMin`, `nbMax`, `nbSum`, `nbProd`, `nbCount`, `nbAverage`, `nbMedian`, `nbMode`, `nbVar`, `nbStdDev` | No (separate `gdal raster neighbors` step) |
| Arg-min / arg-max of a window | `nbMinRef`, `nbMaxRef` | No |
| Convolution | `nbConvol` with any rectangular kernel from a lookup table | No (separate `gdal raster neighbors` step, odd square kernels) |
| User-defined window aggregation | `nbReduce` | No |
| Lookup tables | Exact, bounds, closest key, linear interpolation, key-exists test | No (separate `gdal raster reclassify` step) |
| Multi-column tables | Multi-key join, named or indexed column | No |
| Random numbers | `rand`, `rUniform`, `rNormal`, `rPoisson` | No |
| Grid position | `line`, `column` | No |
| Georeferenced position | Derived from map attributes | `_CENTER_X_`, `_CENTER_Y_` |
| Missing data | Abstract `null`, `isNull`, `null(iX)` | `NODATA` sentinel variable, NaN, `--propagate-nodata` |
| Error recovery | `EXPR ? FALLBACK` | No |
| Halt on an invalid state | `abort` | No |
| Inputs with different extent or resolution | Reconciled automatically by [image virtualization](Image-Virtualization.html) | Different resolutions accepted; inputs should cover the same extent |
| Parallel evaluation | Automatic, on all workers, and on accelerator devices when enabled | Not documented for the expression; compression and warping have their own thread options |

## Execution model

The two tools agree on the basic model: one expression, evaluated per cell, in double precision, converted to the output cell type at the end. They differ in how inputs are bound and aligned.

| Aspect | Dinamica EGO | GDAL |
| --- | --- | --- |
| Binding inputs | Maps, tables and values are connected to the functor and referred to as `iX`, `tX` and `vX` (X from 1 to 100), or by name with the `#`, `%` and `$` prefixes in the [abbreviated syntax](EGO-Script.html#calculator-functor-shorthand) | Each input is given a name (`-i A=file.tif`) and referred to as `A` or `A[band]` |
| Kinds of input | Maps, lookup tables, multi-column tables and scalar values | Rasters only |
| Alignment | Image virtualization builds a common extent at the highest resolution among the inputs. Only the projection must match. | Inputs must share the CRS (unless `--no-check-crs`) and should cover the same extent; resolutions may differ |
| Output | One map per functor, or several maps from [Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html) | One dataset, with one band per expression |
| Out-of-range results | The cell becomes null | Clamped to the range of the output data type by GDAL's standard conversion |

## What only Dinamica EGO can express

### Values at other cells

`iX[LINE, COL]` reads map X at a computed coordinate. Coordinates outside the map are mirrored back into range, and a null target reads as 0. `iX[[LINE, COL]]` does the same but keeps the null. Because the coordinates are ordinary expressions, the cell read can depend on other maps or tables:

```
// Elevation at the cell pointed to by the row and column offsets of a flow direction
downstream := # [ #elevation[[line + #rowOffset, column + #columnOffset]] ] .float32 .default .auto .none;
```

A GDAL expression can only read the current pixel of each input.

### Neighbourhoods inside the expression

The `nbN` functions aggregate a rectangular window. Because they are ordinary expressions, they can be combined with conditionals, tables and other windows in the same calculation, and the window can be anchored anywhere, not just at the current cell:

```
// Local relief, only where the cell is forest (class 3) and the 5x5 window is mostly valid
relief := # [
    if #landuse == 3 and nbCount(#dem, 5, 5) >= 20
    then nbMax(#dem, 5, 5) - nbMin(#dem, 5, 5)
    else null
] .float32 .default .auto .none;
```

`nbMinRef` and `nbMaxRef` return the position of the window minimum or maximum, mapped to a lookup table or to a second map. `nbConvol` applies any rectangular kernel stored in a lookup table.

GDAL 3.12 can compute fixed neighbourhood statistics with `gdal raster neighbors`, as a separate step that writes a new raster. That step applies one method to one square, odd-sized window centred on each pixel. The result can then be used as an input to `gdal raster calc`, but the window cannot depend on the expression, cannot be anchored elsewhere and cannot be evaluated only where a condition holds.

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

GDAL has no equivalent.

### Tables in the expression

Lookup tables give per-cell joins with exact, bound, closest-key and interpolated lookups. Multi-column tables join on several keys at once:

```
// Transition probability keyed by land-use class and elevation zone, weighted by a factor interpolated by slope
probability := # [
    %transitions[[#landuse, %zones[<= #elevation]]] * %slopeFactor[/ #slope]
] .float32 .default .auto .none;
```

GDAL can reclassify a raster with `gdal raster reclassify` as a separate step, but it cannot query a table from inside an expression or key a lookup on a computed value.

### Random numbers

`rand`, `rUniform`, `rNormal` and `rPoisson` draw one sample per cell. This allows stochastic allocation and Monte Carlo perturbation in a single calculation:

```
allocated := ## [ if rand < %probabilityByClass[#landuse] then 1 else 0 ] .uint8 .default .auto .none;
```

GDAL expressions have no random functions.

### Local variables and shared results

`let ... in` evaluates a sub-expression once per cell and names it. In Calculate Multiple Maps, the variables are shared by every output:

```
indices := #* [
    let _ndvi: (#nir - #red) / (#nir + #red) in
    { ndvi: _ndvi, vigorous: if _ndvi > 0.6 then 1 else 0 }
] .float32 .default .auto .none;
```

In GDAL, a repeated sub-expression must be written out again, and several `--calc` expressions do not share intermediate results.

### Null and error handling

In Dinamica EGO, `null` is an abstract value that propagates through any arithmetic, `isNull` tests it, and `EXPR ? FALLBACK` replaces any algebraic error (division by zero, missing table key, null operand) with another expression. `abort` halts the model when the expression reaches an invalid state. See [Null Value Handling](Calculate-Functors.html#null-value-handling).

In GDAL, a NoData input either makes the whole output pixel NoData (`--propagate-nodata`) or enters the expression as its numeric sentinel, which the expression can compare against the `NODATA` variable. There is no error-recovery operator, so a division by zero must be prevented with a conditional before it happens.

## What GDAL expresses more concisely

### Multiband rasters

GDAL broadcasts an expression over bands: with three-band inputs `A` and `B`, `--calc "A + B"` produces three output bands, and `sum(A)` or `avg(A)` aggregate the bands of one input.

Dinamica EGO computes the same results once the layers are extracted and connected as separate maps:

| GDAL | Dinamica EGO |
| --- | --- |
| `--calc "A + B"` on three-band inputs | Calculate Multiple Maps with `{ b1: i1 + i4, b2: i2 + i5, b3: i3 + i6 }` |
| `--flatten --calc "avg(A)"` | `(i1 + i2 + i3) / 3` |

This is a difference in notation, not in what can be computed. The Dinamica EGO form grows with the number of bands, and each calculator accepts at most 100 maps.

### Coordinates

`_CENTER_X_` and `_CENTER_Y_` give the georeferenced coordinates of the pixel centre, in the CRS of the dataset. Dinamica EGO exposes the grid position (`line`, `column`) instead. The georeferenced position can be derived by connecting the output of [Extract Map Attributes](functors/Extract-Map-Attributes.html) as a table and combining `line` and `column` with the registration coordinate, registration cell and original cell size attributes.
<!-- TODO: confirm the registration convention (corner or centre, line direction) and add the exact formula. -->

### Hyperbolic functions

muparser provides `sinh`, `cosh`, `tanh` and their inverses. Dinamica EGO builds them from `exp` and `ln`, for example `(exp(i1) - exp(-i1)) / 2` for `sinh`.

## Composing calculations

GDAL makes up for the narrower expression language by composing steps. A nested pipeline computes a derived raster on the fly and passes it to `gdal raster calc` as an input:

```bash
gdal raster calc \
  -i "SLOPE=[ read dem.tif ! slope ]" \
  -i "ASPECT=[ read dem.tif ! aspect ]" \
  --calc "(SLOPE >= 2) ? ASPECT : -9999" --nodata -9999 \
  -o result.tif
```

Steps can also be written as GDALG files, so they are evaluated lazily when the result is read.

Dinamica EGO composes calculations through the model graph. Calculators, other functors, submodels and containers such as Repeat and For Each connect through ports, and the graph also provides iteration and control flow that neither expression language has. Both tools therefore reach multi-step results. The difference is that Dinamica EGO can put neighbourhood, table and random operations **inside** one expression, where they can depend on each other cell by cell.

## Side-by-side examples

Each example below is complete: the GDAL commands and the EGO scripts read the same input files and write the same result. In the scripts, the arguments after the expression are, in order, the Cell Type, the Null Value, the Result Sparsity and the Result Format of [Calculate Map](functors/Calculate-Map.html); the first two correspond to `--ot` and `--nodata` in `gdal raster calc`.

### Masked index

Same expressive power in both tools.

```bash
gdal raster calc -i "N=nir.tif" -i "R=red.tif" -i "C=cloud.tif" \
  --calc "C == 0 ? (N - R) / (N + R) : -9999" --nodata -9999 --ot Float32 -o ndvi.tif
```

```
Script {{
    nir := LoadMap "nir.tif";
    red := LoadMap "red.tif";
    cloud := LoadMap "cloud.tif";

    ndvi := # [ if #cloud == 0 then (#nir - #red) / (#nir + #red) else null ] .float32 -9999 .auto .none;

    SaveMap ndvi "ndvi.tif";
}};
```

### Focal statistic where a condition holds

Requires two steps in GDAL, and one calculation in Dinamica EGO.

```bash
gdal raster neighbors -i dem.tif --method mean --size 5 -o mean5.tif
gdal raster calc -i "D=dem.tif" -i "M=mean5.tif" -i "L=landuse.tif" \
  --calc "L == 3 ? D - M : -9999" --nodata -9999 --ot Float32 -o tpi.tif
```

```
Script {{
    dem := LoadMap "dem.tif";
    landuse := LoadMap "landuse.tif";

    tpi := # [ if #landuse == 3 then #dem - nbAverage(#dem, 5, 5) else null ] .float32 -9999 .auto .none;

    SaveMap tpi "tpi.tif";
}};
```

### Table-driven, stochastic allocation

No GDAL expression equivalent. `probability.csv` holds the transition probability for each pair of land-use class and elevation zone, with both key columns marked with `*` in its header, and `zones.csv` maps the lower bound of each elevation range to its zone.

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

## Parallel execution

Dinamica EGO parallelizes a map calculation without any change to the expression. The cells of the result are divided into contiguous ranges, one per task, and the tasks run on the workers described in [Parallel Execution](Parallel-Execution.html); the number of tasks follows the [granularity](Parallel-Execution.html#granularity). Each task has its own copy of the local variables. This is safe for every expression because a calculator expression only computes the value of its own cell: it reads the input maps, tables and values, but cannot write to another cell or keep state between cells.

The calculation runs on a single task when the input maps cannot be read in parallel or the result cannot be written in parallel, and when it visits only the non-null cells of a sparse null-strict map (see [Null-strict maps](Calculate-Functors.html#null-strict-maps)). When accelerator devices are enabled, an expression that is complex enough and compatible with them can run on an OpenCL device instead; expressions that use `nbReduce` are not compatible.

The `gdal raster calc` documentation does not describe parallel evaluation of the expression, and the expression should be assumed to run on one thread. GDAL's parallel options apply to other stages of the processing:

| Option | What runs in parallel |
| --- | --- |
| `--co NUM_THREADS=ALL_CPUS` (GeoTIFF) or the `GDAL_NUM_THREADS` configuration option | Compression and decompression of blocks |
| `gdalwarp -multi -wo NUM_THREADS=ALL_CPUS` | Reprojection and resampling |

To evaluate an expression on several processors with GDAL, split the output into windows, run one `gdal raster calc` process per window and assemble the results, for example with `gdalbuildvrt`. Windows used by neighbourhood steps such as `gdal raster neighbors` must overlap by half the window size, and the overlap must be removed when the results are assembled.

## Beyond expressive power

Expressive power is only one criterion. GDAL supports far more formats, runs anywhere GDAL is installed, and evaluates pipelines lazily. Dinamica EGO compiles expressions to native code when the optional native expression support package is installed, skips the null cells of sparse maps when the expression allows it (see [Null-strict maps](Calculate-Functors.html#null-strict-maps)), and integrates the calculation into a model with iteration, calibration and submodels.

## See also

- [Map Algebra Compared with Python](Map-Algebra-Compared-With-Python.html)
- [Calculate Functors — Complete Operator Documentation](Calculate-Functors.html)
- [Calculate Map](functors/Calculate-Map.html)
- [Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html)
- [Image Virtualization](Image-Virtualization.html)
- [gdal raster calc](https://gdal.org/programs/gdal_raster_calc.html), [gdal raster neighbors](https://gdal.org/programs/gdal_raster_neighbors.html) and [gdal raster reclassify](https://gdal.org/programs/gdal_raster_reclassify.html) in the GDAL documentation

{% endraw %}
