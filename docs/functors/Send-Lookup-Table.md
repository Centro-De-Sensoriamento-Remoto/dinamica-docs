---
title: "Send Lookup Table"
nav_order: 13
parent: "Integration Functors"
grand_parent: "Functor List"
---
{% raw %}
# Send Lookup Table

## Description

Sends a lookup table to an external application, such as an R script, through an opened communication session.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Lookup Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | Lookup table to send. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Tag | [String Type](../types/String-Type.html) | Identifier used to match this lookup table with the corresponding receive call in the external application. | Empty |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Out Lookup Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | The lookup table that was sent. |

## Group

[Integration](../Functor-List.html#integration)

## Notes

This functor blocks until the lookup table is sent.

Raises an error if no communication session is open.

See External Communication for how to open a session from an external application and exchange data with it.

## Internal Name

SendLookupTable
{% endraw %}
