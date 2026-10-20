---
title: "Map Metadata"
nav_order: 5
parent: "Modeling Guides"
---
{% raw %}
# Map Metadata

A [Save Map](functors/Save-Map.html) functor can write a metadata file next to each map it saves. Metadata generation is turned on in the functor editor of Save Map, on its *Metadata* tab. Once enabled, every map written by that functor gets its own metadata file.

The metadata file is produced from a template: each keyword (tag) in the template is replaced by a value supplied by the user, by the map itself, or by the system. The metadata file name is the map file name with its extension replaced by the metadata file extension.

When a model runs from the command line, the template and the extension are chosen with the metadata options of [Dinamica Console](Dinamica-Console.html#metadata).

## Template Keywords

The **Source** column tells where each value comes from: **User** values are typed in the Save Map editor, **Map** values are read from the saved map, and **System** values come from the date of the run.

| Keyword | Description | Source |
| --- | --- | --- |
| `%TITLE%` | Title of the map. | User |
| `%DESCRIPTION%` | Description of the map. | User |
| `%SOURCE%` | Source or project originating the map. | User |
| `%CITATION%` | Citation instructing how to cite the map in a scientific publication. | User |
| `%ORIGINAL_SCALE%` | Original scale of the data from where the map was produced. | User |
| `%ADDITIONAL_CATEGORY_INFORMATION%` | Additional information about the categories. Used typically to describe the null value. | User |
| `%PUBLISHERS%` | Publisher of the map. | User |
| `%NUMBER_OF_COLUMNS%` | Number of columns of the map. | Map |
| `%NUMBER_OF_LINES%` | Number of lines of the map. | Map |
| `%CELL_HEIGHT%` | Height of the cells of the map. The height unit is projection dependent. | Map |
| `%CELL_HEIGHT_IN_METERS%` | Height of the cells of the map in meters. | Map |
| `%CELL_WIDTH%` | Width of the cells of the map. The width unit is projection dependent. | Map |
| `%CELL_WIDTH_IN_METERS%` | Width of the cells of the map in meters. | Map |
| `%NUMBER_OF_LAYERS%` | Number of layers/bands of the map. | Map |
| `%NULL_VALUE%` | Value representing the null value (no data) of the map. | Map |
| `%CELL_TYPE%` | Text representing the type of the cell of the map. | Map |
| `%CELL_TYPE_CODE%` | Code representing the type of the cell of the map. See [Cell Type](types/Cell-Type.html). | Map |
| `%CREATION_YEAR%` | Map creation year. | System |
| `%PROJECTION_WKT%` | Map projection represented as a WKT string. | Map |
| `%CATEGORIES%` | List of map categories, if any. Each category is represented by its cell value and name. | Map |
| `%LAYER_RANGES%` | List of map layers and their corresponding minimum and maximum cell values. | Map |
| `%CREATION_DATE%` | Map creation date. | System |
| `%SOURCE_MODEL_FILE%` | Name of the model script file responsible for the generation of the map. | Map |

## Template Example

The template below is available as the template option named "CSR / UFMG (pt-BR)".

```
[IDENTIFICATION]
title = '%TITLE%'
description = '%DESCRIPTION%

Number of Columns : %NUMBER_OF_COLUMNS%
Number of Lines : %NUMBER_OF_LINES%
Cell Height : %CELL_HEIGHT%
Cell Width : %CELL_WIDTH%
Layers : %NUMBER_OF_LAYERS%
Null Value : %NULL_VALUE%
Cell Type : %CELL_TYPE%
Model File : %SOURCE_MODEL_FILE%'
source = '%SOURCE%'
citation = '%CITATION%'
original scale = '%ORIGINAL_SCALE%'
thematic category = 'planning (015)'

[SPATIAL REPRESENTATION SYSTEM]
creation date = %CREATION_YEAR%
original format = 'raster (002)'
coordinate system representation = '%PROJECTION_WKT%'

[CATEGORIES]
additional information = '%ADDITIONAL_CATEGORY_INFORMATION%'
%CATEGORIES%

[RANGE]
%LAYER_RANGES%

[METAMETADATA]
updated = '%CREATION_DATE%'
publishers = '%PUBLISHERS%'
```

## Expanded Metadata File

A possible expansion of a metadata template for a saved map:

```
[IDENTIFICATION]
title = 'Uso da terra no Brasil simulado pelo OTIMIZAGRO para 2030'
description = 'OTIMIZAGRO modela nove cultivos temporários: 1) soja, 2) cana-de-açúcar, 3) milho, 4) algodão, 5) trigo, 6) feijão, 7) arroz, 8) mandioca e 9) fumo e cinco permanentes: 10) café arábica, 11) café robusta, 12) laranja, 13) cacau e 14) banana. Culturas de inverno ou safrinha incluem: 15) trigo, 16) feijão e 17) milho. Transições de desmatamento nos vários biomas e regeneração florestal também são modeladas. 

Number of Columns : 8533
Cell Height : 500.0
Cell Width : 500.0
Number of Layers : 1
Null Cell Value : 0.0
Number of Lines : 8765
Cell Type : Byte
Model File : C:/models/otimizagro.egoml'
source = 'Centro de Sensoriamento Remoto - CSR/UFMG (2015)'
citation = 'Soares-Filho BS (2015) Otimizagro model, Brasil: IGC/UFMG. Available at: <http://csr.ufmg.br/dinamica>'
original scale = 'Não informada'
thematic category = 'planejamentoECadastro (015)'

[SPATIAL REPRESENTATION SYSTEM]
creation date = 2015
original format = 'matricial (002)'
coordinate system representation = 'PROJCS["South_America_Albers_Equal_Area_Conic_MC51W",
    GEOGCS["GCS_South_American_1969",
        DATUM["unknown",
            SPHEROID["unnamed",6378160,298.249999999996]],
        PRIMEM["Greenwich",0],
        UNIT["degree",0.0174532925199433]],
    PROJECTION["Albers_Conic_Equal_Area"],
    PARAMETER["standard_parallel_1",-5],
    PARAMETER["standard_parallel_2",-42],
    PARAMETER["latitude_of_center",-32],
    PARAMETER["longitude_of_center",-51],
    PARAMETER["false_easting",0],
    PARAMETER["false_northing",0],
    UNIT["metre",1]]'

[CATEGORIES]
additional information = ''
24 = 'fumo'
25 = 'milho_2s'
26 = 'feijao_2s'
20 = 'laranja'
21 = 'mandioca'
22 = 'banana'
23 = 'cacau'
40 = 'feijao_feijao'
1 = 'agua'
3 = 'pastagem'
2 = 'urbano'
5 = 'savanas'
4 = 'pastagem_em_AP'
7 = 'florestas'
6 = 'savanas_em_AP'
9 = 'restauro'
8 = 'florestas_em_AP'
39 = 'milho_feijao'
38 = 'soja_feijao'
11 = 'soja'
13 = 'milho'
12 = 'cana_de_acucar'
15 = 'arroz'
14 = 'algodao'
17 = 'feijao'
16 = 'trigo'
19 = 'cafe_robusta'
18 = 'cafe_arabica'
30 = 'floresta_plantada'
37 = 'milho_trigo'
36 = 'soja_trigo'

[RANGE]
layer_0 = '(Min=1.0,Max=40.0)'

[METAMETADATA]
updated = '2015/04/23'
publishers = 'Centro de Sensoriamento Remoto - CSR/UFMG'
```
{% endraw %}
