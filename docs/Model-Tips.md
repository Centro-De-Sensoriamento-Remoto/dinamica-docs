---
title: "Useful Tips for Creating Models"
nav_order: 6
parent: "Modeling Guides"
---
{% raw %}
# Useful Tips for Creating Models

The following are useful tips for creating models.

## File Paths

The Dinamica EGO interface shows absolute filepaths for easier reading, but they are relative indeed. So, to easily change the location of a model, keep the same path between the script file ([ego](EGO-Script.html) or [xml](EGOML-Script.html)) and your data directory. This will work as expected.

## Workdir

The following functors can be placed, directly or indirectly, inside a **[Workdir](functors/Workdir.html)**: [Load Map](functors/Load-Map.html), [Load Categorical Map](functors/Load-Categorical-Map.html), [Load Table](functors/Load-Table.html), [Load Lookup Table](functors/Load-Lookup-Table.html), [Load Weights](functors/Load-Weights.html), [Save Map](functors/Save-Map.html), [Save Table](functors/Save-Table.html), [Save Lookup Table](functors/Save-Lookup-Table.html), and [Save Weights](functors/Save-Weights.html).

When placed inside a Workdir, the file name used by the functor becomes relative to the folder defined by the Workdir. This simplifies switching the input data folder for multiple functors in the same model. You can use several [Workdir](functors/Workdir.html) in the same model.

See the model `mato grosso road with workdirs.egoml` in `guidebook dinamica\extras\examples\run lucc northern mato grosso\run roads with and workdirs` of the [Guidebook dataset](extra/guidebook_dinamica.7z).

## Loading Files from Zip Files

Maps, tables, lookup tables and Weights of Evidence files can be loaded from [zip](https://en.wikipedia.org/wiki/Zip_(file_format)) files.

[Zip](https://en.wikipedia.org/wiki/Zip_(file_format)) files are useful to pack all files used by a model in a single archive. However, zipping all files does not increase the amount of data that Dinamica EGO can handle simultaneously. Behind the curtains, Dinamica unzips the files into a temporary folder and loads them from there.

[Zip](https://en.wikipedia.org/wiki/Zip_(file_format)) files are also limited to 4 GBytes in Dinamica. If you use a file outside the zip archive, these files can be much bigger than that.

To read a file located in a [zip](https://en.wikipedia.org/wiki/Zip_(file_format)) file, you have to use a [Workdir](functors/Workdir.html) container. Then, edit the [Workdir](functors/Workdir.html) and use the [zip](https://en.wikipedia.org/wiki/Zip_(file_format)) file name in the "folder" input port. Place a file loader ([Load Map](functors/Load-Map.html), [Load Weights](functors/Load-Weights.html) etc) inside the [Workdir](functors/Workdir.html) container. The file name mentioned in the file loader must match the name used by the file contained in the [zip](https://en.wikipedia.org/wiki/Zip_(file_format)) archive.

## Loops

A loop executes multiple steps simultaneously when **all** of the following conditions are met:

- No connection is passed out of the loop.
- No Mux functor is used directly inside the loop.
- No member of the loop is expected as an output port of a submodel.

Sometimes, however, it is convenient to force a loop that *could* run its steps simultaneously to run them sequentially instead. A simple way to do this is to place a `MuxValue 0 0` functor inside the loop. See [Basic Data Flow](Basic-Data-Flow.html) for why these conditions hold — a loop's iterations are only independent, and therefore only parallelizable, when nothing connects one to the next.

## Create String

In the formatting parameters of **[Create String](functors/Create-String.html)**:

- **Padding** specifies the *total length* of the final string, in number of characters, including characters such as `"."` and `"-"`.
- **Precision** specifies the total number of numeric digits, before any padding is added.

For example, the value `-14.0392632603687`, formatted as `"<v1, 7, 4>"` (7 characters of padding and 4 digits of precision), produces `"0-14.04"`. The leading `"0"` corresponds to the padding.

## Calculate Python Expression

Packages can be installed either by calling `dinamica.package(...)` from within the expression (runs during execution, so it can be called conditionally) or by listing them on the *packages* input port (installed before the script runs). See [Calculate Python Expression — Utilities](functors/Calculate-Python-Expression.html#utilities) for the full `dinamica.package()` syntax and examples.

## Calculate R Expression

Packages can be installed from **[Calculate R Expression](functors/Calculate-R-Expression.html)** using the `dinamicaPackage("package name")` function (one function call per package). `dinamicaPackage("package")` also acts as an `import` clause: when the package name is the same as the name of the module to be loaded via `import`, the package is installed and the module of the same name is loaded. See [Calculate R Expression — Installing Packages](functors/Calculate-R-Expression.html#installing-packages) for more detail.

## Wizards

See [Wizards](gui/Functor-And-Port-Editors.html#wizards) in the Graphical Interface section.

## Performance

- Avoid the definition of maps using [cell type](types/Cell-Type.html) "1 Bit Integer". This cell type saves memory, but it also has a huge negative impact in performance.
- Keep updated the Dinamica EGO installed in your system.
{% endraw %}
