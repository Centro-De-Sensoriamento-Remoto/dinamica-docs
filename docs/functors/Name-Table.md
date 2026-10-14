---
title: "Name Table"
nav_order: 54
parent: "Map Algebra Functors"
grand_parent: "Functor List"
redirect_from:
  - /Name-Table.html
---
{% raw %}
# Name Table

## Description

Placeholder used to register a table or lookup table under a given name in the container it is placed inside. This functor produces no output itself: the enclosing container inspects its input ports and performs the actual registration.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Base Table Type](../types/Base-Table-Type.html) | Table or lookup table to register in the container. |
| Table Name | [Name Type](../types/Name-Type.html) | Name under which Table will be known inside the container. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Map Algebra Supplementary](../Functor-List.html#map-algebra-supplementary)

## Notes

A hook such as this one is typically used to feed one value of a given type into a container that performs some operation over a series of such values, identified by name.

## Internal Name

NameTable
{% endraw %}
