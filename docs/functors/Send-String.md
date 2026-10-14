---
title: "Send String"
nav_order: 15
parent: "Integration Functors"
grand_parent: "Functor List"
redirect_from:
  - /Send-String.html
---
{% raw %}
# Send String

## Description

Sends a string to an external application, such as an R script, through an opened communication session.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| String | [String Type](../types/String-Type.html) | String to send. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Tag | [String Type](../types/String-Type.html) | Identifier used to match this string with the corresponding receive call in the external application. | Empty |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Out String | [String Type](../types/String-Type.html) | The string that was sent. |

## Group

[Integration](../Functor-List.html#integration)

## Notes

This functor blocks until the string is sent.

Raises an error if no communication session is open.

See External Communication for how to open a session from an external application and exchange data with it.

## Internal Name

SendString
{% endraw %}
