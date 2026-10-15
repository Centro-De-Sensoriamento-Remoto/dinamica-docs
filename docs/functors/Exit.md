---
title: "Exit"
nav_order: 4
parent: "Control Functors"
grand_parent: "Functor List"
---
{% raw %}
# Exit

## Description

Aborts the execution of the model, optionally showing a message explaining why.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Message | [String Type](../types/String-Type.html) | Message explaining the reason for cancelling the execution. When provided, it is shown to the user; otherwise, the execution is cancelled silently. | None |

## Outputs

None.

## Group

[Control](../Functor-List.html#control)

## Notes

When Message is provided and is not empty once leading and trailing spaces are removed, the execution is aborted and the message is shown to the user as the reason. When Message is left empty, or contains only spaces, the execution is cancelled silently instead.

## Internal Name

Exit
{% endraw %}
