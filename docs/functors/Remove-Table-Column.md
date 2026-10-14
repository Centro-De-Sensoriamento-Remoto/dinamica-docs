---
title: "Remove Table Column"
nav_order: 19
parent: "Table Functors"
grand_parent: "Functor List"
redirect_from:
  - /Remove-Table-Column.html
---
{% raw %}
# Remove Table Column

## Description

Removes a data column from the given table.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Table Type](../types/Table-Type.html) | Table from where the data column will be removed. |
| Column Index Or Name | [Index Or Name Type](../types/Index-Or-Name-Type.html) | Index or name of the data column to be removed. The first, i.e. the leftmost, data column has index 1. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Table Type](../types/Table-Type.html) | The resulting table without the specified data column. |

## Group

[Table](../Functor-List.html#table)

## Notes

It is not possible to remove the last remaining data column from a table.

## Internal Name

RemoveTableColumn
{% endraw %}
