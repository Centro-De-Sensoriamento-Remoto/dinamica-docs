---
title: "Find Elevation Graph Paths"
nav_exclude: true
---
{% raw %}
# Find Elevation Graph Paths

## Description

This functor retrieves the ids of the elevation patches along the paths between the specified pseudo-tops and their respective bases.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Elevation Graph | [Elevation Graph Type](Elevation-Graph-Type.html) | Elevation patch graph created from neighborhood relationships and their properties. |
| Pseudo Tops | [Base Table Type](Base-Table-Type.html) | Table or lookup table listing the top elevation patches for which the path patches down to the bases are retrieved. These can be any patches in the elevation patch tree, not necessarily top-level patches. The table's keys are the ids of the top patches; the values associated with each key are ignored. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Search For All Bases | [Boolean Value Type](Boolean-Value-Type.html) | If true, the elevation patches of the paths to every reachable base from each specified top are retrieved. Otherwise, only the elevation patches of the path to the lowest-elevation base are retrieved. | No |
| Pseudo Bases | [Base Table Type](Base-Table-Type.html) | Table whose keys are the ids of elevation patches that can be treated as bases of the graph. For each top in Pseudo Tops, if this table is not provided or the top's id is not present in it, the search uses the regular criterion to decide whether a node is a base; if the id is present, that patch is accepted as a base once reached, and none of its child nodes are analyzed further. | .none |
| Minimum Elevations | [Lookup Table Type](Lookup-Table-Type.html) | Lookup table of elevation patches and the minimum elevation of patches that can be retrieved along the paths between that patch and its bases. For each top in Pseudo Tops, if this table is not provided or the top's id is not present in it, the search treats any elevation as valid; if the id is present, patches with a lower elevation than the associated value are ignored, and a patch is also treated as a base of the graph if all its children are ignored this way. | .none |
| Also Search Parents | [Boolean Value Type](Boolean-Value-Type.html) | If true, the search also follows the parent elevation patches of the patches it visits: for each patch analyzed, paths are expanded toward both its child patches and its parent patches. This flag is meaningful only when Search For All Bases is true. | No |
| Maximum Nodes | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Maximum number of nodes that can be visited between a top elevation patch and its corresponding base. A top exceeding this quantity is ignored. 0 means the number of visited nodes is unlimited. This is an advanced port. | 0 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Path Relations | [Table Type](Table-Type.html) | Table of the elevation patches representing the path between each top and its corresponding base, in the format "Top_Id\*:real, Path_Id\*:real, Index:real". When Search For All Bases is true, Path_Id lists the elevation patches of the paths with no particular ordering; otherwise, Path_Id is ordered from the patch corresponding to the top down to the found base. |
| All Path Patches | [Table Type](Table-Type.html) | Table of the elevation patches that are part of the path between each top and base, in the format "Row_Index\*:real, Top_Id:real, Path_Id:real, Path_Index:real". When Search For All Bases is true, Path_Id lists the elevation patches of the paths with no particular ordering; otherwise, Path_Id is ordered from the patch corresponding to the top down to the found base. |

## Group

[Elevation Graph](Functor-List.html#elevation-graph)

## Notes

Retrieves the ids of the elevation patches along the paths between the specified pseudo-tops and their respective bases, considering either all reachable bases or only the lowest-elevation one, depending on Search For All Bases.

## Internal Name

FindElevationGraphPaths
{% endraw %}
