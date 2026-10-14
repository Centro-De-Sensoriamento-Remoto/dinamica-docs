---
title: "Load Categorical Map"
nav_exclude: true
---
{% raw %}
# Load Categorical Map

## Description

Loads a categorical map — a map whose cells represent classes or categories — from a file. The file format is determined automatically from the filename's extension. If the loaded file does not already carry a categorization, one is determined automatically from the map's cell values. See [Load Map](Load-Map.html) for loading maps whose cells do not represent categories.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Filename | [Map Filename Type](Map-Filename-Type.html) | Name and path of the file to load. If no path is given, the file is located relative to the model script. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Null Value | [Null Value Type](Null-Value-Type.html) | Additional value to treat as null, alongside the file's own null value if it has one. Useful for assigning a null value to files that do not define one. | .none |
| Storage Mode | [Enum Type](Enum-Type.html) | Hint for how the map should be handled: Default follows the memory allocation policy in the application settings; Prefer Memory suggests loading the whole map into memory; Prefer Disk suggests keeping it on disk and loading it on demand, piece by piece; Load As Sparse suggests storing only non-null cells, minimizing storage at the expense of access time. This is only a hint and may be ignored. This is an advanced port. | Default |
| Suffix Digits | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Number of digits used to render Step as a filename suffix. If Step needs more digits than this, it is used unmodified. If zero, no suffix is added. This is an advanced port. | 0 |
| First Window Coordinate X | [Real Value Type](Real-Value-Type.html) | X coordinate of one corner of a crop window, in the map's projection units. Must lie within the file's extent. This is an advanced port. | .none |
| First Window Coordinate Y | [Real Value Type](Real-Value-Type.html) | Y coordinate of one corner of a crop window, in the map's projection units. Must lie within the file's extent. This is an advanced port. | .none |
| Second Window Coordinate X | [Real Value Type](Real-Value-Type.html) | X coordinate of the opposite corner of the crop window, in the map's projection units. Must lie within the file's extent. This is an advanced port. | .none |
| Second Window Coordinate Y | [Real Value Type](Real-Value-Type.html) | Y coordinate of the opposite corner of the crop window, in the map's projection units. Must lie within the file's extent. This is an advanced port. | .none |
| Recreate Categories | [Boolean Value Type](Boolean-Value-Type.html) | If true, the categorization is recreated from the loaded image's values, while preserving any categories already stored in the file. This is an advanced port. | No |
| Step | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Current step or model iteration, appended to Filename as a numeric suffix; automatically bound to the innermost compatible container. This is an advanced port. | .none |
| Workdir | [Workdir Type](Workdir-Type.html) | Work directory Filename is relative to; may be a folder or a Zip archive. When not bound, the directory containing the script is used. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Categorical Map Type](Categorical-Map-Type.html) | Loaded categorical map. |

## Group

[Input / Output](Functor-List.html#input--output)

## Notes

When Null Value is given, any cell already equal to the file's own null value (if it defines one) is converted to Null Value, and any non-null cell that happens to equal Null Value is likewise promoted to null — so a value that meant "no data" before loading still means "no data" after, regardless of how the null definition changed.

The crop window (First/Second Window Coordinate X/Y) must either be left entirely at .none, loading the map in full, or have all four coordinates defined together; a partially defined window is not accepted.

If Step is .none, the loaded filename has no numeric suffix.

For a list of file formats that Load Categorical Map can load, the supported [projections](https://en.wikipedia.org/wiki/Map_projection) and [datums](https://en.wikipedia.org/wiki/Datum_(geodesy)), check the supported map formats.

It is possible to load maps from [Zip](https://en.wikipedia.org/wiki/zip_(file_format)) archives; Workdir may point directly to a Zip archive rather than a folder. See this useful tip to know how to do it.

## Internal Name

LoadCategoricalMap
{% endraw %}
