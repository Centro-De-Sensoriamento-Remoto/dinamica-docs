---
title: "Number Transition Matrix"
nav_exclude: true
---
{% raw %}
# Number Transition Matrix

## Description

Placeholder used to register a transition matrix under a given number in the container it is placed inside. This functor produces no output itself: the enclosing container inspects its input ports and performs the actual registration.

This functor can be placed inside [Select Transition Matrix](Select-Transition-Matrix.html).

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Transition Matrix | [Transition Matrix Type](Transition-Matrix-Type.html) | Matrix of transition rates to register in the container. |
| Matrix Number | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Number under which Transition Matrix will be known inside the container. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Stack Supplementary](Functor-List.html#stack-supplementary)

## Notes

A hook such as this one is typically used to feed one value of a given type into a container that performs some operation over a series of such values.

## Internal Name

NumberTransitionMatrix
{% endraw %}
