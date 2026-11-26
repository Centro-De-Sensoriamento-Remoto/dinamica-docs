---
title: "Release Notes 8.15.0"
nav_exclude: true
---
{% raw %}
# Dinamica EGO 8.15.0

> **Development version.** Dinamica EGO 8.15.0 is currently under development. This list may change before release.

Changes compared to version [8.14.0](Release-Notes-8-14-0.html).

## 1. Image expressions

- **Local variables** - `let _a: EXPR, _b: EXPR in EXPR` declares local variables in image expressions. Each binding is evaluated once and can use the previous ones. See [Local Variables](Calculate-Functors.html#local-variables-let--in).
- **Neighborhood reduce** - `nbReduce(iX, INIT, REDUCE, h, w)` combines the cells of a window into a single value. The accumulator `_acc` starts with `INIT`, and `REDUCE` combines it with each cell of the window, available through `_elem`, `_eline`, `_ecolumn` and `_eindex`. It is available in Calculate Map, Calculate Categorical Map and Calculate Multiple Maps. See [Neighborhood Reduce Operator](Calculate-Functors.html#10-neighborhood-reduce-operator).
- **Null-preserving position access** - the new expression `iX[[line, col]]` returns the value of an image at the given position, like `iX[line, col]`, but returns null instead of 0 when the cell is null. See [Image Operators and Functions](Calculate-Functors.html).
- Fixed the GPU implementation of `iX[line, col]`, which returned null instead of 0 for a null cell. It now behaves like the CPU implementation.
- Fixed expressions that combine `iX[line, col]` with elements not supported on accelerator devices, such as `nbMinRef(...) + i1[line, column]`. Depending on the order of the elements, these expressions were marked as compatible with accelerator devices and sent to them. They now run on the processors.
- Fixed the neighborhood functions in image expressions compiled to native code, which read the cells of the window as 32-bit real numbers. In maps of 64-bit real numbers, the values of the window lost precision.

---

## 2. Calculate Multiple Maps

- New functor [Calculate Multiple Maps](functors/Calculate-Multiple-Maps.html), shorthand `#*`, which evaluates a struct expression and returns one map for each field in a [Struct](types/Struct-Type.html).
- New functor [Extract Struct Map](functors/Extract-Struct-Map.html), which retrieves a map from a Struct by name.

---

## 3. Performance

None of these changes affect results.

### Calculators

- **Skipping cells with null results** - Calculate Map, Calculate Categorical Map and Calculate Multiple Maps no longer evaluate the expression in cells where a null input map guarantees a null result. This is the case of expressions such as `i1 * 2 + i2` or `if isNull(i1) then null else i2`, where a null cell in `i1` always makes the result null. The cell is written as null without evaluating the expression or reading the other maps. In Calculate Multiple Maps, the cell is skipped only when the null input makes every field of the struct null. The input maps used this way are listed in the debug log, under the `FUNCTOR_EXECUTION` subsystem. The calculation on accelerator devices does not use this optimization.
- **Calculating only the non-null cells of a sparse map** - when a sparse input map of Calculate Map, Calculate Categorical Map or Calculate Multiple Maps guarantees a null result wherever its cells are null, the expression is evaluated only at the non-null cells of that map, and every other cell of the result is null. If several input maps meet this condition, the one with the fewest non-null cells is used. The optimization applies when less than 1% of the cells of the map are non-null or when the map has less than 5000 cells. It also applies to sparse maps that are virtualized to match the format of the other input maps. In this case, the calculation runs on the processors and without parallelism. The map used is listed in the debug log, under the `FUNCTOR_EXECUTION` subsystem. See [Null-strict maps](Calculate-Functors.html#null-strict-maps).
- **Result sparsity** - the `resultIsSparse` flag of Calculate Map, Calculate Categorical Map and Calculate Multiple Maps is replaced by the `resultSparsity` port, with the values `.dense`, `.sparse` and `.auto`. With `.auto`, the default, the result is sparse when only the non-null cells of a sparse map are calculated, as described above, and dense otherwise. Models created with earlier versions are converted automatically: `.no` becomes `.dense`, `.yes` becomes `.sparse`, and a model that does not set the flag uses `.dense`, because the flag defaulted to `.no`. When the flag is given by another functor, the model receives a calculation that converts it. See [Calculate Map](functors/Calculate-Map.html).
- **Filling sparse maps with null** - filling a sparse map with its null value no longer visits every cell of the map. Results of Calculate Map, Calculate Categorical Map and Calculate Multiple Maps created as sparse maps benefit from it when the optimization above is used.

### Loading maps

- **Loading sparse maps in parallel** - Load Map and Load Categorical Map with the storage mode `.loadAsSparse` now read the map using multiple tasks, as is already done for maps loaded in memory. Each task reads its part of the map and keeps only the non-null cells. Invalid real values (NaN and infinity) are read as null cells. The map is read by a single task when loading maps in parallel is disabled, for example with the `--disable-parallel-map-load` option of DinamicaConsole.
- **Loading maps in memory** - Load Map and Load Categorical Map read the cells of maps loaded in memory directly into the map, without an intermediate copy. This applies when the map is read by multiple tasks and by a single task.
- **Loading GeoTIFF maps stored in strips** - when Load Map and Load Categorical Map read a GeoTIFF (`.tif`) map stored in strips, in memory or with the storage mode `.loadAsSparse`, the map is read in whole strips, so that every strip is read only once. This applies when the map is read by multiple tasks and by a single task. The parts of the map whose strips are left out of the file, as in sparse maps saved with `SPARSE_OK`, are not read, and their cells are null.
- **Loading GeoTIFF maps stored in tiles** - when Load Map and Load Categorical Map read a GeoTIFF (`.tif`) map stored in tiles, in memory or with the storage mode `.loadAsSparse`, each tile is read and decoded only once. Maps in memory receive the cells of each tile directly. Tiles left out of the file are not read, as with strips, and their cells are null. With multiple tasks, the tiles that need to be read are divided among the tasks. This applies when the map is read by multiple tasks and by a single task.

### Maps kept on disk

- **GeoTIFF maps stored in tiles kept on disk** - when a GeoTIFF (`.tif`) map stored in tiles is kept on disk and read on demand, as with the storage mode Prefer Disk, each tile is read and decoded only once while it is in use. Tiles left out of the file, as in sparse maps saved with `SPARSE_OK`, are not read, and their cells are null. Reading a tiled map line by line, or by tasks that split the map in sections of lines, no longer decodes the same tiles again for each line. This applies to maps opened only for reading.
- **Maps stored in strips kept on disk** - when a map stored in strips, as most GeoTIFF (`.tif`) maps are, is kept on disk and read on demand, as with the storage mode Prefer Disk, its cells are kept in memory in groups of whole strips, and each strip is read whole, instead of in parts of 4 Kbytes. Strips left out of the file are not read and take no space in memory, as with tiles, and their cells are null. This applies to maps opened only for reading whose strips have at most 256 Kbytes.
- **Small maps kept on disk** - maps kept on disk and read on demand, as with the storage mode Prefer Disk, that have less than 2 Mbytes now keep in memory between 1/4 and 1/2 of their cells, as temporary maps already did. Maps with less than 64 Kbytes are still kept entirely in memory. This does not apply to the GeoTIFF maps stored in tiles described above, and maps stored in strips keep at least 8 groups of strips in memory.

### Extracting attributes and saving

- **Extracting attributes of sparse maps** - [Extract Map Attributes](functors/Extract-Map-Attributes.html) visits only the non-null cells of sparse maps, such as maps loaded with the storage mode `.loadAsSparse`, when calculating the dynamic and statistical attributes.
- **Extracting categorical attributes with sparse category maps** - when the category map of [Extract Categorical Map Attributes](functors/Extract-Categorical-Map-Attributes.html) is a sparse map, such as a map loaded with the storage mode `.loadAsSparse`, only its non-null cells are visited, since the cells whose category is null are ignored.
- **Saving maps** - [Save Map](functors/Save-Map.html) writes the cells to the file in blocks of lines instead of one line at a time, in every format except ASCII (`.asc`). Maps kept in memory are written directly from their cells, without an intermediate copy. Sparse maps are written by visiting only their non-null cells, instead of looking up each cell of the map. GeoTIFF (`.tif`) maps with a single layer are written to the file one whole strip at a time, without an intermediate copy.

---

## 4. Map files

- **GeoTIFF compression** - compressed GeoTIFF (`.tif`) maps are now saved with DEFLATE instead of LZW, and the compression uses up to 4 threads.
- **Sparse GeoTIFF maps** - sparse maps saved as GeoTIFF (`.tif`) leave out of the file the blocks whose cells are all null, using the `SPARSE_OK` creation option of GDAL. The files are smaller, and the blocks left out are read as null cells by Dinamica EGO and by other software that reads GeoTIFF files with GDAL.
- **ER Mapper maps with extra data** - ER Mapper (`.ers`) maps whose data file is larger than the header describes are now rejected when the map is opened, however they are loaded, including when kept on disk and read on demand.

---

## 5. Interface

### General

- Removed the Twitter entry from the Help menu.
- Opening the documentation of a functor from the graph action bar no longer hides the navigation panel of the documentation website.
- Fixed importing a submodel into a model that contains a hollow functor.
- Functor and submodel tooltips break their lines at the real width of the text, so lines are no longer broken too early or too wide.
- **Linux** - fixed the graph action bar, which could disappear or lose its transparency. OpenGL rendering is no longer forced, avoiding display problems on newer Linux systems.

### Functor editor

- **Highlighting** - the expression editor highlights the `let` and `in` keywords, the local variables and the separators of `let`/`in` bindings, and the variables of `nbReduce()`.
- **Identifiers shown with names and icons** - fixed several problems in expressions whose identifiers are shown with their names and icons. Long lines could extend past the right edge of the editor and hide part of the expression, the expression could be displayed incorrectly, the arrow keys could move the cursor to the wrong place, double-clicking an identifier did not always select it, and undo could stop working or restore the wrong text. Typing in long expressions is also faster.
- The expression editor opens showing the beginning of the expression.
- **Window size** - the functor editor window opens large enough to show its content without scroll bars whenever it fits on the screen.
- **Enlarging the window** - editors that benefit from more space, such as the editors of expressions, code, tables and lookup tables, now grow when the functor editor window is enlarged, sharing the additional height. Before, this only happened when the window had a single port.
- **Resizing** - port descriptions and messages are no longer displayed with wrong line breaks or cut off after resizing or scrolling the window, and the editors no longer flicker while the window is resized.
{% endraw %}
