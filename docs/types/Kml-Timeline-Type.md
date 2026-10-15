---
title: "Kml Timeline Type"
nav_order: 49
parent: "Type System"
grand_parent: "Core Concepts"
---
{% raw %}
# Kml Timeline Type

A **Kml Timeline** represents an ordered, time-stamped sequence of [Kml](Kml-Type.html) overlays, assembled into a single animated display for Google Earth: each entry can carry a `beginTime`/`endTime` pair so that Google Earth shows and hides it as the timeline plays through those dates.

A Kml Timeline is built entirely through repeated calls to [Set Kml Timeline](../functors/Set-Kml-Timeline.html): each call inserts one Kml entry, either starting a fresh timeline (when its `kmlTimeline` input is left at its default of `.none`) or appending to an existing one. [Mux Kml Timeline](../functors/Mux-Kml-Timeline.html) carries the growing timeline across the iterations of a loop, the same role [Mux Map](../functors/Mux-Map.html) and [Mux Lookup Table](../functors/Mux-Lookup-Table.html) play for their own types -- though since Kml Timeline has no generic carrier functor (unlike [Kml](Kml-Type.html) or [Map](Map-Type.html)), the `initial` value fed into it must itself come from a [Set Kml Timeline](../functors/Set-Kml-Timeline.html) call made before the loop starts. Nothing else in the functor catalog consumes a Kml Timeline: notably, [Save Compressed Kml](../functors/Save-Compressed-Kml.html) accepts only a plain [Kml](Kml-Type.html), and no automatic conversion is registered between the two types.

## GUI Editor

Input [ports](../EGO-Script.html#ports) of type Kml Timeline are non-editable, so a Kml Timeline value cannot be defined using an editor in the graphical interface. A Kml Timeline value must always come from connecting an output produced by another functor -- [Set Kml Timeline](../functors/Set-Kml-Timeline.html) or [Mux Kml Timeline](../functors/Mux-Kml-Timeline.html) -- supplied by wiring that output to the input.

## EGO Script

For the same reason, input [ports](../EGO-Script.html#ports) of type Kml Timeline cannot receive a constant in [EGO Script](../EGO-Script.html) -- see [Constants](../EGO-Script.html#constants). Unlike [Kml](Kml-Type.html), there is no generic carrier functor for Kml Timeline either; a Kml Timeline is always obtained directly from [Set Kml Timeline](../functors/Set-Kml-Timeline.html) or [Mux Kml Timeline](../functors/Mux-Kml-Timeline.html), and reused by referencing the variable bound to its output:

```
// landUse2020 and landUse2021 are Categorical Maps loaded earlier in the model.
// The first call starts a fresh Kml Timeline (kmlTimeline defaults to .none);
// the second call appends to the timeline the first call produced.
overlay2020 := CreateKml landUse2020;
overlay2021 := CreateKml landUse2021;

timeline1 := SetKmlTimeline overlay2020;
timeline2 := SetKmlTimeline overlay2021 timeline1;
```

Building a timeline across a loop instead of a fixed sequence of calls follows the general [mux pattern](../EGO-Script.html#carrying-and-selecting-values-across-iterations): [Mux Kml Timeline](../functors/Mux-Kml-Timeline.html) at the top of the loop body, paired with a [Set Kml Timeline](../functors/Set-Kml-Timeline.html) call at the bottom that feeds its result back in as the next iteration's `feedback` input.

## Automatic Conversions

Kml Timeline Type has no registered conversions to or from any other type. The only conversion registered for it at all is the sequencing conversion to [None Type](None-Type.html) -- used to force execution order via `sequenceInput`/`sequenceOutput` ports, not to transform a value.

See [Type System](../Type-System.html).
{% endraw %}
