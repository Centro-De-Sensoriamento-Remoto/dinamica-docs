---
title: "Histogram Editor"
parent: Map Viewer
grand_parent: Graphical Interface
nav_order: 3
---
{% raw %}
# Histogram Editor

The histogram window assigns a transformation from the original cell values (in any range) to the [palette](Color-Palette.html) range [0, 255]. Values smaller than the "From" limit become 0, and values greater than the "To" limit become 255. All other values are mapped through the histogram curve to the "Y" coordinate on the color palette on the left.

![Histogram editor](../image/map_viewer_histogram.png)

## Transformations

- **None**: no mapping. Cell values are used as they are.
- **Linear**: maps values linearly between the "From" and "To" limits.
- **Equalize**: builds a curve based on [histogram equalization](https://en.wikipedia.org/wiki/Histogram_equalization).
{% endraw %}
