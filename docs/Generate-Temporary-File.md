---
title: "Generate Temporary File"
nav_exclude: true
---
{% raw %}
# Generate Temporary File

## Description

Creates a temporary file, or simply reserves a temporary filename, guaranteeing that the name does not collide with any existing file.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Extension | [String Type](String-Type.html) | Extension for the generated temporary file, without the leading period. It must contain only letters and numbers. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Create File | [Boolean Value Type](Boolean-Value-Type.html) | If true, the file is created empty on disk. If false, only its path is reserved and no file is created. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Filename | [Generic Filename Type](Generic-Filename-Type.html) | Filename of the generated temporary file. |

## Group

[Input / Output](Functor-List.html#input--output)

## Notes

Extension must contain only letters and numbers. Providing an extension with any other character raises an error.

## Internal Name

GenerateTemporaryFile
{% endraw %}
