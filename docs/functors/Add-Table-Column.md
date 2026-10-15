---
title: "Add Table Column"
nav_order: 1
parent: "Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Add Table Column

## Description

Creates a new column in the given table. The position where the new column is inserted determines whether the new column is a key column or a data column.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Table Type](../types/Table-Type.html) | Table where the new column will be created. |
| Column Name | [Name Type](../types/Name-Type.html) | The new column's name. |
| Column Type | [Table Cell Type](../types/Table-Cell-Type.html) | The new column's cell type. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Column Index | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Position where the new column will be inserted. If zero or greater than the last column index, the column is placed as the last table column. If the column already exists, its existing index is kept. This is an advanced port. | 0 |
| Column Should Be Key | [Boolean Value Type](../types/Boolean-Value-Type.html) | Meaningful only when the new column is created between the last key column and the first data column: True makes it a key column, False makes it a data column. This is an advanced port. | False |
| Column Values | [Table Type](../types/Table-Type.html) | Table whose data column holds the initial values of the new data column, keyed the same way. Must have the same key columns (and types) as the table being modified, and exactly one data column; column names are ignored. Must not be provided when the new column is a key column. If the column already exists, these values are merged with the existing ones, overriding conflicting definitions. This is an advanced port. | .none |
| Default Value | [Table Value Type](../types/Table-Value-Type.html) | Value assigned to cells of the new column not covered by Column Values. If not provided, 0 or "" is used, depending on the column type. Using this setting may degrade performance. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Table Type](../types/Table-Type.html) | The resulting table containing the new column. |

## Group

[Table](../Functor-List.html#table)

## Notes

For best performance, avoid specifying a default value and always insert data columns as the last column.

**Example:**

Given the table below

| Key1\* | Key2\* | Value1 | Value2 |
| --- | --- | --- | --- |
| 1 | 2 | 2.2 | 3.1 |
| 1 | 3 | 2.1 | 3.1 |
| 1 | 6 | 1.2 | 4.2 |
| 2 | 2 | 3.2 | 6.1 |

adding a column named "New_Column" of type "Real" at position 2 results in

| Key1\* | New_Column\* | Key2\* | Value1 | Value2 |
| --- | --- | --- | --- | --- |
| 1 | @#C5D9FF: 0.0 | 2 | 2.2 | 3.1 |
| 1 | @#C5D9FF: 0.0 | 3 | 2.1 | 3.1 |
| 1 | @#C5D9FF: 0.0 | 6 | 1.2 | 4.2 |
| 2 | @#C5D9FF: 0.0 | 2 | 3.2 | 6.1 |

## Internal Name

AddTableColumn
{% endraw %}
