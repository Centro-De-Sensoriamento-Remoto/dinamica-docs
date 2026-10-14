---
title: "Regionalize Categorical Map"
nav_order: 10
parent: "Region Functors"
grand_parent: "Functor List"
redirect_from:
  - /Regionalize-Categorical-Map.html
---
{% raw %}
# Regionalize Categorical Map

## Description

Crops a categorical map down to a single region, returning the piece of the map that falls inside that region's mask.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Global Map | [Categorical Map Type](../types/Categorical-Map-Type.html) | The categorical map to crop. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Region Id | [Integer Value Type](../types/Integer-Value-Type.html) | Identifier of the region to extract. When this functor is placed inside a [For Each Region](For-Each-Region.html) or [Region](Region.html) container, this port connects to the current region automatically. | Provided automatically |
| Keep Non Region Cells | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, cells located outside the region's mask — including its extra border — are kept in the result. If false, those cells are filled with null values. | No |
| Recreate Categories | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, the category legend of the cropped region is rebuilt from the values actually present in it. If false, the cropped map keeps the original map's full category legend, whether or not each category is still present in the cropped region. | No |
| Region Manager | [Region Manager Type](../types/Region-Manager-Type.html) | The region manager to read. When this functor is placed inside a [Region Manager](Region-Manager.html), [Region](Region.html), or [For Each Region](For-Each-Region.html) container, this port connects to that container's region manager automatically. | Provided automatically |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Regional Map | [Categorical Map Type](../types/Categorical-Map-Type.html) | Categorical map cropped to the specified region. This functor preserves the category legend of the input map, subject to Recreate Categories above. |

## Group

[Region](../Functor-List.html#region)

## Notes

Region Id can be set to a fixed constant instead of being left to auto-bind, but doing so triggers a warning recommending that it be supplied by an enclosing loop's current iteration instead.

## Internal Name

RegionalizeCategoricalMap
{% endraw %}
