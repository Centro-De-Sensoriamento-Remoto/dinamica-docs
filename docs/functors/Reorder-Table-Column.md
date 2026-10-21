---
title: "Reorder Table Column"
nav_order: 20
parent: "Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Reorder Table Column

## Description

Moves a specified column of a table to a new position.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Table Type](../types/Table-Type.html) | Table whose column will be reordered. |
| Column Index Or Name | [Index Or Name Type](../types/Index-Or-Name-Type.html) | Index or name of the column to be moved. The first, i.e. the leftmost, column has index 1. |
| New Column Index | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Index of the column at which the moved column will be re-inserted. The column currently at this position, and all columns after it, are shifted one position to make room. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Table Type](../types/Table-Type.html) | The resulting table with the column moved to its new position. |

## Group

[Table](../Functor-List.html#table)

## Notes

Key columns and data columns cannot be mixed: a data column cannot be moved to a position occupied by a key column, and vice versa.

If a key column is moved to a position occupied by a data column, or a data column is moved to a position occupied by a key column, the column is instead moved to the position immediately after the last key column (equivalently, immediately before the first data column).

A New Column Index of 0 moves the column to the last position among key columns or data columns, depending on which kind of column is being moved.

See [ReorderTableColumn](../Manipulating-Tables-And-Lookup-Tables.html#reordertablecolumn) in [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for how this functor is used together with other table functors.

## Internal Name

ReorderTableColumn
{% endraw %}
