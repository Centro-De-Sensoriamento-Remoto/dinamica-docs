---
title: "Calc Distance Allocation Map"
nav_order: 7
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calc Distance Allocation Map

## Description

This functor identifies a region of influence for each source feature, used as one of the foci points from which distances are calculated. For each source feature, a region is allocated by assigning to it every cell whose closest source feature it is.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Source | [Categorical Map Type](../types/Categorical-Map-Type.html) | Map whose non-null cells correspond to source features. If Source does not define a null value, this functor reports an error. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Mask | [Map Type](../types/Map-Type.html) | Map indicating the cells for which the distance to the closest source feature is calculated: only cells whose corresponding value in Mask is non-null have their distance calculated. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Allocation | [Categorical Map Type](../types/Categorical-Map-Type.html) | Map of the closest-source-feature regions. Each region is identified by the category of its source feature. Allocation has the same dimensions as Source. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

The distance used to determine each cell's closest source feature is the Euclidean distance.

The calculated allocation map can differ across runs using different numbers of executors, but only for cells where more than one source feature is equally close.

It is recommended that source features be single cells, since the 2D-tree algorithm this functor uses is optimized for that case.

## Internal Name

CalcDistanceAllocationMap
{% endraw %}
