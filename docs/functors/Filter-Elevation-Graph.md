---
title: "Filter Elevation Graph"
nav_order: 2
parent: "Elevation Graph Functors"
grand_parent: "Functor List"
redirect_from:
  - /Filter-Elevation-Graph.html
---
{% raw %}
# Filter Elevation Graph

## Description

This functor filters patches from an elevation patch graph, producing a new graph containing only the patches whose ids are listed in Filtered Patches.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Elevation Graph | [Elevation Graph Type](../types/Elevation-Graph-Type.html) | Elevation patch graph created from neighborhood relationships and their properties. |
| Filtered Patches | [Base Table Type](../types/Base-Table-Type.html) | Table or lookup table whose keys are the ids of the patches, from Elevation Graph, that will be kept in the resulting graph. The values associated with each key are ignored. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Filtered Elevation Graph | [Elevation Graph Type](../types/Elevation-Graph-Type.html) | Elevation patch graph containing only the patches kept by the filtering. |

## Group

[Elevation Graph](../Functor-List.html#elevation-graph)

## Notes

The nodes corresponding to the removed elevation patches have their parent and child node information transferred to the nodes that are kept.

## Internal Name

FilterElevationGraph
{% endraw %}
