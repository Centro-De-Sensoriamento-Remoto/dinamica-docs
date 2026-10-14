---
title: "Assign Map Categories"
nav_exclude: true
---
{% raw %}
# Assign Map Categories

## Description

Copies an input map to the output and assigns it a given categorization, either replacing the map's existing categorization or combining the two.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Input Map | [Map Type](Map-Type.html) | Map that receives the new categorization. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Input Categories | [Categorization Type](Categorization-Type.html) | Categorization to assign to the output map. If not specified, the categorization is automatically generated from the image values. | None |
| Combine Categories | [Boolean Value Type](Boolean-Value-Type.html) | If true, combines Input Categories with the input map's own categorization. If false, the input map's categorization is replaced by Input Categories. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Output Map | [Categorical Map Type](Categorical-Map-Type.html) | Copy of the input map with the new categorization. |

## Group

[Map Algebra](Functor-List.html#map-algebra)

## Notes

When Combine Categories is true, categories from Input Categories take priority over the input map's own categorization: if both define a category under the same name or value, the input map's category is replaced by the one from Input Categories.

## Internal Name

AssignMapCategories
{% endraw %}
