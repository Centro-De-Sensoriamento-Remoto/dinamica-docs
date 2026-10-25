---
title: "Calculate Value 2"
nav_order: 5
parent: "Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calculate Value 2

## Description

**This functor is deprecated and should not be used.** Use [Calculate Value](Calculate-Value.html) instead.

It computes a single value by evaluating an algebraic or logical expression once, in the same way as [Calculate Value](Calculate-Value.html). The only difference is how the data used in the expression is connected: through hooks that identify it by name, instead of by number.

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

The data used in the expression is connected through [Name Table](Name-Table.html) and [Name Value](Name-Value.html) hooks placed inside this container. Each hook gives its data a name, and the expression refers to the data by that name, with the same prefixes used by the [calculator shorthand](../EGO-Script.html#calculator-functor-shorthand): a table or lookup table registered as `rates` is referenced as `%rates`, and a value registered as `threshold` as `$threshold`. The functors that replace this one use [Number Table](Number-Table.html) and [Number Value](Number-Value.html) hooks instead, which identify the data by number (`t1`, `v1`, …).

Maps cannot be connected to this functor, since it has no cell context.

See [Calculate Value](Calculate-Value.html) for the expression features, which apply equally to this functor.

See [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for techniques that combine the table and lookup table functors.

This functor is kept only so that older models that use it continue to load and run.

## Internal Name

CalculateValue2
{% endraw %}
