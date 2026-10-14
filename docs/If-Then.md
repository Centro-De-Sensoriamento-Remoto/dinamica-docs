---
title: "If Then"
nav_exclude: true
---
{% raw %}
# If Then

## Description

Executes the functors it contains only when its condition is true.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Condition | [Boolean Value Type](Boolean-Value-Type.html) | Condition that determines whether the contained functors execute. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Sequence Input | [None Type](None-Type.html) | Ensures that the functor connected to this port finishes executing before this container starts. | None |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Sequence Output | [None Type](None-Type.html) | Connect this port to another container's Sequence Input to make this container finish executing before that other container starts. |

## Group

[Control](Functor-List.html#control)

## Notes

When Condition may be false, and a result produced by the contained functors is used outside the container, connect a matching junction (such as [Map Junction](Map-Junction.html) or [Value Junction](Value-Junction.html)) after the container, so a value still reaches the rest of the model when the content does not execute.

## Internal Name

IfThen
{% endraw %}
