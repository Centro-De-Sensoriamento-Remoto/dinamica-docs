---
title: "Select Percent Matrix"
nav_order: 5
parent: "Stack Functors"
grand_parent: "Functor List"
---
{% raw %}
# Select Percent Matrix

## Description

Container that picks one percent matrix out of a series connected inside it, based on the current step. Each candidate matrix must be connected through a [Number Percent Matrix](Number-Percent-Matrix.html) hook, whose number identifies the step at which that matrix takes over. A matrix begins being selected once the model step reaches its number, and remains selected until the step reaches the number of another connected matrix, allowing one matrix to be swapped for another during a model's execution.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Step | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Step used to pick the matrix, automatically bound to the innermost compatible container. | 1 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Percent Matrix | [Percent Matrix Type](../types/Percent-Matrix-Type.html) | Selected matrix of percents. |

## Group

[Stack](../Functor-List.html#stack)

## Notes

Only [Number Percent Matrix](Number-Percent-Matrix.html) hooks can be connected inside this container.

The selected matrix is the one with the greatest number identifier that is still less than or equal to Step.

## Internal Name

SelectPercentMatrix
{% endraw %}
