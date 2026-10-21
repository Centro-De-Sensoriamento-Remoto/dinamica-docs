---
title: "Table Manager Value"
nav_order: 29
parent: "Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Table Manager Value

## Description

Relays a table manager instance from its input to its output, so it can be connected to two or more other functors.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Table Manager | [Table Manager Type](../types/Table-Manager-Type.html) | Table manager instance. Automatically bound to the innermost enclosing [Table Manager](Table-Manager.html) container. | — |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Table Manager | [Table Manager Type](../types/Table-Manager-Type.html) | The table manager instance provided as this functor's input. |

## Group

[Table](../Functor-List.html#table)

## Notes

This functor is typically used to make the table manager instance from an enclosing [Table Manager](Table-Manager.html) container available to more than one functor at once.

See [TableManagerValue](../Manipulating-Tables-And-Lookup-Tables.html#tablemanagervalue) in [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for how this functor is used together with other table functors.

## Internal Name

TableManagerValue
{% endraw %}
