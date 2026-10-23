---
title: "Folder Type"
nav_order: 16
parent: "Type System"
grand_parent: "Core Concepts"
---
{% raw %}
# Folder Type

A Folder value is a path to a folder, directory, or archive. When used by [Workdir](../functors/Workdir.html), it can also be a URL, an `s3://`, `mem://` or `vsi://` location, or a STACIT query. It's the required input to the [Workdir](../functors/Workdir.html) container — see [Workdir Type](Workdir-Type.html) for how that container turns a Folder path into an active working directory — and it's also what [Folder Junction](../functors/Folder-Junction.html) picks between when choosing one of two possible folders coming from different execution pipelines.

## GUI Editor

The folder editor presents a browser for selecting the target folder, directory, or zip archive, or typing its path directly.

## EGO Script

A Folder constant is written in [EGO Script](../EGO-Script.html) the same way as a [String](String-Type.html) literal, enclosed in double quotes:

```
"c:/data/"
```

## Automatic Conversions

- **Converted from**: [String Type](String-Type.html).
- **Converted to**: [String Type](String-Type.html).

See [Type System](../Type-System.html) for the complete conversion reference across all types.
{% endraw %}
