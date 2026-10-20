---
title: "Calculate Lookup Table Keys And Values"
nav_order: 6
parent: "Lookup Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calculate Lookup Table Keys And Values

## Description

Generates a new lookup table by evaluating two separate expressions once per row of a base lookup table: one expression computes the output key, the other computes the output value. This allows a complete transformation of a table's key-value structure, or the construction of an entirely new lookup table row by row.

This is one of Dinamica EGO's five calculator functors. Use it when both the keys and the values of a lookup table need to be recomputed; use [Calculate Lookup Table Values](Calculate-Lookup-Table-Values.html) instead when only the values need to be recomputed and the keys should be inherited from the base table unchanged. Its abbreviated (shorthand) syntax is `%%`. See [Calculator functor shorthand](../EGO-Script.html#calculator-functor-shorthand) in the EGO Script documentation for the verbose and abbreviated forms, and [Calculate Functors — Complete Operator Documentation](../Calculate-Functors.html) for the full expression language reference.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Key Column Expression | [Image Expression Type](../types/Image-Expression-Type.html) | Expression evaluated once per row to produce the output key. Must be enclosed in square brackets `[ ]` in EGO Script. |
| Value Column Expression | [Image Expression Type](../types/Image-Expression-Type.html) | Expression evaluated once per row to produce the output value. Must be enclosed in square brackets `[ ]` in EGO Script. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Key Column Name | [Name Type](../types/Name-Type.html) | Name of the key column in the resulting lookup table. If omitted, the corresponding name from the table used as format is used. | .none |
| Value Column Name | [Name Type](../types/Name-Type.html) | Name of the value column in the resulting lookup table. If omitted, the corresponding name from the table used as format is used. | .none |
| Base Lookup Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | Lookup table whose row set drives iteration. When not provided, the [Number Table](Number-Table.html) hook with the lowest list index that is connected to a lookup table (rather than a regular table) is used as the row source in the verbose form, or the first lookup table referenced by name in the expression in the abbreviated form — not a union of all connected tables. Prefer this port over a Number Table hook when the table is needed only to define the row set and is not referenced in the expressions, to keep the abbreviated syntax available. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Lookup Table Type](../types/Lookup-Table-Type.html) | Lookup table whose keys and values were both computed by the respective expressions. |

## Group

[Lookup Table](../Functor-List.html#lookup-table)

## Notes

### Connecting data inputs

Tables, lookup tables, and scalar values referenced in either expression must be connected to the functor's ports before writing the expressions, using hook functors:

- Tables and lookup tables → [Number Table](Number-Table.html) → referenced in the expression as `t1`, `t2`, …, `t100`
- Scalar values → [Number Value](Number-Value.html) → referenced as `v1`, `v2`, …, `v100`

Maps cannot be connected — there is no cell context in this functor. In the abbreviated syntax, tables are referenced as `%variableName` and values as `$variableName`. Both expressions share the same set of connected operands.

### Row iteration context

Both expressions are evaluated once per row of the base lookup table. Two keywords reflect the current row inside each expression:

- line — the key of the current row
- column — the value already associated with that key in the base lookup table

If the key expression produces a key that already exists in the output table, the newly computed value replaces the existing one.

### Available expression features

Identical to [Calculate Lookup Table Values](Calculate-Lookup-Table-Values.html): arithmetic and logical operators, scalar references (`vX`), table and lookup table queries (`tX[...]`) in all single-key and multi-column forms, and the line and column row-context keywords are available. Image operators (`iX`), neighbourhood functions, neighbourhood indexing, and convolution are not available. See [The Expression Language](../Calculate-Functors.html#the-expression-language) for the complete reference, or [Image Expression Type](../types/Image-Expression-Type.html) for the navigable operator index.

### Null value handling

Null propagation rules and defensive patterns are covered in [Null Value Handling](../Calculate-Functors.html#null-value-handling) in the Calculate Functors documentation.

## Internal Name

CalculateLookupTableKeysAndValues
{% endraw %}
