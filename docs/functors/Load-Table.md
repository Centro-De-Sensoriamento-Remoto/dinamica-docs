---
title: "Load Table"
nav_order: 6
parent: "Input / Output Functors"
grand_parent: "Functor List"
redirect_from:
  - /Load-Table.html
---
{% raw %}
# Load Table

## Description

Loads a table from a file. The file format is determined automatically from the filename's extension.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Filename | [Table Filename Type](../types/Table-Filename-Type.html) | Name and path of the file to load. If no path is given, the file is located relative to the model script. Only multi-column CSV (comma-separated values) format is accepted. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Unique Id Key Column Creation | [Enum Type](../types/Enum-Type.html) | Behavior for adding an auto-incrementing unique-id key column at the start of the loaded table. Possible values are If Necessary (add the column only when the file needs one), Do Not Create, and Always. This is an advanced port. | If Necessary |
| Suffix Digits | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Number of digits used to render Step as a filename suffix. If Step needs more digits than this, it is used unmodified. If zero, no suffix is added. This is an advanced port. | 0 |
| Step | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Current step or model iteration, appended to Filename as a numeric suffix; automatically bound to the innermost compatible container. This is an advanced port. | .none |
| Workdir | [Workdir Type](../types/Workdir-Type.html) | Work directory Filename is relative to; may be a folder or a Zip archive. When not bound, the directory containing the script is used. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Table Type](../types/Table-Type.html) | Table loaded from the file. |

## Group

[Input / Output](../Functor-List.html#input--output)

## Notes

Only the CSV (comma-separated values) file format is supported.

If Step is .none, the loaded filename has no numeric suffix.

It is possible to load tables from [Zip](https://en.wikipedia.org/wiki/zip_(file_format)) archives; Workdir may point directly to a Zip archive rather than a folder. See this useful tip to know how to do it.

## Internal Name

LoadTable
{% endraw %}
