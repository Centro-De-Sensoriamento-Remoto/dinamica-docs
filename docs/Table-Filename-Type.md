---
title: "Table Filename Type"
nav_exclude: true
---
{% raw %}
# Table Filename Type

A Table Filename is a filename referring to a table file on disk. The file's format is automatically selected based on the filename's extension, and if no path is given, the file is located relative to the model script.

## GUI Editor

The table filename editor presents a file browser for selecting the target table file, or typing its path directly.

## EGO Script

A Table Filename constant is written in [EGO Script](EGO-Script.html) the same way as a [String](String-Type.html) literal, enclosed in double quotes — see [Constants](EGO-Script.html#constants) for the general filename validation rules:

```
"c:/data/population.csv"
```

## Automatic Conversions

- **Converted from**: [String Type](String-Type.html), [Generic Filename Type](Generic-Filename-Type.html), and [Table Value Type](Table-Value-Type.html).
- **Converted to**: [String Type](String-Type.html), [Generic Filename Type](Generic-Filename-Type.html), and [Table Value Type](Table-Value-Type.html).

See [Type System](Type-System.html) for the complete conversion reference across all types.
{% endraw %}
