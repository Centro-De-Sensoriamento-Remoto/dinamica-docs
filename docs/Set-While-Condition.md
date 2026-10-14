---
title: "Set While Condition"
nav_exclude: true
---
{% raw %}
# Set While Condition

## Description

Sets the condition that the innermost [While](While.html) or [Do While](Do-While.html) container holding this functor uses to decide whether it keeps looping.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Condition | [Boolean Value Type](Boolean-Value-Type.html) | Value to be used as the loop condition. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Condition | [Boolean Value Type](Boolean-Value-Type.html) | Value passed on to the enclosing loop container. |

## Group

[Control](Functor-List.html#control)

## Notes

This functor must be placed inside the [While](While.html) or [Do While](Do-While.html) container whose looping condition it sets; its output connects automatically to that container's internal condition input.

## Internal Name

SetWhileCondition
{% endraw %}
