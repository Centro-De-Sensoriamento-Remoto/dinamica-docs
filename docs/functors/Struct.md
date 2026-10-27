---
title: "Struct"
nav_order: 71
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Struct

## Description

Carries a struct — a collection of values organized by identifier, such as the result produced by [Calculate R Expression](Calculate-R-Expression.html) or [Calculate Python Expression](Calculate-Python-Expression.html) — so it can be reused as the input to more than one functor.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Constant | [Struct Type](../types/Struct-Type.html) | A previously initialized struct. This port must be connected to another functor's output; it cannot be set to a constant typed directly into the model. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Object | [Struct Type](../types/Struct-Type.html) | Struct provided by the input port. |

## Group

[Map Algebra Supplementary](../Functor-List.html#map-algebra-supplementary)

## Notes

None.

## Internal Name

Struct
{% endraw %}
