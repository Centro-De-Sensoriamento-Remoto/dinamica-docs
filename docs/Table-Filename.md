---
title: "Table Filename"
nav_exclude: true
---
{% raw %}
# Table Filename

## Description

Declares a table filename value that can be reused as the input to more than one functor, or used as a constant.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Constant | [Table Filename Type](Table-Filename-Type.html) | Table filename value carried by this functor. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Object | [Table Filename Type](Table-Filename-Type.html) | The table filename value provided as this functor's input. |

## Group

[Table](Functor-List.html#table)

## Notes

This functor passes its input value to its output unmodified, and can be used to feed the same table filename into more than one functor, or to hold a constant table filename.

## Internal Name

TableFilename
{% endraw %}
