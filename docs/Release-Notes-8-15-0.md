---
title: "Release Notes 8.15.0"
nav_exclude: true
---
{% raw %}
# Dinamica EGO 8.15.0

> **Development version.** Dinamica EGO 8.15.0 is currently under development. This list may change before release.

Changes compared to version 8.14.0.

## 1. Image expressions

- **Local variables** - `let _a: EXPR, _b: EXPR in EXPR` declares local variables in image expressions. Each binding is evaluated once and can use the previous ones. See [Local Variables](Calculate-Functors.html#local-variables-let--in).
- **Neighborhood reduce** - `nbReduce(iX, INIT, REDUCE, h, w)` combines the cells of a window into a single value. The accumulator `_acc` starts with `INIT`, and `REDUCE` combines it with each cell of the window, available through `_elem`, `_eline`, `_ecolumn` and `_eindex`. It is available in Calculate Map, Calculate Categorical Map and Calculate Multiple Maps. See [Neighborhood Reduce Operator](Calculate-Functors.html#10-neighborhood-reduce-operator).
- **Null-preserving position access** - the new expression `iX[[line, col]]` returns the value of an image at the given position, like `iX[line, col]`, but returns null instead of 0 when the cell is null. See [Image Operators and Functions](Calculate-Functors.html).
- Fixed the GPU implementation of `iX[line, col]`, which returned null instead of 0 for a null cell. It now behaves like the CPU implementation.
- Fixed expressions that combine `iX[line, col]` with elements not supported on accelerator devices, such as `nbMinRef(...) + i1[line, column]`. Depending on the order of the elements, these expressions were marked as compatible with accelerator devices and sent to them. They now run on the processors.

---

## 2. Calculate Multiple Maps

- New functor [Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html), shorthand `#*`, which evaluates a struct expression and returns one map for each field in a [Struct](types/Struct-Type.html).
- New functor [Extract Struct Map](functors/Extract-Struct-Map.html), which retrieves a map from a Struct by name.

---

## 3. Performance

- **Skipping cells with null results** - Calculate Map, Calculate Categorical Map and Calculate Multiple Maps no longer evaluate the expression in cells where a null input map guarantees a null result. This is the case of expressions such as `i1 * 2 + i2` or `if isNull(i1) then null else i2`, where a null cell in `i1` always makes the result null. The cell is written as null without evaluating the expression or reading the other maps. In Calculate Multiple Maps, the cell is skipped only when the null input makes every field of the struct null. Results are unchanged. The input maps used this way are listed in the debug log, under the `FUNCTOR_EXECUTION` subsystem. The calculation on accelerator devices does not use this optimization.

---

## 4. Interface

- Removed the Twitter entry from the Help menu.
{% endraw %}
