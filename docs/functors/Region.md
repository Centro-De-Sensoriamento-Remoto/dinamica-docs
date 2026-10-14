---
title: "Region"
nav_order: 5
parent: "Region Functors"
grand_parent: "Functor List"
redirect_from:
  - /Region.html
---
{% raw %}
# Region

## Description

This container takes a region identifier and a region manager — normally inherited automatically from an enclosing [For Each Region](For-Each-Region.html) or another [Region](Region.html) — and re-exposes them to the functors nested inside it. This lets those functors, which already read the current region through auto-bound inputs, be nested one level deeper without an explicit connection.

This functor is deprecated and will be removed in a future version of Dinamica EGO.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Region Id | [Integer Value Type](../types/Integer-Value-Type.html) | Identifier of the region, from the region manager. When this functor is placed inside a [For Each Region](For-Each-Region.html) or another [Region](Region.html), this port connects to the current region automatically. | Provided automatically |
| Region Manager | [Region Manager Type](../types/Region-Manager-Type.html) | The region manager to use. When this functor is placed inside a [Region Manager](Region-Manager.html), another [Region](Region.html), or a [For Each Region](For-Each-Region.html) container, this port connects to that container's region manager automatically. | Provided automatically |

## Outputs

None.

## Internal Outputs

| Name | Type | Description |
| --- | --- | --- |
| Region Id | [Integer Value Type](../types/Integer-Value-Type.html) | Identifier of the region. |
| Region Manager | [Region Manager Type](../types/Region-Manager-Type.html) | The region manager holding the regions. |

## Group

[Region](../Functor-List.html#region)

## Notes

This functor is deprecated and will be removed in a future version of Dinamica EGO. Its main effect — reducing the number of explicit connections by auto-binding the region identifier and the region manager — is already available directly on the functors that need them.

Raises an error if Region Id does not identify a region known to the region manager.

## Internal Name

Region
{% endraw %}
