---
title: "Calc Patch Label Map"
nav_order: 14
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calc Patch Label Map

## Description

Labels patches of cells in a feature map using sequential numbers. A patch is a contiguous group of neighboring non-null cells; each patch found in Source is assigned its own label in the output map, starting from Initial Patch Label.

Neighboring cells are searched using a window of Window Lines by Window Columns cells, centered on each cell; even window dimensions are automatically rounded up to the nearest odd number. By default, this window is 3x3 and considers cells touching diagonally as well as orthogonally as neighbors, unless Only Orthogonals Are Allowed restricts adjacency to horizontal and vertical neighbors only. Using a window larger than 3x3 allows cells that are not directly touching to still be identified as part of the same patch, bridging small gaps between them.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Source | [Map Type](../types/Map-Type.html) | Map of features. Non-null cells correspond to an occurrence of a feature. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Initial Patch Label | [Integer Value Type](../types/Integer-Value-Type.html) | Label assigned to the first patch found in Source. This is an advanced port. | 1 |
| Only Orthogonals Are Allowed | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, only cells connected horizontally or vertically are considered neighbors. This is an advanced port. | No |
| Window Lines | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number of lines of the neighbor search window. This is an advanced port. | 3 |
| Window Columns | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Number of columns of the neighbor search window. This is an advanced port. | 3 |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Cell type of the output map. | Signed 32 Bit Integer |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Null value of the output map. | -2147483648 |
| Patch Labels Are Sparse | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, forces the output map to be saved as a sparse raster set, which stores only non-null cells, trading slower access time for reduced storage. This is an advanced port. | No |
| Use Sequential Patch Labels | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, patch labels are assigned sequentially with no gaps. Otherwise, the label sequence used to identify patches may contain gaps. This is an advanced port. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Patch Labels | [Categorical Map Type](../types/Categorical-Map-Type.html) | Map with the same dimensions as Source, where each cell holds the label of the patch it belongs to. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

Raises an error if Cell Type is not compatible with categorization, or if Null Value is not compatible with Cell Type.

## Internal Name

CalcPatchLabelMap
{% endraw %}
