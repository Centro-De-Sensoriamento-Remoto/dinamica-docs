---
title: "Map Junction"
nav_order: 16
parent: "Control Functors"
grand_parent: "Functor List"
redirect_from:
  - /Map-Junction.html
---
{% raw %}
# Map Junction

## Description

Picks the first available map from two possible execution pipelines, so a map still reaches the rest of the model even when one of the pipelines that could produce it does not run.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Possible Map 1 | [Map Type](../types/Map-Type.html) | Map produced by one possible execution pipeline. |
| Possible Map 2 | [Map Type](../types/Map-Type.html) | Map produced by another possible execution pipeline. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Map picked. |

## Group

[Control](../Functor-List.html#control)

## Notes

The inputs are checked in order — Possible Map 1, then Possible Map 2 — and the first one that has a map is passed to the output. If neither input has a map, the output is left without one, which allows chaining several junctions together to combine more than two possible pipelines.

This functor is typically placed after a container whose execution is conditional, such as [If Then](If-Then.html) or [Skip On Error](Skip-On-Error.html), so a default map is still available when that container's content does not run or does not finish.

This functor was previously known as "JoinMap".

## Internal Name

MapJunction
{% endraw %}
