---
title: "Select Transition Function Parameter Matrix"
nav_order: 8
parent: "Stack Functors"
grand_parent: "Functor List"
redirect_from:
  - /Select-Transition-Function-Parameter-Matrix.html
---
{% raw %}
# Select Transition Function Parameter Matrix

## Description

Container that picks one matrix of transition function parameters out of a series connected inside it, based on the current step. Each candidate matrix must be connected through a [Number Transition Function Parameter Matrix](Number-Transition-Function-Parameter-Matrix.html) hook, whose number identifies the step at which that matrix takes over. A matrix begins being selected once the model step reaches its number, and remains selected until the step reaches the number of another connected matrix, allowing one matrix to be swapped for another during a model's execution.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Step | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Step used to pick the matrix, automatically bound to the innermost compatible container. | 1 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Function Parameter Matrix | [Transition Function Parameter Matrix Type](../types/Transition-Function-Parameter-Matrix-Type.html) | Selected matrix of transition function parameters. |

## Group

[Stack](../Functor-List.html#stack)

## Notes

Only [Number Transition Function Parameter Matrix](Number-Transition-Function-Parameter-Matrix.html) hooks can be connected inside this container.

The selected matrix is the one with the greatest number identifier that is still less than or equal to Step.

## Internal Name

SelectTransitionFunctionParameterMatrix
{% endraw %}
