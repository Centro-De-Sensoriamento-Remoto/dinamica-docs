---
title: "Create Spatial Index For 2D Points"
nav_order: 1
parent: "Spatial Index: 2D Points Functors"
grand_parent: "Functor List"
---
{% raw %}
# Create Spatial Index For 2D Points

## Description

This functor creates a 2D coordinate spatial index from a table of point properties.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Point Properties | [Table Type](../types/Table-Type.html) | Table of point properties mapping each point's id to its 2D coordinates, in the format "Point_Id\*:real, Point_Y:real, Point_X:real". Point_Y and Point_X hold the Y and X components of each point's location; the unit is arbitrary, and any Cartesian coordinate system can be used. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Spatial Index | Spatial Index 2D Point Type | 2D coordinate spatial index created from Point Properties. |

## Group

[Spatial Index: 2D Points](../Functor-List.html#spatial-index-2d-points)

## Notes

The spatial index represents the spatial organization of the points in the 2D plane, letting other functors query the relative position of points.

## Internal Name

CreateSpatialIndexFor2DPoints
{% endraw %}
