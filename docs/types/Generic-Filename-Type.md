---
title: "Generic Filename Type"
nav_order: 17
parent: "Type System"
grand_parent: "Core Concepts"
redirect_from:
  - /Generic-Filename-Type.html
---
{% raw %}
# Generic Filename Type

A Generic Filename is a filename with no specific format requirement. Unlike [Map Filename Type](Map-Filename-Type.html), [Table Filename Type](Table-Filename-Type.html), [Lookup Table Filename Type](Lookup-Table-Filename-Type.html), and [Weights Filename Type](Weights-Filename-Type.html) — each of which expects an extension matching its own file format — a Generic Filename accepts any file path. [Generate Temporary File](../functors/Generate-Temporary-File.html) is a typical source of one, since a temporary file isn't tied to any particular format.

## GUI Editor

The generic filename editor presents a file browser for selecting the target file, or typing its path directly.

## EGO Script

A Generic Filename constant is written in [EGO Script](../EGO-Script.html) the same way as a [String](String-Type.html) literal, enclosed in double quotes — see [Constants](../EGO-Script.html#constants) for the general filename validation rules:

```
"c:/data/output.txt"
```

## Automatic Conversions

- **Converted from**: [String Type](String-Type.html), [Map Filename Type](Map-Filename-Type.html), [Table Filename Type](Table-Filename-Type.html), [Lookup Table Filename Type](Lookup-Table-Filename-Type.html), [Weights Filename Type](Weights-Filename-Type.html), and [Table Value Type](Table-Value-Type.html).
- **Converted to**: [String Type](String-Type.html), [Map Filename Type](Map-Filename-Type.html), [Table Filename Type](Table-Filename-Type.html), [Lookup Table Filename Type](Lookup-Table-Filename-Type.html), [Weights Filename Type](Weights-Filename-Type.html), and [Table Value Type](Table-Value-Type.html).

See [Type System](../Type-System.html) for the complete conversion reference across all types.
{% endraw %}
