---
title: "Lookup Table Filename Type"
nav_exclude: true
---
{% raw %}
# Lookup Table Filename Type

A Lookup Table Filename is a filename referring to a lookup table file on disk. If no path is given, the file is located relative to the model script. The only valid extension is `.csv`.

## GUI Editor

The lookup table filename editor presents a file browser for selecting the target lookup table file, or typing its path directly.

## EGO Script

A Lookup Table Filename constant is written in [EGO Script](EGO-Script.html) the same way as a [String](String-Type.html) literal, enclosed in double quotes — see [Constants](EGO-Script.html#constants) for the general filename validation rules:

```
"c:/data/transition_rates.csv"
```

## Automatic Conversions

- **Converted from**: [String Type](String-Type.html), [Generic Filename Type](Generic-Filename-Type.html), and [Table Value Type](Table-Value-Type.html).
- **Converted to**: [String Type](String-Type.html), [Generic Filename Type](Generic-Filename-Type.html), and [Table Value Type](Table-Value-Type.html).

See [Type System](Type-System.html) for the complete conversion reference across all types.
{% endraw %}
