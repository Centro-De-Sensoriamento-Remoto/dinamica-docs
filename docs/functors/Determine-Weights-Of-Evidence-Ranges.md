---
title: "Determine Weights Of Evidence Ranges"
nav_order: 5
parent: "Calibration Functors"
grand_parent: "Functor List"
---
{% raw %}
# Determine Weights Of Evidence Ranges

## Description

This container defines the best ranges, or intervals, used to categorize continuous gray-tone spatial variables before their Weights of Evidence coefficients are calculated by [Determine Weights Of Evidence Coefficients](Determine-Weights-Of-Evidence-Coefficients.html). For each variable, the range of values is divided into a sequence of increasingly large buffers, and a breakpoint-finding algorithm is applied to the resulting curve to choose a small number of ranges that still preserve the shape of the underlying relationship between the variable and the modeled transition.

This container accepts one or more [Name Map](Name-Map.html) hooks nested inside it, each assigning a name to a map. These named maps supply the values for the spatial variables referenced by Skeleton.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Initial Landscape | [Categorical Map Type](../types/Categorical-Map-Type.html) | Initial map of land use and cover classes. |
| Final Landscape | [Categorical Map Type](../types/Categorical-Map-Type.html) | Final map of land use and cover classes. |
| Skeleton | [Weights Of Evidence Skeleton Type](../types/Weights-Of-Evidence-Skeleton-Type.html) | Selected spatial variables and their types (category or continuous gray-tone), along with the parameters used to define ranges for each continuous variable, such as increment, minimum and maximum deltas, and tolerance angle. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Fix Abnormal Weights | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, recalculates weights that would otherwise result in abnormal values, such as those arising from a division by zero. If false, those abnormal values are assumed to be zero. This is an advanced port. | No |
| Potential Transition Criteria | [Boolean Value Type](../types/Boolean-Value-Type.html) | Affects how a possible but unexecuted transition from class C to class P is identified. If true, any cell that transitions from C to some other class X (different from P) is considered a case where the C to P transition was possible but did not happen. If false, only a cell that stays in class C is considered such a case. This affects the analysis of concurrent transitions, and is an advanced port. | Yes |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Ranges | [Weights Type](../types/Weights-Type.html) | Ranges defined for each continuous gray-tone variable. |

## Group

[Calibration](../Functor-List.html#calibration)

## Notes

For each continuous variable, a sequence of nested buffers is built by incrementing a minimum delta over the variable's range. The number of cells in each buffer, and the number of occurrences of the modeled transition within it, are used to calculate a weight for that buffer. A breakpoint-finding algorithm, using the same criteria as MicroStation's line-generalizing algorithm, is then applied to the resulting curve to choose a small set of ranges: a new range boundary is placed whenever consecutive points are farther apart than the maximum delta, and no boundary is placed between points closer than the minimum delta, unless the angle between them exceeds the tolerance angle.

Reports an error if a spatial variable named in Skeleton is not provided by a nested Name Map hook.

Reports an error if a spatial variable is categorized as a category variable but its map has cells of type Unsigned 32 Bit Integer or Floating Point (32 Bit).

This method was adapted from Agterberg & Bonham-Carter (1990).

**References**

Agterberg, F.P. and Bonham-Carter, G.F., 1990: Deriving weights of evidence from geoscience contour maps for the prediction of discrete events. XXII Int. Symposium AP-COM, 381-395.

Intergraph Corporation, 1991. Intergraph Microstation PC, Version 4 User's Guide. Bentley Systems, Inc. and Intergraph Corporation, 333 pp.

## Internal Name

DetermineWeightsOfEvidenceRanges

## Usage examples

See practical examples of this functor in [Lesson 18: Building a land-use and land-cover change simulation model](../guidebook/Land-Use-Change-Simulation-Model.html) of the Guidebook.
{% endraw %}
