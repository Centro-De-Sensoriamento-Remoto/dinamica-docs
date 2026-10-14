---
title: "Get Table Column"
nav_exclude: true
---
{% raw %}
# Get Table Column

## Description

Retrieves a data column from the specified table.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Table Type](Table-Type.html) | Table from where the data column will be retrieved. |
| Column Index Or Name | [Index Or Name Type](Index-Or-Name-Type.html) | Index or name of the column to be retrieved. The first, i.e. the leftmost, data column has index 1. The index or name must correspond to a data column; if it corresponds to a key column, this functor reports an error. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Table Type](Table-Type.html) | The resulting table formed by the retrieved column and the table's key columns. |

## Group

[Table](Functor-List.html#table)

## Notes

This functor removes all data columns from the table, keeping only the key columns and the specified data column.

**Example:**

Given the table below

| Key1\* | Key2\* | Value1 | Value2 |
| --- | --- | --- | --- |
| 1 | 2 | 2.2 | 3.1 |
| 1 | 3 | 2.1 | 3.1 |
| 1 | 6 | 1.2 | 4.2 |
| 2 | 2 | 3.2 | 6.1 |

retrieving the column "Value1" results in the following table

| Key1\* | Key2\* | Value1 |
| --- | --- | --- |
| 1 | 2 | 2.2 |
| 1 | 3 | 2.1 |
| 1 | 6 | 1.2 |
| 2 | 2 | 3.2 |

## Internal Name

GetTableColumn
{% endraw %}
