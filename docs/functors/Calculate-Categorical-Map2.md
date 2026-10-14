---
title: "Calculate Categorical Map2"
nav_order: 19
parent: "Map Algebra Functors"
grand_parent: "Functor List"
redirect_from:
  - /Calculate-Categorical-Map2.html
---
{% raw %}
# Calculate Categorical Map2

## Description

**This functor is deprecated.** It computes a new categorical raster map by evaluating an algebraic or logical expression independently for every cell of the output map, in exactly the same way as [Calculate Categorical Map](Calculate-Categorical-Map.html). It is kept only so that older models built with it continue to load and run; new models should use [Calculate Categorical Map](Calculate-Categorical-Map.html) instead.

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

Behaves identically to [Calculate Categorical Map](Calculate-Categorical-Map.html) in every respect except its internal name; see that functor's Notes for the hook mechanism, image virtualization, and null-value handling that both share.

This functor is obsolete and is retained only for backward compatibility with existing models.

## Internal Name

CalculateCategoricalMap2
{% endraw %}
