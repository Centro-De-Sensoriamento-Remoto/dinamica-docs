---
title: "Calc Slope Map"
nav_exclude: true
---
{% raw %}
# Calc Slope Map

## Description

Calculates a slope map from an elevation map. For each cell, the slope is calculated toward every neighboring cell using the elevation difference and the distance between the cells, and the largest of those slopes is assigned to the cell.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Elevation | [Map Type](Map-Type.html) | Elevation map, in meters. May contain null values. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Diagonals Are Longer | [Boolean Value Type](Boolean-Value-Type.html) | If true, the distance to diagonal neighbor cells is multiplied by 1.414213562. This is an advanced port. | Yes |
| Slope In Percent | [Boolean Value Type](Boolean-Value-Type.html) | If true, slope is calculated in percent; otherwise, it is calculated in degrees. | No |
| Cell Type | [Cell Type](Cell-Type.html) | Cell type of the slope map. | Signed 32 Bit Integer |
| Null Value | [Null Value Type](Null-Value-Type.html) | Null value of the slope map. Must be compatible with Cell Type. | .default |
| Slope Is Sparse | [Boolean Value Type](Boolean-Value-Type.html) | If true, the output map is saved as a sparse raster set. This is an advanced port. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Slope | [Map Type](Map-Type.html) | Slope map, with the same dimensions as Elevation. |

## Group

[Map Algebra](Functor-List.html#map-algebra)

## Notes

Raises an error if Null Value is not compatible with Cell Type.

## Internal Name

CalcSlopeMap
{% endraw %}
