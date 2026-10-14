---
title: "Get Table From Key"
nav_order: 10
parent: "Table Functors"
grand_parent: "Functor List"
redirect_from:
  - /Get-Table-From-Key.html
---
{% raw %}
# Get Table From Key

## Description

Retrieves the sub-table corresponding to a given chain of keys from an input table.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Table Type](../types/Table-Type.html) | The input table. |
| Keys | [Tuple Type](../types/Tuple-Type.html) | Chain of keys, starting from the first key column, identifying the sub-table that will be retrieved. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Table Type](../types/Table-Type.html) | The resulting sub-table. |

## Group

[Table](../Functor-List.html#table)

## Notes

Keys is matched against the table's key columns starting from the leftmost one; a tuple with fewer elements than the table's key columns retrieves the sub-table formed by all rows sharing that key prefix, keeping only the remaining (unmatched) key columns.

**Example 1:**

Given the table below

| Key1\* | Key2\* | Key3\* | Value1 | Value2 | Value3 |
| --- | --- | --- | --- | --- | --- |
| 1 | "a" | 11 | 12 | "bbbb" | 23 |
| 1 | "b" | 22 | 12 | "cccc" | 23 |
| 2 | "a" | 11 | 12 | "bbbb" | 14 |
| 2 | "a" | 22 | 12 | "aaaa" | 23 |
| 2 | "d" | 22 | 12 | "dddd" | 12 |

retrieving the sub-table for the key tuple \<2, "a"> (Key1=2, Key2="a") results in

| Key3\* | Value1 | Value2 | Value3 |
| --- | --- | --- | --- |
| 11 | 12 | "bbbb" | 14 |
| 22 | 12 | "aaaa" | 23 |

**Example 2:**

Retrieving the sub-table for the key tuple \<2> (Key1=2 only) from the same table results in

| Key2\* | Key3\* | Value1 | Value2 | Value3 |
| --- | --- | --- | --- | --- |
| "a" | 11 | 12 | "bbbb" | 14 |
| "a" | 22 | 12 | "aaaa" | 23 |
| "d" | 22 | 12 | "dddd" | 12 |

It is not possible to retrieve a sub-table indexed by keys taken from arbitrary key columns — only a prefix of the leftmost key columns can be used this way. To index by a different key column, first bring it to the front with [Reorder Table Column](Reorder-Table-Column.html).

This functor reports an error if the resulting sub-table would have no key columns left, or if the given chain of keys is not present in the input table.

This functor also reports an error if Table is a lookup table, or a table with fewer than two key columns.

## Internal Name

GetTableFromKey

## Usage examples

See practical examples of this functor in Lesson 7: Creating a new column and retrieving a data column from tables
{% endraw %}
