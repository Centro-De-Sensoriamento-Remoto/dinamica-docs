---
title: "Number Weights Filename"
nav_order: 18
parent: "Stack Functors"
grand_parent: "Functor List"
redirect_from:
  - /Number-Weights-Filename.html
---
{% raw %}
# Number Weights Filename

## Description

Placeholder used to register a Weights of Evidence filename under a given number in the container it is placed inside. This functor produces no output itself: the enclosing container inspects its input ports and performs the actual registration.

This functor can be placed inside [Select Weights Filename](Select-Weights-Filename.html).

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Weights Filename | [Weights Filename Type](../types/Weights-Filename-Type.html) | Weights of Evidence filename to register in the container. |
| Filename Number | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number under which Weights Filename will be known inside the container. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Stack Supplementary](../Functor-List.html#stack-supplementary)

## Notes

A hook such as this one is typically used to feed one value of a given type into a container that performs some operation over a series of such values.

## Internal Name

NumberWeightsFilename
{% endraw %}
