---
title: "Core Concepts"
nav_order: 3
has_children: true
---
{% raw %}
# Core Concepts

The ideas the rest of the documentation builds on.

- [Basic Data Flow](Basic-Data-Flow.html) — the execution model underneath both notations: how connections and containers determine execution order, independent of whether the model was written as EGO Script, EGOML, or built visually.
- [Image Virtualization](Image-Virtualization.html) — how Dinamica reconciles maps of different extents, resolutions, or rotations at runtime: every map handed to a functor is wrapped in a virtual version at a shared resolution and extent first, so functors never see mismatched inputs; requirements (shared projection), the Not Allowed / Limited / Unrestricted control under "Tools => Options \| Advanced \| Virtualization", and the functors that opt out of it entirely.
- [Type System](Type-System.html) — the registry tying every type in the engine together: which conversions run automatically when a value is connected from one port to another, which relationships are subtyping instead, and which conversions can fail or lose information.
- [Parallel Execution](Parallel-Execution.html) — how Dinamica EGO runs independent functors, loop steps and parts of each job at the same time on several workers and accelerator devices, and the options that control the number of workers, the granularity and the use of accelerators.
{% endraw %}
