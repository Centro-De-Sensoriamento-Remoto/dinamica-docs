---
title: "Select String"
nav_order: 6
parent: "Stack Functors"
grand_parent: "Functor List"
redirect_from:
  - /Select-String.html
---
{% raw %}
# Select String

## Description

This container picks a string out of a series of strings identified by [Number String](Number-String.html) functors placed inside it, using an index to choose among them.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Step | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Current index, step, or model iteration, used to pick the string. When this functor is placed inside a loop container, this port connects to that container's current step automatically. | Provided automatically |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| String | [String Type](../types/String-Type.html) | String picked out of those present in the series. |

## Group

[Stack](../Functor-List.html#stack)

## Notes

The string selected is the one identified with the greatest index that is still less than or equal to Step.

Strings are identified using an index assigned by a [Number String](Number-String.html) functor placed inside this container.

This container must hold at least one [Number String](Number-String.html) instance; otherwise the model raises an error. If Step is smaller than every index assigned inside the container, the model also raises an error.

## Internal Name

SelectString
{% endraw %}
