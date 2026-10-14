---
title: "Select Weights Filename"
nav_order: 11
parent: "Stack Functors"
grand_parent: "Functor List"
redirect_from:
  - /Select-Weights-Filename.html
---
{% raw %}
# Select Weights Filename

## Description

Container that picks one Weights of Evidence filename out of a series connected inside it, based on the current step. Each candidate filename must be connected through a [Number Weights Filename](Number-Weights-Filename.html) hook, whose number identifies the step at which that filename takes over. A filename begins being selected once the model step reaches its number, and remains selected until the step reaches the number of another connected filename, allowing one filename to be swapped for another during a model's execution.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Step | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Step used to pick the filename, automatically bound to the innermost compatible container. | 1 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Weights Filename | [Weights Filename Type](../types/Weights-Filename-Type.html) | Selected Weights of Evidence filename. |

## Group

[Stack](../Functor-List.html#stack)

## Notes

Only [Number Weights Filename](Number-Weights-Filename.html) hooks can be connected inside this container.

The selected filename is the one with the greatest number identifier that is still less than or equal to Step.

## Internal Name

SelectWeightsFilename
{% endraw %}
