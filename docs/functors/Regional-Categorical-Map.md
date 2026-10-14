---
title: "Regional Categorical Map"
nav_order: 8
parent: "Region Functors"
grand_parent: "Functor List"
redirect_from:
  - /Regional-Categorical-Map.html
---
{% raw %}
# Regional Categorical Map

## Description

Registers a categorical map as the piece belonging to one region of a larger categorical map, under a name that [Merge Regional Categorical Maps](Merge-Regional-Categorical-Maps.html) later reads to rebuild the whole map. This functor produces no output — it is used purely for the side effect of storing the map in the region manager.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Global Map Name | [Name Type](../types/Name-Type.html) | Name under which the regional maps are kept by the region manager. Use the same name in the matching [Merge Regional Categorical Maps](Merge-Regional-Categorical-Maps.html). |
| Regional Map | [Categorical Map Type](../types/Categorical-Map-Type.html) | The categorical map for this region. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Region Id | [Integer Value Type](../types/Integer-Value-Type.html) | Identifier of the region that Regional Map belongs to. When this functor is placed inside a [For Each Region](For-Each-Region.html) or [Region](Region.html) container, this port connects to the current region automatically. | Provided automatically |
| Region Manager | [Region Manager Type](../types/Region-Manager-Type.html) | The region manager to register the map with. When this functor is placed inside a [Region Manager](Region-Manager.html) or [Region](Region.html) container, this port connects to that container's region manager automatically. | Provided automatically |

## Outputs

None.

## Group

[Region](../Functor-List.html#region)

## Notes

Region Id can be set to a fixed constant instead of being left to auto-bind, but doing so triggers a warning recommending that it be supplied by an enclosing loop's current iteration instead.

Registering a map under a Global Map Name that no [Merge Regional Categorical Maps](Merge-Regional-Categorical-Maps.html) reads back is reported with a warning. Registering two maps under the same Global Map Name for the same region manager is also reported with a warning.

Placing this functor inside a [For Each Region](For-Each-Region.html) container has no effect, since the region manager that container exposes does not store regional maps. Use a [Region Manager](Region-Manager.html) (or [Region](Region.html)) instead.

## Internal Name

RegionalCategoricalMap
{% endraw %}
