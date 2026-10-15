---
title: "For Each"
nav_order: 7
parent: "Control Functors"
grand_parent: "Functor List"
---
{% raw %}
# For Each

## Description

Container that executes the functors it contains once for every entry of a given table or lookup table, making each entry's key available to its contents through the internal output port Step.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Elements | [Base Table Type](../types/Base-Table-Type.html) | Table or lookup table whose entries the contained functors are executed for. |

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
| Step | [Real Value Type](../types/Real-Value-Type.html) | Key of the current element being processed. |

## Group

[Control](../Functor-List.html#control)

## Notes

Execution only takes place for entries whose key is greater than or equal to zero and whose associated value is non-zero; other entries in Elements are skipped.

Execution for multiple keys may happen simultaneously when there is no dependency between them.

When Elements can be empty and a result produced by the contained functors is used outside the container, connect a matching [junction](../Functor-List.html#junction) after the container, so a value still reaches the rest of the model if there are no entries to process.

This functor was previously known as "ParallelForEach"; that name is still accepted for backward compatibility with existing scripts.

## Internal Name

ForEach
{% endraw %}
