---
title: "Int Set Type"
nav_exclude: true
---
{% raw %}
# Int Set Type

An Int Set represents a set of integers, most commonly a set of category codes to be treated as a group. [Calc Distance Map](Calc-Distance-Map.html)'s `categories` input is a concrete example: given a Categorical Map and an Int Set of class codes, it returns the distance from every cell to the nearest cell belonging to any of those classes.

## GUI Editor

The int set editor lets you enter a list of integer values.

## EGO Script

An Int Set constant is written in [EGO Script](EGO-Script.html) as a bracketed list of integers, with optional commas between them. The set cannot be empty — at least one integer is required:

```
[ 1, 2, 5 ]
```

## Automatic Conversions

- **Converted from**: [Lookup Table Type](Lookup-Table-Type.html) — each key is rounded to the nearest integer and added to the set; the associated values are discarded.
- **Converted to**: None.

See [Type System](Type-System.html) for the complete conversion reference across all types.
{% endraw %}
