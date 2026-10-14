---
title: "Working with Subregions Using Region Manager"
nav_order: 14
---
{% raw %}
# Working with Subregions Using Region Manager

## Overview

Region Manager exists for three distinct reasons, and it's worth being clear about which one applies before reaching for it:

- **The computation itself requires region-specific inputs.** [Patcher](Patcher.html) and [Expander](Expander.html) each take exactly one [Change Matrix](Change-Matrix-Type.html) and one [Transition Function Parameter Matrix](Transition-Function-Parameter-Matrix-Type.html) per call. If those change quantities or patch parameters genuinely differ by region, there's no single call that can express that — running once per region, with region-specific parameters, is the only way to get that behavior.
- **The map is too large to process as one raster.** Splitting into regions keeps each piece a manageable size to work with, independent of whether the calculation itself cares about regions at all.
- **A windowed or accumulating calculation would be distorted at a hard-clipped edge.** Anything that looks beyond the current cell — a cost surface, a distance calculation, a neighborhood statistic — needs \*real\* context past a region's boundary, not just reserved space for it. `borderCells` reserves that extra space around each region, but by default it's filled with null, not real data — getting real values into it also requires `keepNonRegionCells: Yes` on the [Regionalize Map](Regionalize-Map.html) / [Regionalize Categorical Map](Regionalize-Categorical-Map.html) call that produces the regional map.

The first case is structural: some functors simply can't vary their parameters by region any other way. The second and third are about how a computation is carried out, not what it computes — the same result could, in principle, come from one call over the whole map, if size or edge effects weren't a concern.

Whichever reason applies, the mechanics are the same: define the regions once, from a categorical map whose class values are the boundaries, and everything downstream — reading metadata, narrowing to one region, splitting a map into pieces, and merging the pieces back — works against that single definition. The running example through this page is the first case: running [Patcher](Patcher.html) with a different change matrix and transition function parameter matrix per region.

## Defining regions

[Region Manager](Region-Manager.html) is the container everything else on this page depends on.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `regions` | Input | Categorical Map | Yes | Map of subregions, e.g., countries, states, counties, etc. |
| `borderCells` | Input | Non Negative Integer Value | No, default 0 | Number of lines and columns used to create an additional border around each region. |
| `regionManager` | Internal Output | Region Manager | — | The region manager, exposed to functors nested inside the container. |

A nonzero `borderCells` matters here too: [Patcher](Patcher.html)'s own neighborhood search window (3×3 cells by default) means a region's edge cells still need real context beyond the hard-clipped boundary. `borderCells` alone only reserves that space, though — making it real data instead of null also requires `keepNonRegionCells: Yes` when the region is split out, covered in [Splitting a global map into regions](#splitting-a-global-map-into-regions) below.

**Example** — the shell everything else in this page builds on:

```
landscapeMap := LoadCategoricalMap "c:/data/landscape.tif" .none .default 0;
probabilitiesMap := LoadMap "c:/data/probabilities.tif";
regionsMap := LoadCategoricalMap "c:/data/regions.tif" .none .default 0;

RegionManager regionsMap 5 {{
    // everything below is added here, one section at a time
}};
```

## Reading region metadata

[Get All Regions Info](Get-All-Regions-Info.html) returns boundary details for every region at once, as a table:

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `regionManager` | Input | Region Manager | No, auto-bound | The region manager to read from. |
| `regionsInfo` | Output | Table | — | One row per region: `RegionId*`, `RegionLines`, `RegionColumns`, `RegionTopYCoordinate`, `RegionLeftXCoordinate`, `RegionBottomYCoordinate`, `RegionRightXCoordinate`. |

[Get Region Info](Get-Region-Info.html) is the single-region equivalent, useful when you need more than a bounding box for one particular region — it also returns a mask isolating that region and its coordinate reference system:

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `regionId` | Input | Integer Value | No, auto-bound | Which region to describe. |
| `regionManager` | Input | Region Manager | No, auto-bound | The region manager to read from. |
| `regionMask` | Output | Categorical Map | — | A map isolating just this region. |
| `regionLines` | Output | Positive Integer Value | — | The region's height, in cells. |
| `regionColumns` | Output | Positive Integer Value | — | The region's width, in cells. |
| `regionProjection` | Output | Projection | — | The coordinate reference system of the source map. |
| `regionTopYCoordinate`, `regionLeftXCoordinate`, `regionBottomYCoordinate`, `regionRightXCoordinate` | Output | Real Value | — | The region's four coordinate boundaries. |

Both are for reading region metadata itself — bounding boxes, a region's mask, its coordinate system:

```
RegionManager regionsMap 5 {{
    allRegions := GetAllRegionsInfo;
}};
```

## Visiting one region, or every region

[Region](Region.html) narrows scope to a single region for whatever's nested inside it:

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `regionId` | Input | Integer Value | No, auto-bound (editable) | Which region to select. |
| `regionManager` | Input | Region Manager | No, auto-bound | The region manager to select from. |
| `regionId` | Internal Output | Integer Value | — | Re-exposed to functors nested inside. |
| `regionManager` | Internal Output | Region Manager | — | Re-exposed to functors nested inside. |

A region's ID is one of the regions map's own category values, so the cheapest way to visit every region is [For Each Category](For-Each-Category.html) against that categorization directly — no table needs to be built and then queried for its keys first, the way looping over [Get All Regions Info](Get-All-Regions-Info.html)'s output would require. [For Each Category](For-Each-Category.html) takes a Categorization, but since [Categorical Map Type](Categorical-Map-Type.html) converts to [Categorization Type](Categorization-Type.html) automatically on any connection, the regions map itself can be passed straight in — there's no need for an explicit extraction step like [Get Map Categories](Get-Map-Categories.html) first.

As with [For Each](For-Each.html), [For Each Category](For-Each-Category.html)'s current-step output isn't named `regionId`, so [Region](Region.html) is still nested inside to re-expose it under the right name — [Regionalize Map](Regionalize-Map.html) and the rest of this page's functors auto-bind to a port by that exact name. `step` itself is an internal output, not an ordinary variable, so it can't be passed as a bare argument directly — it has to be aliased to a variable with `=` first, the same way [Region Manager](Region-Manager.html)'s own confirmed example aliases `regionManager` to `manager` before using it.

[For Each Region](For-Each-Region.html) bundles "define regions" and "loop over them" into one container, but it has its own required `regions` input and creates its own region manager internally, rather than sharing one from an enclosing [Region Manager](Region-Manager.html). That works fine when the loop is the entire task. It doesn't work here, because this page's example needs the \*same\* region manager instance still available after the loop, for the merge — and [For Each Region](For-Each-Region.html) can't provide that, since its manager stops existing once its own block ends.

```
RegionManager regionsMap 5 {{
    _ := ForEachCategory regionsMap {{
        regionId = step;

        Region regionId {{
            // regionManager auto-binds from the enclosing RegionManager.
        }};
    }};
}};
```

## Splitting a global map into regions

[Regionalize Map](Regionalize-Map.html) and [Regionalize Categorical Map](Regionalize-Categorical-Map.html) cut a global map down to one region's extent:

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `globalMap` | Input | Map / Categorical Map | Yes | The map to split. |
| `regionId` | Input | Integer Value | No, auto-bound | Which region to extract. |
| `keepNonRegionCells` | Input | Boolean | No, default No | If true, cells outside the region mask (including border cells) are kept rather than set to null. |
| `recreateCategories` | Input | Boolean | No, default No — [Regionalize Categorical Map](Regionalize-Categorical-Map.html) only | If true, the region's category set is recomputed from the values actually present in it. If false, the full category set from the global map is kept, even categories absent from this particular region. |
| `regionManager` | Input | Region Manager | No, auto-bound | The region manager defining the split. |
| `regionalMap` | Output | Map / Categorical Map | — | The map cut down to this region. |

[Patcher](Patcher.html) needs both the landscape and the spatial probability map at matching, region-sized extents. Its neighborhood search window means the border cells reserved by `borderCells` need to hold real data, not null — so `keepNonRegionCells` is set explicitly to `Yes` on both calls, rather than left at its default:

```
Region regionId {{
    regionalLandscape := RegionalizeCategoricalMap { globalMap = landscapeMap, keepNonRegionCells = .yes };
    regionalProbabilities := RegionalizeMap { globalMap = probabilitiesMap, keepNonRegionCells = .yes };
}};
```

## Selecting each region's parameters

[Patcher](Patcher.html)'s `changes` and `transitionParameters` inputs are exactly what makes this a case where regions are structurally necessary — each is a single value per call, with no way to vary it by region except by calling [Patcher](Patcher.html) once per region. Storing each region's parameters as rows in a table, keyed by `RegionId`, and slicing out the current region's rows with [Get Table From Key](Get-Table-From-Key.html) keeps that variation in one place instead of duplicating the whole model per region.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `table` | Input | Table | Yes | The table to read from. |
| `keys` | Input | Tuple | Yes | The leading key(s) identifying which sub-table to retrieve. |
| `result` | Output | Table | — | The matching sub-table, with those keys stripped off. |

```
changesByRegion := LoadTable "c:/data/changes_by_region.csv";
paramsByRegion := LoadTable "c:/data/params_by_region.csv";

regionChanges := GetTableFromKey changesByRegion regionId;
regionParams := GetTableFromKey paramsByRegion regionId;
```

`changesByRegion` is shaped `RegionId*`, `From*`, `To*`, `Cells`; `paramsByRegion` is shaped `RegionId*`, `From*`, `To*`, `Mean_Patch_Size`, `Patch_Size_Variance`, `Patch_Isometry`. Stripping `RegionId` leaves exactly the column layout [Change Matrix Type](Change-Matrix-Type.html) and [Transition Function Parameter Matrix Type](Transition-Function-Parameter-Matrix-Type.html) expect, so both convert automatically once connected to [Patcher](Patcher.html) — no explicit conversion step needed.

## Collecting regional results

[Regional Map](Regional-Map.html) and [Regional Categorical Map](Regional-Categorical-Map.html) tag a per-region fragment under a shared name as it's produced — neither has an output; they're pure collectors, accumulating fragments as a side effect of the loop running:

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `globalMapName` | Input | Name | Yes | The shared name this regional fragment will be collected under. |
| `regionalMap` | Input | Map ([Regional Map](Regional-Map.html)) / Categorical Map ([Regional Categorical Map](Regional-Categorical-Map.html)) | Yes | The result to store — any map, at any extent, not necessarily already clipped to the region. It's clipped down to the corresponding region automatically. |
| `regionId` | Input | Integer Value | No, auto-bound | Which region this fragment belongs to. |
| `regionManager` | Input | Region Manager | No, auto-bound | The region manager this fragment belongs to. |

That last point is worth being explicit about: the map passed in doesn't have to already be region-sized — even the full global map would work, since [Regional Map](Regional-Map.html)/[Regional Categorical Map](Regional-Categorical-Map.html) clip it to the region internally rather than assuming it's already been through [Regionalize Map](Regionalize-Map.html)/[Regionalize Categorical Map](Regionalize-Categorical-Map.html). The worked example below still runs its map through [Regionalize Map](Regionalize-Map.html)/[Regionalize Categorical Map](Regionalize-Categorical-Map.html) first, but for a different reason: [Patcher](Patcher.html) itself needs region-sized inputs to compute against, not just to store the result — the clipping done here is redundant on an already region-sized map, not required by [Regional Map](Regional-Map.html) itself.

```
regionChanges := GetTableFromKey changesByRegion regionId;
regionParams := GetTableFromKey paramsByRegion regionId;

Region regionId {{
    regionalLandscape := RegionalizeCategoricalMap { globalMap = landscapeMap, keepNonRegionCells = .yes };
    regionalProbabilities := RegionalizeMap { globalMap = probabilitiesMap, keepNonRegionCells = .yes };

    { regionalChanged = changedLandscape, _ = corrodedProbabilities, _ = remainingChanges } :=
        Patcher regionalLandscape regionalProbabilities regionChanges regionParams;

    RegionalCategoricalMap "changed_landscape" regionalChanged;
}};
```

[Patcher](Patcher.html) returns three outputs, and this example only stores one of them. `corrodedProbabilities` — the probability surface with used-up areas depleted — and `remainingChanges` — a Change Matrix of whatever couldn't be placed, given the current `neighborWindowLines`/`neighborWindowColumns`/`pruneFactor` — are both genuinely useful diagnostics in a real model, not values to ignore on principle. They're discarded here only because this page is illustrating region-manager mechanics rather than full Patcher diagnostics. Binding a discarded output to `_` isn't required — an unwanted output can simply be left out of the block entirely — but naming `corrodedProbabilities` and `remainingChanges` explicitly here signals that they were considered and deliberately skipped, not overlooked.

A model that does care about `remainingChanges` would most likely want it accumulated across regions too, the same way [the area-by-region example](#computing-per-class-areas-within-each-region) accumulates its table with [Mux Table](Mux-Table.html) — checking, once the loop finishes, whether any region failed to place all of its requested changes.

## Merging regions back into one map

[Merge Regional Maps](Merge-Regional-Maps.html) and [Merge Regional Categorical Maps](Merge-Regional-Categorical-Maps.html) reassemble everything stored under a shared name back into one global mosaic:

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `globalMapName` | Input | Name | Yes | The name the fragments were collected under, via [Regional Map](Regional-Map.html) or [Regional Categorical Map](Regional-Categorical-Map.html). |
| `mergeNonRegionCells` | Input | Boolean | No, default No | If true, cells outside the region mask (including border cells) are merged in too, rather than ignored. Two overlapping cells can only be combined if they share the same value or one of them is null. |
| `regionManager` | Input | Region Manager | No, auto-bound | The region manager the fragments belong to. |
| `globalMap` | Output | Map / Categorical Map | — | The reassembled mosaic. |

There's a trap here worth naming: neither merge functor has a `sequenceInput` of its own, and nothing about `globalMapName` — just a literal string — creates a data dependency on the loop that populated it. Left as-is, the engine has no reason to run the merge \*after\* the loop rather than before or during it. [For Each Category](For-Each-Category.html) does expose a `sequenceOutput` once the whole loop finishes, but with nowhere on the merge functor to plug it into, the fix is a [Group](Group.html) wrapped around the merge, whose own `sequenceInput` the loop's `sequenceOutput` connects into.

A few more things worth knowing before relying on the merge:

- **Splitting keeps border cells so Patcher's neighborhood window has real context; merging discards them anyway.** Each region's own border zone duplicates territory another region already owns and computes for itself. Merging with `mergeNonRegionCells: Yes` would pull that duplicated, independently-computed data back in instead of leaving each region's own interior result as the authority for its own cells — which is why the worked example uses `keepNonRegionCells: Yes` when splitting, but leaves `mergeNonRegionCells` at its default `No`.
- **The merged map's format is inherited from the first fragment stored, not negotiated across all of them.** Cell type, null value, and categorization all come from whichever [Regional Map](Regional-Map.html) or [Regional Categorical Map](Regional-Categorical-Map.html) call registered first for that name — only the dimensions come from the regions map itself. If regions are processed in an order that isn't guaranteed, don't rely on which fragment "wins."
- **Mismatched null values fail the merge, not silently overwrite each other.** When `mergeNonRegionCells` brings overlapping border cells from two different regions together, they can only combine if they agree, or one of them is null — two regions disagreeing on what a cell's value should be raises an error rather than picking one.
- **A layer's sparse storage survives the merge**, so long as every regional fragment for that layer used it too — the merged global layer comes out sparse rather than being densified. See [Map Type](Map-Type.html)'s Storage section for what sparse storage means.
- **Fragments are consumed, not just read.** Once the merge for a given `globalMapName` runs, the manager no longer holds those fragments — there's no merging the same name twice, and nothing left to read back under it afterward.

## Relaying a Region Manager between functors

[Region Manager Value](Region-Manager-Value.html) exists purely to pass a Region Manager value through — the same relay role [Struct](Struct-Type.html)'s carrier functor plays for structs. Its own input auto-binds to the enclosing container's `regionManager` by default and cannot be given as a constant.

## Putting it together

```
landscapeMap := LoadCategoricalMap "c:/data/landscape.tif" .none .default 0;
probabilitiesMap := LoadMap "c:/data/probabilities.tif";
regionsMap := LoadCategoricalMap "c:/data/regions.tif" .none .default 0;

changesByRegion := LoadTable "c:/data/changes_by_region.csv";
paramsByRegion := LoadTable "c:/data/params_by_region.csv";

RegionManager regionsMap 5 {{
    sequenceOut := ForEachCategory regionsMap {{
        regionId = step;

        regionChanges := GetTableFromKey changesByRegion regionId;
        regionParams := GetTableFromKey paramsByRegion regionId;

        Region regionId {{
            regionalLandscape := RegionalizeCategoricalMap { globalMap = landscapeMap, keepNonRegionCells = .yes };
            regionalProbabilities := RegionalizeMap { globalMap = probabilitiesMap, keepNonRegionCells = .yes };

            { regionalChanged = changedLandscape, _ = corrodedProbabilities, _ = remainingChanges } :=
                Patcher regionalLandscape regionalProbabilities regionChanges regionParams;

            RegionalCategoricalMap "changed_landscape" regionalChanged;
        }};
    }};

    _ := Group sequenceOut {{
        finalLandscape := MergeRegionalCategoricalMaps "changed_landscape" .no;
        SaveCategoricalMap finalLandscape "c:/data/changed_landscape_merged.tif";
    }};
}};
```

One region manager, defined once at the top, is what threads the whole thing together: [For Each Category](For-Each-Category.html) loops directly against the categories already attached to `regionsMap`, [Get Table From Key](Get-Table-From-Key.html) slices each region's own change matrix and transition parameters out of the two shared tables, [Region](Region.html) narrows against the manager once per loop iteration, [Regional Categorical Map](Regional-Categorical-Map.html) stores fragments into it, and [Merge Regional Categorical Maps](Merge-Regional-Categorical-Maps.html) — deliberately delayed until the loop's `sequenceOutput` fires — reads every one of those fragments back out of the same instance.

## Computing per-class areas within each region

[Calc Areas](Calc-Areas.html) returns a table of every category's area within a map — this section computes one separately per region and accumulates them into a single table, one region's worth of rows at a time.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `source` | Input | Categorical Map | Yes | The map to measure. |
| `useAuthalicArea` | Input | Boolean | No, default Yes | For geographic (Lat/Long) grids, whether to use an authalic sphere for more accurate area at all latitudes, rather than treating every cell as the same size. |
| `areas` | Output | Table | — | `Category*`, `Area_In_Cells`, `Area_In_Hectares`, `Area_In_Square_Meters`. |

Since each region produces its own `Category`-keyed table, and the goal is one combined table across every region, the accumulator needs a second, leading key — `RegionId` — so each region's rows land in their own, non-overlapping slice. [Mux Table](Mux-Table.html) carries that combined table across loop iterations:

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `initial` | Input | Table | Yes | The starting value, before any iteration has run. |
| `feedback` | Input | Table | Yes | The value produced by the current iteration, becoming `table` for the next one. |
| `table` | Output | Table | — | The accumulated value entering the current iteration. |

This section doesn't use [Region](Region.html) at all — `regionId` is used directly, since [Regionalize Categorical Map](Regionalize-Categorical-Map.html) and [Set Table By Key](Set-Table-By-Key.html) both auto-bind or accept it positionally without needing it re-exposed under a container of its own. There's also no windowed calculation here, so unlike the [Patcher](Patcher.html) example, `keepNonRegionCells` is left at its default — [Calc Areas](Calc-Areas.html) only tallies cells within the region itself:

```
landscapeMap := LoadCategoricalMap "c:/data/landscape.tif" .none .default 0;
regionsMap := LoadCategoricalMap "c:/data/regions.tif" .none .default 0;

emptyRegionAreas := Table [
    "RegionId*#real", "Category*#real", "Area_In_Cells#real", "Area_In_Hectares#real", "Area_In_Square_Meters#real"
];

RegionManager regionsMap 5 {{
    _ := ForEachCategory regionsMap {{
        regionId = step;

        accumulatedAreas := MuxTable emptyRegionAreas nextAccumulatedAreas;

        regionalLandscape := RegionalizeCategoricalMap landscapeMap regionId;
        areaTable := CalcAreas regionalLandscape .no;

        // regionId (an Integer Value) converts to a one-element Tuple
        // automatically here, since it's a connected variable, not a literal.
        nextAccumulatedAreas := SetTableByKey accumulatedAreas regionId areaTable;
    }};

    // nextAccumulatedAreas, not accumulatedAreas (the mux's own output,
    // which lags one iteration behind), holds every region's rows once the
    // loop finishes. The Table carrier passes it out of the loop's scope,
    // since := always binds a functor call.
    allRegionAreas := Table nextAccumulatedAreas;
    SaveTable allRegionAreas "c:/data/area_by_region.csv";
}};
```

Unlike the map-merging example earlier on this page, no [Group](Group.html)/`sequenceOutput` workaround is needed to order the save correctly — `nextAccumulatedAreas` is an ordinary data value with a real dependency chain running back through every iteration, so the engine already knows to wait.

This loop runs one region strictly after another, not in parallel. Each iteration's `accumulatedAreas` is fed directly by the previous iteration's `nextAccumulatedAreas`, so the next region can't start until the current one has finished and been folded into the running table — even though, taken alone, no region's area calculation actually depends on any other region's.
{% endraw %}
