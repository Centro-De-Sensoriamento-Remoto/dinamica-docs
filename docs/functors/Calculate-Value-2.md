---
title: "Calculate Value 2"
nav_order: 5
parent: "Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calculate Value 2

## Description

Evaluates an algebraic or logical expression once and returns a single scalar value, in the same way as [Calculate Value](Calculate-Value.html), but performing all internal operations using double-precision reals throughout, rather than the precision defined by ImageExpression::Value.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Expression | [Image Expression Type](../types/Image-Expression-Type.html) | Algebraic or logical expression that evaluates to a single numeric result. Must be enclosed in square brackets `[ ]` in EGO Script. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Default Value | [Real Value Type](../types/Real-Value-Type.html) | Value returned if evaluating the expression produces an algebraic error. When not provided, evaluation errors are propagated. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Real Value Type](../types/Real-Value-Type.html) | The computed scalar value. |

## Group

[Table](../Functor-List.html#table)

## Notes

Tables, lookup tables, and scalar values referenced in the expression must be connected through hook functors before the expression is written: tables and lookup tables through [Number Table](Number-Table.html) (referenced as `t1`, `t2`, … in the verbose form), and scalar values through [Number Value](Number-Value.html) (`v1`, `v2`, …).

Maps cannot be connected to this functor, since it has no cell context.

See [Calculate Value](Calculate-Value.html) for further notes on syntax and available expression features, which apply equally to this functor.

## Internal Name

CalculateValue2
{% endraw %}
