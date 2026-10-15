---
title: "Determine Weights Of Evidence Correlation"
nav_order: 4
parent: "Calibration Functors"
grand_parent: "Functor List"
---
{% raw %}
# Determine Weights Of Evidence Correlation

## Description

This container calculates the correlation between pairs of spatial variables used in a Weights of Evidence analysis, to help verify that they are spatially independent, an assumption the Weights of Evidence method requires. Correlated variables identified this way can be eliminated, or combined into a new variable that replaces both.

This container accepts one or more [Name Map](Name-Map.html) hooks nested inside it, each assigning a name to a map. These named maps supply the values for the spatial variables referenced by Ranges.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Ranges | [Weights Type](../types/Weights-Type.html) | Pre-defined ranges for each spatial variable whose pairwise correlation will be calculated. |
| Transition | [Transition Set Type](../types/Transition-Set-Type.html) | Transition for which the variables and ranges are defined. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Report | [Table Type](../types/Table-Type.html) | Table with the same information reported to the message log during the calculation: for each pair of variables, the columns "Transition_From", "Transition_To", "First_Variable", "Second_Variable", "Chi_2", "Cramer", "Contingency", "Joint_Entropy", and "Joint_Uncertainity". |

## Group

[Calibration](../Functor-List.html#calibration)

## Notes

The correlation between each pair of variables is calculated from a contingency table built by cross-tabulating the two maps, using Cramer's coefficient and the joint entropy method, following Bonham-Carter (1994).

Reports an error if Transition is empty.

Reports an error if a spatial variable named in Ranges is not provided by a nested Name Map hook.

**References**

Bonham-Carter, G., 1994. Geographic information systems for geoscientists: modelling with GIS. New York, Pergamon.

## Internal Name

DetermineWeightsOfEvidenceCorrelation

## Usage examples

See practical examples of this functor in Lesson 18: Building a land-use and land-cover change simulation model
{% endraw %}
