---
title: "Get Elevation Graph Tops And Bases"
nav_order: 7
parent: "Elevation Graph Functors"
grand_parent: "Functor List"
---
{% raw %}
# Get Elevation Graph Tops And Bases

## Description

This functor retrieves the patches that correspond to local maxima and minima of an elevation patch graph.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Elevation Graph | [Elevation Graph Type](../types/Elevation-Graph-Type.html) | Elevation patch graph created from neighborhood relationships and their properties. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Tops | [Table Type](../types/Table-Type.html) | Properties of the elevation patches corresponding to local maxima, in the format "Top_Id\*:real, Top_Elevation:real, Top_Area:real, Top_Slope:real, Top_Y:real, Top_X:real, Top_Children:real". |
| Bases | [Table Type](../types/Table-Type.html) | Properties of the elevation patches corresponding to local minima, in the format "Base_Id\*:real, Base_Elevation:real, Base_Area:real, Base_Combined_Area:real, Base_Slope:real, Base_Y:real, Base_X:real, Base_Parents:real". |

## Group

[Elevation Graph](../Functor-List.html#elevation-graph)

## Notes

None.

## Internal Name

GetElevationGraphTopsAndBases
{% endraw %}
