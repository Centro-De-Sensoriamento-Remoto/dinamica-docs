---
title: "Calc Lookup Table Intersection"
nav_order: 2
parent: "Lookup Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calc Lookup Table Intersection

## Description

Calculates the lookup table that is the intersection of two lookup tables.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| First Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | The first lookup table. |
| Second Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | The second lookup table. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Use First Table To Solve Duplicated Key | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, and a key occurs in both tables, the value from First Table is kept; if false, the value from Second Table is kept instead. | True |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Lookup Table Type](../types/Lookup-Table-Type.html) | The resulting lookup table, containing only the keys present in both First Table and Second Table. |

## Group

[Lookup Table](../Functor-List.html#lookup-table)

## Notes

The key and value column names of Result are inherited from First Table.

For background on this operation, see [set intersection](https://en.wikipedia.org/wiki/Intersection_(set_theory)).

See [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for techniques that combine the table and lookup table functors.

## Internal Name

CalcLookupTableIntersection
{% endraw %}
