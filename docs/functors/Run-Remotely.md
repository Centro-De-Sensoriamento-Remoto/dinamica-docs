---
title: "Run Remotely"
nav_order: 28
parent: "Control Functors"
grand_parent: "Functor List"
redirect_from:
  - /Run-Remotely.html
---
{% raw %}
# Run Remotely

## Description

This container runs the functors it contains on a remote agent through a network coordinator, instead of running them on the local machine, letting the computationally heavy parts of a model be distributed to other machines. Using this container requires a coordinator and at least one agent to have been set up beforehand, and the coordinator's address and port to have been configured in Tools -> Options \| Execution \| Remote Computing, unless that connection information is instead provided through this container's own input ports.

Different Run Remotely containers in the same model can each connect to a different coordinator, letting different parts of a model be distributed across distinct coordinators and agents.

## Inputs

None.

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Coordinator Connection Info | [Connection Info Type](../types/Connection-Info-Type.html) | Coordinator connection details. When not provided, the details configured in the application settings are used instead. | None |
| Coordinator Identifier | [String Type](../types/String-Type.html) | Optional identifier used by the coordinator to reference this container when presenting information. This is an advanced port. | None |
| Network Error Behavior | [Enum Type](../types/Enum-Type.html) | Behavior to adopt when a network error occurs, such as the coordinator being unreachable. When not provided, the behavior configured in the application settings is used instead. Possible values are Abort Execution and Run Locally. This is an advanced port. | None |
| Sequence Input | [None Type](../types/None-Type.html) | Ensures that the functor connected to this port runs before this container. | None |
| Requirement Expression | [Image Expression Type](../types/Image-Expression-Type.html) | Image expression describing the requirements an agent must satisfy to be chosen to run this container's content. This is an advanced port. | None |
| Job Wait Time Limit | [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html) | Maximum time, in seconds, to wait for the job posted to the coordinator to complete. When this limit is reached, the behavior configured in Network Error Behavior is triggered. This is an advanced port. | None |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Ran Remotely | [Boolean Value Type](../types/Boolean-Value-Type.html) | False if a network error occurred and this container's content ran locally instead of remotely. This output can be ignored. |
| Sequence Output | [None Type](../types/None-Type.html) | Ensures that this container runs before the functor connected to this port. |

## Group

[Control](../Functor-List.html#control)

## Notes

Most data types can be passed from functors outside this container to functors inside it, but maps cannot; connecting a map from outside the container to a contained functor's input raises an error.

Data cannot be passed from a functor inside this container to a functor outside it; doing so raises an error.

Raises an error if a contained functor's output port of type Map has a viewer attached to it.

Reports a warning, and ignores the port's data, if a contained functor's output port has a viewer attached but its type cannot be displayed from inside this container.

When Network Error Behavior is set to Run Locally, a network error causes this container's content to run locally instead of remotely, and Ran Remotely is set to false; when set to Abort Execution, a network error instead reports an error and stops the model.

Available since Dinamica EGO 8.1.0.

See Remote Execution Feature for more information about this functor.

## Internal Name

RunRemotely
{% endraw %}
