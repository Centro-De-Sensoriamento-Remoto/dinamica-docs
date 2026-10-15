---
title: "Calc Interaction Potential Map"
nav_order: 13
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calc Interaction Potential Map

## Description

This functor generates an interaction potential map: a gravitational model between null cells and non-null cells, whose values represent the gravitational masses. The denominator is a function of the distance to the non-null cells, raised to an exponent that acts as a friction coefficient.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Source | [Map Type](../types/Map-Type.html) | Map whose non-null cells correspond to source features. The values of the non-null cells are used as the gravity factor. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Mask | [Map Type](../types/Map-Type.html) | Map whose null cells mask the interaction-potential calculation. | .none |
| Distance Decay Exponent | [Real Value Type](../types/Real-Value-Type.html) | Exponent used by the decay function applied to the distance from each point to the source features, when calculating the total interaction potential. | 2 |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Cell type of the interaction potential map. The calculated potentials are converted to this type, which must be compatible with the values in Source, or this functor reports an error during execution. | Signed 32 Bit Integer |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Null value of the interaction potential map. | .default |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Interaction Potential | [Map Type](../types/Map-Type.html) | Map of the total interaction potential of the source features. Interaction Potential has the same dimensions as Source. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

Total interaction potentials are calculated as real values and converted to the interaction potential map's representable range, where 0 maps to 0 and the greatest potential maps to the greatest value the cell type can represent. No conversion is performed when the interaction potential map's cell type is a floating-point type; the values are kept in their original range in that case.

Mask does not affect which source-feature cells are collected, only the final calculation: a source feature located outside the area indicated by Mask still influences the result.

The potential of each cell is the sum, over every source feature, of the feature's value divided by the distance between the current cell and the feature, raised to Distance Decay Exponent.

## Internal Name

CalcInteractionPotentialMap
{% endraw %}
