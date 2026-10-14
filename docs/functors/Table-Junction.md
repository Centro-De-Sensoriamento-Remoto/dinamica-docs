---
title: "Table Junction"
nav_order: 35
parent: "Control Functors"
grand_parent: "Functor List"
redirect_from:
  - /Table-Junction.html
---
{% raw %}
# Table Junction

## Description

Picks the first available table from two possible execution pipelines, so a table still reaches the rest of the model even when one of the pipelines that could produce it does not run.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Possible Table 1 | [Table Type](../types/Table-Type.html) | Table produced by one possible execution pipeline. |
| Possible Table 2 | [Table Type](../types/Table-Type.html) | Table produced by another possible execution pipeline. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Table Type](../types/Table-Type.html) | Table picked. |

## Group

[Control](../Functor-List.html#control)

## Notes

The inputs are checked in order — Possible Table 1, then Possible Table 2 — and the first one that has a value is passed to the output. If neither input has a value, the output is left without one, which allows chaining several junctions together to combine more than two possible pipelines.

This functor is typically placed after a container whose execution is conditional, such as [If Then](If-Then.html) or [Skip On Error](Skip-On-Error.html), so a default table is still available when that container's content does not run or does not finish.

## Internal Name

TableJunction
{% endraw %}
