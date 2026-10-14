---
title: "Extract Categorical Map Attributes"
nav_order: 28
parent: "Map Algebra Functors"
grand_parent: "Functor List"
redirect_from:
  - /Extract-Categorical-Map-Attributes.html
---
{% raw %}
# Extract Categorical Map Attributes

## Description

Calculates basic statistics from a map for each class delimited by a categorical map, returning them as a table indexed jointly by attribute and class. All layers of the map are analyzed together, and the resulting table refers to them jointly.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Map whose attributes will be extracted. |
| Categorical Map | [Categorical Map Type](../types/Categorical-Map-Type.html) | Map of classes used to delimit the calculation area for each class in Map. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Extract Statistical Attributes | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, statistical attributes (mean, variance, standard deviation, mode, median, unique count) are also extracted. | Yes |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Attributes | [Table Type](../types/Table-Type.html) | Table of extracted attributes, keyed by attribute and by class. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

Attributes has columns "Attribute" (key, the attribute's numeric code) and "Category" (key, the class value from Categorical Map), with the corresponding statistic in the "Value" data column.

Each attribute has a predefined name that can be used to retrieve it by name (rather than by numeric key) in [Calculate Map](Calculate-Map.html), [Calculate Categorical Map](Calculate-Categorical-Map.html), [Calculate Value](Calculate-Value.html), and the lookup table calculators.

If an attribute cannot be determined for a class, its entry is omitted from Attributes rather than being filled with a placeholder. Minimum and maximum values are only determined when the class has at least one non-null cell.

Dynamic attributes, computed across all non-null cells of all layers within each class:

| Key | Predefined Name | Description |
| --- | --- | --- |
| 8 | "nullCells" | number of null cells |
| 9 | "nonNullCells" | number of non-null cells |
| 10 | "minCell" | minimum value (excluding null cells) |
| 11 | "maxCell" | maximum value (excluding null cells) |
| 12 | "cellSum" | sum of the values (excluding null cells) |

Statistical attributes (present only when Extract Statistical Attributes is true), computed across all non-null cells of all layers within each class:

| Key | Predefined Name | Description |
| --- | --- | --- |
| 13 | "meanCell" | average (excluding null cells) |
| 14 | "cellVar" | variance (excluding null cells) |
| 15 | "cellStd" | standard deviation (excluding null cells) |
| 16 | "modeCell" | mode (excluding null cells) |
| 17 | "medianCell" | median (excluding null cells) |
| 18 | "uniqueCells" | total unique occurrences (excluding null cells) |

## Internal Name

ExtractCategoricalMapAttributes
{% endraw %}
