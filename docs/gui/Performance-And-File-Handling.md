---
title: "Performance and File Handling"
parent: Graphical Interface
nav_order: 10
---
{% raw %}
# Performance and File Handling

## Increasing Performance

- Select "Tools => Options \| Advanced \| Automatically detect the number of processors available". When running models from the command line, set the `-processor` option of each model to 0.
- Set the memory management option under "Tools => Options \| Advanced" to "Balanced" or "Aggressive". On the command line, use the option `-memory-allocation-policy` with the value 1 or 4, respectively.
- Install the Enhancement Plugin for Dinamica EGO and clear "Tools => Options \| Advanced \| Disable compilation of native expressions".
- Set "Tools => Options \| System \| Message log level" to Result. This helps most in models with many loop containers such as [Repeat](../functors/Repeat.html), [While](../functors/While.html), and [For](../functors/For.html).
- Avoid maps with the [cell type](../types/Cell-Type.html) "1 Bit Integer". It saves memory, but has a large negative impact on performance.
- Keep Dinamica EGO updated.

These options are described in [Options](Options.html).

## File Paths

The interface shows absolute file paths for readability, but the paths are stored as relative paths. To move a model without breaking its file references, keep the same relative location between the script file ([EGO Script](../EGO-Script.html) or [EGOML](../EGOML-Script.html)) and the data directory.

Alternatively, use the [Workdir](../functors/Workdir.html) functor: every Load and Save functor inside it is relative to the directory set in the Workdir. A model can contain several Workdir containers. For an example, see the folder `Examples\run_lucc_northern_mato_grosso\run_roads_with_comments_and_workdirs` in the Dinamica EGO examples.

## Saving Model Backups

See [Model Backups](Options.html#model-backups) in Options.

## Loading Files from Zip Files

Maps, tables, lookup tables, and Weights of Evidence files can be loaded from [zip](https://en.wikipedia.org/wiki/ZIP_(file_format)) files.

- A zip file packs all the files of a model in a single archive. It does not increase the amount of data Dinamica EGO can handle at once: Dinamica unzips the files into a temporary folder and loads them from there.
- Zip files are limited to 4 GB. Files kept outside the archive can be larger.
- To read a file inside a zip file, use a [Workdir](../functors/Workdir.html) container. Set its `folder` input port to the zip file name, and place a loader such as [Load Map](../functors/Load-Map.html) or [Load Weights](../functors/Load-Weights.html) inside it. The file name in the loader must match the name of the file in the archive.
{% endraw %}
