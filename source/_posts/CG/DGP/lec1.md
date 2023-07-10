---
title: Digital Geometry Processing
plugins:
- mathjax
---

GCL-F-DGP1

<!-- more -->

## Representations

How to represent geometry data in computer.

### Point cloud

$$
P = \{ p _ 1, \dots , p _ n\}
$$

A set of data points in some coord-system.

Applications: scanners

### Signed Distance Function (SDF)

Give the distance of a given point x from the boundary of $\Omega$

1. inside -> neg
2. outside -> pos

> Truncated SDF(TSDF)

### Implicit Function

$$
F(x, y, z) = 0
$$

SDF is some kind of IF.

### Grid

#### Pixel, Voxel

1. Adaptive: Grid-Hierarchical Oct-Tree
2. Patch-based quadtree.
   
   Ref: Adaptive O-CNN

### Triangle Mesh

A collection of triangles. without any mathematical structure.

Geometry component:

- Vertices: $v _ 1 ... v _ N$

Topological component:

- Triangle: $T$
- Edge: $E$

> Topology describes the connectivity.

#### Quad Mesh

不一定是共面的！


> **Homework 1**: Shortest Path, Minimal Spaning Tree 

#### 2-manifold

Euler Formula
$$
N_V -N_E+ N_F= 2(1-g)
$$

- $g$为亏格数量

#### Data Structure - requirements

1. Given $f_j$, find its containing vertices in order
2. Given $v_i$, find its one-ring facets in order
3. Given $v_i$, find adjacent vertices/outgoing edges
4. Given $e_k$, find its connected two facets
5. Given $f_j$ and $e_k$, find another facet which connects $e_k$
6. …

Half edge Data structure!


