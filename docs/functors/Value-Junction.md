---
title: "Value Junction"
nav_order: 36
parent: "Control Functors"
grand_parent: "Functor List"
---
{% raw %}
# Value Junction

## Description

Picks the first available value from two possible execution pipelines, so a value still reaches the rest of the model even when one of the pipelines that could produce it does not run.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Possible Value 1 | [Real Value Type](../types/Real-Value-Type.html) | Value produced by one possible execution pipeline. |
| Possible Value 2 | [Real Value Type](../types/Real-Value-Type.html) | Value produced by another possible execution pipeline. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Value | [Real Value Type](../types/Real-Value-Type.html) | Value picked. |

## Group

[Control](../Functor-List.html#control)

## Notes

The inputs are checked in order — Possible Value 1, then Possible Value 2 — and the first one that has a value is passed to the output. If neither input has a value, the output is left without one, which allows chaining several junctions together to combine more than two possible pipelines.

This functor is typically placed after a container whose execution is conditional, such as [If Then](If-Then.html) or [Skip On Error](Skip-On-Error.html), so a default value is still available when that container's content does not run or does not finish.

This functor was previously known as "JoinDouble" and "JoinValue".

## Internal Name

ValueJunction
{% endraw %}
