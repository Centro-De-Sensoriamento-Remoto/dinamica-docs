---
title: "For Each Region"
nav_exclude: true
---
{% raw %}
# For Each Region

## Description

This container creates and manages the regions identified by a categorical map, and executes the functors it contains once for each region. Each execution is called a step. While a step runs, the container makes the region manager available to its contents through the internal output port Region Manager, and the identifier of the region currently being processed through the internal output port Step.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Regions | [Categorical Map Type](Categorical-Map-Type.html) | Map of subregions, such as countries, states, or counties. The cells that make up a region do not need to be contiguous. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Border Cells | [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html) | Number of lines and columns added as an extra border around each region in its regional maps. | 0 |
| Sequence Input | [None Type](None-Type.html) | Ensures that the functor connected to this port finishes executing before this container starts. | None |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Sequence Output | [None Type](None-Type.html) | Connect this port to another container's Sequence Input to make this container finish executing before that other container starts. |

## Internal Outputs

| Name | Type | Description |
| --- | --- | --- |
| Region Manager | [Region Manager Type](Region-Manager-Type.html) | The region manager holding the regions being iterated. |
| Step | [Integer Value Type](Integer-Value-Type.html) | Identifier of the region currently being processed. |

## Group

[Control](Functor-List.html#control)

## Notes

When there is no dependency between regions, this container may process several of them at the same time instead of one after another.

[Get Region Info](Get-Region-Info.html), [Regionalize Map](Regionalize-Map.html), [Regionalize Categorical Map](Regionalize-Categorical-Map.html), and [Region](Region.html) placed directly inside this container read the current region automatically through their own inputs, with no need to connect Region Manager or Step explicitly.

The region manager this container exposes only supports splitting a map into its regions — it cannot be used to merge regional maps back together. Placing [Merge Regional Maps](Merge-Regional-Maps.html) or [Merge Regional Categorical Maps](Merge-Regional-Categorical-Maps.html) inside this container, reading from its region manager, causes the model to report an error. Placing [Regional Map](Regional-Map.html) or [Regional Categorical Map](Regional-Categorical-Map.html) here has no effect, since there is nothing for them to register a map against.

When a result produced by the contained functors is used outside the container, connect a matching [junction](Functor-List.html#junction) after the container, so a value still reaches the rest of the model if there are no regions to process.

## Internal Name

ForEachRegion
{% endraw %}
