---
title: "Lookup Table"
nav_order: 13
parent: "Lookup Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Lookup Table

## Description

Declares a lookup table value that can be reused as the input to more than one functor, or used as a constant.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Constant | [Lookup Table Type](../types/Lookup-Table-Type.html) | Lookup table value carried by this functor. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Object | [Lookup Table Type](../types/Lookup-Table-Type.html) | The lookup table value provided as this functor's input. |

## Group

[Lookup Table](../Functor-List.html#lookup-table)

## Notes

This functor passes its input value to its output unmodified, and can be used to feed the same lookup table into more than one functor, or to hold a constant lookup table.

See [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for techniques that combine the table and lookup table functors.

## Internal Name

LookupTable
{% endraw %}
