---
title: "Load Lookup Table"
nav_exclude: true
---
{% raw %}
# Load Lookup Table

## Description

Loads a lookup table from a file. The file format is determined automatically from the filename's extension.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Filename | [Lookup Table Filename Type](Lookup-Table-Filename-Type.html) | Name and path of the file to load. If no path is given, the file is located relative to the model script. Only two-column CSV (comma-separated values) format is accepted. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Suffix Digits | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Number of digits used to render Step as a filename suffix. If Step needs more digits than this, it is used unmodified. If zero, no suffix is added. This is an advanced port. | 0 |
| Step | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Current step or model iteration, appended to Filename as a numeric suffix; automatically bound to the innermost compatible container. This is an advanced port. | .none |
| Workdir | [Workdir Type](Workdir-Type.html) | Work directory Filename is relative to; may be a folder or a Zip archive. When not bound, the directory containing the script is used. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Lookup Table Type](Lookup-Table-Type.html) | Lookup table loaded from the file. |

## Group

[Input / Output](Functor-List.html#input--output)

## Notes

Only the CSV (comma-separated values) file format is supported.

If Step is .none, the loaded filename has no numeric suffix.

It is possible to load lookup tables from [Zip](https://en.wikipedia.org/wiki/zip_(file_format)) archives; Workdir may point directly to a Zip archive rather than a folder. See this useful tip to know how to do it.

## Internal Name

LoadLookupTable
{% endraw %}
