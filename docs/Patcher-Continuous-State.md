---
title: "Patcher Continuous State"
nav_exclude: true
---
{% raw %}
# Patcher Continuous State

## Description

This functor generates new patches of a certain class or category, allocating a continuous quantity of stock, rather than a discrete number of cells, up to a specified quota.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Continuous Landscape | [Map Type](Map-Type.html) | Map of stocks. Each cell represents the amount of stock stored, in units per hectare. |
| Probabilities | [Map Type](Map-Type.html) | Map of spatial probabilities. |
| Quota | [Real Value Type](Real-Value-Type.html) | Accumulation quota, in units. |
| Mean | [Real Value Type](Real-Value-Type.html) | Patch mean, in hectares. |
| Variance | [Real Value Type](Real-Value-Type.html) | Patch variance, in hectares. |
| Isometry | [Real Value Type](Real-Value-Type.html) | Patch isometry. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Neighbor Window Lines | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Number of lines of the neighborhood search window. This is an advanced port. | 3 |
| Neighbor Window Columns | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Number of columns of the neighborhood search window. This is an advanced port. | 3 |
| Prune Factor | [Real Value Type](Real-Value-Type.html) | A multiple of the quantity of stock to be allocated, used to size the vector where cells are ranked for the subsequent draw. This is an advanced port. | 10 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Modified Continuous Landscape | [Map Type](Map-Type.html) | Map of remaining stocks. |
| Modified Probabilities | [Map Type](Map-Type.html) | Map of depleted spatial probabilities. |
| Remaining Quota | [Real Value Type](Real-Value-Type.html) | Quota that could not be accumulated. |

## Group

[Simulation](Functor-List.html#simulation)

## Notes

This functor works like Patcher, but accumulates a continuous quantity of stock into new patches, up to Quota, instead of transitioning a discrete number of cells.

Patch isometry is a number varying from 0 to 2. Patches assume a more isometric form as this number increases.

## Internal Name

PatcherContinuousState
{% endraw %}
