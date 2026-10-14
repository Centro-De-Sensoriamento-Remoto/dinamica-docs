---
title: "Name Value"
nav_order: 55
parent: "Map Algebra Functors"
grand_parent: "Functor List"
redirect_from:
  - /Name-Value.html
---
{% raw %}
# Name Value

## Description

Identifies a value by assigning a name to it, so that a container built to consume named values can pick it out by that name.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Value | [Real Value Type](../types/Real-Value-Type.html) | Value to identify. |
| Value Name | [Name Type](../types/Name-Type.html) | Name used to identify the value. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Map Algebra Supplementary](../Functor-List.html#map-algebra-supplementary)

## Notes

This functor must be placed directly inside a container that supports identifying values by name. Placed anywhere else, it has no effect.

## Internal Name

NameValue
{% endraw %}
