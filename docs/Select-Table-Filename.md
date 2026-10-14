---
title: "Select Table Filename"
nav_exclude: true
---
{% raw %}
# Select Table Filename

## Description

Container that picks one table filename out of a series connected inside it, based on the current step. Each candidate filename must be connected through a [Number Table Filename](Number-Table-Filename.html) hook, whose number identifies the step at which that filename takes over. A filename begins being selected once the model step reaches its number, and remains selected until the step reaches the number of another connected filename, allowing one table file to be swapped for another during a model's execution.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Step | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Step used to pick the filename, automatically bound to the innermost compatible container. | 1 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Table Filename | [Table Filename Type](Table-Filename-Type.html) | Selected table filename. |

## Group

[Stack](Functor-List.html#stack)

## Notes

Only [Number Table Filename](Number-Table-Filename.html) hooks can be connected inside this container.

The selected filename is the one with the greatest number identifier that is still less than or equal to Step.

## Internal Name

SelectTableFilename
{% endraw %}
