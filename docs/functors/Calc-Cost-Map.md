---
title: "Calc Cost Map"
nav_order: 4
parent: "Map Algebra Functors"
grand_parent: "Functor List"
redirect_from:
  - /Calc-Cost-Map.html
---
{% raw %}
# Calc Cost Map

## Description

This functor calculates an accumulated cost surface from source features, using a friction map.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Sources | [Map Type](../types/Map-Type.html) | Map whose non-null cells correspond to source features. If Sources does not define a null value, this functor reports an error. |
| Frictions | [Map Type](../types/Map-Type.html) | Map expressing the difficulty of crossing each cell. The difficulty is proportional to the cell value; for a cell to be treated as impassable it must have a value much greater than the others. Null-value cells in Frictions produce null-value cells in the cost map. Negative or zero friction values that do not correspond to Frictions' null value are not allowed, and reported as an error during execution. |
| Also Calculate Cost Direction Map | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, the cost direction map is also calculated and placed in Directions; otherwise, Directions is left empty. Directions are represented using a Moore neighborhood: None=0, NW=1, N=2, NE=3, E=4, SE=5, S=6, SW=7, and W=8. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Cell type of the cost map. It must be compatible with the values in Sources and Frictions, or this functor reports an error during execution. | Signed 32 Bit Integer |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Null value of the cost map. It cannot be 0, since that value is used to indicate source features on the cost map; using 0 is reported as an error during execution. | .default |
| Diagonals Cost More | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, diagonal movements cost more than orthogonal (horizontal/vertical) movements: a diagonal movement's cost is multiplied by 1.414213562. This is an advanced port. | Yes |
| Maximum Number Of Passes | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Maximum number of passes used to calculate the cost map. 0 means as many passes as needed to obtain the optimal cost map are performed. This is an advanced port. | 0 |
| Frictions Are Relative | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, the friction values are relative to the map resolution and represent units per meter; in this case, they are automatically multiplied by the cell resolution, in meters. This is an advanced port. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Costs | [Map Type](../types/Map-Type.html) | Map of the cost to reach one of the source features from any point. Costs has the same dimensions as Sources. |
| Directions | [Map Type](../types/Map-Type.html) | Map of the direction toward the least-cost neighboring cell from any point. Directions has the same dimensions as Sources, and only has a value when Also Calculate Cost Direction Map is true; otherwise it is left empty. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

The cost-map algorithm is "Push broom," though its spatial performance approximates the so-called "Pushgrow" algorithm, especially when using two or more passes.

Penalizing diagonal movements is effective only when cell dimensions (width and height) are taken into account in the cost calculation, friction values are high, or the cost map uses real-numbered cells.

A Sources or Frictions map with real-numbered cells requires a cost map with real-numbered cells, or this functor may report an error retrieving a friction or source-feature value.

Each "pass" used to calculate the cost map actually corresponds to four passes, one in each of the four cardinal directions.

Parts of the friction map that are unreachable from every source feature are excluded from the cost map, and represented there by the null value. Costs are not accumulated across null-value cells, so a region entirely surrounded by null-value cells will not have its costs calculated unless a source feature lies inside that region.

## Internal Name

CalcCostMap

## Usage examples

See practical examples of this functor in Lesson 17: Building a land-use and land-cover change simulation model
{% endraw %}
