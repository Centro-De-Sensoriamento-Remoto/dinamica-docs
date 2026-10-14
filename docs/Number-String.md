---
title: "Number String"
nav_exclude: true
---
{% raw %}
# Number String

## Description

Identifies a string by assigning a number to it, so that a container built to consume numbered strings — such as [Create String](Create-String.html) or [Select String](Select-String.html) — can pick it out by that number.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Value | [String Type](String-Type.html) | String to identify. |
| Value Number | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Number used to identify the string. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Map Algebra Supplementary](Functor-List.html#map-algebra-supplementary)

## Notes

This functor must be placed directly inside one of the containers that consume numbered strings — [Create String](Create-String.html) or [Select String](Select-String.html). Placed anywhere else, it has no effect.

Value Number is normally set to a fixed constant chosen by the model author.

## Internal Name

NumberString
{% endraw %}
