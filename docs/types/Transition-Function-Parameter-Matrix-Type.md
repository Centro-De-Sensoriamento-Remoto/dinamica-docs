---
title: "Transition Function Parameter Matrix Type"
nav_order: 40
parent: "Type System"
grand_parent: "Core Concepts"
---
{% raw %}
# Transition Function Parameter Matrix Type

A Transition Function Parameter Matrix controls the shape and size of patches generated for a given `From`/`To` transition, used by [Patcher](../functors/Patcher.html) and [Expander](../functors/Expander.html) as their `transitionParameters` input. Each entry gives three parameters:

- **Mean Patch Size** — the average size of a generated patch, in hectares.
- **Patch Size Variance** — how much patch size varies around that mean, in the same units. A variance of zero produces uniformly-sized patches; a high variance relative to the mean produces widely varying patch sizes.
- **Patch Isometry** — a dimensionless factor controlling how compact or elongated a patch's shape is. Low values (near 0) produce linear, stretched-out patches; higher values (1.5-2 in Dinamica's own published examples) produce compact, roundish patches that tend to nucleate around a point rather than stretch outward.

## GUI Editor

The editor presents a table with fixed From, To, Mean Patch Size, Patch Size Variance, and Patch Isometry columns.

## EGO Script

A Transition Function Parameter Matrix constant has its own dedicated syntax in [EGO Script](../EGO-Script.html). Each entry is written `FROM->TO MEAN VARIANCE ISOMETRY`, with `FROM` and `TO` as integers joined directly by `->` with no space, followed by the three real-number parameters in order. As with [Transition Matrix](Transition-Matrix-Type.html), a stationary entry (`FROM` equal to `TO`) cannot be written. Commas around each entry are optional, and none are needed between the three parameter values themselves:

```
[
  1->2 20.0 5.0 1.5,
  1->3 5.0 0.0 0.0,
  2->1 10.0 2.0 1.0
]
```

## Automatic Conversions

- **Converted from**: [Table Type](Table-Type.html) — the table must have the columns `From*` (Real), `To*` (Real), `Mean_Patch_Size` (Real), `Patch_Size_Variance` (Real), and `Patch_Isometry` (Real).
- **Converted to**: [Table Type](Table-Type.html), using that same column layout. Unlike Transition Matrix, Change Matrix, and Percent Matrix, this type does not convert to or from [Lookup Table Type](Lookup-Table-Type.html).

See [Type System](../Type-System.html) for the complete conversion reference across all types.
{% endraw %}
