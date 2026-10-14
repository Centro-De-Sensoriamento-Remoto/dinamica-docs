---
title: "Extract Struct Tuple"
nav_order: 7
parent: "Integration Functors"
grand_parent: "Functor List"
redirect_from:
  - /Extract-Struct-Tuple.html
---
{% raw %}
# Extract Struct Tuple

## Description

Extracts a tuple stored in a Struct, such as the one returned by [Calculate R Expression](Calculate-R-Expression.html) or [Calculate Python Expression](Calculate-Python-Expression.html), by its name.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Struct | [Struct Type](../types/Struct-Type.html) | Struct containing the tuple to extract. |
| Name | [String Type](../types/String-Type.html) | Name under which the tuple is stored in the struct. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Tuple | [Tuple Type](../types/Tuple-Type.html) | Extracted tuple. |

## Group

[Integration](../Functor-List.html#integration)

## Notes

Raises an error if no tuple is stored under Name in Struct.

This functor's banner shows the value of Name.

## Internal Name

ExtractStructTuple
{% endraw %}
