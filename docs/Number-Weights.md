---
title: "Number Weights"
nav_exclude: true
---
{% raw %}
# Number Weights

## Description

Placeholder used to register a set of Weights of Evidence coefficients under a given number in the container it is placed inside. This functor produces no output itself: the enclosing container inspects its input ports and performs the actual registration.

This functor can be placed inside [Select Weights](Select-Weights.html).

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Weights | [Weights Type](Weights-Type.html) | Weights of Evidence coefficients to register in the container. |
| Weight Number | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Number under which Weights will be known inside the container. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Stack Supplementary](Functor-List.html#stack-supplementary)

## Notes

A hook such as this one is typically used to feed one value of a given type into a container that performs some operation over a series of such values.

## Internal Name

NumberWeights
{% endraw %}
