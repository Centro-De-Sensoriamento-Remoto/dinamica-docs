---
title: "Introduction"
parent: "Guidebook"
nav_order: 2
---
{% raw %}
# Introduction

![](../image/guidebook_logo_guidebook1.jpg)


Welcome to Dinamica EGO!

An **E**nvironment for **G**eoprocessing **O**bjects with simplicity, flexibility and good performance, optimizing speed and computer resources.

**In this section you will learn what Dinamica EGO is, what a functor is, how this guidebook is organized, and where its data and models are.**

## What is Dinamica EGO?

**Dinamica EGO** is a modeling environment, with outstanding possibilities for the design from the very simple static spatial model to very complex dynamic ones, which can ultimately involve nested iterations, dynamic feedbacks, multi-region approach, manipulation and algebraic combination of data in several formats, such as maps, tables, matrices and constants, decision processes for bifurcating and joining execution pipelines, and a series of complex spatial algorithms for the analysis and simulation of space-time phenomena.

The aim of this guidebook is to introduce the user to the numerous possibilities of **Dinamica EGO** for the design of models that can fully represent the complexity of various geographic phenomena.

Dinamica EGO has been applied to numerous environmental studies, including the modeling of deforestation in the Amazon from local to basin-wide scales, urban dynamics, logging and other forestry rents in the Amazon, cattle ranching, forest fires, river regime, biodiversity, and agricultural expansion in Brazil.

## What is a functor?

Dinamica EGO holds a series of algorithms called **functors**. Each functor performs one operation: the most common spatial analysis algorithms available in a GIS (Geographic Information System), plus algorithms designed especially for spatial simulation, such as transition functions and calibration and validation methods. The [Functor List](../Functor-List.html) describes all of them.

Functors are connected to each other through their **ports**, which carry data of a given type, such as maps, tables, matrices, mathematical expressions and constants. A model is a graph of connected functors, and its execution follows the flow of data from one functor to the next (see [Basic Data Flow](../Basic-Data-Flow.html)). Functors can be enveloped by **containers**, a special type of functor used, for example, to execute iterations or to process data from specific regions of a map.

In the graphical interface, a model is built by dragging functors to the sketch and connecting their ports. Models are saved as scripts, in [EGO Script](../EGO-Script.html) or in [EGOML](../EGOML-Script.html).

Dinamica EGO is designed for performance. Its execution is fully parallel: a fixed number of execution threads, called workers, run independent functors, independent loop steps and pieces of maps at the same time. Large raster maps are processed in parallel even when they are too big to fit in memory. Dinamica EGO can also run R and Python code as part of a model.

## How this Guidebook is organized

The Guidebook is modular. Each module is divided into lessons or examples, in a progressive series of steps:

- **[Module I: Welcome to Dinamica EGO!](Data-Structures-And-File-Formats.html)**: data structures, file formats, the graphical interface and the Map Viewer.
- **[Module II: Working with maps](Opening-And-Saving-Maps.html)**: opening and saving maps, map algebra, map attributes and basic statistics.
- **[Module III: Working with tables](Table-Columns.html)**: creating columns, inserting values, and combining maps and tables.
- **[Module IV: Creating and using Submodels](What-Is-A-Submodel.html)**: what submodels are, and how to create, update, import and publish them.
- **[Module V: Incorporating control structures into a model](Loop-Structures.html)**: loops, regions and successive calculations.
- **[Module VI: Spatial features and spatial analyses](Landscape-Metrics.html)**: landscape metrics, cost surfaces and least-cost pathways, and a complete land-use and land-cover change simulation model.
- **[Module VII: Additional Features](The-Wizard-Editor.html)**: the wizard editor, R and Python coupling, and the script language and console launcher.
- **[Module VIII: Additional applications](Genetic-Algorithm-Calibration.html)**: case studies and tools, from genetic algorithm calibration to agent-based models and ROC analysis.

The complete list of lessons is on the [Guidebook](index.html) start page.

## Where are the data and models?

The data and models used in the lessons are in [guidebook_dinamica.7z](../extra/guidebook_dinamica.7z). It extracts to a `guidebook dinamica` folder with three subfolders:

- `database`: the input maps and tables.
- `models`: the models of each lesson and example.
- `extras`: additional examples and case studies, such as the patterns of change simulations, the Northern Mato Grosso road constructor and the Calculate R Expression examples.

The lessons refer to the files by their path inside `guidebook dinamica`. The archive is in 7z format: Windows 11 opens it directly, and older Windows versions and Linux need a tool such as [7-Zip](https://www.7-zip.org) or `p7zip`.

☞[Next: Lesson 1: Data structures and file formats](Data-Structures-And-File-Formats.html)
{% endraw %}
