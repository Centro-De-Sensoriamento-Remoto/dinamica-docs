---
title: "Sort Lookup Table"
nav_order: 16
parent: "Lookup Table Functors"
grand_parent: "Functor List"
redirect_from:
  - /Sort-Lookup-Table.html
---
{% raw %}
# Sort Lookup Table

## Description

Sorts the content of a lookup table.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Values Or Ids | [Lookup Table Type](../types/Lookup-Table-Type.html) | List of values or ids to sort; the keys only indicate the order of the entries in this list, so it corresponds to a plain list whose keys are indices and whose values are the elements. If Properties is not provided, this list is treated as a list of values to sort directly. Otherwise, it is treated as a list of ids, whose corresponding values are looked up in Properties. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Use Ascending Order | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, values or ids are sorted from lowest to highest, by the values used for comparison; if false, from highest to lowest. | True |
| Properties | [Lookup Table Type](../types/Lookup-Table-Type.html) | Lookup table mapping each id in Values Or Ids to the value used to sort it. If not provided, Values Or Ids is sorted directly as a list of values. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Sorted Values Or Ids | [Lookup Table Type](../types/Lookup-Table-Type.html) | Values Or Ids reordered so that its values (or, when Properties is given, the corresponding looked-up values) are sorted, with keys reassigned as sequential indices reflecting the new order. |

## Group

[Lookup Table](../Functor-List.html#lookup-table)

## Notes

The keys of Values Or Ids indicate only the order of its entries, not their content; the same is true of Sorted Values Or Ids.

## Internal Name

SortLookupTable
{% endraw %}
