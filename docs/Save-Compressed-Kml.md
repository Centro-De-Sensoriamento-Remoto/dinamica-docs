---
title: "Save Compressed Kml"
nav_exclude: true
---
{% raw %}
# Save Compressed Kml

## Description

Saves a KML as a compressed KMZ file, bundling every link it uses into the archive.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Kml Type](Kml-Type.html) | KML to be saved. |
| Filename | [Kmz Filename Type](Kmz-Filename-Type.html) | Name and path of the KMZ file the KML is saved to. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Suffix Digits | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Number of digits used to render Step as a filename suffix. If Step needs more digits than this, it is used unmodified. If zero, no suffix is added. This is an advanced port. | 2 |
| Step | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Model step that produced the file, appended to Filename as a numeric suffix; automatically bound to the innermost compatible container. This is an advanced port. | .none |
| Workdir | [Workdir Type](Workdir-Type.html) | Work directory Filename is relative to; may be a folder or a Zip archive. When not bound, the directory containing the script is used. This is an advanced port. | .none |

## Outputs

None.

## Group

[Input / Output](Functor-List.html#input--output)

## Notes

If Step is .none, the saved filename has no numeric suffix.

## Internal Name

SaveCompressedKml
{% endraw %}
