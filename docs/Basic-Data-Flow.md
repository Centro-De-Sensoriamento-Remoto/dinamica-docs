---
title: "Basic Data Flow"
nav_order: 1
parent: "Core Concepts"
---
{% raw %}
# Basic Data Flow

## Description

A Dinamica EGO model is, at its core, a graph: **functors** connected through their input and output ports. This is true no matter how the model was authored — built visually in the GUI, saved as [EGOML Script](EGOML-Script.html), or written by hand in [EGO Script](EGO-Script.html). Either notation just describes the same underlying graph, and the execution engine schedules functors from that graph, not from the notation used to write it. This page describes how that scheduling works, independently of any particular notation.

## Functors and connections

A **functor** is a processing unit with a fixed set of typed input and output [ports](EGO-Script.html#ports). A **connection** links one functor's output port to another's input port, carrying a value from the first to the second.

In [EGO Script](EGO-Script.html), a connection is expressed by giving an output a variable name and reusing that same name as an input elsewhere — see [Functors, variables, and binding](EGO-Script.html#functors-variables-and-binding). In the GUI, the same connection is drawn as a wire between two functor boxes. Either way, what the engine sees is a connection between two ports; the variable name or the wire is only how that connection happens to be written down.

A connection doesn't require its two ports to share exactly the same type. When the types are compatible, the value is converted automatically as part of crossing the connection — a Real value connected to a port expecting a Tuple becomes a one-element Tuple, for instance. This conversion is a property of the connection itself, not of the value: the same value, written directly into that port as a literal constant instead of connected to it, is not converted at all — a constant is parsed by its target port's own type-specific parser, which recognizes only that one type's literal syntax and rejects every other form, however closely related the types might otherwise be. See [Constants](EGO-Script.html#constants) for how this distinction is expressed in EGO Script specifically, and [Type System](Type-System.html) for the complete catalog of types and their conversions.

## Data dependencies drive execution order

A functor cannot run until every input port it requires has received a value from the functor that produces it. This creates a **dependency**: whenever functor A's output feeds functor B's input — directly, or through a chain of intermediate connections — B depends on A and cannot start before A finishes.

Two functors that share no such chain have no ordering relationship at all. They may run in any order, or at the same time; nothing about where they sit in a script, or where they're placed on a canvas, has any bearing on this. Execution order is entirely a property of the connection graph, not of the notation used to describe it.

## Containers: the second ordering source

**Container functors** group a nested set of functors so that they execute as a single unit — the container starts, its contents run, then it finishes. This has a consequence beyond simple grouping: a dependency on anything produced *inside* a container is really a dependency on the *whole container*. If functor B consumes a value from something inside container A, B will not start until every functor inside A has finished — not just the specific one that produced the value. See [Container functors](EGO-Script.html#container-functors) for how this is expressed in EGO Script.

This makes containers useful even when nothing inside them shares data with anything outside: wrapping two otherwise-independent functors in a container guarantees they run together, in the order the container defines — an ordering that a plain data dependency could never enforce on its own.

## Containers control whether and how their content runs

Grouping and ordering are only part of what a container does. A container has full control over whether its contents run at all, and how many times. [Group](functors/Group.html) runs its contents exactly once, unconditionally — it exists purely for organization and ordering. [If Then](functors/If-Then.html) and [If Not Then](functors/If-Not-Then.html) run their contents only when a condition holds. Loop containers — [Repeat](functors/Repeat.html), [For](functors/For.html), [For Each](functors/For-Each.html), [For Each Category](functors/For-Each-Category.html), [For Each Region](functors/For-Each-Region.html), [While](functors/While.html), [Do While](functors/Do-While.html), and others — run their contents repeatedly, each according to its own rule: a fixed count, a numeric range, the rows of a table, the categories of a map, or a condition re-evaluated before every pass. From inside the block, a functor has no say in any of this — it simply runs, or doesn't, or runs again, whenever the container decides to.

A container that branches or repeats generally needs to exchange a small amount of state with its contents beyond ordinary connections — a loop's current element going in, or its repeat condition coming back out. This happens through dedicated **internal ports**, a separate channel between the container and the functors nested inside it. See [Internal output ports](EGO-Script.html#internal-output-ports) and [Internal input ports](EGO-Script.html#internal-input-ports) for how this is expressed in EGO Script.

## Ordering without data: sequence connections

Sometimes two functors, or two containers, need to run in a specific order even though neither produces a value the other needs. For this, some functors expose sequencing-only ports that carry no data of their own — a connection between them exists purely to force an order. This is the same graph mechanism as an ordinary connection; it simply carries nothing, which is possible because almost every type in the system converts automatically to the type these ports share — see [Type System](Type-System.html#sequencing) for that conversion listed against every type it applies to. See [Sequence ports](EGO-Script.html#sequence-ports) for the EGO Script syntax.

## The one exception: feedback in loops

A loop's running state is usually carried by a **mux** — a functor with two inputs, an initial value and a feedback value, and one output. The feedback input is deliberately exempt from the rule above: the mux does not wait for the functor that produces the feedback value to run first. Instead, it emits whatever that functor produced on the *previous* iteration. See [Carrying and selecting values across iterations](EGO-Script.html#carrying-and-selecting-values-across-iterations) for a worked example.

This exemption is what makes loops possible at all. Without it, the functor that computes a loop's next state and the mux that carries it forward would depend on each other in a cycle, and neither could ever be scheduled. By treating the feedback connection as "last iteration's value" rather than "this iteration's value," the engine breaks the cycle — the same trick a register or flip-flop uses in a clocked circuit to let a signal feed back into its own computation.

The converse also holds. A loop's iterations can run simultaneously as long as three conditions are met: no mux is used directly inside the loop, nothing produced inside the loop is consumed by anything outside it, and no member of the loop is used as a submodel's output port. Without a mux, an iteration carries no state forward to the next one — so, exactly as with any other pair of functors, iterations that share no connection have no dependency on each other, and the engine is free to run several of them at once.

This also means a mux can be used deliberately to force sequential execution, even when a loop would otherwise qualify for parallel execution — any mux inside the loop disqualifies it, since it's the presence of a mux itself, not what it carries, that creates the dependency between iterations. `MuxValue 0 0` is simply the simplest way to add one: a mux whose initial and feedback inputs are both just the constant `0`, carrying no real state, added purely to force the ordering.

## Destructive updates

Execution order also affects performance, separately from correctness. When a value needs to be destructively updated — modified in place, rather than copied — the engine schedules that update to run after every functor that only reads the value, whenever the dependency graph allows it; by the time the update runs, nothing that still needs the old version is left waiting on it, so no copy is needed. This isn't always possible: if two or more functors need to destructively update the same value, no ordering avoids a copy for all of them — only one destructive update can be the last one to run, so at least one of the others has to work from a copy instead. This matters most for large structured values like tables and maps, where copying is expensive — a scalar's copy cost is negligible either way.

This has a particular consequence for mux-fed loops. A value that a functor inside the loop destructively updates on every iteration, and that something outside the loop also reads, can never benefit from the read-before-update scheduling above. The outside reference, per the container rule, can only run once the entire loop has finished — so it can never be scheduled ahead of any single iteration's update, on any pass. Since every iteration executes the same loop body, the engine cannot tell in advance which pass is the last one that outside reference actually needs; it copies the value on every iteration instead, just to keep it safe for that pending read. Feeding the outside reference from the value produced *after* each iteration's update, rather than the mux's own output, avoids creating this conflict at all: nothing destructively updates that value again once it's produced, so there is nothing for the outside reference to wait behind.
{% endraw %}
