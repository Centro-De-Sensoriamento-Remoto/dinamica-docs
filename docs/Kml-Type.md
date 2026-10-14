---
title: "Kml Type"
nav_exclude: true
---
{% raw %}
# Kml Type

A **Kml** represents a single georeferenced image overlay for Google Earth: a rendering of a map's cells, placed and scaled according to the map's projection and extents, so that Google Earth can display it draped over the globe.

A Kml is produced either by rendering a [Categorical Map](Categorical-Map-Type.html) directly via [Create Kml](Create-Kml.html), or by loading an existing overlay from a `.kmz` file via [Load Compressed Kml](Load-Compressed-Kml.html). It is consumed by writing it back out with [Save Compressed Kml](Save-Compressed-Kml.html), or by folding it into a [Kml Timeline](Kml-Timeline-Type.html) with [Set Kml Timeline](Set-Kml-Timeline.html), optionally bounded by a `beginTime`/`endTime` pair. Building a sequence of these entries into a single animated, time-stamped display typically means calling [Set Kml Timeline](Set-Kml-Timeline.html) once per loop iteration; [Mux Kml Timeline](Mux-Kml-Timeline.html) is the loop-feedback functor that carries the growing timeline from one iteration to the next, the same role [Mux Map](Mux-Map.html) and [Mux Lookup Table](Mux-Lookup-Table.html) play for their own types.

## GUI Editor

Input [ports](EGO-Script.html#ports) of type Kml are non-editable, so a Kml value cannot be defined using an editor in the graphical interface. A Kml value must always come from connecting an output produced by another functor -- [Create Kml](Create-Kml.html) or [Load Compressed Kml](Load-Compressed-Kml.html) -- supplied by wiring that output to the input.

## EGO Script

For the same reason, input [ports](EGO-Script.html#ports) of type Kml cannot receive a constant in [EGO Script](EGO-Script.html) -- see [Constants](EGO-Script.html#constants). A Kml is always obtained by calling a functor that produces one, and reused by referencing the variable bound to its output:

```
// Renders a categorical map as a Google Earth overlay and saves it.
landUse := LoadCategoricalMap "c:/data/land_use.tif";
overlay := CreateKml landUse;
SaveCompressedKml overlay "c:/data/land_use.kmz";
```

The generic [Kml](Kml.html) carrier functor exists purely to pass a Kml connection through -- for example, as a placeholder while wiring a model -- but its own input is likewise non-editable; it must itself be connected to another functor's Kml output.

## Automatic Conversions

Kml Type has no registered conversions to or from any other type. The only conversion registered for it at all is the sequencing conversion to [None Type](None-Type.html) -- used to force execution order via `sequenceInput`/`sequenceOutput` ports, not to transform a value.

See [Type System](Type-System.html).
{% endraw %}
