---
title: "Save Map"
nav_order: 11
parent: "Input / Output Functors"
grand_parent: "Functor List"
redirect_from:
  - /Save-Map.html
---
{% raw %}
# Save Map

## Description

Saves a map to a file. The file format is determined automatically from the filename's extension.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Map to be saved. |
| Filename | [Map Filename Type](../types/Map-Filename-Type.html) | Name and path of the file the map is saved to. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Suffix Digits | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Number of digits used to render Step as a filename suffix. If Step needs more digits than this, it is used unmodified. If zero, no suffix is added. This is an advanced port. | 2 |
| Step | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Model step that produced the file, appended to Filename as a numeric suffix; automatically bound to the innermost compatible container. This is an advanced port. | .none |
| Use Compression | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, the saved map's cells are compressed, for output formats that support it; ignored by formats that do not. This is an advanced port. | Yes |
| Workdir | [Workdir Type](../types/Workdir-Type.html) | Work directory Filename is relative to; may be a folder or a Zip archive. When not bound, the directory containing the script is used. This is an advanced port. | .none |
| Ignore Costly Sparse Categories | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, a sparse categorization whose consecutive category values differ by very large gaps is discarded rather than saved, avoiding a costly representation. This is an advanced port. | Yes |

## Outputs

None.

## Group

[Input / Output](../Functor-List.html#input--output)

## Notes

If Step is .none, the saved filename has no numeric suffix.

See Lesson 4, "Opening and Saving maps," for a practical example of this functor.

## Internal Name

SaveMap

## Usage examples

See practical examples of this functor in Lesson 4: Opening and Saving maps
{% endraw %}
