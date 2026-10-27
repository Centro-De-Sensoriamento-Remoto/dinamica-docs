---
title: "Struct Type"
nav_order: 50
parent: "Type System"
grand_parent: "Core Concepts"
---
{% raw %}
# Struct Type

A struct is a container that bundles multiple named values, possibly of different types, into a single value. Each item is retrieved from a struct by name using the matching **Extract Struct** functor for its type.

A struct is also the output of [Calculate Multiple Maps](../functors/Calculate-Multiple-Maps.html), which returns one [Map](Map-Type.html) for each field of its expression; each map is retrieved with [Extract Struct Map](../functors/Extract-Struct-Map.html), passing the name of the field.

A struct's other main use is as the output of [Calculate Python Expression](../functors/Calculate-Python-Expression.html) and [Calculate R Expression](../functors/Calculate-R-Expression.html). An external Python or R script can produce more than one result in a single run, so both functors collect everything the script assigns to `dinamica.outputs` into one struct, returned through a single `result` output port. Each named value is then unpacked downstream with the extractor matching its type: [Extract Struct Number](../functors/Extract-Struct-Number.html) for a [Real Value](Real-Value-Type.html), [Extract Struct String](../functors/Extract-Struct-String.html) for a [String](String-Type.html), [Extract Struct Table](../functors/Extract-Struct-Table.html) for a [Table](Table-Type.html), [Extract Struct Tuple](../functors/Extract-Struct-Tuple.html) for a [Tuple](Tuple-Type.html), and [Extract Struct Lookup Table](../functors/Extract-Struct-Lookup-Table.html) for a [Lookup Table](Lookup-Table-Type.html). Each takes the struct and the item's name, and fails if the struct has no item under that name with that type.

## GUI Editor

A struct cannot be edited. As with [Map](Map-Type.html) and [Categorical Map](Categorical-Map-Type.html), its carrier functor's own input is non-editable — a struct can only be produced by connecting the output of another functor, never typed in directly.

## EGO Script

Since a struct can't be edited, it also can't be written as a literal in a script. It's always obtained by calling a functor that produces one, and reused by referencing the variable bound to its output:

```
result := CalculatePythonExpression code;
total := ExtractStructNumber result "total";
label := ExtractStructString result "label";
```

## Automatic Conversions

Structs can't be converted to or from any other type.

See [Type System](../Type-System.html) for the complete conversion reference across all types.
{% endraw %}
