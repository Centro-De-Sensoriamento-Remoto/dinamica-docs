---
title: "Number And Name Map"
nav_exclude: true
---
{% raw %}
# Number And Name Map

## Description

Placeholder used to register a map under both a number and a name in the environment of the container it is placed inside. This functor produces no output itself: the enclosing container inspects its input ports and performs the actual registration.

This functor can be placed inside [Create Cube Map](Create-Cube-Map.html).

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](Map-Type.html) | Map to register in the environment. |
| Map Number | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Number under which the map will be known inside the container. |
| Map Name | [Name Type](Name-Type.html) | Name under which the map will be known in the environment. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Map Algebra Supplementary](Functor-List.html#map-algebra-supplementary)

## Notes

This functor's banner shows "Map" followed by the values of Map Number and Map Name.

Placing this functor inside a container it is not designed for reports a warning, since it has no effect there.

## Internal Name

NumberAndNameMap
{% endraw %}
