---
title: "Extract Lookup Table From Lookup Table Group"
nav_order: 11
parent: "Lookup Table Functors"
grand_parent: "Functor List"
redirect_from:
  - /Extract-Lookup-Table-From-Lookup-Table-Group.html
---
{% raw %}
# Extract Lookup Table From Lookup Table Group

## Description

Extracts the lookup table corresponding to a given index from a lookup table group.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Lookup Table Group | [Lookup Table Group Type](../types/Lookup-Table-Group-Type.html) | Input lookup table group. |
| Lookup Table Index | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Index of the lookup table to extract from Lookup Table Group, matching the sequential number assigned to it by its [Number Table](Number-Table.html) hook inside the [Create Lookup Table Group](Create-Lookup-Table-Group.html) that produced the group. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Lookup Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | The resulting lookup table. |

## Group

[Lookup Table](../Functor-List.html#lookup-table)

## Notes

None.

## Internal Name

ExtractLookupTableFromLookupTableGroup
{% endraw %}
