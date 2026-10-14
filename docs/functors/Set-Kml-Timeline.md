---
title: "Set Kml Timeline"
nav_order: 36
parent: "Map Algebra Functors"
grand_parent: "Functor List"
redirect_from:
  - /Set-Kml-Timeline.html
---
{% raw %}
# Set Kml Timeline

## Description

Adds a georeferenced KML to a KML timeline, associating it with the time interval given by Begin Time and End Time, so that it appears at the right point when the timeline is played back in Google Earth.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Kml | [Kml Type](../types/Kml-Type.html) | Georeferenced KML to add to the timeline. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Kml Timeline | [Kml Timeline Type](../types/Kml-Timeline-Type.html) | Existing timeline KML, already holding previously added maps, that Kml is appended to; the combined result is returned as Result. If not given, a new timeline is started. | .none |
| Begin Time | [Date Type](../types/Date-Type.html) | Date Kml should begin appearing in the timeline. Accepted formats are year (YYYY), year and month (YYYY-MM), or a complete date (YYYY-MM-DD). | .none |
| End Time | [Date Type](../types/Date-Type.html) | Date Kml should stop appearing in the timeline. Accepted formats are year (YYYY), year and month (YYYY-MM), or a complete date (YYYY-MM-DD). | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Kml Timeline Type](../types/Kml-Timeline-Type.html) | Resulting timeline KML, with georeferenced maps placed at their associated dates. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

None.

## Internal Name

SetKmlTimeline
{% endraw %}
