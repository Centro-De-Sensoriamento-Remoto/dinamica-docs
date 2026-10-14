---
title: "Modeling Guides"
nav_order: 6
has_children: true
---
{% raw %}
# Modeling Guides

Guides to modeling tasks that go beyond a single functor.

- [Manipulating Tables and Lookup Tables](Manipulating-Tables-And-Lookup-Tables.html) — functors and techniques for reading, iterating, restructuring, and computing statistics from tables and lookup tables, from a table with a known shape through to tables with an arbitrary number of columns or keys.
- [Working with Subregions Using Region Manager](Working-With-Subregions.html) — when and why to split a model's computation by region; defining regions from a categorical map with Region Manager; reading region metadata; visiting one region or looping over all of them; splitting a global map into regional pieces and merging them back; and the two supporting patterns — per-region functor parameters and per-region accumulation — a region-based model typically needs.
- [Weights of Evidence Calibration](Weights-Of-Evidence-Calibration.html) — calibrating Weights of Evidence from a pair of landscape maps and a set of predictive variables through to a finished set of ranges and coefficients: what Weights of Evidence is and how to read a weight's sign, preparing categorical and continuous variables, the Skeleton and its parameters, determining ranges and why the underlying algorithm works, determining coefficients and reading the report, checking variable independence, saving and reusing the results, using the calibrated weights downstream, and a basic worked example.
- [Useful Tips for Creating Models](Model-Tips.html) — practical tips that don't fit neatly under a single functor or language feature.
{% endraw %}
