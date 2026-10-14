---
title: "For Each Category"
nav_exclude: true
---
{% raw %}
# For Each Category

## Description

Container that executes the functors it contains once for every class or category present in a categorical map.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Categorical Map Type](Categorical-Map-Type.html) | Map of classes or categories the contained functors are executed for. |

## Optional Inputs

None.

## Outputs

None.

## Internal Outputs

| Name | Type | Description |
| --- | --- | --- |
| Step | [Integer Value Type](Integer-Value-Type.html) | Category being processed in the current execution. |

## Group

[Control](Functor-List.html#control)

## Notes

Executions for different categories can run simultaneously when there is no dependency between them.

When Map has zero categories and a result produced by the contained functors is used outside the container, connect a matching [junction](Functor-List.html#junction) after the container, so a value still reaches the rest of the model if there are no categories to process.

See Lesson 14, "Using For Each Category and Region Manager," for a practical example of this functor.

## Internal Name

ForEachCategory

## Usage examples

See practical examples of this functor in Lesson 14: Using For Each Category and Region Manager
{% endraw %}
