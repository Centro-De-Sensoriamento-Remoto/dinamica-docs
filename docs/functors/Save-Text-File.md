---
title: "Save Text File"
nav_order: 13
parent: "Input / Output Functors"
grand_parent: "Functor List"
redirect_from:
  - /Save-Text-File.html
---
{% raw %}
# Save Text File

## Description

Saves text to a file.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Text | [String Type](../types/String-Type.html) | Text to be saved. |
| Filename | [Generic Filename Type](../types/Generic-Filename-Type.html) | Name and path of the file the text is saved to. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Suffix Digits | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Number of digits used to render Step as a filename suffix. If Step needs more digits than this, it is used unmodified. If zero, no suffix is added. This is an advanced port. | 2 |
| Step | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Model step that produced the file, appended to Filename as a numeric suffix; automatically bound to the innermost compatible container. This is an advanced port. | .none |
| Workdir | [Workdir Type](../types/Workdir-Type.html) | Work directory Filename is relative to; may be a folder or a Zip archive. When not bound, the directory containing the script is used. This is an advanced port. | .none |

## Outputs

None.

## Group

[Input / Output](../Functor-List.html#input--output)

## Notes

If Step is .none, the saved filename has no numeric suffix.

## Internal Name

SaveTextFile
{% endraw %}
