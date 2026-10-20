---
title: "For Each Category"
nav_order: 8
parent: "Control Functors"
grand_parent: "Functor List"
---
{% raw %}
# For Each Category

## Description

Container that executes the functors it contains once for every class or category present in a categorical map.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Categorical Map Type](../types/Categorical-Map-Type.html) | Map of classes or categories the contained functors are executed for. |

## Optional Inputs

None.

## Outputs

None.

## Internal Outputs

| Name | Type | Description |
| --- | --- | --- |
| Step | [Integer Value Type](../types/Integer-Value-Type.html) | Category being processed in the current execution. |

## Group

[Control](../Functor-List.html#control)

## Notes

Executions for different categories can run simultaneously when there is no dependency between them.

When Map has zero categories and a result produced by the contained functors is used outside the container, connect a matching [junction](../Functor-List.html#junction) after the container, so a value still reaches the rest of the model if there are no categories to process.

## Internal Name

ForEachCategory

## Usage examples

See practical examples of this functor in [Lesson 14: Using "For Each Category" and "Region Manager" to work with the concept of region](../guidebook/Regions-With-For-Each-Category.html) of the Guidebook.
{% endraw %}
