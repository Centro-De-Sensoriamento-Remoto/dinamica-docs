---
title: "For"
nav_exclude: true
---
{% raw %}
# For

## Description

This container creates a set of steps between two bounds, changing the step by a fixed increment on every iteration, and executes the functors it contains once for each step. Each execution is called a step. While a step runs, the container makes the current step available to its contents through the internal output port Step.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| First Iteration Step | [Real Value Type](Real-Value-Type.html) | Initial step or model iteration. |
| Last Iteration Step | [Real Value Type](Real-Value-Type.html) | Last step or model iteration. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Step Increment | [Real Value Type](Real-Value-Type.html) | Increment or decrement applied to reach the next step or model iteration. | 1 |
| Sequence Input | [None Type](None-Type.html) | Ensures that the functor connected to this port finishes executing before this container starts. | None |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Sequence Output | [None Type](None-Type.html) | Connect this port to another container's Sequence Input to make this container finish executing before that other container starts. |

## Internal Outputs

| Name | Type | Description |
| --- | --- | --- |
| Step | [Real Value Type](Real-Value-Type.html) | Current step or model iteration. |

## Group

[Control](Functor-List.html#control)

## Notes

Step Increment cannot be zero, and its sign must agree with the direction from First Iteration Step to Last Iteration Step — positive when First Iteration Step is less than Last Iteration Step, negative when it is greater. Otherwise the loop would never reach Last Iteration Step and run forever, so the model raises an error.

Unlike other loop containers, the content of this container always executes at least once, even when First Iteration Step and Last Iteration Step are equal. A result it produces can therefore be used directly outside the container, with no need for a junction.

When there is no dependency between steps, this container may process several of them at the same time instead of one after another.

## Internal Name

For
{% endraw %}
