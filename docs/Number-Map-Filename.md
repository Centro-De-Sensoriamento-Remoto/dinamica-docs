---
title: "Number Map Filename"
nav_exclude: true
---
{% raw %}
# Number Map Filename

## Description

Placeholder used to register a map filename under a given number in the container it is placed inside. This functor produces no output itself: the enclosing container inspects its input ports and performs the actual registration.

This functor can be placed inside [Select Map Filename](Select-Map-Filename.html).

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map Filename | [Map Filename Type](Map-Filename-Type.html) | Map filename to register in the container. |
| Filename Number | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Number under which the filename will be known inside the container. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Stack Supplementary](Functor-List.html#stack-supplementary)

## Notes

Placing this functor inside a container it is not designed for reports a warning, since it has no effect there.

## Internal Name

NumberMapFilename
{% endraw %}
