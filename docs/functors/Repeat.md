---
title: "Repeat"
nav_order: 26
parent: "Control Functors"
grand_parent: "Functor List"
redirect_from:
  - /Repeat.html
---
{% raw %}
# Repeat

## Description

This container executes the functors it contains a specified number of times. Each execution is called an iteration. While an iteration runs, the container makes the current iteration number available to its contents through the internal output port Step, counting from 1 up to Iterations. If Iterations is zero, the contained functors are not executed at all.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Iterations | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Number of iterations. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Sequence Input | [None Type](../types/None-Type.html) | None | Ensures that the functor connected to this port finishes executing before this container starts. See [Sequence ports](../EGO-Script.html#sequence-ports) in the EGO Script documentation. |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Sequence Output | [None Type](../types/None-Type.html) | Connect this port to another container's Sequence Input to make this container finish executing before that other container starts. |

## Internal Outputs

| Name | Type | Description |
| --- | --- | --- |
| Step | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Current iteration, always in the range from 1 to Iterations. |

## Group

[Control](../Functor-List.html#control)

## Notes

When there is no dependency between iterations, this container may run several of them at the same time instead of one after another.

A [Step](Step.html) functor, a file functor (Load\* / Save\*), or a Select\* functor placed directly inside this container reads the current iteration automatically through its own input, with no need to connect it to Step explicitly.

When Iterations is zero and a result produced by the contained functors is used outside the container, connect a matching [junction](../Functor-List.html#junction) after the container, so a value still reaches the rest of the model from another source in that case.

## Internal Name

Repeat
{% endraw %}
