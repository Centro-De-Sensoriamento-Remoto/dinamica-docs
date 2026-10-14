---
title: "Number Transition Function Parameter Matrix"
nav_order: 15
parent: "Stack Functors"
grand_parent: "Functor List"
redirect_from:
  - /Number-Transition-Function-Parameter-Matrix.html
---
{% raw %}
# Number Transition Function Parameter Matrix

## Description

Placeholder used to register a matrix of transition function parameters under a given number in the container it is placed inside. This functor produces no output itself: the enclosing container inspects its input ports and performs the actual registration.

This functor can be placed inside [Select Transition Function Parameter Matrix](Select-Transition-Function-Parameter-Matrix.html).

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Function Parameter Matrix | [Transition Function Parameter Matrix Type](../types/Transition-Function-Parameter-Matrix-Type.html) | Matrix of transition function parameters to register in the container. |
| Matrix Number | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number under which Function Parameter Matrix will be known inside the container. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Stack Supplementary](../Functor-List.html#stack-supplementary)

## Notes

None.

## Internal Name

NumberTransitionFunctionParameterMatrix
{% endraw %}
