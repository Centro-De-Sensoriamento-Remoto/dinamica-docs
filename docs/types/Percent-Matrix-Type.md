---
title: "Percent Matrix Type"
nav_order: 39
parent: "Type System"
grand_parent: "Core Concepts"
---
{% raw %}
# Percent Matrix Type

A Percent Matrix associates a fraction, from 0 to 1, with each `From`/`To` category pair. [Modulate Change Matrix](../functors/Modulate-Change-Matrix.html) uses one to split a [Change Matrix](Change-Matrix-Type.html)'s cell counts in two: the given rate produces `modulatedChanges`, and its complement produces `complementaryChanges`.

## GUI Editor

The percent matrix editor presents a table with fixed `From`/`To`/`Percent` columns.

## EGO Script

A Percent Matrix constant has its own dedicated syntax in [EGO Script](../EGO-Script.html), the same shape as [Transition Matrix](Transition-Matrix-Type.html)'s and [Change Matrix](Change-Matrix-Type.html)'s: each entry is written `FROM->TO PERCENT`, with `FROM` and `TO` as integers joined directly by `->` with no space, followed by the fraction as a real number from 0 to 1. Note that this is a plain real number, not [Percent Type](Percent-Type.html)'s own `%`-suffix literal form. As with [Transition Matrix](Transition-Matrix-Type.html), a stationary entry (`FROM` equal to `TO`) cannot be written. Commas between entries are optional:

```
[
  1->2 0.25,
  1->3 0.1,
  2->1 0.105,
  3->2 0.3
]
```

## Automatic Conversions

- **Converted from**: [Lookup Table Type](Lookup-Table-Type.html) and [Table Type](Table-Type.html) — the table must have the columns `From*` (Real), `To*` (Real), and `Percent` (Real).
- **Converted to**: [Lookup Table Type](Lookup-Table-Type.html) and [Table Type](Table-Type.html), using that same column layout.

See [Type System](../Type-System.html) for the complete conversion reference across all types.
{% endraw %}
