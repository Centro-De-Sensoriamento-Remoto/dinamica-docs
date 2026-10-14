---
title: "Rasterize Shape"
nav_exclude: true
---
{% raw %}
# Rasterize Shape

## Description

Rasterizes a shapefile (or other OGR-supported vector source) into a map, using the given parameters. This functor wraps the GDAL library's `gdal_rasterize` utility.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Input Shape Filename | [Generic Filename Type](Generic-Filename-Type.html) | Filename of the input shape to rasterize. |
| Output Map Filename | [Map Filename Type](Map-Filename-Type.html) | Filename of the resulting rasterized map. Its format is selected from the file extension. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Default Output Value | [Real Value Type](Real-Value-Type.html) | Value assigned to every rasterized feature. Cannot be used together with Shape Attribute Name; exactly one of the two must be given. | .none |
| Shape Attribute Name | [String Type](String-Type.html) | Name of the shape's attribute field supplying the value assigned to each rasterized feature. Cannot be used together with Default Output Value; exactly one of the two must be given. | .none |
| Output Map Cell Type | [Cell Type](Cell-Type.html) | Cell type of the resulting map. Unsigned 1-Bit Integer and Signed 8-Bit Integer are both treated as Unsigned 8-Bit Integer for this functor. | Signed 32 Bit Integer |
| Output Map Null Value | [Null Value Type](Null-Value-Type.html) | Null value of the resulting map. | .default |
| Output Map Cell Width | [Real Value Type](Real-Value-Type.html) | Cell width of the resulting map, in units compatible with its projection. Must be given together with Output Map Cell Height; mutually exclusive with Output Map Lines/Columns. | .none |
| Output Map Cell Height | [Real Value Type](Real-Value-Type.html) | Cell height of the resulting map, in units compatible with its projection. Must be given together with Output Map Cell Width; mutually exclusive with Output Map Lines/Columns. | .none |
| Output Map Lines | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Number of lines of the resulting map. Must be given together with Output Map Columns; mutually exclusive with Output Map Cell Width/Height. This is an advanced port. | .none |
| Output Map Columns | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Number of columns of the resulting map. Must be given together with Output Map Lines; mutually exclusive with Output Map Cell Width/Height. This is an advanced port. | .none |
| Use Cell Center Only | [Boolean Value Type](Boolean-Value-Type.html) | If true, a cell is considered part of a feature based on its center only; if false, the whole cell area is considered. Must be true when rasterizing linear features (roads, rivers, and similar). This is an advanced port. | Yes |
| Use Compression | [Boolean Value Type](Boolean-Value-Type.html) | If true, the output map is compressed, for formats that support it (GeoTiff and HFA; ignored for other formats). This is an advanced port. | Yes |
| Layer Name | [String Type](String-Type.html) | Layer of the input data source containing the features to rasterize. Mutually exclusive with Select Statement. This is an advanced port. | .none |
| Select Statement | [String Type](String-Type.html) | SQL statement evaluated against the data source to produce a virtual layer of the features to rasterize. Mutually exclusive with Layer Name. This is an advanced port. | .none |
| Where Statement | [String Type](String-Type.html) | SQL WHERE expression selecting which features of the input layer are rasterized. This is an advanced port. | .none |
| Additional GDAL Rasterize Arguments | [String Type](String-Type.html) | Additional arguments passed to the underlying `gdal_rasterize` invocation, appended after every other argument. This is an advanced port. | "" |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Output Map Filename | [Map Filename Type](Map-Filename-Type.html) | Same filename given to the Output Map Filename input port. |

## Group

[GDAL / OGR](Functor-List.html#gdal--ogr)

## Notes

This functor is essentially a wrapper around the [GDAL library](https://gdal.org/) utility [GDAL Rasterize](https://gdal.org/programs/gdal_rasterize.html).

The resulting map takes its projection and boundaries from the input shape; use [Transform Map](Transform-Map.html) to change them afterward.

Only the GeoTiff (.tif) and HFA (.img) formats support Use Compression; it is ignored for other formats.

Unlike most functors, this functor cannot be connected directly to a map produced by another functor while it is still in memory — that map must first be saved to disk with [Save Map](Save-Map.html) — because the underlying GDAL utility can only operate on maps already written to a file. Re-arranging an in-memory map into the form GDAL's API expects would heavily impact execution performance and the amount of memory required, which is why this restriction is not worked around internally.

## Internal Name

RasterizeShape
{% endraw %}
