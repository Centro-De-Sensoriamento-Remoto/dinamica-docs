---
title: "Save Lookup Table"
nav_order: 10
parent: "Input / Output Functors"
grand_parent: "Functor List"
redirect_from:
  - /Save-Lookup-Table.html
---
{% raw %}
# Save Lookup Table

## Description

Saves a lookup table to a file. The file format is determined automatically from the filename's extension.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | Lookup table that will be written to the file. |
| Filename | [Lookup Table Filename Type](../types/Lookup-Table-Filename-Type.html) | Name and path of the file where the lookup table will be written. If no path is given, the file is located relative to the model script. Only CSV (comma-separated values) format is accepted. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Suffix Digits | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Number of digits used to render Step as a filename suffix. If Step needs more digits than this, it is used unmodified. If zero, no suffix is added. This is an advanced port. | 2 |
| Step | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Current step or model iteration, appended to Filename as a numeric suffix; automatically bound to the innermost compatible container. This is an advanced port. | .none |
| Workdir | [Workdir Type](../types/Workdir-Type.html) | Work directory Filename is relative to; may be a folder or a Zip archive. When not bound, the directory containing the script is used. This is an advanced port. | .none |

## Outputs

None.

## Group

[Input / Output](../Functor-List.html#input--output)

## Notes

Only the CSV (comma-separated values) file format is supported.

If Step is .none, the saved filename has no numeric suffix.

## Internal Name

SaveLookupTable
{% endraw %}
