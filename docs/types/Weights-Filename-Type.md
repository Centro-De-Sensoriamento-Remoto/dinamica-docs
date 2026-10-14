---
title: "Weights Filename Type"
nav_order: 23
parent: "Type System"
grand_parent: "Core Concepts"
redirect_from:
  - /Weights-Filename-Type.html
---
{% raw %}
# Weights Filename Type

A Weights Filename is a filename referring to a file containing [Weights of Evidence](Weights-Type.html) coefficients or ranges. The file's format is automatically selected based on the filename's extension, and if no path is given, the file is located relative to the model script. Valid extensions are `.dcf`, `.txt`, and `.csv`.

## GUI Editor

The weights filename editor presents a file browser for selecting the target weights file, or typing its path directly.

## EGO Script

A Weights Filename constant is written in [EGO Script](../EGO-Script.html) the same way as a [String](String-Type.html) literal, enclosed in double quotes — see [Constants](../EGO-Script.html#constants) for the general filename validation rules:

```
"c:/data/deforestation_weights.csv"
```

## Automatic Conversions

- **Converted from**: [String Type](String-Type.html), [Generic Filename Type](Generic-Filename-Type.html), and [Table Value Type](Table-Value-Type.html).
- **Converted to**: [String Type](String-Type.html), [Generic Filename Type](Generic-Filename-Type.html), and [Table Value Type](Table-Value-Type.html).

See [Type System](../Type-System.html) for the complete conversion reference across all types.
{% endraw %}
