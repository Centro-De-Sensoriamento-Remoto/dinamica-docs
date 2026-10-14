---
title: "Extract Map Attributes"
nav_order: 29
parent: "Map Algebra Functors"
grand_parent: "Functor List"
redirect_from:
  - /Extract-Map-Attributes.html
---
{% raw %}
# Extract Map Attributes

## Description

Extracts general attributes and basic statistics from a map, returning them as a lookup table keyed by a predefined attribute code. All layers of the map are analyzed together, and the resulting table refers to them jointly.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Map whose attributes will be extracted. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Extract Dynamic Attributes | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, dynamic attributes (null/non-null cell counts, minimum, maximum, sum) are also extracted. | Yes |
| Extract Statistical Attributes | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, statistical attributes (mean, variance, standard deviation, mode, median, unique count) are also extracted. | Yes |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Attributes | [Lookup Table Type](../types/Lookup-Table-Type.html) | Table of extracted attributes, keyed by attribute code. |
| Layer Attributes | [Table Type](../types/Table-Type.html) | Table of per-layer attributes, keyed by layer position in the map. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

Each attribute has a predefined name that can be used to retrieve it by name (rather than by numeric key) with the `tX["NAME"]` syntax in [Calculate Map](Calculate-Map.html), [Calculate Categorical Map](Calculate-Categorical-Map.html), [Calculate Value](Calculate-Value.html), and the lookup table calculators.

If an attribute cannot be determined, its entry is omitted from Attributes rather than being filled with a placeholder. Minimum and maximum values are only determined when the map has at least one non-null cell.

**Basic attributes**

| Key | Predefined Name | Description |
| --- | --- | --- |
| 1 | "lines" | number of lines |
| 2 | "columns" | number of columns |
| 3 | "cells" | lines times columns |
| 4 | "layers" | number of layers |
| 5 | "cellHeight" | cell height, in meters |
| 6 | "cellWidth" | cell width, in meters |
| 7 | "cellArea" | cell area, in hectares |
| 19 | "cellType" | cell type code, see Cell type codes below |
| 20 | "nullValue" | null value |
| 21 | "registrationCoordinateY" | registration coordinate Y |
| 22 | "registrationCoordinateX" | registration coordinate X |
| 23 | "registrationCellY" | registration cell Y |
| 24 | "registrationCellX" | registration cell X |
| 25 | "rotationY" | rotation Y |
| 26 | "rotationX" | rotation X |
| 27 | "originalCellHeight" | cell height as specified by the projection |
| 28 | "originalCellWidth" | cell width as specified by the projection |

**Dynamic attributes** (present only when Extract Dynamic Attributes is true), computed across all non-null cells of all layers:

| Key | Predefined Name | Description |
| --- | --- | --- |
| 8 | "nullCells" | number of null cells |
| 9 | "nonNullCells" | number of non-null cells |
| 10 | "minCell" | minimum value (excluding null cells) |
| 11 | "maxCell" | maximum value (excluding null cells) |
| 12 | "cellSum" | sum of the values (excluding null cells) |

**Statistical attributes** (present only when Extract Statistical Attributes is true), computed across all non-null cells of all layers:

| Key | Predefined Name | Description |
| --- | --- | --- |
| 13 | "meanCell" | average (excluding null cells) |
| 14 | "cellVar" | variance (excluding null cells) |
| 15 | "cellStd" | standard deviation (excluding null cells) |
| 16 | "modeCell" | mode (excluding null cells) |
| 17 | "medianCell" | median (excluding null cells) |
| 18 | "uniqueCells" | total unique occurrences (excluding null cells) |

**Cell type codes** used by attribute 19 ("cellType"):

| Code | Cell Type |
| --- | --- |
| 0 | Unsigned 1 Bit Integer |
| 1 | Signed 8 Bit Integer |
| 2 | Unsigned 8 Bit Integer |
| 3 | Signed 16 Bit Integer |
| 4 | Unsigned 16 Bit Integer |
| 5 | Signed 32 Bit Integer |
| 6 | Unsigned 32 Bit Integer |
| 7 | IEEE 754 32 Bit Real |
| 8 | IEEE 754 64 Bit Real |

Layer Attributes has columns "Layer_Index" (the layer's position) and "Layer_Name" (the layer's name); currently the layer name is the only layer-specific attribute returned.

## Internal Name

ExtractMapAttributes

## Usage examples

See practical examples of this functor in Lesson 6: Extracting map attributes and basic statistics
{% endraw %}
