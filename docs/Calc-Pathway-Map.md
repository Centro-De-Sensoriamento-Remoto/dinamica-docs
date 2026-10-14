---
title: "Calc Pathway Map"
nav_exclude: true
---
{% raw %}
# Calc Pathway Map

## Description

This functor calculates the shortest pathway between source features and an existing network of paths.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Network | [Categorical Map Type](Categorical-Map-Type.html) | Map of the initial network of paths. Non-null value cells represent paths. If Network does not define a null value, this functor reports an error during execution. |
| Sources | [Map Type](Map-Type.html) | Map of the source features from which pathways are searched for. Features are represented by non-null values. |
| Costs Or Directions | [Map Type](Map-Type.html) | Map of the cost of building paths connecting the chosen destinations to the closest network, or map of the direction toward the least-cost cell from the current cell. Negative or zero costs indicate places where the network already exists. |
| Input Represents Directions | [Boolean Value Type](Boolean-Value-Type.html) | If true, Costs Or Directions is assumed to represent cost directions; otherwise, it is assumed to represent costs. A cost-direction cell can only take the eight values corresponding to the directions of a Moore neighborhood: None=0, NW=1, N=2, NE=3, E=4, SE=5, S=6, SW=7, and W=8. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Use Lottery | [Boolean Value Type](Boolean-Value-Type.html) | If true, and Input Represents Directions is false, ties for the lowest cost are broken randomly. This is an advanced port. | No |
| Merge Networks | [Boolean Value Type](Boolean-Value-Type.html) | If true, the map of new paths is merged into the initial network map. | Yes |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Network | [Categorical Map Type](Categorical-Map-Type.html) | Map of the resulting network: the initial network map plus the new paths when Merge Networks is true, or just the new paths otherwise. Network has the same dimensions as the input Network map, and a single layer. |

## Group

[Map Algebra](Functor-List.html#map-algebra)

## Notes

A source feature is ignored by the pathway search if the cost or direction cell at its starting position equals the null value; if the null value is found at any other cell along a path, this functor reports an error.

This functor reports an error if a local minimum is found on the cost map.

Sources uses Map Type, rather than Categorical Map Type, so that Calc Destination Map can be connected directly to it in a typical road-construction arrangement.

## Internal Name

CalcPathwayMap

## Usage examples

See practical examples of this functor in Lesson 17: Building a land-use and land-cover change simulation model
{% endraw %}
