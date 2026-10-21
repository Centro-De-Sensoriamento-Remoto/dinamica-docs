---
title: "Calculate Lookup Table 2"
nav_order: 5
parent: "Lookup Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calculate Lookup Table 2

## Description

Computes a new lookup table by evaluating an algebraic or logical expression once for every key of a format lookup table.

This functor is obsolete; use [Calculate Lookup Table Values](Calculate-Lookup-Table-Values.html) or [Calculate Lookup Table Keys And Values](Calculate-Lookup-Table-Keys-And-Values.html) instead.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Expression | [Image Expression Type](../types/Image-Expression-Type.html) | Algebraic or logical expression used to compute each output value. Must be enclosed in square brackets `[ ]` in EGO Script. |
| Format | [Lookup Table Type](../types/Lookup-Table-Type.html) | Lookup table whose keys define the format (and, by default, the key and value column names) of the output. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Key Name | [Name Type](../types/Name-Type.html) | Name given to the output's key column. If omitted, the corresponding name from Format is used. This is an advanced port. | .none |
| Value Name | [Name Type](../types/Name-Type.html) | Name given to the output's value column. If omitted, the corresponding name from Format is used. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Lookup Table Type](../types/Lookup-Table-Type.html) | Computed output lookup table. |

## Group

[Lookup Table](../Functor-List.html#lookup-table)

## Notes

All operations are performed using the precision defined by ImageExpression::Value; the final result is then converted to LookupTable::Value.

See [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for techniques that combine the table and lookup table functors.

## Internal Name

CalculateLookupTable2
{% endraw %}
