---
title: "Receive Table"
nav_order: 11
parent: "Integration Functors"
grand_parent: "Functor List"
---
{% raw %}
# Receive Table

## Description

Receives a table sent by an external application, such as an R script, through an opened communication session.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Tag | [String Type](../types/String-Type.html) | Identifier used to match this table with the corresponding send call in the external application. | Empty |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Table Type](../types/Table-Type.html) | Received table. |

## Group

[Integration](../Functor-List.html#integration)

## Notes

This functor blocks until the table is received.

Raises an error if no communication session is open.

See External Communication for how to open a session from an external application and exchange data with it, and for the conventions used to represent a table's key columns during the transfer.

## Internal Name

ReceiveTable
{% endraw %}
