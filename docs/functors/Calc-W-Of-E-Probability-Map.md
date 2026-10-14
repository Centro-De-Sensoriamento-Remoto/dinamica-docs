---
title: "Calc W Of E Probability Map"
nav_order: 17
parent: "Map Algebra Functors"
grand_parent: "Functor List"
redirect_from:
  - /Calc-W-Of-E-Probability-Map.html
---
{% raw %}
# Calc W Of E Probability Map

## Description

Container that calculates a spatial probability map for a set of transitions, from a landscape map and a set of Weights of Evidence coefficients.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Landscape | [Categorical Map Type](../types/Categorical-Map-Type.html) | Map of classes or categories. |
| Weights | [Weights Type](../types/Weights-Type.html) | Weights of Evidence coefficients. |
| Transitions | [Transition Set Type](../types/Transition-Set-Type.html) | Transitions for which probabilities are calculated. Each transition produces a layer named `probability_i_to_j`, where i and j are the values of its origin and destination categories. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Cell type of the calculated probability map. Its cells are converted to this type. | Unsigned 8 Bit Integer |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Null value of the calculated probability map. | .default |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Probabilities | [Map Type](../types/Map-Type.html) | Map of the probabilities calculated from the Weights of Evidence coefficients. Probabilities has the same dimensions as Landscape. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

This functor is also known by the alias "CalcWeightsOfEvidence".

Name Map functors placed inside this container register additional variables that Weights' coefficients can refer to, alongside Landscape.

Probabilities are calculated in the range \[0, 1\] and converted to the calculated probability map's representable range, where 0 maps to 0 and 1 maps to the greatest value the cell type can represent. No conversion is performed when the calculated probability map's cell type is a floating-point type; the values are kept in their original \[0, 1\] range in that case.

Variable cells are always read as real values, even when the underlying map stores integers.

Cells where the transition being calculated cannot occur are set to the null value in the calculated probability map.

Variables whose cells equal the null value are ignored in the probability calculation.

## Internal Name

CalcWOfEProbabilityMap
{% endraw %}
