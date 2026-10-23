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
| Sequence Input | [None Type](../types/None-Type.html) | Ensures that the functor connected to this port finishes executing before this container starts. | None |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Sequence Output | [None Type](../types/None-Type.html) | Connect this port to another container's Sequence Input to make this container finish executing before that other container starts. |

## Group

[Control](../Functor-List.html#control)

## Notes

Initial Message, when set, is printed before the contained functors run; Final Message, when set, is printed only after all of them have finished running. Both are printed using the level set in Log Level. Sequence Output is produced only after Final Message has been printed.

Using this container with nothing placed inside it is not recommended unless its execution is ordered with Sequence Input and Sequence Output: with no contained functors and no sequence connections to order it against, when the message is actually printed relative to the rest of the model is unspecified.

This functor has no string-formatting capabilities of its own. To embed a computed value in a message, assemble the string first with [Create String](Create-String.html) and connect its result into Initial Message or Final Message; some types are also converted to a string automatically when connected directly.

## Example

Prints a message after a loop has finished. The message is never printed before the loop ends, but it is not necessarily printed right after it: other functors may run in between. The loop's Sequence Output is connected to the Sequence Input of an empty Print container. Sequence Input is the last optional input of Print, so it is bound by name:

```
// Loops over all the ids; loopDone is available only after the loop finishes.
loopDone := ForEach allIds {{
    // ...
}};

// Printed after the loop has finished, not necessarily right after it.
_ := Print { initialMessage = "Loop finished", sequenceInput = loopDone } {{ }};
```

## Internal Name

Print
{% endraw %}
