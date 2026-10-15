---
title: "Determine Weights Of Evidence Coefficients"
nav_order: 2
parent: "Calibration Functors"
grand_parent: "Functor List"
---
{% raw %}
# Determine Weights Of Evidence Coefficients

## Description

This container determines the Weights of Evidence coefficients for selected spatial variables with respect to the transitions occurring between an initial and a final map. Weights of Evidence is a Bayesian method, originally used in geology to point out favorable areas for phenomena such as mineralization, adapted here to measure the empirical relationship between spatial variables (represented by categorical or continuous maps) and land-use and land-cover change. For each transition and each variable, this container evaluates how much more (or less) likely the transition is within each of the variable's ranges than would be expected by chance, expressing that relationship as a weight and a contrast.

This container accepts one or more [Name Map](Name-Map.html) hooks nested inside it, each assigning a name to a map. These named maps supply the values for the spatial variables referenced by Ranges.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Initial Landscape | [Categorical Map Type](../types/Categorical-Map-Type.html) | Initial map of land use and cover classes. |
| Final Landscape | [Categorical Map Type](../types/Categorical-Map-Type.html) | Final map of land use and cover classes. |
| Ranges | [Weights Type](../types/Weights-Type.html) | Pre-defined intervals for each continuous or categorical spatial variable, for each transition, for which the Weights of Evidence coefficients will be calculated. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Fix Abnormal Weights | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, recalculates weights that would otherwise result in abnormal values, such as those arising from a division by zero. If false, those abnormal values are assumed to be zero. This is an advanced port. | No |
| Potential Transition Criteria | [Boolean Value Type](../types/Boolean-Value-Type.html) | Affects how a possible but unexecuted transition from class C to class P is identified. If true, any cell that transitions from C to some other class X (different from P) is considered a case where the C to P transition was possible but did not happen. If false, only a cell that stays in class C is considered such a case. This affects the analysis of concurrent transitions, and is an advanced port. | Yes |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Weights | [Weights Type](../types/Weights-Type.html) | Weights of Evidence coefficients obtained for the selected spatial variables, with respect to the given transition or transitions. |
| Report | [Table Type](../types/Table-Type.html) | Table with the same information reported to the message log during the calculation: for each transition, variable and range, the columns "Transition_From", "Transition_To", "Variable", "Range_Lower_Limit", "Range_Upper_Limit", "Possible_Transitions", "Executed_Transitions", "Weight_Coefficient", "Contrast", and "Significant". |

## Group

[Calibration](../Functor-List.html#calibration)

## Notes

For each range of a variable, this container compares how often the transition actually occurred within that range against how often it could have occurred, and expresses the difference as a weight; the difference between the weight for the presence of the range and the weight for its absence is the contrast, which reflects the overall strength of the association between that range and the transition. A contrast is considered statistically significant, with 95% probability, when its magnitude is larger than 1.96 times its standard deviation.

Reports an error if a spatial variable named in Ranges is not provided by a nested Name Map hook.

This method was adapted from Agterberg & Bonham-Carter (1990), Goodacre et al. (1993), and Bonham-Carter (1994).

**References**

Agterberg, F.P. and Bonham-Carter, G.F., 1990: Deriving weights of evidence from geoscience contour maps for the prediction of discrete events. XXII Int. Symposium AP-COM, 381-395.

Bonham-Carter, G., 1994: Geographic information systems for geoscientists: modelling with GIS. Pergamon, 398 pp.

Goodacre, C. M., Bonham-Carter, G. F., Agterberg, F. P., Wright, D. F., 1993: A statistical analysis of spatial association of seismicity with drainage patterns and magnetic anomalies in western Quebec. Tectonophysics, 217, 205-305.

## Internal Name

DetermineWeightsOfEvidenceCoefficients

## Usage examples

See practical examples of this functor in Lesson 18: Building a land-use and land-cover change simulation model
{% endraw %}
