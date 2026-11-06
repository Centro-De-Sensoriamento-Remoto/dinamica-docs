---
title: "Calculate Categorical Map"
nav_order: 18
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calculate Categorical Map

## Description

Computes a new categorical raster map by evaluating an algebraic or logical expression independently for every cell of the output map. Functionally identical to [Calculate Map](Calculate-Map.html) — the same inputs, parameters, and expression language apply — except that its output is typed as a categorical map, preserving category semantics for downstream functors that distinguish categorical maps from continuous ones (e.g. [Calc Areas](Calc-Areas.html), [For Each Category](For-Each-Category.html)). Use this functor when the expression produces integer class codes; use [Calculate Map](Calculate-Map.html) instead for continuous or measured values.

This is one of Dinamica EGO's six calculator functors. Its abbreviated (shorthand) syntax is `##`. See [Calculator functor shorthand](../EGO-Script.html#calculator-functor-shorthand) in the EGO Script documentation for the verbose and abbreviated forms, and [Calculate Functors — Complete Operator Documentation](../Calculate-Functors.html) for the full expression language reference.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Expression | [Image Expression Type](../types/Image-Expression-Type.html) | Algebraic or logical formula used to compute each output cell's category code. Must be enclosed in square brackets `[ ]` in EGO Script. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Data type for each output cell. | Signed 32 Bit Integer |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Sentinel value representing "no data" in the output. | .default |
| Result Is Sparse | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, only non-null cells are stored, saving memory at the expense of random-access speed. This is an advanced port. Version 8.14.1 and earlier; replaced by Result Sparsity. | No |
| Result Sparsity[^8150] | [Enum Type](../types/Enum-Type.html) | Defines how the output map is stored. `.dense` stores all cells. `.sparse` stores only the non-null cells, saving memory at the expense of random-access speed. `.auto` makes the output map sparse when the calculation visits only the non-null cells of a sparse input map, because a null cell in it always makes the result null, and dense otherwise. Models created with earlier versions are converted automatically: `.no` becomes `.dense`, `.yes` becomes `.sparse`, and a model that does not set Result Is Sparse uses `.auto`. This is an advanced port. | .auto |
| Result Format | [Map Type](../types/Map-Type.html) | Reference map whose spatial format (extent, resolution, projection) is applied to the output; its category information, if any, is ignored. Prefer this port over a Number Map hook when a map is needed only for format purposes, since a hook defines an identifier in the expression namespace and blocks abbreviated syntax if that identifier goes unused in the expression. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Categorical Map Type](../types/Categorical-Map-Type.html) | Computed categorical output map. Its dimensions come from the connected input maps, or from Result Format when given. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

All behavior — hook functor wiring, shared-cell evaluation and image virtualization across connected maps, null propagation, and the requirement that at least one map or Result Format be provided — is identical to [Calculate Map](Calculate-Map.html). See that functor's Notes for full details.

See [Calculate Functors — Complete Operator Documentation](../Calculate-Functors.html) for the complete expression language, null-value handling rules, and worked examples.

## Internal Name

CalculateCategoricalMap

[^8150]: Available in Dinamica EGO 8.15.0, currently a development version. Details may change before release.

{% endraw %}
