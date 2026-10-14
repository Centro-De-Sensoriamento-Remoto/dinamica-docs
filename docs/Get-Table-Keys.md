---
title: "Get Table Keys"
nav_exclude: true
---
{% raw %}
# Get Table Keys

## Description

Returns a table mapping unique real identifiers to the keys of the first key column of a given table or lookup table. In case the keys of the given table are represented by real numbers, those numbers themselves are used as the unique identifiers.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Base Table Type](Base-Table-Type.html) | Table or lookup table whose first key column's keys will be returned. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Keys | [Table Type](Table-Type.html) | Table mapping unique real identifiers to the keys of the input table's first key column, in the format "Key\*:real, Value". The Value column has the same type as the input table's first key column. |

## Group

[Table](Functor-List.html#table)

## Notes

If the first key column of Table is of type Real, its own values are used as the Key identifiers, so Key and Value hold the same numbers.

If the first key column of Table is of type String, each unique string value is assigned a sequential real identifier (1, 2, 3, and so on), stored in Key, while the original string is kept in Value.

## Internal Name

GetTableKeys
{% endraw %}
