---
title: "Set Table By Key"
nav_order: 21
parent: "Table Functors"
grand_parent: "Functor List"
redirect_from:
  - /Set-Table-By-Key.html
---
{% raw %}
# Set Table By Key

## Description

Updates or inserts the sub-table corresponding to a given chain of keys in a table.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Table Type](../types/Table-Type.html) | The input table. |
| Keys | [Tuple Type](../types/Tuple-Type.html) | Chain of keys, starting from the first key column, identifying the sub-table that will be updated or inserted. |
| Sub Table | [Table Type](../types/Table-Type.html) | Sub-table that will be inserted into Table. Its column names must match the corresponding names in Table, or this functor reports an error, unless Ignore Column Names is set. Its column types must also be compatible. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Ignore Column Names | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, Sub Table's column names are not validated against Table's corresponding columns. | False |
| Combine Sub Tables | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, Sub Table is merged into the existing sub-table already present at the given keys, instead of replacing it. | False |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Table Type](../types/Table-Type.html) | The resulting table. |

## Group

[Table](../Functor-List.html#table)

## Notes

Keys is matched against Table's key columns starting from the leftmost one, the same way as in [Get Table From Key](Get-Table-From-Key.html); it is not possible to index by key columns other than a prefix of the leftmost ones. To index by a different key column, first bring it to the front with [Reorder Table Column](Reorder-Table-Column.html).

**Example 1:**

Given the table below

| Key1\* | Key2\* | Key3\* | Value1 | Value2 | Value3 |
| --- | --- | --- | --- | --- | --- |
| 1 | "a" | 11 | 12 | "bbbb" | 23 |
| 1 | "b" | 22 | 12 | "cccc" | 23 |
| 2 | "d" | 22 | 12 | "dddd" | 12 |

inserting a sub-table corresponding to the tuple of keys \<2, "a">, where 2 corresponds to column "Key1" and "a" corresponds to column "Key2",

| Key3\* | Value1 | Value2 | Value3 |
| --- | --- | --- | --- |
| @#C5D9FF: 11 | @#C5D9FF: 12 | @#C5D9FF: "bbbb" | @#C5D9FF: 14 |
| @#C5D9FF: 22 | @#C5D9FF: 12 | @#C5D9FF: "aaaa" | @#C5D9FF: 23 |

results in

| Key1\* | Key2\* | Key3\* | Value1 | Value2 | Value3 |
| --- | --- | --- | --- | --- | --- |
| 1 | "a" | 11 | 12 | "bbbb" | 23 |
| 1 | "b" | 22 | 12 | "cccc" | 23 |
| @#CCFFCC: 2 | @#CCFFCC: "a" | @#C5D9FF: 11 | @#C5D9FF: 12 | @#C5D9FF: "bbbb" | @#C5D9FF: 14 |
| @#CCFFCC: 2 | @#CCFFCC: "a" | @#C5D9FF: 22 | @#C5D9FF: 12 | @#C5D9FF: "aaaa" | @#C5D9FF: 23 |
| 2 | "d" | 22 | 12 | "dddd" | 12 |

**Example 2:**

Inserting the sub-table corresponding to the tuple of keys \<2>, where 2 corresponds to column "Key1",

| Key2\* | Key3\* | Value1 | Value2 | Value3 |
| --- | --- | --- | --- | --- |
| @#C5D9FF: "a" | @#C5D9FF: 11 | @#C5D9FF: 12 | @#C5D9FF: "bbbb" | @#C5D9FF: 14 |
| @#C5D9FF: "a" | @#C5D9FF: 22 | @#C5D9FF: 12 | @#C5D9FF: "aaaa" | @#C5D9FF: 23 |
| @#C5D9FF: "d" | @#C5D9FF: 22 | @#C5D9FF: 12 | @#C5D9FF: "dddd" | @#C5D9FF: 12 |

results in

| Key1\* | Key2\* | Key3\* | Value1 | Value2 | Value3 |
| --- | --- | --- | --- | --- | --- |
| 1 | "a" | 11 | 12 | "bbbb" | 23 |
| 1 | "b" | 22 | 12 | "cccc" | 23 |
| @#CCFFCC: 2 | @#C5D9FF: "a" | @#C5D9FF: 11 | @#C5D9FF: 12 | @#C5D9FF: "bbbb" | @#C5D9FF: 14 |
| @#CCFFCC: 2 | @#C5D9FF: "a" | @#C5D9FF: 22 | @#C5D9FF: 12 | @#C5D9FF: "aaaa" | @#C5D9FF: 23 |
| @#CCFFCC: 2 | @#C5D9FF: "d" | @#C5D9FF: 22 | @#C5D9FF: 12 | @#C5D9FF: "dddd" | @#C5D9FF: 12 |

If a sub-table already exists at the given keys, it is replaced by Sub Table (or merged with it, if Combine Sub Tables is true). If Sub Table is empty, the existing sub-table at those keys, if any, is removed from Table.

If the given keys are not yet present in Table and Sub Table is empty, this functor has no effect.

Table's own column names are always used as the column names of the resulting table, regardless of Ignore Column Names.

## Internal Name

SetTableByKey

## Usage examples

See practical examples of this functor in Lesson 7: Creating a new column and retrieving a data column from tables
{% endraw %}
