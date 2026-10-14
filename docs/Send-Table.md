---
title: "Send Table"
nav_exclude: true
---
{% raw %}
# Send Table

## Description

Sends a table to an external application, such as an R script, through an opened communication session.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Table Type](Table-Type.html) | Table to send. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Tag | [String Type](String-Type.html) | Identifier used to match this table with the corresponding receive call in the external application. | Empty |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Out Table | [Table Type](Table-Type.html) | The table that was sent. |

## Group

[Integration](Functor-List.html#integration)

## Notes

This functor blocks until the table is sent.

Raises an error if no communication session is open.

See External Communication for how to open a session from an external application and exchange data with it, and for the conventions used to represent a table's key columns during the transfer.

## Internal Name

SendTable
{% endraw %}
