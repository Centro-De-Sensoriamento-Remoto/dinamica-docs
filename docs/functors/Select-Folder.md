---
title: "Select Folder"
nav_order: 1
parent: "Stack Functors"
grand_parent: "Functor List"
redirect_from:
  - /Select-Folder.html
---
{% raw %}
# Select Folder

## Description

This container picks a folder out of a series of folders identified by [Number Folder](Number-Folder.html) functors placed inside it, using an index to choose among them.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Step | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Current index, step, or model iteration, used to pick the folder. When this functor is placed inside a loop container, this port connects to that container's current step automatically. | Provided automatically |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Folder | [Folder Type](../types/Folder-Type.html) | Folder picked out of those present in the series. |

## Group

[Stack](../Functor-List.html#stack)

## Notes

The folder selected is the one identified with the greatest index that is still less than or equal to Step.

Folders are identified using an index assigned by a [Number Folder](Number-Folder.html) functor placed inside this container.

This container must hold at least one [Number Folder](Number-Folder.html) instance; otherwise the model raises an error. If Step is smaller than every index assigned inside the container, the model also raises an error.

## Internal Name

SelectFolder
{% endraw %}
