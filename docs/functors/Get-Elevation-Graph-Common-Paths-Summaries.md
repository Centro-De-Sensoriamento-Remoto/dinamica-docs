---
title: "Get Elevation Graph Common Paths Summaries"
nav_order: 5
parent: "Elevation Graph Functors"
grand_parent: "Functor List"
redirect_from:
  - /Get-Elevation-Graph-Common-Paths-Summaries.html
---
{% raw %}
# Get Elevation Graph Common Paths Summaries

## Description

This functor retrieves the summaries of the elevation patches common between the paths of pseudo-top pairs and their respective bases.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Elevation Graph | [Elevation Graph Type](../types/Elevation-Graph-Type.html) | Elevation patch graph created from neighborhood relationships and their properties. |
| Pseudo Top Pairs For Common Paths | [Base Table Type](../types/Base-Table-Type.html) | Pairs of elevation patch ids for which the nodes common to their respective paths, from top to base, are retrieved. As a table, it must have the format "Top_Id1\*:real, Top_Id2\*:real, \_\_unused\_\_" (the value column is ignored); as a lookup table, its keys and their associated values represent the pairs of patch ids. A pair naming a patch id not defined in Elevation Graph is ignored. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Also Retrieve Lowest Nodes | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, retrieves the id of both the highest and the lowest common elevation patch among those in the common paths between the pseudo-tops and their bases. Otherwise, only the highest common elevation patch's id is retrieved, and the output column for the lowest one is filled with -9999. | Yes |
| Pseudo Bases | [Base Table Type](../types/Base-Table-Type.html) | Table whose keys are the ids of elevation patches that can be treated as bases of the graph. For each top in Pseudo Top Pairs For Common Paths, if this table is not provided or the top's id is not present in it, the search uses the regular criterion to decide whether a node is a base; if the id is present, that patch is accepted as a base once reached, and none of its child nodes are analyzed further. | .none |
| Maximum Nodes | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Maximum number of nodes that can be visited between a top elevation patch and its corresponding base. A top exceeding this quantity is ignored. 0 means the number of visited nodes is unlimited. This is an advanced port. | 0 |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Common Path Summaries | [Table Type](../types/Table-Type.html) | Table of information about the elevation patches common between the paths of each pseudo-top pair and their bases, in the format "Top_Id1\*:real, Top_Id2\*:real, Highest_Path_Id:real, Lowest_Path_Id:real". A pair ignored from Pseudo Top Pairs For Common Paths has no corresponding entry. If Also Retrieve Lowest Nodes is false, Lowest_Path_Id is filled with -9999. |

## Group

[Elevation Graph](../Functor-List.html#elevation-graph)

## Notes

Retrieves information about the elevation patches common between the paths of pairs of pseudo-tops and their respective bases, considering either all reachable bases or only the lowest-elevation one for each top, using the same base-search criteria as Find Elevation Graph Bases and Find Elevation Graph Paths.

## Internal Name

GetElevationGraphCommonPathsSummaries
{% endraw %}
