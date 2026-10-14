---
title: "Send Number"
nav_exclude: true
---
{% raw %}
# Send Number

## Description

Sends a number to an external application, such as an R script, through an opened communication session.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Number | [Real Value Type](Real-Value-Type.html) | Number to send. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Tag | [String Type](String-Type.html) | Identifier used to match this number with the corresponding receive call in the external application. | Empty |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Out Number | [Real Value Type](Real-Value-Type.html) | The number that was sent. |

## Group

[Integration](Functor-List.html#integration)

## Notes

This functor blocks until the number is sent.

Raises an error if no communication session is open.

See External Communication for how to open a session from an external application and exchange data with it.

## Internal Name

SendNumber
{% endraw %}
