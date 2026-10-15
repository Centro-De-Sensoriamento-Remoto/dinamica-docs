---
title: "Receive Lookup Table"
nav_order: 8
parent: "Integration Functors"
grand_parent: "Functor List"
---
{% raw %}
# Receive Lookup Table

## Description

Receives a lookup table sent by an external application, such as an R script, through an opened communication session.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Tag | [String Type](../types/String-Type.html) | Identifier used to match this lookup table with the corresponding send call in the external application. | Empty |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Lookup Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | Received lookup table. |

## Group

[Integration](../Functor-List.html#integration)

## Notes

This functor blocks until the lookup table is received.

Raises an error if no communication session is open.

See External Communication for how to open a session from an external application and exchange data with it.

## Internal Name

ReceiveLookupTable
{% endraw %}
