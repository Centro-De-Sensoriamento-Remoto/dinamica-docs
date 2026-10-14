---
title: "Genetic Algorithm Tool"
nav_exclude: true
---
{% raw %}
# Genetic Algorithm Tool

## Description

This container is a global optimization tool that solves a genetic algorithm, mimicking the principles of biological evolution, to search for a global optimization solution for the model it contains. It evolves a population of candidate individuals across generations, guided by a fitness value that the contained model computes for each individual, and returns the best individual found across all generations.

The [Get Current Individual](Get-Current-Individual.html) and [Set Fitness](Set-Fitness.html) functors must be placed inside this container: the former retrieves the individual being evaluated in the current iteration, and the latter reports the fitness value calculated for that individual back to this container.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Use Convergence Stopping Criteria | [Boolean Value Type](Boolean-Value-Type.html) | If true, the optimization process halts once the evolution of generations becomes asymptotic, as defined by Convergence Limit. If false, the process runs for the total number of generations specified by Number Of Generations. |
| Number Of Generations | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | If Use Convergence Stopping Criteria is true, this specifies the minimum number of generations needed to detect convergence. Otherwise, it is the maximum number of generations. |
| Population Size | [Positive Integer Value Type](Positive-Integer-Value-Type.html) | Number of individuals per population. |
| Individual Genotype | [Lookup Table Group Type](Lookup-Table-Group-Type.html) | Genotype that defines the template for individuals. |
| Default Lower Bound | [Real Value Type](Real-Value-Type.html) | Default lower value for alleles. Must be less than Default Upper Bound. |
| Default Upper Bound | [Real Value Type](Real-Value-Type.html) | Default upper value for alleles. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Convergence Limit | [Percent Type](Percent-Type.html) | Convergence limit, as a percentage of fitness variation across the given number of generations, used to halt the optimization process when Use Convergence Stopping Criteria is true. This is an advanced port. | 0.99 |
| Lower Bound | [Lookup Table Group Type](Lookup-Table-Group-Type.html) | Lower limits per allele. Missing limits fall back to Default Lower Bound. This is an advanced port. | None |
| Upper Bound | [Lookup Table Group Type](Lookup-Table-Group-Type.html) | Upper limits per allele. Missing limits fall back to Default Upper Bound. This is an advanced port. | None |
| Meta Heuristic Evaluation Percent | [Percent Type](Percent-Type.html) | Percentage of individuals whose fitness is estimated using a meta-heuristic (KNN) instead of being calculated by the contained model. This is an advanced port. | None |
| Maximum Log Level | [Log Tag Type](Log-Tag-Type.html) | Maximum log level used while running the contained functors. This is an advanced port. | Warning |
| Sequence Input | [None Type](None-Type.html) | Ensures that the functor connected to this port runs before this container. | None |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Best Individual | [Lookup Table Group Type](Lookup-Table-Group-Type.html) | Best individual found across all generations. |
| Best Individual Fitness | [Real Value Type](Real-Value-Type.html) | Fitness value of the overall best individual. |
| Best Fitness Per Generation | [Lookup Table Type](Lookup-Table-Type.html) | Fitness value of the best individual, for each generation. |
| Worst Fitness Per Generation | [Lookup Table Type](Lookup-Table-Type.html) | Fitness value of the worst individual, for each generation. |
| Sequence Output | [None Type](None-Type.html) | Ensures that this container runs before the functor connected to this port. |

## Group

[Calibration](Functor-List.html#calibration)

## Internal Outputs

| Name | Type | Description |
| --- | --- | --- |
| Current Individual | [Lookup Table Group Type](Lookup-Table-Group-Type.html) | Individual being evaluated in the current iteration. |

## Internal Inputs

| Name | Type | Description |
| --- | --- | --- |
| Fitness | [Real Value Type](Real-Value-Type.html) | Fitness value calculated for the current individual. |

## Notes

A summary of the algorithm this container implements: first, an initial population is generated using Individual Genotype as a seed and the given bounds as limits for each allele. Then, for each generation, the fitness of every individual is calculated and the best individual is recorded; a portion of the population is selected through tournament, and those individuals are reproduced through crossover and mutation to form the next generation. This repeats until the stopping criteria set by Use Convergence Stopping Criteria is reached, at which point the best individual found across all generations is returned.

When Use Convergence Stopping Criteria is true, convergence is detected when the best fitness value has not improved by at least the minimum percentage (1 - Convergence Limit) across the window formed by the last Number Of Generations generations.

When Meta Heuristic Evaluation Percent is set, that percentage of individuals have their fitness estimated with the [KNN algorithm](https://en.wikipedia.org/wiki/K-nearest_neighbor_algorithm) instead of being evaluated by the contained model. This estimation is only used after a portion of the generations have run (typically 30% of the total), so that the KNN algorithm has enough prior results to estimate from.

A "dcf" file holding Weights of Evidence ranges and coefficients can be converted to a corresponding set of "csv" tables, and back, with the ConvertWeightFiles utility, which is useful for calibrating those coefficients with this container.

Reports an error if Default Lower Bound is not less than Default Upper Bound.

Reports an error if Use Convergence Stopping Criteria is true and Convergence Limit is zero.

Reports a warning that cancelling or interrupting the execution of a model using this container may crash the application.

## Internal Name

GeneticAlgorithmTool
{% endraw %}
