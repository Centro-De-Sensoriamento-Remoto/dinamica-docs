---
title: "Region Manager Type"
nav_exclude: true
---
{% raw %}
# Region Manager Type

A Region Manager defines a set of regions — for example, countries, states, or counties — derived from a categorical map whose class values identify each region, and provides the scoping context functors use to work with one region, or all regions, at a time.

[Region Manager](Region-Manager.html) creates one: given a `regions` categorical map and an optional `borderCells` padding (extra lines/columns added around each region), it exposes the resulting Region Manager as its own `regionManager` internal output to the functors nested inside it:

```
RegionManager regionMap 0 {{
    manager = regionManager;
    allRegions := GetAllRegionsInfo manager;
}};
```

From there, a family of functors work with an active Region Manager. [Region](Region.html) narrows scope to a single region — given a region ID and the enclosing Region Manager, both auto-bound, it re-exposes both to the functors nested inside it. [For Each Region](For-Each-Region.html) iterates over every region the enclosing Region Manager defines, exposing the current region's ID as its `step` internal output on each pass. [Get All Regions Info](Get-All-Regions-Info.html) and [Get Region Info](Get-Region-Info.html) retrieve boundary metadata for all regions at once, or one at a time; [Get All Regions Info](Get-All-Regions-Info.html)'s output table gives each region's line and column extent along with its four coordinate boundaries. [Regionalize Map](Regionalize-Map.html) and [Regionalize Categorical Map](Regionalize-Categorical-Map.html) split a global map into per-region pieces; [Regional Map](Regional-Map.html) and [Regional Categorical Map](Regional-Categorical-Map.html) tag and collect those per-region fragments as they're produced, under a shared name; [Merge Regional Maps](Merge-Regional-Maps.html) and [Merge Regional Categorical Maps](Merge-Regional-Categorical-Maps.html) reassemble the tagged fragments back into one global mosaic map.

## GUI Editor

Region Manager Type has no editor. A value can only come from a [Region Manager](Region-Manager.html) container, or be passed through by a [Region](Region.html) or [For Each Region](For-Each-Region.html) container — never typed in directly.

## EGO Script

For the same reason, Region Manager Type has no literal constant syntax in [EGO Script](EGO-Script.html) — see [Constants](EGO-Script.html#constants). [Region Manager Value](Region-Manager-Value.html) exists purely to relay a Region Manager value between two functors, the same role [Struct](Struct-Type.html)'s carrier functor plays for structs; its own input is likewise non-editable and auto-binds to the enclosing container's `regionManager` by default.

## Automatic Conversions

None — Region Manager Type converts to or from no other type.

See [Type System](Type-System.html) for the complete conversion reference across all types.
{% endraw %}
