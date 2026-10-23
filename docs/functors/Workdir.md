---
title: "Workdir"
nav_order: 15
parent: "Input / Output Functors"
grand_parent: "Functor List"
---
{% raw %}
# Workdir

## Description

This container sets the working directory used by the functors it contains to read and write files. The working directory can be a folder, an archive, a remote location, or an area of memory.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Folder | [Folder Type](../types/Folder-Type.html) | Working directory to be used by the contained functors. Besides a regular folder, it accepts an archive, a URL, an S3 location, a memory area, a GDAL virtual path, or a STACIT query, as described in the Notes. |

## Optional Inputs

None.

## Outputs

None.

## Internal Outputs

| Name | Type | Description |
| --- | --- | --- |
| Workdir | [Workdir Type](../types/Workdir-Type.html) | Auto-bindable working directory, picked up automatically by any contained functor that asks for one. |

## Group

[Input / Output](../Functor-List.html#input--output)

## Notes

Inside this container, filenames referring to maps, tables, and Weights of Evidence coefficients or ranges, among others, are resolved relative to this directory.

Folder is interpreted from its text:

| Folder | Meaning |
| --- | --- |
| A local path | A regular folder. |
| A path or URL ending in `.zip`, `.tar`, `.tar.gz`, `.tgz`, `.7z` or `.rar` | An archive. The filenames used by the contained functors are paths inside the archive. The extension is not case sensitive. |
| A path or URL ending in `.gz` | A single compressed file. The filename of the contained loader is ignored, since the compressed file has no name of its own. |
| A URL, such as `https://example.com/data` | A remote folder. The filenames are appended to the URL. |
| `s3://bucket/folder` | An Amazon S3 location. |
| `mem://name` | An area of memory. The text after `mem://` is ignored. |
| `vsi://path` | A GDAL virtual filesystem path. The path that follows `vsi://` is used as written. |
| `STACIT:query` | A STACIT query. The filename is appended to the query as is, so it must start with the `:` of a STACIT option, such as `:asset=lcpri`. |

Archives can be stored locally or at a URL. A URL that ends in an archive extension is read directly from the remote location.

A filename that is already complete ignores the Workdir. This applies to absolute paths, URLs, `s3://`, `mem://` and `vsi://` locations, and STACIT queries.

Loaders that define a crop window, such as [Load Map](Load-Map.html), work with all of these locations. For URLs and archives, only the cells inside the window are transferred or loaded.

Archives and `.gz` files are read-only: saving a file inside a Workdir that points to one raises an error. A `mem://` Workdir can be written, and the saved maps can be loaded back inside the same Workdir using the same filename.

## Internal Name

Workdir

## Usage examples

Loading a map from an archive. The filename is a path inside the archive:

```
Workdir "bundle.zip" {{
    // "southAmerica.tif" is a path inside the archive.
    landscape := LoadMap { filename = "southAmerica.tif" };
}};
```

Loading a map from an archive stored at a URL:

```
Workdir "https://csr.ufmg.br/dinamica_utils/tests/bundle.7z" {{
    landscape := LoadMap { filename = "southAmerica.tif" };
}};
```

Loading a map from a URL folder:

```
Workdir "https://csr.ufmg.br/dinamica_utils" {{
    landscape := LoadMap { filename = "tests/southAmerica.tif" };
}};
```

Loading a compressed map. The filename is ignored for `.gz` files:

```
Workdir "southAmerica.tif.gz" {{
    // The filename is ignored by the "gz" format.
    landscape := LoadMap { filename = "unused filename.tif" };
}};
```

Loading an asset from a STACIT query. The query is set once, and each loader selects its asset:

```
Workdir (String $"(STACIT:"https://planetarycomputer.microsoft.com/api/stac/v1/search?collections=usgs-lcmap-conus-v13&datetime=2021-01-01/2021-12-31&bbox=-79.762,40.496,-71.856,45.013")") {{
    // The filename is appended to the query and selects the asset.
    landcover := LoadMap { filename = ":asset=lcpri" };
}};
```
{% endraw %}
