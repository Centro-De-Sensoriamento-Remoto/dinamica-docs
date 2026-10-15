---
title: "Folder Junction"
nav_order: 5
parent: "Control Functors"
grand_parent: "Functor List"
---
{% raw %}
# Folder Junction

## Description

Picks the first available folder from two possible execution pipelines, so a value still reaches the rest of the model even when one of the pipelines that could produce it does not run.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Possible Folder 1 | [Folder Type](../types/Folder-Type.html) | Folder produced by one possible execution pipeline. |
| Possible Folder 2 | [Folder Type](../types/Folder-Type.html) | Folder produced by another possible execution pipeline. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Folder | [Folder Type](../types/Folder-Type.html) | Folder picked. |

## Group

[Control](../Functor-List.html#control)

## Notes

The inputs are checked in order — Possible Folder 1, then Possible Folder 2 — and the first one that has a value is passed to the output. If neither input has a value, the output is left without one, which allows chaining several junctions together to combine more than two possible pipelines.

This functor is typically placed after a container whose execution is conditional, such as [If Then](If-Then.html) or [Skip On Error](Skip-On-Error.html), so a default value is still available when that container's content does not run or does not finish.

## Internal Name

FolderJunction
{% endraw %}
