---
title: "Get All Regions Info"
nav_order: 1
parent: "Region Functors"
grand_parent: "Functor List"
---
{% raw %}
# Get All Regions Info

## Description

Returns a table with the boundaries of every region held by a region manager, one row per region.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Region Manager | [Region Manager Type](../types/Region-Manager-Type.html) | The region manager to read. When this functor is placed inside a [Region Manager](Region-Manager.html), [Region](Region.html), or [For Each Region](For-Each-Region.html) container, this port connects to that container's region manager automatically. | Provided automatically |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Regions Info | [Table Type](../types/Table-Type.html) | Table with one row per region, with the columns Region Id (key), Region Lines, Region Columns, Region Top Y Coordinate, Region Left X Coordinate, Region Bottom Y Coordinate, and Region Right X Coordinate — the number of lines and columns of the region's map, and the coordinates of its top, left, bottom, and right boundaries. |

## Group

[Region](../Functor-List.html#region)

## Notes

None.

## Internal Name

GetAllRegionsInfo
{% endraw %}
