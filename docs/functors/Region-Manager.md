---
title: "Region Manager"
nav_order: 6
parent: "Region Functors"
grand_parent: "Functor List"
redirect_from:
  - /Region-Manager.html
---
{% raw %}
# Region Manager

## Description

This container builds a region manager from a categorical map whose classes identify regions, and makes it available to the functors nested inside it. The region manager splits a global map into the map of each region, and merges regional maps back together into a global map, so each region can be processed independently. Unlike [For Each Region](For-Each-Region.html), this container does not iterate over the regions — it runs its contents once, with the region manager available to whichever region-aware functors are nested inside, directly or through a [Region](Region.html).

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Regions | [Categorical Map Type](../types/Categorical-Map-Type.html) | Map of subregions, such as countries, states, or counties. The cells that make up a region do not need to be contiguous. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Border Cells | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Number of lines and columns added as an extra border around each region in its regional maps. | 0 |

## Outputs

None.

## Internal Outputs

| Name | Type | Description |
| --- | --- | --- |
| Region Manager | [Region Manager Type](../types/Region-Manager-Type.html) | The region manager holding the regions. |

## Group

[Region](../Functor-List.html#region)

## Notes

When Border Cells is greater than zero, the bounds of each region are increased by "2 \* Border Cells" lines and columns.

Every [Merge Regional Maps](Merge-Regional-Maps.html) or [Merge Regional Categorical Maps](Merge-Regional-Categorical-Maps.html) that reads from this container's region manager must have a matching [Regional Map](Regional-Map.html) or [Regional Categorical Map](Regional-Categorical-Map.html) registering a map under the same name in that same region manager — otherwise the model reports an error. The reverse also holds: a [Regional Map](Regional-Map.html) or [Regional Categorical Map](Regional-Categorical-Map.html) with no matching merge functor is reported with a warning, since it registers a map that nothing reads back. Registering two maps under the same name for the same region manager is likewise reported with a warning.

See Lesson 14, "Using For Each Category and Region Manager," for a worked example of this container.

## Internal Name

RegionManager

## Usage examples

See practical examples of this functor in Lesson 14: Using For Each Category and Region Manager
{% endraw %}
