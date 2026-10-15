---
title: "Python Coupling"
parent: "Module VII: Additional Features"
grand_parent: "Guidebook"
nav_order: 3
---
{% raw %}
# Dinamica EGO and Python Coupling

Dinamica EGO can run arbitrary Python code as part of a model through the [Calculate Python Expression](../functors/Calculate-Python-Expression.html) functor. This lesson walks through a complete example; for the full reference — including the `dinamica.inputs`/`dinamica.outputs` mechanism, all available utilities, and how to retrieve the results back into the model — see [Calculate Python Expression](../functors/Calculate-Python-Expression.html).

## Example

The example below installs `numpy` and uses it to compute area statistics for a table of land cover patches, then returns both summary values and a table of outlier patches — something considerably more convenient with `numpy` than with plain Python loops.

The input, `t1`, is a table of land cover patches with columns `PatchId*` and `Area`. Inside the `CalculatePythonExpression` container, `t1` must be provided by a [Number Table](../functors/Number-Table.html) hook connected to the actual table functor — this is what makes the table available to the expression as `dinamica.inputs["t1"]`. See [Expression inputs](../functors/Calculate-Python-Expression.html#expression-inputs) for the full hook mechanism.

Install `numpy` and load the `Area` column into an array, skipping the header row:

```
dinamica.package("numpy")

areas = numpy.array([row[1] for row in dinamica.inputs["t1"][1:]])
```

Compute the mean and standard deviation of patch area:

```
meanArea = float(numpy.mean(areas))
stdArea = float(numpy.std(areas))
```

Flag patches whose area lies more than two standard deviations from the mean, using `numpy`'s vectorized comparison instead of a manual loop:

```
isOutlier = numpy.abs(areas - meanArea) > 2 * stdArea
```

Return the two summary statistics as scalar outputs:

```
dinamica.outputs["meanArea"] = meanArea
dinamica.outputs["stdArea"] = stdArea
```

Build and return a table containing only the outlier patches:

```
header = dinamica.inputs["t1"][0]
outlierRows = [row for row, flagged in zip(dinamica.inputs["t1"][1:], isOutlier) if flagged]
outlierTable = [header] + outlierRows

dinamica.outputs["outlierPatches"] = dinamica.prepareTable(outlierTable, 1)
```

The complete expression:

```
dinamica.package("numpy")

areas = numpy.array([row[1] for row in dinamica.inputs["t1"][1:]])

meanArea = float(numpy.mean(areas))
stdArea = float(numpy.std(areas))

isOutlier = numpy.abs(areas - meanArea) > 2 * stdArea

dinamica.outputs["meanArea"] = meanArea
dinamica.outputs["stdArea"] = stdArea

header = dinamica.inputs["t1"][0]
outlierRows = [row for row, flagged in zip(dinamica.inputs["t1"][1:], isOutlier) if flagged]
outlierTable = [header] + outlierRows

dinamica.outputs["outlierPatches"] = dinamica.prepareTable(outlierTable, 1)
```

Back in the model, `meanArea`, `stdArea`, and `outlierPatches` are retrieved from the returned `Struct` using the `ExtractStruct*` family of functors — see [Retrieving outputs](../functors/Calculate-Python-Expression.html#retrieving-outputs) for details.

## Reference

The full set of Python utilities available inside the expression — `dinamica.package()`, `dinamica.prepareTable()`, `dinamica.prepareLookupTable()`, and `dinamica.toTable()` — along with their parameters and additional examples of installing packages with specific versions or from custom sources, is documented on the [Calculate Python Expression](../functors/Calculate-Python-Expression.html#utilities) page.

---

### Congratulations, you have successfully completed this lesson!

☞[Next Lesson](Script-Language-And-Console-Launcher.html)
{% endraw %}
