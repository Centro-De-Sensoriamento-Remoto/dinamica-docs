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
- **Null-preserving position access** - the new expression `iX[[line, col]]` returns the value of an image at the given position, like `iX[line, col]`, but returns null instead of 0 when the cell is null. See [Image Operators and Functions](Calculate-Functors.html).
- Fixed the GPU implementation of `iX[line, col]`, which returned null instead of 0 for a null cell. It now behaves like the CPU implementation.

---

## 2. Calculate Multiple Maps

- New functor [Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html), shorthand `#*`, which evaluates a struct expression and returns one map for each field in a [Struct](types/Struct-Type.html).
- New functor [Extract Struct Map](functors/Extract-Struct-Map.html), which retrieves a map from a Struct by name.

---

## 3. Interface

- Removed the Twitter entry from the Help menu.
{% endraw %}
