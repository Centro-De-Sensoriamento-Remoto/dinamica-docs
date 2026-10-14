---
title: "Calc Neighborhood"
nav_exclude: true
---
{% raw %}
# Calc Neighborhood

## Description

This functor calculates the relationship of neighboring features in a feature map.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Source | [Categorical Map Type](Categorical-Map-Type.html) | Map whose non-null cells correspond to features. If Source does not define a null value, this functor reports an error. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Only Orthogonals Are Allowed | [Boolean Value Type](Boolean-Value-Type.html) | If true, only cells connected orthogonally (horizontally/vertically) are considered neighbors. This is an advanced port. | No |
| Window Lines | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Number of lines of the neighbor search window. Even values are rounded up to the nearest odd number. This is an advanced port. | 3 |
| Window Columns | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Number of columns of the neighbor search window. Even values are rounded up to the nearest odd number. This is an advanced port. | 3 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Neighborhood | [Neighborhood Table Type](Neighborhood-Table-Type.html) | Relationship of neighboring features. |

## Group

[Statistics](Functor-List.html#statistics)

## Notes

Only the values present in Source's categorization are used to calculate neighbors; other values are ignored.

A reflexive relationship, with weight 0.0, is always defined for every value present in the categorization, so that even values without neighbors are represented in the resulting table.

A relationship between two neighbors always has weight 1.0, and is represented by two entries: the relationship found and its symmetric counterpart.

## Internal Name

CalcNeighborhood
{% endraw %}
