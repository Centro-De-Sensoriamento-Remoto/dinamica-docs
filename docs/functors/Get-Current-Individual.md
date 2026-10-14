---
title: "Get Current Individual"
nav_order: 7
parent: "Calibration Functors"
grand_parent: "Functor List"
redirect_from:
  - /Get-Current-Individual.html
---
{% raw %}
# Get Current Individual

## Description

When placed inside a [Genetic Algorithm Tool](Genetic-Algorithm-Tool.html) container, this functor retrieves the individual being evaluated in the current iteration of the genetic algorithm.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Current Individual | [Lookup Table Group Type](../types/Lookup-Table-Group-Type.html) | Individual from the current genetic algorithm iteration. When this functor is placed inside a Genetic Algorithm Tool container, this port connects to that container's current individual automatically. This is an advanced port. | Provided automatically |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Current Individual | [Lookup Table Group Type](../types/Lookup-Table-Group-Type.html) | Individual from the current genetic algorithm iteration. |

## Group

[Calibration](../Functor-List.html#calibration)

## Notes

This functor must be placed inside a Genetic Algorithm Tool. If it is not, it has no effect, and a warning is reported when the script is verified.

## Internal Name

GetCurrentIndividual
{% endraw %}
