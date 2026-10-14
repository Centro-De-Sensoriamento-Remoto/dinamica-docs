---
title: "Create Kml"
nav_order: 24
parent: "Map Algebra Functors"
grand_parent: "Functor List"
redirect_from:
  - /Create-Kml.html
---
{% raw %}
# Create Kml

## Description

Creates a georeferenced KML file from a categorical map, so that the map can be opened and viewed in Google Earth.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Categorical Map Type](../types/Categorical-Map-Type.html) | Map from which the georeferenced KML is generated. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Kml | [Kml Type](../types/Kml-Type.html) | Resulting KML. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

[KML (Keyhole Markup Language)](https://en.wikipedia.org/wiki/Keyhole_Markup_Language) is an XML notation for describing geographic annotation and visualization in two-dimensional maps and three-dimensional Earth browsers, developed for use with Google Earth.

## Internal Name

CreateKml
{% endraw %}
