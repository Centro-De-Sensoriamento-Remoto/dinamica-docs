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

**Static attributes**

| Key | Predefined Name | Description |
| --- | --- | --- |
| 1 | "uniqueKeys" | number of unique keys, i.e. rows |

**Statistical key attributes** (present only when Extract Statistical Key Attributes is true), where each key's associated value is used as that key's number of occurrences:

| Key | Predefined Name | Description |
| --- | --- | --- |
| 10 | "minKey" | minimum key |
| 11 | "maxKey" | maximum key |
| 12 | "meanKey" | average of the keys |
| 13 | "modeKey" | mode of the keys |
| 14 | "keyVar" | variance of the keys |
| 15 | "keyStd" | standard deviation of the keys |
| 16 | "medianKey" | median of the keys |

Keys associated with a negative or zero value are treated as absent from the table for this calculation. To instead treat every key as occurring exactly once regardless of its associated value, first pass Table through a [Calculate Lookup Table Values](Calculate-Lookup-Table-Values.html) with the expression `1` to turn every value into 1, and extract attributes from the result.

**Statistical value attributes** (present only when Extract Statistical Value Attributes is true):

| Key | Predefined Name | Description |
| --- | --- | --- |
| 20 | "minValue" | minimum value |
| 21 | "maxValue" | maximum value |
| 22 | "meanValue" | average of the values |
| 23 | "modeValue" | mode of the values |
| 24 | "valueVar" | variance of the values |
| 25 | "valueStd" | standard deviation of the values |
| 26 | "medianValue" | median of the values |

**Dynamic key and value attributes** (present only when Extract Dynamic Key Value Attributes is true):

| Key | Predefined Name | Description |
| --- | --- | --- |
| 30 | "keySum" | sum of the keys; associated values are ignored |
| 31 | "valueSum" | sum of the values |
| 32 | "keyValueProdSum" | sum of each key multiplied by its associated value |

The minimum and maximum key or value attributes are only determined when Table has at least one entry.

See [ExtractLookupTableAttributes](../Manipulating-Tables-And-Lookup-Tables.html#extractlookuptableattributes) in [Manipulating Tables and Lookup Tables](../Manipulating-Tables-And-Lookup-Tables.html) for how this functor is used together with other table functors.

## Internal Name

ExtractLookupTableAttributes
{% endraw %}
