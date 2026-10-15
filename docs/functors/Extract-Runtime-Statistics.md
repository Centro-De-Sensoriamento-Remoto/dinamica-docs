---
title: "Extract Runtime Statistics"
nav_order: 1
parent: "Tools Functors"
grand_parent: "Functor List"
---
{% raw %}
# Extract Runtime Statistics

## Description

Executes the contained functors and extracts information about their execution. The following items are calculated:

1. Number of elapsed seconds spent executing the contained functors.

## Inputs

None.

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| attributes | [Lookup Table Type](../types/Lookup-Table-Type.html) | Table containing the extracted information. |

## Group

[Tools](../Functor-List.html#tools)

## Notes

The output table is keyed by an integer attribute code. Currently only attribute 1 is populated, holding the number of seconds spent running the contained functors.

## Internal Name

ExtractRuntimeStatistics
{% endraw %}
