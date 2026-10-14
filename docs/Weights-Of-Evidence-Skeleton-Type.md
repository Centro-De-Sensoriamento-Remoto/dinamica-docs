---
title: "Weights of Evidence Calibration"
nav_exclude: true
---
{% raw %}
# Weights of Evidence Calibration

## Overview

This page describes the process of calibrating Weights of Evidence: starting from a pair of landscape maps and a set of predictive variables, and ending with a set of ranges and their corresponding coefficients. It covers the practical steps around the two container functors that do the work, [Determine Weights Of Evidence Ranges](Determine-Weights-Of-Evidence-Ranges.html) and [Determine Weights Of Evidence Coefficients](Determine-Weights-Of-Evidence-Coefficients.html); see those pages for the full port reference of each.

## What Is Weights of Evidence

Weights of Evidence is a Bayesian method, originally used in geology to map favorability for events such as mineralization, adapted here to relate a land-use transition to a set of predictive spatial variables.

For a transition from category i to category j, each class of a predictive variable (a category, or a range of a continuous gray-tone variable) is assigned two numbers: a positive weight (W+), reflecting how the transition's likelihood changes for cells that fall inside that class, and a negative weight (W-), reflecting the same for cells that fall outside it.

[Calc W. Of E. Probability Map](Calc-W-Of-E-Probability-Map.html) combines these weights with a transition's baseline probability to produce a probability for each cell, based on which range or category the cell falls into for each variable. This is why a weight's sign has a consistent meaning:

- **Zero** -- leaves the baseline probability unchanged. A range with a zero weight carries no information about the transition, one way or the other.
- **Positive** -- raises the probability above baseline. Cells in that range are more likely than average to make the transition -- the range favors it.
- **Negative** -- lowers the probability below baseline. Cells in that range are less likely than average to make the transition -- the range repels it.

**Contrast** (C = W+ - W-) measures a range's overall association with the transition: it is what determines whether the range meaningfully favors or repels the transition, or has close to no effect. This is the number the significance test applies to (see [Determining Coefficients](#determining-coefficients) below). A range with a Weight_Coefficient near zero and a non-significant Contrast are two ways of saying the same thing: the range isn't doing meaningful explanatory work for the transition.

Every variable's weights combine together to produce a transition's overall probability at each cell, which is why the method requires its input variables to be spatially independent of one another (see [Checking Variable Independence](#checking-variable-independence) below).

## Preparing the Input Variables

Internally, Weights of Evidence operates only on categorical maps. Every predictive variable must ultimately be represented as a [Categorical Map](Categorical-Map-Type.html), but not every variable starts out that way, and the two cases are handled differently:

- **Category variables** -- a map whose values are already the final classes to compare, such as soil type or a protected-area boundary. These enter the calibration directly as categorical.
- **Continuous gray-tone variables** -- a map of raw, unbinned values, such as a slope raster or a distance-to-roads / distance-to-drainage layer generated as a buffer. These do **not** need to be manually classified into intervals before being used. Calibrating them is exactly what the range-determination step below does: it finds the class boundaries and outputs them as the ranges Weights object.

If a variable has already been manually classified into intervals outside Dinamica EGO (for example, a slope map pre-binned into 0-100 m, 100-200 m, and so on), treat it as a Category variable rather than a continuous one -- the calibration process does not re-bin a variable that is already categorical.

## The Weights of Evidence Skeleton

The [Weights Of Evidence Skeleton](Weights-Of-Evidence-Skeleton-Type.html) is the structure that lists the selected spatial variables, marks each one as Category or continuous gray-tone, and, for the continuous ones, carries the parameters used to define their ranges:

| Parameter | Unit | Description |
| --- | --- | --- |
| Increment | The variable's own map unit (e.g. meters, degrees) | Step size used to build the sequence of incremental buffers over the variable's raw value range. |
| Minimum Delta | Cells | Lower bound on the buffer-size interval considered by the line-generalizing algorithm when placing breakpoints. |
| Maximum Delta | Cells | Upper bound on that same buffer-size interval. |
| Tolerance Angle | Decimal degrees | Angle of deviation from a straight line that triggers a new breakpoint; a larger tolerance angle produces fewer, coarser ranges. |

These four parameters apply only to continuous gray-tone variables. A variable marked Category in the Skeleton does not use them at all -- increment, the two deltas, and the tolerance angle have no meaning for a variable that is already classified.

> **Note:** When written as an EGO Script literal, a continuous variable's parameters appear in this order: Increment, **Maximum** Delta, **Minimum** Delta, Tolerance Angle -- the two deltas are reversed from the order shown in the table above. See "Example: A Basic Calibration Model" below for the exact syntax.

## Determining Ranges for a Continuous Variable

[Determine Weights Of Evidence Ranges](Determine-Weights-Of-Evidence-Ranges.html) takes the Skeleton, together with the initial and final landscape maps, and produces the ranges output (a Weights object) used by the coefficient step below.

> **Note:** The ranges output only carries the categorization boundaries -- every weight in it is initialized to zero. It becomes a populated Weights object, with actual coefficients, only after being run through [Determine Weights Of Evidence Coefficients](Determine-Weights-Of-Evidence-Coefficients.html) in the next step.

### Why This Works

Determine Weights Of Evidence Ranges finds range boundaries by watching how the transition's weight changes as it sweeps across a continuous variable's values, rather than requiring pre-set cut points.

Starting at the variable's minimum value, it grows a sequence of nested buffers outward in steps equal to the Increment: the first buffer covers up to one Increment past the minimum, the second covers up to two Increments past it, and so on, each one containing everything the previous one did plus a bit more. For each buffer, it counts how many cells fall inside it and how many of those cells actually made the transition, and from that pair derives the weight (W+) that buffer's edge would produce if used as a single cutoff. Sweeping through the whole sequence of buffers produces a curve: weight as a function of how far the buffer has grown.

Where this curve stays flat, the variable isn't discriminating anything at that point -- going a bit further out doesn't change the odds. Where the curve bends, that's where crossing that value of the variable starts to matter. So the range boundaries are wherever the curve changes direction, which is a shape-finding problem, not something that can be set analytically in advance.

Because the earliest buffers are built from very few cells, their weight estimate is noisy -- a small sample makes for an unreliable ratio. To keep a noisy early buffer from faking a bend that isn't real, the curve is built from each buffer's size multiplied by the exponential of its weight, rather than the raw weight alone, so a buffer's influence on the curve's shape scales with how much data actually backs it.

A line-generalizing algorithm then walks along this curve and keeps extending a straight segment for as long as it plausibly can. It will not place a new breakpoint before Minimum Delta cells have passed since the last one, since a segment needs at least that much support, but it is forced to place one once Maximum Delta cells have passed regardless.

Within that window, whether a breakpoint gets placed is decided by comparing two directions: the direction from the last confirmed breakpoint to the current candidate point, against the direction the segment before that was already heading in (from the breakpoint before it, to the last confirmed one). If the angle between those two directions exceeds the Tolerance Angle, the current point is not a straight continuation of where the curve was already going, so a breakpoint is placed at the last point instead, closing off the previous segment there and starting a new one from it. Straight stretches become single ranges; each breakpoint becomes a range boundary.

This is also why the tuning procedure below works. Raising Minimum Delta forces the algorithm to hold off on placing a breakpoint near the start of the sweep, precisely where the buffer is smallest and the weight estimate is least trustworthy. It is not a workaround -- it tells the range-finder not to treat a segment as real until it is backed by at least that many cells, which is exactly what a low `Possible_Transitions` count on a non-significant row is warning about downstream (see [Determining Coefficients](#determining-coefficients)).

A commonly used starting point for the Skeleton's parameters, for each continuous gray-tone variable in turn, is:

- Increment = 1
- Maximum delta = a large value, such as 5000000, so it does not constrain the search
- Tolerance angle = 5
- Minimum delta = 1, as the starting point to be tuned

From there, the minimum delta is tuned iteratively:

1. Run the range-and-coefficient calculation (the two functors chained together, initial landscape and final landscape feeding both, ranges from the first feeding the second).
1. Inspect the `report` output of [Determine Weights Of Evidence Coefficients](Determine-Weights-Of-Evidence-Coefficients.html) (the same information shown in the message log, in table form). Look at the `Significant` column.
1. The goal is to maximize the number of `Significant = Yes` rows.
1. For any row where `Significant = No`, read that row's `Possible_Transitions` value and set the minimum delta slightly above it, then repeat from step 1.
1. If several rows are not significant at once, use the largest `Possible_Transitions` value among them as the basis for the next minimum delta.

This loop can also be driven automatically within a single model run -- see [Automating the Range Tuning Loop](#automating-the-range-tuning-loop) below.

Each continuous gray-tone variable goes through this tuning individually -- the ranges for one variable do not carry over to another. Category variables skip this section entirely, since none of the four Skeleton parameters apply to them.

## Determining Coefficients

Once ranges have been calibrated for every continuous variable, [Determine Weights Of Evidence Coefficients](Determine-Weights-Of-Evidence-Coefficients.html) takes the initial landscape, final landscape, and ranges, and produces:

- `weights` -- the Weights of Evidence coefficients themselves.
- `report` -- a Table with one row per transition / variable / range combination, in this format:

| Column | Type | Key |
| --- | --- | --- |
| `Transition_From` | Real | Yes |
| `Transition_To` | Real | Yes |
| `Variable` | String | Yes |
| `Range_Lower_Limit` | Real | Yes |
| `Range_Upper_Limit` | Real | Yes |
| `Possible_Transitions` | Real | No |
| `Executed_Transitions` | Real | No |
| `Weight_Coefficient` | Real | No |
| `Contrast` | Real | No |
| `Significant` | Real | No |

### Reading the report

- **Possible_Transitions** -- the number of cells that could have made this transition, given they started in the "from" category and fell inside this variable's range. What counts as "possible" is controlled by `potentialTransitionCriteria` (see below).
- **Executed_Transitions** -- of those possible cells, how many actually made the transition during the observed period.
- **Weight_Coefficient** -- the resulting weight (W+) for that range or category: its contribution to the transition's probability wherever it applies.
- **Contrast** -- W+ minus W- for that range or category. Positive values favor the transition, negative values repel it, and values near zero mean the range has little effect. See [What Is Weights of Evidence](#what-is-weights-of-evidence) above for how this is derived.
- **Significant** -- whether the Contrast passes the 95% confidence threshold (\|C\| > 1.96 S(C)). Rows marked "No" are exactly the ones the range-tuning loop above targets when adjusting the minimum delta.

A strongly positive, significant Contrast marks a range that meaningfully favors the transition; a strongly negative, significant Contrast marks one that suppresses it; a low-magnitude or non-significant Contrast means that range of that variable isn't doing much explanatory work and may be a candidate for coarsening (larger minimum delta) or dropping.

Both functors also expose two optional inputs that affect this calculation:

| Port | Default | Effect |
| --- | --- | --- |
| `fixAbnormalWeights` | No | If true, abnormal weights are recalculated instead of assumed to be zero. |
| `potentialTransitionCriteria` | Yes | When analyzing a transition from category C to category P: if true, any observed transition from C to some other category X (X != P) counts as "possible but not executed"; if false, only X = C counts that way. This changes how concurrent transitions are treated in the analysis. |

## Checking Variable Independence

Weights of Evidence's one formal requirement is that the input variables be spatially independent -- if two variables are highly correlated, their combined contribution double-counts the same spatial signal.

[Determine Weights Of Evidence Correlation](Determine-Weights-Of-Evidence-Correlation.html) checks this pairwise, for every candidate variable at once, against a chosen transition. Required inputs: `ranges` (Weights -- the same output produced by [Determining Ranges for a Continuous Variable](#determining-ranges-for-a-continuous-variable) above) and `transition` (TransitionSet, editable). Output: `report` (Table), with pairwise statistics including Chi-square, Cramer's V, Contingency, Entropy, and Joint Information.

There is no fixed universal threshold for "too correlated" -- it's a judgment call based on the report values. When a pair of variables shows high correlation across these measures, drop one of them or combine both into a new derived variable, then re-run the range and coefficient calibration for the surviving variable set.

## Reusing and Saving Weights

[Save Weights](Save-Weights.html) writes either the ranges or the final coefficients to a file, with the format inferred from the filename extension. For calibrations that vary across model steps, [Number Weights](Number-Weights.html) / [Number Weights Filename](Number-Weights-Filename.html) tag a Weights value or filename with a step number, and the corresponding [Select Weights](Select-Weights.html) / [Select Weights Filename](Select-Weights-Filename.html) container functors pick the right one back out by step during execution.

### Weights file format

When [Save Weights](Save-Weights.html) writes a Weights object to CSV, it uses a five-column table: `From`, `To`, `Variable`, `Range_Lower_Limit`, `Weight`. The upper limit of each range is not stored explicitly -- it is inferred as the next row's `Range_Lower_Limit` for the same transition and variable, with the final range in each group extending to the maximum representable value.

A six-column variant is also accepted when loading a Weights CSV, with an explicit `Range_Upper_Limit` column inserted between `Range_Lower_Limit` and `Weight`. This form is useful for hand-edited or externally generated weight tables, but `Save Weights` itself only ever produces the five-column form.

> **Warning:** In the five-column format, rows must be grouped by transition and variable and sorted ascending by `Range_Lower_Limit` within each group. The upper limit of a range is inferred from the next row's lower limit, and a new group is only detected when the lower limit fails to increase -- not by a change in `Variable` or transition. Interleaved or unsorted rows will silently produce incorrect ranges.

> **Note:** This is not the same table as the `report` output described under [Determining Coefficients](#determining-coefficients) above. The report is a calibration-review artifact with additional statistics (`Possible_Transitions`, `Executed_Transitions`, `Contrast`, `Significant`); it is not a valid input for loading a Weights object back in. The format above is what actually round-trips through `Save Weights` / a Weights-typed file.

## Using the Weights Downstream

A finished, calibrated Weights object is not an end in itself -- it becomes an input to [Calc W. Of E. Probability Map](Calc-W-Of-E-Probability-Map.html), which combines it with the current landscape to produce a per-cell transition probability map.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `landscape` | Input | CategoricalMap | Yes | Map of classes or categories. |
| `weights` | Input | Weights | Yes | The calibrated Weights of Evidence coefficients. |
| `transitions` | Input | TransitionSet | Yes | Which transitions to calculate probability maps for. |
| `cellType` | Input | CellType | No (default Unsigned 8 Bit Integer) | Data cell type of the output map. |
| `nullValue` | Input | NullValue | No (default `.default`) | Null value of the output map. |
| `probabilities` | Output | Map | -- | The resulting spatial probability map. |

That probability map, together with a change matrix derived from the transition rates (via [Calc Change Matrix](Calc-Change-Matrix.html)), is what [Patcher](Patcher.html) and [Expander](Expander.html) consume to allocate the simulated changes across the landscape. In a multi-step simulation running inside a [Repeat](Repeat.html) loop, `Calc W. Of E. Probability Map` is typically recalculated every step against the updated landscape, since dynamic variables (such as distance to previously changed cells) change as the simulation progresses.

## Example: A Basic Calibration Model

This example ties the pieces above together: one continuous variable, one categorical variable, a range calculation, a coefficient calculation, and saving both results.

Each variable here is loaded as its own separate map, connected to its own [Name Map](Name-Map.html). Every map, cube or not, is organized into named [layers](Map-Type.html) -- a single, non-cube map simply has one, defaulting to `layer_0` unless it defines its own name; [Extract Map Layer](Extract-Map-Layer.html) pulls a specific layer out on its own, if one is needed outside a Skeleton reference. It's also possible to assemble every predictive variable into a single multi-layer cube via [Create Cube Map](Create-Cube-Map.html), the way Lesson 18's own example does -- but for a handful of variables that adds a layer of indirection without much benefit. A cube's usefulness shows up with many static variables: one [Name Map](Name-Map.html) alias then covers the whole set, and the model loads and connects one file instead of one per variable. Inside a cube, each layer's name comes from [Number And Name Map](Number-And-Name-Map.html) rather than plain Name Map, since it's assigning both an index and a name to a single layer as it's assembled.

```
// Input maps
Group {{
    initialLandscape := LoadCategoricalMap "landscape_1997.tif";
    finalLandscape   := LoadCategoricalMap "landscape_2000.tif";
}};

// continuous gray-tone
distanceToRoads  := LoadMap "d_all_roads.tif";

// category
protectedAreas   := LoadCategoricalMap "protected_areas.tif";

// The Skeleton: one entry per variable, written "alias/layerName". The
// alias is whatever name is given to that map's Name Map hook below --
// this is how each container matches a Skeleton entry back to the actual
// map connected to it. A map that does not explicitly define its own
// layer names uses the default "layer_0" for its first (here, only)
// layer. A continuous gray-tone variable is followed by four numbers, in
// this order: Increment, Maximum Delta, Minimum Delta, Tolerance Angle
// -- see "The Weights of Evidence Skeleton" above. A category variable
// takes no numbers.
skeleton := WeightsOfEvidenceSkeleton [
    2->1 [
        "roads/layer_0" 100 500000 10 5,
        "protected/layer_0"
    ]
];

// Step 1: determine ranges for the continuous variable(s). Name Map
// assigns each connected map the alias used above in the Skeleton.
ranges := DetermineWeightsOfEvidenceRanges {
    initialLandscape = initialLandscape,
    finalLandscape = finalLandscape,
    skeleton = skeleton
} {{
    NameMap distanceToRoads "roads";
    NameMap protectedAreas  "protected";
}};

// Step 2: determine coefficients from those ranges. Name Map aliases
// here must match Step 1 exactly -- see Tips below.
{ weights = weights, report = report } := DetermineWeightsOfEvidenceCoefficients {
    initialLandscape = initialLandscape,
    finalLandscape = finalLandscape,
    ranges = ranges
} {{
    NameMap distanceToRoads "roads";
    NameMap protectedAreas  "protected";
}};

// Step 3: save the results
Group {{
    SaveWeights { weights = weights, filename = "coefficients.dcf" };
    SaveTable   { table = report, filename = "report.csv" };
}};
```

The saved `coefficients.dcf` is the finished Weights object -- reload it with [Load Weights](Load-Weights.html) wherever [Calc W. Of E. Probability Map](Calc-W-Of-E-Probability-Map.html) needs it (see [Using the Weights Downstream](#using-the-weights-downstream)). The saved `report.csv` can be opened directly in a spreadsheet to review `Contrast` and `Significant` per range, without needing to scroll the message log.

## Automating the Range Tuning Loop

The manual procedure in [Determining Ranges for a Continuous Variable](#determining-ranges-for-a-continuous-variable) above adjusts Minimum Delta by hand, rerunning the model and reading the `Significant` column each time. This example automates that same procedure in a single model run.

The key that makes this possible: a [Weights Of Evidence Skeleton](Weights-Of-Evidence-Skeleton-Type.html) can be expressed as a Table instead of a fixed literal, using the column format `From*`, `To*`, `Variable_Name*`, `Categorical`, `Increment`, `Minimum_Delta`, `Maximum_Delta`, `Tolerance_Angle` -- `Categorical` is 0 for a continuous gray-tone variable, 1 for a category variable. A Table [converts to a Skeleton automatically](Type-System.html#table-format-of-table-shaped-types) wherever one is expected, and unlike a literal, a Table's cells can be rewritten by ordinary functors such as [Set Table Cell Value](Set-Table-Cell-Value.html). That is what lets Minimum Delta change from one iteration to the next.

The model wraps the range-and-coefficient calculation in a [Do While](Do-While.html) loop. Each pass: runs both calibration functors using the current Skeleton table, drills into the resulting `report` to find every range for the variable and transition in question, and scans them for any row where `Significant` is 0. If it finds one, it takes the largest `Possible_Transitions` among the failing rows, moves Minimum Delta just past it, writes that back into the Skeleton table, and loops again. Once every row comes back significant, the loop stops and the results are saved -- the same two outputs as the basic example above.

This assumes exactly one variable and one transition, so each `Range_Lower_Limit` maps to exactly one row; a model with more variables or transitions would need one additional nested [For Each](For-Each.html) per extra key column -- see "Sub-Tables" in [Manipulating Tables and Lookup Tables](Manipulating-Tables-And-Lookup-Tables.html).

```
// ---- Fixed inputs ----
Group {{
    initialLandscape := LoadCategoricalMap "landscape_1997.tif";
    finalLandscape   := LoadCategoricalMap "landscape_2000.tif";
}};

// continuous gray-tone
distanceToRoads := LoadMap "d_all_roads.tif";

// Starting Skeleton, expressed as a Table so Minimum_Delta can be
// rewritten each iteration below.
startingSkeleton := Table [
    "From*", "To*", "Variable_Name*", "Categorical", "Increment", "Minimum_Delta", "Maximum_Delta", "Tolerance_Angle",
    2, 1, "roads/layer_0", 0, 100, 1, 500000, 5
];

// Tune Minimum Delta until every range in the report comes back
// Significant.
_ := DoWhile {{
    skeletonTable := MuxTable startingSkeleton nextSkeletonTable;

    ranges := DetermineWeightsOfEvidenceRanges {
        initialLandscape = initialLandscape,
        finalLandscape = finalLandscape,
        skeleton = skeletonTable
    } {{
        NameMap distanceToRoads "roads";
    }};

    { weights = weights, report = report } := DetermineWeightsOfEvidenceCoefficients {
        initialLandscape = initialLandscape,
        finalLandscape = finalLandscape,
        ranges = ranges
    } {{
        NameMap distanceToRoads "roads";
    }};

    // Drop the three fixed keys (Transition_From, Transition_To,
    // Variable) in one call, leaving a table keyed by Range_Lower_Limit
    // and Range_Upper_Limit -- one row per determined range.
    rangesForVariable := GetTableFromKey report [2, 1, "roads/layer_0"];
    lowerLimits := GetTableKeys rangesForVariable;

    _ := ForEach lowerLimits {{
        anySoFar   := MuxValue 0 nextAny;
        worstSoFar := MuxValue 0 nextWorst;

        lowerLimit := Step;

        // Peel off Range_Lower_Limit too, landing on the single row for
        // this range, still formally keyed by Range_Upper_Limit.
        thisRange := GetTableFromKey rangesForVariable lowerLimit;
        upperLimitKeys := GetTableKeys thisRange;
        upperLimit := GetTableValue upperLimitKeys [1] 2;

        significant := GetTableValue thisRange upperLimit "Significant";
        possible    := GetTableValue thisRange upperLimit "Possible_Transitions";

        isNonSignificant := $ [ not $significant ];

        nextAny := $ [ $isNonSignificant or $anySoFar ];

        nextWorst := $ [
            if $isNonSignificant and $possible > $worstSoFar
            then $possible
            else $worstSoFar
        ];
    }};

    // Move Minimum Delta just past the range that failed significance,
    // and loop again if anything still needs it.
    newMinimumDelta := $ [ $nextWorst + 1 ];

    nextSkeletonTable := SetTableCellValue skeletonTable "Minimum_Delta" [2, 1, "roads/layer_0"] newMinimumDelta;

    keepGoing := $ [ $nextAny ];

    _ := SetWhileCondition keepGoing;
}};

// Step 3: save the results
Group {{
    SaveWeights { weights = weights, filename = "coefficients.dcf" };
    SaveTable   { table = report, filename = "report.csv" };
}};
```

## Tips

- A model with more than one transition needs its own ranges and coefficients per transition; the range parameters from one transition can be copied as a starting point for another, but each must still be tuned independently.
- The [Name Map](Name-Map.html) aliases used inside [Determine Weights Of Evidence Ranges](Determine-Weights-Of-Evidence-Ranges.html) and [Determine Weights Of Evidence Coefficients](Determine-Weights-Of-Evidence-Coefficients.html) must match exactly between the two containers -- this is how each container knows which named map corresponds to which variable in the Skeleton.
- To inspect or chart a report outside the message log, connect its `report` output to [Save Table](Save-Table.html) and export to CSV.
{% endraw %}
