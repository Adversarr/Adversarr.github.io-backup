---
title: SPH Introduction
author: Clover
date: 2022/10/27 # yyyy-mm-dd
categories: Anything
tags:
  - Anything
plugins:
  - mathjax
group: group-cg-paper
sidebar: [group-cg-paper, toc]
---

1106 论文汇报

SPH Fluids in computer graphic

<!-- more -->

## Introduction

### Governing Equations

Consider fluid that consists of a set of small moving fluid elements(i.e. particles), and for each particle, it carries attributes:

1. Density $\rho _ i$
2. Pressure $p _ i$
3. volume $v _ i$

From Newton's second law:

$$
\frac{\mathrm d x _ i} {\mathrm d t} = v _ i 
$$

We use particles to describe the fluid flow, the time rate of change of the velocity is governed by the **Lagrange** view of NS Equation.

$$
\dot v _ i = -\frac 1 {\rho _ i} \nabla p _ i + v \nabla ^ 2 v _ i + \frac{F _ {ext}} {m _ i}
$$

1. Pressure
2. Friction force. $v$ -> kinematic viscosity.
3. External force, such as gravity.

### SPH

Idea: Interpolate the fluid quantities at arbitary positions and to approximate the spatial derivatives, **using a set of sample positions, i.e. adjacent particles** 

*Interpolation*: A quantity $A _ i$ at $x _ i$ is approximated using a weighted sum of neighbour particles:

$$
A _ i = \sum _ {j \in \mathcal N _ i} \frac{m _ j} { \rho _ j } A _ j W _ {ij}
$$

$W _ {ij}$ should be close to a Gaussian, amd can be implemented as:

1. Bell function
2. Quintic Spline -- $C^1$ continuity
3. Cubic Spline -- $C ^ 2$ continuity

*Spatial Derivatives*: Spatial derivatives can be derived:

$$
\begin{aligned}
\nabla A_i = \rho_i + \sum_{j} m_j  \left ( \frac { A _ i} { \rho _ i  ^ 2} + \frac{A _ j} {\rho _ j ^ 2}\right) \nabla W_ { i j }\\
\nabla \cdot \mathbf{A}_i = - \frac 1 { \rho _ i} \sum _ j m _ j \mathbf A _ {ij} \cdot \nabla W _ {ij} \\
\nabla ^ 2 A _ i = 2 \sum _ { j } \frac { m _ j} { \rho _ j} A _ {ij} \frac {\mathbf x _ {ij} \cdot \nabla W _ { ij }}{\mathbf x _ {ij} \cdot \mathbf x _ {ij} + 0.01 h ^ 2}
\end{aligned} 
$$

Here, $\rho$ is computed using:

$$
\rho_i  = \sum_j m_j W_{ij}
$$

> we always use $m / \rho$, and the meaning of $\rho$ here does not matter.

### The solver

Three basic steps:

1. Neighbourhood search
2. Pressure Computation
3. Time Integrations

Neighbourhood search can be solved using VDB or Spatial Ordering/Hashing methods. We focus on 2 and 3.

A typical choice is:

For *Pressure Computation*: 

$$
p_i = k \left( \left ( \frac{\rho_i}{\rho_0}\right) ^ 7 - 1 \right)
$$

where: 

- $\rho_0$ is the rest density.
- $k$ is the stiffness.

```
foreach Particle P:
  find neighbours.
foreach Particle P:
  compute density.
  compute pressure.
foreach Particle P:
  compute pressure force.
  compute viscosity force
  compute external force
  merge all the forces.

foreach Particle P:
  update velocity, position.
```

> **CFL Condition** should be considered carefully when using this method.

$$
\Delta t \le \lambda \frac{ h } { \| v _ {\max} \| }, \qquad \mathrm{with}~~\lambda \approx 0.4
$$

### Neightbourhood Search

*Time*: 
1. Grids: $O(n)$ build, $O(1)$ access
2. Hierarchy: $O(n log n)$ build, $O(log n)$ access.

*Memory*: Hierarchy < Grid.

1. *Iterative*: Reuse the structure frequently, and we can store the neighborhood set, and rebuild it from time to time.
2. *Non-Iterative*: 

#### Uniform Grid

1. Index Sort -> See GPU Gems 3
2. Z-index Sort -> latency, cache hit rate 

#### Hashing

1. hashing,
2. compact hasihing.

> To reduce the memory consumption of plain grid storaging method.
> 
> but it reduce the *cache-hit-rate* 

### GPUs

## Incompressibility

### Non Iterative EOS Solver

**EOS**: Describe the relation between $\rho$, $p$, and $T$(temperature).

Original:

$$
p = p (\rho , T) = \frac{\mu}{R} \rho T
$$

Typically, for water:

$$
\rho = \rho _ 0
$$

Pressure penals the violation of the condition.

### Non Iterative EOS Solvers with Splitting

Split the:

1. Pressure Force
2. Non-Pressure Force

because:

$$
\frac { 1 } {\Delta t} (v(t + \Delta t) - v^ * (t) ) = - (1 / \rho ^ * _ i) \nabla p _ i
$$

```
foreach P: find neighbours
foreach P: compute Non-Pressure forces  -> Advection
foreach P: compute Pressure forces.     -> Projection, use data from Advection
foreach P: update velocity & position
```

### Iterative EOS Solvers with Splitting

Alternatively, *strong-incompressibility*.

```
foreach P: find neighbours
foreach P: compute Non-Pressure part.       -> Advection
repeat until convergence:                   -> Projection(weak)
  foreach P: compute density and pressure
  foreach P: update velocity and positions
```

e.g.:

1. PCISPH
2. LPSPH

### Pressure Projection

Solve a pressure poisson equation(PPE).

$$
\nabla ^ 2 p _ i = \frac {\rho _ 0} {\Delta t} \nabla \cdot v_i
$$

1. IISPH

```
foreach P: find neighbours
foreach P: compute Non-Pressure part.       -> Advection
foreach P: compute rho*
solve PPE                                   -> Projection
compute Pressure Force
update v, x
```

> As the overall computation time of all solvers largely depends on the obtained incompressibility, average or maximum density errors are considered to specify the simulation quality.

## Incompressibility -- Extra

In (EG 2022): There are only two categories:

1. weak-incompressible: incompressible is not enforced, only a *trend* is formulated. Pressure indicates incompressible.
  - Local Pressure Solver
2. strong-incompressible: incompressible PPE is solved.
  - Global Pressure Solver

In this sense: target of PCISPH = IISPH = PBF.

### IISPH

$$
\Delta t^2 \nabla^2 p_i = \rho^0 - (\rho_i - \Delta t \rho_i\nabla \cdot v_i^{*})
$$
step 1: compute the pressure accelerations:

$$
(a_i^P)^l = - \frac{1}{\rho_i} \nabla p_i^l
$$
step 2: compute density change
$$
\Delta \rho = \Delta t \sum_j m_j\Delta t(a_i^p - a_j^p)\Delta W_{ij}
$$
## Boundary Handling

Most methods: Extend the field attributes to the boundary.

### Particle-based Methods

Also sample the particle points on rigid/deformable bodies, compute the penalty force based on distance.

> The boundary particles serve as additional sampling points and typically have the same radius as the fluid particles.

$$
\rho_i = \rho_{\mathcal{F}} + \rho_{\mathcal{B}} \approx \sum_j m_j W_{ij} + \sum_k \tilde{m}_k W_{ik}
$$
when computing the pressure and force, these particles should be considered as well.

**How-to-Sample**: 

1. uniform / non-uniform
2. single-layer/multi-layer

**Pros**: 

1. simplicity: generate, integration, computation

**Cons**: 

1. result in small time-steps for weak-incompressible fluids. (pressure variety is large)
2. even simple geometry shape need large amount of particles.
3. *bumpy representation*: reduce the accuracy of pressure computation, introduce artificial friction. -> Implicit boundary representation.

### Implicit Method

Signed Distance Function.

### Computing the boundary pressure

Original, without boundary:

$$
(a_i^P)^l = - \frac{1}{\rho_i} \nabla p_i^l = - \sum_j m \left( p_i^l/\rho_i^2 + p_j^l/\rho_j^2 \right)\Delta W_{ij}
$$

With boundary:

$$
(a_i^P)^l = - \sum_j m_j \left( p_i^l/\rho_i^2 + p_j^l/\rho_j^2 \right)\Delta W_{ij} - \sum_k m_k \left( p_i^l/\rho_i^2 + p_k^l/\rho_k^2 \right)\Delta W_{ik}
$$

To define $p_k$:

1. Pressure Mirroring: $p_k = p_i$
2. Pressure Extrapolation: 

$$
p_k = \frac{\sum_l p_lW_{kl}+ \mathbf{g} \cdot \sum_j \rho_l(x_k - x_l)W_{kl}}{\sum_l W_{kl}}
$$

### Penalty based Methods

**Cons**: hard to control the stiffness, and have small time steps.

## Other Techniques

1. Adaptive time-step
2. Data-Driven.

### CNNs

Target: enforce incompressibility

Steps:

1. Rasterize to Grid.
2. use cnn on grid to compute the velocity correction.

## Future work

1. Approximate Quality:
    1. particle count is low => degradation of approximation
    2. lack of practical and sufficient solution: because negative pressure are clamped to 0, only projective Jacobi or GS Iteration is allowed. Conj-Grad is not available currently.
2. Unified Solver & Ultimate Coupling:
    1. Unified Coupling solver.
    2. Suitable for multiple particle-resolution.
3. Artist Control
4. Data Driven






