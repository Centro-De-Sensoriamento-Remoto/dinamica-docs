---
title: "Number Table Filename"
nav_exclude: true
---
{% raw %}
# Number Table Filename

## Description

Placeholder used to register a table filename under a given number in the container it is placed inside. This functor produces no output itself: the enclosing container inspects its input ports and performs the actual registration.

This functor can be placed inside [Select Table Filename](Select-Table-Filename.html).

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Filename | [Table Filename Type](Table-Filename-Type.html) | Table filename to register in the container. |
| Filename Number | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Number under which Filename will be known inside the container. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Stack Supplementary](Functor-List.html#stack-supplementary)

## Notes

A hook such as this one is typically used to feed one value of a given type into a container that performs some operation over a series of such values.

## Internal Name

NumberTableFilename
{% endraw %}
