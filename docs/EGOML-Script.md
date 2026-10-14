---
title: "EGOML Script"
nav_order: 2
parent: "Language and Expressions"
---
{% raw %}
# EGOML Script

## Overview

Any model can be saved as an EGOML document. The resulting file uses the extension ".egoml" (the old extension ".xml" is still supported for backward compatibility). See [Basic Data Flow](Basic-Data-Flow.html) for the execution model shared by EGOML and [EGO Script](EGO-Script.html); this page covers the XML notation specifically.

The EGOML file is an XML document written according to the following DTD; see [w3schools' DTD tutorial](https://www.w3schools.com/xml/xml_dtd_intro.asp) for a good introduction to the DTD description syntax:

```xml
<?xml version="1.0"?>
<!DOCTYPE script [
  <!ELEMENT script (property*, functor*, containerfunctor*)>
 
  <!ELEMENT functor (property*, inputport*, outputport*)>
    <!ATTLIST functor
      name   CDATA  #REQUIRED>
 
  <!ELEMENT containerfunctor (property*, inputport*, outputport*, internalinputport*, internaloutputport*, (functor|containerfunctor)*)>
    <!ATTLIST containerfunctor
      name   CDATA  #REQUIRED>
 
  <!ELEMENT property EMPTY>
    <!ATTLIST property
      key  CDATA  #REQUIRED
      value  CDATA  #REQUIRED>
 
  <!ELEMENT inputport (#PCDATA)>
    <!ATTLIST inputport
      name   CDATA  #REQUIRED
      peerid IDREFS #IMPLIED>
  <!ELEMENT outputport EMPTY>
    <!ATTLIST outputport
      name   CDATA  #REQUIRED
      id   ID   #REQUIRED>
   <!ELEMENT internalinputport EMPTY>
    <!ATTLIST internalinputport
      name   CDATA  #REQUIRED
      peerid IDREFS #IMPLIED>
  <!ELEMENT internaloutputport EMPTY>
    <!ATTLIST internaloutputport
      name   CDATA  #REQUIRED
      id   ID   #REQUIRED>
]>
```

## Elements

Each element in the DTD corresponds directly to a piece of the underlying functor graph described in [Basic Data Flow](Basic-Data-Flow.html):

- `script` is the model as a whole — the root element, holding the model's own properties plus every top-level functor and container.
- `functor` is a single functor call, identified by its `name` attribute (such as `LoadMap`). It holds its own properties, its input ports, and its output ports.
- `containerfunctor` is a functor that also holds nested functors and containers — the same element type can nest inside itself, since containers can be placed inside other containers.
- `property` attaches metadata to whatever element contains it, as a `key`/`value` pair. Keys are always written fully expanded — there is no property alias as in the [EGO Script](EGO-Script.html) format. See [Properties](EGO-Script.html#properties) for the catalog of recognized keys — what each one means, and which functors or model-level context they apply to.
- `inputport` and `outputport` are a functor's connection points. An `outputport` declares an `id`; an `inputport` elsewhere in the document references that `id` through its own `peerid` attribute to form a connection — the XML equivalent of two functors sharing a variable name in EGO Script. Forming a connection this way is exactly where automatic type conversion applies — see [Type System](Type-System.html) for the full set of types and how they convert into one another. An `inputport` element can be omitted entirely as long as the port it represents is optional, the same as omitting an optional port in EGO Script's [nominal syntax](EGO-Script.html#nominal-syntax); the port then takes its default value. A required port's `inputport` element can't be omitted this way.
- `internalinputport` and `internaloutputport` work the same way, but connect a container to the functors nested inside it, rather than connecting two ordinary functors to each other.

The DTD defines no equivalent of EGO Script's abbreviated calculator syntax. Every functor in the Calculate family — `CalculateMap`, `CalculateLookupTableValues`, and the others — is represented the same way as any other container: its operands are connected through explicit `NumberMap`/`NumberTable`/`NumberValue` hook functors, as shown in the `CalculateMap` example below. See [Calculator functor shorthand](EGO-Script.html#calculator-functor-shorthand) for the two syntactic forms EGO Script provides for this same underlying structure.

## Example

Below is an example of an EGOML script used to load a map, calculate an image convolution, and save the result:

```xml
<?xml version="1.0" standalone="yes" ?> 
<script>
  <property key="dff.charset" value="UTF-8" /> 
  <property key="dff.date" value="2026-Jul-21 14:32:07" /> 
  <property key="dff.version" value="8.12.0.20260626" /> 
  <property key="metadata.author" value="Dinamica EGO Team" /> 
  <property key="metadata.description" value="This is an example of map algebra expression written in Dinamica’s Calculate Map functor. This functor also performs contextual image operation, such as edge detection filters using nbConvol expression." /> 
  <property key="metadata.organization" value="CSR / UFMG" /> 
  <property key="metadata.showproperties" value="yes" /> 
  <property key="metadata.title" value="Apply Edge Detection Convolution Easier" /> 
  <functor name="LoadMap">
    <property key="dff.functor.alias" value="Input Map" /> 
    <inputport name="filename">"C:/Desenvolvimento/Centro-De-Sensoriamento-Remoto/lesson1/amazon_states.tif"</inputport> 
    <inputport name="nullValue">.none</inputport> 
    <inputport name="storageMode">.default</inputport> 
    <inputport name="suffixDigits">0</inputport> 
    <inputport name="firstWindowCoordinateX">.none</inputport> 
    <inputport name="firstWindowCoordinateY">.none</inputport> 
    <inputport name="secondWindowCoordinateX">.none</inputport> 
    <inputport name="secondWindowCoordinateY">.none</inputport> 
    <inputport name="step">.none</inputport> 
    <inputport name="workdir">.none</inputport> 
    <outputport name="map" id="v1" /> 
  </functor>
  <functor name="LookupTable">
    <inputport name="constant">[ "Key" "Value", 1 1 .. 4 1, 5 -8, 6 1 .. 9 1 ]</inputport> 
    <outputport name="object" id="v2" /> 
  </functor>
  <functor name="SaveMap">
    <inputport name="map" peerid="v3" /> 
    <inputport name="filename">"C:/Desenvolvimento/Centro-De-Sensoriamento-Remoto/dinamica/Release/output.ers"</inputport> 
    <inputport name="suffixDigits">0</inputport> 
    <inputport name="step">.none</inputport> 
    <inputport name="useCompression">.yes</inputport> 
    <inputport name="workdir">.none</inputport> 
    <inputport name="ignoreCostlySparseCategories">.yes</inputport> 
  </functor>
  <containerfunctor name="CalculateMap">
    <property key="dff.functor.alias" value="Edge Map" /> 
    <property key="dff.functor.comment" value="Image convolution in Dinamica EGO" /> 
    <inputport name="expression">[ nbConvol(i1, t1, 3, 3) ]</inputport> 
    <inputport name="cellType">.int32</inputport> 
    <inputport name="nullValue">0</inputport> 
    <inputport name="resultIsSparse">.no</inputport> 
    <inputport name="resultFormat">.none</inputport> 
    <outputport name="result" id="v3" /> 
    <functor name="NumberMap">
      <inputport name="map" peerid="v1" /> 
      <inputport name="mapNumber">1</inputport> 
    </functor>
    <functor name="NumberTable">
      <inputport name="table" peerid="v2" /> 
      <inputport name="tableNumber">1</inputport> 
    </functor>
  </containerfunctor>
</script>
```

The same model, expressed in EGO Script:

```
@charset = UTF-8
@date = 2026-Jul-21 14:32:07
@version = 8.12.0.20260626
@author = Dinamica EGO Team
@description = This is an example of map algebra expression written in Dinamica’s Calculate Map functor. This functor also performs contextual image operation, such as edge detection filters using nbConvol expression.
@organization = CSR / UFMG
@showproperties = yes
@title = Apply Edge Detection Convolution Easier
Script {{
    inputMap := LoadMap "C:/Desenvolvimento/Centro-De-Sensoriamento-Remoto/lesson1/amazon_states.tif" .none .default 0 .none .none .none .none .none .none;

    lookupTable0 := LookupTable [
        "Key" "Value",
        1 1 .. 4 1,
        5 -8,
        6 1 .. 9 1
    ];

    // Image convolution in Dinamica EGO
    edgeMap := # [
        nbConvol(#inputMap, %lookupTable0, 3, 3)
    ] .int32 0 .no .none;

    SaveMap edgeMap "C:/Desenvolvimento/Centro-De-Sensoriamento-Remoto/dinamica/Release/output.ers" 0 .none .yes .none .yes;
}};
```
{% endraw %}
