---
title: "Calculate Functors — Complete Operator Documentation"
nav_order: 4
parent: "Language and Expressions"
---
{% raw %}
# Calculate Functors — Complete Operator Documentation

---

# Overview

Dinamica EGO provides a family of five **calculator functors** that evaluate an algebraic or logical expression and return a result of a specific type. All five share the same underlying **Image Expression Language**, but they differ in what they output, how many expressions they accept, and which language features are available in each context.

| Functor | EGO Script Shorthand | Output Type | Evaluation context |
| --- | --- | --- | --- |
| [Calculate Map](functors/Calculate-Map.html) | `#` | Raster map (continuous) | Once per cell across a spatial grid |
| [Calculate Categorical Map](functors/Calculate-Categorical-Map.html) | `##` | Raster map (categorical) | Once per cell across a spatial grid |
| [Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html)[^8150] | `#*` | Struct of raster maps (continuous), one per field | Once per cell across a spatial grid |
| [Calculate Value](functors/Calculate-Value.html) | `$` | Single scalar value | Once, with no spatial or row context |
| [Calculate Lookup Table Values](functors/Calculate-Lookup-Table-Values.html) | `%` | Lookup table (values computed) | Once per row of a base lookup table |
| [Calculate Lookup Table Keys And Values](functors/Calculate-Lookup-Table-Keys-And-Values.html) | %% | Lookup table (keys and values computed) | Once per row — two separate expressions |

[Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html) is a variant of Calculate Map that evaluates a struct expression, `{ name: expression, ... }`, and returns one map for each field in a single [Struct](types/Struct-Type.html). Its shorthand symbol is `#*`, and it is described in its [own section](#calculatemultiplemaps). Except where noted, everything stated for Calculate Map applies to it.[^8150]

The shorthand symbols are also referred to as **abbreviated syntax** — both terms mean the same thing and are used interchangeably in this documentation and in the Dinamica EGO GUI options.

The expression language, including all arithmetic, logical, conditional, spatial, and stochastic operators, is described in full in [The Expression Language](#the-expression-language) section. Per-functor restrictions and the availability of each operator category are noted both in each functor's own section and in the relevant expression-language subsections. For a complete description of the EGO Script syntax used to call these functors — including the shorthand symbols, hook blocks, and conversion between forms — see [Calculator functor shorthand](EGO-Script.html#calculator-functor-shorthand) in the EGO Script documentation.

---

# Functor Reference

## CalculateMap (`#`)

[Calculate Map](functors/Calculate-Map.html) computes a new **continuous raster map** cell by cell using an algebraic or logical expression. The expression is evaluated independently for every cell in the output map. The result is always computed as a real (floating-point) value and then converted to the output map's chosen cell type.

When an expression references more than one connected map, all of them are evaluated at the same current cell. The connected maps do not need matching extent, resolution, or pixel dimensions beforehand — Dinamica EGO reconciles this automatically at runtime through image virtualization — but they do need to share the same projection. See [Co-located evaluation](#4-image-operators-and-functions) in section 4 for details.

### Inputs and Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| Expression | Image Expression Type | **Yes** | — | The algebraic or logical formula used to compute each output cell. |
| Cell Type | Cell Type Type | No | Signed 32-bit Integer | Data type for each output cell (e.g., byte, int16, float32). |
| Null Value | Null Value Type | No | Based on Cell Type | Sentinel value representing "no data" in the output. |
| Result Is Sparse | Boolean Value Type | No | False | If `True`, only non-null cells are stored — saves memory but slows random access. |
| Result Format | Map Type | No | None | Optional reference map whose spatial format (extent, resolution, projection) is applied to the output. Category information in the reference map is ignored. Prefer this port over a `NumberMap` hook when the map is needed only for format purposes — a hook defines an identifier in the expression namespace and blocks abbreviated syntax if that identifier is unused in the expression. |

### Output

| Name | Type | Description |
| --- | --- | --- |
| Result | Map Type | The computed output map. |

### Available expression features

All expression language features are available: image operators (`iX`, `iX[line,col]`, `iX[[line,col]]`[^8150]), the `line` and `column` spatial keywords, lookup table operators ([section 5](#5-lookup-table-operators)), multi-column table operators ([section 6](#6-multi-column-table-operators)), neighbourhood functions (`nbMin`, `nbMax`, `nbAverage`, etc. — [section 7](#7-image-neighborhood-functions)), neighbourhood indexing (`nbMinRef`, `nbMaxRef` — [section 8](#8-image-neighborhood-indexing-functions)), and the convolution operator (`nbConvol` — [section 9](#9-convolution-operator)).

---

## CalculateCategoricalMap (`##`)

Computes a new **categorical raster map** using an expression. Functionally identical to [Calculate Map](functors/Calculate-Map.html) — the same inputs, parameters, and expression language apply — but the output is typed as a **categorical map**, which preserves category semantics for downstream functors that distinguish categorical maps from continuous maps (e.g., [Calc Areas](functors/Calc-Areas.html), [For Each Category](functors/For-Each-Category.html)).

Use [Calculate Categorical Map](functors/Calculate-Categorical-Map.html) when the expression produces integer class codes rather than measured or continuous values. A common pattern is reclassifying a continuous map into discrete categories based on thresholds.

### Inputs and Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| Expression | Image Expression Type | **Yes** | — | The formula used to compute each output cell's category code. |
| Cell Type | Cell Type Type | No | Signed 32-bit Integer | Data type for each output cell. |
| Null Value | Null Value Type | No | Based on Cell Type | Sentinel value representing "no data" in the output. |
| Result Is Sparse | Boolean Value Type | No | False | If `True`, only non-null cells are stored. |
| Result Format | Map Type | No | None | Optional reference map whose spatial format is applied to the output. Prefer this port over a `NumberMap` hook when the map is needed only for format purposes — a hook defines an identifier in the expression namespace and blocks abbreviated syntax if that identifier is unused in the expression. |

### Output

| Name | Type | Description |
| --- | --- | --- |
| Result | Categorical Map Type | The computed categorical output map. |

### Available expression features

Identical to [Calculate Map](functors/Calculate-Map.html): all operators, spatial keywords, neighbourhood functions, indexing functions, and convolution are available.

---

## CalculateMultipleMaps

[Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html) computes several **continuous raster maps** in one pass. Its expression is a [struct expression](#struct-expressions) whose fields are evaluated once for every cell; each field produces one output map. Local variables declared with `let ... in` around the struct are calculated once per cell and shared by all fields, and every input map is read once per cell.[^8150]

Its shorthand symbol is `#*`.[^8150]

### Inputs and Parameters

The inputs are the same as those of [Calculate Map](functors/Calculate-Map.html), except that the expression must be a struct expression and that Cell Type, Null Value, Result Is Sparse and Result Format apply to all the output maps.

### Output

| Name | Type | Description |
| --- | --- | --- |
| Result | Struct Type | Struct containing one map for each field of the expression, stored under the name of the field. Use [Extract Struct Map](functors/Extract-Struct-Map.html) to retrieve a map. |

### Available expression features

Same as [Calculate Map](functors/Calculate-Map.html). The calculation always runs on the processors.

---

## CalculateValue (`$`)

Evaluates an expression **once** and returns a single **scalar value**. Because there is no current cell, row, or spatial grid, all image-based and neighbourhood operators are unavailable.

[Calculate Value](functors/Calculate-Value.html) is used to compute a single parameter — such as a global threshold, a weighted sum of scalar inputs, or a value derived from a table — that can then be passed as input to other functors.

### Inputs and Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| Expression | Image Expression Type | **Yes** | — | An expression that evaluates to a single numeric result. |

### Output

| Name | Type | Description |
| --- | --- | --- |
| Result | Value Type | The computed scalar value. |

### Available expression features

**Available:** all arithmetic and logical operators (sections [1](#1-general-operators) and [2](#2-general-functions)), scalar value references (`vX`), and lookup table queries (`tX[...]`) in all single-key and multi-column forms ([section 5](#5-lookup-table-operators), [section 6](#6-multi-column-table-operators)).

**Not available:** image operators (`iX`, `iX[line,col]`, `iX[[line,col]]`[^8150]), the `line` and `column` spatial keywords, neighbourhood functions, neighbourhood indexing functions, and the convolution operator. These all require a cell or row context that does not exist in [Calculate Value](functors/Calculate-Value.html).

---

## CalculateLookupTableValues (`%`)

[Calculate Lookup Table Values](functors/Calculate-Lookup-Table-Values.html) evaluates an expression **once per row** of a base lookup table and writes the computed result as the **value** for that row in the output lookup table. The **keys** of the output table are inherited from the base table and are not recomputed.

When the base lookup table argument is `.none`, the row set is not a union of all connected tables. Instead it comes from a single connected lookup table: in the verbose form, this is the lookup table connected via the `NumberTable` port with the lowest index (e.g. `t1` rather than `t2`); in the shorthand form, it is the first lookup table referenced by name in the expression.

### Inputs and Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| Expression | Image Expression Type | **Yes** | — | Formula evaluated for each row. The result becomes the value for that row's key in the output table. |
| Key Column Name | String | **Yes** | — | Name of the key column in the output lookup table. |
| Value Column Name | String | **Yes** | — | Name of the value column in the output lookup table. |
| Base Lookup Table | Lookup Table Type | No | `.none` | A lookup table whose key set drives iteration. When `.none`, the `NumberTable` hook with the lowest list index that is connected to a **lookup table** (not a regular table) is used as the row source (verbose form), or the first lookup table named in the expression (shorthand form) — not a union of all connected tables. Prefer this port over a `NumberTable` hook when the table is needed only to define the row set and is not referenced in the expression, to keep abbreviated syntax available. |

### Output

| Name | Type | Description |
| --- | --- | --- |
| Result | Lookup Table Type | A lookup table with keys from the base table and values computed by the expression. |

### The `line` and `column` keywords in a row-iteration context

Within the expression, **`line` refers to the key of the current row** being iterated, not a spatial row index, and **`column` refers to the value already associated with that key** in the base lookup table — the row's own existing value, available without looking it up explicitly. This allows the expression to read the row's current value directly via `column`, and to look up related values from *other* connected tables using the current row's key: for example, `t1[line]` retrieves the value in table `t1` whose key matches the row currently being computed.

### Available expression features

**Available:** arithmetic and logical operators (sections [1](#1-general-operators) and [2](#2-general-functions)), scalar references (`vX`), lookup table queries (`tX[...]`) in all single-key and multi-column forms ([section 5](#5-lookup-table-operators), [section 6](#6-multi-column-table-operators)), `line` (as the current row key), and `column` (as the current row's value in the base lookup table).

**Not available:** `iX`, `iX[line,col]`, `iX[[line,col]]`[^8150], neighbourhood functions, neighbourhood indexing, and convolution. There is no spatial grid.

---

## CalculateLookupTableKeysAndValues (`%%`)

[Calculate Lookup Table Keys And Values](functors/Calculate-Lookup-Table-Keys-And-Values.html) evaluates **two separate expressions** per row of a base lookup table — one for the **key** and one for the **value** — and writes both into the output lookup table. This allows complete transformation of a table's key-value structure, or construction of an entirely new lookup table row by row.

### Inputs and Parameters

| Name | Type | Required | Default | Description |
| --- | --- | --- | --- | --- |
| Key Column Expression | Image Expression Type | **Yes** | — | Formula evaluated for each row to produce the output key. |
| Value Column Expression | Image Expression Type | **Yes** | — | Formula evaluated for each row to produce the output value. |
| Key Column Name | String | **Yes** | — | Name of the key column in the output lookup table. |
| Value Column Name | String | **Yes** | — | Name of the value column in the output lookup table. |
| Base Lookup Table | Lookup Table Type | No | `.none` | A lookup table whose row set drives iteration. Prefer this port over a `NumberTable` hook when the table is needed only to define the row set and is not referenced in the expression, to keep abbreviated syntax available. |

### Output

| Name | Type | Description |
| --- | --- | --- |
| Result | Lookup Table Type | A lookup table with both keys and values computed by the respective expressions. |

### Available expression features

Same as [Calculate Lookup Table Values](functors/Calculate-Lookup-Table-Values.html): `line` represents the key of the current row in the base table, and `column` represents the value already associated with that key; `vX` and `tX[...]` are available (sections [5](#5-lookup-table-operators) and [6](#6-multi-column-table-operators)); spatial and image operators are not. Both the key expression and the value expression share the same set of connected operands.

---

# Connecting Data Inputs

All data referenced in any expression must be connected to the functor's ports before writing the expression. This is done through **hook** functors — [Number Map](functors/Number-Map.html), [Number Table](functors/Number-Table.html), and [Number Value](functors/Number-Value.html) — which bind a connected data source to a numbered identifier used inside the expression. The same port types apply across all the calculator functors:

- **Maps** are connected via a [Number Map](functors/Number-Map.html) hook → referenced as `i1`, `i2`, …, `i100`
- **Tables and lookup tables** are connected via a [Number Table](functors/Number-Table.html) hook → referenced as `t1`, `t2`, …, `t100`
- **Scalar values** are connected via a [Number Value](functors/Number-Value.html) hook → referenced as `v1`, `v2`, …, `v100`

> **Tip:** Give every connected functor a descriptive alias. The expression editor lists all available identifiers with their aliases at the top, making complex models much easier to read and maintain. The alias is also what generates the functor's variable name, and that variable name is exactly what the shorthand notation references: a map aliased `regions`, for example, is bound to the variable `regions` and is then referenced in a shorthand expression as `#regions`, a table or lookup table as `%regions`, and a value as `$regions`. See [Calculator functor shorthand](EGO-Script.html#calculator-functor-shorthand) for details on the shorthand notation.

> **Note:** Map hook connections (`NumberMap` / `iX`) are only meaningful in [Calculate Map](functors/Calculate-Map.html), [Calculate Categorical Map](functors/Calculate-Categorical-Map.html) and [Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html). In [Calculate Value](functors/Calculate-Value.html), [Calculate Lookup Table Values](functors/Calculate-Lookup-Table-Values.html), and [Calculate Lookup Table Keys And Values](functors/Calculate-Lookup-Table-Keys-And-Values.html) there is no cell context, and `iX` references cannot be used in the expression.

---

# The Expression Language

The expression is written in Dinamica EGO's **Image Expression Language** — a concise algebra where every term operates on the current evaluation unit (a cell, a table row, or nothing, depending on the functor). The language has eight categories of operators and functions described below.

Unless a restriction is noted, every operator is available in all five calculator functors.

Every construct in the language — including a conditional — is itself just an expression that resolves to one value, and any expression can appear anywhere another one is expected. This makes conditionals freely composable: two `if...then...else` results can be summed directly, a conditional's own test can be replaced with another conditional, and so on, without any special syntax for combining them. For example, `if (if i1 > 0 then 1 else i2) then i2 else 1 + i3` nests one conditional inside another's test.

## Identifier Syntax

| Symbol | Refers to | Available in |
| --- | --- | --- |
| `iX` | Value of map X at the current cell | [Calculate Map](functors/Calculate-Map.html), [Calculate Categorical Map](functors/Calculate-Categorical-Map.html) and [Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html) only |
| `tX` | Connected table or lookup table X (used with a bracket operator) | All five functors |
| `vX` | Connected scalar value X | All five functors |
| `line` | Spatial row index of the current cell, **starting at 1** *(map calculators)* **or** key of the current row *(table calculators)* | All except [Calculate Value](functors/Calculate-Value.html) |
| `column` | Spatial column index of the current cell, **starting at 1** *(map calculators)* **or** value associated with the current row's key *(table calculators)* | All except [Calculate Value](functors/Calculate-Value.html) |
| `_name`[^8150] | Local variable introduced by a `let ... in` expression. The name starts with a letter or `_` and continues with letters, digits or `_`, and is case insensitive. It never collides with a function, a constant or an operand: none of them starts with `_`, and in the concise notation maps, tables and values are prefixed with `#`, `%` and `$`. | All calculator functors |

X ranges from 1 to 100. In logical expressions, **zero is false** and any non-zero value is true.

---

# 1. General Operators

The table below lists all infix and prefix operators in **descending precedence order** (highest precedence = evaluated first). All operators are available in all five calculator functors.

| Precedence | Operator | Syntax | Description | Example |
| --- | --- | --- | --- | --- |
| 1 | **Conditional** | `if EXPR then EXPR else EXPR` | Evaluates to the second expression if the condition is true, otherwise the third. Can be nested. | `if i1 > 0 then i1 else 0` |
| 1 | **Local Variables** | `let _a: EXPR, _b: EXPR in EXPR` | Binds one or more local variables and evaluates the body with them in scope. See [Local Variables](#local-variables-let--in). | `let _a: i1 * 2 in _a + _a ^ 2` |
| 2 | **Boolean Or** | `EXPR or EXPR` / `EXPR \|\| EXPR` | True if either argument is true. **Short-circuit evaluated** — the right side is skipped if the left is already true. | `isNull(i1) \|\| i1 > 100` |
| 2 | **Boolean And** | `EXPR and EXPR` / `EXPR && EXPR` | True only if both arguments are true. **Short-circuit evaluated** — the right side is skipped if the left is already false. | `not isNull(i1) and i1 > 0` |
| 3 | **Equal** | `EXPR = EXPR` / `EXPR == EXPR` | True if both sides are equal. | `i1 == 2` |
| 3 | **Not Equal** | `EXPR != EXPR` / `EXPR /= EXPR` / `EXPR <> EXPR` | True if both sides differ. | `i1 != 0` |
| 4 | **Greater Than** | `EXPR > EXPR` |  | `i1 > i2` |
| 4 | **Greater Than Or Equal** | `EXPR >= EXPR` |  | `i1 >= v1` |
| 4 | **Less Than** | `EXPR < EXPR` |  | `i1 < 100` |
| 4 | **Less Than Or Equal** | `EXPR <= EXPR` |  | `i1 <= i2` |
| 5 | **Add** | `EXPR + EXPR` |  | `i1 + i2` |
| 5 | **Subtract** | `EXPR - EXPR` |  | `i1 - i2` |
| 6 | **Multiply** | `EXPR * EXPR` |  | `i1 * 2.5` |
| 6 | **Divide** | `EXPR / EXPR` |  | `i1 / i2` |
| 6 | **Modulo** | `EXPR % EXPR` | Remainder after integer division | `i1 % 100` |
| 7 | **Power** | `EXPR ^ EXPR` | Exponentiation | `i1 ^ 3` |
| 8 | **Catch Error (`?`)** | `EXPR ? EXPR` | If the left expression produces an algebraic error (division by zero, key not found, etc.), evaluate and return the **fallback expression** instead. The fallback can be any expression, including another calculation, a conditional, or a nested `?`. | `(i1 / i2) ? (i1 - i2)` |
| 9 | **Boolean Not** | `not EXPR` / `! EXPR` | Inverts a boolean value. | `not isNull(i1)` |
| 9 | **Negate** | `-EXPR` | Arithmetic negation. | `-ceil(i1 + i2)` |

## Local Variables (`let ... in`)

A `let` expression gives names to intermediate results so they can be reused without repeating the sub-expression:[^8150]

```
let _ndvi: (i1 - i2) / (i1 + i2),
    _scaled: _ndvi * 100,
in if _ndvi > 0.3 then _scaled else 0
```

- Bindings are separated by commas; a trailing comma before `in` is allowed.
- Each binding is evaluated **once per evaluation unit**, in order, and can use the variables bound before it. A variable cannot be used in its own binding.
- A variable is visible only inside the `let` that declares it (its later bindings and its body). A nested `let` can declare a variable with the same name as an outer one; the inner one hides the outer one.
- A `let` is an ordinary expression: it can be used as a function argument, as an operand (inside parentheses) or inside another `let`. The body extends as far to the right as possible.
- All bindings are evaluated even when the body does not use them, so there is no short-circuit. A binding that results in null makes the variable null; use `isNull(_a)` to test it.
- Stochastic functions are drawn once per binding: `let _r: rand in _r - _r` is always 0.

## Struct Expressions

A struct expression produces several results from a single evaluation. It is a list of named fields between braces:[^8150]

```
{ ndvi: (i1 - i2) / (i1 + i2), mask: if i1 > i2 then 1 else 0 }
```

- Each field is a name and an expression separated by `:`. Fields are separated by commas; a trailing comma before `}` is allowed. At least one field is required.
- A field name starts with a letter or `_` and continues with letters, digits or `_`. Names are case insensitive and must be unique within the struct. They have no sigil, because they are never referenced inside the expression; they are the names under which the results are returned.
- A struct is accepted only as the whole expression, or as the body of a `let ... in` that is the whole expression. This includes a `let` whose body is another `let`. A struct cannot be a function argument, an operand, a branch of `if ... then ... else`, the body of a `let` that is not at the top of the expression, or a field of another struct. A field can itself contain a `let ... in` that produces a single value.
- Variables declared by the `let` around the struct are visible to every field and are calculated once per evaluation, however many fields use them:

  ```
  let _ndvi: (i1 - i2) / (i1 + i2) in
  { ndvi: _ndvi, scaled: _ndvi * 100, mask: if _ndvi > 0.3 then 1 else 0 }
  ```

- Fields are evaluated in the order written and cannot refer to each other. A value needed by more than one field is declared with `let`.
- Each field has its own result. When the evaluation of a field results in null or an algebraic error, only that result is null; a field that uses a null local variable is null.
- Only [Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html) accepts a struct expression, and it accepts nothing else. The other calculator functors report an error if their expression is a struct.

---

# 2. General Functions

## Mathematical Functions

All mathematical functions are available in all five calculator functors.

| Function | Syntax | Description | Example |
| --- | --- | --- | --- |
| Square Root | `sqrt(EXPR)` |  | `sqrt(i1 / i4)` |
| Sin | `sin(EXPR)` | Sine; input in radians | `sin(i1 / i4)` |
| Cos | `cos(EXPR)` | Cosine; input in radians | `cos(i1 + i2)` |
| Tan | `tan(EXPR)` | Tangent; input in radians | `tan(i1 * i5 + 6)` |
| Acos | `acos(EXPR)` | Arccosine; output in radians | `acos(i1 + i2)` |
| Asin | `asin(EXPR)` | Arcsine; output in radians | `asin(i1 + i2)` |
| Atan | `atan(EXPR)` | Arctangent; output in radians | `atan(i1 + i2)` |
| Exp | `exp(EXPR)` | Natural exponential (e^x) | `exp(i1 + i2)` |
| Natural Logarithm | `ln(EXPR)` | log base e | `ln(i1 / i4)` |
| Log base 10 | `log(EXPR)` |  | `log(i1 / i4)` |
| Absolute Value | `abs(EXPR)` |  | `abs(i1 + i2)` |
| Ceiling | `ceil(EXPR)` | Smallest integer >= value | `ceil(i1 + i2)` |
| Floor | `floor(EXPR)` | Largest integer \<= value | `floor(i1 + i2)` |
| Round | `round(EXPR)` | Round to nearest integer | `round(i1 / i4)` |
| Maximum | `max(EXPR, EXPR)` | Greater of two values | `max(i1, i2)` |
| Minimum | `min(EXPR, EXPR)` | Lesser of two values | `min(i1, i4)` |
| Signal | `signal(EXPR)` | Returns +1 if positive, -1 if negative, 0 if zero | `signal(i1 - 4)` |
| Pi | `pi` | The constant pi (3.14159265358979323846) | `i1 * pi / 180` |

## Clamping Functions

All clamping functions are available in all five calculator functors.

| Function | Syntax | Description | Example |
| --- | --- | --- | --- |
| Clamp | `clamp(EXPR, EXPR_MIN, EXPR_MAX)` | Constrains a value to \[min, max\]. Equivalent to: `if EXPR < MIN then MIN else if EXPR > MAX then MAX else EXPR` | `clamp(v1, 1, 12)` |
| ClampMod | `clampMod(EXPR, EXPR_MIN, EXPR_MAX)` | Like clamp, but wraps around using modulo when the value is outside the range. Useful for cyclic quantities such as years or angles. Approximately: `(EXPR - MIN) % (MAX - MIN + 1) + MIN` | `clampMod(v1, 2010, 2054)` |

## Random / Stochastic Functions

All stochastic functions are available in all five calculator functors. They generate a new random sample **for each evaluation unit** each time the expression is evaluated. In [Calculate Map](functors/Calculate-Map.html) and [Calculate Categorical Map](functors/Calculate-Categorical-Map.html), this means one sample per cell, making them suitable for spatially stochastic models. In [Calculate Lookup Table Values](functors/Calculate-Lookup-Table-Values.html) and [Calculate Lookup Table Keys And Values](functors/Calculate-Lookup-Table-Keys-And-Values.html), one sample is drawn per table row. In [Calculate Value](functors/Calculate-Value.html), a single sample is drawn for the whole expression.

| Function | Syntax | Description | Example |
| --- | --- | --- | --- |
| Uniform (0-1) | `rand` | Generates a random value uniformly in \[0, 1). Used as a keyword, not a function call. | `if rand > 0.5 then 1 else i2` |
| Uniform (bounded) | `rUniform(EXPR_MIN, EXPR_MAX)` | Generates a random value uniformly between the given bounds. | `if rUniform(12, 15) > 14 then 1 else i2` |
| Normal | `rNormal(EXPR_MEAN, EXPR_STDDEV)` | Generates a random value from a Normal (Gaussian) distribution with the given mean and standard deviation. | `if rNormal(10, 2) > 9 then 1 else i2` |
| Poisson | `rPoisson(EXPR_LAMBDA)` | Generates a random integer from a Poisson distribution with the given lambda. | `if rPoisson(100) > 95 then 1 else i2` |

## Control Functions

| Function | Syntax | Description | Example |
| --- | --- | --- | --- |
| Literal value | `2`, `-3.5e-2`, etc. | Any numeric literal, including scientific notation. Available in all five calculator functors. | `2 + i1 / -3.5e-2` |
| Abort | `abort` | Immediately halts model execution. Useful as a guard inside a conditional to catch unexpected states. Available in all five calculator functors. | `if i1 > 0 then i1 * i2 + 4 else abort` |
| Is Null | `isNull(EXPR)` | Returns 1 if the expression is null, 0 otherwise. Immune to the null poisoning rule — always resolves to 0 or 1. Available in all five calculator functors. | `if not isNull(i1) then i1 else i2` |
| Null | `null` | Makes the current evaluation unit null — the cell, row, or scalar result is marked as missing and any further arithmetic using it propagates null. This is an **abstract** null, not a numeric value; it cannot be used in arithmetic and has no numeric representation. Available in all five calculator functors. | `if i1 > 2 then i1 else null` |

> **Note on null and equality:** Writing `i1 == null` does **not** test for null — because null participates in no arithmetic comparison, it always produces null itself, poisoning the expression. Always use `isNull(i1)` instead. See the [Null Value Handling](#null-value-handling) section for full details.

---

# 3. Value Operators

Available in all five calculator functors.

| Operator | Syntax | Description | Example |
| --- | --- | --- | --- |
| Get Variable Value | `vX` | Returns the scalar (constant) value connected to port X. | `v1 + t1[v2 + 4]` |

---

# 4. Image Operators and Functions

> **Availability:** [Calculate Map](functors/Calculate-Map.html) and [Calculate Categorical Map](functors/Calculate-Categorical-Map.html) only. These operators require a cell context that does not exist in [Calculate Value](functors/Calculate-Value.html), [Calculate Lookup Table Values](functors/Calculate-Lookup-Table-Values.html), or [Calculate Lookup Table Keys And Values](functors/Calculate-Lookup-Table-Keys-And-Values.html).
>
> **Exception:** `line` and `column` are also available in the two lookup table calculators, where they take on row-oriented meanings instead of spatial ones: `line` is the key of the current row, and `column` is the value associated with that key in the base lookup table being iterated.

| Operator | Syntax | Description | Example |
| --- | --- | --- | --- |
| Get Image Value | `iX` | Returns the value of image X at the **current cell**. | `i2` |
| Get Image Value At Location | `iX[LINE_EXPR, COL_EXPR]` | Returns the value of image X at the **specified (line, column) coordinate**. Coordinates outside the image boundary are **mirrored** back into range. For a row coordinate `cellLine` in an image of N rows, `cellLine` is normally expected to be in the range \[1, N\]. When `cellLine` is outside this range, it is mirrored back: if `cellLine` ≤ 0, the effective row is `1 − cellLine` (for instance, `cellLine` = 0 → row 1, `cellLine` = −1 → row 2, `cellLine` = −2 → row 3); if `cellLine` > N, the effective row is `2N + 1 − cellLine` (for instance, `cellLine` = N+1 → row N, `cellLine` = N+2 → row N−1, `cellLine` = N+3 → row N−2). The same formula applies independently to the column coordinate `cellCol`. If the target cell is null, **returns 0** (not null). | `i1[line - 1, column - 2]` |
| Get Image Value At Location (null-preserving)[^8150] | `iX[[LINE_EXPR, COL_EXPR]]` | Same as `iX[LINE_EXPR, COL_EXPR]` (1-indexed coordinates, out-of-bounds coordinates mirrored back into range), except that **returns null** when the target cell is null. The null propagates through the rest of the expression like any other null value. It is accepted wherever `iX[LINE_EXPR, COL_EXPR]` is. | `i1[[line - 1, column]]` |
| Get Image Null Sentinel Value | `null(iX)` | Returns the **numeric sentinel value** stored in image X to represent missing data (e.g. −1, 32767, or any other number defined when the image was created). Unlike the abstract `null` keyword, this is a real number that participates normally in arithmetic — but be aware that using it as if it were a regular data value may produce misleading results. | `if null(i2) > 2 then 1 else null` |
| Get Line Number | `line` | In map calculators: returns the **row index** of the current cell, **counting from 1**. In lookup table calculators: returns the **key of the current row**. | `line + 1` |
| Get Column Number | `column` | In map calculators: returns the **column index** of the current cell being processed, **counting from 1**. In lookup table calculators: returns the **value associated with the key of the current row** in the base lookup table. | `if column / 2 > 50 then 1 else null` |

> **Co-located evaluation.** When an expression references more than one map (`i1`, `i2`, …), the **current cell is shared**: every `iX` is evaluated at the same `line` and `column` for each step of the calculation, so `i1` and `i2` always refer to the same spatial location, not just "image 1" and "image 2" in some generic sense. The connected maps do **not** need to have matching extent, resolution, or pixel dimensions beforehand — Dinamica EGO reconciles this automatically through **image virtualization**: each input map is transparently wrapped in a virtual version sharing a common extent and the highest resolution among the inputs, so that "the current cell" lines up to the same point on the ground across all of them. The one requirement that virtualization does *not* relax is **projection** — all maps given to the calculator at the same time must share the same projection. `iX[LINE_EXPR, COL_EXPR]` breaks the shared-cell default, letting an expression sample a given image at an explicit coordinate instead of the current cell.

> **`line` and `column`** in map calculators are invaluable for creating geometric masks, distance ramps, or for passing precise coordinates into `iX[LINE, COL]` lookups. Both are **1-indexed** — the top-left cell of the map is at `line = 1, column = 1`, not 0. In [Calculate Lookup Table Values](functors/Calculate-Lookup-Table-Values.html) and [Calculate Lookup Table Keys And Values](functors/Calculate-Lookup-Table-Keys-And-Values.html), both keywords serve a different, row-oriented role: `line` is the key of the current table row, and `column` is the value already associated with that key in the base lookup table — so `column` lets the expression read the row's existing value without a separate table lookup, while `t1[line]` (or `%someTable[line]` in shorthand) reads the corresponding value from any other connected table.

---

# 5. Lookup Table Operators

These operators query a **Lookup Table** (`tX`) — a single-key table — and return the associated value. The key lookup rule is controlled by a prefix operator inside the brackets. Available in all five calculator functors.

**General syntax:** `tX[RULE EXPR]`

> If `tX` is bound to a multi-column Table (not a Lookup Table), an error is reported. See section 6 for multi-column tables.

| Operator | Syntax | Description | Example |
| --- | --- | --- | --- |
| Exact match | `tX[EXPR]` | Returns the value whose key **equals** the expression. Returns null if not found. | `t2[i1 + 2]` |
| Equal lower bound | `tX[<= EXPR]` | Returns the value for the **greatest key \<= EXPR**. | `t2[<= 14]` |
| Strict lower bound | `tX[< EXPR]` | Returns the value for the **greatest key \< EXPR**. | `t2[< i1 + 2]` |
| Equal upper bound | `tX[>= EXPR]` | Returns the value for the **smallest key >= EXPR**. | `t2[>= i1 + i3]` |
| Strict upper bound | `tX[> EXPR]` | Returns the value for the **smallest key > EXPR**. | `t2[> i7]` |
| Closest key | `tX[>< EXPR]` | Returns the value for the key **nearest to EXPR** (ties go to the lower key). | `t2[>< 3 + i7]` |
| Linear interpolation | `tX[/ EXPR]` | Returns a **linearly interpolated value** between the two surrounding keys. | `t2[/ i2]` |
| Key existence test | `tX[? EXPR]` / `tX[=? EXPR]` / `tX[==? EXPR]` | Returns **1** if EXPR matches a key in the table, **0** otherwise. Does not retrieve a value. | `t2[? i2]` |
| Named attribute | `tX["NAME"]` | Returns the value bound to a **predefined attribute name** (e.g. `"cellArea"`). Only valid for tables produced by [Extract Map Attributes](functors/Extract-Map-Attributes.html) or [Extract Lookup Table Attributes](functors/Extract-Lookup-Table-Attributes.html). | `t2["cellArea"]` |

> **Note:** The syntax `tX{EXPR}` (curly braces) was a deprecated alias for `tX[<= EXPR]` and is no longer supported.

The bound operators (`<=`, `<`, `>=`, `>`, `><`, `/`) are especially useful for **range-based reclassification** and **interpolation**, where your table defines breakpoints rather than exact class codes.

---

# 6. Multi-Column Table Operators

These operators query a regular **Table** (`tX`) — one with multiple key columns and one or more data columns — using a set of keys simultaneously. Available in all five calculator functors.

**General syntax:** `tX[ [KEY1, KEY2, ...] ]` or `tX[ [KEY1, KEY2, ...] [COL] ]`

> If `tX` is bound to a Lookup Table (single-key), an error is reported.

| Operator | Syntax | Description | Example |
| --- | --- | --- | --- |
| Default column | `tX[ [EXPR, EXPR, ...] ]` | Returns the value in the **first data column** matching the given set of keys. | `t2[ [i1 + 2, i2/2, t1[v2]] ]` |
| Named column | `tX[ [EXPR, EXPR, ...] ["COL_NAME"] ]` | Returns the value in the **named data column** matching the given set of keys. | `t2[ [i1 + 2, i2/2, t1[v2]] ["Area_In_Hectares"] ]` |
| Indexed column | `tX[ [EXPR, EXPR, ...] [EXPR] ]` | Returns the value in the **column indexed by the second expression** matching the given set of keys. Column indices are **1-based**. | `t2[ [i1 + 2, i2/2, t1[v2]] [v1+2] ]` |

These operators allow joining spatial data to rich tabular datasets at the cell level — for example, retrieving a transition probability from a multi-dimensional probability table keyed by land-use class and elevation zone.

---

# 7. Image Neighborhood Functions

> **Availability:** [Calculate Map](functors/Calculate-Map.html) and [Calculate Categorical Map](functors/Calculate-Categorical-Map.html) only. A spatial grid is required.

Neighborhood operators aggregate values from a rectangular window centred on the current cell.

**Full syntax:** `nbN(IMAGE, h, w, y, x)` <br>
**Short syntax (window centred on current cell):** `nbN(IMAGE, h, w)`

| Parameter | Meaning |
| --- | --- |
| `N` | Operator name (see table below) |
| `IMAGE` | An image identifier (`iX`) |
| `h` | Number of window rows |
| `w` | Number of window columns |
| `y` | Row coordinate to anchor the window centre (optional) |
| `x` | Column coordinate to anchor the window centre (optional) |

The window centre defaults to the current cell when `y` and `x` are omitted. For even-sized windows, the centre is displaced toward the top-left corner. When any cell in the window falls outside the image boundary, its coordinate is resolved using the same mirror formula as `iX[LINE, COL]`, applied **independently to each out-of-bounds cell**: for a row coordinate `cellLine` in an image of N rows, if `cellLine` ≤ 0 the effective row is `1 − cellLine`, and if `cellLine` > N the effective row is `2N + 1 − cellLine`; the same applies to column coordinates. This applies to every cell in the window — not just the anchor position — so a window near the edge of the image will sample mirrored cells for all positions that extend beyond the boundary. **Null cells within the window are excluded from all calculations.**

| Operator | Syntax | Description | Example |
| --- | --- | --- | --- |
| Minimum | `nbMin(...)` | Minimum value among non-null cells in the window | `nbMin(i4, 2, 3, line-1, column)` |
| Maximum | `nbMax(...)` | Maximum value among non-null cells in the window | `nbMax(i1, 4, 4) - 1` |
| Sum | `nbSum(...)` | Sum of non-null cells in the window | `nbSum(i3, 5, 5) + 7` |
| Product | `nbProd(...)` | Product of all non-null cells in the window | `if not isNull(i1) then nbProd(i1, 2, 2, 0, column) else 0` |
| Count | `nbCount(...)` | Number of non-null cells in the window | `nbCount(i2, 3, 3) + nbCount(i1, 3, 3, line, column+3)` |
| Average | `nbAverage(...)` | Arithmetic mean of non-null cells in the window | `round(nbAverage(i1, 7, 7))` |
| Median | `nbMedian(...)` | Median of non-null cells. For an even count, the **greater** of the two central values is returned. | `nbMedian(i1, 5, 5)` |
| Mode | `nbMode(...)` | Most frequent value among non-null cells. Returns null if no mode exists; returns the **lesser** value if multiple modes tie. | `nbMode(i1, 5, 5)` |
| Variance | `nbVar(...)` | Population variance of non-null cells: sum of (xi - mean)^2 / n | `nbVar(i4, 7, 7) / 25` |
| Standard Deviation | `nbStdDev(...)` | Population standard deviation of non-null cells: sqrt of variance | `nbStdDev(i2, 3, 3, line+1, column)` |

---

# 8. Image Neighborhood Indexing Functions

> **Availability:** [Calculate Map](functors/Calculate-Map.html) and [Calculate Categorical Map](functors/Calculate-Categorical-Map.html) only.

These operators compute a neighbourhood statistic and then use the result as an **index** to retrieve a value from either a connected Lookup Table or a second image. `TABLE` below always refers to a **Lookup Table** specifically — see section 5 for the operators that query one directly.

> If `TABLE` is bound to a multi-column Table (not a Lookup Table), an error is reported. See section 6 for multi-column tables.

**Full syntax:** <br>
`nbN(IMAGE, h, w, TABLE, y, x)` <br>
`nbN(IMAGE, h, w, IMAGE2, y, x)`

**Short syntax (window centred on current cell):** <br>
`nbN(IMAGE, h, w, TABLE)` <br>
`nbN(IMAGE, h, w, IMAGE2)`

When a **TABLE** (Lookup Table) is provided: the statistic is used as a key to query it, equivalent to `TABLE[statistic]` from section 5. <br>
When an **IMAGE2** is provided: the statistic is used as a pixel coordinate to sample `IMAGE2`.

| Operator | Syntax | Description | Example |
| --- | --- | --- | --- |
| MinRef | `nbMinRef(...)` | Finds the minimum in the window, then uses it as an index into the Lookup Table (or a coordinate into IMAGE2). | `nbMinRef(i4, 2, 3, t1, line, column)` |
| MaxRef | `nbMaxRef(...)` | Finds the maximum in the window, then uses it as an index into the Lookup Table (or a coordinate into IMAGE2). | `nbMaxRef(i4, 2, 3, i1, line, column)` |

---

# 9. Convolution Operator

> **Availability:** [Calculate Map](functors/Calculate-Map.html) and [Calculate Categorical Map](functors/Calculate-Categorical-Map.html) only.

`nbConvol` applies a kernel-weighted convolution to an image — for spatial filtering such as Gaussian blur or edge detection.

**Syntax:** `nbConvol(IMAGE, TABLE, h, w)` / `nbConvol(IMAGE, TABLE, h, w, y, x)`

> If `TABLE` is bound to a multi-column Table (not a Lookup Table), an error is reported. See section 6 for multi-column tables.

| Parameter | Meaning |
| --- | --- |
| `IMAGE` | The image to convolve (`iX`) |
| `TABLE` | A **Lookup Table** whose entries are the kernel coefficients, indexed 1 to h\*w, mapped **left-to-right, top-to-bottom**. |
| `h` | Number of kernel rows |
| `w` | Number of kernel columns |
| `y`, `x` | Anchor position (optional; defaults to window centre) |

Each cell in the window is assigned a unique integer key, starting at 1 and advancing left-to-right, then top-to-bottom. The `TABLE` argument must be a Lookup Table containing one row per window cell, where the key is that cell's index and the value is its convolution coefficient. The result of `nbConvol` is the weighted sum of all pixel values in the window, each multiplied by the coefficient stored at the corresponding key in the table.

The grids below illustrate the index mapping for some common window sizes:

**3×3 window (h=3, w=3):**

|  | col 1 | col 2 | col 3 |
| --- | --- | --- | --- |
| **row 1** | 1 | 2 | 3 |
| **row 2** | 4 | 5 | 6 |
| **row 3** | 7 | 8 | 9 |

**5×5 window (h=5, w=5):**

|  | col 1 | col 2 | col 3 | col 4 | col 5 |
| --- | --- | --- | --- | --- | --- |
| **row 1** | 1 | 2 | 3 | 4 | 5 |
| **row 2** | 6 | 7 | 8 | 9 | 10 |
| **row 3** | 11 | 12 | 13 | 14 | 15 |
| **row 4** | 16 | 17 | 18 | 19 | 20 |
| **row 5** | 21 | 22 | 23 | 24 | 25 |

**3×5 window (h=3, w=5) — non-square example:**

|  | col 1 | col 2 | col 3 | col 4 | col 5 |
| --- | --- | --- | --- | --- | --- |
| **row 1** | 1 | 2 | 3 | 4 | 5 |
| **row 2** | 6 | 7 | 8 | 9 | 10 |
| **row 3** | 11 | 12 | 13 | 14 | 15 |

In all cases the total number of keys required in the table is h × w.

**Example:** Apply a Gaussian-blur kernel stored in `t1` over a 3x3 window on `i1`:

```
nbConvol(i1, t1, 3, 3)
```

---

# Null Value Handling

## General rule (all five functors)

A null value in any operand **poisons the entire expression**: the result becomes null regardless of what the rest of the expression does. This is not a special case — it is the default behaviour for every operator and every operand type, across all five calculator functors.

> **Note:** The keyword `null` (available in all five functors) is an **abstract** sentinel — it carries no numeric value and cannot participate in arithmetic. It is distinct from `null(iX)` (available in map calculators only), which returns the **numeric** value that image X uses internally to mark missing cells. These two are not interchangeable: `null` poisons any expression that uses it; `null(iX)` is a regular number that happens to be the image's no-data sentinel.

| Expression | Null behaviour |
| --- | --- |
| `i1 / 0` | Always null (division by zero on a map cell) |
| `v1 / 0` | Always null — division by zero is null regardless of operand type |
| `t1[v1]` | Null if the key `v1` is not found in lookup table `t1` |
| `i1 + t1[line] / v1 ^ 3` | Null if the map cell `i1`, the table lookup `t1[line]`, or the value `v1` is null |
| `if isNull(t1[v1]) then 1 else 2` | **Never null** — `isNull` itself always resolves to 0 or 1 |
| `if isNull(v1) then i2 else t1[line]` | May be null, depending on `i2` or the table lookup `t1[line]` |
| `(100 / v2) ? 0` | **Never null** — div-by-zero on a value falls back to 0 |
| `(t1[v1]) ? i1` | If the key `v1` is not found in `t1`, falls back to `i1`; may still be null if `i1` is null |

The poison spreads through the entire chain: if `i1` is null, then `i1 + 5` is null, `(i1 + 5) * v1` is null, and so on. There is no way to "un-null" a result once a null has entered the calculation — except by explicitly testing for it first.

A null value inside an `if...then...else` test propagates the same way, regardless of which branch would otherwise have been taken. In `(if (i1 / 3 > 9) then i2 else 1 + i3) + 10`, a null `i1` makes `i1 / 3` null, which makes the comparison `i1 / 3 > 9` null, which makes the whole conditional null — and adding 10 to that null result is still null. Wrapping the expression in `?` catches it: `( (if (i1 / 3 > 9) then i2 else 1 + i3) + 10 ) ? 20` evaluates to 20 whenever the inner expression comes out null for any reason, including a null test clause.

In a realistic expression, null can enter from several independent sources simultaneously. This expression computes a weighted transition probability from two input maps and a per-class calibration table:

```
(i1 * t1[i3] + i2 * (1 - t1[i3])) / v1
```

Here `i1` is a distance map, `i2` a slope map, `i3` a land-use class map, `t1` a calibration table keyed by class code, and `v1` a normalisation scalar. The result is null if *any* of the following is true at the current cell: `i1`, `i2`, or `i3` is null; the class code in `i3` is not a key in `t1`; or `v1` is zero. A single missing class in the calibration table silently nulls every cell of that class, which may be difficult to diagnose. The defensive form makes each failure mode explicit:

```
if isNull(i1) or isNull(i2) or isNull(i3) then null
else (i1 * (t1[i3] ? 0) + i2 * (1 - (t1[i3] ? 0))) / v1
```

The `?` operator provides a fallback of 0 for any missing table key, so cells whose class is absent from the calibration table are treated as having zero weight rather than propagating null.

**Two safe patterns for handling nulls — applicable to map cells, table lookups, and scalar values alike:**

1. `isNull(EXPR)` — test for null and branch:

```
   if isNull(t1[v1]) then 0 else t1[v1]
```

1. `EXPR ? FALLBACK` — catch any algebraic error and substitute a fallback:

```
   (v1 / v2) ? 0
```

> **Note:** `isNull()` is immune to the poisoning rule — it always returns 0 or 1, never null, even when its argument is null. It is the only reliable way to branch on null.

This poisoning behaviour is what makes short expressions like `i1 + 10` or `i1 * i2` work correctly across a whole map without any explicit null-checking: a cell that's null in either input becomes null in the output automatically, so the expression effectively only touches cells where every input is valid.

**Substituting a default for a null operand.** To treat null cells in either of two maps as if they held the value 1 before multiplying them — rather than letting either map's null poison the whole product — the `?` fallback is the most concise form:

```
(i1 ? 1) * (i2 ? 1)
```

The equivalent using `isNull` is more verbose but reads the same way:

```
(if isNull(i1) then 1 else i1) * (if isNull(i2) then 1 else i2)
```

Both are shorthand for the fully exhaustive case analysis, spelled out explicitly:

```
if isNull(i1) and isNull(i2) then 1
else if not isNull(i1) and not isNull(i2) then i1 * i2
else if not isNull(i1) and isNull(i2) then i1
else i2
```

The exhaustive form is only worth writing out when each of the four combinations genuinely needs different treatment; when they don't, as here, the shorter forms above are equivalent and preferable.

If the computed real value exceeds the range of the chosen Cell Type, that cell is also written as null rather than wrapping or clipping. This range check applies to [Calculate Map](functors/Calculate-Map.html) and [Calculate Categorical Map](functors/Calculate-Categorical-Map.html) only — the only two functors that accept a Cell Type parameter and write to a typed cell grid.

## When a conditional's test needs guarding against null

A conditional's test poisoning the whole result is only a problem when the tested operand's nullness shouldn't determine whether the entire expression is invalid. Reclassifying `i1` in place — `if i1 = 2 then 10 else i1` — needs no explicit guard, since a null `i1` making the reclassified result null for that cell is exactly the desired behaviour: the expression is internally equivalent to `if isNull(i1) then null else if i1 = 2 then 10 else i1`.

The same mechanism causes a real bug when the operand being tested isn't the one the null-ness should actually be judged against. Combining a landscape map (`i1`) with a road map (`i2`, where 1 marks a road and null marks everything else) might suggest `if i2 = 1 then 1 else i1` — but this is internally equivalent to `if isNull(i2) then null else if i2 = 1 then 1 else i1`. Since most cells are null in a sparse road map, most of the output becomes null too, discarding `i1`'s landscape values everywhere a road isn't present — even though `i2` being null says nothing about whether `i1`'s value is valid.

Guarding the test with `isNull` fixes it: `if not isNull(i2) and i2 = 1 then 1 else i1` only tests `i2` once it's confirmed non-null, so a null road cell falls through to the landscape value in `i1` instead of nulling the result.

## Exceptions in map calculators

> **Availability:** [Calculate Map](functors/Calculate-Map.html) and [Calculate Categorical Map](functors/Calculate-Categorical-Map.html) only. The two exceptions below involve `iX` references and neighbourhood functions, which do not exist in the other three calculator functors.

- **Coordinate lookup** `iX[LINE_EXPR, COL_EXPR]` — accessing a map at a specific coordinate returns **0**, not null, when the target cell **is null**. Coordinates that fall **outside the image boundary** are mirrored back into range rather than producing an error. For a row coordinate `cellLine` in an image of N rows, `cellLine` is normally expected to be in the range \[1, N\]. When `cellLine` is outside this range, it is mirrored back: if `cellLine` ≤ 0, the effective row is `1 − cellLine` (for instance, `cellLine` = 0 → row 1, `cellLine` = −1 → row 2, `cellLine` = −2 → row 3); if `cellLine` > N, the effective row is `2N + 1 − cellLine` (for instance, `cellLine` = N+1 → row N, `cellLine` = N+2 → row N−1, `cellLine` = N+3 → row N−2). The same formula applies independently to the column coordinate `cellCol`. It can be a source of subtle bugs: an expression that tests `i1[line-1, column] > 0` will silently treat a null neighbour as zero rather than null. A table or lookup-table key lookup (`tX[EXPR]`) that finds no matching key still returns null as normal — this exception applies only to map coordinate lookups. To get a null result instead, use the null-preserving form `iX[[LINE_EXPR, COL_EXPR]]`, which returns null when the target cell is null.
- **Neighbourhood functions** `nbN(iX, h, w)` — operators such as `nbSum`, `nbAverage`, `nbMax`, and so on aggregate over a window of cells and **exclude null cells from the calculation**. If `i1` is null at the current cell, the neighbourhood function simply ignores it and aggregates the remaining non-null cells in the window.

---

# EGO Script Syntax

When writing expressions inside a `.ego` script file (see [EGO Script Language](EGO-Script.html)), the expression must be enclosed in square brackets `[ ]`. Below are examples of each functor in both shorthand and verbose form.

> **A note on operand naming.** Throughout the expression-language tables above, operands are written generically as `iX`, `tX`, and `vX` — the **numbered** form, used when a port is connected via an explicit **hook** functor (`NumberMap`, `NumberTable`, or `NumberValue`) in the **verbose** form below. EGO Script's **shorthand** form instead refers to operands **by name** — the variable already bound elsewhere in the script — prefixed with a sigil that marks its type: `#` for a map, `%` for a table or lookup table, `$` for a value. So `i1` in a verbose expression corresponds to `#someMapVariable` in the shorthand version of the same expression, `t1` corresponds to `%someTableVariable`, and `v1` corresponds to `$someValueVariable`. The two forms are interchangeable but cannot be mixed within a single expression. See [Calculator functor shorthand](EGO-Script.html#calculator-functor-shorthand) in the EGO Script documentation for a full description of both forms.

## CalculateMap (`#`)

```
// Shorthand — normalise a map to the [0, 1] range
result := # [ (#inputMap - $minVal) / ($maxVal - $minVal) ] .float32 .default .no .none;

// Verbose equivalent
result := CalculateMap {
    expression = [ (i1 - v1) / (v2 - v1) ],
    cellType = .float32,
    nullValue = .default,
    resultIsSparse = .no,
    resultFormat = .none
} {{
    // i1
    NumberMap   inputMap 1;
    // v1
    NumberValue minVal   1;
    // v2
    NumberValue maxVal   2;
}};
```

## CalculateMultipleMaps

The maps in the resulting struct are retrieved with [Extract Struct Map](functors/Extract-Struct-Map.html):[^8150]

```
// Shorthand — vegetation index, its scaled version and a mask, calculated in one pass
indices := #* [
    let _ndvi: (#nir - #red) / (#nir + #red)
    in {
        ndvi: _ndvi,
        scaled: _ndvi * 100,
        mask: if _ndvi > 0.3 then 1 else 0
    }
] .float32 .default .no .none;

// Verbose equivalent
indices := CalculateMultipleMaps {
    expression = [
        let _ndvi: (i1 - i2) / (i1 + i2)
        in {
            ndvi: _ndvi,
            scaled: _ndvi * 100,
            mask: if _ndvi > 0.3 then 1 else 0
        }
    ],
    cellType = .float32,
    nullValue = .default,
    resultIsSparse = .no,
    resultFormat = .none
} {{
    // i1
    NumberMap nir 1;
    // i2
    NumberMap red 2;
}};

// Retrieves each map from the struct
ndvi := ExtractStructMap indices "ndvi";
scaled := ExtractStructMap indices "scaled";
mask := ExtractStructMap indices "mask";
```

## CalculateCategoricalMap (`##`)

```
// Shorthand — reclassify a continuous map into three categories
landUse := ## [
    if #elevationMap < $lowThreshold then 1
    else if #elevationMap < $highThreshold then 2
    else 3
] .int8 .default .no .none;

// Verbose equivalent
landUse := CalculateCategoricalMap {
    expression = [
        if i1 < v1 then 1
        else if i1 < v2 then 2
        else 3
    ],
    cellType = .int8,
    nullValue = .default,
    resultIsSparse = .no,
    resultFormat = .none
} {{
    // i1
    NumberMap   elevationMap    1;
    // v1
    NumberValue lowThreshold    1;
    // v2
    NumberValue highThreshold   2;
}};
```

## CalculateValue (`$`)

```
// Shorthand — compute a weighted combination of two scalar inputs
blendedRate := $ [ $weight * $rateA + (1 - $weight) * $rateB ];

// Verbose equivalent
blendedRate := CalculateValue {
    expression = [ v1 * v2 + (1 - v1) * v3 ]
} {{
    // v1
    NumberValue weight          1;
    // v2
    NumberValue rateA           2;
    // v3
    NumberValue rateB           3;
}};

// Shorthand — look up a scalar threshold from a calibration table
threshold := $ [ %calibrationTable[$targetClass] ];

// Verbose equivalent
threshold := CalculateValue {
    expression = [ t1[v1] ]
} {{
    // t1
    NumberTable calibrationTable 1;
    // v1
    NumberValue targetClass      1;
}};
```

## CalculateLookupTableValues (`%`)

```
// Shorthand — mark each row in a lookup table where value meets a threshold
hilltops := % [
    if %saddleHeights[line] >= $minimumHeight and %saddleAngles[line] >= $minimumSlopeAngle then 1 else null
] "Top_Id" "Is_Hilltop" .none;

// Verbose equivalent
hilltops := CalculateLookupTableValues [
    if t1[line] >= v1 and t2[line] >= v2 then 1 else null
] "Top_Id" "Is_Hilltop" .none {{
    // t1
    NumberTable saddleHeights     1;
    // t2
    NumberTable saddleAngles      2;
    // v1
    NumberValue minimumHeight     1;
    // v2
    NumberValue minimumSlopeAngle 2;
}};

// Shorthand — transform values using a calibration lookup table, iterating base table keys
dominantTops := % [
    if %dominanceLookup[line] = line then 1 else null
] "Top_Id" "Is_Dominant" dominanceLookup;
```

## CalculateLookupTableKeysAndValues (`%%`)

```
// Shorthand — extract two columns from a multi-column table into a new lookup table
nearestDistances := %% {
    keyColumnExpression   = [ %nearestPoints[[line]["Point_Id"]] ],
    valueColumnExpression = [ %nearestPoints[[line]["Nearest_Distance"]] ],
    keyColumnName   = "Point_Id",
    valueColumnName = "Nearest_Distance",
    baseLookupTable = pointKeys
};

// Verbose equivalent
nearestDistances := CalculateLookupTableKeysAndValues [
    t1[[line]["Point_Id"]]
] [
    t1[[line]["Nearest_Distance"]]
] "Point_Id" "Nearest_Distance" pointKeys {{
    // t1
    NumberTable nearestPoints 1;
}};
```

---

# Practical Examples

## CalculateMap examples

### Normalise a raster to \[0, 1\]

```
(i1 - v1) / (v2 - v1)
```

`i1` = input map; `v1` = global minimum, `v2` = global maximum.

### Weighted combination of two probability maps

```
i1 * v1 + i2 * (1 - v1)
```

`i1`, `i2` = the two maps to blend; `v1` = blending weight.

### Convert degrees to radians and apply a trig function

```
sin(i1 * pi / 180)
```

`i1` = map of values in degrees.

### Clamp output to a valid range

```
clamp(i1 * v1 + i2 * v2, 0, 1)
```

`i1`, `i2` = input maps; `v1`, `v2` = their respective blending weights.

### Fill null cells with the local mean

```
if isNull(i1) then nbAverage(i1, 3, 3) else i1
```

`i1` = input map.

### Focal range (texture measure)

```
nbMax(i1, 5, 5) - nbMin(i1, 5, 5)
```

`i1` = input map.

### Stochastic perturbation with Gaussian noise

```
i1 + rNormal(0, v1)
```

`i1` = input map; adds Gaussian noise with zero mean and standard deviation `v1` to every cell.

### Coordinate-based gradient ramp

```
line / v1
```

Produces a north-to-south gradient scaled by scalar `v1`.

### Arbitrary pixel lookup (map sampling at computed location)

```
i2[round(i1), column]
```

For each cell, samples `i2` at the row given by image `i1`, same column.

### Guard against division by zero with a fallback

```
(i1 / i2) ? (i1 - i2)
```

`i1` = numerator map, `i2` = denominator map. If `i2` is zero at a cell, falls back to `i1 - i2` instead of producing null.

---

## CalculateCategoricalMap examples

### Binary mask from a category map

```
if i1 == 2 then 1 else 0
```

`i1` = input categorical map.

### Multi-condition reclassification into categories

```
if i1 == 1 then 10
else if i1 == 2 then 20
else if i1 == 3 then 35
else null
```

`i1` = input categorical map.

### Reclassify a continuous map into classes using lookup table breakpoints

```
t1[<= i1]
```

`i1` = continuous input map; `t1` = breakpoint lookup table mapping value thresholds to category codes. Assigns each cell the category value from `t1` whose key is the greatest key \<= the cell value — implementing interval-based reclassification without if/else chains.

### Assign a category based on multiple input maps

```
if i1 > v1 and i2 < v2 then 1
else if i1 > v1 then 2
else 3
```

`i1` = slope map, `i2` = distance map; `v1`, `v2` = threshold scalars.

### Reclassify using a lookup table of region memberships

```
if %regionCounts[?#regions] then 1 else null
```

Assigns category 1 to every cell whose region identifier (map `regions`) appears as a key in lookup table `regionCounts`, null otherwise. Written in shorthand: the map is referenced as `#regions` and the lookup table as `%regionCounts`.

---

## CalculateValue examples

### Compute a weighted average of two scalar parameters

```
v1 * v2 + (1 - v1) * v3
```

`v1` = weight, `v2`, `v3` = the two values to blend.

### Look up a scalar threshold from a calibration table

```
t1[v1]
```

`t1` = calibration lookup table, `v1` = the key to look up.

### Derive a running counter increment

```
v1 + 1
```

When `v1` holds the previous iteration's counter value, this computes the next step.

### Convert a parameter value using a linear formula

```
(v1 - v2) / (v3 - v2)
```

Normalises `v1` to the range defined by `v2` (minimum) and `v3` (maximum).

---

## CalculateLookupTableValues examples

### Mark rows that satisfy a threshold condition

```
if t1[line] >= v1 and t2[line] >= v2 then 1 else null
```

`t1`, `t2` = operand lookup tables; `v1`, `v2` = threshold values. Iterates over all row keys; `t1[line]` and `t2[line]` retrieve the corresponding values from each table.

### Apply a multiplicative scaling factor to existing table values

```
t1[line] * v1
```

Scales every value in table `t1` by a constant `v1`, producing a new lookup table with the same keys.

### Identify rows where a key equals its own value

```
if t1[line] = line then 1 else null
```

Returns 1 for rows where the value stored under that key equals the key itself.

### Range-based reclassification via an interval table

```
t1[<= line]
```

For each key, looks up the value from `t1` whose key is the greatest key \<= the current row key — interpolating class membership from a breakpoint table.

---

## CalculateLookupTableKeysAndValues examples

### Extract two columns from a multi-column table into a lookup table

```
// Key expression
t1[[line]["Point_Id"]]

// Value expression
t1[[line]["Nearest_Distance"]]
```

For each row in the base lookup table, the key is drawn from the `"Point_Id"` column of `t1` and the value from `"Nearest_Distance"`.

### Remap keys and scale values simultaneously

```
// Key expression
line * 10

// Value expression
t1[line] / v1
```

`t1` = base lookup table being iterated; `v1` = scaling divisor. Multiplies each key by 10 and divides the corresponding value by `v1`.

---

# Multi-key table join

```
t1[ [i1, i2] ["TransitionProb"] ]
```

`i1`, `i2` = map layers providing the composite key values; `t1` = multi-key probability table. Looks up a transition probability using two map values as composite keys. Available in [Calculate Map](functors/Calculate-Map.html) and [Calculate Categorical Map](functors/Calculate-Categorical-Map.html); the same syntax works in the table calculators by substituting `line` or `vX` for `iX`.

---

# Expression Editor — Workflow

The steps differ by group of calculator functors. Each group is described separately below.

## CalculateMap and CalculateCategoricalMap

> **Note:** [Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html) follows the same steps; its expression must be a [struct expression](#struct-expressions).

1. **Connect your inputs first.** Connect all required maps ([Number Map](functors/Number-Map.html)), tables ([Number Table](functors/Number-Table.html)), and scalars ([Number Value](functors/Number-Value.html)) to the operator's ports before opening the editor.
1. **Open the expression editor.** All connected identifiers appear with their aliases at the top.
1. **Write the expression** using the listed identifiers.
1. **Set Cell Type** if the default (Signed 32-bit Integer) does not suit your output — for example, float for probability maps or int8 for compact categorical maps.
1. **Set Null Value** if you need a specific no-data sentinel.

## CalculateValue

1. **Connect your inputs first.** Connect all required tables ([Number Table](functors/Number-Table.html)) and scalars ([Number Value](functors/Number-Value.html)) to the operator's ports before opening the editor. Maps cannot be connected, since [Calculate Value](functors/Calculate-Value.html) has no cell context.
1. **Open the expression editor.** All connected identifiers appear with their aliases at the top.
1. **Write the expression** using the listed identifiers. There is no Cell Type or Null Value to set — the result is a single scalar.

## CalculateLookupTableValues and CalculateLookupTableKeysAndValues

1. **Connect your inputs first.** Connect all required tables ([Number Table](functors/Number-Table.html)) and scalars ([Number Value](functors/Number-Value.html)) to the operator's ports before opening the editor.
1. **Set the Key Column Name and Value Column Name** for the output lookup table.
1. **Connect a Base Lookup Table**, or leave it as `.none`, in which case the row source is the `NumberTable` hook with the lowest list index that is connected to a lookup table (not a regular table) in verbose form, or the first lookup table referenced by name in the expression in shorthand form.
1. **Open the expression editor.** All connected identifiers appear with their aliases at the top. [Calculate Lookup Table Values](functors/Calculate-Lookup-Table-Values.html) has a single expression; [Calculate Lookup Table Keys And Values](functors/Calculate-Lookup-Table-Keys-And-Values.html) has separate key and value expressions.
1. **Write the expression(s)**, using `line` for the current row's key and `column` for the current row's existing value where needed.

---

# Notes and Caveats

- **Choose the right functor for the output type.** Use [Calculate Map](functors/Calculate-Map.html) for continuous rasters, [Calculate Categorical Map](functors/Calculate-Categorical-Map.html) for class-coded rasters (so that downstream functors treat them as categorical), [Calculate Value](functors/Calculate-Value.html) for a single scalar, and the two lookup table calculators ([Calculate Lookup Table Values](functors/Calculate-Lookup-Table-Values.html), [Calculate Lookup Table Keys And Values](functors/Calculate-Lookup-Table-Keys-And-Values.html)) for row-by-row table construction.
- **Several maps from the same inputs.** Use [Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html) when more than one map is calculated from the same inputs or shares intermediate results, instead of repeating the sub-expressions in several [Calculate Map](functors/Calculate-Map.html) functors.[^8150]
- **`line` and `column` are context-dependent.** In [Calculate Map](functors/Calculate-Map.html) and [Calculate Categorical Map](functors/Calculate-Categorical-Map.html), `line` is the spatial row index and `column` is the spatial column index of the current pixel, both **starting at 1**. In [Calculate Lookup Table Values](functors/Calculate-Lookup-Table-Values.html) and [Calculate Lookup Table Keys And Values](functors/Calculate-Lookup-Table-Keys-And-Values.html), both are still available but take on row-oriented meanings: `line` is the key of the current table row, and `column` is the value already associated with that key in the base lookup table. A different table's value for that same key can be retrieved with `%someTable[line]`. See [section 4](#4-image-operators-and-functions) for full details.
- **Native compilation.** Expression calculations across all five calculator functors can be compiled to native code automatically (requires the optional native expression support package), delivering near-C performance — no user action is needed beyond installing the package.
- **Overflow produces null.** If the result exceeds the Cell Type's range, the cell becomes null rather than wrapping. Applies to [Calculate Map](functors/Calculate-Map.html) and [Calculate Categorical Map](functors/Calculate-Categorical-Map.html) only — the only two functors with a Cell Type parameter.
- **Neighbourhood functions ignore nulls.** All `nbN` operators ([section 7](#7-image-neighborhood-functions)) skip null cells in their window; only non-null cells contribute to the statistic.
- **`iX[LINE, COL]` returns 0, not null, when the target cell is null.** Coordinates outside the image boundary are mirrored rather than treated as out-of-bounds. This is the one exception to the general null-propagation rule. See [section 4](#4-image-operators-and-functions) and [Null Value Handling](#null-value-handling). Use `iX[[LINE, COL]]` to get null instead.

---

# Internal Names

| Functor | Internal name |
| --- | --- |
| Calculate Map | `CalculateMap` |
| Calculate Multiple Maps[^8150] | `CalculateMultipleMaps` |
| Calculate Categorical Map | `CalculateCategoricalMap` |
| Calculate Value | `CalculateValue` |
| Calculate Lookup Table Values | `CalculateLookupTableValues` |
| Calculate Lookup Table Keys and Values | `CalculateLookupTableKeysAndValues` |

[^8150]: Available in Dinamica EGO 8.15.0, currently a development version. Details may change before release.

{% endraw %}
