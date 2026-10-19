---
title: "Lesson 15: Using \"Repeat\" to make successive calculations"
parent: "Guidebook"
nav_order: 17
---
{% raw %}
# Lesson 15: Using "Repeat" to make successive calculations

In Lesson 9 we calculated the biomass of the protected areas (PA) for a single year. Here we will calculate the biomass per PA, for each year of designation and category, i.e. strictly protected and sustainable use conservation units and indigenous reserves.

For this, we will use:

- The protected areas map in the year 2000 (`guidebook dinamica\database\protected areas\protected areas 2000.tif`)
- The Legal Amazon Biomass map (`guidebook dinamica\database\biomass\biomass.tif`)

**This exercise is very similar to the Lesson 9 model. But now [Calculate Map](../functors/Calculate-Map.html) produces a map containing the remaining forest for each category and every year.**

Grab the container [Repeat](../functors/Repeat.html) from the Control tab and place it on the sketch. Drag the Lesson 9 model into it. It will automatically resize to envelop Calculate Map. We extract the attributes and statistics by category using an [Extract Categorical Map Attributes](../functors/Extract-Categorical-Map-Attributes.html). This functor calculates basic statistics from a map for each area delimited by a class. Also grab the functors Get table from key and Lookup table and place it within the Repeat.

![](../image/guidebook_15a.png)

The functor [Lookup Table](../functors/Lookup-Table.html) is a structure used as a link to other functors, transforming a table into a lookup table if the table has only two columns, one for numeric keys and another for values.

The functor [Get Table From Key](../functors/Get-Table-From-Key.html) retrieves the sub-table corresponding to the given chain of keys (In this case: “12”) from a given input table.

![](../image/guidebook_15b.png)

Click on the [Mux Table](../functors/Mux-Table.html) with the Edit Functor Ports. Every Mux functor has two input ports. In the first iteration, the model reads the input from the Initial port; thereafter from the port Feedback.

> **Tip:** Note that in addition to the Year and CO2 content columns we have the category of Protected Areas.

![](../image/guidebook_15c.png)

Mark the eye button at the top of “[Save Table](../functors/Save-Table.html)” to view the results after model run.

Click on the layout tool Left to Right and your final model will look like the one below:

![](../image/guidebook_15d.png)

**Save and run the model!**

Now, click on eye button of “[Save Lookup Table](../functors/Save-Lookup-Table.html)” to see the result. This functor output is a table that looks like this:

![](../image/guidebook_15e.png)

The result is returned in a table that contains the extracted classes and their corresponding attributes per year and category.

## Congratulations, you have successfully completed this lesson!

☞[Next: Lesson 16: Calculating landscape metrics](Landscape-Metrics.html)
{% endraw %}
