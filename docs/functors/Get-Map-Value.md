---
title: "Get Map Value"
nav_order: 33
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Get Map Value

## Description

Retrieves the value of a map cell at a specified line and column.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Map the value is retrieved from. |
| Cell Line | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Line of the cell. Line 1 is the topmost line. |
| Cell Column | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Column of the cell. Column 1 is the leftmost column. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Value If Null | [Real Value Type](../types/Real-Value-Type.html) | Value returned when the cell at the specified coordinates equals Map's null value. This is an advanced port. | 0.0 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Cell Value | [Real Value Type](../types/Real-Value-Type.html) | Retrieved cell value. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

Raises an error if Cell Line or Cell Column falls outside the dimensions of Map.

## Internal Name

GetMapValue
{% endraw %}
