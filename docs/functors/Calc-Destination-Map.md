---
title: "Calc Destination Map"
nav_order: 6
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calc Destination Map

## Description

This functor calculates a map of destination cells by selecting suitable cells in an attractiveness map.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Attraction | [Map Type](../types/Map-Type.html) | Map of attractiveness. Attractiveness values less than or equal to zero are ignored. |
| Horizontal Quadrants | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number of horizontal quadrants into which Attraction is divided. |
| Vertical Quadrants | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number of vertical quadrants into which Attraction is divided. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Minimum Distance Between Destinations | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Minimum distance, in meters, between adjacent destinations. | 0 |
| Maximum Attempts Per Destination | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Maximum number of draws attempted for each destination to be chosen, until one is found that does not violate the minimum-distance constraint. This is an advanced port. | 15 |
| Destinations Per Quadrant | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Maximum number of destinations chosen in each quadrant. This is an advanced port. | 1 |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Cell type of the destination map. | Unsigned 8 Bit Integer |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Null value of the destination map. | .default |
| Destination Is Sparse | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, the destination map is stored as a sparse raster. This is an advanced port. | Yes |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Destination | [Map Type](../types/Map-Type.html) | Map of the cells chosen as destinations. Destination has the same dimensions as Attraction, and cells chosen as destinations carry their attractiveness value. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

This functor is outdated; prefer Select Random Points, Select Random Point Cluster, [Patcher](Patcher.html), or [Expander](Expander.html) instead.

For each quadrant into which Attraction is divided, as many destination cells are drawn as specified by Destinations Per Quadrant. A quadrant may draw fewer than that, or none at all, when it has no valid (non-null, greater-than-zero) attractiveness cells left, or when its remaining candidate cells all lie closer than Minimum Distance Between Destinations to a destination already drawn.

Attractiveness is used as a selection probability for each cell: the higher the attractiveness, the greater the chance that the corresponding cell is selected.

Attraction cannot have real-numbered values.

## Internal Name

CalcDestinationMap
{% endraw %}
