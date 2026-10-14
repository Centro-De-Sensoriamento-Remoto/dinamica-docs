---
title: "Number Table Filename"
nav_order: 14
parent: "Stack Functors"
grand_parent: "Functor List"
redirect_from:
  - /Number-Table-Filename.html
---
{% raw %}
# Number Table Filename

## Description

Placeholder used to register a table filename under a given number in the container it is placed inside. This functor produces no output itself: the enclosing container inspects its input ports and performs the actual registration.

This functor can be placed inside [Select Table Filename](Select-Table-Filename.html).

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Filename | [Table Filename Type](../types/Table-Filename-Type.html) | Table filename to register in the container. |
| Filename Number | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number under which Filename will be known inside the container. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Stack Supplementary](../Functor-List.html#stack-supplementary)

## Notes

A hook such as this one is typically used to feed one value of a given type into a container that performs some operation over a series of such values.

## Internal Name

NumberTableFilename
{% endraw %}
