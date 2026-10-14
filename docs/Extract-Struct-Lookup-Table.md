---
title: "Extract Struct Lookup Table"
nav_exclude: true
---
{% raw %}
# Extract Struct Lookup Table

## Description

Extracts a lookup table stored in a Struct, such as the one returned by [Calculate R Expression](Calculate-R-Expression.html) or [Calculate Python Expression](Calculate-Python-Expression.html), by its name.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Struct | [Struct Type](Struct-Type.html) | Struct containing the lookup table to extract. |
| Name | [String Type](String-Type.html) | Name under which the lookup table is stored in the struct. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Lookup Table | [Lookup Table Type](Lookup-Table-Type.html) | Extracted lookup table. |

## Group

[Integration](Functor-List.html#integration)

## Notes

Raises an error if no lookup table is stored under Name in Struct.

This functor's banner shows the value of Name.

## Internal Name

ExtractStructLookupTable
{% endraw %}
