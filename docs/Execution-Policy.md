---
title: "Execution Policy"
nav_exclude: true
---
{% raw %}
# Execution Policy

## Description

This container executes the functors it contains under a specified processor and parallelization policy, temporarily overriding the policy otherwise in effect for as long as its content runs.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Maximum Granularity | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Maximum granularity used to split a job into parallel tasks. Set to 0 to use the default granularity. | 0 |
| Force Specified Granularity | [Boolean Value Type](Boolean-Value-Type.html) | Always use the granularity specified in Maximum Granularity, even when the current granularity is already within that limit. | No |
| Computing Target | [Enum Type](Enum-Type.html) | How the contained functors should be run: Default suggests the use of accelerator computing devices when available, while still allowing regular processors to be used; Processors Only forces the use of regular processors; Accelerator Devices Only forces the use of accelerator computing devices, and raises an error during execution if none are available. | None |

## Outputs

None.

## Group

[Control](Functor-List.html#control)

## Notes

This functor was previously known as "ProcessorPolicy".

The policy in effect before this container ran is always restored once its content finishes executing, whether or not an error occurs.

## Internal Name

ExecutionPolicy
{% endraw %}
