---
title: "Do While"
nav_order: 2
parent: "Control Functors"
grand_parent: "Functor List"
redirect_from:
  - /Do-While.html
---
{% raw %}
# Do While

## Description

This container executes the functors it contains at least once, and keeps executing them for as long as the condition set by a [Set While Condition](Set-While-Condition.html) functor placed inside it is true. Each execution is called a step. While a step runs, the container makes the current step available to its contents through the internal output port Step.

## Inputs

None.

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
| Condition | [Boolean Value Type](../types/Boolean-Value-Type.html) | Current value of the condition that keeps the loop running. |

## Group

[Control](../Functor-List.html#control)

## Notes

This container has no condition port of its own. Place a [Set While Condition](Set-While-Condition.html) functor inside it and connect its output to decide whether the loop keeps running.

Because the content always executes at least once, a result it produces can be used directly outside the container, with no need for a junction.

## Internal Name

DoWhile
{% endraw %}
