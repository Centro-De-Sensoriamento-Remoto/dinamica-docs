---
title: "Get Projection Info"
nav_exclude: true
---
{% raw %}
# Get Projection Info

## Description

Retrieves descriptive information about a projection, in several standard representations.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Projection | [Projection Type](Projection-Type.html) | Projection whose information will be retrieved. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| WKT | [String Type](String-Type.html) | Projection expressed in WKT (well-known text) syntax. |
| ERMapper Equivalent Projection | [String Type](String-Type.html) | Projection's name using the equivalent ERMapper keyword, or an empty string if it has no ERMapper equivalent. |
| ERMapper Equivalent Datum | [String Type](String-Type.html) | Projection's datum name using the equivalent ERMapper keyword, or an empty string if it has no ERMapper equivalent. |
| ERMapper Equivalent Unit | [String Type](String-Type.html) | Projection's unit name using the equivalent ERMapper keyword, or an empty string if it has no ERMapper equivalent. |
| UTM Hemisphere | [Integer Value Type](Integer-Value-Type.html) | UTM hemisphere code, if Projection is UTM: 1 = North Hemisphere, 2 = South Hemisphere, -1 = not UTM. |
| UTM Zone | [Integer Value Type](Integer-Value-Type.html) | UTM zone code, if Projection is UTM, or -1 otherwise. |
| Coordinate Type | [Integer Value Type](Integer-Value-Type.html) | Coordinate type code: 1 = Eastings/Northings, 2 = Latitude/Longitude, -1 = undefined. |
| Proj4 | [String Type](String-Type.html) | Projection expressed in PROJ.4 syntax. |
| EPSG Code | [Integer Value Type](Integer-Value-Type.html) | Projection's EPSG code, if it has one, or -1 otherwise. |

## Group

[Map Algebra](Functor-List.html#map-algebra)

## Notes

None.

## Internal Name

GetProjectionInfo
{% endraw %}
