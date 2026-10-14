---
title: "Workdir Type"
nav_exclude: true
---
{% raw %}
# Workdir Type

A Workdir value represents the active working directory that relative filenames are resolved against. It's produced only by the [Workdir](Workdir.html) container functor, from the [Folder](Folder-Type.html) path given to its own `folder` input, and exposed as that container's `workdir` internal output. Functors placed inside a Workdir — [Load Map](Load-Map.html), [Load Categorical Map](Load-Categorical-Map.html), [Load Table](Load-Table.html), [Load Lookup Table](Load-Lookup-Table.html), [Load Weights](Load-Weights.html), [Save Map](Save-Map.html), Save Categorical Map, [Save Table](Save-Table.html), [Save Lookup Table](Save-Lookup-Table.html), and [Save Weights](Save-Weights.html) — each have their own `workdir` input auto-bound to it, so the filename they're given is resolved relative to that folder instead of the model script's own location.

## GUI Editor

Workdir Type has no editor. It can only be produced by an enclosing [Workdir](Workdir.html) container and consumed by auto-binding into a functor's own `workdir` input — never typed in directly.

## EGO Script

For the same reason, Workdir Type has no literal constant syntax in [EGO Script](EGO-Script.html) — see [Constants](EGO-Script.html#constants). The [Workdir](Workdir.html) container itself has no output, so it appears as a bare statement rather than an assignment. A functor placed inside it has its filename resolved relative to the folder given to the container, without needing to reference the workdir explicitly:

```
Workdir "c:/data/landscape.zip" {{
    // "landscape.tif" is resolved relative to "c:/data/landscape.zip".
    landscape := LoadCategoricalMap { filename = "landscape.tif" };
}};
```

## Automatic Conversions

None — Workdir Type converts to or from no other type.

See [Type System](Type-System.html) for the complete conversion reference across all types.
{% endraw %}
