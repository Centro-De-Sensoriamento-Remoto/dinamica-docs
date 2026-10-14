---
title: "Calc Cost Allocation Map"
nav_exclude: true
---
{% raw %}
# Calc Cost Allocation Map

## Description

This functor identifies a region of influence for each source feature, used as one of the foci points from which an accumulated cost surface is calculated. For each source feature, a region is allocated by assigning to it every cell that has a lower cost to reach that feature than any other.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Sources | [Categorical Map Type](Categorical-Map-Type.html) | Map whose non-null cells correspond to source features. If Sources does not define a null value, this functor reports an error. |
| Costs Or Directions | [Map Type](Map-Type.html) | Map of accumulated cost per cell, or of its corresponding cost directions. |
| Input Represents Directions | [Boolean Value Type](Boolean-Value-Type.html) | If true, Costs Or Directions is assumed to represent cost directions; otherwise, it is assumed to represent costs. A cost-direction cell can only take the eight values corresponding to the directions of a Moore neighborhood: None=0, NW=1, N=2, NE=3, E=4, SE=5, S=6, SW=7, and W=8. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Use Lottery | [Boolean Value Type](Boolean-Value-Type.html) | If true, ties for the lowest cost are broken randomly. This is an advanced port. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Allocation | [Categorical Map Type](Categorical-Map-Type.html) | Map of cost regions, one per source feature — similar to a watershed. Each region is identified by the category of its source feature. Allocation has the same dimensions as Sources. |

## Group

[Map Algebra](Functor-List.html#map-algebra)

## Notes

This functor reports an error if a local minimum is found on the cost map.

## Internal Name

CalcCostAllocationMap
{% endraw %}
