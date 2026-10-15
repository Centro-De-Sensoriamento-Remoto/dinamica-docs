---
title: "Number Map"
nav_order: 61
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Number Map

## Description

Placeholder used to register a map under a given number in the container it is placed inside. This functor produces no output itself: the enclosing container inspects its input ports and performs the actual registration.

This functor can be placed inside [Calculate Map](Calculate-Map.html), [Calculate Categorical Map](Calculate-Categorical-Map.html), [Select Map](Select-Map.html), and [Calculate Python Expression](Calculate-Python-Expression.html) (where map values are not currently supported, so connecting this hook to that container raises an error at runtime).

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Map to register in the container. |
| Map Number | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number under which the map will be known inside the container. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Map Algebra Supplementary](../Functor-List.html#map-algebra-supplementary)

## Notes

This functor's banner shows "Map" followed by the value of Map Number.

Reports a warning if Map Number is provided through a connection rather than as a constant.

Placing this functor inside a container it is not designed for reports a warning, since it has no effect there.

## Internal Name

NumberMap
{% endraw %}
