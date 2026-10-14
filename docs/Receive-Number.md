---
title: "Receive Number"
nav_exclude: true
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
| Tag | [String Type](String-Type.html) | Identifier used to match this number with the corresponding send call in the external application. | Empty |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Number | [Real Value Type](Real-Value-Type.html) | Received number. |

## Group

[Integration](Functor-List.html#integration)

## Notes

This functor blocks until the number is received.

Raises an error if no communication session is open.

See External Communication for how to open a session from an external application and exchange data with it.

## Internal Name

ReceiveNumber
{% endraw %}
