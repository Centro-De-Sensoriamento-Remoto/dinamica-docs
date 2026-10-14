---
title: "Workdir"
nav_order: 15
parent: "Input / Output Functors"
grand_parent: "Functor List"
redirect_from:
  - /Workdir.html
---
{% raw %}
# Workdir

## Description

This container sets the working directory used by the functors it contains to read and write files.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Folder | [Folder Type](../types/Folder-Type.html) | Working directory to be used by the contained functors. |

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

Folder can be set to a regular folder or to a zip file. Inside this container, filenames referring to maps, tables, and Weights of Evidence coefficients or ranges, among others, are resolved relative to this directory.

## Internal Name

Workdir
{% endraw %}
