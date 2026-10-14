---
title: "Calc Areas"
nav_exclude: true
---
{% raw %}
# Calc Areas

## Description

This functor calculates the area of each source feature.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Source | [Categorical Map Type](Categorical-Map-Type.html) | Map whose non-null cells correspond to categories or classes. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Use Authalic Area | [Boolean Value Type](Boolean-Value-Type.html) | If true, the area of each cell in a geographic (Lat/Long) grid is computed using an authalic sphere, which preserves surface area during projection. This improves the accuracy of area calculations across all latitudes by avoiding distortions. If the grid is geographic but this option is false, all cells are treated as having the same area, calculated by treating the length of one degree of latitude or longitude as a constant 111255 meters. This is an advanced port. | Yes |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Areas | [Table Type](Table-Type.html) | Area of each source feature, in cells, hectares, and square meters. |

## Group

[Map Algebra](Functor-List.html#map-algebra)

## Notes

Only the areas of classes or categories present in Source's categorization are calculated; other values are ignored.

The resulting table has the following format.

| Column Name | Key or Data? | Column Type | Description |
| --- | --- | --- | --- |
| "Category" | Key | Real | Category in the feature map |
| "Area_In_Cells" | Data | Real | Area of corresponding category in cells |
| "Area_In_Hectares" | Data | Real | Area of corresponding category in hectares |
| "Area_In_Square_Meters" | Data | Real | Area of corresponding category in square meters |

**References**

Santini, M., Taramelli, A. and Sorichetta, A., 2010: [ASPHAA: A GIS-Based Algorithm to Calculate Cell Area on a Latitude-Longitude (Geographic) Regular Grid](https://www.researchgate.net/publication/220606016_ASPHAA_A_GIS-Based_algorithm_to_calculate_cell_area_on_a_latitude-longitude_Geographic_regular_grid). Transactions in GIS, 14(3), 351-377.

## Internal Name

CalcAreas

## Usage examples

See practical examples of this functor in Lesson 9: Working with maps and tables
{% endraw %}
