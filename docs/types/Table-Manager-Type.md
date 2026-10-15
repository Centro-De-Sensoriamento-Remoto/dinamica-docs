---
title: "Table Manager Type"
nav_order: 51
parent: "Type System"
grand_parent: "Core Concepts"
---
{% raw %}
# Table Manager Type

A **Table Manager** represents a container-scoped registry for assembling one [Table](Table-Type.html) out of independently produced fragments -- the same "manager" pattern [Region Manager Type](Region-Manager-Type.html) uses for maps, applied to tables instead. The [Table Manager](../functors/Table-Manager.html) container itself has no inputs or outputs of its own; it opens a management context and exposes an internal output port `tableManager` to whatever runs inside its block, the same way [Region Manager](../functors/Region-Manager.html) exposes `regionManager` or [Workdir](../functors/Workdir.html) exposes `workdir`.

Within that block, [Sub Table](../functors/Sub-Table.html) registers one fragment at a time: a `tableName`, a `keys` Tuple identifying where the fragment belongs, and the fragment's row data as `subTable`. Sub Table's own output is just a pass-through of that same `subTable`; the actual effect -- recording the fragment under the enclosing Table Manager -- happens as a side effect. [Merge Sub Tables](../functors/Merge-Sub-Tables.html), called from within the same block, then collects every fragment registered under a given `tableName` and inserts them, by their respective keys, into a supplied `baseTable`.

Because [Sub Table](../functors/Sub-Table.html) auto-binds only to the enclosing Table Manager's fixed `tableManager` output -- never to a mux's per-iteration feedback -- a loop whose body calls nothing but [Sub Table](../functors/Sub-Table.html) carries no state from one iteration to the next, so its iterations qualify to run in parallel under the rule described in [The one exception: feedback in loops](../Basic-Data-Flow.html#the-one-exception-feedback-in-loops). This is the type's purpose: it lets a table be assembled from parts produced independently, in contrast to [Mux Table](../functors/Mux-Table.html), which threads a single table through loop feedback and so forces its iterations to run in sequence.

[Table Manager Value](../functors/Table-Manager-Value.html) plays the same supporting role [Region Manager Value](../functors/Region-Manager-Value.html) plays for regions: it re-exposes the manager reference for a functor that needs it explicitly, somewhere auto-binding does not reach on its own.

## GUI Editor

Input [ports](../EGO-Script.html#ports) of type Table Manager are non-editable, so a Table Manager value cannot be defined using an editor in the graphical interface. A Table Manager value must always come from the internal output of an enclosing [Table Manager](../functors/Table-Manager.html) container -- there is no functor that produces one directly outside that context.

## EGO Script

For the same reason, input [ports](../EGO-Script.html#ports) of type Table Manager cannot receive a constant in [EGO Script](../EGO-Script.html) -- see [Constants](../EGO-Script.html#constants). A Table Manager is read with the `variable = tableManager;` internal-output form at the top of a [Table Manager](../functors/Table-Manager.html) block -- see [Internal output ports](../EGO-Script.html#internal-output-ports) -- or received automatically wherever [Sub Table](../functors/Sub-Table.html), [Merge Sub Tables](../functors/Merge-Sub-Tables.html), or [Table Manager Value](../functors/Table-Manager-Value.html) auto-bind to the enclosing container. [Table Manager](../functors/Table-Manager.html) itself has no outputs, so it is called as a bare statement, with no assignment and no underscore:

```
// regionOneAreas and regionTwoAreas are Tables produced independently -- for
// example, by two loop iterations that never depend on each other's output --
// so the loop producing them is free to run its iterations in parallel.
// areaShell is a Table already shaped with the RegionId*/Area columns.
TableManager {{
    _ := SubTable "areas" [1] regionOneAreas;
    _ := SubTable "areas" [2] regionTwoAreas;

    mergedAreas := MergeSubTables areaShell "areas";
}};

// mergedAreas is defined inside the block above but used here, after it.
SaveTable mergedAreas "c:/data/areas.csv";
```

The generic [Table Manager Value](../functors/Table-Manager-Value.html) carrier functor exists to pass a Table Manager reference along explicitly -- for example, into a submodel input or a container where auto-binding does not reach. Inside a Table Manager block its own input auto-binds to that container's `tableManager`; used anywhere else, it needs an explicit connection to a Table Manager value, since its input has no real default of its own.

## Automatic Conversions

Table Manager Type has no registered conversions to or from any other type. The only conversion registered for it at all is the sequencing conversion to [None Type](None-Type.html) -- used to force execution order via `sequenceInput`/`sequenceOutput` ports, not to transform a value. This is the same as [Region Manager Type](Region-Manager-Type.html), its counterpart for maps.

See [Type System](../Type-System.html).
{% endraw %}
