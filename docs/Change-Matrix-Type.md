---
title: "Change Matrix Type"
nav_exclude: true
---
{% raw %}
# Change Matrix Type

A Change Matrix gives the number of cells to transition from one category to another. Each entry has a `From` category, a `To` category, and a whole-number count of cells.

[Calc Change Matrix](Calc-Change-Matrix.html) is the typical source: given a [Transition Matrix](Transition-Matrix-Type.html) of proportional rates and the current landscape, it multiplies each rate against the landscape's actual class areas to produce the corresponding cell counts. [Patcher](Patcher.html) and [Expander](Expander.html) both consume one directly to know how many cells of each transition to allocate spatially, and each also returns a `remainingChanges` output — the portion left unallocated after that step. [Add Change Matrix](Add-Change-Matrix.html) sums two Change Matrices together, and [Modulate Change Matrix](Modulate-Change-Matrix.html) splits one in two using a [Percent Matrix](Percent-Matrix-Type.html) of rates, producing a `modulatedChanges` matrix and a complementary `complementaryChanges` matrix.

## GUI Editor

The change matrix editor presents a table with fixed `From`/`To`/`Cells` columns.

## EGO Script

A Change Matrix constant has its own dedicated syntax in [EGO Script](EGO-Script.html), the same shape as [Transition Matrix](Transition-Matrix-Type.html)'s: each entry is written `FROM->TO CELLS`, with `FROM` and `TO` as integers joined directly by `->` with no space. Unlike Transition Matrix's rate, `CELLS` is an integer, not a real number. As with [Transition Matrix](Transition-Matrix-Type.html), a stationary entry (`FROM` equal to `TO`) cannot be written. Commas between entries are optional:

```
[
  1->2 150,
  1->3 75,
  2->1 40,
  3->1 200
]
```

## Automatic Conversions

- **Converted from**: [Lookup Table Type](Lookup-Table-Type.html) and [Table Type](Table-Type.html) — the table must have the columns `From*` (Real), `To*` (Real), and `Cells` (Real).
- **Converted to**: [Lookup Table Type](Lookup-Table-Type.html) and [Table Type](Table-Type.html), using that same column layout.

See [Type System](Type-System.html) for the complete conversion reference across all types.
{% endraw %}
