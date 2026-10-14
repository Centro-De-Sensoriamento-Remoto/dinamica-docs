---
title: "Date Type"
nav_order: 3
parent: "Type System"
grand_parent: "Core Concepts"
redirect_from:
  - /Date-Type.html
---
{% raw %}
# Date Type

A Date value represents a calendar date — for example, [Set Kml Timeline](../functors/Set-Kml-Timeline.html)'s `beginTime` and `endTime` inputs use it to bound the period a georeferenced image applies to within a [Kml Timeline](Kml-Timeline-Type.html). A Date can represent a year alone (`YYYY`), a year and month (`YYYY-MM`), or a complete date (`YYYY-MM-DD`).

## GUI Editor

Date Type has no editor. A value can only be obtained through the automatic conversion below, never typed in directly.

## EGO Script

For the same reason, Date Type has no literal constant syntax in [EGO Script](../EGO-Script.html) — see [Constants](../EGO-Script.html#constants). A Date value is obtained through an automatic conversion from [Real Value](Real-Value-Type.html) or [String](String-Type.html) wherever a Date Type input is expected:

```
timeline := SetKmlTimeline {
    kml = georeferencedImage,
    beginTime = "2020-01",
    endTime = "2020-12-31"
};
```

## Automatic Conversions

- **Converted from**: [Real Value Type](Real-Value-Type.html) and [String Type](String-Type.html).
- **Converted to**: None.

See [Type System](../Type-System.html) for the complete conversion reference across all types.
{% endraw %}
