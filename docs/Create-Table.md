---
title: "Create Table"
nav_exclude: true
---
{% raw %}
# Create Table

## Description

This functor creates a new table using a model table as a format.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Table](Table-Type.html) | Input table containing the model used to create the new table. |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Table](Table-Type.html) | The resulting empty table. |

## Group

[Table](Functor-List.html#table)

## Notes

The new table is created removing all elements from the input table.

## Internal Name

CreateTable
{% endraw %}
