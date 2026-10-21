---
title: "Extract Map Values"
nav_order: 8
parent: "Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Extract Map Values

## Description

Extracts every cell value of a map, together with its coordinates, into a single table with one row per cell.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Input map. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Keys Type | [Enum Type](../types/Enum-Type.html) | Determines how each output row's unique "Id" is generated. With Default, the id is assigned randomly when execution is parallel, or sequentially otherwise. With Use Map Values As Keys, the cell's own value is used as its id. With Use Coordinate Indexes as Keys, the cell's coordinate index (row-major position) is used as its id. | Default |
| Include Null Values | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, cells whose value equals Map's null value are also included in the output table. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Cells | [Table Type](../types/Table-Type.html) | Resulting table of cell values and coordinates. |

## Group

[Table](../Functor-List.html#table)

## Notes

Cells has the following format:

| Column Name | Key or Data? | Column Type | Description |
| --- | --- | --- | --- |
| "Id" | Key | Real | Unique row identifier, generated as determined by Keys Type. |
| "Value" | Data | Real | The cell's value. |
| "Line" | Data | Real | The cell's line, with the topmost line indexed as 1. |
| "Column" | Data | Real | The cell's column, with the leftmost column indexed as 1. |

By default, cells equal to Map's null value are skipped, unless Include Null Values is true.

Raises an error if Keys Type is Use Map Values As Keys and Map has more than one layer, since a cell value would then no longer be unique across layers.

See [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for techniques that combine the table and lookup table functors.

## Internal Name

ExtractMapValues
{% endraw %}
