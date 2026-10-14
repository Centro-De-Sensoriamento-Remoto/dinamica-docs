---
title: "Select Lookup Table"
nav_order: 2
parent: "Stack Functors"
grand_parent: "Functor List"
redirect_from:
  - /Select-Lookup-Table.html
---
{% raw %}
# Select Lookup Table

## Description

Container that picks one lookup table out of a series connected inside it, based on the current step. Each candidate table must be connected through a [Number Table](Number-Table.html) hook, whose number identifies the step at which that table takes over. A table begins being selected once the model step reaches its number, and remains selected until the step reaches the number of another connected table, allowing one lookup table to be swapped for another during a model's execution.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Step | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Step used to pick the lookup table, automatically bound to the innermost compatible container. | 1 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | Selected lookup table. |

## Group

[Stack](../Functor-List.html#stack)

## Notes

Only [Number Table](Number-Table.html) hooks connected to a lookup table can be used inside this container.

The selected lookup table is the one with the greatest number identifier that is still less than or equal to Step.

## Internal Name

SelectLookupTable
{% endraw %}
