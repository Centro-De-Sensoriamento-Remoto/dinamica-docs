---
title: "Create Elevation Graph"
nav_exclude: true
---
{% raw %}
# Create Elevation Graph

## Description

This functor creates the elevation patch graph from neighborhood information and patch properties.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Neighborhood Table | [Neighborhood Table Type](Neighborhood-Table-Type.html) | Defines spatial connectivity between elevation patches. Elevation patches are represented by their corresponding ids. |
| Properties | [Table Type](Table-Type.html) | Table of elevation patch properties, in the format "Patch_Id\*:real, Patch_Elevation:real, Patch_Area:real, Patch_Slope:real, Patch_Y:real, Patch_X:real". Patch_Y and Patch_X typically hold the coordinates of each patch's centroid. Neighboring patches, per Neighborhood Table, must have different elevation values in Properties, or this functor reports an error. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Elevation Graph | [Elevation Graph Type](Elevation-Graph-Type.html) | Elevation patch graph created from the neighborhood relationships and their properties. |

## Group

[Elevation Graph](Functor-List.html#elevation-graph)

## Notes

The elevation patch graph is a directed graph whose nodes correspond to the patches defined in Neighborhood Table, typically built from a terrain map. Its edges represent the adjacency and elevation-difference relationships between each patch and its neighbors: a node's parent nodes are its higher-elevation neighbors, and its child nodes are its lower-elevation neighbors. Neighboring patches must have different elevation values according to Properties, or this functor reports an error.

## Internal Name

CreateElevationGraph
{% endraw %}
