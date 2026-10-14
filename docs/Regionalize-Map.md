---
title: "Regionalize Map"
nav_exclude: true
---
{% raw %}
# Regionalize Map

## Description

Crops a map down to a single region, returning the piece of the map that falls inside that region's mask.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Global Map | [Map Type](Map-Type.html) | The map to crop. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Region Id | [Integer Value Type](Integer-Value-Type.html) | Identifier of the region to extract. When this functor is placed inside a [For Each Region](For-Each-Region.html) or [Region](Region.html) container, this port connects to the current region automatically. | Provided automatically |
| Keep Non Region Cells | [Boolean Value Type](Boolean-Value-Type.html) | If true, cells located outside the region's mask — including its extra border — are kept in the result. If false, those cells are filled with null values. | No |
| Region Manager | [Region Manager Type](Region-Manager-Type.html) | The region manager to read. When this functor is placed inside a [Region Manager](Region-Manager.html), [Region](Region.html), or [For Each Region](For-Each-Region.html) container, this port connects to that container's region manager automatically. | Provided automatically |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Regional Map | [Map Type](Map-Type.html) | Map cropped to the specified region. |

## Group

[Region](Functor-List.html#region)

## Notes

Region Id can be set to a fixed constant instead of being left to auto-bind, but doing so triggers a warning recommending that it be supplied by an enclosing loop's current iteration instead.

## Internal Name

RegionalizeMap

## Usage examples

See practical examples of this functor in Lesson 14: Using For Each Category and Region Manager
{% endraw %}
