---
title: "Calc Kernel Map"
nav_order: 2
parent: "Statistics Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calc Kernel Map

## Description

This functor calculates the kernel density of an event map representing a point pattern.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Events | [Map Type](../types/Map-Type.html) | Map showing the location of events. Events are represented by non-null cells, indicating the number of occurrences on the cell. |
| Bandwidth | [Real Value Type](../types/Real-Value-Type.html) | Radius, in meters, of the disc centered on each cell within which events contribute to the kernel estimate. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Mask | [Map Type](../types/Map-Type.html) | Map whose null cells mask the kernel calculation. | .none |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Null value of the calculated kernel map. | .default |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Kernel Map | [Map Type](../types/Map-Type.html) | Map showing the kernel density estimate for each cell. |

## Group

[Statistics](../Functor-List.html#statistics)

## Notes

Kernel density estimation produces a continuous estimate of the spatial intensity of a point pattern, making it possible to explore hotspots and other patterns in the distribution of events even when overlapping points would make visual inspection misleading.

Increasing Bandwidth spreads the density estimate over a wider area around each cluster: with a large bandwidth the density appears flatter and local features are obscured, while a small bandwidth reveals local hotspot patterns more sharply.

The kernel function used is the quartic function k(h) = (3/PI)\*(1-h^2)^2.

**References**

Bailey, T. and Gatrell, A., 1995: Interactive Spatial Data Analysis. Longman, Harlow.

Silverman, W., 1986: Density estimation. Chapman and Hall, London.

## Internal Name

CalcKernelMap
{% endraw %}
