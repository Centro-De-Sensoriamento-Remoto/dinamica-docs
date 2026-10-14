---
title: "Load Weights"
nav_order: 8
parent: "Input / Output Functors"
grand_parent: "Functor List"
redirect_from:
  - /Load-Weights.html
---
{% raw %}
# Load Weights

## Description

Loads Weights of Evidence coefficients or ranges from a file. The file format is determined automatically from the filename's extension.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Filename | [Weights Filename Type](../types/Weights-Filename-Type.html) | Name and path of the file to load. If no path is given, the file is located relative to the model script. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Suffix Digits | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Number of digits used to render Step as a filename suffix. If Step needs more digits than this, it is used unmodified. If zero, no suffix is added. This is an advanced port. | 0 |
| Step | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Current step or model iteration, appended to Filename as a numeric suffix; automatically bound to the innermost compatible container. This is an advanced port. | .none |
| Workdir | [Workdir Type](../types/Workdir-Type.html) | Work directory Filename is relative to; may be a folder or a Zip archive. When not bound, the directory containing the script is used. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Weights | [Weights Type](../types/Weights-Type.html) | Weights of Evidence coefficients or ranges loaded from the file. |

## Group

[Input / Output](../Functor-List.html#input--output)

## Notes

Two file formats are supported: the legacy DCF/TXT format, and CSV. In CSV format, the coefficients or ranges are represented as a table in the format "From\*:real, To\*:real, Variable\*:string, Range_Lower_Limit\*:real, Range_Upper_Limit\*:real, Weight:real" (the Range_Upper_Limit column is optional).

If Step is .none, the loaded filename has no numeric suffix.

The loaded Weights of Evidence coefficients or ranges can be edited directly by clicking on this functor's editor.

Workdir may point to a folder or to a Zip archive, allowing Weights files to be loaded directly from a Zip file.

## Internal Name

LoadWeights
{% endraw %}
