---
title: "Calc Distance Map"
nav_order: 8
parent: "Map Algebra Functors"
grand_parent: "Functor List"
redirect_from:
  - /Calc-Distance-Map.html
---
{% raw %}
# Calc Distance Map

## Description

Calculates a map representing the Euclidean distance, in meters, from every cell to the nearest cell belonging to each of a set of given categories.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Categorical Map | [Categorical Map Type](../types/Categorical-Map-Type.html) | Map of classes or categories for which distances are calculated. A null cell in this map produces a null cell at the same position in the distance map. |
| Categories | [Int Set Type](../types/Int-Set-Type.html) | Categories for which distance maps are calculated. Each category produces a layer named "distance_to_i", where i is the category's value in Categorical Map. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Cell type of the distance map. | Signed 32 Bit Integer |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Null value of the distance map. | -2147483648 |
| Truncate Distance | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, a distance exceeding the largest value representable in the output map is truncated to that largest value instead of reporting an error. This is an advanced port. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Distance | [Map Type](../types/Map-Type.html) | Map of distances, in meters, with the same dimensions as Categorical Map, and one layer per category in Categories. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

Raises an error if Categories is empty, or if the only category given corresponds to Categorical Map's null value.

Raises an error if Null Value is not compatible with Cell Type.

Reports a warning if Cell Type could degrade performance.

## Internal Name

CalcDistanceMap

## Usage examples

See practical examples of this functor in Lesson 18: Building a land-use and land-cover change simulation model
{% endraw %}
