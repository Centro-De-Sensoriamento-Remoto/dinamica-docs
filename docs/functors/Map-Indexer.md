---
title: "Map Indexer"
nav_order: 35
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Map Indexer

## Description

Builds a lookup table by pairing, cell by cell, the values of two maps: the values of one map become the table's keys, and the values of the other, at the same coordinates, become the corresponding values.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Key Map | [Map Type](../types/Map-Type.html) | Map whose values become the keys of the resulting table. |
| Value Map | [Map Type](../types/Map-Type.html) | Map whose values become the values of the resulting table. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Key Value Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | Table pairing each non-null cell value of Key Map with the value found at the same coordinates in Value Map. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

A cell whose value in Key Map is null is skipped.

The topmost line and leftmost column of a map both have coordinate 1.

## Internal Name

MapIndexer
{% endraw %}
