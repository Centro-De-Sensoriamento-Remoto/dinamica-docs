---
title: "Calculate Lookup Table 2"
nav_order: 5
parent: "Lookup Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calculate Lookup Table 2

## Description

**This functor is deprecated and should not be used.** Use [Calculate Lookup Table Values](Calculate-Lookup-Table-Values.html) or [Calculate Lookup Table Keys And Values](Calculate-Lookup-Table-Keys-And-Values.html) instead.

It computes a lookup table by evaluating an algebraic or logical expression once for every key of a format lookup table, in the same way as [Calculate Lookup Table Values](Calculate-Lookup-Table-Values.html). The only difference is how the data used in the expression is connected: through hooks that identify it by name, instead of by number.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Expression | [Image Expression Type](../types/Image-Expression-Type.html) | Algebraic or logical expression used to compute each output value. Must be enclosed in square brackets `[ ]` in EGO Script. |
| Format | [Lookup Table Type](../types/Lookup-Table-Type.html) | Lookup table whose keys define the format (and, by default, the key and value column names) of the output. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Key Name | [Name Type](../types/Name-Type.html) | Name given to the output's key column. If omitted, the corresponding name from Format is used. This is an advanced port. | .none |
| Value Name | [Name Type](../types/Name-Type.html) | Name given to the output's value column. If omitted, the corresponding name from Format is used. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Lookup Table Type](../types/Lookup-Table-Type.html) | Computed output lookup table. |

## Group

[Lookup Table](../Functor-List.html#lookup-table)

## Notes

The data used in the expression is connected through [Name Table](Name-Table.html) and [Name Value](Name-Value.html) hooks placed inside this container. Each hook gives its data a name, and the expression refers to the data by that name, with the same prefixes used by the [calculator shorthand](../EGO-Script.html#calculator-functor-shorthand): a table or lookup table registered as `rates` is referenced as `%rates`, and a value registered as `threshold` as `$threshold`. The functors that replace this one use [Number Table](Number-Table.html) and [Number Value](Number-Value.html) hooks instead, which identify the data by number (`t1`, `v1`, …).

For example, this call copies the values of the lookup table registered as `table`:

```
result := CalculateLookupTable2 [ %table[line] ] formatTable {{
    NameTable formatTable "table";
}};
```

All operations are performed using the precision defined by ImageExpression::Value; the final result is then converted to LookupTable::Value.

See [Calculate Lookup Table Values](Calculate-Lookup-Table-Values.html) for the expression features, which apply equally to this functor.

See [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for techniques that combine the table and lookup table functors.

This functor is kept only so that older models that use it continue to load and run.

## Internal Name

CalculateLookupTable2
{% endraw %}
