---
title: "Get Lookup Table Value"
nav_order: 12
parent: "Lookup Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Get Lookup Table Value

## Description

Retrieves the value corresponding to a specified key from a lookup table.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | Lookup table to search. |
| Key | [Real Value Type](../types/Real-Value-Type.html) | Key to search for in Table. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Value If Not Found | [Real Value Type](../types/Real-Value-Type.html) | Value returned if Key is not present in Table. If not provided, an error is reported when the key is not found. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Value | [Real Value Type](../types/Real-Value-Type.html) | Value corresponding to the given key. |

## Group

[Lookup Table](../Functor-List.html#lookup-table)

## Notes

If Key is not found in Table and Value If Not Found is not provided, this functor reports an error, interrupting the model's execution.

To find an approximate match, or to interpolate between neighboring keys, instead use a [Calculate Value](Calculate-Value.html), [Calculate Map](Calculate-Map.html), [Calculate Categorical Map](Calculate-Categorical-Map.html), or [Calculate Lookup Table](Calculate-Lookup-Table.html) with one of the Lookup Table Operators described in the Image Expression Type documentation.

## Internal Name

GetLookupTableValue
{% endraw %}
