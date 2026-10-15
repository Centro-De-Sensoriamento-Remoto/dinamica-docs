---
title: "Determine Weights Of Evidence Continuous Occurrences"
nav_order: 3
parent: "Calibration Functors"
grand_parent: "Functor List"
---
{% raw %}
# Determine Weights Of Evidence Continuous Occurrences

## Description

This container determines Weights of Evidence coefficients for selected spatial variables with respect to a map of occurrences, using the same Weights of Evidence method as [Determine Weights Of Evidence Coefficients](Determine-Weights-Of-Evidence-Coefficients.html). Unlike that container, which works from a transition between an initial and a final map, this one works from a map where each cell holds a count of how many times some event occurred at that location, so the map of occurrences does not need to be binary.

This container accepts one or more [Name Map](Name-Map.html) hooks nested inside it, each assigning a name to a map. These named maps supply the values for the spatial variables referenced by Ranges.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Occurrences | [Map Type](../types/Map-Type.html) | Map of occurrences. Each cell holds the number of times the modeled event occurred at that location. |
| Mask | [Map Type](../types/Map-Type.html) | Map defining, through cells other than its null value, which cells should be analyzed. Its cells must be representable as a 32 Bit Integer. |
| Ranges | [Weights Type](../types/Weights-Type.html) | Pre-defined ranges of each spatial variable for which the Weights of Evidence coefficients will be calculated. Only the ranges defined for the first transition are used; ranges defined for any other transition are ignored. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Fix Abnormal Weights | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, recalculates weights that would otherwise result in abnormal values, such as those arising from a division by zero. If false, those abnormal values are assumed to be zero. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Weights | [Weights Type](../types/Weights-Type.html) | Weights of Evidence coefficients obtained for the selected spatial variables, with respect to the given occurrences. |

## Group

[Calibration](../Functor-List.html#calibration)

## Notes

Cells with zero occurrences are also used in the calculation: one is always added to the number of occurrences found at a cell before it is used. Only cells located outside the area defined by Mask are excluded from the calculation.

Reports an error if a spatial variable named in Ranges is not provided by a nested Name Map hook.

Reports an error if Mask has cells that cannot be represented as a 32 Bit Integer.

This method was adapted from Agterberg & Bonham-Carter (1990), Goodacre et al. (1993), and Bonham-Carter (1994).

**References**

Agterberg, F.P. and Bonham-Carter, G.F., 1990: Deriving weights of evidence from geoscience contour maps for the prediction of discrete events. XXII Int. Symposium AP-COM, 381-395.

Bonham-Carter, G., 1994: Geographic information systems for geoscientists: modelling with GIS. Pergamon, 398 pp.

Goodacre, C. M., Bonham-Carter, G. F., Agterberg, F. P., Wright, D. F., 1993: A statistical analysis of spatial association of seismicity with drainage patterns and magnetic anomalies in western Quebec. Tectonophysics, 217, 205-305.

## Internal Name

DetermineWeightsOfEvidenceContinuousOccurrences
{% endraw %}
