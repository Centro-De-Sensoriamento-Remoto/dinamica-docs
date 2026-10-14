---
title: "Calc Lookup Table Difference"
nav_exclude: true
---
{% raw %}
# Calc Lookup Table Difference

## Description

Calculates the difference between two lookup tables.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| First Table | [Lookup Table Type](Lookup-Table-Type.html) | The first lookup table. |
| Second Table | [Lookup Table Type](Lookup-Table-Type.html) | The second lookup table. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Use Symmetrical Difference | [Boolean Value Type](Boolean-Value-Type.html) | If true, the symmetrical difference between First Table and Second Table is calculated, keeping the keys present in only one of the two tables; if false, the relative complement is calculated instead, keeping only the keys of First Table that do not occur in Second Table. | False |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Lookup Table Type](Lookup-Table-Type.html) | The resulting lookup table. |

## Group

[Lookup Table](Functor-List.html#lookup-table)

## Notes

The key and value column names of Result are inherited from First Table.

For background on the two set operations this functor can compute, see [relative complement](https://en.wikipedia.org/wiki/Complement_(set_theory)#Relative_complement) and [symmetric difference](https://en.wikipedia.org/wiki/Symmetric_difference).

## Internal Name

CalcLookupTableDifference
{% endraw %}
