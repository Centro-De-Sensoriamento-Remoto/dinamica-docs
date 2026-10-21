---
title: "Table Manager"
nav_order: 28
parent: "Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Table Manager

## Description

Container that creates and manages the fragments and sub-tables corresponding to complete tables, letting tables be assembled incrementally from pieces produced at different points of a model.

## Inputs

None.

## Optional Inputs

None.

## Outputs

None.

## Internal Outputs

| Name | Type | Description |
| --- | --- | --- |
| Table Manager | [Table Manager Type](../types/Table-Manager-Type.html) | Table manager instance, internally linked to the [Sub Table](Sub-Table.html), [Merge Sub Tables](Merge-Sub-Tables.html), and [Table Manager Value](Table-Manager-Value.html) functors placed inside this container. |

## Group

[Table](../Functor-List.html#table)

## Notes

[Sub Table](Sub-Table.html) and [Merge Sub Tables](Merge-Sub-Tables.html) functors placed inside this container automatically bind their advanced Table Manager port to this container's internal output.

See [TableManager](../Manipulating-Tables-And-Lookup-Tables.html#tablemanager) in [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for how this functor is used together with other table functors.

## Internal Name

TableManager
{% endraw %}
