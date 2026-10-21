---
title: "Create Empty Table"
nav_order: 6
parent: "Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Create Empty Table

## Description

Creates a new empty table using a model table as a format.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Format Table | [Table Type](../types/Table-Type.html) | Input table containing the model used to create the new empty table. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Table Type](../types/Table-Type.html) | The resulting empty table. |

## Group

[Table](../Functor-List.html#table)

## Notes

The new table is created by removing all rows from Format Table, keeping only its column structure (names and types).

This functor was previously known as "CreateTable"; that name is still accepted for backward compatibility with existing scripts.

See [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for techniques that combine the table and lookup table functors.

## Internal Name

CreateEmptyTable
{% endraw %}
