---
title: "Create Table"
nav_order: 7
parent: "Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Create Table

## Description

This functor creates a new table using a model table as a format.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Table](../types/Table-Type.html) | Input table containing the model used to create the new table. |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Table](../types/Table-Type.html) | The resulting empty table. |

## Group

[Table](../Functor-List.html#table)

## Notes

The new table is created removing all elements from the input table.

## Internal Name

CreateTable
{% endraw %}
