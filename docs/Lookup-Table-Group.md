---
title: "Lookup Table Group"
nav_exclude: true
---
{% raw %}
# Lookup Table Group

## Description

Declares a lookup table group value that can be reused as the input to more than one functor.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Constant | [Lookup Table Group Type](Lookup-Table-Group-Type.html) | Lookup table group value carried by this functor. Unlike most other data-carrier functors, this value cannot be entered as a literal constant — it must come from another functor's output, such as [Create Lookup Table Group](Create-Lookup-Table-Group.html). |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Object | [Lookup Table Group Type](Lookup-Table-Group-Type.html) | The lookup table group value provided as this functor's input. |

## Group

[Table](Functor-List.html#table)

## Notes

This functor passes its input value to its output unmodified, and can be used to feed the same lookup table group into more than one functor.

## Internal Name

LookupTableGroup
{% endraw %}
