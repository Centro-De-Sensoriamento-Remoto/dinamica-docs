---
title: "Calc Reciprocal Similarity Map"
nav_order: 1
parent: "Validation Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calc Reciprocal Similarity Map

## Description

Calculates fuzzy similarity indices between two categorical maps. Instead of comparing cells one-to-one, each cell is compared against a neighborhood of cells around the corresponding location in the other map, following the method described by Hagen (2003), "Fuzzy set approach to assessing similarity of categorical maps." This produces two directional similarity maps: how well the first map matches the neighborhood of the second, and how well the second matches the neighborhood of the first.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| First Map | [Categorical Map Type](../types/Categorical-Map-Type.html) | A map consisting of classes or categories. Its format is used to determine the format of the resulting similarity maps. |
| Second Map | [Categorical Map Type](../types/Categorical-Map-Type.html) | A map consisting of classes or categories. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Window Size | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Window size, with equal number of lines and columns, used to compute the similarities. Only odd numbers are acceptable. | 5 |
| Use Exponential Decay | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, the similarity is calculated using an exponential decay function truncated by the window size. Otherwise, a constant function is used, in which the similarity is 1 if a matching cell is found within the search window, and zero if not. | Yes |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Cell type of the similarity maps. The calculated similarities, originally in the \[0, 1\] range, are converted to this type. If Cell Type is a floating point type, no conversion is performed and the values are kept in the original \[0, 1\] range. | Signed 8 Bit Integer |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Null value of the similarity maps. | Provided automatically |
| Exponential Decay Divisor | [Real Value Type](../types/Real-Value-Type.html) | Value used to attenuate the distance in the exponential decay function. This value must be greater than zero, and should be increased when Use Exponential Decay is set to a wider window. This is an advanced port. | 2 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| First Similarity | [Map Type](../types/Map-Type.html) | Map showing the degree of spatial match from the first to the second input map. Similarity varies from zero (no match) to 1 (perfect match) within the specified window size. |
| First Mean | [Real Value Type](../types/Real-Value-Type.html) | The mean similarity index, for the given window size, comparing the first map to the second. |
| Second Similarity | [Map Type](../types/Map-Type.html) | Map showing the degree of spatial match from the second to the first input map. Similarity varies from zero (no match) to 1 (perfect match) within the specified window size. |
| Second Mean | [Real Value Type](../types/Real-Value-Type.html) | The mean similarity index, for the given window size, comparing the second map to the first. |

## Group

[Validation](../Functor-List.html#validation)

## Notes

Comparing two maps cell by cell tends to underestimate their spatial agreement, since two maps can show a similar spatial pattern without their cells lining up exactly. This functor addresses that by comparing each cell against a neighborhood of cells in the other map rather than against a single corresponding cell.

Because the comparison is directional, the similarity from the first map to the second is generally not the same as the similarity from the second map to the first. It is recommended to compare both directions and consider the lower of the two, since random maps tend to score higher than expected.

When Use Exponential Decay is enabled, the contribution of a neighboring cell to the similarity score decays exponentially with its distance from the window center, following S = 1/2^(d/A), where d is the distance from the center and A is the Exponential Decay Divisor. A smaller Exponential Decay Divisor makes the similarity value fall off more sharply with distance, while a larger divisor spreads the decay out so that farther cells within the window still contribute meaningfully to the score. When Use Exponential Decay is false, a constant function is used instead: any matching cell found within the window contributes fully to the similarity, regardless of its distance from the center.

This method should not be applied directly to simulation maps. Compute the maps of changes first and compare those instead, since simulation maps typically contain a large proportion of unchanged background cells that would inflate the similarity score without reflecting the simulation's actual accuracy.

If the map used to control the similarity calculation contains only null cells, the resulting mean similarity is defined as 1.

Reports an error if Window Size is not an odd number.

Reports an error if Exponential Decay Divisor is not greater than zero.

Reports an error if Null Value is not compatible with Cell Type.

Reports a warning if Cell Type could degrade performance.

**References**

Costanza, R., 1989. Model goodness of fit: a multiple resolution procedure. Ecological Modelling, 47, 199-215.

Goodacre, C. M., Bonham-Carter, G. F., Agterberg, F. P., Wright, D. F., 1993. A statistical analysis of spatial association of seismicity with drainage patterns and magnetic anomalies in western Quebec. Tectonophysics, 217, 205-305.

Hagen, A., 2003. Fuzzy set approach to assessing similarity of categorical maps. International Journal of Geographical Information Science, 17(3), 235-249.

Pontius, R.G. Jr., 2002. Statistical Methods to Partition Effects of Quantity and Location During Comparison of Categorical Maps at Multiple Resolutions. Photogrammetric Engineering & Remote Sensing 68(10), 1041-1049.

Power, C., Simms, A., White, R., 2001. Hierarchical fuzzy pattern matching for the regional comparison of Land Use Maps. International Journal of Geographical Information Science 15(1), 77-100.

## Internal Name

CalcReciprocalSimilarityMap

## Usage examples

See practical examples of this functor in [Lesson 18: Building a land-use and land-cover change simulation model](../guidebook/Land-Use-Change-Simulation-Model.html) of the Guidebook.
{% endraw %}
