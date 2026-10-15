---
title: "Region Manager Value"
nav_order: 7
parent: "Region Functors"
grand_parent: "Functor List"
---
{% raw %}
# Region Manager Value

## Description

A data carrier functor that passes a region manager value from its input to its output unchanged, so it can be used to connect two other functors through an explicit connection instead of relying on auto-binding.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Region Manager | [Region Manager Type](../types/Region-Manager-Type.html) | The region manager to carry. When this functor is placed inside a [Region Manager](Region-Manager.html), [Region](Region.html), or [For Each Region](For-Each-Region.html) container, this port connects to that container's region manager automatically. | Provided automatically |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Region Manager | [Region Manager Type](../types/Region-Manager-Type.html) | The region manager provided as input. |

## Group

[Region](../Functor-List.html#region)

## Notes

None.

## Internal Name

RegionManagerValue
{% endraw %}
