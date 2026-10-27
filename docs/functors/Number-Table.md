---
title: "Number Table"
nav_order: 64
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Number Table

## Description

Placeholder used to register a table or lookup table under a given number in the container it is placed inside. This functor produces no output itself: the enclosing container inspects its input ports and performs the actual registration.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Base Table Type](../types/Base-Table-Type.html) | Table or lookup table to register in the container. |
| Table Number | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number under which Table will be known inside the container. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Map Algebra Supplementary](../Functor-List.html#map-algebra-supplementary)

## Notes

A hook such as this one is typically used to feed one value of a given type into a container that performs some operation over a series of such values, such as Calculate Table.

## Internal Name

NumberTable
{% endraw %}
