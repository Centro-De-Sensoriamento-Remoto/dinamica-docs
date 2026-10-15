---
title: "Create Lookup Table Group"
nav_order: 9
parent: "Lookup Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Create Lookup Table Group

## Description

Container that creates a lookup table group out of a series of lookup tables connected inside it.

## Inputs

None.

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Lookup Table Group | [Lookup Table Group Type](../types/Lookup-Table-Group-Type.html) | The resulting lookup table group, comprising the set of lookup tables connected inside this container. |

## Group

[Lookup Table](../Functor-List.html#lookup-table)

## Notes

Each lookup table inside this container must be provided by a corresponding [Number Table](Number-Table.html) hook.

The numbers assigned by the Number Table hooks must be sequential, starting at 1 with no gaps (1, 2, 3, and so on); otherwise this functor reports an error asking for the offending number to be renumbered.

The tables can later be retrieved individually from the group with [Extract Lookup Table From Lookup Table Group](Extract-Lookup-Table-From-Lookup-Table-Group.html), using the same sequential number as the index.

## Internal Name

CreateLookupTableGroup
{% endraw %}
