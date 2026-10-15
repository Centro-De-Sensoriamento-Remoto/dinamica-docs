---
title: "Load Text File"
nav_order: 7
parent: "Input / Output Functors"
grand_parent: "Functor List"
---
{% raw %}
# Load Text File

## Description

Loads text from a file.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Filename | [Generic Filename Type](../types/Generic-Filename-Type.html) | Name and path of the file to load. If no path is given, the file is located relative to the model script. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Suffix Digits | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Number of digits used to render Step as a filename suffix. If Step needs more digits than this, it is used unmodified. If zero, no suffix is added. This is an advanced port. | 0 |
| Step | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Current step or model iteration, appended to Filename as a numeric suffix; automatically bound to the innermost compatible container. This is an advanced port. | .none |
| Workdir | [Workdir Type](../types/Workdir-Type.html) | Work directory Filename is relative to; may be a folder or a Zip archive. When not bound, the directory containing the script is used. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Text | [String Type](../types/String-Type.html) | Text loaded from the file. |

## Group

[Input / Output](../Functor-List.html#input--output)

## Notes

If Step is .none, the loaded filename has no numeric suffix.

## Internal Name

LoadTextFile
{% endraw %}
