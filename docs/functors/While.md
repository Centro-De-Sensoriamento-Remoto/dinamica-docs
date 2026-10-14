---
title: "While"
nav_order: 37
parent: "Control Functors"
grand_parent: "Functor List"
redirect_from:
  - /While.html
---
{% raw %}
# While

## Description

This container executes the functors it contains while its condition is true. The condition is checked once before the first execution, using the value supplied to Initial Condition, and afterwards using the value set by a [Set While Condition](Set-While-Condition.html) functor placed inside it. Each execution is called a step. While a step runs, the container makes the current step available to its contents through the internal output port Step.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Initial Condition | [Boolean Value Type](../types/Boolean-Value-Type.html) | Initial value of the condition that controls whether the loop runs. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Sequence Input | [None Type](../types/None-Type.html) | Ensures that the functor connected to this port finishes executing before this container starts. | None |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Sequence Output | [None Type](../types/None-Type.html) | Connect this port to another container's Sequence Input to make this container finish executing before that other container starts. |

## Internal Outputs

| Name | Type | Description |
| --- | --- | --- |
| Step | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Current iteration step. |

## Internal Inputs

| Name | Type | Description |
| --- | --- | --- |
| Condition | [Boolean Value Type](../types/Boolean-Value-Type.html) | Current value of the condition that keeps the loop running, after the first execution. |

## Group

[Control](../Functor-List.html#control)

## Notes

Beyond the first execution, this container has no condition port of its own. Place a [Set While Condition](Set-While-Condition.html) functor inside it and connect its output to decide whether the loop keeps running.

When Initial Condition may be false, and a result produced by the contained functors is used outside the container, connect a matching [junction](../Functor-List.html#junction) after the container, so a value still reaches the rest of the model when the content never executes.

## Internal Name

While
{% endraw %}
