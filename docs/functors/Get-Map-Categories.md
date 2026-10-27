---
title: "Get Map Categories"
nav_order: 32
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Get Map Categories

## Description

Extracts a copy of the categorization of a map.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Categorical Map | [Map Type](../types/Map-Type.html) | Map whose categorization will be extracted. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Categories | [Categorization Type](../types/Categorization-Type.html) | Categorization extracted from Categorical Map. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

Raises an error if Categorical Map has no categorization defined. If this is expected to happen, use a [Skip All On Error](Skip-All-On-Error.html) to intercept the error, and a [Calculate Categorical Map](Calculate-Categorical-Map.html) to derive the categories from the map's values instead.

## Internal Name

GetMapCategories
{% endraw %}
