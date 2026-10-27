---
title: "Calculate Multiple Maps"
nav_order: 22
parent: "Map Algebra Functors"
grand_parent: "Functor List"
---
{% raw %}
# Calculate Multiple Maps

## Description

Computes several continuous raster maps at once by evaluating a single struct expression, `{ name: expression, ... }`, independently for every cell. Each field of the struct produces one map, and all the maps are returned together in a [Struct](../types/Struct-Type.html). Use [Extract Struct Map](Extract-Struct-Map.html) to retrieve each map by its field name.

Use this functor instead of several [Calculate Map](Calculate-Map.html) functors when the maps share inputs or intermediate results. The input maps are read once per cell, and a value declared with `let ... in` around the struct is calculated once per cell and reused by every field. See [Struct Expressions](../Calculate-Functors.html#struct-expressions) for the syntax.

This is one of Dinamica EGO's calculator functors. Its abbreviated (shorthand) syntax is `#*`. See [Calculator functor shorthand](../EGO-Script.html#calculator-functor-shorthand) in the EGO Script documentation for the verbose and abbreviated forms.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Expression | [Image Expression Type](../types/Image-Expression-Type.html) | Struct expression that defines how the cells of each output map are calculated. Must be enclosed in square brackets `[ ]` in EGO Script. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Cell Type | [Cell Type](../types/Cell-Type.html) | Data type for the cells of all the output maps. | Signed 32 Bit Integer |
| Null Value | [Null Value Type](../types/Null-Value-Type.html) | Sentinel value representing "no data" in all the output maps. | .default |
| Result Is Sparse | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, the output maps store only non-null cells, saving memory at the expense of random-access speed. This is an advanced port. | No |
| Result Format | [Map Type](../types/Map-Type.html) | Reference map whose spatial format (extent, resolution, projection) is applied to the output maps; its category information, if any, is ignored. Prefer this port over a Number Map hook when a map is needed only for format purposes, since a hook defines an identifier in the expression namespace and blocks abbreviated syntax if that identifier goes unused in the expression. This is an advanced port. | .none |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Result | [Struct Type](../types/Struct-Type.html) | Struct containing one [Map](../types/Map-Type.html) for each field of the expression, stored under the name of the field. The dimensions of the maps come from the connected input maps, or from Result Format when given. |

## Group

[Map Algebra](../Functor-List.html#map-algebra)

## Notes

### Struct expression

The expression must be a struct expression, written as `{ name1: expression1, name2: expression2, ... }`. A struct is accepted only as the whole expression or as the body of a `let ... in` that is the whole expression. An expression that does not produce a struct is rejected, and [Calculate Map](Calculate-Map.html) and the other calculator functors reject struct expressions. See [Struct Expressions](../Calculate-Functors.html#struct-expressions) in the Calculate Functors documentation for the complete rules.

### Evaluation

The expression is evaluated once for each cell, and the value of each field is written to the corresponding output map. Connecting data, spatial context, image virtualization and the available expression features are the same as in [Calculate Map](Calculate-Map.html).

All the output maps share the same Cell Type, Null Value, sparseness and format. When the evaluation of a field results in null or an algebraic error, such as a division by zero, only the cell of that field's map is null; the other maps are not affected. A field whose value depends on a null local variable is null.

### Accelerator devices

The calculation always runs on the processors. Expressions that produce structs are not compiled for accelerator devices.

## Internal Name

CalculateMultipleMaps

## Usage examples

The following script calculates a vegetation index, a scaled version of it and a mask in a single pass over the input maps, and then extracts each result from the struct:

```
// Shorthand
multi := #* [
    let _ndvi: (#nir - #red) / (#nir + #red)
    in {
        ndvi: _ndvi,
        scaled: _ndvi * 100,
        mask: if _ndvi > 0.3 then 1 else 0
    }
] .float32 .default .no .none;

// Verbose equivalent
multi := CalculateMultipleMaps {
    expression = [
        let _ndvi: (i1 - i2) / (i1 + i2),
            _scaled: _ndvi * 100
        in {
            ndvi: _ndvi,
            scaled: _scaled,
            mask: if _ndvi > 0.3 then 1 else 0
        }
    ],
    cellType = .float32,
    nullValue = .default,
    resultIsSparse = .no,
    resultFormat = .none
} {{
    // i1
    NumberMap nir 1;
    // i2
    NumberMap red 2;
}};

// Retrieves each map from the struct
ndvi := ExtractStructMap multi "ndvi";
scaled := ExtractStructMap multi "scaled";
mask := ExtractStructMap multi "mask";
```
{% endraw %}
