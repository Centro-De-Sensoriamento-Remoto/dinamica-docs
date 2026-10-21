---
title: "Sub Table"
nav_order: 24
parent: "Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Sub Table

## Description

Registers a table as the sub-table identified by a given chain of keys, within the named set of sub-tables managed by the enclosing [Table Manager](Table-Manager.html).

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table Name | [Name Type](../types/Name-Type.html) | Name of the set of sub-tables, within the table manager, that this sub-table belongs to. |
| Sub Table | [Table Type](../types/Table-Type.html) | The sub-table. |
| Keys | [Tuple Type](../types/Tuple-Type.html) | Chain of keys used to identify the sub-table. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Empty Sub Table Is Allowed | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, an empty table can be passed as Sub Table without this functor reporting an error. This is an advanced port. | True |
| Table Manager | [Table Manager Type](../types/Table-Manager-Type.html) | Table manager where the fragments and sub-tables corresponding to complete tables are kept. Automatically bound to the innermost enclosing [Table Manager](Table-Manager.html) container. This is an advanced port. | — |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Object | [Table Type](../types/Table-Type.html) | The sub-table's value. |

## Group

[Table](../Functor-List.html#table)

## Notes

This functor must be placed inside a [Table Manager](Table-Manager.html) container, which supplies the Table Manager port automatically.

Sub-tables registered under the same Table Name, distinguished by their Keys, are later combined into a single table by [Merge Sub Tables](Merge-Sub-Tables.html).

See [SubTable](../Manipulating-Tables-And-Lookup-Tables.html#subtable) in [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for how this functor is used together with other table functors.

## Internal Name

SubTable
{% endraw %}
