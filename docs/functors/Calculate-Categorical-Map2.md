---
title: "Calculate Categorical Map2"
nav_order: 19
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calculate Categorical Map2

## Description

**This functor is deprecated and should not be used.** Use [Calculate Categorical Map](Calculate-Categorical-Map.html) instead.

It computes a categorical raster map by evaluating an algebraic or logical expression independently for every cell of the output map, in the same way as [Calculate Categorical Map](Calculate-Categorical-Map.html). The only difference is how the data used in the expression is connected: through hooks that identify it by name, instead of by number.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Expression | [Image Expression Type](../types/Image-Expression-Type.html) | Algebraic or logical formula used to compute each output cell's category code. Must be enclosed in square brackets `[ ]` in EGO Script. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Data type for each output cell. | Signed 32 Bit Integer |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Sentinel value representing "no data" in the output. | .default |
| Result Is Sparse | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, only non-null cells are stored, saving memory at the expense of random-access speed. This is an advanced port. | No |
| Result Format | [Map Type](../types/Map-Type.html) | Reference map whose spatial format (extent, resolution, projection) is applied to the output; its category information, if any, is ignored. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Categorical Map Type](../types/Categorical-Map-Type.html) | Computed categorical output map. Its dimensions come from the connected input maps, or from Result Format when given. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

The data used in the expression is connected through [Name Map](Name-Map.html), [Name Table](Name-Table.html) and [Name Value](Name-Value.html) hooks placed inside this container. Each hook gives its data a name, and the expression refers to the data by that name, with the same prefixes used by the [calculator shorthand](../EGO-Script.html#calculator-functor-shorthand): a map registered as `distance` is referenced as `#distance`, a table or lookup table registered as `rates` as `%rates`, and a value registered as `threshold` as `$threshold`. The functors that replace this one use [Number Map](Number-Map.html), [Number Table](Number-Table.html) and [Number Value](Number-Value.html) hooks instead, which identify the data by number (`i1`, `t1`, `v1`, …).

At least one map must be connected through a Name Map hook, unless Result Format is connected, since the format of the output map is taken from them.

See [Calculate Categorical Map](Calculate-Categorical-Map.html) for image virtualization, null-value handling and the expression features, which apply equally to this functor.

This functor is kept only so that older models that use it continue to load and run.

## Internal Name

CalculateCategoricalMap2
{% endraw %}
