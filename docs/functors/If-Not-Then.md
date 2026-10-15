---
title: "If Not Then"
nav_order: 11
parent: "Control Functors"
grand_parent: "Functor List"
---
{% raw %}
# If Not Then

## Description

Executes the functors it contains only when its condition is false.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Condition | [Boolean Value Type](../types/Boolean-Value-Type.html) | Condition that determines whether the contained functors execute. The contained functors run when this value is false. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Sequence Input | [None Type](../types/None-Type.html) | Ensures that the functor connected to this port finishes executing before this container starts. | None |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Sequence Output | [None Type](../types/None-Type.html) | Connect this port to another container's Sequence Input to make this container finish executing before that other container starts. |

## Group

[Control](../Functor-List.html#control)

## Notes

When Condition may be true, and a result produced by the contained functors is used outside the container, connect a matching junction (such as [Map Junction](Map-Junction.html) or [Value Junction](Value-Junction.html)) after the container, so a value still reaches the rest of the model when the content does not execute.

## Internal Name

IfNotThen
{% endraw %}
