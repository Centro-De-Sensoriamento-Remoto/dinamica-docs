---
title: "Neighborhood Table Type"
nav_order: 38
parent: "Type System"
grand_parent: "Core Concepts"
redirect_from:
  - /Neighborhood-Table-Type.html
---
{% raw %}
# Neighborhood Table Type

A Neighborhood Table defines a weight between pairs of locations — for example, how strongly one spatial feature influences another. [Calc Neighborhood](../functors/Calc-Neighborhood.html) computes one directly from a [Categorical Map](Categorical-Map-Type.html), identifying each non-null feature's neighbors within a search window and weighting them by adjacency, without needing the data built by hand.

## GUI Editor

Neighborhood Table Type has no dedicated editor of its own — its carrier functor's input cannot be represented by a constant. A value is obtained either directly, from a functor such as [Calc Neighborhood](../functors/Calc-Neighborhood.html), or through the automatic conversion described below.

## EGO Script

For the same reason, Neighborhood Table Type has no literal constant syntax in [EGO Script](../EGO-Script.html) — see [Constants](../EGO-Script.html#constants). A Neighborhood Table is obtained either by calling a functor that produces one directly, such as [Calc Neighborhood](../functors/Calc-Neighborhood.html), or through the automatic conversion from [Table](Table-Type.html) or [Elevation Graph](Elevation-Graph-Type.html) described below.

## Automatic Conversions

- **Converted from**: [Table Type](Table-Type.html) — the table must have the columns `Neighbor1*` (Real), `Neighbor2*` (Real), and `Weight` (Real). [Elevation Graph Type](Elevation-Graph-Type.html).
- **Converted to**: [Table Type](Table-Type.html), using that same column layout.

See [Type System](../Type-System.html#table-format-of-table-shaped-types) for the shared table-format pattern this type's conversions follow, and for the complete conversion reference across all types.
{% endraw %}
