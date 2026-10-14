---
title: "Select Weights"
nav_exclude: true
---
{% raw %}
# Select Weights

## Description

Container that picks one set of Weights of Evidence coefficients out of a series connected inside it, based on the current step. Each candidate set must be connected through a [Number Weights](Number-Weights.html) hook, whose number identifies the step at which that set takes over. A set begins being selected once the model step reaches its number, and remains selected until the step reaches the number of another connected set, allowing one set of coefficients to be swapped for another during a model's execution.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Step | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Step used to pick the coefficients, automatically bound to the innermost compatible container. | 1 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Weights | [Weights Type](Weights-Type.html) | Selected Weights of Evidence coefficients. |

## Group

[Stack](Functor-List.html#stack)

## Notes

Only [Number Weights](Number-Weights.html) hooks can be connected inside this container.

The selected coefficients are the ones with the greatest number identifier that is still less than or equal to Step.

## Internal Name

SelectWeights
{% endraw %}
