---
title: "Calc Integral Map"
nav_order: 12
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calc Integral Map

## Description

Generates an integral image (summed-area table) from a map: each output cell holds the cumulative sum of all cells up to and including its position. See [Summed-area table](https://en.wikipedia.org/wiki/Summed-area_table) for background on the technique.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Input | [Map Type](../types/Map-Type.html) | Map the cumulative sum is calculated from. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Use Full Precision | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, the output map uses the largest available cell type, avoiding precision errors when the running sum could exceed Input's cell type range. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Map Type](../types/Map-Type.html) | Resulting integral map. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

None.

## Internal Name

CalcIntegralMap
{% endraw %}
