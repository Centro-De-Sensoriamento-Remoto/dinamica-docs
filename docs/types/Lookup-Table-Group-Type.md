---
title: "Lookup Table Group Type"
nav_order: 28
parent: "Type System"
grand_parent: "Core Concepts"
---
{% raw %}
# Lookup Table Group Type

A Lookup Table Group is a generic collection of [Lookup Table](Lookup-Table-Type.html) values, each identified by a positive integer index. It's used where a functor needs to work with a whole set of lookup tables together rather than one at a time — for example, [Genetic Algorithm Tool](../functors/Genetic-Algorithm-Tool.html) represents each individual in its population as a Lookup Table Group, since a candidate solution there is typically made up of several related parameter lookup tables rather than a single one.

## GUI Editor

Input ports of type Lookup Table Group are non-editable, so a lookup table group cannot be defined using an editor in the graphical interface. A value must always come from connecting an output produced by another functor — [Create Lookup Table Group](../functors/Create-Lookup-Table-Group.html) assembles multiple lookup tables into a group, and [Extract Lookup Table From Lookup Table Group](../functors/Extract-Lookup-Table-From-Lookup-Table-Group.html) does the reverse, pulling a single [Lookup Table](Lookup-Table-Type.html) back out by its index.

## EGO Script

For the same reason, input ports of type Lookup Table Group cannot receive a constant in [EGO Script](../EGO-Script.html) — see [Constants](../EGO-Script.html#constants). A single Lookup Table also converts automatically wherever a Lookup Table Group is expected, so it can be connected directly without an intermediate step:

```
rates := [ 1991 0.02, 1993 0.025 ];
// rates converts automatically from LookupTable to LookupTableGroup here.
first := ExtractLookupTableFromLookupTableGroup rates 1;
```

## Automatic Conversions

- **Converted from**: [Table Type](Table-Type.html) and [Lookup Table Type](Lookup-Table-Type.html).
- **Converted to**: [Table Type](Table-Type.html), [Base Table Type](Base-Table-Type.html), and [Lookup Table Type](Lookup-Table-Type.html) — each of these narrowing conversions checks that every lookup table in the group actually fits the expected shape.

See [Type System](../Type-System.html#table-format-of-table-shaped-types) for how a Lookup Table Group's format is treated as a generic collection rather than a single fixed shape, and for the complete conversion reference across all types.
{% endraw %}
