---
title: "Transition Set Type"
nav_exclude: true
---
{% raw %}
# Transition Set Type

A Transition Set is a plain set of transitions — unlike [Transition Matrix](Transition-Matrix-Type.html), [Change Matrix](Change-Matrix-Type.html), and [Percent Matrix](Percent-Matrix-Type.html), which each pair a `From`/`To` transition with a value (a rate, a cell count, a percentage), a Transition Set only records which transitions are included, with no value attached. [Determine Weights Of Evidence Correlation](Determine-Weights-Of-Evidence-Correlation.html)'s `transition` input is a concrete example, specifying which particular From/To transitions to compute correlation diagnostics for.

## GUI Editor

The transition set editor presents a list of `From`/`To` transitions.

## EGO Script

A Transition Set constant has its own dedicated syntax in [EGO Script](EGO-Script.html). Each entry is written `FROM->TO`, with `FROM` and `TO` as integers joined directly by `->` with no space. A stationary entry (`FROM` equal to `TO`) is allowed. Commas between entries are optional:

```
[
  1->2,
  1->1,
  2->1,
  3->1
]
```

## Automatic Conversions

- **Converted from**: [Lookup Table Type](Lookup-Table-Type.html).
- **Converted to**: None.

See [Type System](Type-System.html) for the complete conversion reference across all types.
{% endraw %}
