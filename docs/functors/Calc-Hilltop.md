---
title: "Calc Hilltop"
nav_order: 11
parent: "Map Algebra Functors"
grand_parent: "Functor List"
redirect_from:
  - /Calc-Hilltop.html
---
{% raw %}
# Calc Hilltop

## Description

Identifies hilltop and plateau permanent protection areas from an elevation map that has already been segmented into hypsometric (elevation-band) patches. Each patch is treated as the content of one elevation contour band, and is expected to carry a unique identifier that links it to its mean elevation in Elevation Table, and optionally to its mean slope and its area in Slope Table and Area Table.

For each local maximum found in the elevation patches, the functor walks downhill along neighboring patches until it reaches a base: either a local minimum, or, when Hill Base Slope is set, the nearest sufficiently flat patch encountered along the way, whichever comes first. The vertical distance between that top and its base is the hill's height, and the steepest line connecting them determines its dip slope. A top only becomes a classified hill when its height falls between Hill Minimum Height and Hill Maximum Height and its dip slope is at least Hill Minimum Slope; hilltops separated by less than Least Distance are grouped and share the same base for this classification. Once a hill is classified, the protected area extends from its top down to the fraction of its height given by Hillside Fraction. A flat top whose area is at least Plateau Minimum Area, whose own slope does not exceed Plateau Maximum Slope, and that is bordered by an escarpment of at least Escarpment Minimum Slope is instead classified as a plateau.

The numeric defaults for Hill Minimum Height, Hill Maximum Height, Hill Base Slope, Hill Minimum Slope, Plateau Minimum Area, Plateau Maximum Slope, Escarpment Minimum Slope, Least Distance, and Hillside Fraction reproduce the thresholds used in Brazilian environmental legislation (CONAMA Resolution No. 303/2002) to define hills, mountains, plateaus, and their associated permanent protection areas; they can be overridden to apply a different classification criterion.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Elevation Patches | [Map Type](../types/Map-Type.html) | Map of elevation patches. Each patch is a contiguous group of cells falling within one elevation band, and carries a unique identifier. |
| Elevation Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | Relates each patch identifier in Elevation Patches to the mean elevation of its non-null cells. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Slope Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | Relates each patch identifier to the mean slope of its non-null cells. | .none |
| Area Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | Relates each patch identifier to the total area of its non-null cells. | .none |
| Hill Minimum Height | [Real Value Type](../types/Real-Value-Type.html) | Least height, measured from base to top, for an elevation to be classified as a hill. | 50.0 |
| Hill Maximum Height | [Real Value Type](../types/Real-Value-Type.html) | Height above which an elevation is no longer classified as a hill, becoming a mountain instead. | 300.0 |
| Hill Base Slope | [Real Value Type](../types/Real-Value-Type.html) | Maximum mean slope a patch may have to be treated as a flat area, and therefore as an alternative base for the hill, instead of using the nearest local minimum. | 5.72957795 (degrees) |
| Hill Minimum Slope | [Real Value Type](../types/Real-Value-Type.html) | Least slope, measured along the steepest line from top to base, for an elevation to be classified as a hill. | 17.1887339 (degrees) |
| Plateau Minimum Area | [Real Value Type](../types/Real-Value-Type.html) | Least top area for an elevation to be classified as a plateau. | 10.0 (hectares) |
| Plateau Maximum Slope | [Real Value Type](../types/Real-Value-Type.html) | Maximum mean slope a top may have to be classified as a plateau. | 5.72957795 (degrees) |
| Escarpment Minimum Slope | [Real Value Type](../types/Real-Value-Type.html) | Least mean slope a bordering patch must have to be considered an escarpment, which a plateau's top must be surrounded by. | 45.0 (degrees) |
| Least Distance | [Real Value Type](../types/Real-Value-Type.html) | Least distance between hilltops below which the hilltops are grouped and share the same base for classification purposes. | 500.0 |
| Hillside Fraction | [Real Value Type](../types/Real-Value-Type.html) | Fraction of a hill's height, measured down from its top, that is marked as a protected area. This is an advanced port. | 0.67 |
| Classify Upper Areas | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, extends the protected-area classification to areas that lie above and adjoin an already-classified protected area but that would not, on their own, meet the classification criteria. This is an advanced port. | Yes |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Hilltop | [Lookup Table Type](../types/Lookup-Table-Type.html) | Table of elevation-patch identifiers classified as permanent protection areas, together with their elevation. |
| Hills Height | [Lookup Table Type](../types/Lookup-Table-Type.html) | Table of hill identifiers and their height, i.e., the elevation difference between a hill's top and its base. |
| Hill Dip Slope | [Lookup Table Type](../types/Lookup-Table-Type.html) | Table of hill identifiers and their dip slope, in degrees, obtained from the ratio between the hill's height and the horizontal distance from its top to its nearest base. |
| Plateaus | [Lookup Table Type](../types/Lookup-Table-Type.html) | Table of top identifiers classified as plateaus. Note that only part of a plateau's top, not its whole area, is classified as a protected area. |
| Local Maxima | [Lookup Table Type](../types/Lookup-Table-Type.html) | Table of patch identifiers and elevations corresponding to local maxima. |
| Local Minima | [Lookup Table Type](../types/Lookup-Table-Type.html) | Table of patch identifiers and elevations corresponding to local minima. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

Vertically normalizing the elevation map before segmenting it into patches is recommended: doing so attenuates noise, reduces the number of resulting patches, and makes the classification more representative, which also improves performance.

Raises an error if any of Hill Minimum Height, Hill Maximum Height, Hill Base Slope, Hill Minimum Slope, Plateau Minimum Area, Plateau Maximum Slope, Escarpment Minimum Slope, or Least Distance is set to a negative value.

## Internal Name

CalcHilltop
{% endraw %}
