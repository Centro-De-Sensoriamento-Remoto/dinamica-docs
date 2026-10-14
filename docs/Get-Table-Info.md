---
title: "Get Table Info"
nav_exclude: true
---
{% raw %}
# Get Table Info

## Description

Gets information about the columns of a given input table or lookup table.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Base Table Type](Base-Table-Type.html) | Input table or lookup table whose column information will be retrieved. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Table Info | [Table Type](Table-Type.html) | Table with detailed information about every input table column, in the format "Column_Index\*:real, Column_Name:string, Is_Key_Column:real, Column_Type:real, Column_Type_Name:string". Is_Key_Column is 1 for a key column and 0 for a data column; Column_Type is 0 for a string column and 1 for a real (numeric) column; Column_Type_Name spells out the same information as "string" or "real". |
| Column Names | [Table Type](Table-Type.html) | Table mapping each input table column's name to its index, in the format "Column_Name\*:string, Column_Index:real". |

## Group

[Table](Functor-List.html#table)

## Notes

Table Info has the following format:

| Column Name | Key or Data? | Column Type | Description |
| --- | --- | --- | --- |
| "Column_Index" | Key | Real | Index of the corresponding table column. |
| "Column_Name" | Data | String | Name of the corresponding table column. |
| "Is_Key_Column" | Data | Real | 1 if the corresponding column is a key column, 0 if it is a data column. |
| "Column_Type" | Data | Real | 0 if the column holds strings, 1 if it holds real numbers. |
| "Column_Type_Name" | Data | String | Name of the column type: "string" or "real". |

Column Names has the following format:

| Column Name | Key or Data? | Column Type | Description |
| --- | --- | --- | --- |
| "Column_Name" | Key | String | Name of the corresponding table column. |
| "Column_Index" | Data | Real | Index of the corresponding table column. |

## Internal Name

GetTableInfo
{% endraw %}
