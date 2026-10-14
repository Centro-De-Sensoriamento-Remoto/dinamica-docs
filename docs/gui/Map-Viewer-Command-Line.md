---
title: "Map Viewer Command Line"
parent: Map Viewer
grand_parent: Graphical Interface
nav_order: 7
---
{% raw %}
# Map Viewer Command Line

The Map Viewer can run as a command line tool that loads an `.egov` file (a saved viewer state) and saves the resulting stack of maps as a `.png` image.

```
"<Folder where Dinamica EGO is installed>\DinamicaMapViewer" <egov filename> <resulting png filename> [png width] [png height]
```

| Parameter | Description |
|---|---|
| egov filename | The location of the egov file. |
| resulting png filename | The location where the png file is saved. |
| png width | The width of the output png file. Optional. |
| png height | The height of the output png file. Optional. |

Example:

```
"C:\Program Files\Dinamica EGO\DinamicaMapViewer" "c:\Maps\maps.egov" "c:\Outputs\result.png" 800 600
```
{% endraw %}
