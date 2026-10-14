---
title: "Group"
nav_order: 10
parent: "Control Functors"
grand_parent: "Functor List"
redirect_from:
  - /Group.html
---
{% raw %}
# Group

## Description

Executes the functors it contains as a single step. This container has no effect of its own beyond organizing part of a model visually, or forcing an execution order through its Sequence Input and Sequence Output ports.

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

## Group

[Control](../Functor-List.html#control)

## Notes

Group is a convenient way to group a set of functors visually; they do not need to be connected to one another to form a data flow chain.

## Internal Name

Group
{% endraw %}
