---
title: "Library and Sketch"
parent: Graphical Interface
nav_order: 3
---
{% raw %}
# Library and Sketch

## Library

- You can instantiate a functor by dragging it or by double-clicking its name.
- When a functor is created by dragging its name, you can hold down the **Shift** key while dragging so that it is automatically connected to the functor currently selected in the sketch.
- The **Favorites** tab shows the functors that have been marked with a star. To mark a functor as a favorite, click the star next to its name.
- You can reorder the tabs ("All", "Favorites", etc.) by dragging a tab to its new position in the tab bar.
- A submodel's group in the Library — including subgroup placement — is set by whoever creates or edits it; see [Updating Local Submodels](Submodels-In-The-GUI.html#updating-local-submodels) for details. This does not apply to ordinary functors, whose Library placement is fixed by their own definition.

## Sketch

This panel is also referred to as the Model Presentation panel; see [Interface Elements](Interface-Elements.html#model-presentation) for the full reference on its panels and bars.

- You can zoom using the mouse wheel.
- You can pan by dragging the mouse while holding down the right button.
- If a selected functor is not visible, you can center the view on it by clicking its name in its action bar (the bar shown above a functor when it is selected).
- You can copy the path of the model open in the sketch by hovering the mouse over the tab bearing the model's name and pressing **Ctrl+C**, or by left-clicking the tab and choosing the corresponding option from the menu that opens. In this menu, you can choose between the full file name of the model and the name of the folder where the model is saved.
- To connect functors that are far apart and not visible on screen at the same time, select the source functor and—without selecting the destination functor—scroll the view so that the destination functor becomes visible (note that the source functor's action bar remains visible). Choose the "create connection" option in the action bar and click the destination functor.
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
  - When pasting into an external text editor, the selection is pasted using the EGO Script representation of that fragment, written according to the settings specified in **Options \| EGO Script**.
- Likewise, you can paste a script fragment into a model after copying it from an external text editor to the system clipboard. The only restriction is that the fragment must be syntactically valid. Ports connected to variables whose definitions were not copied are treated as disconnected.

## Drag and Drop

- Models, images, R and Python scripts, and files in general can be dragged into the sketch. What is done with the file depends on its representation.
- Dragging an R or a Python script into the sketch creates a [Calculate R Expression](../functors/Calculate-R-Expression.html) or a [Calculate Python Expression](../functors/Calculate-Python-Expression.html) functor, respectively. The script's content is used to fill in the `expression` port.
- A filename can be dragged into any filename editor (`MapFilename`, `TableFilename`, `Folder`, etc.). The filename is used to fill in the editor.
- If the application is run as administrator (using "Run as Administrator" or equivalent), drag and drop of files from Windows Explorer is disabled. This is done by Windows and affects any application, not just Dinamica EGO.
{% endraw %}
