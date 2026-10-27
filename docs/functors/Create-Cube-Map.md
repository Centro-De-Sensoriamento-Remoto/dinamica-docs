---
title: "Create Cube Map"
nav_order: 24
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Create Cube Map

## Description

Assembles the maps connected inside this container into a single multilayer map (a raster cube), stacking one layer per connected map. Each map is connected through a [Number And Name Map](Number-And-Name-Map.html) hook, which supplies the name and stacking position of its layer; hooks with position 0 are treated as unordered and are placed, sorted alphabetically by name, below every explicitly positioned layer.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Cell type of the output map. |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Null value of the output map. Must be compatible with Cell Type. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Multilayer map assembled from the connected layers. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

Only [Number And Name Map](Number-And-Name-Map.html) hooks can be connected inside this container.

Only the first layer of each connected map is added to the cube; any further layers of that map are ignored.

Every connected map must share the same dimensions; the first map's spatial format is used to validate the others and to build the output map.

Categorization data carried by the connected maps is discarded.

Each connected map's cells are cast to the output Cell Type; a cell whose value cannot be represented without truncation raises an error. Null cells are converted to the output Null Value.

Raises an error if no map is connected inside this container, if two connected maps share the same name, or if two connected maps are assigned the same stacking position.

Raises an error if Null Value is not compatible with Cell Type.

## Internal Name

CreateCubeMap
{% endraw %}
