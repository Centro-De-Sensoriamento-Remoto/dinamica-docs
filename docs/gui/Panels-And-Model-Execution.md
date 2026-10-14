---
title: "Panels and Model Execution"
parent: Graphical Interface
nav_order: 4
---
{% raw %}
# Panels and Model Execution

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

## Model Overview

- You can pan the model view in the Sketch panel by left-clicking on the desired part of the model in the overview representation. You can also right-click and drag to scroll the model content in the sketch.
- You can zoom the model view in the Sketch panel by right-clicking the small handle in the lower-right corner of the rectangle representing the currently visible Sketch area and dragging.
- You can also use the mouse wheel to zoom from within either the Overview or the Sketch. When zooming from the Sketch, the zoom is centered on the mouse location.

## Explorer

- In addition to showing the organization of functors and containers in the model, the Explorer panel shows useful information about certain functors in the **Attributes** column. This includes an indication of whether a loop can execute multiple steps simultaneously, and whether a functor has input and/or output ports exported as part of a submodel or wizard. To see what a given attribute means, hover the mouse over the attribute icon to view its tooltip.
- You can find out which functors in the model take the most time to execute. Click the **"Show model bottleneck only"** icon, and only the 10% of functors responsible for the largest total execution times are shown. This information is also available for the local submodel panels.

## Issue Panel

- The Issue Panel also retains the most recent errors and warnings generated during model execution. To view them, keep the **"Also show last execution issues"** toggle enabled.

## Model Execution

- The progress bar shown in the lower-left corner of the interface during model execution has an additional function: hovering the mouse over it displays a tooltip with information about the execution, including which task each "worker" is performing. This tooltip keeps updating with the current execution status as long as the mouse pointer remains within it.
{% endraw %}
