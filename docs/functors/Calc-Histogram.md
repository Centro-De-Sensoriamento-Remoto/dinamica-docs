---
title: "Calc Histogram"
nav_order: 1
parent: "Statistics Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calc Histogram

## Description

Calculates a histogram from a map.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Any map. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Interval Width | [Real Value Type](../types/Real-Value-Type.html) | Width of each histogram interval (bin). | 1 |
| Cumulative | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, the calculated histogram is cumulative. | No |
| Relative | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, the values in the histogram are normalized by the total number of occurrences. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Histogram | [Lookup Table Type](../types/Lookup-Table-Type.html) | The calculated histogram. |

## Group

[Statistics](../Functor-List.html#statistics)

## Notes

Only the map's first layer is used to build the histogram.

Each key in the output table is the lower bound of an interval, obtained by rounding the corresponding cell value down to the nearest multiple of Interval Width; the associated value is the count of cells falling in that interval (or, if Relative is true, that count divided by the total number of non-null cells). Because of this rounding, the lowest and highest keys in the resulting table can fall outside the range of values actually present in Map.

Setting both Cumulative and Relative produces a histogram of cumulative relative frequencies.

Raises an error if Interval Width is not greater than 0.

## Internal Name

CalcHistogram
{% endraw %}
