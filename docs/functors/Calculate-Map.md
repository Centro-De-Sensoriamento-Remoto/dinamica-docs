---
title: "Calculate Map"
nav_order: 20
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calculate Map

## Description

Computes a new continuous raster map by evaluating an algebraic or logical expression independently for every cell of the output map. The expression result is always computed as a real (floating-point) value and then converted to the output map's chosen Cell Type. Use this functor when the expression produces continuous or measured values; use [Calculate Categorical Map](Calculate-Categorical-Map.html) instead when the expression produces integer class codes that downstream functors should treat as categories.

This is one of Dinamica EGO's five calculator functors. Its abbreviated (shorthand) syntax is `#`. See [Calculator functor shorthand](../EGO-Script.html#calculator-functor-shorthand) in the EGO Script documentation for the verbose and abbreviated forms, and [Calculate Functors — Complete Operator Documentation](../Calculate-Functors.html) for the full expression language reference.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Expression | [Image Expression Type](../types/Image-Expression-Type.html) | Algebraic or logical formula used to compute each output cell. Must be enclosed in square brackets `[ ]` in EGO Script. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Data type for each output cell. | Signed 32 Bit Integer |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Sentinel value representing "no data" in the output. | .default |
| Result Is Sparse | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, only non-null cells are stored, saving memory at the expense of random-access speed. This is an advanced port. | No |
| Result Format | [Map Type](../types/Map-Type.html) | Reference map whose spatial format (extent, resolution, projection) is applied to the output; its category information, if any, is ignored. Prefer this port over a Number Map hook when a map is needed only for format purposes, since a hook defines an identifier in the expression namespace and blocks abbreviated syntax if that identifier goes unused in the expression. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Map Type](../types/Map-Type.html) | Computed output map. Its dimensions come from the connected input maps, or from Result Format when given. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

### Connecting data inputs

All maps, tables, and scalar values referenced in the expression must be connected to the functor's ports before writing the expression, using hook functors:

- Maps → [Number Map](Number-Map.html) → referenced in the expression as `i1`, `i2`, …, `i100`
- Tables and lookup tables → [Number Table](Number-Table.html) → referenced as `t1`, `t2`, …, `t100`
- Scalar values → [Number Value](Number-Value.html) → referenced as `v1`, `v2`, …, `v100`

In the abbreviated syntax, operands are referenced directly by the variable name they are bound to, prefixed with `#` for maps, `%` for tables, and `$` for values — eliminating the hook block entirely.

### Spatial context and image virtualization

The expression is evaluated independently once per cell across the output map. Two spatial keywords are available inside the expression:

- line — the row index of the current cell, starting at 1
- column — the column index of the current cell, starting at 1

When the expression references more than one map, all of them are evaluated at the same current cell — `i1` and `i2` always refer to the same spatial location. Connected maps do not need matching extent, resolution, or pixel dimensions: Dinamica EGO reconciles this automatically through image virtualization, transparently wrapping each input in a virtual version sharing a common extent and the highest resolution among the inputs. The one requirement that virtualization does not relax is projection — all connected maps must share the same projection.

The `iX[LINE, COL]` form samples a map at an explicit coordinate rather than the current cell. Coordinates outside the image boundary are mirrored back into range. For a row coordinate cellLine in an image of N rows, cellLine is normally expected to be in the range \[1, N\]. When cellLine is outside this range, it is mirrored back: if cellLine ≤ 0, the effective row is `1 − cellLine` (for instance, cellLine = 0 → row 1, cellLine = −1 → row 2, cellLine = −2 → row 3); if cellLine > N, the effective row is `2N + 1 − cellLine` (for instance, cellLine = N+1 → row N, cellLine = N+2 → row N−1, cellLine = N+3 → row N−2). The same formula applies independently to the column coordinate cellCol. If the target cell is null, the result is 0 rather than null.

### Available expression features

All expression language features are available — there are no restrictions. For the full operator reference, see [The Expression Language](../Calculate-Functors.html#the-expression-language) in the Calculate Functors documentation, or the [Image Expression Type](../types/Image-Expression-Type.html) page for the GUI editor and a navigable operator index.

### Null value handling

Null propagation, the two map-calculator exceptions (`iX[LINE, COL]` returning 0 and neighbourhood functions excluding nulls), and defensive patterns are covered in [Null Value Handling](../Calculate-Functors.html#null-value-handling) in the Calculate Functors documentation. If the computed result exceeds the range of the chosen Cell Type, that cell is also written as null rather than wrapping or clipping.

### Performance

Expression calculations can be compiled to native code automatically (requires the optional native expression support package), delivering near-C performance without any change to the model.

## Internal Name

CalculateMap

## Usage examples

- [CalculateMap practical examples](../Calculate-Functors.html) in the Calculate Functors documentation
- [Lesson 5: Implementing simple map algebra on Dinamica EGO](../guidebook/Simple-Map-Algebra.html) in the Guidebook
{% endraw %}
