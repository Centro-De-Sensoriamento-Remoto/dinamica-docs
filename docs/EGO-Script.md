---
title: "EGO Script Language"
nav_order: 1
parent: "Language and Expressions"
---
{% raw %}
# EGO Script Language

# Introduction

EGO Script is a simple, text-based language for creating and editing Dinamica EGO models. A model written in this format is stored in a file with the `.ego` extension. An `.ego` file is just another way of describing a model — it is equivalent to the XML form Dinamica EGO uses internally. Because the two are interchangeable, you can write a model as an EGO script, open it in the graphical interface, edit it there, and save it again, moving freely between the textual and visual representations. See [Basic Data Flow](Basic-Data-Flow.html) for the execution model shared by both representations; this tutorial covers the textual notation specifically.

> **Caution:** When you round-trip a model through the graphical interface, the interface can rewrite a model's layout and the format of its inputs and outputs according to the options currently in effect, so a script reopened and saved from the GUI may not come back byte-for-byte identical to what you wrote. This is normal, and the resulting model is equivalent.

> **Tip:** There are two practical ways to move between the visual and textual representations. First, a whole model can be saved as a `.ego` file from the GUI via *File* → *Save Model*, and reopened via *File* → *Open Model*. Second, any selection of functors in the GUI sketch — or the entire model — can be copied to the clipboard and pasted directly into an external text editor as an EGO Script fragment; conversely, any EGO Script fragment copied from a text editor can be pasted straight into the GUI sketch.

This tutorial introduces the language from the ground up: the structure of a model, how functors are called and wired together, how containers and properties work, and the shorthand used to write expressions.

# Overview

A complete EGO script model can be as short as the example below. It loads a raster map and saves a copy of it in a different format:

```
Script {{
  // Loads a GeoTiff map.
  x := LoadMap "c:/map.tif";
  // Saves an ERMapper map.
  SaveMap x "c:/map-copy.ers";
}};
```

Even this small example shows every essential element of the language.

## The Script block

The `Script {{ }}` block delimits the script text. A single file can carry several script elements, and the `Script` block is what groups them together. For backward compatibility with earlier versions, this declaration may be omitted.

> **Tip:** Omitting the `Script` block is discouraged — always wrap a model in an explicit `Script` block.

## Functors, variables, and binding

Each statement inside the block calls a **functor** — a processing unit that consumes inputs and produces outputs. The second line of the example calls a [Load Map](functors/Load-Map.html) to load the GeoTiff file `"map.tif"`, and binds the resulting map to the variable `x`. Two conventions are worth noting right away. First, a functor's name is written **without spaces** (`LoadMap`, not `Load Map`). Second, a variable is always defined and bound with the `:=` operator. The third line calls [Save Map](functors/Save-Map.html) to write the map held by `x` to an ERMapper file named `"c:/map-copy.ers"`. The position of a value relative to the functor name determines whether it is an input or an output:

- Values and variables written **after** the functor name are bound to its **input** ports.
- Variables written **before** the `:=` operator are bound to its **output** ports.

So in `x := LoadMap "c:/map.tif"`, the string `"c:/map.tif"` is an input and `x` receives the output; in `SaveMap x "c:/map-copy.ers"`, both `x` and the filename are inputs, and the call produces no output at all.

A variable name must begin with an underscore or a letter, and may be followed by any combination of underscores, letters, and digits (`[_a-zA-Z][_a-zA-Z0-9]*`). Variable names are case-sensitive.

Variables are how functors pass data to one another: a functor that reads a variable depends on the functor that binds it, and cannot run before it. Functors that share no variable, directly or through a chain of variables, have no dependency on each other and may run in any order or at the same time. [Container functors](#container-functors) add a second ordering constraint on top of this. See [Basic Data Flow](Basic-Data-Flow.html) for the complete execution model, which does not depend on EGO Script.

> **Note:** The position of a functor definition in the script file does not determine when it runs. Unless two functors are connected by a data dependency — directly or through a chain of variables — never assume anything about their relative execution order. The only exception is [containers](#container-functors), covered later in this section.

## A first look at comments

The sequence `//` begins a comment, which continues to the end of the line. The two comment lines in the example document what each step does. Comments are more than annotations — they attach to the functor that follows them and are preserved with the model; the [Comments](#comments) section of the reference describes this in detail.

# Reference

This section describes how a functor call is written in EGO Script, the three interchangeable styles for supplying its inputs, how container functors hold and communicate with the functors nested inside them, the shorthand notation used to write the calculator functors that evaluate expressions, and how comments and properties annotate a model.

---

## Functor calls

A functor call binds **outputs** — the variables written before `:=` — and consumes **inputs** — the values, variables, and constants written after the functor name. Every functor defines a fixed set of typed **[ports](#ports)** for its inputs and outputs:

```
areaTable := CalcAreas landscape .no;
```

Here [Calc Areas](functors/Calc-Areas.html) reads two inputs (`landscape` and the constant `.no`) and produces one output, bound to the variable `areaTable`. Constants are written with a leading dot (`.no`, `.default`, `.int32`, `.none`) — see [Constants](#constants) below.

Inputs can be supplied in three interchangeable styles — [positional](#positional-syntax), [nominal](#nominal-syntax), and [inline](#inline-syntax). The styles may be mixed freely between calls, and even within a single call.

### Ports

Every input and output of a functor is a **port**. Ports have a name and a type, and input ports are either required or optional, possibly nullable, and editable or not; these attributes are described in [Functors and Ports](Functors-And-Ports.html#ports). In a script, they determine what a call may leave out and what it may write as a constant. A required input must always be supplied, while an optional one may be omitted and then takes its default value — see [Positional syntax](#positional-syntax) and [Nominal syntax](#nominal-syntax) below for how. A nullable port can also be explicitly left without a value with `.none`. Only editable ports accept [constants](#constants); a non-editable port must be bound to a variable or to an [inlined](#inline-syntax) call.

For how port names are written in the script and displayed in the GUI, see [Alias and variable name conversion](#alias-and-variable-name-conversion). For the ports that connect containers to the functors nested inside them, see [Internal output ports](#internal-output-ports), [Internal input ports](#internal-input-ports) and [Auto-bound ports](#auto-bound-ports) below.

### Constants

Constants supply a fixed value directly to an input port, without connecting a functor. Despite often looking similar in syntax, every constant is interpreted and validated according to the type of the port it is supplied to — a value that is valid for one port type may be rejected by another. They come in four forms.

Automatic type conversion — such as a Real value becoming a Tuple, or a String becoming a Code value — only happens when a value is **connected**: through a variable reference, or a functor call inlined directly into an argument. It never applies to a constant. A constant is parsed by the port's own type-specific parser, which accepts only that type's literal syntax and rejects anything else, even a literal that some other, compatible type would accept. See [Basic Data Flow](Basic-Data-Flow.html#functors-and-connections) for this distinction and [Type System](Type-System.html) for the complete catalog of types and conversions.

**Numeric literals** — integer or real values written directly: `0`, `250`, `3.14`.

**Text constants** — text enclosed in double quotes. Despite looking identical in syntax, text constants are interpreted and validated according to the port's type. The types that accept the basic `%%"%%text%%"%%` form include `String`, `MapFilename`, `TableFilename`, `LookupTableFilename`, `WeightsFilename`, `GenericFilename`, `Folder`, and `Name` — but each imposes its own validation:

- **Filename ports** (`MapFilename`, `TableFilename`, etc.) typically verify that the file extension is appropriate for that type. For example, `"test.tif"` is accepted by a `MapFilename` port but rejected by a `TableFilename` port, since `.tif` is not a valid table file extension.
- **`Name` ports** only accept identifiers that follow the same naming rules as variables — starting with a letter or underscore, followed only by letters, digits, and underscores. `"distance_to_roads"` is valid; `"Distance To Roads"` is not.

```
// used as a MapFilename
"c:/data/landscape.tif"
// used as a Name
"distanceToRoads"
```

[Code](types/Code-Type.html) ports also accept this basic `"text"` form, but interpret it differently from the types above: rather than validating the text itself, the content is decoded as base64 to produce the script — see the note below.

For `String` ports that contain line breaks or double-quote characters, use the extended form `$"DELIMITER(content)DELIMITER"`. The content is everything between the opening `(` and the closing `)`, and the DELIMITER — any sequence of characters placed between the `%%"%%` and the `(`, including empty — makes the closing `)"` unambiguous. The delimiter must be identical on both sides. [Code](types/Code-Type.html) ports accept this same extended form directly too, using the content as the literal script text with no encoding involved — see [Code Type](types/Code-Type.html) for the full grammar. No other port type accepts it:

```
// basic form — line break inside the content
$"(Hello
world)"

// X as delimiter — content contains )" which would otherwise terminate the basic form early
$"X(some )" text)X"
```

**Dot constants** — a leading dot followed by a keyword: `.yes`, `.no`, `.int32`, `.default`. Each data type defines its own set of dot constants and the constants accepted by a port depend entirely on its type. Two dot constants are predefined and available for **any** input port regardless of type:

- `.UNBOUND` — the port is not connected, or its connection is deliberately being ignored. This appears in particular when a script fragment is copied from the GUI to a text editor and some of the original connections are not part of the copied selection.
- `.none` — the port is intentionally left without a value. Valid **only for optional nullable input ports**.

**Structured constants** — complex values enclosed in square brackets `[ … ]`, specific to individual functors and can be multi-line: `[ 2->1 0.05 ]`, `[ "Key" "Value" ]`.

Lookup table literals support an additional shorthand: `startKey startValue .. endKey endValue` auto-generates every key from `startKey` to `endKey` (incrementing by one), with values linearly interpolated between `startValue` and `endValue`. Range entries and plain `key value` entries can be mixed freely, and commas between entries are optional:

```
[ "Key" "Value", 1 1 .. 4 1, 5 -8, 6 1 .. 9 1 ]
```

Since the start and end values in each range above are equal, interpolating between them keeps the value constant — keys 1–4 and 6–9 all map to `1`, and key 5 maps to `-8`. When a script is saved from the GUI, ranges like this are automatically collapsed back into `..` notation where possible. See [Lookup Table Type](types/Lookup-Table-Type.html) for the full syntax, including optional key/value column names, and [Table Type](types/Table-Type.html) for the syntax rules that apply to tables in general.

A general table follows the same bracket syntax but allows any number of columns, mixing Real and String data, with types inferred from each column's own values unless overridden with a `#type` suffix:

```
[
  "PatchId*#string", "Area", "Category",
  007, 12.4, "forest",
  013, 8.7, "pasture"
]
```

Without the `#string` override, `PatchId`'s unquoted values would be inferred as Real numbers — `007` would collapse to the number `7`, losing its leading zero. The explicit type forces String interpretation instead, preserving each value exactly as written. `Area` and `Category` are left to plain inference: Real from `12.4`/`8.7`, String from the quoted `"forest"`/`"pasture"`.

A call can mix all forms with variable references in a single argument list:

```
landscape := LoadCategoricalMap "c:/data/landscape.tif" .none .default 0;
```

Here `"c:/data/landscape.tif"` is a map filename constant (the `filename` port is type `MapFilename`), `.none` leaves the nullable `nullValue` port without a value, `.default` is a storage mode dot constant, and `0` is a numeric literal.

```
changes := CalcChangeMatrix landscape [ 2->1 0.05 ];
```

Here `[ 2->1 0.05 ]` is a structured constant representing a transition matrix with a 5% rate from class 2 to class 1.

> **Note:** [Code](types/Code-Type.html) — the type used for expression inputs such as the Python code in [Calculate Python Expression](functors/Calculate-Python-Expression.html) — has its own literal syntax, parsed directly rather than through a conversion, and accepts two forms: the extended `$"DELIMITER(content)DELIMITER"` form described above, taken directly as the script's text with no encoding involved; and the basic double-quoted `"text"` form, whose content is instead decoded as base64 to produce the script. See [Code Type](types/Code-Type.html) for the full grammar and examples of both forms.

### Positional syntax

In positional syntax, arguments fill the input ports in order: the first argument fills the first port, the second fills the second, and so on.

```
landscape := LoadCategoricalMap "c:/landscape.tif";
areaTable := CalcAreas landscape .no;
```

**Omitting optional inputs.** A functor's optional input ports always come after its required ones. In positional syntax you may stop supplying arguments early, but you cannot skip an optional input and then supply a later one — once you omit a port, every port after it is omitted too. To leave a gap, use [nominal syntax](#nominal-syntax) (described below) for that call.

[Load Categorical Map](functors/Load-Categorical-Map.html), for example, takes a required filename followed by several optional inputs; this call supplies the first few of them positionally and omits the rest:

```
landscape := LoadCategoricalMap "c:/landscape.ers" .none .default 0 0 0 100 100;
```

**Discarding outputs.** A functor may return several outputs. Write an underscore (`_`) in any output position to discard that output. When you want only one output from the middle of the list, underscores act as placeholders for the positions you skip:

```
// GetProjectionInfo returns nine outputs; keep only the seventh (the coordinate type):
_ _ _ _ _ _ coordinateType _ _ := GetProjectionInfo landscape;

// GetElevationGraphInfo returns three outputs; keep only the first:
patchInfo _ _ := GetElevationGraphInfo elevationGraph .no .no;
```

A functor with no outputs at all is written as a bare call, with no assignment and no underscore — there is nothing to discard. [Save Map](functors/Save-Map.html) and [Save Table](functors/Save-Table.html) are the common cases.

### Nominal syntax

In nominal syntax (also referred to as **named parameters** in the Dinamica EGO GUI options), inputs are enclosed in a pair of **single curly braces** `{ }` and bound **by port name**: each entry is written as `portName = value`, with entries separated by commas. Order does not matter, and any optional port may be omitted regardless of position. See [Ports](#ports) above for a full description of port properties including types, nullability, and default values. This is the clearest style for functors with many optional inputs:

```
patchMap := CalcPatchLabelMap {
    source = elevationMap,
    initialPatchLabel = 1,
    onlyOrthogonalsAreAllowed = .no,
    windowLines = 3,
    windowColumns = 3,
    cellType = .int32,
    nullValue = .default,
    patchLabelsAreSparse = .no,
    useSequentialPatchLabels = .no
};
```

> **Note:** Port names in the script use camelCase with a lowercase first letter (e.g. `cellType`, `resultIsSparse`). In the GUI the same ports are displayed with spaces between words and all words capitalised (e.g. "Cell Type", "Result Is Sparse"). The same conversion rules that govern functor aliases and variable names apply here — see [Alias and variable name conversion](#alias-and-variable-name-conversion).

> **Note:** The single braces `{ }` used here for nominal syntax are distinct from the double braces `{{ }}` used to delimit a [container functor](#container-functors)'s block of contained functors.

Outputs follow the **opposite** rule. An output is bound by name as `variable = portName` — the variable you choose on the left, the functor's output port name on the right — also inside single braces `{ }`, placed before `:=`:

```
{ areaTable = areas } := CalcAreas { source = landscape };
```

When a functor produces multiple outputs, all of them can be bound in a single braces block, separated by commas:

```
{ woeCoefficients = weights, woeReport = report } := DetermineWeightsOfEvidenceCoefficients initialLandscape finalLandscape ranges;
```

When only some of a functor's outputs are wanted, the rest can simply be left out of the block entirely — nominal syntax binds by name, so there's no position to hold open the way [positional syntax](#positional-syntax) requires. An unwanted output can also be bound to `_` instead of omitted; this changes nothing about execution, it only makes explicit, at the call site, that the output was considered and deliberately discarded rather than overlooked.

So inputs read `portName = value` while outputs read `variable = portName`. The two directions are summarized below:

| Position | Form | Left side | Right side |
| --- | --- | --- | --- |
| Input (after name) | `portName = value` | input port name | value/variable |
| Output (before `:=`) | `variable = portName` | your variable | output port name |

Styles may be combined. A call can take positional inputs but bind a named output, or vice versa:

```
landscape := LoadCategoricalMap { filename = "c:/landscape.tif" };
{ areaTable = areas } := CalcAreas landscape;
SaveTable { table = areaTable, filename = "c:/areas.csv" };
```

The port names used in nominal syntax are the input and output names defined by each functor (for instance, [Calc Patch Label Map](functors/Calc-Patch-Label-Map.html) defines the inputs `source`, `initialPatchLabel`, `windowLines`, and so on). Names are case-sensitive.

### Inline syntax

Inline syntax nests one call directly inside another instead of binding an intermediate variable. The nested call is wrapped in parentheses, and its single output is passed straight into the enclosing input port — the same idea as nesting function calls in conventional programming languages.

These two fragments are equivalent. The first names an intermediate variable:

```
landscape := LoadCategoricalMap { filename = "c:/landscape.tif" };
{ areaTable = areas } := CalcAreas landscape;
```

The second inlines the `LoadCategoricalMap` call into the `CalcAreas` call:

```
{ areaTable = areas } := CalcAreas (LoadCategoricalMap { filename = "c:/landscape.tif" });
```

Inline calls nest to any depth and combine with the other styles. This call computes a column with one functor and feeds it straight into another that adds the column to a table, which is in turn fed into a third functor:

```
spatialIndex := CreateSpatialIndexFor2DPoints (AddTableColumn {
    table = yCoordinateTable,
    columnName = "X_Coordinate",
    columnType = .real,
    columnIndex = 0,
    columnShouldBeKey = .no,
    columnValues = xCoordinateTable,
    defaultValue = .none
});
```

Inlining is convenient only when you need a single output from the nested call. If you need more than one of its outputs, bind it to variables instead.

Setting the `@inline` property on a functor prevents it from being inlined when the script is written. The same effect also applies automatically whenever any other property is defined for the functor — such as a comment, a custom alias, or any other annotation — because an inlined functor carries no separate node to attach that information to, so it would be lost. See [Properties](#properties) for the full list of functor properties.

---

## Container functors

A **container functor** holds other functors and runs them as part of its own execution — see [Containers](Functors-And-Ports.html#containers) for the kinds of containers and [Basic Data Flow](Basic-Data-Flow.html#containers-the-second-ordering-source) for how they affect execution order. In EGO Script, the contained functors are written inside a double-brace block `{{ … }}` that follows the container call:

```
_ := Group .none {{
    attributeTable := ExtractCategoricalMapAttributes landscape regions .yes;
    cellCounts := GetTableFromKey attributeTable [ 9 ];
    countLookup := LookupTable cellCounts;
}};
```

Containers nest to any depth, and like any functor they may carry properties such as a label or color (see [Functor properties](#functor-properties), below). The [calculator functors](#calculator-functor-shorthand) are containers too: each holds the expression it evaluates and, in its verbose form, a block of operand definitions.

A container communicates with its contents through internal ports — [internal output ports](#internal-output-ports) carry values into the block, and [internal input ports](#internal-input-ports) carry values back to the container — and can be ordered against other containers through [sequence ports](#sequence-ports). The subsections below show how each of these is written, followed by the loop idioms built on muxes and junctions. For combining the error-handling containers with junctions and conditional containers, see [Handling Errors](Handling-Errors.html).

Some containers exist to bracket a computation with side effects that happen before and after it — see [Containers](Functors-And-Ports.html#containers). [Print](functors/Print.html) is the clearest example: it prints an `initialMessage` before its contents run and a `finalMessage` after they complete:

```
_ := Print "Beginning execution" "Finished execution" {{
    // Perform some complicated computation that produces a numeric result...
    result := ...;
}};
```

Either message can be omitted with `.none`. If the final message needs to include a value produced by the computation, a nested [Print](functors/Print.html) can be placed at the end of the body. The inner `Print` only runs after `result` is computed, since it depends on it — and [Create String](functors/Create-String.html) with [Number Value](functors/Number-Value.html) is used to embed the computed value in the message string:

```
_ := Print "Beginning execution" .none {{
    // Perform some complicated computation that produces a numeric result...
    result := ...;

    message := CreateString "Finished execution. Result: <v1>" {{
        NumberValue result 1;
    }};
    _ := Print message .none {{ }};
}};
```

Bracketing a computation is not the only way to order a [Print](functors/Print.html). Like other containers, it has a `sequenceInput` and a `sequenceOutput` (see [Sequence ports](#sequence-ports), below), so a message can also be printed after a functor or container that is outside of it, or be placed before one. The ordering is only a constraint: a message connected this way is never printed before the functor it waits for, but other functors may still run between the two. As `sequenceInput` comes after the other optional inputs of `Print`, it is usually bound by name:

```
// Loops over all the ids; loopDone is available only after the loop finishes.
loopDone := ForEach allIds {{
    // ...
}};

// Printed only after the loop has finished.
_ := Print { initialMessage = "Loop finished", sequenceInput = loopDone } {{ }};
```

### Sequence ports

Most containers have a `sequenceInput` and a `sequenceOutput` port that carry no data and only impose execution order. See [Sequence ports](Functors-And-Ports.html#sequence-ports) for how they behave and which containers lack them. Since any output can be connected to a `sequenceInput`, the output of one container can feed directly into the next container's sequencing slot:

```
// ForEachCategory completes before Group starts.
sequenceOut := ForEachCategory finalLandscape .none {{
    // ...
}};
_ := Group sequenceOut {{
    // ...
}};
```

### Internal output ports

An [internal output port](Functors-And-Ports.html#internal-ports) carries a value from the container into the functors nested inside it, such as a loop's current element or a manager object made available to a block.

An internal output port is read at the top of the block with the same `variable = portName` form used for ordinary outputs — your variable on the left, the port name on the right. If present, these bindings **must be the first declarations inside the container block**, before any functor calls. A loop, for example, exposes its current element through an internal output port named `step`:

```
ForEachCategory categorization {{
    // read the internal output port `step`
    currentCategory = step;
    categoryId := Step currentCategory;
    // ...
}};
```

Here `step` is the port the loop provides, and `currentCategory` is the variable that receives it for use inside the block.

The binding is optional in this particular case. [Step](functors/Step.html)'s own input is auto-bound to the enclosing container's `step` port — see [Auto-bound ports](#auto-bound-ports) below — so `categoryId := Step;` on its own would have worked. It is written out here to make the port visible; internal outputs with no such auto-bound consumer, like the one in the next example, always have to be read explicitly.

`RegionManager` provides another example. It creates a region context and exposes it to the functors inside its block through an internal output port:

```
RegionManager regionMap 0 {{
    // read the internal output port `regionManager`
    manager = regionManager;
    allRegions := GetAllRegionsInfo manager;
}};
```

`manager = regionManager;` reads the container's internal output port `regionManager` into the variable `manager`, which [Get All Regions Info](functors/Get-All-Regions-Info.html) then consumes. The name on the right is always the port; the name on the left is your variable.

### Internal input ports

An [internal input port](Functors-And-Ports.html#internal-ports) carries a value the other way: from the functors inside the block back to the container. The condition that decides whether a loop repeats is the clearest example.

A `While` or `DoWhile` loop has an internal input port for its repeat condition. It is fed by placing a [Set While Condition](functors/Set-While-Condition.html) functor inside the loop body — the `condition` output port of `SetWhileCondition` is **auto-bound** (see [Auto-bound ports](#auto-bound-ports) below) to the loop's `condition` internal input, so no explicit connection is needed:

```
_ := DoWhile .none {{
    // ... contained functors compute `keepGoing`, a non-zero value to continue ...
    // condition output auto-binds to the loop
    _ := SetWhileCondition keepGoing;
}};
```

The value set by `SetWhileCondition` during an iteration decides whether the loop runs again: once the iteration finishes, the loop runs its body again if the value is true and stops otherwise. [While](functors/While.html) also tests its `initialCondition` input before the first iteration, so its body may not run at all; [Do While](functors/Do-While.html) has no initial condition and always runs its body at least once.

### Auto-bound ports

An **auto-bound** port needs no binding in the script: when its functor is placed inside a compatible container, the port connects by itself to the container's matching internal port. This is the mechanism behind the two examples above — [Step](functors/Step.html)'s input reads a loop's `step` internal output, and [Set While Condition](functors/Set-While-Condition.html)'s output feeds a loop's `condition` internal input, with nothing written to connect them. See [Auto-bound ports](Functors-And-Ports.html#auto-bound-ports) for the complete list of auto-bound ports and [Internal ports](Functors-And-Ports.html#internal-ports) for the internal ports of every container.

### Carrying and selecting values across iterations

A [mux](Functors-And-Ports.html#muxes-and-junctions) carries a value across the iterations of a loop: on the first iteration it emits its *initial* input, and on every later one its *feedback* input, the value produced by the previous pass. Written at the top of the loop body, with its feedback input bound to a variable assigned further down, it forms the loop's running state. This loop counts from 0 and stops once the counter reaches 10:

```
_ := DoWhile .none {{
    // First pass: 0. Later passes: `nextCount` from the previous pass.
    count := MuxValue 0 nextCount;

    nextCount := $ [ $count + 1 ];

    // A boolean converts to a real (true -> 1, false -> 0), so a value calculator turns a
    // stop test into the numeric flag the loop expects: non-zero continues, zero stops.
    keepGoing := $ [ $nextCount < 10 ];

    _ := SetWhileCondition keepGoing;
}};
```

> **Note:** A mux's feedback input is the one exception to the dependency rule in [Functors, variables, and binding](#functors-variables-and-binding) — the mux does not wait for the functor that produces its feedback value to run before it runs; it emits the value that functor produced on the previous iteration instead. This is also why, in the example above, `nextCount` is passed into `MuxValue` on a line above the line that assigns `nextCount`: the mux and the calculator each depend on the other's output, so no matter which one is written first in the script, the other's variable is necessarily used before it is assigned. [Basic Data Flow](Basic-Data-Flow.html#the-one-exception-feedback-in-loops) explains why this exception is what makes loops schedulable at all, and when a loop's iterations can run in parallel.

A [junction](Functors-And-Ports.html#muxes-and-junctions) selects between two dataflows: it passes its first input through if that input carries data, and its second input otherwise. If both are empty, the junction reports an error:

```
// `primary` if it has data, otherwise `fallback`:
chosen := MapJunction primary fallback;
```

---

## Calculator functor shorthand

A family of **calculator functors** evaluates an expression and returns a result of a given type:

| Functor | Returns |
| --- | --- |
| [Calculate Map](Calculate-Functors.html) | a map |
| [Calculate Categorical Map](Calculate-Functors.html) | a categorical map |
| [Calculate Multiple Maps](Calculate-Functors.html)[^8150] | a struct with one map for each field of a [struct expression](Calculate-Functors.html#struct-expressions) |
| [Calculate Lookup Table Values](Calculate-Functors.html) | a lookup table (keys taken from a base table; values computed) |
| [Calculate Lookup Table Keys And Values](Calculate-Functors.html) | a lookup table (both keys and values computed) |
| [Calculate Value](Calculate-Functors.html) | a single value |

> **See also:** This section covers only the EGO Script syntax used to call these functors. For the full semantics of each one — inputs, parameters, the expression language, and null handling — see [Calculate Functors — Complete Operator Documentation](Calculate-Functors.html).

Each of these functors can be written in two syntactic forms: the **verbose form**, which uses the functor's full name and explicit **hook** functors to connect data, or the **abbreviated syntax** (also called **shorthand**), which replaces the functor name with a compact symbol and references operands directly by variable name. The abbreviated symbol for each functor is:

| Shorthand | Functor |
| --- | --- |
| `#` | `CalculateMap` |
| `##` | `CalculateCategoricalMap` |
| `#*`[^8150] | `CalculateMultipleMaps` |
| `%` | `CalculateLookupTableValues` |
| `%%` | `CalculateLookupTableKeysAndValues` |
| `$` | `CalculateValue` |

> **Note:** The shorthand is the symbol alone — the `[ … ]` that usually appears next is simply the functor's first argument (the expression to evaluate), not part of the symbol itself. Whatever follows the bracket (`.int8 .default .no .none`, or a base table and column names) are the functor's remaining inputs, supplied in positional order.

### Verbose form

In the verbose form, data is connected through **hook** functors — [Number Map](functors/Number-Map.html), [Number Table](functors/Number-Table.html), and [Number Value](functors/Number-Value.html) — which supply maps, tables, and scalar values to the expression respectively. Each hook is assigned a number, and the expression references it by a type-specific numbered prefix: `i1`, `i2`… for maps; `t1`, `t2`… for tables and lookup tables; `v1`, `v2`… for values. Each type is numbered independently:

```
proximityMap := CalculateCategoricalMap {
    expression = [
        if t1[?i1] then 1 else null
    ],
    cellType = .int8,
    nullValue = .default,
    resultIsSparse = .no,
    resultFormat = .none
} {{
    // i1
    NumberMap   regions      1;
    // t1
    NumberTable regionCounts 1;
}};
```

The following uses two table hooks and two value hooks at once, keeping every top whose height and slope both clear a threshold:

```
hilltops := CalculateLookupTableValues [
    if t1[line] >= v1 and t2[line] >= v2 then 1 else null
] "Top_Id" "Is_Hilltop" .none {{
    // t1
    NumberTable saddleHeights     1;
    // t2
    NumberTable saddleAngles      2;
    // v1
    NumberValue minimumHeight     1;
    // v2
    NumberValue minimumSlopeAngle 2;
}};
```

### Abbreviated syntax

In the abbreviated syntax, the hook block is omitted entirely. The expression references connected data directly by variable name, prefixed by a sigil that identifies the type:

| Type | Sigil | Named form | Verbose equivalent |
| --- | --- | --- | --- |
| map | `#` | `#regions` | `i1`, `i2`, … |
| table or lookup table | `%` | `%regionCounts` | `t1`, `t2`, … |
| value | `$` | `$radius` | `v1`, `v2`, … |

The same two calculations from the verbose section above, written in abbreviated syntax:

```
proximityMap := ## [
    if %regionCounts[?#regions] then 1 else null
] .int8 .default .no .none;
```

From version 8.15.0, the `resultIsSparse` port of Calculate Map, Calculate Categorical Map and Calculate Multiple Maps is replaced by `resultSparsity`, whose values are `.dense`, `.sparse` and `.auto`, the default. In the examples above, `resultIsSparse = .no` and `.no` are then written as `resultSparsity = .auto` and `.auto`. Scripts created with earlier versions keep working: `.no` is read as `.dense` and `.yes` as `.sparse`.[^8150]

```
hilltops := % [
    if %saddleHeights[line] >= $minimumHeight and %saddleAngles[line] >= $minimumSlopeAngle then 1 else null
] "Top_Id" "Is_Hilltop" .none;
```

The operands are named directly and the hook block disappears entirely. A lookup by key is written `%table[key]`; `?` tests whether a key is present, as in `%regionCounts[?#regions]`.

### Conversion between forms

Converting abbreviated syntax to verbose is always lossless. Converting verbose to abbreviated is only possible when all hooks are free of comments, properties, and identifiers that do not appear in the expression.

> **Note:** This distinction applies only to saved or generated script text. The graphical interface always displays and edits a calculator functor's expression in the verbose `i1`/`t1`/`v1` form, with each hook represented as its own functor node, regardless of whether the *Use abbreviated syntax* option is enabled or which form the underlying file uses. The `#name`/`%name`/`$name` abbreviated form exists only in script text; the graphical interface has no corresponding abbreviated representation.

A common situation where this matters: if you connect a map or lookup table purely to define the output format — not because it is referenced in the expression — connecting it via a `NumberMap` or `NumberTable` hook will block abbreviated syntax, since the hook defines an identifier absent from the expression. Use the dedicated port instead: the `Result Format` input port for map calculators, or the `Base Lookup Table` input port for lookup table calculators. These connections do not create hooks and do not affect the availability of abbreviated syntax.

> **Note:** This constraint applies specifically when the GUI saves a script or generates a fragment in abbreviated syntax. When writing a script by hand in a text editor, the situation does not arise — you simply write the appropriate form directly.

> **Tip:** You can control which form Dinamica EGO uses when saving a script via the *Use abbreviated syntax for Calculate family functors* option, found under *Tools* → *Options* \| *EGO Script* — see [Script generation options](#script-generation-options) for the full list of generation options.

### The two lookup-table calculators

`CalculateLookupTableValues` (`%`) computes only the **values** of a lookup table; the keys are taken from a base table supplied as an argument. The example below marks each row whose key equals its own value:

```
// Shorthand
dominantTops := % [
    if %dominanceLookup[line] = line then 1 else null
] "Top_Id" "Is_Dominant" dominanceLookup;

// Verbose equivalent
dominantTops := CalculateLookupTableValues [
    if t1[line] = line then 1 else null
] "Top_Id" "Is_Dominant" dominanceLookup {{
    // t1
    NumberTable dominanceLookup 1;
}};
```

`CalculateLookupTableKeysAndValues` (`%%`) computes **both** the keys and the values, using a separate expression for each. In the verbose form the two expressions are the functor's first two positional arguments:

```
// Shorthand
nearestDistances := %% {
    keyColumnExpression   = [ %nearestPoints[[line]["Point_Id"]] ],
    valueColumnExpression = [ %nearestPoints[[line]["Nearest_Distance"]] ],
    keyColumnName   = "Point_Id",
    valueColumnName = "Nearest_Distance",
    baseLookupTable = pointKeys
};

// Verbose equivalent
nearestDistances := CalculateLookupTableKeysAndValues [
    t1[[line]["Point_Id"]]
] [
    t1[[line]["Nearest_Distance"]]
] "Point_Id" "Nearest_Distance" pointKeys {{
    // t1
    NumberTable nearestPoints 1;
}};
```

### Side-by-side comparison

The following example illustrates how the two forms look on a realistic expression involving multiple map operands, a value operand, a neighbourhood function, and the `?` error-catch operator.

**Verbose form:**

```
// Restore the noisy cells marked for restoration. The replacement value is
// derived from a window that grows with the current time step.
updatedRestoredImage := CalculateMap [
    if i1 = 2 then
        nbMedian(i2, v1, v1) ? i3
    else
        i3
] cellType nullValue .no .none {{
    NumberMap  arePixelsOriginalOrNoisyWithCategories 1;
    NumberMap  originalPixelsOnlyInRestoredImage     2;
    NumberMap  currentRestoredImage                  3;
    NumberValue lK                                   1;
}};
```

**Shorthand form:**

```
// Restore the noisy cells marked for restoration. The replacement value is
// derived from a window that grows with the current time step.
updatedRestoredImage := # [
    if #arePixelsOriginalOrNoisyWithCategories = 2 then
        nbMedian(#originalPixelsOnlyInRestoredImage, $lK, $lK) ? #currentRestoredImage
    else
        #currentRestoredImage
] cellType nullValue .no .none;
```

In the verbose form the three maps arrive as `i1`, `i2`, `i3` and the value as `v1`, each supplied by a hook in the trailing block. In the abbreviated form the same operands are referenced directly by their variable names — `#arePixelsOriginalOrNoisyWithCategories`, `#originalPixelsOnlyInRestoredImage`, `#currentRestoredImage`, and `$lK` — with the trailing block omitted entirely.

---

## Comments

A single-line comment begins with `//` and runs to the end of the line:

```
// This is a single-line comment.
```

A multi-line comment is surrounded by `/*` and `*/`:

```
/* This is a multi-line
comment */
```

The two styles differ in one important way:

> **Note:** Multi-line comments are not preserved when a model is opened in the graphical interface, but single-line comments are. Because of this, a multi-line comment is usually better written as consecutive `//` lines:

```
// This is a multi-line
// comment
```

A comment placed immediately before a functor becomes that functor's `comment` property (see [Properties](#properties)). A comment placed before the `Script` keyword becomes the model's title (`metadata.title`).

### Brief and extended comments

When a `//` comment is parsed, the line `===` splits it into two separate properties: the text before `===` becomes the functor's `comment` (the brief comment), and the text after it becomes its `extendedcomment` (the extended comment):

```
// Generate the initial seed.
//
// ===
// Living cells are represented by 1 and dead cells by 0.
```

Here `Generate the initial seed.` is stored as the `comment` property and `Living cells are represented by 1 and dead cells by 0.` as the `extendedcomment` property. In the graphical interface, the `comment` is displayed directly on the functor's visual node; the `extendedcomment` appears only in the tooltip shown when hovering over the node.

---

## Properties

A **property** annotates a functor (or the model as a whole) with metadata. Properties do not change what a model computes; they affect how it is labeled, displayed, and organized in the visual editor, and they carry documentation.

A property is written immediately before the functor it applies to. There are two equivalent syntaxes — the `@` form and the comment form:

```
@name = value
```

```
/** name = value */
```

A property name must start with a letter or `_`, followed by letters, `_`, and `.`. A value may contain any characters, including blanks; a value that spans line breaks must be surrounded by double quotes. If the value itself contains a double-quote character, it must be escaped as `\"`:

```
@alias = Largest Patch Area
@collapsed = yes
@notes = "The model input is a map where the non-null values identify the patches.

The output is a table containing the largest patch index per category."
@description = "The input map must have values in the range [0, 1].
Use \"null\" to mark cells that should be excluded from the analysis."
```

Internally each property has a fully qualified name (such as `dff.functor.alias`), but many are read and written in a **short form** that drops the qualified prefix. Writing the `@shortName = value` form forces the short name to expand to its full property name.

### Functor properties

The per-functor properties you will see most often are:

| Short form | Qualified name | Effect |
| --- | --- | --- |
| `alias` | `dff.functor.alias` | A human-readable name shown for the functor in the GUI in place of its variable name. When saving, the alias is used to derive the variable name. When loading, the variable name is used to reconstruct the alias. See [Alias and variable name conversion](#alias-and-variable-name-conversion) below. |
| `color` | `dff.functor.color` | A background color for the functor's node, as a hex code such as `#ccffcc`. Useful to visually differentiate or group related functors and groups. |
| `inline` | `dff.functor.inline` | When set, prevents the functor from being inlined when the script is written. Any other property defined on the functor (a comment, alias, etc.) has the same effect automatically, since an inlined functor has no separate node to preserve that information. Values: `yes`/`no` or `true`/`false`. |
| `comment` | `dff.functor.comment` | The functor's brief comment — the text before `===` in a `//` comment (see [Comments](#comments)). |
| `extendedcomment` | `dff.functor.extendedcomment` | The functor's extended comment — the text after `===` in a `//` comment (see [Comments](#comments)). |
| `collapsed` | `dff.container.collapsed` | Indicates that a container is drawn closed (its contents hidden) in the graphical interface. Applies to containers only. Values: `yes`/`no` or `true`/`false`. |
| `ignoredIssues` | `dff.functor.ignoredissues` | Suppresses a specific category of GUI warning for the functor — observed values include `Experimental` (the functor is experimental) and `ResultIgnored` (an output is intentionally left unused). |

> **Note:** A few per-functor properties exist only while a model is open in the editor and are never written to the saved model: `dff.functor.text`, `dff.functor.file`, `dff.functor.line`, and `dff.functor.column`.

### Light enum

A **light enum** turns an integer-valued port into a named dropdown in the GUI, replacing the free-form numeric field with a set of labelled choices. The underlying value stored and passed is still an integer; the dropdown is a presentation layer only.

Any port belonging to the integer family of types (`IntegerValue`, `NonNegativeIntegerValue`, `PositiveIntegerValue`) can be annotated as a light enum, in any model — not just submodels. The annotation applies to carrier functors of those types that expose an editor.

The annotation is written immediately before the carrier functor using the `@lightenum.<portName>` property, where `<portName>` is the actual name of the port being annotated. The value is a JSON object with two fields:

- `enabled` — `true` to activate the dropdown, `false` to disable it.
- `values` — a mapping from integer values (as quoted strings) to human-readable labels.

```
@lightenum.constant = {"enabled":true,"values":{"1":"Mean","2":"Median","3":"Bounding Box"}}
centroidType := PositiveIntegerValue 1;
```

Here the GUI presents a dropdown with options "Mean", "Median", and "Bounding Box" instead of a numeric field. Selecting "Mean" passes the value `1` to any functor that receives `centroidType`; selecting "Bounding Box" passes `3`.

For its use alongside submodel port declarations, see [Submodels](#submodels).

### Alias and variable name conversion

The GUI and the script use two directions of conversion between an alias and a variable name.

**Saving (alias → variable name):** When the GUI writes a script, it derives the variable name from the alias by splitting the alias into words — using spaces, underscores, and lowercase-to-uppercase transitions (CamelCase) as word boundaries — then recombining them as a valid identifier. Leading and trailing spaces or underscores are ignored. Non-alphanumeric characters other than underscores are ignored entirely. The result starts with a lowercase letter.

| Alias | Variable name |
| --- | --- |
| `Initial Landscape` | `initialLandscape` |
| `initial_landscape` | `initialLandscape` |
| `Deforestation Rate (%/yr)` | `deforestationRateYr` |
| `WOfE Probability Map` | `wOfEProbabilityMap` |
| `_Slope_` | `slope` |

If two or more functors produce the same variable name from their aliases, a number is appended to disambiguate: the first functor keeps the base name, subsequent ones become `name2`, `name3`, and so on.

If the conversion alias → variable → alias does not round-trip back to the same original alias — for example because non-alphanumeric characters were discarded — the GUI explicitly writes the `@alias` property in the saved script to preserve the original alias without loss of information. In such cases you will see an explicit `@alias = ...` annotation even though the functor's variable name is present.

**Loading (variable name → alias):** When a script is read back into the GUI and a functor has no explicit `@alias` property, the alias is reconstructed from the variable name using the following rules:

- The first letter is converted to uppercase.
- A space is inserted at every lowercase-to-uppercase transition.
- A space is inserted at every letter-to-digit and digit-to-letter transition.
- Sequences of consecutive uppercase letters are treated as a single word — no space is inserted within them.
- Leading and trailing underscores are discarded.
- Internal underscores (and sequences of multiple underscores) are converted to a single space.

| Variable name | Reconstructed alias |
| --- | --- |
| `initialLandscape` | `Initial Landscape` |
| `distance_to_deforested` | `Distance To Deforested` |
| `calcURL` | `Calc URL` |
| `map2Region` | `Map 2 Region` |
| `saddleHeight2` | `Saddle Height 2` |

One case is excluded from this reconstruction: a variable name that is just the functor's own name, lowercased at the front, with a trailing number — for example `lookupTable0` for a `LookupTable` functor. This pattern is recognized as an **auto-generated name**: one the GUI assigned on its own because no alias was ever set, rather than a name a person chose. Such names are not reconstructed into an alias like `Lookup Table 0`; the functor is simply shown with no alias.

### Model-level metadata

A separate group of properties describes the model as a whole rather than any single functor. These also use a short form, dropping the `metadata.` (or `dff.`) prefix:

| Short form | Qualified name | Describes |
| --- | --- | --- |
| `charset` | `dff.charset` | The character encoding of the script file (e.g. `UTF-8`). |
| `title` | `metadata.title` | The model's title. |
| `author` | `metadata.author` | The model's author. |
| `organization` | `metadata.organization` | The author's organization. |
| `description` | `metadata.description` | A description of what the model does. |
| `keywords` | `metadata.keywords` | Search keywords for the model. |
| `notes` | `metadata.notes` | Free-form notes about the model. |
| `showproperties` | `metadata.showproperties` | Whether the property window opens when the model is opened. Values: `yes`/`no` or `true`/`false`. |
| `metaversion` | `metadata.version` | The model's metadata version. |
| `date` | `dff.date` | The date the model was last written. |
| `version` | `dff.version` | The version of Dinamica EGO that last updated the model. |

> **Note:** `description` is **model-level** metadata; it is not a property of an individual functor.

Submodels expose their own inputs and outputs to callers through a further set of properties, such as `@submodel.in.constant.name` and `@submodel.out.result.name`. These are described in the [Submodels](#submodels) section below.

---

## Submodels

A [submodel](Submodels.html) is an EGO Script file that exposes some of its functor ports as named inputs and outputs, so it can be used as a self-contained, reusable functor in other models. From a scripting perspective, what makes a file a submodel is a set of model-level and functor-level properties that declare its interface. For information about submodel types, storage, the GUI workflow, and the Submodel Store, see [Submodels](Submodels.html).

### Submodel identity properties

| Property | Description | Example |
| --- | --- | --- |
| `@submodel.name` | The functor name of the submodel — this is effectively the name of the new functor that other models and submodels can use. It also appears as the display name in the functor library. | `AbortConditionally` |
| `@submodel.description` | Documentation for the submodel. | `Aborts the execution conditionally and prints a message before terminating the model.` |
| `@submodel.group` | Functor library group path, using `:` as a hierarchy separator. | `Elevation Graph:Utilities` |
| `@submodel.documentation` | URL where the submodel's documentation can be found. | `https://example.com/docs/my-submodel` |
| `@submodel.largeicon` | Base64-encoded large icon (32×32 px) displayed in the functor library. | *base64 string* |
| `@submodel.smallicon` | Base64-encoded small icon (16×16 px) displayed in the functor library. | *base64 string* |

These describe the submodel's own identity. A script that instead **calls** an external submodel it may not be able to resolve uses `@submodel.import` — see [Importing an external submodel interface](#importing-an-external-submodel-interface) below. The two aren't mutually exclusive: a submodel definition that itself calls other submodels can carry both, declaring its own identity with these properties while also declaring `@submodel.import` for whichever of those calls it can't guarantee will resolve.

### Declaring input ports

A submodel input port is declared by placing `@submodel.in.<portName>.*` properties before the functor whose port is being exported. The `<portName>` part of the key is the **actual name of that functor's input port**. The `@submodel.in.<portName>.name` sub-property defines the port's name in the submodel interface. Any functor port can be exported as a submodel input, and multiple port declarations can precede a single functor.

| Property | Description | Example |
| --- | --- | --- |
| `@submodel.in.<portName>.name` | The port name in the submodel interface. | `shouldAbort` |
| `@submodel.in.<portName>.description` | Documentation for the port. | `If true, aborts the model execution.` |
| `@submodel.in.<portName>.optional` | Whether the caller must supply a value, or may leave it to fall back to whatever value is already configured on the port inside the submodel. | `yes` or `no` |
| `@submodel.in.<portName>.order` | Position of the port in the resulting submodel's interface. | `1` |
| `@submodel.in.<portName>.advanced` | Whether the port is hidden under an "Advanced" section in the GUI. | `yes` or `no` |
| `@submodel.in.<portName>.group` | Places the port in a named tab in the GUI functor editor. Ports sharing the same group name appear together in the same tab. A numeric prefix of the form `N -` (e.g. `1 - Patches`, `4 - Hilltop Criteria`) controls the tab's position — the prefix is stripped from the displayed tab name, so `1 - Patches` creates a tab named *Patches* that appears first. If no group is specified, the port appears in the default *General* tab; ports marked `advanced = yes` appear in the *Advanced* tab. | `2 - Hilltop Clustering` |

> **Note:** A submodel input port can never be declared nullable, even if the underlying functor port itself is nullable. Marking it `optional = yes` only means the caller may omit an explicit value and let the port fall back to whatever is already configured on it inside the submodel — the port always ends up with some value, never none.

Integer-valued ports can also be annotated with `@lightenum` to present them as a named dropdown in the GUI — see [Light enum](#light-enum) for details. The annotation is placed before the `@submodel.in.*` block:

```
@lightenum.constant = {"enabled":true,"values":{"1":"Mean","2":"Median","3":"Bounding Box"}}
@submodel.in.constant.advanced = no
@submodel.in.constant.description = Integer value identifying the type of centroid to calculate.
@submodel.in.constant.name = centroidType
@submodel.in.constant.optional = yes
@submodel.in.constant.order = 2
centroidType := PositiveIntegerValue 1;
```

The example below declares two required inputs. Both use `@submodel.in.constant.*` as the key because the functors `BooleanValue` and `String` each have a single input port named `constant`:

```
@submodel.in.constant.advanced = no
@submodel.in.constant.description = If true, aborts the model execution.
@submodel.in.constant.name = shouldAbort
@submodel.in.constant.optional = no
@submodel.in.constant.order = 1
shouldAbort := BooleanValue .UNBOUND;

@submodel.in.constant.advanced = no
@submodel.in.constant.description = Message displayed before aborting the model.
@submodel.in.constant.name = errorMessage
@submodel.in.constant.optional = no
@submodel.in.constant.order = 2
errorMessage := String .UNBOUND;
```

Optional inputs carry their default value directly instead of `.UNBOUND`. The following declares an optional, advanced input with a string default:

```
@submodel.in.constant.advanced = yes
@submodel.in.constant.description = Message used to report an invalid value.
@submodel.in.constant.name = errorMessageFormat
@submodel.in.constant.optional = yes
@submodel.in.constant.order = 3
errorMessageFormat := String $"(The value <v1> is not valid.)";
```

### Declaring output ports

Output ports follow the same pattern as inputs. `@submodel.out.<portName>.*` properties are placed before the functor whose output is being exported, where `<portName>` is the actual name of that functor's output port.

| Property | Description | Example |
| --- | --- | --- |
| `@submodel.out.<portName>.name` | The port name in the submodel interface. | `returnedValue` |
| `@submodel.out.<portName>.description` | Documentation for the port. | `Always returns true if the validation succeeds.` |
| `@submodel.out.<portName>.order` | Position of the port in the resulting submodel's interface. | `1` |

The `BooleanValue` functor has an output port named `object`. The following exports it as `returnedValue`:

```
@submodel.out.object.description = Always returns true if the validation succeeds.
@submodel.out.object.name = returnedValue
@submodel.out.object.order = 1
_ := BooleanValue .yes;
```

### Complete example

The two submodels below illustrate both concepts together. `AbortConditionally` is a simple submodel with two inputs and no outputs. `ValidateInputValue` has three inputs (one optional and advanced), one output, and calls `AbortConditionally` internally.

**AbortConditionally:**

```
@charset = UTF-8
@submodel.name = AbortConditionally
@submodel.description = Aborts the execution conditionally and prints a message before terminating the model.
@submodel.group = Control
Script {{
    @submodel.in.constant.advanced = no
    @submodel.in.constant.description = If true, aborts the model execution.
    @submodel.in.constant.name = shouldAbort
    @submodel.in.constant.optional = no
    @submodel.in.constant.order = 1
    shouldAbort := BooleanValue .UNBOUND;

    @submodel.in.constant.advanced = no
    @submodel.in.constant.description = Message displayed before aborting the model.
    @submodel.in.constant.name = errorMessage
    @submodel.in.constant.optional = no
    @submodel.in.constant.order = 2
    errorMessage := String .UNBOUND;

    // ...
}};
```

The resulting `AbortConditionally` functor exposes:

**Inputs:**

| Order | Name | Type | Required | Default | Advanced | Description |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `shouldAbort` | BooleanValue | Yes | — | No | If true, aborts the model execution. |
| 2 | `errorMessage` | String | Yes | — | No | Message displayed before aborting the model. |

**ValidateInputValue** (calls `AbortConditionally` internally):

```
@charset = UTF-8
@submodel.name = ValidateInputValue
@submodel.description = Validate a numeric value using a custom expression. The execution will be aborted if the given value is not valid according to the given expression.
@submodel.group = Development
Script {{
    @submodel.in.constant.advanced = no
    @submodel.in.constant.description = Value that will be validated.
    @submodel.in.constant.name = inputValue
    @submodel.in.constant.optional = no
    @submodel.in.constant.order = 1
    inputValue := RealValue .UNBOUND;

    @submodel.in.constant.advanced = no
    @submodel.in.constant.description = Expression used to validate the input value. The input value should be mentioned in the expression as "v1". The given expression must return zero if the value is valid, and non-zero if the value is invalid.
    @submodel.in.constant.name = validationExpression
    @submodel.in.constant.optional = no
    @submodel.in.constant.order = 2
    validationExpression := ImageExpression .UNBOUND;

    @submodel.in.constant.advanced = yes
    @submodel.in.constant.description = Message used to report an invalid value. The invalid value can be mentioned using the tag <v1>.
    @submodel.in.constant.name = errorMessageFormat
    @submodel.in.constant.optional = yes
    @submodel.in.constant.order = 3
    errorMessageFormat := String $"(The value <v1> is not valid.)";

    // ...

    // ValidateInputValue calls AbortConditionally as part of its implementation.
    AbortConditionally isValueValid completeErrorMessage;

    @submodel.out.object.description = Always returns true if the validation succeeds. This value can be used to chain validation with subsequent functors.
    @submodel.out.object.name = returnedValue
    @submodel.out.object.order = 1
    _ := BooleanValue .yes;
}};
```

The resulting `ValidateInputValue` functor exposes:

**Inputs:**

| Order | Name | Type | Required | Default | Advanced | Description |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | `inputValue` | RealValue | Yes | — | No | Value that will be validated. |
| 2 | `validationExpression` | ImageExpression | Yes | — | No | Expression used to validate the input value. The input value should be mentioned as `v1`. Must return zero if valid, non-zero if invalid. |
| 3 | `errorMessageFormat` | String | No | `$"(The value <v1> is not valid.)"` | Yes | Message used to report an invalid value. The value can be mentioned using the tag `<v1>`. |

**Outputs:**

| Order | Name | Description |
| --- | --- | --- |
| 1 | `returnedValue` | Always returns true if the validation succeeds. Can be used to chain validation with subsequent functors. |

### Calling a submodel

Once defined, a submodel is called exactly like any other functor. Outputs are bound left to right in port order; inputs are supplied positionally in port order. The following call validates that a projection type value equals 2, providing a custom error message as the optional third input:

```
_ := ValidateInputValue projectionType [ v1 = 2 ] $"(An elevation map with geographic projections cannot be used.)";
```

The optional `errorMessageFormat` port is supplied explicitly here. It could be omitted, in which case the default `$"(The value <v1> is not valid.)"` would be used instead.

### File location

It is conventional to name the submodel file after its `@submodel.name` value with a `.ego` extension, but what matters is the value of that property, not the filename. Where the file is placed determines whether it becomes a local or user submodel:

- **Local submodel** — place the file in the `<modelfile>_ego_Submodels` folder next to the main model file.
- **User submodel** — place the file in the user submodel folder:
  - **Windows:** `C:\Users\<User>\Documents\Dinamica EGO <version>\Submodels\`
  - **Linux:** `/home/<User>/Dinamica EGO <version>/Submodels/`

See [Submodels](Submodels.html) for full details on submodel types, storage paths, and the Submodel Store.

### Importing an external submodel interface

A script that calls a submodel normally resolves the call by locating and loading the submodel's actual implementation, following [File location](#file-location) above. The `@submodel.import` property handles the case where that resolution fails — the submodel isn't installed, or isn't present alongside the script being opened. This applies equally to a plain model and to a submodel definition — `ValidateInputValue` in the [Complete example](#complete-example) above calls `AbortConditionally` internally, and could carry `@submodel.import = AbortConditionally { ... }` if `AbortConditionally` weren't guaranteed to be resolvable wherever `ValidateInputValue` is opened. The property always names the external submodel being called — never the script's own submodel, if it is one; `ValidateInputValue` would not declare itself this way.

The property is written once, model-level: the called submodel's functor name, followed by three bracketed groups giving its required inputs, its optional inputs, and its outputs, each a comma-separated list of `"portName": TypeName` pairs:

```
@submodel.import = CreateElevationGraphPatchesAndProperties { { "elevationMap": Map, "verticalResolution": PositiveIntegerValue } { "onlyOrthogonalNeighborsAreAllowed": BooleanValue } { "elevationNeighborhoodTable": NeighborhoodTable, "elevationGraphProperties": Table, "discretizedElevationMap": Map, "uniqueDiscretizedPatchMap": CategoricalMap } }
```

When a script calls more than one submodel it may need to import this way, every declaration is packed into the same property, one submodel per semicolon-separated group:

```
@submodel.import = CreateAndFilterElevationGraph { { "elevationPatchNeighborhoodTable": NeighborhoodTable, "elevationPatchProperties": Table } { "minimumElevationPatchSize": RealValue, "maximumElevationPatchSize": RealValue } { "elevationGraph": ElevationGraph } }; IdentifyHilltops { { "elevationGraph": ElevationGraph, "maximumHilltopDistance": RealValue, "minimumHilltopToSaddleHeight": RealValue, "minimumHilltopToSaddleSlopeAngle": RealValue, "hilltopFraction": Percent, "maximumHilltopClusteringDistance": RealValue } { "printInfo": BooleanValue, "maximumNodes": NonNegativeIntegerValue } { "hillTopAnalysis": Table, "hilltopRationale": LookupTable } }
```

When the real submodel can't be resolved, the parser falls back to this declaration and constructs a **hollow functor**: a shell with the declared ports, but no implementation behind them. This is what lets the model load at all despite the missing piece — every connection, type, and the overall graph structure still check out, even though nothing is actually there to execute.

> **Caution:** A hollow functor is a provisional placeholder, not a stable state. A model can't be run while it contains one, since there's nothing behind it to execute — and it can't be saved in that state either. The real submodel implementation has to be resolved and substituted back in first, by making it locatable again (installing it, or placing it alongside the script per [File location](#file-location) above).

This property describes the underlying model graph, not something specific to one notation — it works identically whether the model is written as EGO Script or [EGOML Script](EGOML-Script.html).

## Script generation options

When the GUI saves a script or generates an EGO Script fragment, a set of options controls how the output is formatted. These are found under *Tools* → *Options* \| *EGO Script*:

| Option | Description |
| --- | --- |
| **Minimum number of functor inputs to use named parameters** | Below this threshold, inputs are written in positional syntax; at or above it, nominal (named parameter) syntax is used instead. |
| **Inline any suitable functor** | When enabled, eligible functors are written inline rather than as separate named definitions. |
| ↳ **Inline suitable functors using named parameters** | When enabled, functors are eligible for inlining even if their inputs would be written using nominal syntax. |
| ↳ **Also inline: Suitable containers** | Extends inlining to container functors that qualify. |
| ↳ **Also inline: Suitable muxes** | Extends inlining to mux functors that qualify. |
| ↳ **Also inline: Suitable functors bound to feedback inputs** | Extends inlining to functors whose output feeds back into a loop's mux. |
| **Use abbreviated syntax for Calculate family functors** | Whether the `Calculate` family is written using the shorthand symbol (`#`, `##`, `#*`, `%`, etc.) or the full functor name. See the [Calculator functor shorthand](#calculator-functor-shorthand) section for details. |
| **Preferred number of columns before wrapping comments** | The line width at which the generator wraps long comment text. |

[^8150]: Available in Dinamica EGO 8.15.0, currently a development version. Details may change before release.

{% endraw %}
