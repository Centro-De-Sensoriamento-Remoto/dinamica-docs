---
title: "Receive Number"
nav_order: 10
parent: "Integration Functors"
grand_parent: "Functor List"
---
{% raw %}
# Receive Number

## Description

Receives a number sent by an external application, such as an R script, through an opened communication session.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Tag | [String Type](../types/String-Type.html) | Identifier used to match this number with the corresponding send call in the external application. | Empty |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Number | [Real Value Type](../types/Real-Value-Type.html) | Received number. |

## Group

[Integration](../Functor-List.html#integration)

## Notes

This functor blocks until the number is received.

Raises an error if no communication session is open.

See External Communication for how to open a session from an external application and exchange data with it.

## Internal Name

ReceiveNumber
{% endraw %}
