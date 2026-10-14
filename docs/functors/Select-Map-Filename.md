---
title: "Select Map Filename"
nav_order: 4
parent: "Stack Functors"
grand_parent: "Functor List"
redirect_from:
  - /Select-Map-Filename.html
---
{% raw %}
# Select Map Filename

## Description

Container that picks one map filename out of a series of filenames connected inside it, based on the current step. Each candidate filename must be connected through a [Number Map Filename](Number-Map-Filename.html) hook, whose number identifies the step at which that filename takes over. A filename begins being selected once the model step reaches its number, and remains selected until the step reaches the number of another connected filename, allowing one filename to be swapped for another during a model's execution.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Step | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Step used to pick the filename, automatically bound to the innermost compatible container. | 1 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Map Filename | [Map Filename Type](../types/Map-Filename-Type.html) | Selected map filename. |

## Group

[Stack](../Functor-List.html#stack)

## Notes

Only [Number Map Filename](Number-Map-Filename.html) hooks can be connected inside this container.

The selected filename is the one with the greatest number identifier that is still less than or equal to Step.

## Internal Name

SelectMapFilename
{% endraw %}
