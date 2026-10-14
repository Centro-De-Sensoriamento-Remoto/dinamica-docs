---
title: "Calculate Value"
nav_order: 4
parent: "Table Functors"
grand_parent: "Functor List"
redirect_from:
  - /Calculate-Value.html
---
{% raw %}
# Calculate Value

## Description

Evaluates an algebraic or logical expression once and returns a single scalar value. Unlike the map and lookup table calculators, there is no current cell, row, or spatial grid: the expression is evaluated in a purely scalar context, drawing only on tables, lookup tables, and scalar values connected through hooks.

This is one of Dinamica EGO's five calculator functors. Its abbreviated (shorthand) syntax is `$`. See [Calculator functor shorthand](../EGO-Script.html#calculator-functor-shorthand) in the EGO Script documentation for the verbose and abbreviated forms, and [Calculate Functors — Complete Operator Documentation](../Calculate-Functors.html) for the full expression language reference.

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

### Connecting data inputs

Tables, lookup tables, and scalar values referenced in the expression must be connected to the functor's ports before writing the expression, using hook functors:

- Tables and lookup tables → [Number Table](Number-Table.html) → referenced in the expression as t1, t2, …, t100
- Scalar values → [Number Value](Number-Value.html) → referenced as v1, v2, …, v100

Maps cannot be connected — there is no cell context in this functor. In the abbreviated syntax, tables are referenced as `%variableName` and values as `$variableName`.

### Available expression features

Image operators (`iX`), the line and column spatial keywords, neighbourhood functions, neighbourhood indexing, and convolution are not available — there is no cell or row context. Available features are arithmetic and logical operators and table and lookup table queries (`tX[...]`) in all single-key and multi-column forms. See [The Expression Language](../Calculate-Functors.html#the-expression-language) for the complete reference, or [Image Expression Type](../types/Image-Expression-Type.html) for the navigable operator index.

All operations are performed using the precision defined by ImageExpression::Value; the final result is then converted to a double-precision real. See [Calculate Value 2](Calculate-Value-2.html) for a variant that instead performs all operations using double precision throughout.

### Null value handling

Null propagation rules and defensive patterns are covered in [Null Value Handling](../Calculate-Functors.html#null-value-handling) in the Calculate Functors documentation.

## Internal Name

CalculateValue

## Usage examples

- [CalculateValue practical examples](../Calculate-Functors.html) in the Calculate Functors documentation
- Lesson 8: Inserting and getting a specific value into a table
{% endraw %}
