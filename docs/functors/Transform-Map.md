---
title: "Transform Map"
nav_order: 2
parent: "GDAL / OGR Functors"
grand_parent: "Functor List"
---
{% raw %}
# Transform Map

## Description

Reprojects a map file according to a set of parameters. It can also crop and reproject a map based on the projection, extents, and cell size of a given format map. This functor is also known by the alias `ReprojectMap` in EGO Script.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Input Map Filename | [Map Filename Type](../types/Map-Filename-Type.html) | Filename of the input map to reproject. |
| Output Map Filename | [Map Filename Type](../types/Map-Filename-Type.html) | Filename of the resulting reprojected map. Its format is selected from the file extension. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Output Format Map Filename | [Map Filename Type](../types/Map-Filename-Type.html) | Filename of a format map whose projection, extents, and cell size become the default attributes of the output. Mutually exclusive with Output Map Projection. | .none |
| Output Map Projection | [Projection Type](../types/Projection-Type.html) | Projection to reproject the input map into; the output's extents and cell size are then computed automatically (either can still be overridden by the relevant ports). Mutually exclusive with Output Format Map Filename. | .none |
| Output Map Cell Type | [Cell Type](../types/Cell-Type.html) | Cell type of the output map. Unsigned 1-Bit Integer and Signed 8-Bit Integer are both treated as Unsigned 8-Bit Integer for this functor. | Signed 32 Bit Integer |
| Output Map Null Value | [Null Value Type](../types/Null-Value-Type.html) | Null value of the output map. | .default |
| Resampling Method | [Enum Type](../types/Enum-Type.html) | Resampling method used to compute output values from the input map: Nearest, Bilinear, Cubic, Cubic Spline, Lanzos, Average, Mode, Maximum, Minimum, Median, 1st Quartile, or 3rd Quartile. This is an advanced port. | Nearest |
| Additional Input Map Null Value | [Null Value Type](../types/Null-Value-Type.html) | Additional value to treat as null in the input map, alongside its own null value if it has one. This is an advanced port. | .none |
| Input Map Projection | [Projection Type](../types/Projection-Type.html) | Projection to assume for the input map, overriding its own. When not given, the input map's own projection is used. This is an advanced port. | .none |
| Output Map Lines | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number of lines of the output map. Must be given together with Output Map Columns; mutually exclusive with Output Map Cell Width/Height. This is an advanced port. | .none |
| Output Map Columns | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number of columns of the output map. Must be given together with Output Map Lines; mutually exclusive with Output Map Cell Width/Height. This is an advanced port. | .none |
| Output Map Cell Width | [Real Value Type](../types/Real-Value-Type.html) | Cell width of the output map, in units compatible with its projection. Must be given together with Output Map Cell Height; mutually exclusive with Output Map Lines/Columns. This is an advanced port. | .none |
| Output Map Cell Height | [Real Value Type](../types/Real-Value-Type.html) | Cell height of the output map, in units compatible with its projection. Must be given together with Output Map Cell Width/Height; mutually exclusive with Output Map Lines/Columns. This is an advanced port. | .none |
| Use Compression | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, the output map is compressed, for formats that support it (GeoTiff and HFA; ignored for other formats). This is an advanced port. | Yes |
| Additional GDAL Warp Arguments | [String Type](../types/String-Type.html) | Additional arguments passed to the underlying `gdalwarp` invocation, appended after every other argument. This is an advanced port. | "" |
| Additional GDAL Translate Arguments | [String Type](../types/String-Type.html) | Additional arguments passed to the underlying `gdal_translate` invocation, appended after every other argument. This is an advanced port. | "" |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Output Map Filename | [Map Filename Type](../types/Map-Filename-Type.html) | Same filename given to the Output Map Filename input port. |

## Group

[GDAL / OGR](../Functor-List.html#gdal--ogr)

## Notes

This functor wraps the [GDAL library](https://gdal.org/) utilities [GDAL Warp](https://gdal.org/programs/gdalwarp.html) and [GDAL Translate](https://gdal.org/programs/gdal_translate.html): GDAL Warp is used to reproject the map, and GDAL Translate is used to clip the reprojected map to the boundaries of a given mask.

Categorization information present in the input map is not preserved by the reprojection.

Only the GeoTiff (.tif) and HFA (.img) formats support Use Compression; it is ignored for other formats.

Unlike most functors, this functor cannot be connected directly to a map produced by another functor while it is still in memory — that map must first be saved to disk with [Save Map](Save-Map.html) — because the underlying GDAL utility can only operate on maps already written to a file. Re-arranging an in-memory map into the form GDAL's API expects would heavily impact execution performance and the amount of memory required, which is why this restriction is not worked around internally.

## Internal Name

TransformMap
{% endraw %}
