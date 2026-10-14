---
title: "Number Percent Matrix"
nav_order: 13
parent: "Stack Functors"
grand_parent: "Functor List"
redirect_from:
  - /Number-Percent-Matrix.html
---
{% raw %}
# Number Percent Matrix

## Description

Placeholder used to register a percent matrix under a given number in the container it is placed inside. This functor produces no output itself: the enclosing container inspects its input ports and performs the actual registration.

This functor can be placed inside [Select Percent Matrix](Select-Percent-Matrix.html).

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Percent Matrix | [Percent Matrix Type](../types/Percent-Matrix-Type.html) | Matrix of percents to register in the container. |
| Matrix Number | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number under which Percent Matrix will be known inside the container. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Stack Supplementary](../Functor-List.html#stack-supplementary)

## Notes

A hook such as this one is typically used to feed one value of a given type into a container that performs some operation over a series of such values.

## Internal Name

NumberPercentMatrix
{% endraw %}
