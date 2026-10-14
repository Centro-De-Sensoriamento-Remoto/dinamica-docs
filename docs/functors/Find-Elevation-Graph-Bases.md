---
title: "Find Elevation Graph Bases"
nav_order: 3
parent: "Elevation Graph Functors"
grand_parent: "Functor List"
redirect_from:
  - /Find-Elevation-Graph-Bases.html
---
{% raw %}
# Find Elevation Graph Bases

## Description

This functor retrieves the ids of the elevation patches that correspond to the bases of the paths from the specified pseudo-tops.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Elevation Graph | [Elevation Graph Type](../types/Elevation-Graph-Type.html) | Elevation patch graph created from neighborhood relationships and their properties. |
| Pseudo Tops | [Base Table Type](../types/Base-Table-Type.html) | Table or lookup table listing the top elevation patches for which the base patches are retrieved. These can be any patches in the elevation patch tree, not necessarily top-level patches. The table's keys are the ids of the top patches; the values associated with each key are ignored. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Search For All Bases | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, the elevation patches of every reachable base from each specified top are retrieved. Otherwise, only the elevation patch of the lowest-elevation base is retrieved. | No |
| Pseudo Bases | [Base Table Type](../types/Base-Table-Type.html) | Table whose keys are the ids of elevation patches that can be treated as bases of the graph. For each top in Pseudo Tops, if this table is not provided or the top's id is not present in it, the search uses the regular criterion to decide whether a node is a base; if the id is present, that patch is accepted as a base once reached, and none of its child nodes are analyzed further. | .none |
| Minimum Elevations | [Lookup Table Type](../types/Lookup-Table-Type.html) | Lookup table of elevation patches and the minimum elevation of patches that can be retrieved along the paths between that patch and its bases. For each top in Pseudo Tops, if this table is not provided or the top's id is not present in it, the search treats any elevation as valid; if the id is present, patches with a lower elevation than the associated value are ignored, and a patch is also treated as a base of the graph if all its children are ignored this way. | .none |
| Maximum Nodes | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Maximum number of nodes that can be visited between a top elevation patch and its corresponding base. A top exceeding this quantity is ignored. 0 means the number of visited nodes is unlimited. This is an advanced port. | 0 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Base Relations | [Table Type](../types/Table-Type.html) | Table of the elevation patches representing the base corresponding to each top, in the format "Top_Id\*:real, Base_Id\*:real, Index:real". |
| All Base Patches | [Table Type](../types/Table-Type.html) | Table of the elevation patches representing the bases corresponding to each top, without any specific structure, in the format "Row_Index\*:real, Top_Id:real, Base_Id:real, Base_Index:real". |

## Group

[Elevation Graph](../Functor-List.html#elevation-graph)

## Notes

Retrieves the ids of the elevation patches corresponding to the bases of the paths from the specified pseudo-tops, considering either all reachable bases or only the lowest-elevation one, depending on Search For All Bases.

## Internal Name

FindElevationGraphBases
{% endraw %}
