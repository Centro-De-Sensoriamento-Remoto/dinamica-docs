---
title: "Insert Map Layer"
nav_order: 34
parent: "Map Algebra Functors"
grand_parent: "Functor List"
redirect_from:
  - /Insert-Map-Layer.html
---
{% raw %}
# Insert Map Layer

## Description

Inserts or replaces a layer of a map at a given position.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Map the new layer is inserted into. |
| Layer | [Map Type](../types/Map-Type.html) | Map whose first layer will be inserted into Map. Any further layers are ignored. |
| Layer Position | [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html) | Position where the layer is inserted. A value of zero, or one greater than Map's current number of layers, appends the new layer at the end. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Layer Name | [Name Type](../types/Name-Type.html) | Name the layer receives inside Map. If the layer is being replaced and no name is given, the replaced layer's original name is kept; if the layer is being added and no name is given, a unique name is generated automatically. | .none |
| Replace Layer | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, the layer at Layer Position is replaced by the new layer. If false, the layer currently at that position, and every layer after it, is shifted forward to make room for the new layer. This flag has no effect when the new layer is appended at the end. | No |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Map containing the new layer alongside the layers it already had. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

Only the first layer of Layer is used; any further layers it has are ignored.

Layer must already be in the same format as Map; no conversion is performed.

## Internal Name

InsertMapLayer
{% endraw %}
