---
title: "Log Policy"
nav_order: 14
parent: "Control Functors"
grand_parent: "Functor List"
---
{% raw %}
# Log Policy

## Description

This container executes the functors it contains under a specified maximum log level, temporarily overriding the log policy otherwise in effect for as long as its content runs.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Maximum Log Level | [Log Tag Type](../types/Log-Tag-Type.html) | Maximum log level allowed while the contained functors execute. | Debug 2 |
| Force Specified Log Level | [Boolean Value Type](../types/Boolean-Value-Type.html) | Always use Maximum Log Level, even when the log level already in effect is more restrictive. | No |
| Sequence Input | [None Type](../types/None-Type.html) | Ensures that the functor connected to this port finishes executing before this container starts. | None |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Sequence Output | [None Type](../types/None-Type.html) | Connect this port to another container's Sequence Input to make this container finish executing before that other container starts. |

## Group

[Control](../Functor-List.html#control)

## Notes

When Maximum Log Level is less restrictive than the log level already in effect, or when Force Specified Log Level is true, the log level is temporarily changed to Maximum Log Level while the contained functors execute. The previous log level is always restored afterwards, whether or not an error occurs.

## Internal Name

LogPolicy
{% endraw %}
