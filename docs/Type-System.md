---
title: "Type System"
nav_order: 7
---
{% raw %}
# Type System

## Overview

Every port in the engine has a **type**, and a port accepts a value if it's exactly that type — or if some path leads from the value's actual type to the port's. That path works one of two ways: most of the time it's a registered conversion, actual logic that runs when the connection is made; a few times it's subtyping instead, where the source type is already, structurally, a value of the target type and nothing needs to run at all. This page lists both together in the same tables — see [Converters and subtyping](#converters-and-subtyping) below for how the two are told apart.

Each type here is implemented by a dedicated type class, named after the data it represents with a `Type` suffix: [Region Manager Type](Region-Manager-Type.html) is the class backing the region manager data, [Table Type](Table-Type.html) the class backing tables, and so on. This page refers to every type by that full class name and links each one to its own page.

See [Ports](EGO-Script.html#ports) on the EGO Script page for how a port's type governs what it can receive, and [Basic Data Flow](Basic-Data-Flow.html#functors-and-connections) for the general rule this page's conversions follow.

## How automatic conversion works

Automatic type conversion only happens when a value is **connected** from one port to another — a variable reference, or a functor call inlined directly into an argument. It never applies to a constant written directly into a port; a constant is instead parsed by the receiving port's own type-specific literal syntax, which accepts only that type's own literal form. See [Constants](EGO-Script.html#constants) for this rule in full.

**Conditional conversions.** Some conversions can fail outright, for two different reasons. The first is a mismatch between a generic holder's declared type and what it actually contains: converting an already-typed, known value never fails, but converting a generic holder type (such as [Table Value Type](Table-Value-Type.html)) does depend on what it actually contains. [Table Value Type](Table-Value-Type.html) → [String Type](String-Type.html) and [Table Value Type](Table-Value-Type.html) → [Real Value Type](Real-Value-Type.html) are the clearest examples: each only succeeds if the [Table Value Type](Table-Value-Type.html) value actually holds that type. Wrapping such a conversion in [Skip On Error](Skip-On-Error.html) turns the failure into a type test — see [Manipulating Tables and Lookup Tables](Manipulating-Tables-And-Lookup-Tables.html) for a full worked example of this pattern. The same conditional logic governs every type that converts to or from [Table Type](Table-Type.html) itself — see [Table format of table-shaped types](#table-format-of-table-shaped-types) below for the exact column layout each one expects.

The second reason is content validation: the source value's type is compatible, but its actual content doesn't satisfy the target type's constraints. [String Type](String-Type.html) → [Real Value Type](Real-Value-Type.html) is the clearest example — connecting the string `"test"` to a Real Value Type port fails outright, since `"test"` isn't parseable as a number, while `"3.14"` succeeds. The same content-validation governs every conversion that narrows the numeric chain in [Value types](#value-types) below: [Integer Value Type](Integer-Value-Type.html) → [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) fails for any negative input, for instance, since there's no way to represent it in the narrower type at all. The named filename converters ([String Type](String-Type.html) → [Map Filename Type](Map-Filename-Type.html) and similar) apply the same extension-checking rule [Constants](EGO-Script.html#constants) documents for literal filenames — confirmed for [Weights Filename Type](Weights-Filename-Type.html) (`.dcf`, `.txt`, `.csv`), [Table Filename Type](Table-Filename-Type.html) and [Lookup Table Filename Type](Lookup-Table-Filename-Type.html) (`.csv` for both), and [Kmz Filename Type](Kmz-Filename-Type.html) (`.kmz`). [Generic Filename Type](Generic-Filename-Type.html) is the exception: it accepts any extension, matching its role as a filename with no specific format requirement.

**Information loss.** Failing outright and losing information are two different things — a conversion that never fails can still be irreversible. [Real Value Type](Real-Value-Type.html) → [Integer Value Type](Integer-Value-Type.html) is the clearest example: it never fails, since every real number truncates to some integer, but the fractional part is simply dropped — `3.9` and `3.1` both become `3`, and neither the original value nor the fact that something was lost survives the conversion. The opposite case — guaranteed to succeed \*and\* fully recoverable — describes the widening direction of that same numeric chain instead; see [Value types](#value-types) below for exactly which steps are which. Every table from here on carries a **Notes** column stating this directly for the specific pair on that row; a plain `—` means this page has no confirmed failure or loss behavior for that conversion beyond the general rules above, not that the question doesn't apply.

**Sequencing.** A conversion **to [None Type](None-Type.html)** is registered for almost every type in the system. This isn't meant to transform data — it's what lets [sequence ports](EGO-Script.html#sequence-ports) accept a connection from any container's output regardless of what that container actually produces: connecting an output to a [None Type](None-Type.html)-typed input creates a dependency edge without needing the value itself, so the engine schedules the connected functor to run after the one that produced it. The types that support this are listed separately in [Sequencing](#sequencing) below, rather than repeated in every table.

### Converters and subtyping

A path from one type to another works one of two ways. Most entries in the tables below are **registered converters** — real conversion logic that runs when the connection is made, subject to the conditional-failure pattern above. A few are **subtyping** instead: the source type is already, structurally, a value of the target type, so a port declared for the target accepts it directly, with nothing to register and nothing to run. Both kinds appear together in the same tables from here on; every table has a **Notes** column stating how each specific entry behaves — subtyping, a possible failure, or information loss — so that looking up one conversion tells the whole story without cross-referencing this section.

Three relationships in this system work through subtyping:

- [Categorical Map Type](Categorical-Map-Type.html) is a subtype of [Map Type](Map-Type.html) — see [Map and raster types](#map-and-raster-types) below.
- [Table Type](Table-Type.html) and [Lookup Table Type](Lookup-Table-Type.html) are both subtypes of [Base Table Type](Base-Table-Type.html) — see [Table and Lookup Table types](#table-and-lookup-table-types) below.
- [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) is a subtype of [Integer Value Type](Integer-Value-Type.html), mirroring the actual mathematical relationship between the value sets: non-negative integers are a subset of all integers. [Positive Integer Value Type](Positive-Integer-Value-Type.html)'s relationship to Non Negative Integer Value Type, by contrast, runs through an ordinary registered converter rather than subtyping, even though the value sets nest the same way — see [Value types](#value-types) below for both, side by side.

## Value types

The chain running through [Positive Integer Value Type](Positive-Integer-Value-Type.html), [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html), [Integer Value Type](Integer-Value-Type.html), and [Real Value Type](Real-Value-Type.html) behaves differently depending on direction, and the Notes column below states each step's behavior directly. **Widening** — positive to non-negative to integer to real — only relaxes which values are allowed; the number itself never changes, so every registered step is both guaranteed to succeed and fully recoverable. (Non Negative Integer Value Type's own step to Integer Value Type isn't among these registered steps at all — it's the subtyping entry from [Converters and subtyping](#converters-and-subtyping) above, so the question of failing or losing information doesn't apply to it; nothing runs.) **Narrowing** the other way splits into two different behaviors: [Integer Value Type](Integer-Value-Type.html) → [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) and [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) → [Positive Integer Value Type](Positive-Integer-Value-Type.html) both fail outright if the value falls outside the narrower range — negative, or zero, respectively — since there's no way to represent those values in the target type at all. [Real Value Type](Real-Value-Type.html) → [Integer Value Type](Integer-Value-Type.html) is different again: it never fails, but it's lossy — the fractional part is simply truncated and can't be recovered. See [How automatic conversion works](#how-automatic-conversion-works) above for these two dimensions — failure and information loss — stated generally.

Five of these types also converge on [Null Value Type](Null-Value-Type.html) — not to be confused with [None Type](None-Type.html) above. Where None Type is the sequencing mechanism, Null Value Type is an ordinary type in its own right; converting to it always succeeds, and it converts onward only to None Type, nowhere else.

**Boolean conversions.** [Boolean Value Type](Boolean-Value-Type.html) converts from four of the numeric types below — Integer, Non-Negative Integer, Positive Integer, and Real — using a non-zero-is-true rule, and converts back out to Integer, Non-Negative Integer, Real, Null, and String, using True → 1 / False → 0 (or True → `"true"` / False → `"false"` for String). There is deliberately no Boolean Value Type → Positive Integer Value Type entry: False converts to zero, and zero has no valid representation in Positive Integer Value Type, so no converter is registered for that specific pair.

**Log Tag conversions.** [Log Tag Type](Log-Tag-Type.html) converts to and from the same four numeric types by the level's position number in [Log Tag Type](Log-Tag-Type.html)'s own table (e.g. Info is level 4, so Info ↔ 4 in either direction), and separately converts to String Type using the level's name rather than its number (Info → `"Info"`).

**Code conversions.** [Code Type](Code-Type.html) holds a script (for example, the Python expression in [Calculate Python Expression](Calculate-Python-Expression.html)), and its conversion to and from [String Type](String-Type.html) carries that script's own text — neither direction involves base64. Converting Code Type to String Type produces the script's textual representation; converting String Type to Code Type takes the string's text directly as the script, with no base64 encoding required on either side.

| From | To | Notes |
| --- | --- | --- |
| [Boolean Value Type](Boolean-Value-Type.html) | [Integer Value Type](Integer-Value-Type.html) | True → 1, False → 0 |
| [Boolean Value Type](Boolean-Value-Type.html) | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | True → 1, False → 0 |
| [Boolean Value Type](Boolean-Value-Type.html) | [Null Value Type](Null-Value-Type.html) | — |
| [Boolean Value Type](Boolean-Value-Type.html) | [Real Value Type](Real-Value-Type.html) | True → 1, False → 0 |
| [Boolean Value Type](Boolean-Value-Type.html) | [String Type](String-Type.html) | True → `"true"`, False → `"false"` |
| [Code Type](Code-Type.html) | [String Type](String-Type.html) | Produces the script's textual representation — not a base64 encoding |
| [Index Or Name Type](Index-Or-Name-Type.html) | [Integer Value Type](Integer-Value-Type.html) | Can fail — only succeeds if the value holds an index rather than a name |
| [Index Or Name Type](Index-Or-Name-Type.html) | [Name Type](Name-Type.html) | Can fail — only succeeds if the value holds a name rather than an index |
| [Index Or Name Type](Index-Or-Name-Type.html) | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Can fail — only succeeds if the value holds an index rather than a name |
| [Index Or Name Type](Index-Or-Name-Type.html) | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Can fail — only succeeds if the value holds an index rather than a name |
| [Index Or Name Type](Index-Or-Name-Type.html) | [Real Value Type](Real-Value-Type.html) | Can fail — only succeeds if the value holds an index rather than a name |
| [Index Or Name Type](Index-Or-Name-Type.html) | [String Type](String-Type.html) | — |
| [Integer Value Type](Integer-Value-Type.html) | [Boolean Value Type](Boolean-Value-Type.html) | Zero → False, any non-zero value → True |
| [Integer Value Type](Integer-Value-Type.html) | [Enum Type](Enum-Type.html) | Can fail — only succeeds if the number matches a valid index in the target port's own enum definition (see [Enum Type](Enum-Type.html)) |
| [Integer Value Type](Integer-Value-Type.html) | [Index Or Name Type](Index-Or-Name-Type.html) | — |
| [Integer Value Type](Integer-Value-Type.html) | [Log Tag Type](Log-Tag-Type.html) | The number selects the level by its position in Log Tag Type's table (e.g. 4 → Info) |
| [Integer Value Type](Integer-Value-Type.html) | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Can fail — no valid target when the input is negative |
| [Integer Value Type](Integer-Value-Type.html) | [Null Value Type](Null-Value-Type.html) | — |
| [Integer Value Type](Integer-Value-Type.html) | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Can fail — no valid target when the input isn't positive |
| [Integer Value Type](Integer-Value-Type.html) | [Real Value Type](Real-Value-Type.html) | Lossless — widening; every integer is exactly representable as a real |
| [Integer Value Type](Integer-Value-Type.html) | [String Type](String-Type.html) | — |
| [Log Tag Type](Log-Tag-Type.html) | [Integer Value Type](Integer-Value-Type.html) | Converts to the level's number (e.g. Info → 4) |
| [Log Tag Type](Log-Tag-Type.html) | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Converts to the level's number (e.g. Info → 4) |
| [Log Tag Type](Log-Tag-Type.html) | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Can fail — no valid target when the level is Unconditional (numeric value 0); converts to the level's number otherwise (e.g. Info → 4). Registered in source as unconditional (no failure case), which appears to be a bug given the Unconditional case. |
| [Log Tag Type](Log-Tag-Type.html) | [Real Value Type](Real-Value-Type.html) | Converts to the level's number (e.g. Info → 4) |
| [Log Tag Type](Log-Tag-Type.html) | [String Type](String-Type.html) | Converts to the level's name, not its number (e.g. Info → `"Info"`) |
| [Name Type](Name-Type.html) | [Index Or Name Type](Index-Or-Name-Type.html) | — |
| [Name Type](Name-Type.html) | [String Type](String-Type.html) | — |
| [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | [Integer Value Type](Integer-Value-Type.html) | **Subtyping** — no conversion runs; see Converters and subtyping |
| [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | [Boolean Value Type](Boolean-Value-Type.html) | Zero → False, any non-zero value → True |
| [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | [Enum Type](Enum-Type.html) | Can fail — only succeeds if the number matches a valid index in the target port's own enum definition |
| [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | [Index Or Name Type](Index-Or-Name-Type.html) | — |
| [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | [Log Tag Type](Log-Tag-Type.html) | The number selects the level by its position in Log Tag Type's table (e.g. 4 → Info) |
| [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | [Null Value Type](Null-Value-Type.html) | — |
| [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Can fail — no valid target when the input is zero |
| [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | [Real Value Type](Real-Value-Type.html) | — |
| [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | [String Type](String-Type.html) | — |
| [Positive Integer Value Type](Positive-Integer-Value-Type.html) | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Lossless — widening; the value itself is unchanged |
| [Positive Integer Value Type](Positive-Integer-Value-Type.html) | [Boolean Value Type](Boolean-Value-Type.html) | Zero → False, any non-zero value → True — though a Positive Integer is never zero, so this always yields True in practice |
| [Positive Integer Value Type](Positive-Integer-Value-Type.html) | [Enum Type](Enum-Type.html) | Can fail — only succeeds if the number matches a valid index in the target port's own enum definition |
| [Positive Integer Value Type](Positive-Integer-Value-Type.html) | [Index Or Name Type](Index-Or-Name-Type.html) | — |
| [Positive Integer Value Type](Positive-Integer-Value-Type.html) | [Log Tag Type](Log-Tag-Type.html) | The number selects the level by its position in Log Tag Type's table (e.g. 4 → Info) |
| [Positive Integer Value Type](Positive-Integer-Value-Type.html) | [Null Value Type](Null-Value-Type.html) | — |
| [Positive Integer Value Type](Positive-Integer-Value-Type.html) | [Real Value Type](Real-Value-Type.html) | — |
| [Positive Integer Value Type](Positive-Integer-Value-Type.html) | [String Type](String-Type.html) | — |
| [Real Value Type](Real-Value-Type.html) | [Boolean Value Type](Boolean-Value-Type.html) | Zero → False, any non-zero value → True |
| [Real Value Type](Real-Value-Type.html) | [Enum Type](Enum-Type.html) | Can fail — only succeeds if the number matches a valid index in the target port's own enum definition |
| [Real Value Type](Real-Value-Type.html) | [Index Or Name Type](Index-Or-Name-Type.html) | — |
| [Real Value Type](Real-Value-Type.html) | [Integer Value Type](Integer-Value-Type.html) | Lossy — truncates the fractional part |
| [Real Value Type](Real-Value-Type.html) | [Log Tag Type](Log-Tag-Type.html) | The number selects the level by its position in Log Tag Type's table (e.g. 4 → Info) |
| [Real Value Type](Real-Value-Type.html) | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Can fail on negative input; lossy (truncates) otherwise |
| [Real Value Type](Real-Value-Type.html) | [Null Value Type](Null-Value-Type.html) | — |
| [Real Value Type](Real-Value-Type.html) | [Percent Type](Percent-Type.html) | — |
| [Real Value Type](Real-Value-Type.html) | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Can fail when not positive; lossy (truncates) otherwise |
| [Real Value Type](Real-Value-Type.html) | [String Type](String-Type.html) | — |
| [Real Value Type](Real-Value-Type.html) | [Date Type](Date-Type.html) | — |
| [String Type](String-Type.html) | [Code Type](Code-Type.html) | Takes the string's text directly as the script — no base64 encoding required |
| [String Type](String-Type.html) | [Date Type](Date-Type.html) | — |
| [String Type](String-Type.html) | [Index Or Name Type](Index-Or-Name-Type.html) | — |
| [String Type](String-Type.html) | [Name Type](Name-Type.html) | — |
| [String Type](String-Type.html) | [Real Value Type](Real-Value-Type.html) | Can fail — the string must parse as a valid number (e.g. "test" fails, "3.14" succeeds) |

## Filename and text types

Filenames largely behave like [String Type](String-Type.html) with an extra validation step on the way in — see [Constants](EGO-Script.html#constants) for the extension-checking rules each filename type applies to its text. Every filename type here converts to and from String Type; most of them — Generic, Map, Table, Lookup Table, and Weights Filename Type — also convert to and from a generic [Table Value Type](Table-Value-Type.html) holder, the same generic-holder role Table Value Type plays for the table-shaped types further down this page. That direction is lossy in every case: going into Table Value Type discards the parent folder path and keeps only the filename itself, so round-tripping back out through String Type or another filename type does not restore the original folder. Folder Type, Kmz Filename Type, and [Projection Type](Projection-Type.html) are the exceptions: they connect only to String Type, not to Table Value Type.

| From | To | Notes |
| --- | --- | --- |
| [Folder Type](Folder-Type.html) | [String Type](String-Type.html) | — |
| [String Type](String-Type.html) | [Folder Type](Folder-Type.html) | — |
| [String Type](String-Type.html) | [Generic Filename Type](Generic-Filename-Type.html) | Always succeeds — accepts any extension |
| [String Type](String-Type.html) | [Map Filename Type](Map-Filename-Type.html) | — |
| [String Type](String-Type.html) | [Table Filename Type](Table-Filename-Type.html) | Can fail — extension must be `.csv` |
| [String Type](String-Type.html) | [Lookup Table Filename Type](Lookup-Table-Filename-Type.html) | Can fail — extension must be `.csv` |
| [String Type](String-Type.html) | [Weights Filename Type](Weights-Filename-Type.html) | Can fail — extension must be `.dcf`, `.txt`, or `.csv` |
| [String Type](String-Type.html) | [Kmz Filename Type](Kmz-Filename-Type.html) | Can fail — extension must be `.kmz` |
| [String Type](String-Type.html) | [Projection Type](Projection-Type.html) | Expects WKT (Well-Known Text) format |
| [Generic Filename Type](Generic-Filename-Type.html) | [String Type](String-Type.html) | — |
| [Generic Filename Type](Generic-Filename-Type.html) | [Map Filename Type](Map-Filename-Type.html) | — |
| [Generic Filename Type](Generic-Filename-Type.html) | [Table Filename Type](Table-Filename-Type.html) | Can fail — extension must be `.csv` |
| [Generic Filename Type](Generic-Filename-Type.html) | [Lookup Table Filename Type](Lookup-Table-Filename-Type.html) | Can fail — extension must be `.csv` |
| [Generic Filename Type](Generic-Filename-Type.html) | [Weights Filename Type](Weights-Filename-Type.html) | Can fail — extension must be `.dcf`, `.txt`, or `.csv` |
| [Generic Filename Type](Generic-Filename-Type.html) | [Table Value Type](Table-Value-Type.html) | Lossy — discards the parent folder path, keeping only the filename itself |
| [Map Filename Type](Map-Filename-Type.html) | [Generic Filename Type](Generic-Filename-Type.html) | — |
| [Map Filename Type](Map-Filename-Type.html) | [String Type](String-Type.html) | — |
| [Map Filename Type](Map-Filename-Type.html) | [Table Value Type](Table-Value-Type.html) | Lossy — discards the parent folder path, keeping only the filename itself |
| [Table Filename Type](Table-Filename-Type.html) | [String Type](String-Type.html) | — |
| [Table Filename Type](Table-Filename-Type.html) | [Generic Filename Type](Generic-Filename-Type.html) | — |
| [Table Filename Type](Table-Filename-Type.html) | [Table Value Type](Table-Value-Type.html) | Lossy — discards the parent folder path, keeping only the filename itself |
| [Lookup Table Filename Type](Lookup-Table-Filename-Type.html) | [String Type](String-Type.html) | — |
| [Lookup Table Filename Type](Lookup-Table-Filename-Type.html) | [Generic Filename Type](Generic-Filename-Type.html) | — |
| [Lookup Table Filename Type](Lookup-Table-Filename-Type.html) | [Table Value Type](Table-Value-Type.html) | Lossy — discards the parent folder path, keeping only the filename itself |
| [Weights Filename Type](Weights-Filename-Type.html) | [String Type](String-Type.html) | — |
| [Weights Filename Type](Weights-Filename-Type.html) | [Generic Filename Type](Generic-Filename-Type.html) | — |
| [Weights Filename Type](Weights-Filename-Type.html) | [Table Value Type](Table-Value-Type.html) | Lossy — discards the parent folder path, keeping only the filename itself |
| [Kmz Filename Type](Kmz-Filename-Type.html) | [String Type](String-Type.html) | — |
| [Table Value Type](Table-Value-Type.html) | [Map Filename Type](Map-Filename-Type.html) | — |
| [Table Value Type](Table-Value-Type.html) | [Table Filename Type](Table-Filename-Type.html) | Can fail — extension must be `.csv` |
| [Table Value Type](Table-Value-Type.html) | [Lookup Table Filename Type](Lookup-Table-Filename-Type.html) | Can fail — extension must be `.csv` |
| [Table Value Type](Table-Value-Type.html) | [Weights Filename Type](Weights-Filename-Type.html) | Can fail — extension must be `.dcf`, `.txt`, or `.csv` |
| [Table Value Type](Table-Value-Type.html) | [Generic Filename Type](Generic-Filename-Type.html) | — |
| [Projection Type](Projection-Type.html) | [String Type](String-Type.html) | Produces WKT (Well-Known Text) format |

## Table and Lookup Table types

[Table Type](Table-Type.html) sits at the center of this group. It and [Lookup Table Type](Lookup-Table-Type.html) are both subtypes of [Base Table Type](Base-Table-Type.html) — see [Converters and subtyping](#converters-and-subtyping) above — so their path back to Base Table Type, marked `Subtyping` in the Notes column below, needs no conversion at all, while the narrowing direction the other way round is an ordinary registered check against a specific shape. The rest of the table is more ordinary conversion territory: [Table Value Type](Table-Value-Type.html) moving to and from the scalar types a table cell can actually hold, and the individual value types converting into [Tuple Type](Tuple-Type.html) and [Table Cell Type](Table-Cell-Type.html) for use as keys and column declarations.

| From | To | Notes |
| --- | --- | --- |
| [Base Table Type](Base-Table-Type.html) | [Table Type](Table-Type.html) | Can fail — Base Table Type is a generic container; only succeeds if what it actually holds is already shaped like a Table |
| [Base Table Type](Base-Table-Type.html) | [Lookup Table Type](Lookup-Table-Type.html) | Can fail — Base Table Type is a generic container; only succeeds if what it actually holds is already shaped like a Lookup Table |
| [Lookup Table Type](Lookup-Table-Type.html) | [Base Table Type](Base-Table-Type.html) | **Subtyping** — no conversion runs; see Converters and subtyping |
| [Lookup Table Type](Lookup-Table-Type.html) | [Table Type](Table-Type.html) | — |
| [Lookup Table Type](Lookup-Table-Type.html) | [Lookup Table Group Type](Lookup-Table-Group-Type.html) | — |
| [Lookup Table Type](Lookup-Table-Type.html) | [Change Matrix Type](Change-Matrix-Type.html) | — |
| [Lookup Table Type](Lookup-Table-Type.html) | [Percent Matrix Type](Percent-Matrix-Type.html) | — |
| [Lookup Table Type](Lookup-Table-Type.html) | [Transition Matrix Type](Transition-Matrix-Type.html) | — |
| [Lookup Table Type](Lookup-Table-Type.html) | [Transition Set Type](Transition-Set-Type.html) | — |
| [Lookup Table Type](Lookup-Table-Type.html) | [Int Set Type](Int-Set-Type.html) | — |
| [Lookup Table Group Type](Lookup-Table-Group-Type.html) | [Table Type](Table-Type.html) | — |
| [Lookup Table Group Type](Lookup-Table-Group-Type.html) | [Base Table Type](Base-Table-Type.html) | — |
| [Lookup Table Group Type](Lookup-Table-Group-Type.html) | [Lookup Table Type](Lookup-Table-Type.html) | — |
| [Table Type](Table-Type.html) | [Base Table Type](Base-Table-Type.html) | **Subtyping** — no conversion runs; see Converters and subtyping |
| [Table Type](Table-Type.html) | [Lookup Table Type](Lookup-Table-Type.html) | — |
| [Table Type](Table-Type.html) | [Lookup Table Group Type](Lookup-Table-Group-Type.html) | — |
| [Table Type](Table-Type.html) | [Categorization Type](Categorization-Type.html) | — |
| [Table Type](Table-Type.html) | [Weights Of Evidence Skeleton Type](Weights-Of-Evidence-Skeleton-Type.html) | — |
| [Table Type](Table-Type.html) | [Change Matrix Type](Change-Matrix-Type.html) | — |
| [Table Type](Table-Type.html) | [Neighborhood Table Type](Neighborhood-Table-Type.html) | — |
| [Table Type](Table-Type.html) | [Percent Matrix Type](Percent-Matrix-Type.html) | — |
| [Table Type](Table-Type.html) | [Transition Function Parameter Matrix Type](Transition-Function-Parameter-Matrix-Type.html) | — |
| [Table Type](Table-Type.html) | [Transition Matrix Type](Transition-Matrix-Type.html) | — |
| [Table Type](Table-Type.html) | [Weights Type](Weights-Type.html) | — |
| [Table Value Type](Table-Value-Type.html) | [Tuple Type](Tuple-Type.html) | — |
| [Table Value Type](Table-Value-Type.html) | [Generic Filename Type](Generic-Filename-Type.html) | — |
| [Table Value Type](Table-Value-Type.html) | [Index Or Name Type](Index-Or-Name-Type.html) | — |
| [Table Value Type](Table-Value-Type.html) | [Integer Value Type](Integer-Value-Type.html) | — |
| [Table Value Type](Table-Value-Type.html) | [Name Type](Name-Type.html) | — |
| [Table Value Type](Table-Value-Type.html) | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | — |
| [Table Value Type](Table-Value-Type.html) | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | — |
| [Table Value Type](Table-Value-Type.html) | [Real Value Type](Real-Value-Type.html) | Can fail — only succeeds if the value actually holds a Real Value |
| [Table Value Type](Table-Value-Type.html) | [String Type](String-Type.html) | Can fail — only succeeds if the value actually holds a String |
| [Table Value Type](Table-Value-Type.html) | [Table Filename Type](Table-Filename-Type.html) | — |
| [Table Value Type](Table-Value-Type.html) | [Lookup Table Filename Type](Lookup-Table-Filename-Type.html) | — |
| [Table Value Type](Table-Value-Type.html) | [Weights Filename Type](Weights-Filename-Type.html) | — |
| [Table Value Type](Table-Value-Type.html) | [Map Filename Type](Map-Filename-Type.html) | — |
| [Integer Value Type](Integer-Value-Type.html) | [Table Cell Type](Table-Cell-Type.html) | — |
| [Integer Value Type](Integer-Value-Type.html) | [Table Value Type](Table-Value-Type.html) | — |
| [Integer Value Type](Integer-Value-Type.html) | [Tuple Type](Tuple-Type.html) | — |
| [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | [Table Cell Type](Table-Cell-Type.html) | — |
| [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | [Table Value Type](Table-Value-Type.html) | — |
| [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | [Tuple Type](Tuple-Type.html) | — |
| [Positive Integer Value Type](Positive-Integer-Value-Type.html) | [Table Cell Type](Table-Cell-Type.html) | — |
| [Positive Integer Value Type](Positive-Integer-Value-Type.html) | [Table Value Type](Table-Value-Type.html) | — |
| [Positive Integer Value Type](Positive-Integer-Value-Type.html) | [Tuple Type](Tuple-Type.html) | — |
| [Real Value Type](Real-Value-Type.html) | [Table Cell Type](Table-Cell-Type.html) | — |
| [Real Value Type](Real-Value-Type.html) | [Table Value Type](Table-Value-Type.html) | — |
| [Real Value Type](Real-Value-Type.html) | [Tuple Type](Tuple-Type.html) | — |
| [Name Type](Name-Type.html) | [Table Value Type](Table-Value-Type.html) | — |
| [Name Type](Name-Type.html) | [Tuple Type](Tuple-Type.html) | — |
| [String Type](String-Type.html) | [Table Value Type](Table-Value-Type.html) | — |
| [String Type](String-Type.html) | [Tuple Type](Tuple-Type.html) | — |

## Map and raster types

[Categorical Map Type](Categorical-Map-Type.html)'s path to [Map Type](Map-Type.html), marked `Subtyping` in the Notes column below, is the clearest example of subtyping on this page — see [Converters and subtyping](#converters-and-subtyping) above. A Categorical Map Type value converts automatically wherever a Map Type is expected, keeping its cells and null value intact and dropping only the guarantee that a categorization is attached; the reverse never happens automatically, since an arbitrary Map Type value isn't guaranteed to carry one — which is why there's no corresponding Map Type → Categorical Map Type entry at all. The rest of the table below is [Cell Type](Cell-Type.html)'s round trip with the numeric value types, and the two paths a categorical map takes toward its supporting data: its legend, as a [Categorization Type](Categorization-Type.html), and its spatial reference, as a [Projection Type](Projection-Type.html).

| From | To | Notes |
| --- | --- | --- |
| [Cell Type](Cell-Type.html) | [Real Value Type](Real-Value-Type.html) | Converts to the cell type's number (e.g. Signed 32 Bit Integer → 5) |
| [Cell Type](Cell-Type.html) | [Integer Value Type](Integer-Value-Type.html) | Converts to the cell type's number (e.g. Signed 32 Bit Integer → 5) |
| [Cell Type](Cell-Type.html) | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Converts to the cell type's number (e.g. Signed 32 Bit Integer → 5) |
| [Cell Type](Cell-Type.html) | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Can fail — no valid target when the cell type is 1 Bit Integer (numeric value 0); converts to the cell type's number otherwise (e.g. Signed 32 Bit Integer → 5). Registered in source as unconditional (no failure case), which appears to be a bug given the 1 Bit Integer case. |
| [Real Value Type](Real-Value-Type.html) | [Cell Type](Cell-Type.html) | The number selects the cell type by its position in Cell Type's table (e.g. 5 → Signed 32 Bit Integer) |
| [Integer Value Type](Integer-Value-Type.html) | [Cell Type](Cell-Type.html) | The number selects the cell type by its position in Cell Type's table (e.g. 5 → Signed 32 Bit Integer) |
| [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | [Cell Type](Cell-Type.html) | The number selects the cell type by its position in Cell Type's table (e.g. 5 → Signed 32 Bit Integer) |
| [Positive Integer Value Type](Positive-Integer-Value-Type.html) | [Cell Type](Cell-Type.html) | The number selects the cell type by its position in Cell Type's table (e.g. 5 → Signed 32 Bit Integer) |
| [Categorical Map Type](Categorical-Map-Type.html) | [Map Type](Map-Type.html) | **Subtyping** — no conversion runs; see Converters and subtyping |
| [Categorical Map Type](Categorical-Map-Type.html) | [Categorization Type](Categorization-Type.html) | — |
| [Categorical Map Type](Categorical-Map-Type.html) | [Projection Type](Projection-Type.html) | — |
| [Categorization Type](Categorization-Type.html) | [Table Type](Table-Type.html) | — |
| [Table Type](Table-Type.html) | [Categorization Type](Categorization-Type.html) | — |
| [Map Type](Map-Type.html) | [Projection Type](Projection-Type.html) | — |

## Simulation types

Every matrix-shaped type here — [Change Matrix Type](Change-Matrix-Type.html), [Percent Matrix Type](Percent-Matrix-Type.html), [Transition Matrix Type](Transition-Matrix-Type.html), and the rest — follows the same pattern: each one converts to and from a [Table Type](Table-Type.html) (or [Lookup Table Type](Lookup-Table-Type.html)) with one particular expected column layout, and converting between them is mostly a matter of adding or checking for that layout. This is a conversion relationship, not structural identity — [Neighborhood Table Type](Neighborhood-Table-Type.html) and [Weights Type](Weights-Type.html), for instance, have no editable constant of their own despite converting to and from Table Type; a value is obtained only from a producing functor or from this conversion. See [Table format of table-shaped types](#table-format-of-table-shaped-types) below for the exact columns each one expects.

| From | To | Notes |
| --- | --- | --- |
| [Change Matrix Type](Change-Matrix-Type.html) | [Lookup Table Type](Lookup-Table-Type.html) | — |
| [Change Matrix Type](Change-Matrix-Type.html) | [Table Type](Table-Type.html) | — |
| [Lookup Table Type](Lookup-Table-Type.html) | [Change Matrix Type](Change-Matrix-Type.html) | — |
| [Lookup Table Type](Lookup-Table-Type.html) | [Percent Matrix Type](Percent-Matrix-Type.html) | — |
| [Lookup Table Type](Lookup-Table-Type.html) | [Transition Matrix Type](Transition-Matrix-Type.html) | — |
| [Lookup Table Type](Lookup-Table-Type.html) | [Transition Set Type](Transition-Set-Type.html) | — |
| [Table Type](Table-Type.html) | [Change Matrix Type](Change-Matrix-Type.html) | — |
| [Table Type](Table-Type.html) | [Neighborhood Table Type](Neighborhood-Table-Type.html) | — |
| [Table Type](Table-Type.html) | [Percent Matrix Type](Percent-Matrix-Type.html) | — |
| [Table Type](Table-Type.html) | [Transition Function Parameter Matrix Type](Transition-Function-Parameter-Matrix-Type.html) | — |
| [Table Type](Table-Type.html) | [Transition Matrix Type](Transition-Matrix-Type.html) | — |
| [Table Type](Table-Type.html) | [Weights Type](Weights-Type.html) | — |
| [Percent Matrix Type](Percent-Matrix-Type.html) | [Lookup Table Type](Lookup-Table-Type.html) | — |
| [Percent Matrix Type](Percent-Matrix-Type.html) | [Table Type](Table-Type.html) | — |
| [Transition Matrix Type](Transition-Matrix-Type.html) | [Lookup Table Type](Lookup-Table-Type.html) | — |
| [Transition Matrix Type](Transition-Matrix-Type.html) | [Table Type](Table-Type.html) | — |
| [Transition Function Parameter Matrix Type](Transition-Function-Parameter-Matrix-Type.html) | [Table Type](Table-Type.html) | — |
| [Neighborhood Table Type](Neighborhood-Table-Type.html) | [Table Type](Table-Type.html) | — |
| [Elevation Graph Type](Elevation-Graph-Type.html) | [Neighborhood Table Type](Neighborhood-Table-Type.html) | — |
| [Elevation Graph Type](Elevation-Graph-Type.html) | [String Type](String-Type.html) | — |
| [Weights Type](Weights-Type.html) | [Table Type](Table-Type.html) | — |

## Calibration types

The one conversion pair here follows the same table-shaped logic as the simulation types above, though its exact column layout isn't confirmed — see the note in [Table format of table-shaped types](#table-format-of-table-shaped-types) below.

| From | To | Notes |
| --- | --- | --- |
| [Table Type](Table-Type.html) | [Weights Of Evidence Skeleton Type](Weights-Of-Evidence-Skeleton-Type.html) | — |
| [Weights Of Evidence Skeleton Type](Weights-Of-Evidence-Skeleton-Type.html) | [Table Type](Table-Type.html) | — |

## Table format of table-shaped types

Several of the types above convert to and from [Table Type](Table-Type.html) (or [Lookup Table Type](Lookup-Table-Type.html)) under one particular, expected column layout: converting to Table Type keeps the same rows but drops the type's special meaning, and converting from Table Type checks that the table actually has this shape — the same conditional-conversion pattern described above. As noted in Simulation types, this is strictly a conversion relationship: it doesn't imply the type has an editor or constant syntax matching Table Type's own. In fact, [Transition Matrix Type](Transition-Matrix-Type.html), [Change Matrix Type](Change-Matrix-Type.html), [Percent Matrix Type](Percent-Matrix-Type.html), [Transition Function Parameter Matrix Type](Transition-Function-Parameter-Matrix-Type.html), and [Weights Of Evidence Skeleton Type](Weights-Of-Evidence-Skeleton-Type.html) each have their own dedicated EGO Script literal syntax, keyed on `From->To` pairs rather than named columns — see each type's own page for its exact grammar. The engine registers an exact default format for most of these; key columns are marked `*` the way [Table Type](Table-Type.html) itself marks them. [Table Type's own Automatic Conversions section](Table-Type.html#automatic-conversions) and [Manipulating Tables and Lookup Tables](Manipulating-Tables-And-Lookup-Tables.html) both describe the Lookup Table Type row below in those same terms — its `*#real, #real` shape already matching what a single-value table needs.

| Type | Direction | Table format |
| --- | --- | --- |
| [Lookup Table Type](Lookup-Table-Type.html) | ↔ Table Type | `Key*` (Real), `Value` (Real) |
| [Categorization Type](Categorization-Type.html) | ↔ Table Type | `Value*` (Real), `Name` (String), `Color_Red` (Real), `Color_Green` (Real), `Color_Blue` (Real) — `Name` may be left blank when converting into a Categorization; it falls back to an auto-generated `class_N` (or `class_nN` for a negative value) |
| [Change Matrix Type](Change-Matrix-Type.html) | ↔ Table Type | `From*` (Real), `To*` (Real), `Cells` (Real) |
| [Percent Matrix Type](Percent-Matrix-Type.html) | ↔ Table Type | `From*` (Real), `To*` (Real), `Percent` (Real) |
| [Transition Matrix Type](Transition-Matrix-Type.html) | ↔ Table Type | `From*` (Real), `To*` (Real), `Rate` (Real) |
| [Transition Function Parameter Matrix Type](Transition-Function-Parameter-Matrix-Type.html) | ↔ Table Type | `From*` (Real), `To*` (Real), `Mean_Patch_Size` (Real), `Patch_Size_Variance` (Real), `Patch_Isometry` (Real) |
| [Neighborhood Table Type](Neighborhood-Table-Type.html) | ↔ Table Type | `Neighbor1*` (Real), `Neighbor2*` (Real), `Weight` (Real) |
| [Weights Type](Weights-Type.html) | ↔ Table Type | `From*` (Real), `To*` (Real), `Variable*` (String), `Range_Lower_Limit*` (Real), `Range_Upper_Limit*` (Real), `Weight` (Real) |
| [Weights Of Evidence Skeleton Type](Weights-Of-Evidence-Skeleton-Type.html) | ↔ Table Type | `From*` (Real), `To*` (Real), `Variable_Name*` (String), `Categorical` (Real), `Increment` (Real), `Minimum_Delta` (Real), `Maximum_Delta` (Real), `Tolerance_Angle` (Real) |

> **Note:** [Transition Set Type](Transition-Set-Type.html) is left out of this table on purpose — it converts one-way from [Lookup Table Type](Lookup-Table-Type.html) but never to or from [Table Type](Table-Type.html) directly, so it has no registered table format either. [Base Table Type](Base-Table-Type.html) and [Lookup Table Group Type](Lookup-Table-Group-Type.html) are left out for a different reason: neither has a fixed column layout to state — see [Table and Lookup Table types](#table-and-lookup-table-types) above for how each of them converts.

## Region types

[Region Manager Type](Region-Manager-Type.html) stands apart from every other type on this page: it has no automatic conversions to or from anything else. The only conversion registered for it at all is the sequencing conversion to [None Type](None-Type.html) described below.

## Sequencing

A conversion **to [None Type](None-Type.html)** — used to force an execution order between two functors rather than to transform a value, most visibly through the `sequenceInput`/`sequenceOutput` ports [EGO Script](EGO-Script.html#sequence-ports) exposes on most containers — is registered for the following types:

[Connection Info Type](Connection-Info-Type.html), [Boolean Value Type](Boolean-Value-Type.html), [Code Type](Code-Type.html), [Date Type](Date-Type.html), [Enum Type](Enum-Type.html), [Folder Type](Folder-Type.html), [Generic Filename Type](Generic-Filename-Type.html), [Image Expression Type](Image-Expression-Type.html), [Index Or Name Type](Index-Or-Name-Type.html), [Int Set Type](Int-Set-Type.html), [Integer Value Type](Integer-Value-Type.html), [Log Tag Type](Log-Tag-Type.html), [Name Type](Name-Type.html), [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html), [Null Value Type](Null-Value-Type.html), [Percent Type](Percent-Type.html), [Positive Integer Value Type](Positive-Integer-Value-Type.html), [Real Value Type](Real-Value-Type.html), [String Type](String-Type.html), [Struct Type](Struct-Type.html), [Workdir Type](Workdir-Type.html), [Categorical Map Type](Categorical-Map-Type.html), [Categorization Type](Categorization-Type.html), [Cell Type](Cell-Type.html), [Kml Type](Kml-Type.html), [Kml Timeline Type](Kml-Timeline-Type.html), [Kmz Filename Type](Kmz-Filename-Type.html), [Map Type](Map-Type.html), [Map Filename Type](Map-Filename-Type.html), [Projection Type](Projection-Type.html), [Weights Of Evidence Skeleton Type](Weights-Of-Evidence-Skeleton-Type.html), [Change Matrix Type](Change-Matrix-Type.html), [Neighborhood Table Type](Neighborhood-Table-Type.html), [Percent Matrix Type](Percent-Matrix-Type.html), [Transition Function Parameter Matrix Type](Transition-Function-Parameter-Matrix-Type.html), [Transition Matrix Type](Transition-Matrix-Type.html), [Transition Set Type](Transition-Set-Type.html), [Weights Type](Weights-Type.html), [Weights Filename Type](Weights-Filename-Type.html), [Elevation Graph Type](Elevation-Graph-Type.html), [Region Manager Type](Region-Manager-Type.html), [Base Table Type](Base-Table-Type.html), [Lookup Table Type](Lookup-Table-Type.html), [Lookup Table Filename Type](Lookup-Table-Filename-Type.html), [Lookup Table Group Type](Lookup-Table-Group-Type.html), [Table Filename Type](Table-Filename-Type.html), [Table Type](Table-Type.html), [Table Manager Type](Table-Manager-Type.html), [Table Value Type](Table-Value-Type.html), [Tuple Type](Tuple-Type.html)
{% endraw %}
