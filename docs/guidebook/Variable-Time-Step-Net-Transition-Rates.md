---
title: "Calculate variable time-step net transition rates"
parent: "Module VIII: Additional applications"
grand_parent: "Guidebook"
nav_order: 8
---
{% raw %}
# Calculate variable time-step net transition rates

Here we provide an example of a model that can be used to run multiple time step simulations when the time-period matrix cannot be decomposed to a multiple-step transition matrix because it is not an ergodic matrix, i.e. [Markov chain matrix](https://en.wikipedia.org/wiki/Markov_chain).

For matrices that cannot be decomposed into multiple-step transition matrices, this models calculates first gross transition rates for a time-period and a specified time-step and then derives variable net transition rates, producing, as a result, a unique transition matrix for each model iteration. Output transition matrices are saved into files that can be loaded in a simulation with the same number of time-steps.

![](../image/guidebook_model3.jpg)

**To download this model and another one that runs the simulation using the multiple step transition matrices, please access:**

[http://csr.ufmg.br/~britaldo/simulate_2003_in_annual_time_steps.zip](http://csr.ufmg.br/~britaldo/simulate_2003_in_annual_time_steps.zip)

To work properly, these models' subfolder must be placed under the folder:

\Examples\run_urban_dynamics_of_savassi_bh (This is an example provided with Dinamica EGO installation)

--- *[Britaldo Soares Filho](mailto:britaldo@csr.ufmg.br) 2011/03/11 13:16*
{% endraw %}
