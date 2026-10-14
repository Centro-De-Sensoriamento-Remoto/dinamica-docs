---
title: "Submodels"
nav_order: 4
---
{% raw %}
# Submodels

Submodels are a way of reusing parts of a model to perform specific operations inside other models.

By using them, we can reduce the amount of work we have to put in when creating models that share similar functionalities. They are also an important tool for abstraction, hiding unnecessary details and making it easier to reason about the model concept and its implementation.

Conceptually, a submodel is a combination of functors exporting inputs and outputs to be bound externally, but, from the user point of view, a submodel is used just like any other ordinary functor.

![Submodel Overview](image/basic_overview_submodels.png)

Submodels are also first class citizens that can be transferred from one model to another. They can also be modified and updated at any time without breaking the model where they are being used. They can also depend on other submodels, as long as their definitions do not form a cycle — if an operation (creating, updating, or using a submodel) would introduce a dependency cycle, Dinamica detects the potential cycle and prevents the operation from completing.

## Submodel Types

Basically, we have four different types of submodels in Dinamica EGO: system submodels, user submodels, local submodels, and store submodels. The different types of submodels are identified by different icon badges on the representation of the corresponding functors on the model.

> **Note:** The storage paths mentioned throughout this page (in the table below and in the [Where Submodels Are Stored](#where-submodels-are-stored) section) differ between **Windows** and **Linux**; both are listed where relevant.

![Functor icon is decorated by badge representing local submodel](image/submodel_with_badge.png)

| Type | Badge/Decoration | Description |
| --- | --- | --- |
| System Submodel | ![](image/systembadge16.png) | System submodels are submodels provided by Dinamica itself and cannot be changed by the user. System submodels can be used in models created by any user. On Windows, they are usually located at `C:\Program Files\Dinamica EGO <version>\Submodels`. On Linux, system submodels are stored inside the application itself, with no corresponding filesystem path. |
| User Submodel | ![](image/userbadge16.png) | User submodels are submodels created by each user and are available only for that specific user. User submodels can be used in models created only by that user. On Windows, they are usually located at `C:\Users\<User>\Documents\Dinamica EGO <version>\Submodels`. On Linux, they are usually located at `/home/<User>/Dinamica EGO <version>/Submodels`. |
| Local Submodel | ![](image/localbadge16.png) | Local submodels are submodels that are related to a specific model. They are bound to that model and cannot be used in a different model unless they are explicitly transferred to it. |
| Store Submodel |  | Store submodels are submodels downloaded by the user from the online Submodel Store. They are kept in a SQLite database. On Windows, it is typically located at `C:\Users\<User>\AppData\Local\Dinamica EGO <version>\SubmodelDatabase.sqlite`. On Linux, it is typically located at `/home/<User>/.local/share/Dinamica EGO <version>/SubmodelDatabase.sqlite`. |

> **Note:** If submodels of different types share the same name, there is a precedence order: **local submodels** take precedence over **user submodels**, which in turn take precedence over **store submodels**.

System and user submodels are presented in the *Submodels* tab while local submodels are presented in the *Local Submodels* tab of the Functor Library. Local submodels are only presented when their associated model is opened.

![System and user submodels on the functor library tab (left) and local submodels on the functor library tab (right)](image/submodel_functor_library.png)

In practice, users can only create local submodels. These local submodels can later be promoted to user submodels, making them a definitive part of the user's tool set.

![Different Types of Submodels](image/submodel_types.png)

### Access Scope

The four submodel types differ in who can see and use them, from narrowest to broadest:

- **Local Submodel** — scoped to the single model it belongs to. It is not automatically visible from any other model, not even other models owned by the same user; to use it elsewhere, it must be explicitly copied into that other model (see [Copying (Importing) a Local Submodel Between Models](#copying-importing-a-local-submodel-between-models)), becoming an independent copy in the process.
- **User Submodel** — scoped to the user account that created it. It is automatically available across all of that user's models, with no import step needed, but it is not visible to other users of the same machine.
- **Store Submodel** — same per-user scope as a user submodel (available across all of that user's models, not visible to other users), but its content comes from the shared online [Submodel Store](#the-submodel-store) rather than from something the user authored. The distinction from a user submodel is about origin, versioning, and storage, not visibility.
- **System Submodel** — the broadest scope: bundled with the Dinamica EGO installation itself, so it is available to every user on every model, and cannot be modified by any user.

This scope ordering is also why local submodels take precedence over user submodels, which in turn take precedence over store submodels, when names collide. A local submodel can be widened to user scope by [publishing](#turning-a-local-submodel-into-a-user-submodel-publishing) it; there is no equivalent operation to widen a user or store submodel into a system submodel.

### Where Submodels Are Stored

#### Local Submodels

Local submodels are stored together with the model script. When using the [EGO Script](EGO-Script.html) (`.ego`) or [EGOML](EGOML-Script.html) (`.egoml`) format, Dinamica creates a folder next to the script named after the script filename, with the extension replaced by `_ego` or `_egoml` and `_Submodels` appended. For example, a model named `simulation model.egoml` will have its local submodels stored in a subfolder called `simulation model_egoml_Submodels`, and the script files corresponding to each local submodel are located inside that folder. Using a unique submodel folder for each script guarantees that submodels from one script are completely independent from the submodels of any other script.

> **Note:** If a folder named "Submodels" exists in the same folder as the script, and the script-specific `..._Submodels` folder described above is not found, Dinamica reads the local submodels from that generic "Submodels" folder instead — this folder is shared among all the scripts located in that folder. This is legacy behavior and may be removed in a future version.

The EGOMLX format works differently: it stores the local submodels and the script together in the same binary file, so no separate submodel folder is used.

#### User Submodels

User submodels are typically stored in the folder `C:\Users\<User>\Documents\Dinamica EGO <version>\Submodels` on Windows, or `/home/<User>/Dinamica EGO <version>/Submodels` on Linux.

#### Store Submodels

Store submodels — those downloaded by the user from the online Submodel Store — are kept in a SQLite database. On Windows, it is typically located at `C:\Users\<User>\AppData\Local\Dinamica EGO <version>\SubmodelDatabase.sqlite`. On Linux, it is typically located at `/home/<User>/.local/share/Dinamica EGO <version>/SubmodelDatabase.sqlite`.

#### System Submodels

System submodels are provided by Dinamica itself: on Windows they are usually located at `C:\Program Files\Dinamica EGO <version>\Submodels`, while on Linux they are stored inside the application itself, with no corresponding filesystem path.

> **Tip:** Changing the definition of **user submodels** may break existing models that use that definition, making those models useless unless the user manually updates each one of them. On the other hand, **local submodels** can be safely updated since their updates are propagated to all local submodels from the same model and to the main model itself.

---

## Creating Local Submodels

Local submodels can be created by simply selecting the parts of a model that will be converted to a submodel and choosing *Edit* → *Create Submodel* (K). The selection will be replaced by the new submodel and the visual representation of the new submodel will be available to be edited as a new tab on the script editor.

At any time, the user can make changes to the local submodel and apply those changes by clicking *Apply Changes / Edit Submodel Properties* on the model toolbar. See the [Updating Local Submodels](#updating-local-submodels) section below for more information.

It is also possible to select parts of a local submodel and create another local submodel using that selection. The new local submodel will be a dependency of the previous one, but the submodel creation process is basically the same.

If the selection is empty, an empty local submodel will be created. The process for updating an empty submodel is the same process used to update any local submodel.

[Video: Creating local submodels](https://www.youtube.com/watch?v=YvoteWC_lnI)

### Creating a Submodel Directly as a Script

A submodel does not have to be created through the GUI: any `.ego` file that declares the right set of `@submodel.*` properties (name, description, group, and its input/output port declarations) is a valid submodel. See [Submodels](EGO-Script.html#submodels) in the EGO Script reference for the full property syntax.

Whether a hand-written submodel script becomes a local or a user submodel is determined entirely by where the file is placed, following the same [storage locations](#where-submodels-are-stored) used for submodels created through the GUI — the `@submodel.name` property, not the filename, is what identifies the submodel.

## Instantiating Local Submodels

Local submodels from a model are placed in a special tab on the Functor Library called *Local Submodels*. These local submodels are grouped by model name.

To instantiate a local submodel as part of a model, just expand the group on the *Local Submodels* tab corresponding to the current model and drag the submodel functor representation to the model presentation area.

It is worth noting that dragging the functor representation belonging to a different model will import the definition of the local submodel from that model — see [Copying (Importing) a Local Submodel Between Models](#copying-importing-a-local-submodel-between-models) below.

![Instantiating functor corresponding to local submodel](image/instatiating_local_submodel.gif)

### Searching for Submodels

The search boxes throughout the interface (for example, in the Explorer or in the Functor Library) support special filters that narrow results down to submodels: `is:submodel` (any submodel), `is:systemsubmodel`, `is:usersubmodel`, `is:localsubmodel`, and `is:storesubmodel`. The *Also search for additional info* option must be enabled in the search box menu for these filters to work.

## Navigating Submodels

Navigating between the local submodels and the main model in a script editor can be done by clicking on the corresponding model/submodel tab on the model/submodel tabs or clicking on the submodel overview button above the model/submodel tabs.

![Navigating between local submodels](image/navigating_submodels.png)

## Updating Local Submodels

At any time, the user can add or remove inputs and outputs or even change the combination of functors defining the submodel.

The functor action bar of all functors contained inside a submodel script exhibits additional options for *export functor inputs and outputs*. Exporting a new input or output can be performed following the steps below:

First, click on the functor whose inputs or outputs will be exported.

Select *export functor inputs and outputs* on the functor action bar and choose the inputs or outputs that will be exported. It is possible to define the input and output names and their corresponding descriptions. It is also possible to mark an exported input as advanced or optional. Optional inputs can also define an optional value that will be assigned to the port if no explicit value is provided. A submodel's input ports cannot be declared nullable; a caller-optional input is only made available through this *optional* marking and its associated default value, not by accepting a null value directly.

> **Note:** Any port from the integer family of types can be declared a light enum, which presents it in the GUI as a labeled dropdown instead of a free-form numeric field, via the *Make port available as an enum value* control. This is not specific to submodels — it can be set on any carrier functor of an integer value type in any model, provided the carrier has an editor. When such a carrier's port is exported as a submodel input, its light enum configuration carries over into the submodel's interface.

Choose *Submodel Options* on the model toolbar and then click *Apply Changes / Edit Submodel Properties*. That brings up the submodel editor dialog where you can define a new name, description, documentation URL, and icon for the submodel, or reorder its inputs and outputs (or even remove some of them). Clicking *Ok* propagates the changes to all parts of your model (and dependent submodels) where the submodel is used.

The submodel editor dialog also lets you set the submodel's **group**, which controls where it appears in the Functor Library. A group name can contain subgroups by separating them with a colon (`":"`); for example, `"Elevation Graph:Tools:Debug"` places the submodel in a *Debug* subgroup, itself inside a *Tools* subgroup, inside an *Elevation Graph* group. This is specific to submodels: an ordinary functor's placement in the Library is fixed by its own definition and cannot be changed by the user, but a submodel's group — and therefore whether it appears in a subgroup — is under the control of whoever creates or edits it.

Below you can see two examples of updating the input and output ports of a local submodel:

- **Example 1** — exporting and updating ports using the functor action bar:<br> [Video: Updating local submodels ports](https://www.youtube.com/watch?v=i6T9GGqfU80)
- **Example 2** — an additional approach to the same task:<br> [Video: Updating local submodels ports (additional approach)](https://www.youtube.com/watch?v=FK5xIYCS0KI)

Beware that connected inputs cannot be exported. They must be disconnected first.

It is also worth noting that it is possible to safely rename inputs and outputs. The connections to the port will be maintained when the changes are propagated.

> **Tip:** Dinamica EGO comes with a set of icons from the [Fat Cow Icon Set](http://www.fatcow.com/free-icons) that can be used to customize the local submodels created by users. The icons come in size 16x16 and 32x32 pixels. The overall color of the chosen icon is automatically used to define the color of the functor representing the submodel on the graphical interface. The set of icons is usually installed in the folder `IconSamples` in your Dinamica EGO installation folder.

When updating a local submodel, the changes from all dependent local submodels will also be propagated. This means that updating a submodel always updates the whole chain of local submodels that use that submodel as part of their definition.

[Video: Updating local submodels (propagation through a chain of dependent submodels)](https://www.youtube.com/watch?v=wDtyrRbUNo4)

Removing ports from a local submodel is also similar to updating the exported ports. You can remove the ports using the *export functor inputs and outputs* option on the functor action bar and unchecking the corresponding port on the *Exported Ports* dialog, or using the *Apply Changes / Edit Submodel Properties* dialog.

Changing the order of the input or output ports can only be done by editing the port list on the *Apply Changes / Edit Submodel Properties* dialog.

[Video: Removing ports and changing port order](https://www.youtube.com/watch?v=zx6moYBS3YU)

## Submodel Dependencies

Since submodels can use other submodels as part of their definitions, it is very convenient to know how those dependencies are organized. The dependency viewer is not limited to local submodels — it shows the local, user, store, and system submodels a model uses, and how they depend on each other.

You can open it by clicking the graph icon at the bottom of the model toolbar, or by choosing *Submodels* → *Show Model Dependencies* (Ctrl+U).

![Local submodel dependency viewer](image/local_submodel_dependencies.png)

On the dependency graph viewer, every submodel involved is represented by its name and corresponding icon. An arrow pointing from a submodel A to a submodel B means that submodel A is used by submodel B. Multiple arrows mean that a submodel is used more than once. Clicking on any local submodel shown in the visualization navigates to it.

Clicking the *Remove Unused* button removes all local submodels defined by the current model that are not being used, either as part of the model's own definition or by any of its other local submodels.

## Copying (Importing) a Local Submodel Between Models

It is possible to copy local submodel definitions between models. Once the submodel is copied from one model to another, the submodels can be modified and updated independently.

You can copy a local submodel definition by dragging a local submodel from the Functor Library to the model presentation area. The process is similar to the instantiation of a regular functor.

[Video: Importing local submodels](https://www.youtube.com/watch?v=v8OKfyWsYoM)

It is also possible to copy the submodel definition by clicking the *Import submodel definition* button on the functor library bar of the local submodel tab of the Functor Library. The definitions of system and user submodels can also be imported using the corresponding *Import submodel definition* button on the functor library bar of the submodel tab of the Functor Library.

Submodels already used in the model can also be imported through the *Submodels* menu: *Submodels* → *Import Selected Submodel* (Ctrl+G) imports the definition of the currently selected submodel instance, while *Submodels* → *Import All Submodels* imports the definitions of every system, store, and user submodel used directly or indirectly by the model.

## Turning a Local Submodel into a User Submodel (Publishing)

Once your local submodel has been developed and fully tested, you can turn it into a user submodel.

To publish a local submodel into a user submodel, click the *Publish Submodel* button on the *Submodel Options* drop-down menu located on the model toolbar.

Turning a local submodel into a user submodel makes reusing the submodel easier — the submodel will always be available to be used in your next models — but it has some drawbacks as well. You are fully responsible for the consequences of updating a user submodel. Beware that, unlike local submodels, your models will not carry a copy of a user submodel as part of their definition. So, if you change a user submodel in a way that breaks compatibility with the models using its definition, those models will not work anymore.

### Dependency Propagation When Publishing as a User Submodel

When a local submodel is published as a user submodel, its dependencies become local submodels of the published submodel, rather than independent user submodels of their own.

Consider a local submodel **A** that depends on local submodels **B** and **C**, where **B** also depends on **C**. Publishing **A** as a user submodel produces a single user submodel, **A**, containing **B** and **C** as local submodels of **A**. **B** and **C** sit side by side inside **A**'s own local submodel set, so **B** does not get a separate copy of **C** — it uses the single copy of **C** held by their common parent **A**, the same way one local submodel depends on another local submodel of the same model. **B** and **C** are not added to the user's submodel set as independent, top-level entries — only **A** is.

This flat structure holds regardless of whether **A** uses **C** directly. Even if **C** is used only by **B**, and not by **A** itself, publishing **A** still places **B** and **C** side by side as local submodels of **A** — **C** is not nested inside **B**.

### Republishing and Naming Collisions

Publishing or sending a submodel again — whether because the local submodel changed, or because a user submodel of the same name already exists for some other reason — behaves differently depending on the target:

- **User submodels are overwritten by name.** Publishing a local submodel as a user submodel always replaces whatever user submodel currently holds that name, whether that is an earlier published version of the same submodel or an unrelated existing user submodel that happens to share the name. Since dependencies become local submodels of the published submodel rather than independent user submodels (see [Dependency Propagation When Publishing as a User Submodel](#dependency-propagation-when-publishing-as-a-user-submodel) above), republishing **A** does not touch any independently named user submodels **B** or **C** — it simply replaces **A**'s local submodels **B** and **C** with their current definitions.
- **Store submodels are versioned, not overwritten.** Sending a submodel to the Store again does not replace the previous submission; it creates a new version, tagged with the Dinamica EGO version in use at the time, following the same versioning behavior described in [Versioning and Compatibility](#versioning-and-compatibility).

### Sending a Submodel to the Store

A user submodel can be sent to the online [Submodel Store](#the-submodel-store), becoming a store submodel. There are two ways to do this:

- From a local submodel directly, using the *Publish Submodel as a Store Submodel* option on the *Submodel Options* drop-down menu. This first turns the local submodel into a user submodel, then sends that user submodel to the Store.
- From an existing user submodel, using the corresponding button on the *Submodel Manager* dialog (*Submodels* → *Submodel Manager*), which sends that user submodel to the Store directly.

### Dependency Propagation When Sending to the Store

When a submodel is sent to the Store, its dependencies are packaged with it rather than published as independent store submodels.

Consider the same local submodel **A**, depending on **B** and **C**, with **B** also depending on **C**. Sending **A** to the Store as a store submodel produces the following structure:

- **A** receives its own local submodel copy of **B** and its own local submodel copy of **C**.
- **B**, in turn, receives its own local submodel copy of **C** — a separate copy from the one held directly by **A**.

The store submodel package therefore ends up containing two independent copies of **C**: one local to **A**, and one local to **B**. Once packaged, these copies are independent of each other, the same as any other local submodels obtained through copying (see [Copying (Importing) a Local Submodel Between Models](#copying-importing-a-local-submodel-between-models)).

Unlike publishing to a user submodel, this nesting follows the actual dependency graph. If **C** is used only by **B**, and not by **A** itself, the store submodel package nests **C** inside **B** instead of placing it directly inside **A**: **C** becomes a local submodel of **B**, and **B** a local submodel of **A**.

### Dependencies Are Scoped to Their Store Submodel

The local submodel copies of **B** and **C** packaged inside store submodel **A** exist only because **A** depends on them — they have no independent identity of their own. A packaged dependency inside one store submodel is entirely independent of a same-named dependency packaged inside a different store submodel, and of any unrelated user or store submodel that might share the same name; each store submodel's packaged dependencies are private to it.

## The Submodel Store

The Submodel Store is Dinamica EGO's online repository of submodels shared by the community.

### Browsing and Installing Submodels

To browse and install submodels from the Submodel Store, choose *Submodels* → *Submodel Store* on the model toolbar. Select the desired submodel from the list and click *Install Selected* to download it; it then becomes available locally as a store submodel.

> **Tip:** To publish your own submodel to the Store instead of installing one, see [Sending a Submodel to the Store](#sending-a-submodel-to-the-store).

### Versioning and Compatibility

Store submodels are versioned in relation to the Dinamica EGO version active at the time each update is published, rather than through an independent version number. Each time a submodel is published or updated, that update is tagged with the Dinamica EGO version used to make it.

When a user requests a store submodel, they receive the **most recently published update that is compatible with their installed version** — that is, the newest update, among all updates tagged with a version less than or equal to the user's own, regardless of whether an even newer update exists for a higher, incompatible version. Updating a submodel using the same Dinamica EGO version as a previous update simply overrides that previous update, since both share the same version tag.

This has a subtle consequence: an update published later using an **older** Dinamica EGO version can still become the newest compatible update for users on a **newer** version, superseding an update they had previously received — as long as no newer update exists that is tagged with an even higher version. The following worked example illustrates this:

1. A user on Dinamica 8.10 publishes Submodel X, then updates it twice more, all while still on 8.10. Since every one of these updates shares the same version tag (8.10), each one overrides the previous one, leaving "Submodel X v3" as the current update tagged 8.10.
1. At this point, both Dinamica 8.10 and Dinamica 8.11 users receive "Submodel X v3" — 8.10 because it is their own version's update, and 8.11 because no update tagged 8.11 exists yet, so the newest compatible update is still the one tagged 8.10.
1. A user on Dinamica 8.11 now updates Submodel X to "v4". This creates a new update tagged 8.11. From this point, Dinamica 8.11 users receive "Submodel X v4" (the newest update compatible with 8.11), while Dinamica 8.10 users are unaffected and still receive "Submodel X v3" (the update tagged 8.11 is not compatible with them).
1. A user on Dinamica 8.10 now updates Submodel X again, to "v3.1". This overrides the existing update tagged 8.10 (previously "v3"). Dinamica 8.10 users now receive "Submodel X v3.1". Because this update is more recent than the "v4" update tagged 8.11, it also becomes the newest compatible update for Dinamica 8.11 users — so Dinamica 8.11 users now receive "Submodel X v3.1" too, even though "v4" still exists.

### Checking for Updates

To check whether an installed store submodel has a newer, compatible update available (see [Versioning and Compatibility](#versioning-and-compatibility) above), choose *Submodels* → *Submodel Manager* (Ctrl+G), then use the *Check for Updates* option.

## Deleting Submodels

### Deleting a Local Submodel

To delete a local submodel, select it among the local submodels of the model and choose *Remove Submodel* on the *Submodel Options* menu. If the submodel is still being used — either by the main model script or by another local submodel — Dinamica reports this, shows where it is being used, and the removal fails.

> **Tip:** Before attempting to remove a local submodel, it is a good idea to check the [dependency viewer](#submodel-dependencies) (*Submodels* → *Show Model Dependencies*) to confirm the submodel is not being used elsewhere.

### Deleting a User or Store Submodel

User and store submodels are both removed through the *Submodel Manager* dialog (*Submodels* → *Submodel Manager*): select the submodel in question and click *Remove*.

> **Warning:** Removing a user submodel will break any model script that uses it as part of its definition, since — unlike local submodels — models do not carry their own copy of a user submodel's definition.

## Submodel Expansion and Execution

Before executing a model, Dinamica EGO can expand all submodels used in it, replacing each submodel instance with its internal functor definition. This expansion does not modify the model the user is working on — it is applied to a copy of the model that is submitted for execution, leaving the original model and its submodel instances untouched. This removes data copy constraints caused by submodel usage.

- This behavior is controlled by the *Expand submodels before executing a model* option, found under *Tools* → *Options* | *Advanced*. On the command line, it can be disabled using the `-disable-submodel-expansions` flag of the [Dinamica Console](Dinamica-Console.html).
- When submodel expansion is enabled, the *Remove all unnecessary intermediate carrier functors before executing a model* option (same Options panel; `-remove-redundant-carriers` on the command line) can additionally be enabled to remove unnecessary intermediate carrier functors introduced by the expansion. Use with caution: removal can prevent the content of some output ports from being inspected and, in rare cases, may change model semantics.

It is also possible to manually expand submodels as part of editing the model itself, replacing a submodel instance — local, user, store, or system — with its internal definition. This can be done for the currently selected submodel via *Submodels* → *Expand Selected Submodel* (Ctrl+E), or for every submodel used directly or indirectly by the model via *Submodels* → *Expand All Submodels*. Unlike the automatic expansion that happens before execution, these options do change the model being edited by the user — the expanded functors permanently replace the submodel instance in the model.

---

## See Also

- Functor Library
- Model Presentation
- [Dinamica Console](Dinamica-Console.html)
- [EGO Script — Submodels](EGO-Script.html#submodels)
{% endraw %}
