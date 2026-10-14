---
title: "Functor Editor"
parent: Graphical Interface
nav_order: 4
---
{% raw %}
# Functor Editor

- Hovering the mouse over a port's description in an editor displays the tooltip for that port, showing its name, type, description, and flags.
- Hovering the mouse over a port's connection information ("This port input is being provided by...") displays the tooltip for the functor and output port to which the input port being edited is connected.

## Calculate Map / Calculate Categorical Map / Calculate Lookup Table Values / Calculate Lookup Table Keys And Values / Calculate Value

- Hovering the mouse over a name such as `i1`, `t1`, `v1`, etc. in the editor of the port containing the expression displays the tooltip for the functor and output port to which the corresponding NumberMap, NumberTable, or NumberValue is connected.
- Clicking a name such as `i1`, `t1`, `v1`, etc. in the editor of the port containing the expression inserts the corresponding identifier at the current cursor position in the expression.
- If the functor connected to the NumberMap, NumberTable, or NumberValue has an alias associated with it, that alias is used to represent the corresponding variable (`i1`, `t1`, `v1`, etc.) in the expression shown by the editor, making it easier to read.
{% endraw %}
