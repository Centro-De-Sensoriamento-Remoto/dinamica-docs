---
title: "Extract Lookup Table Attributes"
nav_order: 10
parent: "Lookup Table Functors"
grand_parent: "Functor List"
---
{% raw %}
# Extract Lookup Table Attributes

## Description

Extracts general attributes and basic statistics from a lookup table, returning them as a lookup table keyed by a predefined attribute code.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| Table | [Lookup Table Type](../types/Lookup-Table-Type.html) | Lookup table whose attributes will be extracted. |

## Optional Inputs

| Name | Type | Description | Default Value |
| --- | --- | --- | --- |
| Extract Statistical Key Attributes | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, statistical key attributes (items 10-16) are also extracted. | True |
| Extract Statistical Value Attributes | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, statistical value attributes (items 20-26) are also extracted. | True |
| Extract Dynamic Key Value Attributes | [Boolean Value Type](../types/Boolean-Value-Type.html) | If true, dynamic key and value attributes (items 30-32) are also extracted. | True |

## Outputs

| Name | Type | Description |
| --- | --- | --- |
| Attributes | [Lookup Table Type](../types/Lookup-Table-Type.html) | Table of extracted attributes, keyed by attribute code. |

## Group

[Lookup Table](../Functor-List.html#lookup-table)

## Notes

Each attribute has a predefined name that can be used to retrieve it by name (rather than by numeric key) with the `tX["NAME"]` syntax in [Calculate Map](Calculate-Map.html), [Calculate Categorical Map](Calculate-Categorical-Map.html), [Calculate Value](Calculate-Value.html), and the lookup table calculators.

If an attribute cannot be determined, its entry is omitted from Attributes rather than being filled with a placeholder.

Static attributes and their keys: 1 "uniqueKeys" (number of unique keys, i.e. rows).

Statistical key attributes and their keys (present only when Extract Statistical Key Attributes is true), where each key's associated value is used as that key's number of occurrences: 10 "minKey", 11 "maxKey", 12 "meanKey", 13 "modeKey", 14 "keyVar", 15 "keyStd", 16 "medianKey". Keys associated with a negative or zero value are treated as absent from the table for this calculation. To instead treat every key as occurring exactly once regardless of its associated value, first pass Table through a [Calculate Lookup Table Values](Calculate-Lookup-Table-Values.html) with the expression `1` to turn every value into 1, and extract attributes from the result.

Statistical value attributes and their keys (present only when Extract Statistical Value Attributes is true): 20 "minValue", 21 "maxValue", 22 "meanValue", 23 "modeValue", 24 "valueVar", 25 "valueStd", 26 "medianValue".

Dynamic key and value attributes and their keys (present only when Extract Dynamic Key Value Attributes is true): 30 "keySum" (sum of the keys; associated values are ignored), 31 "valueSum" (sum of the values), 32 "keyValueProdSum" (sum of each key multiplied by its associated value).

The minimum and maximum key or value attributes are only determined when Table has at least one entry.

See [ExtractLookupTableAttributes](../Manipulating-Tables-And-Lookup-Tables.html#extractlookuptableattributes) in [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for how this functor is used together with other table functors.

## Internal Name

ExtractLookupTableAttributes
{% endraw %}
