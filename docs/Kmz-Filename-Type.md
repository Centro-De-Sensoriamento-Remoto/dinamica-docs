---
title: "Kmz Filename Type"
nav_exclude: true
---
{% raw %}
# Kmz Filename Type

A Kmz Filename is a filename referring to a compressed KML (`.kmz`) file on disk, used to load or save [Kml](Kml-Type.html) data. If no path is given, the file is located relative to the model script.

## GUI Editor

The kmz filename editor presents a file browser for selecting the target kmz file, or typing its path directly.

## EGO Script

A Kmz Filename constant is written in [EGO Script](EGO-Script.html) the same way as a [String](String-Type.html) literal, enclosed in double quotes — see [Constants](EGO-Script.html#constants) for the general filename validation rules:

```
"c:/data/boundaries.kmz"
```

## Automatic Conversions

- **Converted from**: [String Type](String-Type.html).
- **Converted to**: [String Type](String-Type.html).

See [Type System](Type-System.html) for the complete conversion reference across all types.
{% endraw %}
