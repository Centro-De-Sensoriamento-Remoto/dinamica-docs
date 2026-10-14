---
title: "Find Nearest 2D Points From Spatial Index"
nav_exclude: true
---
{% raw %}
# Find Nearest 2D Points From Spatial Index

## Description

This functor retrieves the points nearest to a set of specified points, using a 2D coordinate spatial index.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Spatial Index | Spatial Index 2D Point Type | 2D coordinate spatial index created from a table of point properties. |
| Points | [Base Table Type](Base-Table-Type.html) | Table or lookup table of point ids for which the nearest points are retrieved. The table's keys are the point ids; data columns are ignored. A point not found in Spatial Index is ignored. |
| Number Of Nearest Points | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Maximum number of points retrieved for each specified point id. 0 retrieves every point within the distance threshold set by Maximum Distance. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Minimum Distance | [Real Value Type](Real-Value-Type.html) | Minimum distance threshold for the points retrieved, in the same unit as the point coordinates. Negative values are treated as zero. | 0 |
| Maximum Distance | [Real Value Type](Real-Value-Type.html) | Maximum distance threshold for the points retrieved, in the same unit as the point coordinates. Negative values, or zero, are treated as the maximum possible distance. | 0 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Nearest Points | [Table Type](Table-Type.html) | Table of the nearest points retrieved for each specified point, in the format "Point_Id\*:real, Nearest_Id\*:real, Nearest_Distance:real, Nearest_Index:real". |
| All Nearest Points | [Table Type](Table-Type.html) | Nearest points retrieved for each specified point, as a flat listing, in the format "Row_Index\*:real, Point_Id:real, Nearest_Id:real, Nearest_Distance:real, Nearest_Index:real". |

## Group

[Spatial Index: 2D Points](Functor-List.html#spatial-index-2d-points)

## Notes

The spatial index represents the spatial organization of the points in the 2D plane, letting this functor query the relative position of points.

## Internal Name

FindNearest2DPointsFromSpatialIndex
{% endraw %}
