---
title: "Manipulating Tables and Lookup Tables"
nav_order: 1
parent: "Modeling Guides"
---
{% raw %}
# Manipulating Tables and Lookup Tables

## Overview

This page covers the functors and techniques used to read, iterate over, and restructure Tables and Lookup Tables once they exist. See [Table Type](types/Table-Type.html) and [Lookup Table Type](types/Lookup-Table-Type.html) for the general format of these two types — column naming, key marking, and type inference — which this page assumes as background.

## Tuple Type

A **Tuple** is a sequence of table cells, most often used to represent the key (or full set of keys) identifying a table row. Tuple elements are ordered by column index and have no names of their own — a Tuple by itself doesn't say which column each element belongs to; that mapping only exists in the context of the table it's being used against.

A Tuple literal uses bracket syntax — `[2007]` for a single-element Tuple, `[2007, "Boston"]` for several at once, the same list syntax a Table or Lookup Table literal uses. This bracket form is required when writing a Tuple as a literal constant: automatic conversion between types, such as a Real value becoming a one-element Tuple, only happens when a value is **connected** from one port to another — a variable reference, or a functor call inlined directly into the argument — never when a literal constant is parsed straight into a port (see [Constants](EGO-Script.html#constants) for this rule stated generally, beyond just Tuples). Each port's literal syntax is parsed by that type's own parser, which only accepts its own type's literal form; a bare `2007` fails wherever a Tuple is expected, even though a Real *value*, once connected, converts to a Tuple automatically. Binding a Tuple literal to a reusable name goes through the [Tuple](functors/Tuple.html) functor, the same way [Table](functors/Table.html) and [Lookup Table](functors/Lookup-Table.html) wrap their own literals.

[Add Tuple Value](functors/Add-Tuple-Value.html) serves a different case: appending one element — often a connected variable, rather than a literal — to a Tuple that already exists. Every example below that builds a key from a variable, rather than writing every element as a literal, uses it for exactly this.

```
// A Tuple literal can hold more than one element directly, the same as a
// Table or Lookup Table literal; binding it to a name goes through Tuple.
fullKey := Tuple [2007, "Boston"];

// AddTupleValue reaches a one-element Tuple the same way, then appends to
// it — the pattern used throughout this page, typically with a connected
// variable rather than a second literal like the one shown here.
yearOnly := Tuple [2007];
alsoFullKey := AddTupleValue yearOnly "Boston";
```

Every functor below that identifies a row or sub-table by key takes that key as a Tuple.

Three functors operate on Tuples themselves, independently of any table.

### AddTupleValue

Appends one element to the end of a Tuple.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `tuple` | Input | Tuple | Yes | The Tuple to append to. |
| `value` | Input | TableValue | Yes | The element to append. |
| `result` | Output | Tuple | — | The Tuple with the new element at the end. |

### GetTupleSize

Reports how many elements a Tuple holds.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `tuple` | Input | Tuple | Yes | The Tuple to measure. |
| `result` | Output | Real | — | The number of elements. |

### GetTupleValue

Retrieves one element by position rather than by column name.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `index` | Input | index | Yes | Which element to retrieve, counting from 1. |
| `tuple` | Input | Tuple | Yes | The Tuple to read from. |
| `result` | Output | TableValue | — | The element at that position, as a generic value holding either a Real or a String. |

## Retrieving values, rows, and columns

### GetTableValue

Reads a single cell.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `table` | Input | Table | Yes | The table to read from. |
| `keys` | Input | Tuple | Yes | The key identifying the row. |
| `column` | Input | name or index | Yes | Which value column to read. An index counts every column left to right, starting at 1, including key columns: the first key column has index 1, and the first value column's index is one past the number of key columns, not 1 (see [Table Type](types/Table-Type.html)). |
| `valueIfNotFound` | Input | TableValue | No | Returned instead of failing if the key isn't present. |
| `result` | Output | TableValue | — | The value at that key and column, as a generic value holding either a Real or a String. It converts to whichever of the two the column actually holds when it is connected onward. |

### GetTableRow

Reads an entire row — key and value columns together — for one key at once.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `keys` | Input | Tuple | Yes | The key identifying the row. |
| `table` | Input | Table | Yes | The table to read from. |
| `result` | Output | Tuple | — | The full row, as a Tuple — the key comes first, followed by each value column in order. |

### GetLookupTableValue

The Lookup Table equivalent of `GetTableValue` — no column argument, since a Lookup Table only ever has one.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `table` | Input | Lookup Table | Yes | The lookup table to read from. |
| `key` | Input | Real | Yes | The key to look up. |
| `valueIfNotFound` | Input | Real | No | Returned instead of failing if the key isn't present. |
| `value` | Output | Real | — | The value for that key. |

### GetTableColumn

Retrieves an entire column, across every row, as a new table containing just the keys and that one column — unlike the three functors above, which each read a single cell or a single row.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `table` | Input | Table | Yes | The table to read from. |
| `columnIndexOrName` | Input | name or index | Yes | Which value column to retrieve. |
| `result` | Output | Table | — | A table with the same keys as the input, holding only the one retrieved column. |

**Example** — [Calc Areas](functors/Calc-Areas.html) returns a single output of type Table, with columns `Category` (key), `Area_In_Cells`, `Area_In_Hectares`, and `Area_In_Square_Meters` — every area measure for every category, in one call. A common mistake is to treat this output as if it were a single hectares figure; it's a table, and the column of interest has to be read out of it:

```
areaTable := CalcAreas landscape .no;
// the Area_In_Hectares column
hectaresColumn := GetTableColumn areaTable 3;
```

**Example** — a small constant table and lookup table, each read with the functor above that matches its shape:

```
myLookupTable := LookupTable [
    "Key" "Value",
    1 10,
    2 20,
    3 30
];
// lookedUpValue will be 20.
lookedUpValue := GetLookupTableValue myLookupTable 2;

myTable := Table [
    "CityId*", "Population", "Area",
    1, 667137, 125,
    2, 39398, 6
];
// population will be 667137.
population := GetTableValue myTable [1] "Population";

// wholeRow will be the three-element Tuple (2, 39398, 6) — the key (CityId)
// first, then Population, then Area.
wholeRow := GetTableRow [2] myTable;
```

### GetTableKeys

Lists the keys of a table's first key column.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `table` | Input | Table or Lookup Table | Yes | The table whose keys are wanted. |
| `keys` | Output | Table | — | One row per distinct key of the input's first key column: a unique index, then the key itself. |

## Iterating over Lookup Table values

A [For Each](functors/For-Each.html) loop executes once per row of the table connected to its `elements` port, which accepts either a general Table or a Lookup Table; over a Lookup Table that means once per key. Inside the loop, a [Step](functors/Step.html) functor retrieves the current key — its input auto-binds to the container's current iteration value, the same mechanism described in [Internal output ports](EGO-Script.html#internal-output-ports), so it needs no explicit wiring. From there, the key can be used directly, or passed to [Get Lookup Table Value](functors/Get-Lookup-Table-Value.html) to retrieve the corresponding value.

A loop like this can often run its iterations in parallel — see [Basic Data Flow](Basic-Data-Flow.html) for the conditions that allow it.

> **Note:** A loop that only prints, like the one below, meets those conditions — no mux, nothing consumed outside the loop, no submodel output port — so the engine is free to run iterations in any order, or concurrently. The printed lines can come out in a different order than the source table, and if two iterations genuinely run at the same time, their output can even interleave rather than appearing as clean, separate lines. Forcing a specific order means forcing sequential execution, which means introducing a mux — a plain `MuxValue 0 0` is enough, at the cost of losing the parallelism these loops would otherwise qualify for; see [The one exception: feedback in loops](Basic-Data-Flow.html#the-one-exception-feedback-in-loops).

> **Note:** Dinamica prints every functor's own start and end at the Info level. Left unfiltered, a `Print` call's message would be buried in that noise. Wrapping the loop in [Log Policy](functors/Log-Policy.html), with `maximumLogLevel = .result`, restricts what gets logged from inside it to Result and anything more severe — Unconditional, Error, Warning, Result; Info and the Debug levels are suppressed. `Print`'s own `logLevel = .result` then places the custom message at exactly that threshold, so it stays visible. Every example on this page that prints uses both together for that reason.

**Example** — printing every entry of a Lookup Table. [Print](functors/Print.html) is itself a container — its `initialMessage` is printed before whatever it contains runs, so an empty `{{ }}` block is enough when the only goal is to print something. [Create String](functors/Create-String.html) builds a message from a format string and the values connected inside it, referenced the same way a Code expression references a hook (see [Verbose form](EGO-Script.html#verbose-form)) — by a numbered, type-prefixed tag (`<v1>` for the first connected value, and so on). This example also uses `{ initialMessage = message, logLevel = .result }` [nominal syntax](EGO-Script.html#nominal-syntax) for `Print`, and the `_` [discard convention](EGO-Script.html#positional-syntax) for outputs that aren't needed:

```
myLookupTable := LookupTable [
    "Key" "Value",
    1 10,
    2 20,
    3 30
];

LogPolicy { maximumLogLevel = .result } {{
    _ := ForEach myLookupTable {{
        key := Step;
        value := GetLookupTableValue myLookupTable key;

        message := CreateString "(Key: <v1>, Value: <v2>)" {{
            NumberValue key 1;
            NumberValue value 2;
        }};

        Print { initialMessage = message, logLevel = .result } {{ }};
    }};
}};
```

## Iterating over Table rows

Table rows are iterated the same way, but need one extra functor: [Get Table Keys](functors/Get-Table-Keys.html) returns a table mapping unique indices to the keys of the input table's first key column. When the key column is already Real-typed, those indices and the keys are the same numbers, so the mapping is trivial. When the key column is String-typed, the indices are distinct numeric placeholders, and a `GetTableValue` call inside the loop is needed to map the current index back to its actual String key — this indirection is *why* String-typed key columns are usually avoided when a table will be iterated (see [Table Type](types/Table-Type.html)).

A table with more than one key column can only be iterated one key column at a time this way. To examine every key column, nest loops — see [Sub-Tables](#sub-tables) below.

**Example** — printing every entry of a Table with a Real-typed key column. General tables are wrapped in `Table` rather than `LookupTable`:

```
myTable := Table [
    "CityId*", "Population",
    1, 667137,
    2, 39398
];

allKeys := GetTableKeys myTable;

LogPolicy { maximumLogLevel = .result } {{
    _ := ForEach allKeys {{
        key := Step;
        value := GetTableValue myTable key "Population";

        message := CreateString "(Key: <v1>, Value: <v2>)" {{
            NumberValue key 1;
            NumberValue value 2;
        }};

        Print { initialMessage = message, logLevel = .result } {{ }};
    }};
}};
```

**Example** — the same, but with a String-typed key column. This is the extra-indirection case described above: `GetTableKeys` returns indices, not the original keys, so an extra `GetTableValue` inside the loop maps each index back to its String key before it can be used:

```
myStringKeyedTable := Table [
    "CityName*#string", "Population",
    "Boston", 667137,
    "Chelsea", 39398
];

indexToKey := GetTableKeys myStringKeyedTable;

LogPolicy { maximumLogLevel = .result } {{
    _ := ForEach indexToKey {{
        index := Step;
        key := GetTableValue indexToKey index 2;
        value := GetTableValue myStringKeyedTable key "Population";

        message := CreateString "(Key: <s1>, Value: <v1>)" {{
            NumberString key 1;
            NumberValue value 1;
        }};

        Print { initialMessage = message, logLevel = .result } {{ }};
    }};
}};
```

**Example** — a table with more than one value column. Nothing new is needed: call `GetTableValue` once per value column and combine the results:

```
myTable := Table [
    "CityId*", "Population", "Area",
    1, 667137, 125,
    2, 39398, 6
];

allKeys := GetTableKeys myTable;

LogPolicy { maximumLogLevel = .result } {{
    _ := ForEach allKeys {{
        key := Step;
        population := GetTableValue myTable key "Population";
        area := GetTableValue myTable key "Area";

        message := CreateString "(CityId: <v1>, Population: <v2>, Area: <v3>)" {{
            NumberValue key 1;
            NumberValue population 2;
            NumberValue area 3;
        }};

        Print { initialMessage = message, logLevel = .result } {{ }};
    }};
}};
```

## Sub-Tables

A **sub-table** is a table containing only the rows matching one specific value of a key, with that key column removed from the result. Sub-tables are how Dinamica handles tables with more than one key column: peel off one key at a time, working with what remains.

### GetTableFromKey

Retrieves the rows matching the given key(s), with those key columns dropped from the result.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `table` | Input | Table | Yes | The table to read from. |
| `keys` | Input | Tuple | Yes | The leftmost key(s) identifying the sub-table. |
| `result` | Output | Table | — | The matching sub-table. |

### SetTableByKey

Inserts or replaces the rows matching the given key(s).

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `table` | Input | Table | Yes | The table to update. |
| `keys` | Input | Tuple | Yes | The leftmost key(s) identifying where the sub-table goes. |
| `subTable` | Input | Table | Yes | The replacement rows. Column types must match `table`, and so must column names unless `ignoreColumnNames` says otherwise. |
| `ignoreColumnNames` | Input | Boolean | No | Skips validating the sub-table's column names against `table`. Default `.no`. |
| `combineSubTables` | Input | Boolean | No | Merges the incoming rows with the sub-table already stored under those keys instead of replacing it. Default `.no`. |
| `result` | Output | Table | — | The updated table. |

Both [Get Table From Key](functors/Get-Table-From-Key.html) and [Set Table By Key](functors/Set-Table-By-Key.html) only operate on the table's **leftmost** key column(s) — they can't reach into the middle of a composite key. If the key you need isn't leftmost, reorder the columns first with [Reorder Table Column](functors/Reorder-Table-Column.html), which moves one column (key or value) to a new index; key and value columns can't be moved across each other.

### ReorderTableColumn

Moves one column to a new position.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `table` | Input | Table | Yes | The table to reorder. |
| `columnIndexOrName` | Input | name or index | Yes | Which column to move. |
| `newColumnIndex` | Input | index | Yes | The position to move it to. |
| `result` | Output | Table | — | The reordered table. |

### SetTableCellValue

Writes a single cell — the write counterpart to `GetTableValue`.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `table` | Input | Table | Yes | The table to update. |
| `column` | Input | name or index | Yes | Which value column to write to. |
| `keys` | Input | Tuple | Yes | The key identifying the row. |
| `value` | Input | TableValue | Yes | The value to store. |
| `result` | Output | Table | — | The updated table. |

**Worked example.** Take a table of commodity prices, keyed by `Year` and `City`:

| Year\* | City\* | Price |
| --- | --- | --- |
| 2004 | Boston | 1200 |
| 2004 | Chelsea | 1453 |
| 2007 | Boston | 4332 |
| 2007 | Chelsea | 233 |

Retrieving the sub-table for `Year` 2007 — a single key, since `Year` is leftmost — leaves `City`/`Price` pairs:

| City\* | Price |
| --- | --- |
| Boston | 4332 |
| Chelsea | 233 |

To instead retrieve by `City` first, `City` would need to be reordered ahead of `Year`, since `GetTableFromKey` can only key off the leftmost column(s). With three key columns, the same idea nests: peel off the leftmost key to get a sub-table, then peel off the next leftmost key of *that* sub-table, and so on — which is exactly how nested `ForEach` loops iterate a multi-key table one column at a time; see [Container functors](EGO-Script.html#container-functors) for how nesting containers this way affects execution order.

**Example** — building the table above, retrieving the 2007 sub-table, updating one of its prices with [Set Table Cell Value](functors/Set-Table-Cell-Value.html), writing it back, and finally reordering `City` ahead of `Year` to key by `City` instead:

```
priceTable := Table [
    "Year*", "City*", "Price",
    2004, "Boston", 1200,
    2004, "Chelsea", 1453,
    2007, "Boston", 4332,
    2007, "Chelsea", 233
];

// Retrieve the City*/Price sub-table for Year 2007.
pricesIn2007 := GetTableFromKey priceTable [2007];

// Replace the price for Chelsea within that sub-table.
updatedPricesIn2007 := SetTableCellValue pricesIn2007 "Price" ["Chelsea"] 999;

// Write the modified sub-table back under the same key.
priceTable2 := SetTableByKey priceTable [2007] updatedPricesIn2007;

// Move City (currently index 2) ahead of Year (index 1), so sub-tables can
// instead be retrieved by City first.
priceTableByCity := ReorderTableColumn priceTable2 "City" 1;
// citySubTable will be the Year*/Price pairs for Boston.
citySubTable := GetTableFromKey priceTableByCity ["Boston"];
```

**Example** — printing every entry of a table with more than one key column. `GetTableKeys` only ever iterates the *first* key column, so a table with several needs one nested loop per extra key: peel off a sub-table for each `Year`, then iterate the `City` key within it:

```
priceTable := Table [
    "Year*", "City*", "Price",
    2004, "Boston", 1200,
    2004, "Chelsea", 1453,
    2007, "Boston", 4332,
    2007, "Chelsea", 233
];

yearKeys := GetTableKeys priceTable;

LogPolicy { maximumLogLevel = .result } {{
    _ := ForEach yearKeys {{
        year := Step;
        pricesInYear := GetTableFromKey priceTable year;

        cityKeys := GetTableKeys pricesInYear;

        _ := ForEach cityKeys {{
            cityIndex := Step;
            // City is String-typed, so cityIndex is a placeholder, not the real
            // city — map it back the same way as any String-typed key column.
            city := GetTableValue cityKeys cityIndex 2;
            price := GetTableValue pricesInYear city "Price";

            message := CreateString "(Year: <v1>, City: <s1>, Price: <v2>)" {{
                NumberValue year 1;
                NumberString city 1;
                NumberValue price 2;
            }};

            Print { initialMessage = message, logLevel = .result } {{ }};
        }};
    }};
}};
```

A modified version of the same example: instead of reading `Price` from the City-only sub-table, build the full composite key — both `Year` and `City` together, as a Tuple — and read directly from the original table:

```
priceTable := Table [
    "Year*", "City*", "Price",
    2004, "Boston", 1200,
    2004, "Chelsea", 1453,
    2007, "Boston", 4332,
    2007, "Chelsea", 233
];

yearKeys := GetTableKeys priceTable;

LogPolicy { maximumLogLevel = .result } {{
    _ := ForEach yearKeys {{
        year := Step;
        pricesInYear := GetTableFromKey priceTable year;

        cityKeys := GetTableKeys pricesInYear;

        _ := ForEach cityKeys {{
            cityIndex := Step;
            city := GetTableValue cityKeys cityIndex 2;

            // The composite key, built by appending City onto Year.
            fullKey := AddTupleValue year city;

            price := GetTableValue priceTable fullKey "Price";

            message := CreateString "(Year: <v1>, City: <s1>, Price: <v2>)" {{
                NumberValue year 1;
                NumberString city 1;
                NumberValue price 2;
            }};

            Print { initialMessage = message, logLevel = .result } {{ }};
        }};
    }};
}};
```

`GetTableFromKey` is still needed, because `GetTableKeys` only ever returns the first key column and so cannot enumerate the cities directly: taking the sub-table for a `Year` is what makes `City` the first key column, and therefore enumerable. What changes is the read itself: `GetTableValue` is called against `priceTable` with the full `(Year, City)` Tuple, not against `pricesInYear` with `City` alone.

## Storing results across a loop

A [Mux Table](functors/Mux-Table.html) or [Mux Lookup Table](functors/Mux-Lookup-Table.html) can carry a Table or Lookup Table across the iterations of a loop, the same way [Mux Value](functors/Mux-Value.html) carries a single value — see [Carrying and selecting values across iterations](EGO-Script.html#carrying-and-selecting-values-across-iterations). Each iteration reads the mux's current output, adds a row to it with `AddTableRow`, and feeds the result back in as the mux's `feedback` input for the next iteration, building up a result table one row at a time.

The accumulated table is read after the loop the same way any container's internal result is read from outside it: a functor after the loop simply takes the accumulator's feedback variable as an input. There's nothing special about this — the loop is guaranteed to finish before anything depending on it runs, per [Basic Data Flow](Basic-Data-Flow.html).

### AddTableRow

Appends a row to a Table.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `table` | Input | Table | Yes | The table to add a row to. |
| `values` | Input | Tuple | Yes | The whole row — key columns first, then value columns, in column order. |
| `result` | Output | Table | — | The table with the new row. |

### SetLookupTableValue

Inserts or replaces one entry of a Lookup Table. It plays the same role for a Lookup Table accumulator that `AddTableRow` plays for a Table one.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `table` | Input | Lookup Table | Yes | The lookup table to update. |
| `key` | Input | Real | Yes | The key to insert or replace. |
| `value` | Input | Real | Yes | The value to store under it. |
| `updatedTable` | Output | Lookup Table | — | The updated lookup table. |

```
sourceLookup := LookupTable [
    "Key" "Value",
    1 667137,
    2 39398,
    3 181045
];

emptyResults := Table [
    "CityId*#real", "DoubledPopulation#real"
];

_ := ForEach sourceLookup {{
    accumulated := MuxTable emptyResults nextAccumulated;

    key := Step;
    population := GetLookupTableValue sourceLookup key;
    doubled := $ [ $population * 2 ];

    newRow := AddTupleValue key doubled;
    nextAccumulated := AddTableRow accumulated newRow;
}};

// finalResults holds every row added across all iterations. Use nextAccumulated,
// not accumulated (the mux's own output), which lags one iteration behind.
// The Table carrier passes it through, since := always binds a functor call.
finalResults := Table nextAccumulated;
```

> **Note:** This is also a reason to avoid reading `accumulated` anywhere else in the same iteration, beyond its use in `AddTableRow`. The engine schedules operations to minimize copying: when a value only needs to be read before it's destructively updated, the reads are scheduled first and the update last, avoiding a copy entirely. But if two or more functors both need to destructively update the same value, no scheduling avoids a copy for all of them — only one destructive update can safely be the last one to run. See [Basic Data Flow](Basic-Data-Flow.html#destructive-updates) for this same rule stated generally, beyond just tables.

**Why this isn't the best approach.** The mux above disqualifies this loop from the parallel execution described earlier — it's what ties every iteration to the one before it, forcing the loop to run sequentially even though the per-iteration work is otherwise completely independent (each row's value depends only on that row's own key).

When the transformation is this simple — one output row per input row, computed independently — the calculator shorthand already covered in [Lookup Table Operators](Calculate-Functors.html#5-lookup-table-operators) produces the same result without a loop, a mux, or the sequential cost that comes with one:

```
doubledResults := % [ %sourceLookup[line] * 2 ] "CityId" "DoubledPopulation" sourceLookup;
```

One difference in shape: the loop accumulates into a Table, since `emptyResults` was declared as one, while `%` always returns a Lookup Table. Where the Table form is the one wanted, a `Table` carrier converts it — `asTable := Table doubledResults` — one Real key and one Real value fitting both types equally well.

## Table Manager

The accumulator pattern in [Storing results across a loop](#storing-results-across-a-loop) uses a Mux to carry a growing table from one iteration to the next -- which, as that section's closing note explains, forces the loop to run sequentially, one iteration at a time. **Table Manager** solves the same class of problem -- building a table with an extra key column from results computed across a loop -- without that cost: each iteration registers its own sub-table independently, with no Mux and nothing threaded between iterations, so the loop producing those partial results stays eligible to run in parallel, per [Basic Data Flow](Basic-Data-Flow.html). A single [MergeSubTables](#mergesubtables) call combines everything afterward.

A container and two functors do the core work; a fourth covers a narrower case:

### TableManager

A container functor. It creates the manager instance and exposes it to whatever runs inside it.

| Port | Direction | Type | Description |
| --- | --- | --- | --- |
| `tableManager` | Internal Output | TableManager | The manager instance. Auto-binds to the `tableManager` input of [SubTable](#subtable) and [MergeSubTables](#mergesubtables) calls nested anywhere inside this container, including inside further nested containers such as a [For](functors/For.html) loop or a [Group](functors/Group.html). |

The container itself takes no inputs and defines no regular outputs.

### SubTable

Registers one sub-table under a name and a key.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `tableName` | Input | Name | Yes | Identifies which set of sub-tables this one joins. |
| `keys` | Input | Tuple | Yes | The key identifying this sub-table within the set. |
| `subTable` | Input | Table | Yes | The sub-table itself. |
| `emptySubTableIsAllowed` | Input | Boolean | No | Whether an empty sub-table is accepted rather than raising an error. Default `.yes`. |
| `tableManager` | Input | TableManager | Yes | Auto-binds to the enclosing [TableManager](#table-manager) container; normally left unconnected. |
| `object` | Output | Table | -- | The same sub-table passed in, returned unchanged so it can still be referenced or connected onward. |

Every `SubTable` call sharing a `tableName` is checked against the first one registered under that name: the `keys` tuple must have the same element types, and `subTable` must have the same columns. A mismatch, or registering the same `keys` twice under the same `tableName`, raises an error.

### MergeSubTables

Combines every sub-table registered under a name into a base table, then discards them from the manager.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `baseTable` | Input | Table | Yes | The table the combined sub-tables are inserted into. |
| `tableName` | Input | Name | Yes | Which set of sub-tables to merge. |
| `allowNamesWithNoAssociatedSubTables` | Input | Boolean | No | If `.no`, merging a name nothing was ever registered under raises an error; if `.yes`, it's silently skipped. Default `.no`. |
| `tableManager` | Input | TableManager | Yes | Auto-binds to the enclosing [TableManager](#table-manager) container. |
| `table` | Output | Table | -- | `baseTable` with every sub-table registered under `tableName` inserted, each keyed by the Tuple it was registered with. |

Each sub-table's `keys` tuple can hold more than one element; every element becomes its own leading key column on `baseTable`. A `tableName` can only be merged once -- the merge removes its sub-tables from the manager as it runs.

> **Warning:** `MergeSubTables` has no data dependency on the `SubTable` calls that feed it -- its `baseTable` input, its literal `tableName`, and its auto-bound manager are all available from the moment the container starts, and none of them depend on the loop that registered the sub-tables. Placing it after a loop in the script, even inside the same `TableManager` container, does **not** guarantee it runs after that loop finishes; the two have no connection, so the engine is free to run them in either order or at the same time. Force the ordering explicitly with a [Group](functors/Group.html) gated by the loop's `sequenceOutput`, as in the example below -- see [Ordering without data: sequence connections](Basic-Data-Flow.html#ordering-without-data-sequence-connections) and [Sequence ports](EGO-Script.html#sequence-ports).

### TableManagerValue

An explicit pass-through for a TableManager instance, for the rare case where auto-bind doesn't reach -- for instance, threading a manager through a submodel boundary as a named port rather than relying on ambient container nesting. Within a single model, auto-bind on `SubTable` and `MergeSubTables` makes this unnecessary.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `tableManager` | Input | TableManager | No | Auto-binds to the enclosing [TableManager](#table-manager) container. |
| `tableManager` | Output | TableManager | -- | The same instance, under an explicit name. |

### Example

Building a two-key table from per-year sub-tables computed inside a loop, with the merge correctly sequenced after the loop:

```
emptyPriceTable := Table [ "Year*#real", "City*#string", "Price#real" ];

TableManager {{
    // forDone carries no data of its own; it exists purely so the Group
    // below can force itself to wait for every iteration of this loop.
    forDone := For 2004 2007 {{
        year := Step;

        // Stand-in for a per-year computation; in practice this might come
        // from a database query, a Calculate Table Values call, or another
        // model entirely. A Table literal only accepts literal cell values,
        // so a real per-year computation would build this row by row with
        // AddTupleValue and AddTableRow instead, the same as any table
        // whose contents aren't known until the model runs.
        yearPrices := Table [
            "City*", "Price",
            "Boston", 4000,
            "Chelsea", 200
        ];

        _ := SubTable "prices" year yearPrices;
    }};

    // Group's sequenceInput, fed from the loop's sequenceOutput, forces
    // this Group -- and MergeSubTables inside it -- to wait for the whole
    // loop to finish, without threading a Mux through its iterations.
    _ := Group forDone {{
        priceTable := MergeSubTables emptyPriceTable "prices";
    }};
}};
```

`priceTable` is usable here, once the Group it was produced inside — and through its `sequenceInput`, the loop that Group was forced to wait for — has finished.

The loop's own iterations are still eligible to run in parallel with each other: nothing inside it is a Mux, nothing inside it is consumed from outside it, and it feeds no submodel output port -- see [Basic Data Flow](Basic-Data-Flow.html). Only the loop as a whole is sequenced against the merge, which is why this avoids the cost the Mux-accumulator pattern above pays on every single iteration.

> **Note:** `year` is passed to `SubTable` directly, not wrapped in brackets as `[year]`. Bracket syntax is for Tuple **literals**; a connected Real value converts to a one-element Tuple automatically on connection, the same pattern used by `GetTableFromKey` in [Sub-Tables](#sub-tables) above.

## Printing a table with a generic format

Every example so far assumes the reader already knows a table's shape — its column names and their types — since `GetTableValue` and `CreateString`'s hooks are each wired to one specific name and type at authoring time. Printing a table generically, with any number of columns of any mix of Real and String, needs a different approach: read each row as a Tuple, discover how many elements it has, and determine each element's type at runtime rather than assuming it.

[Get Table Row](functors/Get-Table-Row.html), [Get Tuple Size](functors/Get-Tuple-Size.html), and [Get Tuple Value](functors/Get-Tuple-Value.html) make the column-count side of this possible: a row read as a Tuple can be measured with `GetTupleSize`, and each of its elements retrieved by position, rather than by column name, with `GetTupleValue`. Each retrieved element has type `TableValue` — a generic type able to hold either a Real or a String.

[String](functors/String.html) and [Real Value](functors/Real-Value.html) each convert a `TableValue` the same conditional way: the conversion only succeeds if the `TableValue` actually holds that type, and raises an error otherwise — converting an already-typed, known `RealValue` or String, by contrast, never fails. Wrapping each attempt in its own [Skip On Error](functors/Skip-On-Error.html) turns that failure into "produced nothing" instead of aborting the model, so only the attempt that actually matches the `TableValue`'s real type ever produces a display string; the other attempt simply fails silently and produces nothing. A [String Junction](functors/String-Junction.html) then picks whichever one exists.

> **Note:** A junction always tries its first port before its second — see [Carrying and selecting values across iterations](EGO-Script.html#carrying-and-selecting-values-across-iterations) for this rule stated generally, since it applies identically to every Junction functor (`String`, `Table`, `Value`, `Lookup Table`, `Map`, `Categorical Map`, `Folder`). It makes no practical difference here, though: the two attempts below are mutually exclusive by construction, so only one of `stringDisplay`/`realDisplay` is ever available for the junction to pick regardless of port order.

```
myTable := Table [
    "CityId*", "CityName", "Population",
    1, "Boston", 667137,
    2, "Chelsea", 39398
];

allKeys := GetTableKeys myTable;

LogPolicy { maximumLogLevel = .result } {{
    _ := ForEach allKeys {{
        key := Step;
        row := GetTableRow key myTable;
        rowSize := GetTupleSize row;

        // row[1] is the key itself; the actual value columns start at
        // index 2, so the loop skips index 1.
        _ := For 2 rowSize {{
            columnIndex := Step;
            cellValue := GetTupleValue columnIndex row;
            // Displayed as a 1-based value-column number, not the raw
            // Tuple index, which is offset by the key at position 1.
            displayColumn := $ [ $columnIndex - 1 ];

            // Try the cell as a String; SkipOnError leaves stringDisplay
            // unproduced if cellValue is actually a Real, rather than
            // aborting the model.
            _ := SkipOnError .yes {{
                stringDisplay := String cellValue;
            }};

            // Try the cell as a Real instead; SkipOnError leaves
            // realDisplay unproduced if cellValue is actually a String.
            _ := SkipOnError .yes {{
                asReal := RealValue cellValue;
                realDisplay := String asReal;
            }};

            // Exactly one of the two attempts above ever succeeds;
            // StringJunction picks whichever one was produced.
            cellDisplay := StringJunction stringDisplay realDisplay;

            message := CreateString "(Key: <v1>, Column: <v2>, Value: <s1>)" {{
                NumberValue key 1;
                NumberValue displayColumn 2;
                NumberString cellDisplay 1;
            }};

            Print { initialMessage = message, logLevel = .result } {{ }};
        }};
    }};
}};
```

This generalizes the value side of printing — any number of columns, any mix of Real and String — but not the key side: `key := Step` used directly as `myTable`'s row key still assumes a single, Real-typed key column, the same assumption the basic iteration example earlier makes. A table with a *known, fixed* number of key columns can still use the techniques already covered in [Iterating over Table rows](#iterating-over-table-rows) and [Sub-Tables](#sub-tables) — mapping a String key's placeholder index back, or nesting one loop per key column. When the number of key columns isn't known in advance, see [Printing a table with any number of key columns](#printing-a-table-with-any-number-of-key-columns) below.

## Computing new columns for a table

A new column can be derived from an existing table's own data, one metric at a time. [Calculate Lookup Table Values](functors/Calculate-Lookup-Table-Values.html) evaluates an expression once per key of a base lookup table, producing a new Lookup Table keyed the same way — so each derived metric comes out as its own separate result — and a later expression can reference an earlier result directly, the same way it references any other connected table. A general Table cannot serve as that base, since the `baseLookupTable` port only accepts a Lookup Table; `GetTableKeys` supplies one, its index-to-key result already having the right shape. Its keys are the source table's own only while the first key column is Real-typed, so that index and key coincide; a String-typed key column would supply placeholder indices instead, as [Iterating over Table rows](#iterating-over-table-rows) describes. [Add Table Column](functors/Add-Table-Column.html) then merges each of those results back into the original table as a new column, one call per column, since each call only ever adds one.

### AddTableColumn

Adds one column to a table.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `table` | Input | Table | Yes | The table the column is added to. |
| `columnName` | Input | Name | Yes | The new column's name. |
| `columnType` | Input | cell type | Yes | The new column's cell type. |
| `columnIndex` | Input | index | No | Where to insert it. Zero, or an index past the last column, appends it; if the column already exists, its current index is kept. Default 0. |
| `columnShouldBeKey` | Input | Boolean | No | Meaningful only when the column lands after the last key column and before the first data column: whether it becomes a key column. Default `.no`. |
| `columnValues` | Input | Table | No | Initial values, as a table with the same key columns and types as `table` and exactly one data column; its column names are ignored. Must be omitted when the new column is a key column. If the column already exists, these values are merged in, overriding conflicts. Default `.none`. |
| `defaultValue` | Input | TableValue | No | Value for cells `columnValues` doesn't mention; 0 or an empty string is used if it isn't given. Setting it may cost performance. Default `.none`. |
| `result` | Output | Table | — | The table with the new column. |

```
stationData := Table [
    "StationId*", "Jan_mm", "Feb_mm", "Mar_mm", "Apr_mm", "May_mm", "Jun_mm", "Jul_mm", "Aug_mm", "Sep_mm", "Oct_mm", "Nov_mm", "Dec_mm",
    1,  85,  75,  95, 100,  90,  85,  80,  90,  95, 105, 110,  95,
    2,  90,  80, 100, 105,  95, 100,  95, 100, 105, 110, 115, 100,
    3, 100,  90, 105,  95,  85,  75,  70,  85,  95, 110, 120, 105,
    4,  75,  70,  90,  95, 100, 105, 100,  95,  90,  95,  90,  80,
    5,  95,  85, 100, 100,  90,  85,  85,  90,  90, 100, 105, 100,
    6, 110, 100, 105, 100,  90,  80,  75,  85,  90, 105, 115, 110
];

stationKeys := GetTableKeys stationData;

averages := % [
    ( %stationData[[line]["Jan_mm"]] + %stationData[[line]["Feb_mm"]] + %stationData[[line]["Mar_mm"]] +
      %stationData[[line]["Apr_mm"]] + %stationData[[line]["May_mm"]] + %stationData[[line]["Jun_mm"]] +
      %stationData[[line]["Jul_mm"]] + %stationData[[line]["Aug_mm"]] + %stationData[[line]["Sep_mm"]] +
      %stationData[[line]["Oct_mm"]] + %stationData[[line]["Nov_mm"]] + %stationData[[line]["Dec_mm"]] ) / 12
] "StationId" "Average_mm" stationKeys;

stdDevs := % [
    sqrt( (
        (%stationData[[line]["Jan_mm"]] - %averages[line])^2 +
        (%stationData[[line]["Feb_mm"]] - %averages[line])^2 +
        (%stationData[[line]["Mar_mm"]] - %averages[line])^2 +
        (%stationData[[line]["Apr_mm"]] - %averages[line])^2 +
        (%stationData[[line]["May_mm"]] - %averages[line])^2 +
        (%stationData[[line]["Jun_mm"]] - %averages[line])^2 +
        (%stationData[[line]["Jul_mm"]] - %averages[line])^2 +
        (%stationData[[line]["Aug_mm"]] - %averages[line])^2 +
        (%stationData[[line]["Sep_mm"]] - %averages[line])^2 +
        (%stationData[[line]["Oct_mm"]] - %averages[line])^2 +
        (%stationData[[line]["Nov_mm"]] - %averages[line])^2 +
        (%stationData[[line]["Dec_mm"]] - %averages[line])^2
    ) / 12 )
] "StationId" "StdDev_mm" stationKeys;

withAverage := AddTableColumn { table = stationData, columnName = "Average_mm", columnType = .real, columnValues = averages };
enrichedStationData := AddTableColumn { table = withAverage, columnName = "StdDev_mm", columnType = .real, columnValues = stdDevs };
```

`stdDevs` demonstrates the chaining directly: rather than re-deriving the twelve-term average a second time inside the deviation formula, `%averages[line]` looks up the already-computed mean for the current row, the same way `%stationData[[line]["Jan_mm"]]` looks up a raw monthly value — both are just references to a connected table, one newly derived and one original.

Each `AddTableColumn` call only adds a single column, so producing two new columns takes two calls, the second operating on the first's result — `withAverage` is a genuine intermediate table, not a byproduct to discard. `columnValues` expects a table with the same key column(s) as the target and exactly one data column; a Lookup Table's `*#real, #real` shape already matches that, converting the same way documented in [Automatic Conversions](types/Table-Type.html#automatic-conversions) on Table Type.

## Computing statistics for an arbitrary number of data columns

The previous section names every column explicitly in the expression — workable for twelve months, but it doesn't scale to a table with, say, one column per day of the year. When the number of data columns isn't known in advance, a loop reading each row generically — the same `GetTupleSize`/`GetTupleValue` technique already used for printing — can compute a per-row result instead. Four sections follow. Three of them — looping row by row, looping column by column, and, best of all when it's available, reorganizing the data so no loop is needed at all — are alternative ways to compute that same per-row result, roughly from most to least manual. The remaining one aggregates in the opposite direction instead: across rows rather than columns, one result per day rather than one per station.

### Looping row by row

Imagine a table shaped like the station data from before, but with one column per day instead of one per month. The code fragments that follow call it `dailyStationData`:

| StationId\* | Day_1 | Day_2 | Day_3 | ... | Day_365 |
| --- | --- | --- | --- | --- | --- |
| 1 | ... | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... | ... |
| ... |  |  |  |  |  |

`GetTableRow` reads an entire row as a Tuple — the key first, then every data column in order (see [GetTableRow](#gettablerow) above) — and `GetTupleSize` reports how many elements it has, so the loop bound adapts to however many day columns the table actually has.

```
allStationIds := GetTableKeys dailyStationData;

emptyAverages := LookupTable [ "Key" "Value" ];
emptyStdDevs := LookupTable [ "Key" "Value" ];

_ := ForEach allStationIds {{
    stationId := Step;
    row := GetTableRow stationId dailyStationData;
    rowSize := GetTupleSize row;
    // row[1] is the key itself; the actual day values start at index 2.
    dayCount := $ [ $rowSize - 1 ];

    // First pass: sum every day's value to compute the average.
    _ := For 2 rowSize {{
        dayIndex := Step;
        cellValue := GetTupleValue dayIndex row;
        dailyValue := RealValue cellValue;

        runningSum := MuxValue 0 nextRunningSum;
        nextRunningSum := $ [ $runningSum + $dailyValue ];
    }};

    average := $ [ $nextRunningSum / $dayCount ];

    // Second pass: sum the squared deviations from that average.
    _ := For 2 rowSize {{
        devDayIndex := Step;
        devCellValue := GetTupleValue devDayIndex row;
        devDailyValue := RealValue devCellValue;

        devRunningSum := MuxValue 0 nextDevRunningSum;
        nextDevRunningSum := $ [ $devRunningSum + ($devDailyValue - $average)^2 ];
    }};

    stdDev := $ [ sqrt( $nextDevRunningSum / $dayCount ) ];

    // Accumulate (StationId, average) and (StationId, stdDev) pairs into
    // two growing result tables, the same accumulator pattern as before.
    averagesAccum := MuxLookupTable emptyAverages nextAveragesAccum;
    nextAveragesAccum := SetLookupTableValue averagesAccum stationId average;

    stdDevsAccum := MuxLookupTable emptyStdDevs nextStdDevsAccum;
    nextStdDevsAccum := SetLookupTableValue stdDevsAccum stationId stdDev;
}};

averages := LookupTable nextAveragesAccum;
stdDevs := LookupTable nextStdDevsAccum;
```

Four muxes are threaded through this loop, at two nesting levels. Inside a station, two separate `MuxValue` passes sum that station's own daily values — one for the average, a second for the squared deviations from it, since the standard deviation formula needs the average already known before it can compute those deviations. Outside them, two `MuxLookupTable` accumulators carry the growing results across stations, one per statistic. [Set Lookup Table Value](functors/Set-Lookup-Table-Value.html) is what actually inserts each computed value into its growing table — the write counterpart to `GetLookupTableValue`. `RealValue cellValue` is used directly here, without the `SkipOnError` type test from the generic printer — this example assumes every data column is genuinely numeric, which is reasonable for daily measurements, unlike the printer, which had to handle either type. The second pass's variable names all carry a `dev` marker (`devDayIndex`, `devCellValue`, `devDailyValue`, `devRunningSum`, `nextDevRunningSum`) to keep them clearly distinct from the first pass's, even though each `For` loop is its own separate container.

### Looping column by column

The row-by-row approach above isn't the only way to handle an arbitrary number of data columns. `GetTableColumn` inverts the iteration: instead of looping over stations and, within each one, over days, this loops over days, and for each one pulls that entire day's values — every station at once — as a table shaped `(StationId → that day's value)`. `%` then folds each day into a running per-station total, one call per day, rather than a mux-driven inner sum.

```
allStationIds := GetTableKeys dailyStationData;
firstStationId := GetTableValue allStationIds [1] 2;
sampleRow := GetTableRow firstStationId dailyStationData;
sampleRowSize := GetTupleSize sampleRow;
dayCount := $ [ $sampleRowSize - 1 ];

initialSums := % [ 0 ] "StationId" "Sum" allStationIds;

// First pass: sum every day's column, per station, to compute the average.
_ := For 1 dayCount {{
    dayNumber := Step;
    // dailyStationData's columns are StationId (index 1), then each
    // day in order, so day N sits at raw column index N + 1.
    rawColumnIndex := $ [ $dayNumber + 1 ];
    dayColumn := GetTableColumn dailyStationData rawColumnIndex;

    runningSums := MuxLookupTable initialSums nextRunningSums;
    // Adds this day's value for each station to that station's
    // running total, computed for every station in one call. The [2]
    // names dayColumn's single data column explicitly; it can be left
    // out — [[line]] alone reads the first data column by default.
    nextRunningSums := % [ column + %dayColumn[[line][2]] ] "StationId" "Sum" runningSums;
}};

sums := LookupTable nextRunningSums;
averages := % [ %sums[line] / $dayCount ] "StationId" "Average_mm" sums;

initialSquaredDevSums := % [ 0 ] "StationId" "SquaredDevSum" allStationIds;

// Second pass: sum the squared deviations from each station's own average,
// now that it's known.
_ := For 1 dayCount {{
    devDayNumber := Step;
    devRawColumnIndex := $ [ $devDayNumber + 1 ];
    devDayColumn := GetTableColumn dailyStationData devRawColumnIndex;

    devRunningSums := MuxLookupTable initialSquaredDevSums nextDevRunningSums;
    nextDevRunningSums := % [ column + (%devDayColumn[[line][2]] - %averages[line])^2 ] "StationId" "SquaredDevSum" devRunningSums;
}};

squaredDevSums := LookupTable nextDevRunningSums;
stdDevs := % [ sqrt( %squaredDevSums[line] / $dayCount ) ] "StationId" "StdDev_mm" squaredDevSums;
```

`firstStationId` picks an arbitrary station just to measure the row shape once, the same `GetTableRow`/`GetTupleSize` technique as above, minus 1 for the key — every row has the same number of columns, so any one station works. `initialSums` starts every station at zero via a single-call `%`, evaluated once per key of `allStationIds` — the base lookup table supplying the station keys — with no other operand referenced. Inside the first loop, `%dayColumn[[line][2]]` reads the current day's value for the row currently being computed — the multi-column operator, since `dayColumn` is a Table, not a Lookup Table — while `column` reads that same row's running total from `runningSums`, the base table the whole expression is evaluated against. Converting first is possible — `LookupTable dayColumn` — and the Lookup Table operator is cheaper per query, but the conversion walks the whole column before any query happens; for a table consulted once per pass, as here, that up-front cost can outweigh what it saves.

The second loop repeats this shape for the sum of squared deviations, referencing `%averages[line]` — the already-computed per-station mean from the first loop, looked up by key — the same chaining technique already established in [Computing new columns for a table](#computing-new-columns-for-a-table). Its variables all carry a `dev` marker (`devDayNumber`, `devRawColumnIndex`, `devDayColumn`, `devRunningSums`, `nextDevRunningSums`) to keep them clearly distinct from the first loop's, even though each `For` loop is its own separate container. Two muxes thread through this version instead of the four the row-by-row approach needed — one `MuxLookupTable` carrying the running sums day to day, a second carrying the running squared-deviation sums — and both sit at the same level; there's still no inner mux within either pass, since `%` handles summing across all stations for a given day in one call rather than needing an accumulator of its own.

### Aggregating across rows instead of columns

The two techniques above both compute one result per station, aggregating across days. The opposite direction — one result per day, aggregating across stations — needs a different pair of functors: [Get Table Column](functors/Get-Table-Column.html) still extracts one day's values, but instead of folding them together with `%`, [Extract Lookup Table Attributes](functors/Extract-Lookup-Table-Attributes.html) computes summary statistics over an entire Lookup Table directly, including `meanValue` — the mean of the values themselves, exactly the average across stations this needs. `valueStd` is the matching standard deviation, taken over the population of values in the lookup table, so it divides by the number of entries rather than one less — the same convention as the hand-written formulas earlier on this page, and the two therefore agree.

Its result is a Lookup Table like any other — a Real key for each attribute (see the port table below), a Real value holding that attribute's figure. The names such as `"meanValue"` are labels for those keys, not a key type of their own; the `tX["NAME"]` operator, one of the [Lookup Table Operators](Calculate-Functors.html#5-lookup-table-operators), is what lets an expression address a key by its name instead of its number, resolving one to the other at evaluation time. No conversion or carrier is needed either way — `attrs` connects to it exactly as any Lookup Table would.

#### ExtractLookupTableAttributes

Computes summary statistics over an entire Lookup Table.

| Port | Direction | Type | Required? | Description |
| --- | --- | --- | --- | --- |
| `table` | Input | Lookup Table | Yes | The lookup table to summarise. |
| `extractStatisticalKeyAttributes` | Input | Boolean | No | Include the key statistics: `minKey`, `maxKey`, `meanKey`, `modeKey`, `keyVar`, `keyStd`, `medianKey`. Each key/value pair's value counts as that key's number of occurrences. Default `.yes`. |
| `extractStatisticalValueAttributes` | Input | Boolean | No | Include the value statistics: `minValue`, `maxValue`, `meanValue`, `modeValue`, `valueVar`, `valueStd`, `medianValue`. These summarise the values alone; the keys play no part in them. Default `.yes`. |
| `extractDynamicKeyValueAttributes` | Input | Boolean | No | Include the sums: `keySum`, `valueSum`, `keyValueProdSum`. Default `.yes`. |
| `attributes` | Output | Lookup Table | — | The calculated attributes, keyed by the numeric code of each attribute — `1` for `uniqueKeys` (always present), `10`-`16` for the key statistics, `20`-`26` for the value statistics, `30`-`32` for the sums. The `tX["NAME"]` operator (see above) is the normal way to read a specific one by its name instead of its code. |

**Example** — the average and standard deviation across all stations for a single day:

```
oneDayColumn := GetTableColumn dailyStationData 2;

attrs := ExtractLookupTableAttributes { table = oneDayColumn, extractStatisticalKeyAttributes = .no, extractDynamicKeyValueAttributes = .no };
averageAcrossStations := $ [ %attrs["meanValue"] ];
stdDevAcrossStations := $ [ %attrs["valueStd"] ];

message := CreateString "(Average across stations for Day 1: <v1>, StdDev: <v2>)" {{
    NumberValue averageAcrossStations 1;
    NumberValue stdDevAcrossStations 2;
}};

LogPolicy { maximumLogLevel = .result } {{
    Print { initialMessage = message, logLevel = .result } {{ }};
}};
```

**Example** — the same computation repeated for every day, building a `(Day → average across stations)` result:

```
allStationIds := GetTableKeys dailyStationData;
firstStationId := GetTableValue allStationIds [1] 2;
sampleRow := GetTableRow firstStationId dailyStationData;
sampleRowSize := GetTupleSize sampleRow;
dayCount := $ [ $sampleRowSize - 1 ];

emptyDayAverages := LookupTable [ "Key" "Value" ];
emptyDayStdDevs := LookupTable [ "Key" "Value" ];

_ := For 1 dayCount {{
    dayNumber := Step;
    // dailyStationData's columns are StationId (index 1), then each
    // day in order, so day N sits at raw column index N + 1.
    rawColumnIndex := $ [ $dayNumber + 1 ];
    dayColumn := GetTableColumn dailyStationData rawColumnIndex;

    attrs := ExtractLookupTableAttributes { table = dayColumn, extractStatisticalKeyAttributes = .no, extractDynamicKeyValueAttributes = .no };
    averageAcrossStations := $ [ %attrs["meanValue"] ];
    stdDevAcrossStations := $ [ %attrs["valueStd"] ];

    dayAveragesAccum := MuxLookupTable emptyDayAverages nextDayAveragesAccum;
    nextDayAveragesAccum := SetLookupTableValue dayAveragesAccum dayNumber averageAcrossStations;

    dayStdDevsAccum := MuxLookupTable emptyDayStdDevs nextDayStdDevsAccum;
    nextDayStdDevsAccum := SetLookupTableValue dayStdDevsAccum dayNumber stdDevAcrossStations;
}};

dayAverages := LookupTable nextDayAveragesAccum;
dayStdDevs := LookupTable nextDayStdDevsAccum;
```

`ExtractLookupTableAttributes` only needs `extractStatisticalValueAttributes` here — the other two attribute groups are switched off, since both `meanValue` and `valueStd` come from that one group. Two accumulators thread through the loop instead of one, `MuxLookupTable` carrying each day-by-day result separately — the average across stations and its standard deviation both still come from the same single `ExtractLookupTableAttributes` call, though, not a second pass over the data.

### An alternative organization: long format

The wide format used throughout the examples above — one row per station, one column per day — isn't the only way to organize this data. A long format instead uses one row per (station, day) combination, with two key columns instead of one. The fragments in this section call it `longFormatData`:

| StationId\* | Day\* | Precipitation_mm |
| --- | --- | --- |
| 1 | 1 | ... |
| 1 | 2 | ... |
| ... | ... | ... |
| 6 | 365 | ... |

This trades a wide table for a longer, denser one — but it also means every aggregate computed with a loop above can instead be reached directly with `GetTableFromKey` and `ExtractLookupTableAttributes`, no loop at all: peeling off one key, the same technique from [Sub-Tables](#sub-tables), leaves a sub-table already shaped like a Lookup Table, ready for a single `ExtractLookupTableAttributes` call.

**Example** — the average and standard deviation across days for a single station:

```
stationSubTable := GetTableFromKey longFormatData [1];

attrs := ExtractLookupTableAttributes { table = stationSubTable, extractStatisticalKeyAttributes = .no, extractDynamicKeyValueAttributes = .no };
averageForStation := $ [ %attrs["meanValue"] ];
stdDevForStation := $ [ %attrs["valueStd"] ];

message := CreateString "(Average across days for Station 1: <v1>, StdDev: <v2>)" {{
    NumberValue averageForStation 1;
    NumberValue stdDevForStation 2;
}};

LogPolicy { maximumLogLevel = .result } {{
    Print { initialMessage = message, logLevel = .result } {{ }};
}};
```

**Example** — the average across stations for a single day. `Day` isn't leftmost, so `ReorderTableColumn` moves it there first, the same technique from Sub-Tables:

```
longFormatDataByDay := ReorderTableColumn longFormatData "Day" 1;

daySubTable := GetTableFromKey longFormatDataByDay [1];

attrs := ExtractLookupTableAttributes { table = daySubTable, extractStatisticalKeyAttributes = .no, extractDynamicKeyValueAttributes = .no };
averageForDay := $ [ %attrs["meanValue"] ];
stdDevForDay := $ [ %attrs["valueStd"] ];

message := CreateString "(Average across stations for Day 1: <v1>, StdDev: <v2>)" {{
    NumberValue averageForDay 1;
    NumberValue stdDevForDay 2;
}};

LogPolicy { maximumLogLevel = .result } {{
    Print { initialMessage = message, logLevel = .result } {{ }};
}};
```

Unlike every example in the previous section, neither of these needs a loop or a mux — `GetTableFromKey` does the equivalent of what a whole `For` loop with `GetTableColumn` did before, in a single call. Neither `stationSubTable`/`daySubTable` going into `ExtractLookupTableAttributes`, nor `attrs` going into the `tX["NAME"]` operator right after, needs an explicit `LookupTable` carrier — the first is a direct connection between two ports, and the second reads straight from the Lookup Table that operator is built for.

This "no loop" advantage is specific to querying a single, known key. Computing the same statistic for **every** station, or **every** day, still needs a loop over that set of keys — though only one level of it, since each pass resolves its whole aggregate in a single `ExtractLookupTableAttributes` call, with no inner accumulator the way the wide-format loops needed one.

**Example** — the average across days, for every station:

```
allStationIds := GetTableKeys longFormatData;

emptyStationAverages := LookupTable [ "Key" "Value" ];
emptyStationStdDevs := LookupTable [ "Key" "Value" ];

_ := ForEach allStationIds {{
    stationId := Step;
    stationSubTable := GetTableFromKey longFormatData stationId;

    attrs := ExtractLookupTableAttributes { table = stationSubTable, extractStatisticalKeyAttributes = .no, extractDynamicKeyValueAttributes = .no };
    averageForStation := $ [ %attrs["meanValue"] ];
    stdDevForStation := $ [ %attrs["valueStd"] ];

    stationAveragesAccum := MuxLookupTable emptyStationAverages nextStationAveragesAccum;
    nextStationAveragesAccum := SetLookupTableValue stationAveragesAccum stationId averageForStation;

    stationStdDevsAccum := MuxLookupTable emptyStationStdDevs nextStationStdDevsAccum;
    nextStationStdDevsAccum := SetLookupTableValue stationStdDevsAccum stationId stdDevForStation;
}};

stationAverages := LookupTable nextStationAveragesAccum;
stationStdDevs := LookupTable nextStationStdDevsAccum;
```

**Example** — the average across stations, for every day:

```
longFormatDataByDay := ReorderTableColumn longFormatData "Day" 1;
allDayIds := GetTableKeys longFormatDataByDay;

emptyDayAverages := LookupTable [ "Key" "Value" ];
emptyDayStdDevs := LookupTable [ "Key" "Value" ];

_ := ForEach allDayIds {{
    day := Step;
    daySubTable := GetTableFromKey longFormatDataByDay day;

    attrs := ExtractLookupTableAttributes { table = daySubTable, extractStatisticalKeyAttributes = .no, extractDynamicKeyValueAttributes = .no };
    averageForDay := $ [ %attrs["meanValue"] ];
    stdDevForDay := $ [ %attrs["valueStd"] ];

    dayAveragesAccum := MuxLookupTable emptyDayAverages nextDayAveragesAccum;
    nextDayAveragesAccum := SetLookupTableValue dayAveragesAccum day averageForDay;

    dayStdDevsAccum := MuxLookupTable emptyDayStdDevs nextDayStdDevsAccum;
    nextDayStdDevsAccum := SetLookupTableValue dayStdDevsAccum day stdDevForDay;
}};

dayAverages := LookupTable nextDayAveragesAccum;
dayStdDevs := LookupTable nextDayStdDevsAccum;
```

Both follow the same shape as the single-key examples above, just wrapped in a `ForEach` over every key and accumulated with `MuxLookupTable` — one accumulator per statistic — the same accumulator pattern used throughout this page.

## Printing a table with any number of key columns

Long format, as above, is a good fit for computing a statistic — one row per key naturally supports "summarize everything for this key." It's a poor fit for a different goal: printing or otherwise working with a table's rows exactly as given, preserving its actual key structure, rather than reshaping it into something new. That's a harder problem: printing every row means iterating the first key's values, and for each of those, the second key's values, and so on, with a nesting depth that has to match however many key columns the table actually has. A model's graph is fixed before it runs, so there's no direct way to wire up "however many nested loops turn out to be needed" for an arbitrary table.

The practical way to solve this different goal is to reshape the table's *keys* instead of its rows, using a tool built for arbitrary shapes to begin with. [Calculate Python Expression](functors/Calculate-Python-Expression.html) can read a table with any number of key columns as a plain list of lists — see [Expression inputs](functors/Calculate-Python-Expression.html#expression-inputs) — regardless of how many of its columns are keys, since Python doesn't need to know that shape in advance the way EGO Script's connections do. Turning every original key column into a plain data column, and generating a single new sequential key to replace them, collapses the table down to the simple single-key shape the earlier examples on this page already handle.

```
myTable := Table [
    "Year*", "City*", "Product*", "Price",
    2004, "Boston", "Widget", 1200,
    2004, "Boston", "Gadget", 300,
    2004, "Chelsea", "Widget", 1453,
    2007, "Boston", "Widget", 4332,
    2007, "Chelsea", "Widget", 233,
    2007, "Chelsea", "Gadget", 87
];

result := CalculatePythonExpression $"(
inputTable = dinamica.inputs['t1']
header = inputTable[0]
rows = inputTable[1:]

# header holds plain column names only, so nothing needs stripping here.
# Every original column, key or not, becomes a plain data column; a single
# sequential integer becomes the new (and only) key.
newHeader = ['Id*'] + list(header)
newRows = [[i + 1] + list(row) for i, row in enumerate(rows)]
newTable = [newHeader] + newRows

dinamica.outputs['reshapedTable'] = dinamica.prepareTable(newTable, 1)
)" {{
    NumberTable myTable 1;
}};

reshapedTable := ExtractStructTable result "reshapedTable";

allIds := GetTableKeys reshapedTable;

LogPolicy { maximumLogLevel = .result } {{
    _ := ForEach allIds {{
        id := Step;
        row := GetTableRow id reshapedTable;
        rowSize := GetTupleSize row;

        // row[1] is the key itself; the actual value columns start at
        // index 2, so the loop skips index 1.
        _ := For 2 rowSize {{
            columnIndex := Step;
            cellValue := GetTupleValue columnIndex row;
            displayColumn := $ [ $columnIndex - 1 ];

            // Same generic Real/String printing technique as the earlier
            // example: try both conversions independently, each guarded by
            // its own SkipOnError, and let StringJunction pick whichever
            // one was actually produced.
            _ := SkipOnError .yes {{
                stringDisplay := String cellValue;
            }};

            _ := SkipOnError .yes {{
                asReal := RealValue cellValue;
                realDisplay := String asReal;
            }};

            cellDisplay := StringJunction stringDisplay realDisplay;

            message := CreateString "(Key: <v1>, Column: <v2>, Value: <s1>)" {{
                NumberValue id 1;
                NumberValue displayColumn 2;
                NumberString cellDisplay 1;
            }};

            Print { initialMessage = message, logLevel = .result } {{ }};
        }};
    }};
}};
```

`dinamica.inputs` passes column names alone — no `*` key markers and no `#type` annotations — so the Python side has nothing to strip, and no way to tell which of the original columns were keys. Losing that distinction costs nothing here, since the reshape turns every original column into a plain data column regardless. The outgoing header marks `Id` instead, and `prepareTable`'s second argument declares that one column as the key. Everything after the Python call is the same single-key iteration and generic value-printing already established — nothing about it needs to know how many keys the original table had.

## Choosing between Tables and Lookup Tables

A Lookup Table's fixed shape — one Real key, one Real value — makes it faster to query and iterate than a general Table, and it supports proximity-based lookups (nearest key, linear interpolation) that Tables don't. Prefer a Lookup Table whenever the data actually fits that shape, including inside map/value expressions, where Lookup Table operands add less evaluation overhead than Table operands — see [Lookup Table Operators](Calculate-Functors.html#5-lookup-table-operators) and [Multi-Column Table Operators](Calculate-Functors.html#6-multi-column-table-operators) for how each is queried from within an expression.

Reach for a general Table instead when a single Real value per Real key isn't enough — when a row needs more than one associated value, or a String value, or a String key, or when rows need to be indexed by more than one key at once. A String key column costs more than the type change alone: iterating one means mapping each placeholder index back to its actual key inside the loop, so prefer a Real key column wherever the data allows.
{% endraw %}
