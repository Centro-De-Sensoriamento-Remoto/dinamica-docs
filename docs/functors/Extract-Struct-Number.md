---
title: "Extract Struct Number"
nav_order: 4
parent: "Integration Functors"
grand_parent: "Functor List"
redirect_from:
  - /Extract-Struct-Number.html
---
{% raw %}
# Extract Struct Number

## Description

Extracts a number stored in a Struct, such as the one returned by [Calculate R Expression](Calculate-R-Expression.html) or [Calculate Python Expression](Calculate-Python-Expression.html), by its name.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Struct | [Struct Type](../types/Struct-Type.html) | Struct containing the number to extract. |
| Name | [String Type](../types/String-Type.html) | Name under which the number is stored in the struct. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Number | [Real Value Type](../types/Real-Value-Type.html) | Extracted number. |

## Group

[Integration](../Functor-List.html#integration)

## Notes

Raises an error if no number is stored under Name in Struct.

This functor's banner shows the value of Name.

## Internal Name

ExtractStructNumber
{% endraw %}
