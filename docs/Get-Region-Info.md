---
title: "Get Region Info"
nav_exclude: true
---
{% raw %}
# Get Region Info

## Description

Returns the mask, dimensions, projection, and boundary coordinates of a single region held by a region manager.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Region Id | [Integer Value Type](Integer-Value-Type.html) | Identifier of the region to describe. When this functor is placed inside a [For Each Region](For-Each-Region.html) or [Region](Region.html) container, this port connects to the current region automatically. | Provided automatically |
| Region Manager | [Region Manager Type](Region-Manager-Type.html) | The region manager to read. When this functor is placed inside a [Region Manager](Region-Manager.html), [Region](Region.html), or [For Each Region](For-Each-Region.html) container, this port connects to that container's region manager automatically. | Provided automatically |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Region Mask | [Categorical Map Type](Categorical-Map-Type.html) | Map representing the region's mask and geographic extent. |
| Region Lines | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Total number of lines of the region's map. |
| Region Columns | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Total number of columns of the region's map. |
| Region Projection | [Projection Type](Projection-Type.html) | Coordinate reference system of the original map the region was extracted from. |
| Region Top Y Coordinate | [Real Value Type](Real-Value-Type.html) | Y coordinate of the region's top boundary. |
| Region Left X Coordinate | [Real Value Type](Real-Value-Type.html) | X coordinate of the region's left boundary. |
| Region Bottom Y Coordinate | [Real Value Type](Real-Value-Type.html) | Y coordinate of the region's bottom boundary. |
| Region Right X Coordinate | [Real Value Type](Real-Value-Type.html) | X coordinate of the region's right boundary. |

## Group

[Region](Functor-List.html#region)

## Notes

Region Id can be set to a fixed constant instead of being left to auto-bind, but doing so triggers a warning recommending that it be supplied by an enclosing loop's current iteration instead.

## Internal Name

GetRegionInfo
{% endraw %}
