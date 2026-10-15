---
title: "Submodel Group"
nav_order: 34
parent: "Control Functors"
grand_parent: "Functor List"
---
{% raw %}
# Submodel Group

## Description

This container executes the functors it contains using submodel semantics, discarding any content already produced by them if an error occurs.

## Inputs

None.

## Optional Inputs

None.

## Outputs

None.

## Group

[Control](../Functor-List.html#control)

## Notes

This functor is equivalent to combining [Skip All On Error](Skip-All-On-Error.html) with Trap And Ignore Errors set to false and [Log Policy](Log-Policy.html) with Maximum Log Level set to Unconditional. It exists so that a submodel can be represented without requiring Boolean Value or Log Tag.

## Internal Name

SubmodelGroup
{% endraw %}
