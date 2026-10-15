---
title: "Skip All On Error"
nav_order: 30
parent: "Control Functors"
grand_parent: "Functor List"
---
{% raw %}
# Skip All On Error

## Description

This container executes the functors it contains, capturing and discarding any error raised during their execution instead of letting it stop the model.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Trap And Ignore Errors | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, an error raised by a contained functor is captured and ignored. If false, this container behaves like a regular [Group](Group.html) and lets the error propagate. | Yes |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Execution Completed Successfully | [Boolean Value Type](../types/Boolean-Value-Type.html) | True if the contained functors ran to completion without errors. This output can be ignored. |

## Group

[Control](../Functor-List.html#control)

## Notes

Unlike [Skip On Error](Skip-On-Error.html), any results already produced by contained functors before the error occurred are discarded once the error is captured.

When a result produced by a contained functor is used outside this container, connect a matching junction (such as [Map Junction](Map-Junction.html) or [Value Junction](Value-Junction.html)) between the contained functor and the one that uses its result outside the container; otherwise, all subsequent execution is cancelled when an error occurs.

This functor does not capture errors that cannot be ignored, nor the cancellation of the model by the user.

## Internal Name

SkipAllOnError
{% endraw %}
