---
title: "Calc Cumulative Flow Map"
nav_order: 5
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calc Cumulative Flow Map

## Description

Calculates a cumulative flow map from a flow direction map, an optional flow weight map, and an optional flow partition map. Each cell of the resulting map holds the total flow it receives, directly or indirectly, from its neighbors.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Flow Directions | [Map Type](../types/Map-Type.html) | Map of possible flow directions between cells. Can hold either a single direction or multiple directions per cell. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Weight | [Map Type](../types/Map-Type.html) | Weight of the flow, that is, how much a cell's flow contributes to the flow of the cell it flows into. When not provided, every cell is treated as having a weight of 1. | None |
| Flow Partition | [Map Type](../types/Map-Type.html) | For a multidirectional flow, indicates how much of a cell's flow goes to each neighbor it flows into. Must have at least 8 layers, one for each neighbor direction: layers 5, 6, and 7 for the neighbors above; layers 4 and 0 for the neighbors to the left and right; and layers 3, 2, and 1 for the neighbors below. When not provided, flow is divided evenly among the cells it flows into. | None |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Cell type of the output map. | Signed 32 Bit Integer |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Null value of the output map. Cannot be zero. | Provided automatically |
| Accumulation Is Sparse | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, forces the accumulated flow map to be stored as a sparse raster, which stores only non-null cells, trading faster access for lower memory use. This is an advanced port. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Flow Accumulation | [Map Type](../types/Map-Type.html) | Map of accumulated flow, where each cell holds all the flow it receives directly and indirectly from its neighbors. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

The elevation map used to build Flow Directions must be the same one used by [Calc Flow Direction Map](Calc-Flow-Direction-Map.html) to produce it; see that functor for more on the flow direction map.

When a cell points to its neighbor on a given side, the functor reads that neighbor's share of the flow from the Flow Partition layer assigned to that side, according to the following layout:

|   |   |   |
| --- | --- | --- |
| Layer 5 | Layer 6 | Layer 7 |
| Layer 4 |  | Layer 0 |
| Layer 3 | Layer 2 | Layer 1 |

For example, a cell pointing to its left neighbor reads layer 4 at the same position. If Flow Partition is not provided, the flow is evenly divided among the possible branches.

Flow Weight defines how much a cell contributes to the overall accumulated flow. If it is not provided, the functor assumes a weight of 1 for every cell.

Raises an error if Null Value is zero.

## Internal Name

CalcCumulativeFlowMap
{% endraw %}
