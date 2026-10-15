---
title: "Base Table Type"
nav_order: 26
parent: "Type System"
grand_parent: "Core Concepts"
---
{% raw %}
# Base Table Type

A **Base Table** is the common supertype shared by [Table](Table-Type.html) and [Lookup Table](Lookup-Table-Type.html): both are subtypes of Base Table Type, so a Table or a Lookup Table can be connected directly to any port declared as Base Table Type, with no conversion involved. It exists purely to let a functor accept either shape generically — [Number Table](../functors/Number-Table.html), [Get Table Info](../functors/Get-Table-Info.html), and [Get Table Keys](../functors/Get-Table-Keys.html) all take a Base Table Type input specifically so they work the same way whether they're given a Table or a Lookup Table.

There is no dedicated carrier functor for Base Table Type, and no way to hold one as a standalone value — a Base Table always begins life as an actual Table or Lookup Table; "Base Table" is only ever the port's declared type, not something separately constructed.

## GUI Editor

Base Table Type ports are non-editable — no port anywhere in the interface is declared as Base Table Type and also editable. A value only reaches one by being a Table or Lookup Table connected in from elsewhere.

## EGO Script

For the same reason, Base Table Type has no literal constant syntax in [EGO Script](../EGO-Script.html) — see [Constants](../EGO-Script.html#constants). Any variable bound to a [Table](Table-Type.html) or [Lookup Table](Lookup-Table-Type.html) can be passed directly wherever a Base Table Type input is expected:

```
landCover := Table [
  "Category*", "Area",
  1, 450.2,
  2, 129.8
];

// landCover satisfies the BaseTable input directly -- it's a Table, and
// Table is a subtype of Base Table Type, so nothing needs to convert.
info := GetTableInfo landCover;
```

## Automatic Conversions

- **Converted from**: [Table Type](Table-Type.html) and [Lookup Table Type](Lookup-Table-Type.html) — this is **subtyping**: both are already, structurally, a Base Table, so no conversion logic runs. [Lookup Table Group Type](Lookup-Table-Group-Type.html).
- **Converted to**: [Table Type](Table-Type.html) and [Lookup Table Type](Lookup-Table-Type.html) — each can fail, since Base Table Type is a generic container and these only succeed if what it actually holds is already shaped like the target.

See [Type System](../Type-System.html) for the complete conversion reference across all types.
{% endraw %}
