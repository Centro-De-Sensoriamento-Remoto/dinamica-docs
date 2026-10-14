---
title: "Table Manager Value"
nav_exclude: true
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
| Table Manager | [Table Manager Type](Table-Manager-Type.html) | Table manager instance. Automatically bound to the innermost enclosing [Table Manager](Table-Manager.html) container. | — |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Table Manager | [Table Manager Type](Table-Manager-Type.html) | The table manager instance provided as this functor's input. |

## Group

[Table](Functor-List.html#table)

## Notes

This functor is typically used to make the table manager instance from an enclosing [Table Manager](Table-Manager.html) container available to more than one functor at once.

## Internal Name

TableManagerValue
{% endraw %}
