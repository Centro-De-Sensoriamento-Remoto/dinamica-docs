---
title: "Send Tuple"
nav_order: 17
parent: "Integration Functors"
grand_parent: "Functor List"
---
{% raw %}
# Send Tuple

## Description

Sends a tuple of numbers to an external application, such as an R script, through an opened communication session.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Tuple | [Tuple Type](../types/Tuple-Type.html) | Tuple of numbers to send. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Tag | [String Type](../types/String-Type.html) | Identifier used to match this tuple with the corresponding receive call in the external application. | Empty |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Out Tuple | [Tuple Type](../types/Tuple-Type.html) | The tuple of numbers that was sent. |

## Group

[Integration](../Functor-List.html#integration)

## Notes

This functor blocks until the tuple is sent.

Raises an error if no communication session is open.

In R, a tuple corresponds to a list or vector of real values, sent or received with Dinamica::sendNumberVector() and Dinamica::receiveNumberVector(). See External Communication for how to open a session from an external application and exchange data with it.

## Internal Name

SendTuple
{% endraw %}
