---
title: "Crop Map To Extents"
nav_order: 27
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Crop Map To Extents

## Description

Crops an input map to a rectangular window defined by the coordinates of two opposite corners, expressed in the map's projection. The window can be specified using either pair of opposite corners; the functor determines the correct bounding box regardless of which two corners are given. The cropping is applied to every layer of the map.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Input map to be cropped. |
| First Window Coordinate X | [Real Value Type](../types/Real-Value-Type.html) | X coordinate of the first corner of the crop window, in the map's projection units. Must lie within the map's extent. |
| First Window Coordinate Y | [Real Value Type](../types/Real-Value-Type.html) | Y coordinate of the first corner of the crop window, in the map's projection units. Must lie within the map's extent. |
| Second Window Coordinate X | [Real Value Type](../types/Real-Value-Type.html) | X coordinate of the second, opposite corner of the crop window, in the map's projection units. Must lie within the map's extent. |
| Second Window Coordinate Y | [Real Value Type](../types/Real-Value-Type.html) | Y coordinate of the second, opposite corner of the crop window, in the map's projection units. Must lie within the map's extent. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Output | [Map Type](../types/Map-Type.html) | Cropped map, corresponding to the defined window. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

The cropping window can be defined by any two opposite corners; this functor determines the correct bounding box regardless of which corners are given (for example, upper-left and lower-right, or upper-right and lower-left).

If Map has multiple layers, the cropping is applied to every layer.

Raises an error if any of the four window coordinates falls outside the extent of Map.

## Internal Name

CropMapToExtents
{% endraw %}
