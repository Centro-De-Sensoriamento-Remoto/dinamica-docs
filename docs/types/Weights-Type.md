---
title: "Weights Type"
nav_order: 43
parent: "Type System"
grand_parent: "Core Concepts"
redirect_from:
  - /Weights-Type.html
---
{% raw %}
# Weights Type

A Weights value stores Weights of Evidence data, used in calibration and simulation. What it holds depends on where it sits in the calibration pipeline: it can represent either a set of pre-defined ranges (intervals) for continuous variables, or a set of computed coefficients for those ranges once calibrated.

[Determine Weights Of Evidence Ranges](../functors/Determine-Weights-Of-Evidence-Ranges.html) takes a [Weights Of Evidence Skeleton](Weights-Of-Evidence-Skeleton-Type.html) — which variables to use, and how to discretize them — along with a pair of calibration maps, and produces a Weights value holding the resulting ranges. That Weights value then becomes the `ranges` input to [Determine Weights Of Evidence Coefficients](../functors/Determine-Weights-Of-Evidence-Coefficients.html), [Determine Weights Of Evidence Continuous Occurrences](../functors/Determine-Weights-Of-Evidence-Continuous-Occurrences.html), and [Determine Weights Of Evidence Correlation](../functors/Determine-Weights-Of-Evidence-Correlation.html), each producing its own Weights output — coefficients, for the first two — from it. [Calc W. Of E. Probability Map](../functors/Calc-W-Of-E-Probability-Map.html) is the ultimate consumer, using a Weights value of coefficients to compute a spatial probability map.

## GUI Editor

Weights Type has no editor. A value can only be obtained by loading one from a file with [Load Weights](../functors/Load-Weights.html), or by connecting the output of one of the calibration functors above — never typed in directly.

## EGO Script

For the same reason, Weights Type has no literal constant syntax in [EGO Script](../EGO-Script.html) — see [Constants](../EGO-Script.html#constants). Weights values are usually read from an external file using [Load Weights](../functors/Load-Weights.html) and written using [Save Weights](../functors/Save-Weights.html), or produced directly by a calibration functor:

```
{ woeCoefficients = weights, woeReport = report } := DetermineWeightsOfEvidenceCoefficients initialLandscape finalLandscape ranges;
```

## Automatic Conversions

- **Converted from**: [Table Type](Table-Type.html). Two column layouts are accepted: `From*` (Real), `To*` (Real), `Variable*` (String), `Range_Lower_Limit*` (Real), `Range_Upper_Limit*` (Real), `Weight` (Real); or the same without `Range_Upper_Limit`.
- **Converted to**: [Table Type](Table-Type.html), using the six-column layout above.

See [Type System](../Type-System.html) for the complete conversion reference across all types.
{% endraw %}
