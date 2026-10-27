---
title: "Name Map"
nav_order: 54
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Name Map

## Description

Placeholder used to register a map under a given name in the environment of the container it is placed inside. This functor produces no output itself: the enclosing container inspects its input ports and performs the actual registration.

This functor can be placed inside [Calculate Map2](Calculate-Map2.html), [Calculate Categorical Map2](Calculate-Categorical-Map2.html), [Calc W Of E Probability Map](Calc-W-Of-E-Probability-Map.html), [Determine Weights Of Evidence Coefficients](Determine-Weights-Of-Evidence-Coefficients.html), [Determine Weights Of Evidence Continuous Occurrences](Determine-Weights-Of-Evidence-Continuous-Occurrences.html), [Determine Weights Of Evidence Correlation](Determine-Weights-Of-Evidence-Correlation.html), and [Determine Weights Of Evidence Ranges](Determine-Weights-Of-Evidence-Ranges.html).

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Map | [Map Type](../types/Map-Type.html) | Map to register in the environment. |
| Map Name | [Name Type](../types/Name-Type.html) | Name under which the map will be known inside the container. |

## Optional Inputs

None.

## Outputs

None.

## Group

[Map Algebra Supplementary](../Functor-List.html#map-algebra-supplementary)

## Notes

This functor's banner shows the value of Map Name.

Placing this functor inside a container it is not designed for reports a warning, since it has no effect there.

## Internal Name

NameMap
{% endraw %}
