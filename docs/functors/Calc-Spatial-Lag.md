---
title: "Calc Spatial Lag"
nav_order: 4
parent: "Statistics Functors"
grand_parent: "Functor List"
redirect_from:
  - /Calc-Spatial-Lag.html
---
{% raw %}
# Calc Spatial Lag

## Description

Container that iteratively solves a spatial lag regression, y = pLag \* W \* y + X \* B + E, over independent variables registered inside it.

## Inputs

| Name | Type | Description |
| --- | --- | --- |
| P Lag | [Real Value Type](../types/Real-Value-Type.html) | Spatial autoregressive coefficient (p) used in the regression. |
| W Neighborhoods | [Neighborhood Table Type](../types/Neighborhood-Table-Type.html) | Spatial weight matrix (W) used in the regression. |
| X1 | [Lookup Table Type](../types/Lookup-Table-Type.html) | Values of the observed dependent variable (X1) for each region. When the observed result is not yet known, X1 stands in for it; in that case, supply a lookup table with the same number of records and every value set to zero. |
| B Coefficients | [Lookup Table Type](../types/Lookup-Table-Type.html) | Regression coefficients (B): the coefficient of the observed variable (index 0), followed by the coefficient of each independent variable registered in this container. |
| E Error | [Real Value Type](../types/Real-Value-Type.html) | Random error term (E) of the regression. |

## Optional Inputs

None.

## Outputs

| Name | Type | Description |  |  |
| --- | --- | --- | --- | --- |
| Y Result | [Lookup Table Type](../types/Lookup-Table-Type.html) | Result (y) of the equation y = pLag \* W \* y + X \* B + E, solved iteratively until convergence. |  |  |
| Y Predicted Result | [Lookup Table Type](../types/Lookup-Table-Type.html) | Predicted result (y | **) of the equation y** | **= pLag \* W \* X1 + X \* B + E.** |

## Group

[Statistics](../Functor-List.html#statistics)

## Notes

The independent variables (X) used in the regression are registered inside this container by functors representing a numbered table (Number Table), each identified by a sequential number starting at 1.

The number of coefficients supplied in B Coefficients must equal the number of independent variables registered in this container, plus one for the observed variable's own coefficient (index 0).

W represents the spatial interaction of a phenomenon: in a binary weight matrix, unit i is a neighbor of unit j when the corresponding matrix cell is 1.

**References**

ANSELIN, L. SpaceStat Tutorial. Urbana-Champaign, University of Illinois, 1992.

ANSELIN, L. Spatial Externalities, Spatial Multipliers and Spatial Econometrics. Urbana-Champaign, University of Illinois, 2002.

## Internal Name

CalcSpatialLag
{% endraw %}
