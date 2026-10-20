---
title: "Lesson 12: Updating, importing and publishing a local submodel"
parent: "Guidebook"
nav_order: 14
---
{% raw %}
# Lesson 12: Updating, importing and publishing a local submodel on Dinamica EGO

### What will you learn?

- How to update a submodel
- How to import an submodel
- How to publish an submodel

### Updating Local Submodels

At any time, the user can add or remove inputs and outputs or even change the combination of functors defining the submodel.
The [functor action bar](../gui/Interface-Elements.html#functor-action-bar) of all functors within a submodel script exhibits additional options for **exporting functor inputs and outputs**. Exporting a new input or output can be performed following the steps below:

- Click on the functor which inputs or outputs will be exported.

- Select the **export functor inputs and outputs** on the [functor action bar](../gui/Interface-Elements.html#functor-action-bar) and choose the input or outputs that will be exported. It is possible to define the input and output names and their corresponding descriptions. It is also possible to mark an exported input as advanced or optional. Optional inputs can also define an optional value that will be assigned to the port if no explicit value is provided.

- Choose the **Submodel Options** submenu on the model toolbar and then click on **Apply Changes / Edit Submodel Properties**. That brings the submodel editor dialog where you can define a new name, description and icon for the submodel or reorder its inputs and outputs (or even remove some of them). Clicking **Ok** propagates the changes to all parts of your model (and dependent submodels) where the submodel is used.

Below you can see two examples of updating the inputs and output ports of a local submodel.

#### Example 1

<div class="video">
  <iframe src="https://www.youtube-nocookie.com/embed/i6T9GGqfU80?mute=1" title="Updating local submodels ports" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
</div>

#### Example 2

<div class="video">
  <iframe src="https://www.youtube-nocookie.com/embed/FK5xIYCS0KI?mute=1" title="Updating local submodels ports (additional approach)" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
</div>

- Beware that connected inputs cannot be exported. They must be disconnected first. It is also worth noting that it is possible to safely rename inputs and outputs. The connections to the port will be maintained when the changes are propagated.

> **Tip:** Dinamica EGO comes with a set of icons from the [Fat Cow Icon Set](https://web.archive.org/web/20131231225029/http://www.fatcow.com/free-icons) that can be used to customize the local submodels created by users. The icons come in size 16x16 and 32x32 pixels. The overall color of the icon chosen is automatically used to define the color of the functor representing the submodel on the graphical interface.
> The set of icons are usually installed in the folder `IconSamples` in your Dinamica EGO installation folder

- When updating a local submodel, the changes from all dependent local submodels will also be propagated. It means that updating a submodel always updates the whole chain of local submodels that uses that submodel as part of their definition.

<div class="video">
  <iframe src="https://www.youtube-nocookie.com/embed/wDtyrRbUNo4?mute=1" title="Updating local submodels" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
</div>

- Removing ports from a local submodel is also similar to updating the exported ports. You can remove the ports using the **export functor inputs and outputs** option on the [functor action bar](../gui/Interface-Elements.html#functor-action-bar) and unchecking the corresponding port on the **Exported Ports** dialog or using the **Apply Changes / Edit Submodel Properties** dialog. Changing the order of the inputs or output ports can only be done by editing the port list on the **Apply Changes / Edit Submodel Properties** dialog.

<div class="video">
  <iframe src="https://www.youtube-nocookie.com/embed/zx6moYBS3YU?mute=1" title="Removing ports and changing port order" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
</div>

### Importing a Local Submodel Between Models

It is possible to copy local submodels definitions between models. Once the submodel is copied from one model to another, the submodels can be modified and updated independently.

You can copy a local submodel definition by dragging a local submodel from the [functor library](../gui/Interface-Elements.html#functor-library) to the [model presentation](../gui/Interface-Elements.html#model-presentation) area. The process is similar to the instantiation of a regular functor.

<div class="video">
  <iframe src="https://www.youtube-nocookie.com/embed/v8OKfyWsYoM?mute=1" title="Importing local submodels" allow="accelerometer; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy"></iframe>
</div>

It is also possible to copy the submodel definition by clicking on the **Import submodel definition** button on the [functor library bar](../gui/Interface-Elements.html#functor-library-bar) of the local submodel tab of the [functor library](../gui/Interface-Elements.html#functor-library). The definition of system submodel and system submodels can also be imported using the corresponding "Import submodel definition" button on the [functor library bar](../gui/Interface-Elements.html#functor-library-bar) of the submodel tab of the [functor library](../gui/Interface-Elements.html#functor-library).

## Publishing a Local Submodel as a User Submodel

Once your local submodel is developed and fully tested, you can turn it into a user submodel.

To publish a local submodel into a user submodel, click on the **Publish Submodel** button on the submodel **Submodel Options** drop down menu located on the model toolbar.

Turning a local submodel into a user submodel makes reusing a submodel easier, the submodel will always be available to be used on your next models, but that implies in some drawbacks as well. You are fully responsible for the consequences of updating a user submodel. Unlike local submodels, your models will not carry a copy of a user submodel as part of their definition. So, if you change a user submodel in a way that breaks compatibility with the model using its definition, your models will not work anymore.

#### Congratulations, you have successfully completed this lesson!

☞[Next: Lesson 13: Loop structures](Loop-Structures.html)
{% endraw %}
