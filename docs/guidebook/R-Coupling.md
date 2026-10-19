---
title: "R Coupling"
parent: "Guidebook"
nav_order: 22
---
{% raw %}
# Dinamica EGO and R Coupling

## What will you learn?

- Couple R to Dinamica EGO
- [Calculate R Expression](../functors/Calculate-R-Expression.html)
- Select the R Interpreter to Use

Dinamica EGO can run R scripts as part of a model, and exchange data with an R session running alongside the model. Follow these steps:

1. **Set up R.** On Windows, install the Dinamica EGO Enhancement Plugin, or use a local R installation; on Linux, install R and configure Dinamica EGO to use it. See [Setup](../functors/Calculate-R-Expression.html#setup) on Calculate R Expression.
1. **Run an R script in a model.** [Calculate R Expression](../functors/Calculate-R-Expression.html) receives data through hooks (`t1`, `v1`, `s1`, …) and returns its results in a Struct, read with the Extract Struct functors. Its page has worked examples, and the [Guidebook dataset](../extra/guidebook_dinamica.7z) has example models in `guidebook dinamica\extras\examples\various applications\calculate r expression`.
1. **Select the R interpreter.** Choose between the plugin's interpreter and a local R installation in *Tools → Options | Integration*.
1. **Exchange data with a running R session.** For models where R and Dinamica EGO run side by side, see [Coupling with R](../Coupling-With-R.html), which also describes the legacy ways of calling one tool from the other.

Congratulations, you have successfully completed this lesson!

☞[Next: Python Coupling](Python-Coupling.html)
{% endraw %}
