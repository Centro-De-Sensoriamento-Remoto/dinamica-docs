---
title: "Get Elevation Graph Info"
nav_order: 6
parent: "Elevation Graph Functors"
grand_parent: "Functor List"
---
{% raw %}
# Get Elevation Graph Info

## Description

This functor retrieves complete information from an elevation patch graph, including each patch's own properties and its relationship with neighboring patches.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Elevation Graph | [Elevation Graph Type](../types/Elevation-Graph-Type.html) | Elevation patch graph created from neighborhood relationships and their properties. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Also Retrieve Parent Info | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, Parent Patch Info is filled with the relationships of each patch's neighboring patches that are higher than it. If false, that table is left empty. | No |
| Also Retrieve Child Info | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, Child Patch Info is filled with the relationships of each patch's neighboring patches that are lower than it. If false, that table is left empty. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Patch Info | [Table Type](../types/Table-Type.html) | Table of property relationships for each elevation patch, in the format "Patch_Id\*:real, Patch_Elevation:real, Patch_Area:real, Patch_Combined_Area:real, Patch_Slope:real, Patch_Y:real, Patch_X:real, Patch_Parents:real, Patch_Children:real". |
| Parent Patch Info | [Table Type](../types/Table-Type.html) | Table of the relationships between each elevation patch and its neighboring patches that are higher than it, in the format "Patch_Id\*:real, Parent_Id\*:real, Index:real". Empty when Also Retrieve Parent Info is false. |
| Child Patch Info | [Table Type](../types/Table-Type.html) | Table of the relationships between each elevation patch and its neighboring patches that are lower than it, in the format "Patch_Id\*:real, Child_Id\*:real, Index:real". Empty when Also Retrieve Child Info is false. |

## Group

[Elevation Graph](../Functor-List.html#elevation-graph)

## Notes

None.

## Internal Name

GetElevationGraphInfo
{% endraw %}
