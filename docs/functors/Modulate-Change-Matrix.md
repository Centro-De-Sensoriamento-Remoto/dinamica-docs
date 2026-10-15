---
title: "Modulate Change Matrix"
nav_order: 4
parent: "Simulation Functors"
grand_parent: "Functor List"
---
{% raw %}
# Modulate Change Matrix

## Description

This functor is used to split the quantity of changes between different types of transition functions, i.e. Expander versus Patcher.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Changes | [Change Matrix Type](../types/Change-Matrix-Type.html) | Matrix of quantity of changes. |
| Modulation Rates | [Percent Matrix Type](../types/Percent-Matrix-Type.html) | Matrix setting the percents of changes for a set of transitions. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Modulated Changes | [Change Matrix Type](../types/Change-Matrix-Type.html) | Matrix of current quantity of changes as set by the matrix of percents. |
| Complementary Changes | [Change Matrix Type](../types/Change-Matrix-Type.html) | Matrix of complementary quantity of changes. Input matrix of changes minus the matrix of current quantity of changes. |

## Group

[Simulation](../Functor-List.html#simulation)

## Notes

This functor reports an error if a transition present in Changes has no corresponding rate in Modulation Rates.

## Internal Name

ModulateChangeMatrix

## Usage examples

See practical examples of this functor in Lesson 18: Building a land-use and land-cover change simulation model
{% endraw %}
