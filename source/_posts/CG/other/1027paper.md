---
title: 
author: Clover
date: 2022/10/27 # yyyy-mm-dd
categories: Anything
tags:
  - Anything
math: false # true
plugins:
  - mathjax
---

1027 论文汇报

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

\nabla A _ i = \rho _ i + \sum _ {j} m _ j  \left ( \frac { A _ i} { \rho _ i  ^ 2} + \frac{A _ j} {\rho _ j ^ 2}\right) \nabla W_ { i j }\\

\nabla \cdot \mathbf A _ i = - \frac 1 { \rho _ i} \sum _ j m _ j \mathbf A _ {ij} \cdot \nabla W _ {ij} \\

\nabla ^ 2 A _ i = 2 \sum _ { j } \frac { m _ j} { \rho _ j} A _ {ij} \frac {\mathbf x _ {ij} \cdot \nabla W _ { ij }}{\mathbf x _ {ij} \cdot \mathbf x _ {ij} + 0.01 h ^ 2}

\end{aligned} 
$$

Here, $\rho$ is computed using:

$$
\rho _ i  = \sum  _ j m _ j W _ { i j }
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
p _ i = k \left( \left ( \frac{\rho _ i}{\rho _ 0}\right) ^ 7 - 1 \right)
$$

where: 

- $\rho _ 0$ is the rest density.
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

## InCompressibility

### Non Iterative EOS Solver

**EOS**: Describe the relation between $\rho$, $p$, and $T$(temperature).

Original:

$$
p = p (\rho , T) = \frac{\mu} {R} \rho T
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
repeat until convergence:                   -> Projection
  foreach P: compute density and pressure
  foreach P: update velocity and positions
```

e.g.:

1. PCISPH
2. LPSPH

### Pressure Projection

Solve a pressure poisson equation(PPE).








