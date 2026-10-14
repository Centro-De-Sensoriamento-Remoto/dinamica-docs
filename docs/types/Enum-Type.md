---
title: "Enum Type"
nav_order: 4
parent: "Type System"
grand_parent: "Core Concepts"
redirect_from:
  - /Enum-Type.html
---
{% raw %}
# Enum Type

An Enum value selects one option from a fixed, named set of choices. Unlike [Cell Type](Cell-Type.html) or [Log Tag Type](Log-Tag-Type.html), which each have exactly one set of options shared by every port of that type, Enum Type is backed by a registry of separately named **enum definitions** — such as `ComputingTargetEnum` or `EnvironmentKeyEnum` — each one a list of dot-constant/label pairs. A given port declares which named definition it uses, so two different Enum Type ports can accept entirely different sets of options depending on which definition they reference.

Some examples, spanning several unrelated functors:

- [Transform Map](../functors/Transform-Map.html)'s `resamplingMethod` offers fourteen resampling algorithms: `.nearest` (0, "Nearest"), `.bilinear` (1, "Bilinear"), `.cubic` (2, "Cubic"), `.spline` (3, "Cubic Spline"), `.lanzo` (4, "Lanzos"), `.average` (5, "Average"), `.mode` (6, "Mode"), `.maximum` (7, "Maximum"), `.minimum` (8, "Minimum"), `.median` (9, "Median"), `.1quartile` (10, "1st Quartile"), `.3quartile` (11, "3rd Quartile"), `.rms` (12, "Root Mean Square"), and `.sum` (13, "Weighted Sum").
- [Load Map](../functors/Load-Map.html)'s `storageMode` offers `.default` (0, "Default"), `.preferMemory` (1, "Prefer Memory"), `.preferDisk` (2, "Prefer Disk"), and `.loadAsSparse` (3, "Load As Sparse") — this is the same `storageMode` mechanism described on the [Map Type](Map-Type.html) page's Storage section, confirmed here to be an ordinary Enum Type port rather than a separate mechanism of its own.
- [Get Environment Value](../functors/Get-Environment-Value.html)'s `key` uses the `EnvironmentKeyEnum` definition, offering ten options identifying which environment path or fact to retrieve — `.temp`, `.modelDir`, `.modelTempFolder`, `.userFolder`, `.userSubmodelFolder`, `.storeSubmodelFolder`, `.appFolder`, `.appVersion`, `.baseOS`, and `.osExeExtension`. Unlike the examples above, this port is required and has no default — every call must choose one explicitly.
- [Execution Policy](../functors/Execution-Policy.html)'s `computingTarget` uses the `ComputingTargetEnum` definition: `.default` (0, "Default"), `.processorsOnly` (1, "Processors Only"), and `.acceleratorDevicesOnly` (2, "Accelerator Devices Only").

Like any other type, an Enum Type port can also be nullable: [Run Remotely](../functors/Run-Remotely.html)'s `networkErrorBehavior` offers `.abortExecution` (0) and `.runLocally` (1), but defaults to `.none` rather than to either option, falling back to the application's own setting when left unspecified.

## GUI Editor

The enum editor presents a dropdown listing the port's own named enum definition. This is the same dropdown experience [light enum](../EGO-Script.html#light-enum) recreates for the integer-family value types — light enum exists precisely for ports that need this presentation without actually being Enum Type underneath.

## EGO Script

An Enum constant uses the same dot-constant syntax as any other type — see [Constants](../EGO-Script.html#constants) — but which dot-constants a given port accepts depends entirely on the named enum definition that port references, not on any single, universal list:

```
elevation := LoadMap {
    filename = "c:/data/elevation.tif",
    storageMode = .preferMemory
};
```

## Automatic Conversions

- **Converted from**: [Integer Value Type](Integer-Value-Type.html), [Non Negative Integer Value Type](Non-Negative-Integer-Value-Type.html), [Positive Integer Value Type](Positive-Integer-Value-Type.html), and [Real Value Type](Real-Value-Type.html) — the number selects the option whose index matches it.
- **Converted to**: None.

See [Type System](../Type-System.html) for the complete conversion reference across all types.
{% endraw %}
