---
title: "Step"
nav_order: 32
parent: "Control Functors"
grand_parent: "Functor List"
---
{% raw %}
# Step

## Description

Receives and passes on the current step or iteration of the innermost loop container holding this functor.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Step | [Real Value Type](../types/Real-Value-Type.html) | Current step or model iteration. When this functor is placed inside a loop container, this port connects to that container's current step automatically. | Provided automatically |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Step | [Real Value Type](../types/Real-Value-Type.html) | Current step or model iteration. |

## Group

[Control](../Functor-List.html#control)

## Notes

This functor should be placed directly or indirectly inside a loop container. Placing it outside any loop container, connecting Step to a functor that is not a loop container, or setting Step to a fixed constant, all report a warning.

## Internal Name

Step
{% endraw %}
