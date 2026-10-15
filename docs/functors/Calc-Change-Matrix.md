---
title: "Calc Change Matrix"
nav_order: 2
parent: "Simulation Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calc Change Matrix

## Description

This functor calculates the quantity of changes, multiplying the transition rates by the number of cells of each category to be changed.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Landscape | [Categorical Map Type](../types/Categorical-Map-Type.html) | Map of values for each category to be changed. |
| Transition Matrix | [Transition Matrix Type](../types/Transition-Matrix-Type.html) | A transition matrix containing transition rates. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Changes | [Change Matrix Type](../types/Change-Matrix-Type.html) | Matrix with the quantity of changes for each transition. |

## Group

[Simulation](../Functor-List.html#simulation)

## Notes

Since transition rates represent percentage of changes (net rates), they need to be multiplied by the number of cells of a certain category available for change to calculate the quantity of changes in terms of number of cells (crude rates).

The resulting number of cells (crude rate) is always rounded to the nearest integer value.

## Internal Name

CalcChangeMatrix

## Usage examples

See practical examples of this functor in Lesson 18: Building a land-use and land-cover change simulation model
{% endraw %}
