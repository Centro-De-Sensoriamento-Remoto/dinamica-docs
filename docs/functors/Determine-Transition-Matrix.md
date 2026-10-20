---
title: "Determine Transition Matrix"
nav_order: 1
parent: "Calibration Functors"
grand_parent: "Functor List"
---
{% raw %}
# Determine Transition Matrix

## Description

Determines a matrix of transition rates between two time-series maps: a single-step transition matrix for the entire period between the initial and final landscape maps, and a multi-step transition matrix for a given number of time steps into which that period is divided.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Initial Landscape | [Categorical Map Type](../types/Categorical-Map-Type.html) | Initial map of land use and cover classes. |
| Final Landscape | [Categorical Map Type](../types/Categorical-Map-Type.html) | Final map of land use and cover classes. |
| Time Steps | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number of time steps between the initial and final landscape maps. A step can be any unit of time, such as a year or a month, since Dinamica EGO uses it only as an external reference parameter. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Single Step Matrix | [Transition Matrix Type](../types/Transition-Matrix-Type.html) | Transition matrix for the entire period between the initial and final landscape maps. |
| Multi Step Matrix | [Transition Matrix Type](../types/Transition-Matrix-Type.html) | Transition matrix for a single time step, derived by dividing the period between the initial and final landscape maps by Time Steps. |

## Group

[Calibration](../Functor-List.html#calibration)

## Notes

Only the classes present in the categorization of the initial or final map are used when determining the transitions that occurred between the two maps; any other values are ignored.

A cell is ignored in the calculation if its value is null in either the initial or the final map.

To analyze a historical context, Initial Landscape should be the older map of the time series.

Deriving the multi-step matrix from the single-step matrix requires an eigendecomposition of the single-step matrix, which is only possible when that matrix is ergodic, that is, when it has well-defined eigenvalues and eigenvectors. See <http://mathworld.wolfram.com/EigenDecompositionTheorem.html> for details on this decomposition and on why it is not always possible.

The transition matrix describes a system that changes over discrete time increments, in which the value of any variable in a given period is the sum of fixed percentages of the values of the variables in the previous period. The fractions in each column of the transition matrix sum to one; the diagonal need not be filled in, since it represents the percentage of unchanged cells. The transition rates are passed to the model as a fixed parameter within a given phase; the time step itself can span any amount of time, since Dinamica treats the time unit only as an externally set reference parameter.

## Internal Name

DetermineTransitionMatrix

## Usage examples

See practical examples of this functor in [Lesson 18: Building a land-use and land-cover change simulation model](../guidebook/Land-Use-Change-Simulation-Model.html) of the Guidebook.
{% endraw %}
