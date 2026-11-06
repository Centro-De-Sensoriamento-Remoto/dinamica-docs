---
title: "Release Notes 8.15.0"
nav_exclude: true
---
{% raw %}
# Dinamica EGO 8.15.0

> **Development version.** Dinamica EGO 8.15.0 is currently under development. This list may change before release.

Changes compared to version [8.14.0](Release-Notes-8-14-0.html).

## 1. Image expressions

- **Local variables** - `let _a: EXPR, _b: EXPR in EXPR` declares local variables in image expressions. Each binding is evaluated once and can use the previous ones. See [Local Variables](Calculate-Functors.html#local-variables-let--in).
- **Neighborhood reduce** - `nbReduce(iX, INIT, REDUCE, h, w)` combines the cells of a window into a single value. The accumulator `_acc` starts with `INIT`, and `REDUCE` combines it with each cell of the window, available through `_elem`, `_eline`, `_ecolumn` and `_eindex`. It is available in Calculate Map, Calculate Categorical Map and Calculate Multiple Maps. See [Neighborhood Reduce Operator](Calculate-Functors.html#10-neighborhood-reduce-operator).
- **Null-preserving position access** - the new expression `iX[[line, col]]` returns the value of an image at the given position, like `iX[line, col]`, but returns null instead of 0 when the cell is null. See [Image Operators and Functions](Calculate-Functors.html).
- Fixed the GPU implementation of `iX[line, col]`, which returned null instead of 0 for a null cell. It now behaves like the CPU implementation.
- Fixed expressions that combine `iX[line, col]` with elements not supported on accelerator devices, such as `nbMinRef(...) + i1[line, column]`. Depending on the order of the elements, these expressions were marked as compatible with accelerator devices and sent to them. They now run on the processors.
- Fixed the neighborhood functions in image expressions compiled to native code, which read the cells of the window as 32-bit real numbers. In maps of 64-bit real numbers, the values of the window lost precision.

---

## 2. Calculate Multiple Maps

- New functor [Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html), shorthand `#*`, which evaluates a struct expression and returns one map for each field in a [Struct](types/Struct-Type.html).
- New functor [Extract Struct Map](functors/Extract-Struct-Map.html), which retrieves a map from a Struct by name.

---

## 3. Performance

- **Skipping cells with null results** - Calculate Map, Calculate Categorical Map and Calculate Multiple Maps no longer evaluate the expression in cells where a null input map guarantees a null result. This is the case of expressions such as `i1 * 2 + i2` or `if isNull(i1) then null else i2`, where a null cell in `i1` always makes the result null. The cell is written as null without evaluating the expression or reading the other maps. In Calculate Multiple Maps, the cell is skipped only when the null input makes every field of the struct null. Results are unchanged. The input maps used this way are listed in the debug log, under the `FUNCTOR_EXECUTION` subsystem. The calculation on accelerator devices does not use this optimization.
- **Calculating only the non-null cells of a sparse map** - when a sparse input map of Calculate Map, Calculate Categorical Map or Calculate Multiple Maps guarantees a null result wherever its cells are null, the expression is evaluated only at the non-null cells of that map, and every other cell of the result is null. If several input maps meet this condition, the one with the fewest non-null cells is used. The optimization applies when less than 1% of the cells of the map are non-null or when the map has less than 5000 cells. It also applies to sparse maps that are virtualized to match the format of the other input maps. In this case, the calculation runs on the processors and without parallelism. Results are unchanged. The map used is listed in the debug log, under the `FUNCTOR_EXECUTION` subsystem.
- **Filling sparse maps with null** - filling a sparse map with its null value no longer visits every cell of the map. Results of Calculate Map, Calculate Categorical Map and Calculate Multiple Maps created as sparse maps benefit from it when the optimization above is used.
- **GeoTIFF compression** - compressed GeoTIFF (`.tif`) maps are now saved with DEFLATE instead of LZW, and the compression uses up to 4 threads.

---

## 4. Interface

- Removed the Twitter entry from the Help menu.
{% endraw %}
