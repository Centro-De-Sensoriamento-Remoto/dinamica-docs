---
title: "Functors and Ports"
nav_order: 2
parent: "Core Concepts"
---
{% raw %}
# Functors and Ports

## Description

Every Dinamica EGO model is built from **functors** connected through their **ports**. A functor is a processing unit: it receives values through its input ports, performs a single operation on them, and delivers its results through its output ports. The set of ports is fixed by the functor itself and listed on its own page in the [Functor List](Functor-List.html). Most functors produce at least one output, but some act only through a side effect — [Save Map](functors/Save-Map.html) and [Save Table](functors/Save-Table.html) write files and produce nothing a connection could carry.

This page describes functors and ports independently of how a model is written. [Basic Data Flow](Basic-Data-Flow.html) explains how the engine decides when each functor runs, and [EGO Script](EGO-Script.html) shows how all of this is expressed in text.

## Ports

A **port** is a typed connection point. A connection links an output port of one functor to an input port of another, and the value produced by the first becomes the input of the second. The port's **type** determines what it can receive: an input port accepts a value of its exact type, or of any type that converts to it automatically across the connection. That conversion belongs to the connection, not to the value — a constant written directly into a port is parsed by the port's own type and never converted. See [Basic Data Flow](Basic-Data-Flow.html#functors-and-connections) for this distinction and [Type System](Type-System.html) for every type and conversion.

An input port is either **required** or **optional**. A required port must always receive something, either a connection or a constant, and a model whose required inputs are not all supplied cannot run. An optional port has a **default value**, specific to that port and shown on the functor's page, which is used whenever the port is left unset. A functor always lists its optional ports after its required ones, which is what allows a textual call to simply stop supplying inputs once it reaches the optional ones it doesn't need.

Some optional ports are also **nullable**, meaning that the absence of a value is itself a meaningful input. When such a port's default is already "no value", leaving it unset and explicitly supplying "no value" have the same effect; the explicit form only makes clear that the absence was chosen deliberately rather than overlooked.

Finally, a port is either **editable** or not. An editable port can take a constant, typed into the graphical interface or written into a script. A non-editable port can only be fed by a connection from another functor.

## Containers

A **container** is a functor that holds other functors and runs them as part of its own execution: the container starts, its contents run, and then it finishes. [Basic Data Flow](Basic-Data-Flow.html#containers-the-second-ordering-source) explains how this affects execution order. What a container does with its contents varies, and most containers fall into one of a few families.

[Group](functors/Group.html) is the simplest: it runs its contents exactly once, and exists to organize a model and give a block shared properties such as a label or color. [If Then](functors/If-Then.html) and [If Not Then](functors/If-Not-Then.html) run their contents only when a condition is true or false, respectively. The loop containers run their contents repeatedly, each with its own rule: [Repeat](functors/Repeat.html) a fixed number of times, [For](functors/For.html) over a numeric range, [For Each](functors/For-Each.html) over the rows of a table, [For Each Category](functors/For-Each-Category.html) over the categories of a map, [For Each Region](functors/For-Each-Region.html) over its regions, and [While](functors/While.html) and [Do While](functors/Do-While.html) for as long as a condition holds. Context containers — [Region Manager](functors/Region-Manager.html), [Region](functors/Region.html), [Table Manager](functors/Table-Manager.html) and [Workdir](functors/Workdir.html) — establish a region, a table manager or a working directory and run their contents once, with that context available to every functor inside them. [Skip On Error](functors/Skip-On-Error.html) and [Skip All On Error](functors/Skip-All-On-Error.html) run their contents while capturing any error raised inside them, as described in [Error-handling containers](#error-handling-containers) below. Even the [calculator functors](Calculate-Functors.html) are containers, holding the expression they evaluate and, in the verbose form, the hook functors that supply its operands.

Not every container is about control flow, though. Some functors are containers only so that a side effect is guaranteed to happen around a computation. [Print](functors/Print.html) is the clearest example: it prints its `initialMessage` before its contents run and its `finalMessage` after they complete. Without the container, nothing would tie the messages to the computation — there is no data dependency between them, so the engine would be free to print either message at any point.

### Internal ports

A container that loops or provides a context needs to share a small amount of state with its contents: the current element of a loop, the region manager of a region context, or the condition that tells a `While` loop whether to continue. This exchange goes through **internal ports**, a channel between the container and its contents that is separate from the container's ordinary inputs and outputs. An **internal output port** carries a value from the container into its contents, and an **internal input port** carries a value from the contents back to the container. See [Internal output ports](EGO-Script.html#internal-output-ports) and [Internal input ports](EGO-Script.html#internal-input-ports) for how they are read and fed in EGO Script.

The internal output ports of each container are:

| Container | Internal output port | Type | Description |
| --- | --- | --- | --- |
| [Do While](functors/Do-While.html) | `step` | NonNegativeIntegerValue | Current iteration index, starting at 1. |
| [For](functors/For.html) | `step` | RealValue | Current value in the numeric range being iterated. |
| [For Each](functors/For-Each.html) | `step` | RealValue | Current row value from the table being iterated. |
| [For Each Category](functors/For-Each-Category.html) | `step` | IntegerValue | Current category code from the categorical map. |
| [For Each Region](functors/For-Each-Region.html) | `step` | IntegerValue | Current region identifier. |
| [For Each Region](functors/For-Each-Region.html) | `regionManager` | RegionManager | The region manager for the current region. |
| [Repeat](functors/Repeat.html) | `step` | NonNegativeIntegerValue | Current iteration index, starting at 1. |
| [While](functors/While.html) | `step` | NonNegativeIntegerValue | Current iteration index, starting at 1. |
| [Region Manager](functors/Region-Manager.html) | `regionManager` | RegionManager | The region manager for the current region context. |
| [Region](functors/Region.html) | `regionManager` | RegionManager | The region manager. |
| [Region](functors/Region.html) | `regionId` | IntegerValue | The current region identifier. |
| [Workdir](functors/Workdir.html) | `workdir` | Workdir | The working directory defined by the container. |
| [Table Manager](functors/Table-Manager.html) | `tableManager` | TableManager | The table manager defined by the container. |
| [Genetic Algorithm Tool](functors/Genetic-Algorithm-Tool.html) | `currentIndividual` | LookupTableGroup | The current individual in the genetic algorithm population. |

And the internal input ports:

| Container | Internal input port | Type | Set by |
| --- | --- | --- | --- |
| [While](functors/While.html) | `condition` | BooleanValue | [Set While Condition](functors/Set-While-Condition.html) |
| [Do While](functors/Do-While.html) | `condition` | BooleanValue | [Set While Condition](functors/Set-While-Condition.html) |
| [Genetic Algorithm Tool](functors/Genetic-Algorithm-Tool.html) | `fitness` | RealValue | [Set Fitness](functors/Set-Fitness.html) |

### Auto-bound ports

Most of the time, an internal port doesn't need to be connected by hand. Some functors have ports that are **auto-bound**: when the functor is placed inside a compatible container, the port connects by itself to the container's matching internal port. [Step](functors/Step.html), for instance, automatically reads the `step` of the loop that encloses it, and [Set While Condition](functors/Set-While-Condition.html) automatically feeds the `condition` of its enclosing `While` or `Do While`. This is also why a `Load*` functor placed inside a loop or a [Workdir](functors/Workdir.html) picks up the current step and working directory without any explicit connection.

The complete set of auto-bound ports is:

| Port | Direction | Functors | Binds to the internal port of |
| --- | --- | --- | --- |
| `step` | input | [Step](functors/Step.html), all `Load*` and `Save*` functors, all `Select*` functors | [Repeat](functors/Repeat.html), [For](functors/For.html), [For Each](functors/For-Each.html), [For Each Category](functors/For-Each-Category.html), [For Each Region](functors/For-Each-Region.html), [While](functors/While.html), [Do While](functors/Do-While.html) |
| `workdir` | input | all `Load*` and `Save*` functors | [Workdir](functors/Workdir.html) |
| `regionManager` | input | [Get All Regions Info](functors/Get-All-Regions-Info.html), [Get Region Info](functors/Get-Region-Info.html), [Region](functors/Region.html), [Region Manager Value](functors/Region-Manager-Value.html), [Regional Map](functors/Regional-Map.html), [Regional Categorical Map](functors/Regional-Categorical-Map.html), [Regionalize Map](functors/Regionalize-Map.html), [Regionalize Categorical Map](functors/Regionalize-Categorical-Map.html), [Merge Regional Maps](functors/Merge-Regional-Maps.html), [Merge Regional Categorical Maps](functors/Merge-Regional-Categorical-Maps.html) | [Region Manager](functors/Region-Manager.html), [Region](functors/Region.html), [For Each Region](functors/For-Each-Region.html) |
| `regionId` | input | [Get Region Info](functors/Get-Region-Info.html), [Region](functors/Region.html), [Regional Map](functors/Regional-Map.html), [Regional Categorical Map](functors/Regional-Categorical-Map.html), [Regionalize Map](functors/Regionalize-Map.html), [Regionalize Categorical Map](functors/Regionalize-Categorical-Map.html) | [Region](functors/Region.html) |
| `tableManager` | input | [Merge Sub Tables](functors/Merge-Sub-Tables.html), [Sub Table](functors/Sub-Table.html), [Table Manager Value](functors/Table-Manager-Value.html) | [Table Manager](functors/Table-Manager.html) |
| `currentIndividual` | input | [Get Current Individual](functors/Get-Current-Individual.html) | [Genetic Algorithm Tool](functors/Genetic-Algorithm-Tool.html) |
| `condition` | output | [Set While Condition](functors/Set-While-Condition.html) | [While](functors/While.html), [Do While](functors/Do-While.html) |
| `fitness` | output | [Set Fitness](functors/Set-Fitness.html) | [Genetic Algorithm Tool](functors/Genetic-Algorithm-Tool.html) |

### Sequence ports

Sometimes two containers must run in a given order even though neither needs anything the other produces. For this, most containers expose a pair of ordinary ports that carry no data at all: an optional `sequenceInput` and a `sequenceOutput`. Connecting one container's `sequenceOutput`, or any other output, to another container's `sequenceInput` makes the second wait for the first to finish. Any output can be used this way because almost every type converts automatically to the type these ports share — see [Type System](Type-System.html#sequencing). The ordering is only a constraint between the two: other functors may still run in between.

Sequence ports are only needed when no data dependency already exists; if one container consumes a value produced by the other, the order is already settled. A few containers don't expose them — [Workdir](functors/Workdir.html), [Region](functors/Region.html), [Region Manager](functors/Region-Manager.html) and [Table Manager](functors/Table-Manager.html) — and ordering them requires a **forced dependency** instead: a dummy value produced inside one container and consumed inside the other. Older models use the same pattern where a sequence port would now be the natural choice. [Skip On Error](functors/Skip-On-Error.html) and [Skip All On Error](functors/Skip-All-On-Error.html) lack sequence ports too, but their `executionCompletedSuccessfully` output can be connected in the same way. See [Sequence ports](EGO-Script.html#sequence-ports) for the EGO Script syntax.

## Muxes and junctions

Two families of functors manage how a value moves from one iteration, or one dataflow, to another. Both are typed, with one functor per kind of data.

A **mux** carries a value across the iterations of a loop. It has two inputs — an initial value and a feedback value — and on the first iteration it emits the initial value, while on every later iteration it emits the feedback value produced during the previous one. A mux at the start of a loop body, fed back by a value computed at its end, therefore holds the loop's running state. Its feedback input is the one exception to the rule that a functor waits for everything it consumes, as explained in [Basic Data Flow](Basic-Data-Flow.html#the-one-exception-feedback-in-loops). The family includes [Mux Map](functors/Mux-Map.html), [Mux Categorical Map](functors/Mux-Categorical-Map.html), [Mux Table](functors/Mux-Table.html), [Mux Lookup Table](functors/Mux-Lookup-Table.html), [Mux Value](functors/Mux-Value.html) and [Mux Tuple](functors/Mux-Tuple.html), among others.

A **junction** chooses between two dataflows. If its first input carries data, the junction passes it through; if not, it passes the second one instead, and if neither carries data it reports an error. Junctions are mostly used to supply a fallback when a value may be missing, such as when part of a model was skipped by an error-handling container. The family includes [Map Junction](functors/Map-Junction.html), [Categorical Map Junction](functors/Categorical-Map-Junction.html), [Table Junction](functors/Table-Junction.html), [Lookup Table Junction](functors/Lookup-Table-Junction.html), [Value Junction](functors/Value-Junction.html), [String Junction](functors/String-Junction.html) and [Folder Junction](functors/Folder-Junction.html).

See [Carrying and selecting values across iterations](EGO-Script.html#carrying-and-selecting-values-across-iterations) for an example of both in EGO Script.

## Error-handling containers

[Skip On Error](functors/Skip-On-Error.html) and [Skip All On Error](functors/Skip-All-On-Error.html) run their contents and, if any of them raises an error, capture it instead of stopping the model. Both take a `trapAndIgnoreErrors` input — when it is false they behave as a plain [Group](functors/Group.html) and let errors through — and both report the outcome through an `executionCompletedSuccessfully` output that later functors can test.

The two differ in what they do with results already produced when the error happens. [Skip On Error](functors/Skip-On-Error.html) keeps the outputs of every functor that completed before the error, while [Skip All On Error](functors/Skip-All-On-Error.html) discards all of them, so its contents either succeed together or produce nothing. See [Handling Errors](Handling-Errors.html) for how to combine them with junctions and conditional containers.
{% endraw %}
