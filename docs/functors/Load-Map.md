---
title: "Load Map"
nav_order: 5
parent: "Input / Output Functors"
grand_parent: "Functor List"
---
{% raw %}
# Load Map

## Description

Loads a map from a file. The file format is determined automatically from the filename's extension. See [Load Categorical Map](Load-Categorical-Map.html) for loading maps whose cells represent categories.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Filename | [Map Filename Type](../types/Map-Filename-Type.html) | Name and path of the file to load. If no path is given, the file is located relative to the Workdir, or to the model script when there is none. It can also be a URL, an `s3://`, `mem://` or `vsi://` location, or a STACIT query. See the Notes. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Additional value to treat as null, alongside the file's own null value if it has one. Useful for assigning a null value to files that do not define one. | .none |
| Storage Mode | [Enum Type](../types/Enum-Type.html) | Hint for how the map should be handled: Default follows the memory allocation policy in the application settings; Prefer Memory suggests loading the whole map into memory; Prefer Disk suggests keeping it on disk and loading it on demand, piece by piece; Load As Sparse suggests storing only non-null cells, minimizing storage at the expense of access time. This is only a hint and may be ignored. This is an advanced port. | Default |
| Suffix Digits | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Number of digits used to render Step as a filename suffix. If Step needs more digits than this, it is used unmodified. If zero, no suffix is added. This is an advanced port. | 0 |
| First Window Coordinate X | [Real Value Type](../types/Real-Value-Type.html) | X coordinate of one corner of a crop window, in the map's projection units. Must lie within the file's extent. This is an advanced port. | .none |
| First Window Coordinate Y | [Real Value Type](../types/Real-Value-Type.html) | Y coordinate of one corner of a crop window, in the map's projection units. Must lie within the file's extent. This is an advanced port. | .none |
| Second Window Coordinate X | [Real Value Type](../types/Real-Value-Type.html) | X coordinate of the opposite corner of the crop window, in the map's projection units. Must lie within the file's extent. This is an advanced port. | .none |
| Second Window Coordinate Y | [Real Value Type](../types/Real-Value-Type.html) | Y coordinate of the opposite corner of the crop window, in the map's projection units. Must lie within the file's extent. This is an advanced port. | .none |
| Step | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Current step or model iteration, appended to Filename as a numeric suffix; automatically bound to the innermost compatible container. This is an advanced port. | .none |
| Workdir | [Workdir Type](../types/Workdir-Type.html) | Work directory Filename is relative to. It accepts the same locations as the Folder input of [Workdir](Workdir.html): a folder, an archive, a URL, and so on. When not bound, the directory containing the script is used. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Loaded map, or, when the crop window is defined, only the cropped window of it. |

## Group

[Input / Output](../Functor-List.html#input--output)

## Notes

When Null Value is given, any cell already equal to the file's own null value (if it defines one) is converted to Null Value, and any non-null cell that happens to equal Null Value is likewise promoted to null — so a value that meant "no data" before loading still means "no data" after, regardless of how the null definition changed.

The crop window (First/Second Window Coordinate X/Y) must either be left entirely at .none, loading the map in full, or have all four coordinates defined together; a partially defined window is not accepted.

If Step is .none, the loaded filename has no numeric suffix.

For a list of file formats that Load Map can load, the supported [projections](https://en.wikipedia.org/wiki/Map_projection) and [datums](https://en.wikipedia.org/wiki/Datum_(geodesy)), check the supported map formats.

Maps can also be loaded from archives, remote locations and STACIT queries. Filename accepts a local path, a URL (such as `https://...`), an `s3://` location, a `mem://` location, a GDAL virtual filesystem path starting with `vsi://`, or a STACIT query starting with `STACIT:`. A Filename that ends in `.gz` is read as a compressed map.

To read several maps from the same archive, URL or STACIT query, place the loaders inside a [Workdir](Workdir.html). A relative Filename is then resolved against it; see [Workdir](Workdir.html) for the supported archive formats and the rules for each kind of location. A complete Filename (a full path, URL, `s3://`, `mem://` or `vsi://` location, or STACIT query) ignores the Workdir.

The crop window (First/Second Window Coordinate X/Y) also works with URLs, archives and STACIT queries: only the cells inside the window are transferred or loaded, not the whole file.

## Internal Name

LoadMap

## Usage examples

See practical examples of this functor in [Lesson 4: Opening and Saving maps](../guidebook/Opening-And-Saving-Maps.html) of the Guidebook.

Loading a map from a URL:

```
landscape := LoadMap { filename = "https://csr.ufmg.br/dinamica_utils/tests/southAmerica.tif" };
```

Loading a compressed map from a URL:

```
landscape := LoadMap { filename = "https://csr.ufmg.br/dinamica_utils/tests/southAmerica.tif.gz" };
```

Loading an asset from a STACIT query:

```
landcover := LoadMap { filename = (String $"(STACIT:"https://planetarycomputer.microsoft.com/api/stac/v1/search?collections=usgs-lcmap-conus-v13&datetime=2021-01-01/2021-12-31&bbox=-79.762,40.496,-71.856,45.013":asset=lcpri)") };
```

Loading a map from an archive, using a [Workdir](Workdir.html):

```
Workdir "bundle.zip" {{
    // "southAmerica.tif" is a path inside the archive.
    landscape := LoadMap { filename = "southAmerica.tif" };
}};
```

Loading only a window of a map stored at a URL. The four numbers are the window coordinates, in the map's projection units:

```
// Only the cells inside the window are transferred.
Workdir "https://csr.ufmg.br/dinamica_utils" {{
    landscape := LoadMap "tests/AREA_IMOVEL_5107701.tif" .none .default 0 585237 8370193 617017 8344073;
}};
```
{% endraw %}
