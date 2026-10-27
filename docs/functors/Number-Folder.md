---
title: "Number Folder"
nav_order: 61
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Number Folder

## Description

Identifies a folder by assigning a number to it, so that [Select Folder](Select-Folder.html) can pick it out by that number.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Value | [Folder Type](../types/Folder-Type.html) | Folder to identify. |
| Value Number | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number used to identify the folder. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Map Algebra Supplementary](../Functor-List.html#map-algebra-supplementary)

## Notes

This functor must be placed directly inside a [Select Folder](Select-Folder.html) container. Placed anywhere else, it has no effect.

Value Number is normally set to a fixed constant chosen by the model author.

## Internal Name

NumberFolder
{% endraw %}
