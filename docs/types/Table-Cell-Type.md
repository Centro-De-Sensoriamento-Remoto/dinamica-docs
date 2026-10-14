---
title: "Table Cell Type"
nav_order: 29
parent: "Type System"
grand_parent: "Core Concepts"
redirect_from:
  - /Table-Cell-Type.html
---
{% raw %}
# Table Cell Type

## Description

Declares a table cell type value that can be reused as the input to more than one functor, or used as a constant.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Constant | [Table Cell Type](Table-Cell-Type.html) | Table cell type value carried by this functor. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Object | [Table Cell Type](Table-Cell-Type.html) | The table cell type value provided as this functor's input. |

## Group

[Table](../Functor-List.html#table)

## Notes

This functor passes its input value to its output unmodified, and can be used to feed the same table cell type into more than one functor, or to hold a constant table cell type.

## Internal Name

TableCellType
{% endraw %}
