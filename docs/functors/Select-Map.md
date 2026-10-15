---
title: "Select Map"
nav_order: 3
parent: "Stack Functors"
grand_parent: "Functor List"
---
{% raw %}
# Select Map

## Description

Container that picks one map out of a series of maps connected inside it, based on the current step. Each candidate map must be connected through a [Number Map](Number-Map.html) hook, whose number identifies the step at which that map takes over. A map begins being selected once the model step reaches its number, and remains selected until the step reaches the number of another connected map, allowing one map to be swapped for another during a model's execution.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Step | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Step used to pick the map, automatically bound to the innermost compatible container. | — |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Selected map. |

## Group

[Stack](../Functor-List.html#stack)

## Notes

Only [Number Map](Number-Map.html) hooks can be connected inside this container.

The selected map is the one with the greatest number identifier that is still less than or equal to Step.

## Internal Name

SelectMap
{% endraw %}
