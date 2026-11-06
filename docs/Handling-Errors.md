---
title: "Handling Errors"
nav_order: 7
parent: "Modeling Guides"
---
{% raw %}
# Handling Errors

## Overview

A model normally stops at the first error raised by any of its functors. [Skip On Error](functors/Skip-On-Error.html) and [Skip All On Error](functors/Skip-All-On-Error.html) change this for the functors they contain: an error raised inside them is captured, and the rest of the model keeps running. See [Error-handling containers](Functors-And-Ports.html#error-handling-containers) for what the two containers do and how they differ.

Capturing the error is only half of the job. Something outside the container still has to react to the outcome, and the right tool depends on what the model needs: a [junction](Functors-And-Ports.html#muxes-and-junctions) when the goal is a fallback value, or [If Then](functors/If-Then.html) and [If Not Then](functors/If-Not-Then.html) when the two outcomes need to do different things. The functors inside the container are usually independent of each other, with no data dependency forcing an order between them, and what distinguishes the two containers is what happens to their results when one of them fails partway through. The sections below show each combination.

## Falling back to a matched set of values

[Skip All On Error](functors/Skip-All-On-Error.html) discards **all** results produced inside it when any of its functors raises an error, even the results of functors that had already completed successfully on their own. Outside the container, a junction then tests whether each value propagated out: if it was discarded, the junction falls back to its default; if no error occurred, the value propagates normally and the junction forwards it.

This makes [Skip All On Error](functors/Skip-All-On-Error.html) the right choice when several values only make sense together. The example below loads a categorical map together with a lookup table of transition weights that only applies to that specific map. If either file is missing, both should fall back to a matched pair of defaults, rather than pairing a real map with mismatched default weights, or the reverse:

```
_ := SkipAllOnError .yes {{
    // loadedMap and loadedWeights need to succeed together or not at all --
    // if either file is missing, SkipAllOnError discards both, even
    // whichever one loaded successfully, so the junctions below always
    // fall back to a matched, consistent pair of defaults.
    loadedMap := LoadMap mapFilename;
    loadedWeights := LoadLookupTable weightsFilename;
}};

// If either load failed, both loadedMap and loadedWeights were discarded,
// and both junctions fall back to their defaults. If both succeeded, each
// junction forwards the real value.
mapOrDefault := MapJunction loadedMap defaultMap;
weightsOrDefault := LookupTableJunction loadedWeights defaultWeights;
```

[Skip On Error](functors/Skip-On-Error.html) would be a mistake here. Since `loadedMap` and `loadedWeights` have no data dependency on each other, nothing guarantees which of the two, if either, has already completed by the time the other raises its error — see [Basic Data Flow](Basic-Data-Flow.html#data-dependencies-drive-execution-order). The outcome would be a race: a real map could end up paired with default weights, or the reverse, unpredictably from run to run. [Skip All On Error](functors/Skip-All-On-Error.html) avoids the race entirely by discarding both regardless of which one failed or how far the other had gotten, which is exactly what "succeed together or not at all" requires.

## Testing for success only

When the model only needs to know whether the contents succeeded, and not to substitute a value, no junction is necessary. Both containers report the outcome directly through their `executionCompletedSuccessfully` output:

```
result := SkipAllOnError .yes {{
    _ := LoadMap inputMapFilename;
}};
```

`result` is that boolean directly. The matched-fallback pattern above earns its extra complexity only when a real value, not just a flag, needs a fallback on failure.

## Keeping partial results

[Skip On Error](functors/Skip-On-Error.html) behaves differently: instead of discarding everything, it keeps the outputs of every functor that had already completed when the error was raised. It is the right choice when partial results are genuinely useful on their own, and whatever it keeps is what each branch of the model has to work with afterwards.

When the branches only need to pick between two values, a junction is still the simplest tool. When they need to carry out different logic, [If Then](functors/If-Then.html) and [If Not Then](functors/If-Not-Then.html) can test the container's `executionCompletedSuccessfully` output directly, with no separate sentinel value. This example attempts to load an optional mask map; if it loads, the matching branch has the mask itself to work with, and if it is missing or fails to load, the other branch proceeds without one:

```
maskLoaded := SkipOnError .yes {{
    mask := LoadMap maskFilename;
}};

// maskLoaded is SkipOnError's own boolean output; mask itself -- preserved
// on success -- is what the matching branch below actually needs.
_ := IfThen maskLoaded {{
    _ := Print "Mask loaded; masking enabled" .none {{ }};
}};

_ := IfNotThen maskLoaded {{
    _ := Print "Mask not found; continuing without one" .none {{ }};
}};
```

## Choosing between a junction and a conditional

The two tools answer different questions. A junction picks one of two values and hands it onward, which is all that is needed when both outcomes lead to the same kind of value — [Printing a table with a generic format](Manipulating-Tables-And-Lookup-Tables.html#printing-a-table-with-a-generic-format) uses one to pick between two mutually exclusive attempts, each wrapped in its own [Skip On Error](functors/Skip-On-Error.html). [If Then](functors/If-Then.html) and [If Not Then](functors/If-Not-Then.html) earn their place when the two outcomes need to do something different.
{% endraw %}
