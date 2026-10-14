---
title: "None Type"
nav_exclude: true
---
{% raw %}
# None Type

None Type is not a data type in the ordinary sense — it holds no value at all. Its sole purpose is to let one functor force another to run before or after it, without exchanging any actual data between them. This is what backs the `sequenceInput`/`sequenceOutput` ports exposed by most container functors ([Group](Group.html), [While](While.html), [Do While](Do-While.html), [If Then](If-Then.html), [If Not Then](If-Not-Then.html), and others): connecting an output to a `sequenceInput` creates a dependency in the execution graph — forcing the producing functor to complete first — without the connected value itself ever being used. See [Sequence ports](EGO-Script.html#sequence-ports) on the EGO Script page for the general mechanism this type exists to support.

Because a None Type port only cares that something is connected, not what, almost every other type in the system registers an automatic conversion to it — any output, of any type, can be wired directly into a `sequenceInput`/`sequenceOutput` slot. See [Automatic Conversions](#automatic-conversions) below for the complete list.

## GUI Editor

None Type has no editor. A `sequenceInput` port left unconnected is simply empty (written as `.none` — see [EGO Script](EGO-Script.html) below) rather than holding any value of its own; there is nothing to type in or select.

## EGO Script

None Type has no literal constant syntax, since it holds no value to write — see [Constants](EGO-Script.html#constants). Leaving a `sequenceInput` port disconnected is written as `.none`, the same empty-value marker used for any other nullable, unconnected port; it does not construct a None Type value, it simply states that no sequencing dependency is being imposed:

```
// ForEachCategory completes before Group starts.
sequenceOut := ForEachCategory finalLandscape .none {{
    // ...
}};
_ := Group sequenceOut {{
    // ...
}};
```

## Automatic Conversions

- **Converted from**: nearly every other type in the system — [Connection Info Type](Connection-Info-Type.html), [Boolean Value Type](Boolean-Value-Type.html), [Code Type](Code-Type.html), [Date Type](Date-Type.html), [Enum Type](Enum-Type.html), [Folder Type](Folder-Type.html), [Generic Filename Type](Generic-Filename-Type.html), [Image Expression Type](Image-Expression-Type.html), [Index Or Name Type](Index-Or-Name-Type.html), [Int Set Type](Int-Set-Type.html), [Integer Value Type](Integer-Value-Type.html), [Log Tag Type](Log-Tag-Type.html), [Name Type](Name-Type.html), [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html), [Null Value Type](Null-Value-Type.html), [Percent Type](Percent-Type.html), [Positive Integer Value Type](Positive-Integer-Value-Type.html), [Real Value Type](Real-Value-Type.html), [String Type](String-Type.html), [Struct Type](Struct-Type.html), [Workdir Type](Workdir-Type.html), [Categorical Map Type](Categorical-Map-Type.html), [Categorization Type](Categorization-Type.html), [Cell Type](Cell-Type.html), [Kml Type](Kml-Type.html), [Kml Timeline Type](Kml-Timeline-Type.html), [Kmz Filename Type](Kmz-Filename-Type.html), [Map Type](Map-Type.html), [Map Filename Type](Map-Filename-Type.html), [Projection Type](Projection-Type.html), [Weights Of Evidence Skeleton Type](Weights-Of-Evidence-Skeleton-Type.html), [Change Matrix Type](Change-Matrix-Type.html), [Neighborhood Table Type](Neighborhood-Table-Type.html), [Percent Matrix Type](Percent-Matrix-Type.html), [Transition Function Parameter Matrix Type](Transition-Function-Parameter-Matrix-Type.html), [Transition Matrix Type](Transition-Matrix-Type.html), [Transition Set Type](Transition-Set-Type.html), [Weights Type](Weights-Type.html), [Weights Filename Type](Weights-Filename-Type.html), [Elevation Graph Type](Elevation-Graph-Type.html), [Region Manager Type](Region-Manager-Type.html), [Base Table Type](Base-Table-Type.html), [Lookup Table Type](Lookup-Table-Type.html), [Lookup Table Filename Type](Lookup-Table-Filename-Type.html), [Lookup Table Group Type](Lookup-Table-Group-Type.html), [Table Filename Type](Table-Filename-Type.html), [Table Type](Table-Type.html), [Table Manager Type](Table-Manager-Type.html), [Table Value Type](Table-Value-Type.html), and [Tuple Type](Tuple-Type.html). In every case, the conversion discards the source value entirely — only the fact that a value existed, and when it became available, is preserved.
- **Converted to**: None.

See [Type System](Type-System.html#sequencing) for the complete, authoritative list this section is drawn from, and for the wider conversion reference across all types.
{% endraw %}
