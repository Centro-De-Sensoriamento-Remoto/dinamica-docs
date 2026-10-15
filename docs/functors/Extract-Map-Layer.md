---
title: "Extract Map Layer"
nav_order: 30
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Extract Map Layer

## Description

Extracts one layer from a multilayer map (a raster cube) and returns it as its own single-layer map.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Multilayer map from which the layer is extracted. |
| Layer Index Or Name | [Index Or Name Type](../types/Index-Or-Name-Type.html) | Index or name of the layer to extract. The topmost layer has index 1. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Layer | [Map Type](../types/Map-Type.html) | Extracted layer, as its own single-layer map. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

The topmost layer of Map has index 1.

## Internal Name

ExtractMapLayer
{% endraw %}
