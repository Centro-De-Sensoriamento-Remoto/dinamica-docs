---
title: "Functor and Port Editors"
parent: Graphical Interface
nav_order: 2
---
{% raw %}
# Functor and Port Editors

How the values of a functor's ports are edited in the graphical interface. Open a functor's editor with the edit button in its [action bar](Interface-Elements.html#functor-action-bar).

## Port Tooltips

- Hovering the mouse over a port's description in an editor displays the tooltip for that port, showing its name, type, description, and flags.
- Hovering the mouse over a port's connection information ("This port input is being provided by...") displays the tooltip for the functor and output port to which the input port being edited is connected.

## Calculator Functor Editors

This applies to [Calculate Map](../functors/Calculate-Map.html), [Calculate Categorical Map](../functors/Calculate-Categorical-Map.html), [Calculate Lookup Table Values](../functors/Calculate-Lookup-Table-Values.html), [Calculate Lookup Table Keys And Values](../functors/Calculate-Lookup-Table-Keys-And-Values.html), and [Calculate Value](../functors/Calculate-Value.html).

- Hovering the mouse over a name such as `i1`, `t1`, `v1`, etc. in the editor of the port containing the expression displays the tooltip for the functor and output port to which the corresponding NumberMap, NumberTable, or NumberValue is connected.
- Clicking a name such as `i1`, `t1`, `v1`, etc. in the editor of the port containing the expression inserts the corresponding identifier at the current cursor position in the expression.
- If the functor connected to the NumberMap, NumberTable, or NumberValue has an alias, that alias is used to represent the corresponding variable (`i1`, `t1`, `v1`, etc.) in the expression shown by the editor, making it easier to read.

## Port Editors by Type

Each type page has a **GUI Editor** section describing how a port of that type is edited in the graphical interface, or why it cannot be edited there. These are the sections:

- [Base Table Type](../types/Base-Table-Type.html#gui-editor)
- [Boolean Value Type](../types/Boolean-Value-Type.html#gui-editor)
- [Categorical Map Type](../types/Categorical-Map-Type.html#gui-editor)
- [Categorization Type](../types/Categorization-Type.html#gui-editor)
- [Change Matrix Type](../types/Change-Matrix-Type.html#gui-editor)
- [Code Type](../types/Code-Type.html#gui-editor)
- [Connection Info Type](../types/Connection-Info-Type.html#gui-editor)
- [Date Type](../types/Date-Type.html#gui-editor)
- [Elevation Graph Type](../types/Elevation-Graph-Type.html#gui-editor)
- [Enum Type](../types/Enum-Type.html#gui-editor)
- [Folder Type](../types/Folder-Type.html#gui-editor)
- [Generic Filename Type](../types/Generic-Filename-Type.html#gui-editor)
- [Image Expression Type](../types/Image-Expression-Type.html#gui-editor)
- [Index Or Name Type](../types/Index-Or-Name-Type.html#gui-editor)
- [Int Set Type](../types/Int-Set-Type.html#gui-editor)
- [Integer Value Type](../types/Integer-Value-Type.html#gui-editor)
- [Kml Timeline Type](../types/Kml-Timeline-Type.html#gui-editor)
- [Kml Type](../types/Kml-Type.html#gui-editor)
- [Kmz Filename Type](../types/Kmz-Filename-Type.html#gui-editor)
- [Log Tag Type](../types/Log-Tag-Type.html#gui-editor)
- [Lookup Table Filename Type](../types/Lookup-Table-Filename-Type.html#gui-editor)
- [Lookup Table Group Type](../types/Lookup-Table-Group-Type.html#gui-editor)
- [Lookup Table Type](../types/Lookup-Table-Type.html#gui-editor)
- [Map Filename Type](../types/Map-Filename-Type.html#gui-editor)
- [Map Type](../types/Map-Type.html#gui-editor)
- [Name Type](../types/Name-Type.html#gui-editor)
- [Neighborhood Table Type](../types/Neighborhood-Table-Type.html#gui-editor)
- [Non Negative Integer Value Type](../types/Non-Negative-Integer-Value-Type.html#gui-editor)
- [None Type](../types/None-Type.html#gui-editor)
- [Null Value Type](../types/Null-Value-Type.html#gui-editor)
- [Percent Matrix Type](../types/Percent-Matrix-Type.html#gui-editor)
- [Percent Type](../types/Percent-Type.html#gui-editor)
- [Positive Integer Value Type](../types/Positive-Integer-Value-Type.html#gui-editor)
- [Projection Type](../types/Projection-Type.html#gui-editor)
- [Real Value Type](../types/Real-Value-Type.html#gui-editor)
- [Region Manager Type](../types/Region-Manager-Type.html#gui-editor)
- [String Type](../types/String-Type.html#gui-editor)
- [Struct Type](../types/Struct-Type.html#gui-editor)
- [Table Filename Type](../types/Table-Filename-Type.html#gui-editor)
- [Table Manager Type](../types/Table-Manager-Type.html#gui-editor)
- [Table Type](../types/Table-Type.html#gui-editor)
- [Table Value Type](../types/Table-Value-Type.html#gui-editor)
- [Transition Function Parameter Matrix Type](../types/Transition-Function-Parameter-Matrix-Type.html#gui-editor)
- [Transition Matrix Type](../types/Transition-Matrix-Type.html#gui-editor)
- [Transition Set Type](../types/Transition-Set-Type.html#gui-editor)
- [Tuple Type](../types/Tuple-Type.html#gui-editor)
- [Weights Filename Type](../types/Weights-Filename-Type.html#gui-editor)
- [Weights Type](../types/Weights-Type.html#gui-editor)
- [Workdir Type](../types/Workdir-Type.html#gui-editor)

## Wizards

Input and output ports of a model can be exported to a wizard. Functors that export ports to a wizard are shown with a blue border. Functors that are part of a submodel cannot export input and/or output ports to wizards.
{% endraw %}
