---
title: "Receive Tuple"
nav_order: 13
parent: "Integration Functors"
grand_parent: "Functor List"
---
{% raw %}
# Receive Tuple

## Description

Receives a tuple of numbers sent by an external application, such as an R script, through an opened communication session.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Tag | [String Type](../types/String-Type.html) | Identifier used to match this tuple with the corresponding send call in the external application. | Empty |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Tuple | [Tuple Type](../types/Tuple-Type.html) | Received tuple of numbers. |

## Group

[Integration](../Functor-List.html#integration)

## Notes

This functor blocks until the tuple is received.

Raises an error if no communication session is open.

In R, a tuple corresponds to a list or vector of real values, sent or received with Dinamica::sendNumberVector() and Dinamica::receiveNumberVector(). See External Communication for how to open a session from an external application and exchange data with it.

## Internal Name

ReceiveTuple
{% endraw %}
