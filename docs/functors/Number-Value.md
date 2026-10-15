---
title: "Number Value"
nav_order: 64
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Number Value

## Description

This hook functor identifies a value by assigning a number to it, so that a container built to consume numbered values — most commonly one of the calculator functors, such as [Calculate Map](Calculate-Map.html) — can pick it out by that number. It performs no computation itself: the enclosing container inspects its Value and Value Number ports and registers the value under that number, making it available as v`N` inside the container's expression.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Value | [Real Value Type](../types/Real-Value-Type.html) | Value to identify. |
| Value Number | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number by which the value will be known inside the container — for example, 1 makes it available as v1. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Map Algebra Supplementary](../Functor-List.html#map-algebra-supplementary)

## Notes

### Purpose as a placeholder

Number Value only stores the value and the number under which it should be registered. The container it is placed inside inspects those ports and performs the actual registration.

### Valid containers

This functor must be placed directly inside one of the containers that consume numbered values — [Calculate Map](Calculate-Map.html), [Calculate Categorical Map](Calculate-Categorical-Map.html), [Calculate Lookup Table Values](Calculate-Lookup-Table-Values.html), [Calculate Value](Calculate-Value.html), [Create String](Create-String.html), [Calculate R Expression](Calculate-R-Expression.html), [Calculate Python Expression](Calculate-Python-Expression.html), or [Calculate Lookup Table Keys And Values](Calculate-Lookup-Table-Keys-And-Values.html). Placing it inside any other functor is not supported and will fail validation.

### Referencing the value in an expression

Once registered, the value is available inside the container's expression as vN (for example, Value Number = 1 gives v1). This applies to the verbose syntax only. The separate abbreviated syntax eliminates hook functors like Number Value entirely, referencing each connected input directly by its port name instead — see [Calculator functor shorthand](../EGO-Script.html#calculator-functor-shorthand).

### Visual banner

Value Number is normally set to a fixed constant chosen by the model author; connecting it to another functor's output instead reports a warning, since the identifier is meant to stay fixed and readable.

Once Value Number is set, this functor's banner in the model diagram shows "#N"; once the value itself is known, it reads "Value #N is X" (for example, "Value #1 is 42"), making the variable easy to identify in the diagram.

## Internal Name

NumberValue

## Usage examples

[Connecting data inputs](Calculate-Map.html#connecting-data-inputs) in the Calculate Map documentation — shows Number Value exposing a scalar as v1.
{% endraw %}
