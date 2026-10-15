---
title: "Merge Sub Tables"
nav_order: 18
parent: "Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Merge Sub Tables

## Description

Combines all sub-tables registered under a given name, within the enclosing [Table Manager](Table-Manager.html), into Base Table.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Base Table | [Table Type](../types/Table-Type.html) | Table where the resulting combination of the sub-tables will be stored. |
| Table Name | [Name Type](../types/Name-Type.html) | Name of the set of sub-tables, registered via [Sub Table](Sub-Table.html), that will be combined. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Allow Names With No Associated Sub Tables | [Boolean Value Type](../types/Boolean-Value-Type.html) | If false, this functor reports an error when there are no sub-tables registered under Table Name. This is an advanced port. | False |
| Table Manager | [Table Manager Type](../types/Table-Manager-Type.html) | Table manager where the fragments and sub-tables corresponding to complete tables are kept. Automatically bound to the innermost enclosing [Table Manager](Table-Manager.html) container. This is an advanced port. | — |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Table Type](../types/Table-Type.html) | Table resulting from combining the registered sub-tables into Base Table. |

## Group

[Table](../Functor-List.html#table)

## Notes

This functor must be placed inside a [Table Manager](Table-Manager.html) container, which supplies the Table Manager port automatically.

Each sub-table combined into the result must have been previously registered under the same Table Name by a [Sub Table](Sub-Table.html) functor connected to the same table manager.

## Internal Name

MergeSubTables
{% endraw %}
