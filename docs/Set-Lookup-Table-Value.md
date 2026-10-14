---
title: "Set Lookup Table Value"
nav_exclude: true
---
{% raw %}
# Set Lookup Table Value

## Description

Inserts a value into a lookup table at a specified key. If the key is already present, its value is replaced.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Lookup Table Type](Lookup-Table-Type.html) | Lookup table where the value will be inserted. |
| Key | [Real Value Type](Real-Value-Type.html) | Key of the entry that will be inserted into Table. |
| Value | [Real Value Type](Real-Value-Type.html) | Value of the entry that will be inserted into Table. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Updated Table | [Lookup Table Type](Lookup-Table-Type.html) | The updated lookup table. |

## Group

[Lookup Table](Functor-List.html#lookup-table)

## Notes

If Key already has a value assigned in Table, that value is replaced by Value.

This functor was previously known as "UpdateLookupTable"; that name is still accepted for backward compatibility with existing scripts.

## Internal Name

SetLookupTableValue
{% endraw %}
