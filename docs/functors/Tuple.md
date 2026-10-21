---
title: "Tuple"
nav_order: 31
parent: "Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Tuple

## Description

Declares a tuple value that can be reused as the input to more than one functor, or used as a constant.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Constant | [Tuple Type](../types/Tuple-Type.html) | Tuple value carried by this functor. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Object | [Tuple Type](../types/Tuple-Type.html) | The tuple value provided as this functor's input. |

## Group

[Table](../Functor-List.html#table)

## Notes

This functor passes its input value to its output unmodified, and can be used to feed the same tuple into more than one functor, or to hold a constant tuple.

See [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for techniques that combine the table and lookup table functors.

## Internal Name

Tuple
{% endraw %}
