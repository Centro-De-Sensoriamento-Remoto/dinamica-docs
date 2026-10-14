---
title: "Set Map Values"
nav_order: 37
parent: "Map Algebra Functors"
grand_parent: "Functor List"
redirect_from:
  - /Set-Map-Values.html
---
{% raw %}
# Set Map Values

## Description

Builds a map from three lookup tables that describe, per cell identifier, a cell's value and its line and column coordinates.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Value Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | Table of cell values, keyed by cell identifier. |
| Line Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | Table of cell lines (Y coordinates), keyed by cell identifier. The topmost line is 1. |
| Column Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | Table of cell columns (X coordinates), keyed by cell identifier. The leftmost column is 1. |
| Map Format | [Map Type](../types/Map-Type.html) | Map supplying the output's spatial format (geometry and projection). |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Cell type of the output map. |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Null value of the output map. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Result Is Sparse | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, forces the output map to be created as a sparse raster set, which stores only non-null cells, trading slower access time for reduced storage. This is an advanced port. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Map built from the given cell values and coordinates. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

A cell identifier missing from Value Table, Line Table, or Column Table raises an error.

A cell identifier present in Line Table and Column Table but omitted from Value Table is filled with null in the output map.

## Internal Name

SetMapValues
{% endraw %}
