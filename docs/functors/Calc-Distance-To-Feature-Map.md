---
title: "Calc Distance To Feature Map"
nav_order: 9
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calc Distance To Feature Map

## Description

Calculates a map representing the Euclidean distance, in meters, from every cell to the nearest cell representing a feature.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Source | [Categorical Map Type](../types/Categorical-Map-Type.html) | Map for which distances are calculated. A feature is represented by any non-null value. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Mask | [Map Type](../types/Map-Type.html) | Map restricting which cells have their distance calculated: only cells whose corresponding cell in Mask is non-null have a distance calculated. | None |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Cell type of the distance map. | Signed 32 Bit Integer |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Null value of the distance map. | -2147483648 |
| Truncate Distance | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, a distance exceeding the largest value representable in the output map is truncated to that largest value instead of reporting an error. This is an advanced port. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Distance | [Map Type](../types/Map-Type.html) | Map of distances, in meters, with the same dimensions as Source. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

Mask only restricts which cells receive a calculated distance in the output; it has no effect on which cells of Source are collected as features, so a feature located outside the area defined by Mask still influences the result.

Raises an error if Null Value is not compatible with Cell Type.

Reports a warning if Cell Type could degrade performance.

## Internal Name

CalcDistanceToFeatureMap
{% endraw %}
