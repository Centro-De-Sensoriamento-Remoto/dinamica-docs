---
title: "Get Table Value"
nav_order: 14
parent: "Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Get Table Value

## Description

Gets a value from a table.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Table Type](../types/Table-Type.html) | Table to extract the value from. |
| Keys | [Tuple Type](../types/Tuple-Type.html) | Keys corresponding to the desired value. |
| Column | [Index Or Name Type](../types/Index-Or-Name-Type.html) | Column name or index where the value is located. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Value If Not Found | [Table Value Type](../types/Table-Value-Type.html) | Value returned if any of the given keys is not present in the table. If not provided, an error is reported when the keys are not found. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Table Value Type](../types/Table-Value-Type.html) | Value extracted from the table. |

## Group

[Table](../Functor-List.html#table)

## Notes

If the given keys are not found in the input table and Value If Not Found is not provided, this functor reports an error.

See [GetTableValue](../Manipulating-Tables-And-Lookup-Tables.html#gettablevalue) in [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for how this functor is used together with other table functors.

## Internal Name

GetTableValue
{% endraw %}
