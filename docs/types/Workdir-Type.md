---
title: "Workdir Type"
nav_order: 52
parent: "Type System"
grand_parent: "Core Concepts"
---
{% raw %}
# Workdir Type

A Workdir value represents the active working directory that relative filenames are resolved against. It's produced only by the [Workdir](../functors/Workdir.html) container functor, from the [Folder](Folder-Type.html) path given to its own `folder` input, and exposed as that container's `workdir` internal output. Functors placed inside a Workdir — [Load Map](../functors/Load-Map.html), [Load Categorical Map](../functors/Load-Categorical-Map.html), [Load Table](../functors/Load-Table.html), [Load Lookup Table](../functors/Load-Lookup-Table.html), [Load Weights](../functors/Load-Weights.html), [Save Map](../functors/Save-Map.html), Save Categorical Map, [Save Table](../functors/Save-Table.html), [Save Lookup Table](../functors/Save-Lookup-Table.html), and [Save Weights](../functors/Save-Weights.html) — each have their own `workdir` input auto-bound to it, so the filename they're given is resolved relative to that folder instead of the model script's own location.

## GUI Editor

Workdir Type has no editor. It can only be produced by an enclosing [Workdir](../functors/Workdir.html) container and consumed by auto-binding into a functor's own `workdir` input — never typed in directly.

## EGO Script

For the same reason, Workdir Type has no literal constant syntax in [EGO Script](../EGO-Script.html) — see [Constants](../EGO-Script.html#constants). The [Workdir](../functors/Workdir.html) container itself has no output, so it appears as a bare statement rather than an assignment. A functor placed inside it has its filename resolved relative to the folder given to the container, without needing to reference the workdir explicitly:

```
Workdir "c:/data/landscape.zip" {{
    // "landscape.tif" is resolved relative to "c:/data/landscape.zip".
    landscape := LoadCategoricalMap { filename = "landscape.tif" };
}};
```

## Automatic Conversions

None — Workdir Type converts to or from no other type.

See [Type System](../Type-System.html) for the complete conversion reference across all types.
{% endraw %}
