---
title: "Expressions, Groups and Aliases"
parent: Map Viewer
grand_parent: Graphical Interface
nav_order: 3
---
{% raw %}
# Expressions, Groups and Aliases

Expressions calculate new values over the loaded maps, map groups let one expression run over several maps, and aliases give maps descriptive names.

## Expressions and Map Groups

### Calculate Expression

The Map Viewer accepts calculate expressions that are executed on each loaded map or on each [map group](#map-groups). The text area colors the known elements automatically. The expression syntax is described in [Image Expression Type](../types/Image-Expression-Type.html). The default expression for a loaded map is `i1`.

![Calculate expression dialog](../image/map_viewer_calculate_expression.png)

### Map Groups

A map group is created from a series of maps in the stack. Groups aggregate information and allow a single calculate expression to run over several maps.

#### Creating a Map Group

Click the "Create map group" toolbar button. In the dialog that opens, select maps in the left column (the loaded stack) and move them to the right column to build the new group.

![Create map group dialog](../image/map_viewer_create_group.png)

The new group looks like a normal loaded map, except that it lists the maps in the group with their indices for use in the [calculate expression](#calculate-expression).

![New group](../image/map_viewer_new_group.png)

## Map Alias

An alias gives a map a more meaningful name in the Map Viewer.

> **Important:** Aliases are used only by the Map Viewer. Other components of Dinamica EGO do not use them, and they have no impact on simulations.

### Setting an Alias

1. Load a map. See [Loading Maps](Map-Viewer-Interface.html#loading-maps).
2. Click the information icon ![Information icon](../image/map_viewer_map_information_icon.png) to show the map information.
3. In the dialog, type the new alias in the top text field.

   ![Map information dialog](../image/map_viewer_map_info.png)

4. Click "Apply map alias" ![Apply map alias](../image/map_viewer_apply_map_alias.png) to set the alias, or "Restore original alias" ![Restore original alias](../image/map_viewer_restore_original_alias.png) to revert it.

You can also change the alias by double-clicking the map name or alias in the "Maps" window.

![Changing the alias in the Maps window](../image/map_viewer_change_alias.gif)

After the change, the alias is shown wherever the map file name would appear: the legend, the map information dialog, and the movie maker.

![Alias shown in the legend](../image/map_viewer_map_alias_showing.png)
{% endraw %}
