---
title: "Lookup Table Filename"
nav_order: 14
parent: "Lookup Table Functors"
grand_parent: "Functor List"
redirect_from:
  - /Lookup-Table-Filename.html
---
{% raw %}
# Lookup Table Filename

## Description

Declares a lookup table filename value that can be reused as the input to more than one functor, or used as a constant.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Constant | [Lookup Table Filename Type](../types/Lookup-Table-Filename-Type.html) | Lookup table filename value carried by this functor. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Object | [Lookup Table Filename Type](../types/Lookup-Table-Filename-Type.html) | The lookup table filename value provided as this functor's input. |

## Group

[Lookup Table](../Functor-List.html#lookup-table)

## Notes

This functor passes its input value to its output unmodified, and can be used to feed the same lookup table filename into more than one functor, or to hold a constant lookup table filename.

## Internal Name

LookupTableFilename
{% endraw %}
