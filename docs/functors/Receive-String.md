---
title: "Receive String"
nav_order: 10
parent: "Integration Functors"
grand_parent: "Functor List"
redirect_from:
  - /Receive-String.html
---
{% raw %}
# Receive String

## Description

Receives a string sent by an external application, such as an R script, through an opened communication session.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Tag | [String Type](../types/String-Type.html) | Identifier used to match this string with the corresponding send call in the external application. | Empty |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| String | [String Type](../types/String-Type.html) | Received string. |

## Group

[Integration](../Functor-List.html#integration)

## Notes

This functor blocks until the string is received.

Raises an error if no communication session is open.

See External Communication for how to open a session from an external application and exchange data with it.

## Internal Name

ReceiveString
{% endraw %}
