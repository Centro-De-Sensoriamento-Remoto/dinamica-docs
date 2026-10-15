---
title: "Print"
nav_order: 24
parent: "Control Functors"
grand_parent: "Functor List"
---
{% raw %}
# Print

## Description

This container prints messages to the application console before and after executing the functors it contains.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Initial Message | [String Type](../types/String-Type.html) | Message printed before the contained functors execute. | None |
| Final Message | [String Type](../types/String-Type.html) | Message printed after the contained functors execute. | None |
| Log Level | [Log Tag Type](../types/Log-Tag-Type.html) | Log level used to print both messages. The log level indicates whether a message is a regular progress message or an error message, for example. | Unconditional |

## Outputs

None.

## Group

[Control](../Functor-List.html#control)

## Notes

Initial Message, when set, is printed before the contained functors run; Final Message, when set, is printed only after all of them have finished running. Both are printed using the level set in Log Level.

Using this container with nothing placed inside it is not recommended: with no contained functors to order its execution against, when the message is actually printed relative to the rest of the model becomes unspecified.

This functor has no string-formatting capabilities of its own. To embed a computed value in a message, assemble the string first with [Create String](Create-String.html) and connect its result into Initial Message or Final Message; some types are also converted to a string automatically when connected directly.

## Internal Name

Print
{% endraw %}
