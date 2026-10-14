---
title: "Useful Tips for Using the Graphical Interface"
nav_order: 18
---
{% raw %}
# Useful Tips for Using the Graphical Interface

The following are useful tips for working with the graphical interface.

## All Panels

You can perform searches using special options. For example, `is:functor` shows only functors, and `is:loop` shows only containers that are loops. These commands are valid in every search box of the interface. To use them, the **"Also search for additional info"** option must be enabled in the search box menu.

### Search Filters Common to All Panels

- `is:container`
- `is:loop`
- `is:junction`
- `is:carrier`
- `is:hook`
- `is:mux`
- `is:loader`
- `is:saver`
- `is:deprecated`
- `is:submodel`
- `is:systemsubmodel`
- `is:usersubmodel`
- `is:localsubmodel`
- `is:storesubmodel`
- `is:functor`

### Search Filters Specific to the Explorer

- `is:hollow`
- `is:submodelinput`
- `is:submodeloutput`

You can also search by values defined in the port editors of basic types: enter the value, or part of it, to find the functor containing the matching port. The basic types are `RealValue`, `BooleanValue`, `Percent`, `String`, `Name`, `Folder`, `NullValue`, `TableValue`, `TableCellType`, `IndexOrName`, `CellType`, `LogTag`, the `IntegerValue` type family, and the `Filename` type family.

### Search Filters Specific to the Issue Panel

- `is:hollow`
- `is:runtime`
- `is:error`
- `is:warning`

### Negated Search Patterns

Prefixing a search term with the `!` character excludes matching results instead of including them. This is supported by the Functor Library, the Explorer panel, the Issue panel, the Submodel Manager, and the search fields of the projection editor.

## Options (Tools => Options)

Several interface options are accessible from **Tools => Options**. They are grouped below by what each one actually controls.

### Number of Workers

The GUI option "Tools => Options | Advanced | Automatically detect the number of processors available" controls how many workers Dinamica EGO uses to execute a model in parallel. Here, "processors" refers to the number of CPU cores (or logical processors) available on the machine. If you are running your models using the command line, the equivalent is the "-processors" option, set to 0 for automatic detection (uses the total number of processor cores).

Automatic detection sizes the number of workers to the number of processors available. However, oversubscribing this number — i.e., using more workers than you have processors — can be beneficial when the task being executed is heavily I/O-bound, since workers spend part of their time waiting on I/O rather than using the CPU, and extra workers can keep the CPU busy during those waits.

### Memory Management

The memory management option "Tools => Options | Advanced" controls how Dinamica EGO handles input and resulting maps in memory versus on disk. If you are using the command line tool, the equivalent is the "-memory-allocation-policy" option.

Five policies are available:

- **Prefer Memory** — keeps input and resulting maps in memory whenever possible. If there isn't enough free memory, maps are stored on disk and brought back piece by piece. Execution might fail if there isn't enough free memory left for other operations.
- **Balanced** — keeps input maps on disk and tries to keep resulting maps in memory whenever possible, storing them on disk instead if memory is limited or if doing so could constrain memory available for other operations. *(-memory-allocation-policy 1)*
- **Prefer Disk** — keeps all maps, including resulting ones, on disk, loading them into memory piece by piece as needed.
- **Memory Only** — keeps input and resulting maps entirely in memory. If there isn't enough free memory, an error is reported and execution is aborted.
- **Aggressive** — keeps resulting maps in memory whenever possible, falling back to disk (and reloading piece by piece) only when memory is insufficient. *(-memory-allocation-policy 4)*

**Aggressive** is the preferred setting for maximizing performance, since it favors keeping resulting maps in memory. **Balanced** is a more conservative, safer choice — it keeps input maps on disk and is more cautious about keeping resulting maps in memory, reducing the risk of running low on memory for other operations at some cost to performance.

### Native Expression Compilation

Make sure the "Enhancement Plugin for Dinamica EGO" extension is installed and the GUI option "Tools => Options | Advanced | Disable compilation of native expressions" is unchecked. This allows expressions to be compiled to native code, which improves performance.

### Virtualization

The "Tools => Options | Advanced | Virtualization" option controls how Dinamica EGO handles maps with different extents, resolutions, or numbers of lines and columns (also known as raster map virtualization). See [Image Virtualization](Image-Virtualization.html) for the full explanation of what virtualization does and what each of the available options (Not Allowed, Unrestricted, Limited) means.

### Message Log Level

The GUI option "Tools => Options | System | Message log level" controls the amount of messages generated during model execution — it is not a performance setting. Setting it to Result reduces the volume of messages shown. *This helps when running models with lots of loop containers like [Repeat](Repeat.html), [While](While.html), [For](For.html) etc, which would otherwise generate a large number of messages*.

When the log level is set to Debug or above, it is also possible to define which specific debugging actions (called **log subsystems**) should be logged.

### Model Backups

The checkbox "Create backup copy of the current model script upon saving", under "Tools => Options | General | Model Backup", makes Dinamica EGO copy the content of a model script file every time it is about to be overwritten by a "Save" or "Save As" — this protects against accidental loss of a previous version of the model.

The "Backup Folder" field controls where these copies are placed. If left empty, copies are placed in the same folder as the original model. To restore a model to a previous state, copy the corresponding file back from the backup folder to its original location.

### EGO Script Formatting

The settings under "Options | EGO Script" control how a model selection is formatted when it is copied and pasted as EGO Script into an external text editor. See [Sketch](#sketch) for the copy/paste mechanism itself.

## Library

- You can instantiate a functor by dragging it or by double-clicking its name.
- When a functor is created by dragging its name, you can hold down the **Shift** key while dragging so that it is automatically connected to the functor currently selected in the sketch.
- The **Favorites** tab shows the functors that have been marked with a star. To mark a functor as a favorite, click the star next to its name.
- You can reorder the tabs ("All", "Favorites", etc.) by dragging a tab to its new position in the tab bar.
- A submodel's group in the Library — including subgroup placement — is set by whoever creates or edits it; see [Updating Local Submodels](Submodels.html#updating-local-submodels) for details. This does not apply to ordinary functors, whose Library placement is fixed by their own definition.

## Sketch

This panel is also referred to as the Model Presentation panel; see Model Presentation for the full reference on its panels and bars.

- You can zoom using the mouse wheel.
- You can pan by dragging the mouse while holding down the right button.
- If a selected functor is not visible, you can center the view on it by clicking its name in its action bar (the bar shown above a functor when it is selected).
- You can copy the path of the model open in the sketch by hovering the mouse over the tab bearing the model's name and pressing **Ctrl+C**, or by left-clicking the tab and choosing the corresponding option from the menu that opens. In this menu, you can choose between the full file name of the model and the name of the folder where the model is saved.
- To connect functors that are far apart and not visible on screen at the same time, select the source functor and—without selecting the destination functor—scroll the view so that the destination functor becomes visible (note that the source functor's action bar remains visible). Choose the "create connection" option in the action bar and click the destination functor. See Connecting Distant Functors for this and the alternative method below.
- Another way to connect distant functors that are not simultaneously visible is to use the selection-navigation mechanism:
  1. Click the source (output) functor. You may also simply search for this functor in the interface's functor Explorer and then click the **"View functor"** button in that Explorer.
  1. Do the same for the destination (input) functor.
  1. Click the connection button in the action bar and, while the connection is still in progress, press **Alt+Right Arrow**. This selects the destination functor and brings it into view.
  1. Click the destination functor to complete the connection.
- You can use **Alt+Right Arrow** and **Alt+Left Arrow** to navigate between your most recent functor selections: **Alt+Left Arrow** returns to the previous selection, and **Alt+Right Arrow** advances to the next one. You can also skip across multiple selections by holding **Alt** while moving from selection to selection with the arrow keys.
- When you select a connection between two functors, the connection action bar is shown in the upper-right corner of the sketch. Hovering the mouse over the name of each port in this action bar displays a tooltip for the port and for the functor it belongs to, including its banner, comment, and alias.
- The functor information panel (shown when you click the "?" icon in a functor's action bar) can be used to identify which connection represents the link to a given port of the functor. Click the desired port name in the port list, and the connection corresponding to that port is selected in the model view.
- The functor information panel can also be used to find out which port is connected, being edited, or being viewed. This information is shown next to the corresponding port name.
- You can reorder the tabs corresponding to the open models by dragging a tab to its new position in the tab bar.
- You can reorder the tabs corresponding to the local submodels of the open model by dragging a tab to its new position in the tab bar.
- The functor representation uses borders to convey certain information. More than one border can be visible at the same time:
  - **Yellow border** – the functor has one or more warnings.
  - **Red border** – the functor has one or more errors.
  - **Green border** – the functor exports input and/or output ports as part of a submodel.
  - **Blue border** – the functor's input and/or output ports are exported to a wizard. (Note: functors that are part of a submodel cannot export input and/or output ports to wizards.)
- After copying the current selection of the displayed model using **Copy Selection** or **Ctrl+C**, you can paste that selection into the same model, into another model, or into an external text editor.
  - When pasting into the **same model**, functors are reconnected to the output ports their original representations were connected to. Hold **Ctrl+Shift+V** to paste without this reconnection instead.
  - When pasting into **another model** or into an **external text editor**, ports connected to functors that were not selected and copied are shown as disconnected (`.UNBOUND`).
  - When pasting into an external text editor, the selection is pasted using the EGO Script representation of that fragment, written according to the settings specified in **Options | EGO Script**.
- Likewise, you can paste a script fragment into a model after copying it from an external text editor to the system clipboard. The only restriction is that the fragment must be syntactically valid. Ports connected to variables whose definitions were not copied are treated as disconnected.

## Drag and Drop

- Models, images, R and Python scripts, and files in general can be dragged into the sketch. What is done with the file depends on its representation.
- Dragging an R or a Python script into the sketch creates a [Calculate R Expression](Calculate-R-Expression.html) or a [Calculate Python Expression](Calculate-Python-Expression.html) functor, respectively. The script's content is used to fill in the `expression` port.
- A filename can be dragged into any filename editor (`MapFilename`, `TableFilename`, `Folder`, etc.). The filename is used to fill in the editor.
- If the application is run as administrator (using "Run as Administrator" or equivalent), drag and drop of files from Windows Explorer is disabled. This is done by Windows and affects any application, not just Dinamica EGO.

## Model Overview

- You can pan the model view in the Sketch panel by left-clicking on the desired part of the model in the overview representation. You can also right-click and drag to scroll the model content in the sketch.
- You can zoom the model view in the Sketch panel by right-clicking the small handle in the lower-right corner of the rectangle representing the currently visible Sketch area and dragging.
- You can also use the mouse wheel to zoom from within either the Overview or the Sketch. When zooming from the Sketch, the zoom is centered on the mouse location.

## Explorer

- In addition to showing the organization of functors and containers in the model, the Explorer panel shows useful information about certain functors in the **Attributes** column. This includes an indication of whether a loop can execute multiple steps simultaneously, and whether a functor has input and/or output ports exported as part of a submodel or wizard. To see what a given attribute means, hover the mouse over the attribute icon to view its tooltip.
- You can find out which functors in the model take the most time to execute. Click the **"Show model bottleneck only"** icon, and only the 10% of functors responsible for the largest total execution times are shown. This information is also available for the local submodel panels.

## Functor Editor

- Hovering the mouse over a port's description in an editor displays the tooltip for that port, showing its name, type, description, and flags.
- Hovering the mouse over a port's connection information ("This port input is being provided by...") displays the tooltip for the functor and output port to which the input port being edited is connected.

## Model Execution

- The progress bar shown in the lower-left corner of the interface during model execution has an additional function: hovering the mouse over it displays a tooltip with information about the execution, including which task each "worker" is performing. This tooltip keeps updating with the current execution status as long as the mouse pointer remains within it.

## Calculate Map / Calculate Categorical Map / Calculate Lookup Table Values / Calculate Lookup Table Keys And Values / Calculate Value

- Hovering the mouse over a name such as `i1`, `t1`, `v1`, etc. in the editor of the port containing the expression displays the tooltip for the functor and output port to which the corresponding NumberMap, NumberTable, or NumberValue is connected.
- Clicking a name such as `i1`, `t1`, `v1`, etc. in the editor of the port containing the expression inserts the corresponding identifier at the current cursor position in the expression.
- If the functor connected to the NumberMap, NumberTable, or NumberValue has an alias associated with it, that alias is used to represent the corresponding variable (`i1`, `t1`, `v1`, etc.) in the expression shown by the editor, making it easier to read.

## Issue Panel

- The Issue Panel also retains the most recent errors and warnings generated during model execution. To view them, keep the **"Also show last execution issues"** toggle enabled.
{% endraw %}
