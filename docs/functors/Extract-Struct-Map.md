---
title: "Extract Struct Map"
nav_order: 4
parent: "Integration Functors"
grand_parent: "Functor List"
---
{% raw %}
# Extract Struct Map

## Description

Extracts a map stored in a Struct, such as the one returned by [Calculate Multiple Maps](Calculate-Multiple-Maps.html), by its name.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Struct | [Struct Type](../types/Struct-Type.html) | Struct containing the map to extract. |
| Name | [String Type](../types/String-Type.html) | Name under which the map is stored in the struct. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Extracted map. |

## Group

[Integration](../Functor-List.html#integration)

## Notes

Raises an error if no map is stored under Name in Struct.

This functor's banner shows the value of Name.

## Internal Name

ExtractStructMap
{% endraw %}
