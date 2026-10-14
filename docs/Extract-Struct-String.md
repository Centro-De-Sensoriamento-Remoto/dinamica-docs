---
title: "Extract Struct String"
nav_exclude: true
---
{% raw %}
# Extract Struct String

## Description

Extracts a string stored in a Struct, such as the one returned by [Calculate R Expression](Calculate-R-Expression.html) or [Calculate Python Expression](Calculate-Python-Expression.html), by its name.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Struct | [Struct Type](Struct-Type.html) | Struct containing the string to extract. |
| Name | [String Type](String-Type.html) | Name under which the string is stored in the struct. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| String | [String Type](String-Type.html) | Extracted string. |

## Group

[Integration](Functor-List.html#integration)

## Notes

Raises an error if no string is stored under Name in Struct.

This functor's banner shows the value of Name.

## Internal Name

ExtractStructString
{% endraw %}
