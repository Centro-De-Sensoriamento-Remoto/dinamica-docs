---
title: "Create Connection Info"
nav_order: 1
parent: "Distributed Functors"
grand_parent: "Functor List"
redirect_from:
  - /Create-Connection-Info.html
---
{% raw %}
# Create Connection Info

## Description

Builds a connection info value from an address and a port number, so it can be passed to a functor such as [Run Remotely](Run-Remotely.html) instead of relying on the connection details configured in the application settings.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Address | [String Type](../types/String-Type.html) | Hostname, IPv4, or IPv6 address. IPv4 addresses are divided into four octets, each a number between 0 and 255, separated by dots (e.g., 192.168.0.1). IPv6 addresses are divided into eight groups of four hexadecimal digits, separated by colons (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334). | Empty |
| Port | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Port number, in the range 1 to 65535. | None |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Connection Info Type](../types/Connection-Info-Type.html) | Connection info built from Address and Port. |

## Group

[Distributed](../Functor-List.html#distributed)

## Notes

Reports an error if Port is outside the range 1 to 65535.

## Internal Name

CreateConnectionInfo
{% endraw %}
