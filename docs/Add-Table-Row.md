---
title: "Add Table Row"
nav_exclude: true
---
{% raw %}
# Add Table Row

## Description

Inserts a row into the specified table.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Table Type](Table-Type.html) | Table where the new row will be created. |
| Values | [Tuple Type](Tuple-Type.html) | All values to be added as the new row. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Table Type](Table-Type.html) | The resulting table containing the new row. |

## Group

[Table](Functor-List.html#table)

## Notes

The tuple corresponding to the new row must have elements corresponding to all of the table's columns, otherwise this functor reports an error.

If a row with the same keys as the given tuple already exists in the input table, the existing row is updated with the new values.

## Internal Name

AddTableRow
{% endraw %}
