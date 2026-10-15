---
title: "Extract Struct String"
nav_order: 5
parent: "Integration Functors"
grand_parent: "Functor List"
---
{% raw %}
# Extract Struct String

## Description

Extracts a string stored in a Struct, such as the one returned by [Calculate R Expression](Calculate-R-Expression.html) or [Calculate Python Expression](Calculate-Python-Expression.html), by its name.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Struct | [Struct Type](../types/Struct-Type.html) | Struct containing the string to extract. |
| Name | [String Type](../types/String-Type.html) | Name under which the string is stored in the struct. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| String | [String Type](../types/String-Type.html) | Extracted string. |

## Group

[Integration](../Functor-List.html#integration)

## Notes

Raises an error if no string is stored under Name in Struct.

This functor's banner shows the value of Name.

## Internal Name

ExtractStructString
{% endraw %}
