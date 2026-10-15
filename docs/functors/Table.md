---
title: "Table"
nav_order: 25
parent: "Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Table

## Description

Declares a table value that can be reused as the input to more than one functor, or used as a constant.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Constant | [Table Type](../types/Table-Type.html) | Table value carried by this functor. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Object | [Table Type](../types/Table-Type.html) | The table value provided as this functor's input. |

## Group

[Table](../Functor-List.html#table)

## Notes

This functor passes its input value to its output unmodified, and can be used to feed the same table into more than one functor, or to hold a constant table.

## Internal Name

Table
{% endraw %}
