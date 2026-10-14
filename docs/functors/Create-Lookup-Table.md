---
title: "Create Lookup Table"
nav_order: 8
parent: "Lookup Table Functors"
grand_parent: "Functor List"
redirect_from:
  - /Create-Lookup-Table.html
---
{% raw %}
# Create Lookup Table

## Description

Creates a lookup table populated between an initial and a final key, interpolating the values assigned to each.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Initial Key | [Real Value Type](../types/Real-Value-Type.html) | Initial (first) key of the resulting lookup table. |
| Final Key | [Real Value Type](../types/Real-Value-Type.html) | Final (last) key of the resulting lookup table. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Initial Value | [Real Value Type](../types/Real-Value-Type.html) | Value assigned to Initial Key. | 0.0 |
| Final Value | [Real Value Type](../types/Real-Value-Type.html) | Value assigned to Final Key. | 0.0 |
| Increment | [Real Value Type](../types/Real-Value-Type.html) | Interval between consecutive keys of the resulting lookup table. | 1.0 |
| Key Name | [Name Type](../types/Name-Type.html) | Name given to the lookup table's key column. This is an advanced port. | "Key" |
| Value Name | [Name Type](../types/Name-Type.html) | Name given to the lookup table's value column. This is an advanced port. | "Value" |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Lookup Table Type](../types/Lookup-Table-Type.html) | The resulting lookup table. |

## Group

[Lookup Table](../Functor-List.html#lookup-table)

## Notes

The values between Initial Key and Final Key are linearly interpolated between Initial Value and Final Value.

Final Key is included in the resulting lookup table only if the interval between it and the immediately preceding key is compatible with Increment.

## Internal Name

CreateLookupTable
{% endraw %}
