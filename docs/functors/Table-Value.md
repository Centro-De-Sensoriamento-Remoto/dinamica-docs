---
title: "Table Value"
nav_order: 30
parent: "Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Table Value

## Description

Declares a value, which may be a real number or a string, that can be reused as the input to more than one functor, or used as a constant. This is the general value type used to interoperate with table functions.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Constant | [Table Value Type](../types/Table-Value-Type.html) | Value carried by this functor. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Object | [Table Value Type](../types/Table-Value-Type.html) | The value provided as this functor's input. |

## Group

[Table](../Functor-List.html#table)

## Notes

This functor passes its input value to its output unmodified, and can be used to feed the same value into more than one functor, or to hold a constant real number or string for use with table functions.

## Internal Name

TableValue
{% endraw %}
