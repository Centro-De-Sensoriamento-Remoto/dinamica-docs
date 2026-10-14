---
title: "Percent Type"
nav_order: 12
parent: "Type System"
grand_parent: "Core Concepts"
redirect_from:
  - /Percent-Type.html
---
{% raw %}
# Percent Type

A Percent value represents a fraction or ratio. [Genetic Algorithm Tool](../functors/Genetic-Algorithm-Tool.html) uses it for its `convergenceLimit` input, the percentage of fitness variation across generations used to decide when to halt optimization, and for `metaHeuristicEvaluationPercent`, the percentage of individuals whose fitness is estimated by meta-heuristic evaluation rather than computed directly.

## GUI Editor

The percent editor accepts a plain numeric value; it does not accept the `%` suffix available in EGO Script.

## EGO Script

A Percent constant can be written in [EGO Script](../EGO-Script.html) as either a plain fraction between 0 and 1, or as a number followed by `%` between 0 and 100. The two forms are interchangeable — `0.3456` and `34.56%` represent the same value:

```
0.3456
0.0134
0.0054
```

```
34.56%
1.34%
0.54%
```

## Automatic Conversions

- **Converted from**: [Real Value Type](Real-Value-Type.html).
- **Converted to**: None.

See [Type System](../Type-System.html) for the complete conversion reference across all types.
{% endraw %}
