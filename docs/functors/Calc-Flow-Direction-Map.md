---
title: "Calc Flow Direction Map"
nav_order: 10
parent: "Map Algebra Functors"
grand_parent: "Functor List"
redirect_from:
  - /Calc-Flow-Direction-Map.html
---
{% raw %}
# Calc Flow Direction Map

## Description

Calculates a flow direction map from an elevation map: for each cell, the direction toward the neighboring cell with the steepest downhill slope, or, when requested, every downhill direction combined into a single value.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Elevation | [Map Type](../types/Map-Type.html) | Elevation map for which the flow is determined. The unit of elevation does not matter. A null cell remains null in the output. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Diagonals Are Longer | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, a diagonal neighbor's center is treated as farther from the evaluated cell's center than an orthogonal neighbor's, attenuating its slope by the square root of two. This is an advanced port. | Yes |
| Return All Directions | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, the output cell holds the bitwise combination of every direction with a downhill slope. If false, it holds only the direction of the steepest downhill slope. This is an advanced port. | No |
| Use Lottery | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, and two or more neighbors are tied for the steepest downhill slope, one is chosen at random. If false, the first one evaluated is chosen. Only meaningful when Return All Directions is false. This is an advanced port. | No |
| Flow Also In Flat Areas | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, a cell whose neighbors are all at the same elevation (so it would otherwise get no flow direction) is assigned the direction of a same-elevation neighbor that does have a flow direction. This is an advanced port. | Yes |
| Flow Direction Is Sparse | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, the flow direction map is stored as a sparse raster, which stores only non-null cells, trading faster access for lower memory use. This is an advanced port. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Flow Directions | [Map Type](../types/Map-Type.html) | Map where each non-null cell holds the direction of its steepest downhill neighbor, or the combined bitmask of every downhill direction when Return All Directions is true. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

Directions are encoded using the following mask, read clockwise starting from the neighbor directly to the right of the evaluated cell (X): 32, 64, and 128 for the neighbors above; 16 and 1 for the neighbors to the left and right; 8, 4, and 2 for the neighbors below. Several directions can be packed into a single value by summing them, which is what Return All Directions does.

See [Calc Cumulative Flow Map](Calc-Cumulative-Flow-Map.html), which consumes this functor's output.

## Internal Name

CalcFlowDirectionMap
{% endraw %}
