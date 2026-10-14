---
title: "Get Environment Value"
nav_exclude: true
---
{% raw %}
# Get Environment Value

## Description

Returns a piece of information about the application or operating system environment.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Key | [Enum Type](Enum-Type.html) | Type of value to return: Temporary Directory, Model Directory, Model Temporary Folder, User Folder, User Submodel Folder, Store Submodel Folder, Dinamica EGO Application Folder, Dinamica EGO Version, Operating System, or Operating System Executable Extension. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Value | [String Type](String-Type.html) | Value for the selected Key. |

## Group

[Tools](Functor-List.html#tools)

## Notes

Model Directory raises an error if the current model script has not yet been saved to disk.

## Internal Name

GetEnvironmentValue
{% endraw %}
