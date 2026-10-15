---
title: "Transition Matrix Type"
nav_order: 41
parent: "Type System"
grand_parent: "Core Concepts"
---
{% raw %}
# Transition Matrix Type

A Transition Matrix defines the rate at which cells transition from one category to another over a period of time. Each entry gives a `From` category, a `To` category, and a rate — the proportion of `From` cells that transition to `To` over that period. A category's rates sum to 1 across all its entries, but the stationary (`From` = `To`) share — the proportion that doesn't change — cannot be written directly; it's implied as whatever remains once the category's other rates are accounted for.

[Determine Transition Matrix](../functors/Determine-Transition-Matrix.html) calculates one directly from a pair of calibration maps: given an `initialLandscape`, a `finalLandscape`, and a `timeSteps` count, it returns a `singleStepMatrix` (rates for the entire calibrated period) and a `multiStepMatrix` (rates normalized to one time unit, suitable for driving an iterative simulation), deriving each category's stationary share the same way. [Calc Change Matrix](../functors/Calc-Change-Matrix.html) is the typical consumer: given a Transition Matrix and the current landscape, it converts each entry's proportional rate into an absolute [Change Matrix](Change-Matrix-Type.html) entry — the actual number of cells to change, based on the landscape's current class areas.

## GUI Editor

The transition matrix editor presents a table with fixed `From`/`To`/`Rate` columns.

## EGO Script

A Transition Matrix constant has its own dedicated syntax in [EGO Script](../EGO-Script.html) — the same shape [Change Matrix](Change-Matrix-Type.html) and [Percent Matrix](Percent-Matrix-Type.html) also use. Each entry is written `FROM->TO RATE`, with `FROM` and `TO` as integers joined directly by `->` with no space, followed by the rate as a real number. A stationary entry (`FROM` equal to `TO`) cannot be written; only the rates for actual transitions are given. Commas between entries are optional. This example gives class 1 a 10% chance of becoming class 2 and a 5% chance of becoming class 3 (85% remaining stationary), class 2 a 2% chance of becoming class 1 (98% stationary), and class 3 a 15% chance of becoming class 1 (85% stationary):

```
[
  1->2 0.1,
  1->3 0.05,
  2->1 0.02,
  3->1 0.15
]
```

## Automatic Conversions

- **Converted from**: [Lookup Table Type](Lookup-Table-Type.html) and [Table Type](Table-Type.html) — the table must have the columns `From*` (Real), `To*` (Real), and `Rate` (Real).
- **Converted to**: [Lookup Table Type](Lookup-Table-Type.html) and [Table Type](Table-Type.html), using that same column layout.

See [Type System](../Type-System.html) for the complete conversion reference across all types.
{% endraw %}
