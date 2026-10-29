---
title: "Type System"
nav_order: 3
parent: "Core Concepts"
has_children: true
---
{% raw %}
# Type System

## Overview

Every port in the engine has a **type**, and a port accepts a value if it's exactly that type — or if some path leads from the value's actual type to the port's. That path works one of two ways: most of the time it's a registered conversion, actual logic that runs when the connection is made; a few times it's subtyping instead, where the source type is already, structurally, a value of the target type and nothing needs to run at all. This page lists both together in the same tables — see [Converters and subtyping](#converters-and-subtyping) below for how the two are told apart.

Each type here is implemented by a dedicated type class, named after the data it represents with a `Type` suffix: [Region Manager Type](types/Region-Manager-Type.html) is the class backing the region manager data, [Table Type](types/Table-Type.html) the class backing tables, and so on. This page refers to every type by that full class name and links each one to its own page.

See [Ports](EGO-Script.html#ports) on the EGO Script page for how a port's type governs what it can receive, and [Basic Data Flow](Basic-Data-Flow.html#functors-and-connections) for the general rule this page's conversions follow.

## How automatic conversion works

Automatic type conversion only happens when a value is **connected** from one port to another — a variable reference, or a functor call inlined directly into an argument. It never applies to a constant written directly into a port; a constant is instead parsed by the receiving port's own type-specific literal syntax, which accepts only that type's own literal form. See [Constants](EGO-Script.html#constants) for this rule in full.

**Conditional conversions.** Some conversions can fail outright, for two different reasons. The first is a mismatch between a generic holder's declared type and what it actually contains: converting a generic holder type (such as [Table Value Type](types/Table-Value-Type.html)) depends on what it actually holds. [Table Value Type](types/Table-Value-Type.html) → [String Type](types/String-Type.html) and [Table Value Type](types/Table-Value-Type.html) → [Real Value Type](types/Real-Value-Type.html) are the clearest examples: each only succeeds if the [Table Value Type](types/Table-Value-Type.html) value actually holds that type. Wrapping such a conversion in [Skip On Error](functors/Skip-On-Error.html) turns the failure into a type test — see [Manipulating Tables and Lookup Tables](Manipulating-Tables-And-Lookup-Tables.html) for a full worked example of this pattern. The same conditional logic governs every type that converts to or from [Table Type](types/Table-Type.html) itself — see [Table format of table-shaped types](#table-format-of-table-shaped-types) below for the exact column layout each one expects.

The second reason is content validation: the source value's type is compatible, but its actual content doesn't satisfy the target type's constraints. [String Type](types/String-Type.html) → [Real Value Type](types/Real-Value-Type.html) is the clearest example — connecting the string `"test"` to a Real Value Type port fails outright, since `"test"` isn't parseable as a number, while `"3.14"` succeeds. The same content-validation governs every conversion that narrows the numeric chain in [Value types](#value-types) below: [Integer Value Type](types/Integer-Value-Type.html) → [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) fails for any negative input, for instance, since there's no way to represent it in the narrower type at all. The named filename converters ([String Type](types/String-Type.html) → [Table Filename Type](types/Table-Filename-Type.html) and similar) apply the same extension-checking rule [Constants](EGO-Script.html#constants) documents for literal filenames: [Weights Filename Type](types/Weights-Filename-Type.html) (`.dcf`, `.txt`, `.csv`), [Table Filename Type](types/Table-Filename-Type.html) and [Lookup Table Filename Type](types/Lookup-Table-Filename-Type.html) (`.csv` for both), and [Kmz Filename Type](types/Kmz-Filename-Type.html) (`.kmz`). [Generic Filename Type](types/Generic-Filename-Type.html) and [Map Filename Type](types/Map-Filename-Type.html) accept any extension. Every filename type except [Folder Type](types/Folder-Type.html) rejects an empty filename, and a [Table Value Type](types/Table-Value-Type.html) holding a number never converts to a filename.

**Information loss.** Failing outright and losing information are two different things — a conversion that never fails can still be irreversible. [Real Value Type](types/Real-Value-Type.html) → [Integer Value Type](types/Integer-Value-Type.html) is the clearest example: it rounds down, so `3.9` and `3.1` both become `3` (and `-3.1` becomes `-4`), and neither the original value nor the fact that something was lost survives the conversion. It fails only for values outside the integer range. The opposite case — guaranteed to succeed \*and\* fully recoverable — describes the widening direction of that same numeric chain instead; see [Value types](#value-types) below for exactly which steps are which. Every table from here on carries a **Notes** column stating this directly for the specific pair on that row; a plain `—` means the conversion always succeeds.

**Sequencing.** A conversion **to [None Type](types/None-Type.html)** is registered for almost every type in the system. This isn't meant to transform data — it's what lets [sequence ports](EGO-Script.html#sequence-ports) accept a connection from any container's output regardless of what that container actually produces: connecting an output to a [None Type](types/None-Type.html)-typed input creates a dependency edge without needing the value itself, so the engine schedules the connected functor to run after the one that produced it. The types that support this are listed separately in [Sequencing](#sequencing) below, rather than repeated in every table.

### Converters and subtyping

A path from one type to another works one of two ways. Most entries in the tables below are **registered converters** — real conversion logic that runs when the connection is made, subject to the conditional-failure pattern above. A few are **subtyping** instead: the source type is already, structurally, a value of the target type, so a port declared for the target accepts it directly, with nothing to register and nothing to run. Both kinds appear together in the same tables from here on; every table has a **Notes** column stating how each specific entry behaves — subtyping, a possible failure, or information loss — so that looking up one conversion tells the whole story without cross-referencing this section.

Three relationships in this system work through subtyping:

- [Categorical Map Type](types/Categorical-Map-Type.html) is a subtype of [Map Type](types/Map-Type.html) — see [Map and raster types](#map-and-raster-types) below.
- [Table Type](types/Table-Type.html) and [Lookup Table Type](types/Lookup-Table-Type.html) are both subtypes of [Base Table Type](types/Base-Table-Type.html) — see [Table and Lookup Table types](#table-and-lookup-table-types) below.
- [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) is a subtype of [Integer Value Type](types/Integer-Value-Type.html), mirroring the actual mathematical relationship between the value sets: non-negative integers are a subset of all integers. [Positive Integer Value Type](types/Positive-Integer-Value-Type.html)'s relationship to Non Negative Integer Value Type, by contrast, runs through an ordinary registered converter rather than subtyping, even though the value sets nest the same way — see [Value types](#value-types) below for both, side by side.

## Value types

The chain running through [Positive Integer Value Type](types/Positive-Integer-Value-Type.html), [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html), [Integer Value Type](types/Integer-Value-Type.html), and [Real Value Type](types/Real-Value-Type.html) behaves differently depending on direction, and the Notes column below states each step's behavior directly. **Widening** — positive to non-negative to integer to real — only relaxes which values are allowed; the number itself never changes, so every registered step is both guaranteed to succeed and fully recoverable. (Non Negative Integer Value Type's own step to Integer Value Type isn't among these registered steps at all — it's the subtyping entry from [Converters and subtyping](#converters-and-subtyping) above, so the question of failing or losing information doesn't apply to it; nothing runs.) **Narrowing** the other way splits into two different behaviors: [Integer Value Type](types/Integer-Value-Type.html) → [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) and [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) → [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) both fail outright if the value falls outside the narrower range — negative, or zero, respectively — since there's no way to represent those values in the target type at all. [Real Value Type](types/Real-Value-Type.html) → [Integer Value Type](types/Integer-Value-Type.html) is different again: it rounds down, losing the fractional part, and fails only for values outside the integer range. [Real Value Type](types/Real-Value-Type.html) → [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) and → [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) truncate toward zero instead and then apply the range check: `-0.5` becomes `0` and is accepted as non-negative, while `0.9` becomes `0` and fails as positive. See [How automatic conversion works](#how-automatic-conversion-works) above for these two dimensions — failure and information loss — stated generally.

Five of these types also converge on [Null Value Type](types/Null-Value-Type.html) — not to be confused with [None Type](types/None-Type.html) above. Where None Type is the sequencing mechanism, Null Value Type is an ordinary type in its own right; converting to it always succeeds, and it converts onward only to None Type, nowhere else.

**Boolean conversions.** [Boolean Value Type](types/Boolean-Value-Type.html) converts from four of the numeric types below — Integer, Non-Negative Integer, Positive Integer, and Real — using a non-zero-is-true rule (for Real, values within rounding tolerance of zero also count as zero), and converts back out to Integer, Non-Negative Integer, Real, Null, and String, using True → 1 / False → 0 (or True → `"true"` / False → `"false"` for String). There is deliberately no Boolean Value Type → Positive Integer Value Type entry: False converts to zero, and zero has no valid representation in Positive Integer Value Type, so no converter is registered for that specific pair.

**Log Tag conversions.** [Log Tag Type](types/Log-Tag-Type.html) converts to and from the same four numeric types by the level's position number in [Log Tag Type](types/Log-Tag-Type.html)'s own table (e.g. Info is level 4, so Info ↔ 4 in either direction), and separately converts to String Type using the level's name rather than its number (Info → `"Info"`). A number that isn't a valid level number fails; a real is rounded to the nearest integer first.

**Code conversions.** [Code Type](types/Code-Type.html) holds a script (for example, the Python expression in [Calculate Python Expression](functors/Calculate-Python-Expression.html)), and its conversion to and from [String Type](types/String-Type.html) carries that script's own text — neither direction involves base64. Converting Code Type to String Type produces the script's textual representation; converting String Type to Code Type takes the string's text directly as the script, with no base64 encoding required on either side.

| From | To | Notes |
| --- | --- | --- |
| [Boolean Value Type](types/Boolean-Value-Type.html) | [Integer Value Type](types/Integer-Value-Type.html) | True → 1, False → 0 |
| [Boolean Value Type](types/Boolean-Value-Type.html) | [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | True → 1, False → 0 |
| [Boolean Value Type](types/Boolean-Value-Type.html) | [Null Value Type](types/Null-Value-Type.html) | — |
| [Boolean Value Type](types/Boolean-Value-Type.html) | [Real Value Type](types/Real-Value-Type.html) | True → 1, False → 0 |
| [Boolean Value Type](types/Boolean-Value-Type.html) | [String Type](types/String-Type.html) | True → `"true"`, False → `"false"` |
| [Code Type](types/Code-Type.html) | [String Type](types/String-Type.html) | Produces the script's textual representation — not a base64 encoding |
| [Index Or Name Type](types/Index-Or-Name-Type.html) | [Integer Value Type](types/Integer-Value-Type.html) | Can fail — only succeeds if the value holds an index rather than a name |
| [Index Or Name Type](types/Index-Or-Name-Type.html) | [Name Type](types/Name-Type.html) | Can fail — only succeeds if the value holds a name rather than an index |
| [Index Or Name Type](types/Index-Or-Name-Type.html) | [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | Can fail — only succeeds if the value holds an index rather than a name |
| [Index Or Name Type](types/Index-Or-Name-Type.html) | [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | Can fail — only succeeds if the value holds an index rather than a name |
| [Index Or Name Type](types/Index-Or-Name-Type.html) | [Real Value Type](types/Real-Value-Type.html) | Can fail — only succeeds if the value holds an index rather than a name |
| [Index Or Name Type](types/Index-Or-Name-Type.html) | [String Type](types/String-Type.html) | Can fail — only succeeds if the value holds a name rather than an index |
| [Integer Value Type](types/Integer-Value-Type.html) | [Boolean Value Type](types/Boolean-Value-Type.html) | Zero → False, any non-zero value → True |
| [Integer Value Type](types/Integer-Value-Type.html) | [Enum Type](types/Enum-Type.html) | Can fail — negative values fail; the number is the option's index in the target port's enumeration (see [Enum Type](types/Enum-Type.html)) |
| [Integer Value Type](types/Integer-Value-Type.html) | [Index Or Name Type](types/Index-Or-Name-Type.html) | Can fail — the value must be greater than zero |
| [Integer Value Type](types/Integer-Value-Type.html) | [Log Tag Type](types/Log-Tag-Type.html) | Can fail — the number must be a valid level number (e.g. 4 → Info) |
| [Integer Value Type](types/Integer-Value-Type.html) | [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | Can fail — no valid target when the input is negative |
| [Integer Value Type](types/Integer-Value-Type.html) | [Null Value Type](types/Null-Value-Type.html) | — |
| [Integer Value Type](types/Integer-Value-Type.html) | [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | Can fail — no valid target when the input isn't positive |
| [Integer Value Type](types/Integer-Value-Type.html) | [Real Value Type](types/Real-Value-Type.html) | Lossless — widening; every integer is exactly representable as a real |
| [Integer Value Type](types/Integer-Value-Type.html) | [String Type](types/String-Type.html) | — |
| [Log Tag Type](types/Log-Tag-Type.html) | [Integer Value Type](types/Integer-Value-Type.html) | Converts to the level's number (e.g. Info → 4) |
| [Log Tag Type](types/Log-Tag-Type.html) | [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | Converts to the level's number (e.g. Info → 4) |
| [Log Tag Type](types/Log-Tag-Type.html) | [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | Can fail — fails for Unconditional (numeric value 0); converts to the level's number otherwise (e.g. Info → 4) |
| [Log Tag Type](types/Log-Tag-Type.html) | [Real Value Type](types/Real-Value-Type.html) | Converts to the level's number (e.g. Info → 4) |
| [Log Tag Type](types/Log-Tag-Type.html) | [String Type](types/String-Type.html) | Converts to the level's name, not its number (e.g. Info → `"Info"`) |
| [Name Type](types/Name-Type.html) | [Index Or Name Type](types/Index-Or-Name-Type.html) | — |
| [Name Type](types/Name-Type.html) | [String Type](types/String-Type.html) | — |
| [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | [Integer Value Type](types/Integer-Value-Type.html) | **Subtyping** — no conversion runs; see Converters and subtyping |
| [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | [Boolean Value Type](types/Boolean-Value-Type.html) | Zero → False, any non-zero value → True |
| [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | [Enum Type](types/Enum-Type.html) | The number is the option's index in the target port's enumeration |
| [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | [Index Or Name Type](types/Index-Or-Name-Type.html) | Can fail — fails for zero |
| [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | [Log Tag Type](types/Log-Tag-Type.html) | Can fail — the number must be a valid level number (e.g. 4 → Info) |
| [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | [Null Value Type](types/Null-Value-Type.html) | — |
| [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | Can fail — no valid target when the input is zero |
| [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | [Real Value Type](types/Real-Value-Type.html) | — |
| [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | [String Type](types/String-Type.html) | — |
| [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | Lossless — widening; the value itself is unchanged |
| [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | [Boolean Value Type](types/Boolean-Value-Type.html) | Zero → False, any non-zero value → True — though a Positive Integer is never zero, so this always yields True in practice |
| [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | [Enum Type](types/Enum-Type.html) | The number is the option's index in the target port's enumeration |
| [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | [Index Or Name Type](types/Index-Or-Name-Type.html) | — |
| [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | [Log Tag Type](types/Log-Tag-Type.html) | Can fail — the number must be a valid level number (e.g. 4 → Info) |
| [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | [Null Value Type](types/Null-Value-Type.html) | — |
| [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | [Real Value Type](types/Real-Value-Type.html) | — |
| [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | [String Type](types/String-Type.html) | — |
| [Real Value Type](types/Real-Value-Type.html) | [Boolean Value Type](types/Boolean-Value-Type.html) | Zero, or a value within rounding tolerance of zero → False, anything else → True |
| [Real Value Type](types/Real-Value-Type.html) | [Enum Type](types/Enum-Type.html) | Can fail — rounds down first; negative values fail; the number is the option's index in the target port's enumeration |
| [Real Value Type](types/Real-Value-Type.html) | [Index Or Name Type](types/Index-Or-Name-Type.html) | Can fail — the value must be greater than zero; the fractional part is dropped |
| [Real Value Type](types/Real-Value-Type.html) | [Integer Value Type](types/Integer-Value-Type.html) | Lossy — rounds down (`3.9` → `3`, `-3.1` → `-4`); fails for values outside the integer range |
| [Real Value Type](types/Real-Value-Type.html) | [Log Tag Type](types/Log-Tag-Type.html) | Can fail — rounds to the nearest integer, which must be a valid level number (e.g. 4.2 → Info) |
| [Real Value Type](types/Real-Value-Type.html) | [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | Lossy — truncates toward zero, then fails if the result is negative (`-0.5` → `0` succeeds, `-1.5` fails) |
| [Real Value Type](types/Real-Value-Type.html) | [Null Value Type](types/Null-Value-Type.html) | — |
| [Real Value Type](types/Real-Value-Type.html) | [Percent Type](types/Percent-Type.html) | Can fail — the value must be in [0, 1] |
| [Real Value Type](types/Real-Value-Type.html) | [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | Lossy — truncates toward zero, then fails if the result isn't positive (`0.9` → `0` fails) |
| [Real Value Type](types/Real-Value-Type.html) | [String Type](types/String-Type.html) | — |
| [Real Value Type](types/Real-Value-Type.html) | [Date Type](types/Date-Type.html) | Lossy — drops the fractional part and uses the result as a year (`2024.7` → `"2024"`) |
| [String Type](types/String-Type.html) | [Code Type](types/Code-Type.html) | Takes the string's text directly as the script — no base64 encoding required |
| [String Type](types/String-Type.html) | [Date Type](types/Date-Type.html) | Takes the text as the date without validating it |
| [String Type](types/String-Type.html) | [Index Or Name Type](types/Index-Or-Name-Type.html) | — |
| [String Type](types/String-Type.html) | [Name Type](types/Name-Type.html) | Can fail — must contain only letters, digits and underscores, and start with a letter or an underscore |
| [String Type](types/String-Type.html) | [Real Value Type](types/Real-Value-Type.html) | Can fail — the string must parse as a valid number (e.g. "test" fails, "3.14" succeeds) |

## Filename and text types

Filenames largely behave like [String Type](types/String-Type.html) with an extra validation step on the way in — see [Constants](EGO-Script.html#constants) for the extension-checking rules each filename type applies to its text. Every filename type here converts to and from String Type; most of them — Generic, Map, Table, Lookup Table, and Weights Filename Type — also convert to and from a generic [Table Value Type](types/Table-Value-Type.html) holder, the same generic-holder role Table Value Type plays for the table-shaped types further down this page. That direction is lossy in every case: going into Table Value Type discards the parent folder path and keeps only the filename itself, so round-tripping back out through String Type or another filename type does not restore the original folder. Folder Type, Kmz Filename Type, and [Projection Type](types/Projection-Type.html) are the exceptions: they connect only to String Type, not to Table Value Type. Converting into a filename type fails for an empty filename, except for Folder Type, where an empty name means the current directory.

| From | To | Notes |
| --- | --- | --- |
| [Folder Type](types/Folder-Type.html) | [String Type](types/String-Type.html) | — |
| [String Type](types/String-Type.html) | [Folder Type](types/Folder-Type.html) | Accepts any name; an empty name means the current directory |
| [String Type](types/String-Type.html) | [Generic Filename Type](types/Generic-Filename-Type.html) | Can fail only for an empty filename — accepts any extension |
| [String Type](types/String-Type.html) | [Map Filename Type](types/Map-Filename-Type.html) | Can fail only for an empty filename — accepts any extension |
| [String Type](types/String-Type.html) | [Table Filename Type](types/Table-Filename-Type.html) | Can fail — extension must be `.csv` |
| [String Type](types/String-Type.html) | [Lookup Table Filename Type](types/Lookup-Table-Filename-Type.html) | Can fail — extension must be `.csv` |
| [String Type](types/String-Type.html) | [Weights Filename Type](types/Weights-Filename-Type.html) | Can fail — extension must be `.dcf`, `.txt`, or `.csv` |
| [String Type](types/String-Type.html) | [Kmz Filename Type](types/Kmz-Filename-Type.html) | Can fail — extension must be `.kmz` |
| [String Type](types/String-Type.html) | [Projection Type](types/Projection-Type.html) | Can fail — the text must be valid WKT (Well-Known Text), or a PROJ.4 definition starting with `+`; an empty string gives the default RAW projection |
| [Generic Filename Type](types/Generic-Filename-Type.html) | [String Type](types/String-Type.html) | — |
| [Generic Filename Type](types/Generic-Filename-Type.html) | [Map Filename Type](types/Map-Filename-Type.html) | — |
| [Generic Filename Type](types/Generic-Filename-Type.html) | [Table Filename Type](types/Table-Filename-Type.html) | Can fail — extension must be `.csv` |
| [Generic Filename Type](types/Generic-Filename-Type.html) | [Lookup Table Filename Type](types/Lookup-Table-Filename-Type.html) | Can fail — extension must be `.csv` |
| [Generic Filename Type](types/Generic-Filename-Type.html) | [Weights Filename Type](types/Weights-Filename-Type.html) | Can fail — extension must be `.dcf`, `.txt`, or `.csv` |
| [Generic Filename Type](types/Generic-Filename-Type.html) | [Table Value Type](types/Table-Value-Type.html) | Lossy — discards the parent folder path, keeping only the filename itself |
| [Map Filename Type](types/Map-Filename-Type.html) | [Generic Filename Type](types/Generic-Filename-Type.html) | — |
| [Map Filename Type](types/Map-Filename-Type.html) | [String Type](types/String-Type.html) | — |
| [Map Filename Type](types/Map-Filename-Type.html) | [Table Value Type](types/Table-Value-Type.html) | Lossy — discards the parent folder path, keeping only the filename itself |
| [Table Filename Type](types/Table-Filename-Type.html) | [String Type](types/String-Type.html) | — |
| [Table Filename Type](types/Table-Filename-Type.html) | [Generic Filename Type](types/Generic-Filename-Type.html) | — |
| [Table Filename Type](types/Table-Filename-Type.html) | [Table Value Type](types/Table-Value-Type.html) | Lossy — discards the parent folder path, keeping only the filename itself |
| [Lookup Table Filename Type](types/Lookup-Table-Filename-Type.html) | [String Type](types/String-Type.html) | — |
| [Lookup Table Filename Type](types/Lookup-Table-Filename-Type.html) | [Generic Filename Type](types/Generic-Filename-Type.html) | — |
| [Lookup Table Filename Type](types/Lookup-Table-Filename-Type.html) | [Table Value Type](types/Table-Value-Type.html) | Lossy — discards the parent folder path, keeping only the filename itself |
| [Weights Filename Type](types/Weights-Filename-Type.html) | [String Type](types/String-Type.html) | — |
| [Weights Filename Type](types/Weights-Filename-Type.html) | [Generic Filename Type](types/Generic-Filename-Type.html) | — |
| [Weights Filename Type](types/Weights-Filename-Type.html) | [Table Value Type](types/Table-Value-Type.html) | Lossy — discards the parent folder path, keeping only the filename itself |
| [Kmz Filename Type](types/Kmz-Filename-Type.html) | [String Type](types/String-Type.html) | — |
| [Table Value Type](types/Table-Value-Type.html) | [Map Filename Type](types/Map-Filename-Type.html) | Can fail — the value must hold a non-empty string; accepts any extension |
| [Table Value Type](types/Table-Value-Type.html) | [Table Filename Type](types/Table-Filename-Type.html) | Can fail — the value must hold a string with extension `.csv` |
| [Table Value Type](types/Table-Value-Type.html) | [Lookup Table Filename Type](types/Lookup-Table-Filename-Type.html) | Can fail — the value must hold a string with extension `.csv` |
| [Table Value Type](types/Table-Value-Type.html) | [Weights Filename Type](types/Weights-Filename-Type.html) | Can fail — the value must hold a string with extension `.dcf`, `.txt`, or `.csv` |
| [Table Value Type](types/Table-Value-Type.html) | [Generic Filename Type](types/Generic-Filename-Type.html) | Can fail — the value must hold a non-empty string; accepts any extension |
| [Projection Type](types/Projection-Type.html) | [String Type](types/String-Type.html) | Produces WKT (Well-Known Text) format |

## Table and Lookup Table types

[Table Type](types/Table-Type.html) sits at the center of this group. It and [Lookup Table Type](types/Lookup-Table-Type.html) are both subtypes of [Base Table Type](types/Base-Table-Type.html) — see [Converters and subtyping](#converters-and-subtyping) above — so their path back to Base Table Type, marked `Subtyping` in the Notes column below, needs no conversion at all. The other way round, Base Table Type → Table Type always succeeds, while Base Table Type → Lookup Table Type checks the layout when the value holds a Table. The rest of the table is more ordinary conversion territory: [Table Value Type](types/Table-Value-Type.html) moving to and from the scalar types a table cell can actually hold, and the individual value types converting into [Tuple Type](types/Tuple-Type.html) and [Table Cell Type](types/Table-Cell-Type.html) for use as keys and column declarations.

| From | To | Notes |
| --- | --- | --- |
| [Base Table Type](types/Base-Table-Type.html) | [Table Type](types/Table-Type.html) | Always succeeds — a Lookup Table held in it becomes a two-column Table |
| [Base Table Type](types/Base-Table-Type.html) | [Lookup Table Type](types/Lookup-Table-Type.html) | Can fail — when the value holds a Table, the Table must have exactly the Lookup Table layout (`*#real, #real`) |
| [Lookup Table Type](types/Lookup-Table-Type.html) | [Base Table Type](types/Base-Table-Type.html) | **Subtyping** — no conversion runs; see Converters and subtyping |
| [Lookup Table Type](types/Lookup-Table-Type.html) | [Table Type](types/Table-Type.html) | — |
| [Lookup Table Type](types/Lookup-Table-Type.html) | [Lookup Table Group Type](types/Lookup-Table-Group-Type.html) | A group holding only this lookup table |
| [Lookup Table Type](types/Lookup-Table-Type.html) | [Change Matrix Type](types/Change-Matrix-Type.html) | Can fail — decodes each key as `From + To / 1000` (`1.002` → 1 → 2); fails for From = To or a negative cell count; cell counts are truncated |
| [Lookup Table Type](types/Lookup-Table-Type.html) | [Percent Matrix Type](types/Percent-Matrix-Type.html) | Can fail — decodes each key as `From + To / 1000` (`1.002` → 1 → 2); fails for From = To or a percent outside [0, 1] |
| [Lookup Table Type](types/Lookup-Table-Type.html) | [Transition Matrix Type](types/Transition-Matrix-Type.html) | Can fail — decodes each key as `From + To / 1000` (`1.002` → 1 → 2); fails for From = To, a rate outside [0, 1], or rates for the same From adding up to more than 1; a rate of 0 drops the transition |
| [Lookup Table Type](types/Lookup-Table-Type.html) | [Transition Set Type](types/Transition-Set-Type.html) | Each key is a From and its value the To, both truncated to integers |
| [Lookup Table Type](types/Lookup-Table-Type.html) | [Int Set Type](types/Int-Set-Type.html) | Lossy — keys are rounded to the nearest integer; values are dropped |
| [Lookup Table Group Type](types/Lookup-Table-Group-Type.html) | [Table Type](types/Table-Type.html) | Produces `Index*`, `Key*`, `Value`, one row per entry |
| [Lookup Table Group Type](types/Lookup-Table-Group-Type.html) | [Base Table Type](types/Base-Table-Type.html) | Can fail — fails if the group is empty; keeps only the first lookup table |
| [Lookup Table Group Type](types/Lookup-Table-Group-Type.html) | [Lookup Table Type](types/Lookup-Table-Type.html) | Can fail — fails if the group is empty; keeps only the first lookup table |
| [Table Type](types/Table-Type.html) | [Base Table Type](types/Base-Table-Type.html) | **Subtyping** — no conversion runs; see Converters and subtyping |
| [Table Type](types/Table-Type.html) | [Lookup Table Type](types/Lookup-Table-Type.html) | Can fail — the table must be exactly `*#real, #real` |
| [Table Type](types/Table-Type.html) | [Lookup Table Group Type](types/Lookup-Table-Group-Type.html) | Can fail — the table must be exactly `*#real, *#real, #real` (index, key, value) |
| [Table Type](types/Table-Type.html) | [Categorization Type](types/Categorization-Type.html) | Can fail — the table must match the Categorization layout; values must fit a 32-bit integer and colors must be in [0, 255] |
| [Table Type](types/Table-Type.html) | [Weights Of Evidence Skeleton Type](types/Weights-Of-Evidence-Skeleton-Type.html) | Can fail — the table must match the Weights Of Evidence Skeleton layout |
| [Table Type](types/Table-Type.html) | [Change Matrix Type](types/Change-Matrix-Type.html) | Can fail — the table must match the Change Matrix layout; fails for From = To or a negative cell count; cell counts are truncated |
| [Table Type](types/Table-Type.html) | [Neighborhood Table Type](types/Neighborhood-Table-Type.html) | Can fail — the table must match the Neighborhood Table layout |
| [Table Type](types/Table-Type.html) | [Percent Matrix Type](types/Percent-Matrix-Type.html) | Can fail — the table must match the Percent Matrix layout; fails for From = To or a percent outside [0, 1] |
| [Table Type](types/Table-Type.html) | [Transition Function Parameter Matrix Type](types/Transition-Function-Parameter-Matrix-Type.html) | Can fail — the table must match the Transition Function Parameter Matrix layout; fails for From = To, a negative isometry, a negative mean or variance, or a mean and variance that are both zero |
| [Table Type](types/Table-Type.html) | [Transition Matrix Type](types/Transition-Matrix-Type.html) | Can fail — the table must match the Transition Matrix layout; fails for From = To, a rate outside [0, 1], or rates for the same From adding up to more than 1; a rate of 0 drops the transition |
| [Table Type](types/Table-Type.html) | [Weights Type](types/Weights-Type.html) | Can fail — the table must match one of the two Weights layouts |
| [Table Value Type](types/Table-Value-Type.html) | [Tuple Type](types/Tuple-Type.html) | A tuple holding this single value |
| [Table Value Type](types/Table-Value-Type.html) | [Generic Filename Type](types/Generic-Filename-Type.html) | Can fail — the value must hold a non-empty string; accepts any extension |
| [Table Value Type](types/Table-Value-Type.html) | [Index Or Name Type](types/Index-Or-Name-Type.html) | Can fail — a number is rounded to the nearest integer and must be greater than zero; a string becomes a name |
| [Table Value Type](types/Table-Value-Type.html) | [Integer Value Type](types/Integer-Value-Type.html) | Can fail — the value must hold a number within the integer range; the fractional part is dropped |
| [Table Value Type](types/Table-Value-Type.html) | [Name Type](types/Name-Type.html) | Can fail — the value must hold a string that is a valid name |
| [Table Value Type](types/Table-Value-Type.html) | [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | Can fail — the value must hold a number; the fractional part is dropped and the result must be zero or greater |
| [Table Value Type](types/Table-Value-Type.html) | [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | Can fail — the value must hold a number; the fractional part is dropped and the result must be greater than zero |
| [Table Value Type](types/Table-Value-Type.html) | [Real Value Type](types/Real-Value-Type.html) | Can fail — only succeeds if the value actually holds a Real Value |
| [Table Value Type](types/Table-Value-Type.html) | [String Type](types/String-Type.html) | Can fail — only succeeds if the value actually holds a String |
| [Table Value Type](types/Table-Value-Type.html) | [Table Filename Type](types/Table-Filename-Type.html) | Can fail — the value must hold a string with extension `.csv` |
| [Table Value Type](types/Table-Value-Type.html) | [Lookup Table Filename Type](types/Lookup-Table-Filename-Type.html) | Can fail — the value must hold a string with extension `.csv` |
| [Table Value Type](types/Table-Value-Type.html) | [Weights Filename Type](types/Weights-Filename-Type.html) | Can fail — the value must hold a string with extension `.dcf`, `.txt`, or `.csv` |
| [Table Value Type](types/Table-Value-Type.html) | [Map Filename Type](types/Map-Filename-Type.html) | Can fail — the value must hold a non-empty string; accepts any extension |
| [Integer Value Type](types/Integer-Value-Type.html) | [Table Cell Type](types/Table-Cell-Type.html) | Can fail — the number must be a valid table cell type number |
| [Integer Value Type](types/Integer-Value-Type.html) | [Table Value Type](types/Table-Value-Type.html) | — |
| [Integer Value Type](types/Integer-Value-Type.html) | [Tuple Type](types/Tuple-Type.html) | — |
| [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | [Table Cell Type](types/Table-Cell-Type.html) | Can fail — the number must be a valid table cell type number |
| [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | [Table Value Type](types/Table-Value-Type.html) | — |
| [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | [Tuple Type](types/Tuple-Type.html) | — |
| [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | [Table Cell Type](types/Table-Cell-Type.html) | Can fail — the number must be a valid table cell type number |
| [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | [Table Value Type](types/Table-Value-Type.html) | — |
| [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | [Tuple Type](types/Tuple-Type.html) | — |
| [Real Value Type](types/Real-Value-Type.html) | [Table Cell Type](types/Table-Cell-Type.html) | Can fail — the number must be a valid table cell type number; rounds to the nearest integer first |
| [Real Value Type](types/Real-Value-Type.html) | [Table Value Type](types/Table-Value-Type.html) | — |
| [Real Value Type](types/Real-Value-Type.html) | [Tuple Type](types/Tuple-Type.html) | — |
| [Name Type](types/Name-Type.html) | [Table Value Type](types/Table-Value-Type.html) | — |
| [Name Type](types/Name-Type.html) | [Tuple Type](types/Tuple-Type.html) | — |
| [String Type](types/String-Type.html) | [Table Value Type](types/Table-Value-Type.html) | — |
| [String Type](types/String-Type.html) | [Tuple Type](types/Tuple-Type.html) | — |

## Map and raster types

[Categorical Map Type](types/Categorical-Map-Type.html)'s path to [Map Type](types/Map-Type.html), marked `Subtyping` in the Notes column below, is the clearest example of subtyping on this page — see [Converters and subtyping](#converters-and-subtyping) above. A Categorical Map Type value converts automatically wherever a Map Type is expected, keeping its cells and null value intact and dropping only the guarantee that a categorization is attached; the reverse never happens automatically, since an arbitrary Map Type value isn't guaranteed to carry one — which is why there's no corresponding Map Type → Categorical Map Type entry at all. The rest of the table below is [Cell Type](types/Cell-Type.html)'s round trip with the numeric value types, and the two paths a categorical map takes toward its supporting data: its legend, as a [Categorization Type](types/Categorization-Type.html), and its spatial reference, as a [Projection Type](types/Projection-Type.html).

| From | To | Notes |
| --- | --- | --- |
| [Cell Type](types/Cell-Type.html) | [Real Value Type](types/Real-Value-Type.html) | Converts to the cell type's number (e.g. Signed 32 Bit Integer → 5) |
| [Cell Type](types/Cell-Type.html) | [Integer Value Type](types/Integer-Value-Type.html) | Converts to the cell type's number (e.g. Signed 32 Bit Integer → 5) |
| [Cell Type](types/Cell-Type.html) | [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | Converts to the cell type's number (e.g. Signed 32 Bit Integer → 5) |
| [Cell Type](types/Cell-Type.html) | [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | Can fail — fails for 1 Bit Integer (numeric value 0); converts to the cell type's number otherwise (e.g. Signed 32 Bit Integer → 5) |
| [Real Value Type](types/Real-Value-Type.html) | [Cell Type](types/Cell-Type.html) | Can fail — the number must be a valid cell type number (e.g. 5 → Signed 32 Bit Integer); rounds to the nearest integer first |
| [Integer Value Type](types/Integer-Value-Type.html) | [Cell Type](types/Cell-Type.html) | Can fail — the number must be a valid cell type number (e.g. 5 → Signed 32 Bit Integer) |
| [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html) | [Cell Type](types/Cell-Type.html) | Can fail — the number must be a valid cell type number (e.g. 5 → Signed 32 Bit Integer) |
| [Positive Integer Value Type](types/Positive-Integer-Value-Type.html) | [Cell Type](types/Cell-Type.html) | Can fail — the number must be a valid cell type number (e.g. 5 → Signed 32 Bit Integer) |
| [Categorical Map Type](types/Categorical-Map-Type.html) | [Map Type](types/Map-Type.html) | **Subtyping** — no conversion runs; see Converters and subtyping |
| [Categorical Map Type](types/Categorical-Map-Type.html) | [Categorization Type](types/Categorization-Type.html) | — |
| [Categorical Map Type](types/Categorical-Map-Type.html) | [Projection Type](types/Projection-Type.html) | — |
| [Categorization Type](types/Categorization-Type.html) | [Table Type](types/Table-Type.html) | — |
| [Table Type](types/Table-Type.html) | [Categorization Type](types/Categorization-Type.html) | Can fail — the table must match the Categorization layout; values must fit a 32-bit integer and colors must be in [0, 255] |
| [Map Type](types/Map-Type.html) | [Projection Type](types/Projection-Type.html) | — |

## Simulation types

Every matrix-shaped type here — [Change Matrix Type](types/Change-Matrix-Type.html), [Percent Matrix Type](types/Percent-Matrix-Type.html), [Transition Matrix Type](types/Transition-Matrix-Type.html), and the rest — follows the same pattern: each one converts to and from a [Table Type](types/Table-Type.html) (or [Lookup Table Type](types/Lookup-Table-Type.html)) with one particular expected column layout, and converting between them is mostly a matter of adding or checking for that layout. This is a conversion relationship, not structural identity — [Neighborhood Table Type](types/Neighborhood-Table-Type.html) and [Weights Type](types/Weights-Type.html), for instance, have no editable constant of their own despite converting to and from Table Type; a value is obtained only from a producing functor or from this conversion. See [Table format of table-shaped types](#table-format-of-table-shaped-types) below for the exact columns each one expects. Conversions between a matrix type and [Lookup Table Type](types/Lookup-Table-Type.html) encode each transition as a single key, `From + To / 1000` (transition 1 → 2 is key `1.002`), so only `To` values from 0 to 999 survive the round trip.

| From | To | Notes |
| --- | --- | --- |
| [Change Matrix Type](types/Change-Matrix-Type.html) | [Lookup Table Type](types/Lookup-Table-Type.html) | Lossy — the key is `From + To / 1000` (1 → 2 becomes `1.002`); only `To` values from 0 to 999 survive |
| [Change Matrix Type](types/Change-Matrix-Type.html) | [Table Type](types/Table-Type.html) | — |
| [Lookup Table Type](types/Lookup-Table-Type.html) | [Change Matrix Type](types/Change-Matrix-Type.html) | Can fail — decodes each key as `From + To / 1000` (`1.002` → 1 → 2); fails for From = To or a negative cell count; cell counts are truncated |
| [Lookup Table Type](types/Lookup-Table-Type.html) | [Percent Matrix Type](types/Percent-Matrix-Type.html) | Can fail — decodes each key as `From + To / 1000` (`1.002` → 1 → 2); fails for From = To or a percent outside [0, 1] |
| [Lookup Table Type](types/Lookup-Table-Type.html) | [Transition Matrix Type](types/Transition-Matrix-Type.html) | Can fail — decodes each key as `From + To / 1000` (`1.002` → 1 → 2); fails for From = To, a rate outside [0, 1], or rates for the same From adding up to more than 1; a rate of 0 drops the transition |
| [Lookup Table Type](types/Lookup-Table-Type.html) | [Transition Set Type](types/Transition-Set-Type.html) | Each key is a From and its value the To, both truncated to integers |
| [Table Type](types/Table-Type.html) | [Change Matrix Type](types/Change-Matrix-Type.html) | Can fail — the table must match the Change Matrix layout; fails for From = To or a negative cell count; cell counts are truncated |
| [Table Type](types/Table-Type.html) | [Neighborhood Table Type](types/Neighborhood-Table-Type.html) | Can fail — the table must match the Neighborhood Table layout |
| [Table Type](types/Table-Type.html) | [Percent Matrix Type](types/Percent-Matrix-Type.html) | Can fail — the table must match the Percent Matrix layout; fails for From = To or a percent outside [0, 1] |
| [Table Type](types/Table-Type.html) | [Transition Function Parameter Matrix Type](types/Transition-Function-Parameter-Matrix-Type.html) | Can fail — the table must match the Transition Function Parameter Matrix layout; fails for From = To, a negative isometry, a negative mean or variance, or a mean and variance that are both zero |
| [Table Type](types/Table-Type.html) | [Transition Matrix Type](types/Transition-Matrix-Type.html) | Can fail — the table must match the Transition Matrix layout; fails for From = To, a rate outside [0, 1], or rates for the same From adding up to more than 1; a rate of 0 drops the transition |
| [Table Type](types/Table-Type.html) | [Weights Type](types/Weights-Type.html) | Can fail — the table must match one of the two Weights layouts |
| [Percent Matrix Type](types/Percent-Matrix-Type.html) | [Lookup Table Type](types/Lookup-Table-Type.html) | Lossy — the key is `From + To / 1000` (1 → 2 becomes `1.002`); only `To` values from 0 to 999 survive |
| [Percent Matrix Type](types/Percent-Matrix-Type.html) | [Table Type](types/Table-Type.html) | — |
| [Transition Matrix Type](types/Transition-Matrix-Type.html) | [Lookup Table Type](types/Lookup-Table-Type.html) | Lossy — the key is `From + To / 1000` (1 → 2 becomes `1.002`); only `To` values from 0 to 999 survive |
| [Transition Matrix Type](types/Transition-Matrix-Type.html) | [Table Type](types/Table-Type.html) | — |
| [Transition Function Parameter Matrix Type](types/Transition-Function-Parameter-Matrix-Type.html) | [Table Type](types/Table-Type.html) | — |
| [Neighborhood Table Type](types/Neighborhood-Table-Type.html) | [Table Type](types/Table-Type.html) | — |
| [Elevation Graph Type](types/Elevation-Graph-Type.html) | [Neighborhood Table Type](types/Neighborhood-Table-Type.html) | Each node paired with itself gets weight 0; each node paired with each of its parents gets weight 1 |
| [Elevation Graph Type](types/Elevation-Graph-Type.html) | [String Type](types/String-Type.html) | Produces the graph as JSON |
| [Weights Type](types/Weights-Type.html) | [Table Type](types/Table-Type.html) | — |

## Calibration types

The one conversion pair here follows the same table-shaped logic as the simulation types above — see [Table format of table-shaped types](#table-format-of-table-shaped-types) below for its column layout.

| From | To | Notes |
| --- | --- | --- |
| [Table Type](types/Table-Type.html) | [Weights Of Evidence Skeleton Type](types/Weights-Of-Evidence-Skeleton-Type.html) | Can fail — the table must match the Weights Of Evidence Skeleton layout |
| [Weights Of Evidence Skeleton Type](types/Weights-Of-Evidence-Skeleton-Type.html) | [Table Type](types/Table-Type.html) | — |

## Table format of table-shaped types

Several of the types above convert to and from [Table Type](types/Table-Type.html) (or [Lookup Table Type](types/Lookup-Table-Type.html)) under one particular, expected column layout: converting to Table Type keeps the same rows but drops the type's special meaning, and converting from Table Type checks that the table actually has this shape — the same conditional-conversion pattern described above. As noted in Simulation types, this is strictly a conversion relationship: it doesn't imply the type has an editor or constant syntax matching Table Type's own. In fact, [Transition Matrix Type](types/Transition-Matrix-Type.html), [Change Matrix Type](types/Change-Matrix-Type.html), [Percent Matrix Type](types/Percent-Matrix-Type.html), [Transition Function Parameter Matrix Type](types/Transition-Function-Parameter-Matrix-Type.html), and [Weights Of Evidence Skeleton Type](types/Weights-Of-Evidence-Skeleton-Type.html) each have their own dedicated EGO Script literal syntax, keyed on `From->To` pairs rather than named columns — see each type's own page for its exact grammar. The engine registers an exact default format for most of these; key columns are marked `*` the way [Table Type](types/Table-Type.html) itself marks them. Converting from Table Type checks only the number of columns, their types and which ones are keys; column names are not checked, so the names below are the ones produced when converting to Table Type. [Table Type's own Automatic Conversions section](types/Table-Type.html#automatic-conversions) and [Manipulating Tables and Lookup Tables](Manipulating-Tables-And-Lookup-Tables.html) both describe the Lookup Table Type row below in those same terms — its `*#real, #real` shape already matching what a single-value table needs.

| Type | Direction | Table format |
| --- | --- | --- |
| [Lookup Table Type](types/Lookup-Table-Type.html) | ↔ Table Type | `Key*` (Real), `Value` (Real) |
| [Lookup Table Group Type](types/Lookup-Table-Group-Type.html) | ↔ Table Type | `Index*` (Real), `Key*` (Real), `Value` (Real) — one row per entry; `Index` is the lookup table's position in the group, starting at 0 |
| [Categorization Type](types/Categorization-Type.html) | ↔ Table Type | `Value*` (Real), `Name` (String), `Color_Red` (Real), `Color_Green` (Real), `Color_Blue` (Real) — `Name` may be left blank when converting into a Categorization; it falls back to an auto-generated `class_N` (or `class_nN` for a negative value) |
| [Change Matrix Type](types/Change-Matrix-Type.html) | ↔ Table Type | `From*` (Real), `To*` (Real), `Cells` (Real) |
| [Percent Matrix Type](types/Percent-Matrix-Type.html) | ↔ Table Type | `From*` (Real), `To*` (Real), `Percent` (Real) |
| [Transition Matrix Type](types/Transition-Matrix-Type.html) | ↔ Table Type | `From*` (Real), `To*` (Real), `Rate` (Real) |
| [Transition Function Parameter Matrix Type](types/Transition-Function-Parameter-Matrix-Type.html) | ↔ Table Type | `From*` (Real), `To*` (Real), `Mean_Patch_Size` (Real), `Patch_Size_Variance` (Real), `Patch_Isometry` (Real) |
| [Neighborhood Table Type](types/Neighborhood-Table-Type.html) | ↔ Table Type | `Neighbor1*` (Real), `Neighbor2*` (Real), `Weight` (Real) |
| [Weights Type](types/Weights-Type.html) | ↔ Table Type | `From*` (Real), `To*` (Real), `Variable*` (String), `Range_Lower_Limit*` (Real), `Range_Upper_Limit*` (Real), `Weight` (Real) — converting into Weights also accepts the same layout without `Range_Upper_Limit`, where each range ends at the next row's `Range_Lower_Limit` |
| [Weights Of Evidence Skeleton Type](types/Weights-Of-Evidence-Skeleton-Type.html) | ↔ Table Type | `From*` (Real), `To*` (Real), `Variable_Name*` (String), `Categorical` (Real), `Increment` (Real), `Minimum_Delta` (Real), `Maximum_Delta` (Real), `Tolerance_Angle` (Real) |

> **Note:** [Transition Set Type](types/Transition-Set-Type.html) is left out of this table on purpose — it converts one-way from [Lookup Table Type](types/Lookup-Table-Type.html) but never to or from [Table Type](types/Table-Type.html) directly, so it has no registered table format either. [Base Table Type](types/Base-Table-Type.html) is left out for a different reason: it has no fixed column layout of its own — see [Table and Lookup Table types](#table-and-lookup-table-types) above for how it converts.

## Region types

[Region Manager Type](types/Region-Manager-Type.html) stands apart from every other type on this page: it has no automatic conversions to or from anything else. The only conversion registered for it at all is the sequencing conversion to [None Type](types/None-Type.html) described below.

## Sequencing

A conversion **to [None Type](types/None-Type.html)** — used to force an execution order between two functors rather than to transform a value, most visibly through the `sequenceInput`/`sequenceOutput` ports [EGO Script](EGO-Script.html#sequence-ports) exposes on most containers — is registered for the following types:

[Connection Info Type](types/Connection-Info-Type.html), [Boolean Value Type](types/Boolean-Value-Type.html), [Code Type](types/Code-Type.html), [Date Type](types/Date-Type.html), [Enum Type](types/Enum-Type.html), [Folder Type](types/Folder-Type.html), [Generic Filename Type](types/Generic-Filename-Type.html), [Image Expression Type](types/Image-Expression-Type.html), [Index Or Name Type](types/Index-Or-Name-Type.html), [Int Set Type](types/Int-Set-Type.html), [Integer Value Type](types/Integer-Value-Type.html), [Log Tag Type](types/Log-Tag-Type.html), [Name Type](types/Name-Type.html), [Non Negative Integer Value Type](types/Non-Negative-Integer-Value-Type.html), [Null Value Type](types/Null-Value-Type.html), [Percent Type](types/Percent-Type.html), [Positive Integer Value Type](types/Positive-Integer-Value-Type.html), [Real Value Type](types/Real-Value-Type.html), [String Type](types/String-Type.html), [Struct Type](types/Struct-Type.html), [Workdir Type](types/Workdir-Type.html), [Categorical Map Type](types/Categorical-Map-Type.html), [Categorization Type](types/Categorization-Type.html), [Cell Type](types/Cell-Type.html), [Kml Type](types/Kml-Type.html), [Kml Timeline Type](types/Kml-Timeline-Type.html), [Kmz Filename Type](types/Kmz-Filename-Type.html), [Map Type](types/Map-Type.html), [Map Filename Type](types/Map-Filename-Type.html), [Projection Type](types/Projection-Type.html), [Weights Of Evidence Skeleton Type](types/Weights-Of-Evidence-Skeleton-Type.html), [Change Matrix Type](types/Change-Matrix-Type.html), [Neighborhood Table Type](types/Neighborhood-Table-Type.html), [Percent Matrix Type](types/Percent-Matrix-Type.html), [Transition Function Parameter Matrix Type](types/Transition-Function-Parameter-Matrix-Type.html), [Transition Matrix Type](types/Transition-Matrix-Type.html), [Transition Set Type](types/Transition-Set-Type.html), [Weights Type](types/Weights-Type.html), [Weights Filename Type](types/Weights-Filename-Type.html), [Elevation Graph Type](types/Elevation-Graph-Type.html), [Region Manager Type](types/Region-Manager-Type.html), [Base Table Type](types/Base-Table-Type.html), [Lookup Table Type](types/Lookup-Table-Type.html), [Lookup Table Filename Type](types/Lookup-Table-Filename-Type.html), [Lookup Table Group Type](types/Lookup-Table-Group-Type.html), [Table Filename Type](types/Table-Filename-Type.html), [Table Type](types/Table-Type.html), [Table Manager Type](types/Table-Manager-Type.html), [Table Value Type](types/Table-Value-Type.html), [Tuple Type](types/Tuple-Type.html)
{% endraw %}
