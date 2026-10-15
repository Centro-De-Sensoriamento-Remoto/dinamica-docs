---
title: "Set Fitness"
nav_order: 8
parent: "Calibration Functors"
grand_parent: "Functor List"
---
{% raw %}
# Set Fitness

## Description

Passes the fitness value calculated for the current individual to the nearest enclosing [Genetic Algorithm Tool](Genetic-Algorithm-Tool.html) container.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Fitness | [Real Value Type](../types/Real-Value-Type.html) | Fitness value calculated for the current individual. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Fitness | [Real Value Type](../types/Real-Value-Type.html) | Fitness value calculated for the current individual, passed to the enclosing Genetic Algorithm Tool container. |

## Group

[Calibration](../Functor-List.html#calibration)

## Notes

This functor must be placed inside a Genetic Algorithm Tool. Once the fitness of the current individual has been calculated, this functor reports that value back to the genetic algorithm.

## Internal Name

SetFitness
{% endraw %}
