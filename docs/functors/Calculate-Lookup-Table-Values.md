---
title: "Calculate Lookup Table Values"
nav_order: 7
parent: "Lookup Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calculate Lookup Table Values

## Description

Generates a new lookup table by evaluating an expression once per row of a base lookup table. The keys of the output table are inherited unchanged from the base table; only the values are computed by the expression.

This is one of Dinamica EGO's five calculator functors. Use it to recompute the values of an existing lookup table row by row while keeping the same key structure; use [Calculate Lookup Table Keys And Values](Calculate-Lookup-Table-Keys-And-Values.html) instead when the keys also need to be recomputed. Its abbreviated (shorthand) syntax is `%`. See [Calculator functor shorthand](../EGO-Script.html#calculator-functor-shorthand) in the EGO Script documentation for the verbose and abbreviated forms, and [Calculate Functors — Complete Operator Documentation](../Calculate-Functors.html) for the full expression language reference.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Value Column Expression | [Image Expression Type](../types/Image-Expression-Type.html) | Expression evaluated once per row of Base Lookup Table; its result becomes that row's value in the output table. Must be enclosed in square brackets `[ ]` in EGO Script. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Key Column Name | [Name Type](../types/Name-Type.html) | Name of the key column in the resulting lookup table. If omitted, the corresponding name from the table used as format is used. | .none |
| Value Column Name | [Name Type](../types/Name-Type.html) | Name of the value column in the resulting lookup table. If omitted, the corresponding name from the table used as format is used. | .none |
| Base Lookup Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | Lookup table whose key set drives iteration. When not provided, the [Number Table](Number-Table.html) hook with the lowest list index that is connected to a lookup table (rather than a regular table) is used as the row source in the verbose form, or the first lookup table referenced by name in the expression in the abbreviated form — not a union of all connected tables. Prefer this port over a Number Table hook when the table is needed only to define the row set and is not referenced in the expression, to keep the abbreviated syntax available. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Lookup Table Type](../types/Lookup-Table-Type.html) | Lookup table with keys from Base Lookup Table and values computed by Value Column Expression. |

## Group

[Lookup Table](../Functor-List.html#lookup-table)

## Notes

### Connecting data inputs

Tables, lookup tables, and scalar values referenced in the expression must be connected to the functor's ports before writing the expression, using hook functors:

- Tables and lookup tables → [Number Table](Number-Table.html) → referenced in the expression as `t1`, `t2`, …, `t100`
- Scalar values → [Number Value](Number-Value.html) → referenced as `v1`, `v2`, …, `v100`

Maps cannot be connected — there is no cell context in this functor. In the abbreviated syntax, tables are referenced as `%variableName` and values as `$variableName`.

### Row iteration context

The expression is evaluated once per row of the base lookup table. Two keywords reflect the current row inside the expression:

- line — the key of the current row
- column — the value already associated with that key in the base lookup table

This allows the expression to read the row's existing value directly via column, and to look up related values from other connected tables using the current row's key — for example, `t1[line]` retrieves the value from table `t1` whose key matches the current row.

### Available expression features

Image operators (`iX`), neighbourhood functions, neighbourhood indexing, and convolution are not available — there is no spatial grid. Available features are arithmetic and logical operators, scalar references (`vX`), table and lookup table queries (`tX[...]`) in all single-key and multi-column forms, and the line and column row-context keywords. See [The Expression Language](../Calculate-Functors.html#the-expression-language) for the complete reference, or [Image Expression Type](../types/Image-Expression-Type.html) for the navigable operator index.

### Null value handling

Null propagation rules and defensive patterns are covered in [Null Value Handling](../Calculate-Functors.html#null-value-handling) in the Calculate Functors documentation.

See [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for techniques that combine the table and lookup table functors.

## Internal Name

CalculateLookupTableValues
{% endraw %}
