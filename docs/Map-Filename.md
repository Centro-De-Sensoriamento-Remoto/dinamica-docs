---
title: "Map Filename"
nav_exclude: true
---
{% raw %}
# Map Filename

## Description

Declares a filename referring to a map file that can be reused as the input to more than one functor, instead of repeating the same constant throughout the model.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Constant | [Map Filename Type](Map-Filename-Type.html) | Value or constant representing a map filename. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Object | [Map Filename Type](Map-Filename-Type.html) | Value or constant representing a map filename, provided as the functor input. |

## Group

[Map Algebra Supplementary](Functor-List.html#map-algebra-supplementary)

## Notes

Can be used to pass a constant filename to more than one functor, or to connect two or more functors.

## Internal Name

MapFilename
{% endraw %}
