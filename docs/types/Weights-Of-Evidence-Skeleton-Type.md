---
title: "Weights Of Evidence Skeleton Type"
nav_order: 44
parent: "Type System"
grand_parent: "Core Concepts"
---
{% raw %}
# Weights Of Evidence Skeleton Type

A Weights Of Evidence Skeleton value describes how a Weights of Evidence calibration is set up. For each transition, it lists the predictive variables to analyze, marks each one as categorical or continuous gray-tone, and, for each continuous variable, carries the parameters used to divide its values into ranges.

[Determine Weights Of Evidence Ranges](../functors/Determine-Weights-Of-Evidence-Ranges.html) consumes it through its `skeleton` input: together with the initial and final landscape maps, the skeleton determines the ranges of each variable, returned as a [Weights](Weights-Type.html) value that the rest of the calibration builds on. [Weights Of Evidence Skeleton](../functors/Weights-Of-Evidence-Skeleton.html) declares a skeleton once, so the same value can be connected to more than one functor. See [Weights of Evidence Calibration](../Weights-Of-Evidence-Calibration.html) for the complete calibration process and for how to choose the parameters.

## Variables and parameters

Each variable is identified as `alias/layerName`. The alias is the name given to the map by a [Name Map](../functors/Name-Map.html) hook inside the calibration container, and the layer name selects one layer of that map; a map that does not define its own layer names uses `layer_0` for its first layer.

A continuous gray-tone variable carries four parameters:

| Parameter | Unit | Description |
| --- | --- | --- |
| Increment | The variable's own map unit (e.g. meters, degrees) | Step size used to build the sequence of incremental buffers over the variable's value range. |
| Minimum Delta | Cells | Lower bound on the buffer-size interval considered by the line-generalizing algorithm when placing breakpoints. |
| Maximum Delta | Cells | Upper bound on that same buffer-size interval. |
| Tolerance Angle | Decimal degrees | Angle of deviation from a straight line that triggers a new breakpoint; a larger tolerance angle produces fewer, coarser ranges. |

A categorical variable is already classified, so it carries none of these parameters.

## EGO Script

A skeleton constant lists the variables of each transition inside brackets, after the transition written as `from->to`. Entries are separated by commas. A continuous variable is followed by its four parameters in the order Increment, **Maximum** Delta, **Minimum** Delta, Tolerance Angle -- the two deltas are reversed from the order of the table above. A categorical variable is written alone:

```
@charset = UTF-8
Script {{
    // Transition from 2 to 1: "roads/layer_0" is continuous, "protected/layer_0" is categorical.
    skeleton := WeightsOfEvidenceSkeleton [
        2->1 [
            "roads/layer_0" 100 500000 10 5,
            "protected/layer_0"
        ]
    ];
}};
```

See [Example: A Basic Calibration Model](../Weights-Of-Evidence-Calibration.html#example-a-basic-calibration-model) for this skeleton used in a complete model.

## Automatic Conversions

- **Converted from**: [Table Type](Table-Type.html), with the columns `From*` (Real), `To*` (Real), `Variable_Name*` (String), `Categorical` (Real), `Increment` (Real), `Minimum_Delta` (Real), `Maximum_Delta` (Real) and `Tolerance_Angle` (Real). `Categorical` is 0 for a continuous gray-tone variable and 1 for a categorical variable. The conversion fails if the table does not have this layout.
- **Converted to**: [Table Type](Table-Type.html), using the same layout.

Because a table's cells can be changed by ordinary functors such as [Set Table Cell Value](../functors/Set-Table-Cell-Value.html), expressing a skeleton as a table lets a model change its parameters while it runs. See [Automating the Range Tuning Loop](../Weights-Of-Evidence-Calibration.html#automating-the-range-tuning-loop) for an example.

See [Type System](../Type-System.html) for the complete conversion reference across all types.
{% endraw %}
