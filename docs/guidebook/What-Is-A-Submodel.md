---
title: "Lesson 10: What is a submodel, their types and where they are stored"
parent: "Guidebook"
nav_order: 12
---
{% raw %}
# Lesson 10: Submodels in Dinamica EGO

Submodels enable the reusing of parts of a model to perform specific operations inside other models. By using them, we can reduce the amount of work we have to put on when creating models that share similar functionalities. They are also an important tool for abstraction, hiding unnecessary details and making easier to reason about the model concept and its implementation. Conceptually, a submodel is a combination of functors exporting inputs and outputs to be bound externally, but, from the user point of view, a submodel is used just like any other ordinary functor.

![Submodel Overview](../image/basic_overview_submodels.png)

Submodels are also first class citizen that can be transferred from one model to another. They can also be modified and updated at any time without breaking the model where they are being used. They can also depend on other submodels, as long as their definition do not form a cycle.

## Submodel Types

Basically, we have three different types of submodels in Dinamica EGO: system submodels, user submodels and local submodels. The different types of submodels are identified by different icon badges on the representation of the corresponding functors on the model.

![Functor icon is decorated by badge representing local submodel](../image/submodel_with_badge.png)

| Type | Badge/Decoration | Documentation |
|---|---|---|
| System Submodel | ![](../image/systembadge16.png) | System submodels are submodels provided by Dinamica itself and cannot be changed by the user. System submodels can be used in models created by any user. Usually, system submodels are located at `C:\Program Files\Dinamica EGO\Submodels`. |
| User Submodel | ![](../image/userbadge16.png) | User submodels are submodels created by each user and are available only for that specific user. User submodels can be used in models created only by that user. Usually, user submodels are located at `C:\Users\<User>\Documents\Dinamica EGO\Submodels`. |
| Local Submodel | ![](../image/localbadge16.png) | Local submodels are submodels that are related to a specific model. They are bound to that model and cannot be used in a different model unless they are explicitly transferred to it. |

System and user submodels are displayed in the "Submodels" tab while local submodels are shown in the "Local Submodels" tab of the Functor Library. Local submodels are only available when their associated model is opened.

![System and user submodels on the functor library tab (left) and local submodels on the functor library tab (right)](../image/submodel_functor_library.png)

In practice, users can only create local submodels. These local submodels can later be promoted to user submodels making them a definitive part of the user's tool set.

![Different Types of Submodels](../image/submodel_types.png)

> **Note:** Changing the definition of **user submodels** may break existent models that make use of that definition, making those models useless unless the user manually updates each one of them. On the other hand, **local submodels** can be safely updated since their updates are propagated to all the local submodels of the same model and to the main model itself.

## Where Local Submodels Are Stored

Local submodels are stored in a folder based on the model name. If the model containing the local submodel is named `simulation model.egoml`, its local submodels will be stored in a subfolder called `simulation model_egoml_Submodels`. Basically, the naming algorithm just replaces "." with "_" and appends "_Submodels" to the file name. Using a unique submodel folder for each model guarantees that submodels from one model are completely independent from the submodels from any other model. Local submodels can also be defined in a folder called "Submodels" located in the same folder where the model file is located, and shared among all the models located in that folder. However, the folder is automatically converted into an unique submodel folder when the model is saved by the graphical interface.

User submodels are stored typically in the folder `C:\Users\<User>\Documents\Dinamica EGO <version>\Submodels` on Windows, or `/home/<User>/Dinamica EGO <version>/Submodels` on Linux.

Store submodels are kept in a SQLite database, typically `C:\Users\<User>\AppData\Local\Dinamica EGO <version>\SubmodelDatabase.sqlite` on Windows.

## Congratulations, you have successfully completed this lesson!

☞[Next Lesson](Creating-A-Submodel.html)
{% endraw %}
