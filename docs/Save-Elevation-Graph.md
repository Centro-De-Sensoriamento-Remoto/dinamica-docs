---
title: "Save Elevation Graph"
nav_exclude: true
---
{% raw %}
# Save Elevation Graph

## Description

This functor saves an elevation patch graph using the Graphviz DOT format, the JSON format, or both.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Elevation Graph | [Elevation Graph Type](Elevation-Graph-Type.html) | Elevation patch graph created from neighborhood relationships and their properties. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Dot Filename | [Generic Filename Type](Generic-Filename-Type.html) | Filename where Elevation Graph is saved in the Graphviz DOT format, if provided. Useful for debugging, or for transferring the elevation graph to other software. This is an advanced port. | .none |
| Json Filename | [Generic Filename Type](Generic-Filename-Type.html) | Filename where Elevation Graph is saved in the JSON format, if provided. Useful for debugging, or for transferring the elevation graph to other software. This is an advanced port. | .none |

## Outputs

None.

## Group

[Elevation Graph: Debug](Functor-List.html#elevation-graph-debug)

## Notes

This functor reports an error if neither Dot Filename nor Json Filename is provided.

## Internal Name

SaveElevationGraph
{% endraw %}
