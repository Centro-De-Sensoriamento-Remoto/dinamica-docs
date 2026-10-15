---
title: "Merge Regional Categorical Maps"
nav_order: 3
parent: "Region Functors"
grand_parent: "Functor List"
---
{% raw %}
# Merge Regional Categorical Maps

## Description

Rebuilds a single categorical map by merging together all the regional categorical maps that [Regional Categorical Map](Regional-Categorical-Map.html) registered under a given name in the same region manager.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Global Map Name | [Name Type](../types/Name-Type.html) | Name under which the regional categorical maps to merge were registered by [Regional Categorical Map](Regional-Categorical-Map.html). |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Merge Non Region Cells | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, cells located outside a region's mask — including its extra border — are merged in as well. If false, those cells are ignored. Merging two cells only works when they carry the same value, or when one of them is null. | No |
| Region Manager | [Region Manager Type](../types/Region-Manager-Type.html) | The region manager to read. When this functor is placed inside a [Region Manager](Region-Manager.html) or [Region](Region.html) container, this port connects to that container's region manager automatically. | Provided automatically |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Global Map | [Categorical Map Type](../types/Categorical-Map-Type.html) | Mosaic of the regional categorical maps registered under Global Map Name. |

## Group

[Region](../Functor-List.html#region)

## Notes

This functor raises an error if no [Regional Categorical Map](Regional-Categorical-Map.html) registered a map under Global Map Name in the same region manager.

Merging cells outside the region masks raises an error if two different regional maps disagree on the value of the same cell — that is, both give it a non-null value, and the values differ.

Placing this functor inside a [For Each Region](For-Each-Region.html) container raises an error, since the region manager that container exposes does not store regional maps — it only splits a map into regions, it does not collect them back together. Use a [Region Manager](Region-Manager.html) (or [Region](Region.html)) instead, with [Regional Categorical Map](Regional-Categorical-Map.html) registering each region's map inside it.

## Internal Name

MergeRegionalCategoricalMaps
{% endraw %}
