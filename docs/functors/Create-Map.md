---
title: "Create Map"
nav_order: 25
parent: "Map Algebra Functors"
grand_parent: "Functor List"
redirect_from:
  - /Create-Map.html
---
{% raw %}
# Create Map

## Description

Creates an empty map with the given dimensions, cell type, projection, and georeferencing. Every cell of the resulting map is initialized with the specified null value.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Lines | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number of lines of the map. |
| Columns | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number of columns of the map. |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Cell type of the map. |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Null value of the map. |
| Projection | [Projection Type](../types/Projection-Type.html) | Projection assigned to the map. |
| Cell Width | [Real Value Type](../types/Real-Value-Type.html) | Width of a cell. The unit depends on the assigned projection. |
| Cell Height | [Real Value Type](../types/Real-Value-Type.html) | Height of a cell. The unit depends on the assigned projection. |
| Registration Coordinate Y | [Real Value Type](../types/Real-Value-Type.html) | Y registration coordinate of the map (Northing or Latitude). The unit depends on the assigned projection. |
| Registration Coordinate X | [Real Value Type](../types/Real-Value-Type.html) | X registration coordinate of the map (Easting or Longitude). The unit depends on the assigned projection. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Registration Cell Y | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Line index of the cell to which the registration coordinate corresponds. Line 1 is the topmost line. This is an advanced port. | 1 |
| Registration Cell X | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Column index of the cell to which the registration coordinate corresponds. Column 1 is the leftmost column. This is an advanced port. | 1 |
| Create As Sparse | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, forces the map to be created as a sparse raster set, which stores only non-null cells, trading slower access time for reduced storage. This is an advanced port. | Yes |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Created map. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

All cells of the created map are initialized with the specified null value.

## Internal Name

CreateMap
{% endraw %}
