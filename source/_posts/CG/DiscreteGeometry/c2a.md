---
title: 离散微分几何 - 1 - Introduction 
author: Clover
date: 2022/8/8 # yyyy-mm-dd
# categories: {random}
# tags:
#  - {random}
math: true
plugins:
  - mathjax
  - katex
---


<!--more-->


## Combinatorial Surfaces （Mesh）

### What is a mesh?

1. simplical complex
    1. Abstract/geometric
    2. Oriented, manifold simplical complex.
2. Cell complex
3. Data structures.

### Connection to DG?

1. Topological space. <-> Abstract simplical complex

## Convex Set

1. Definition.
2. Convex Hull

### Simplex

1. Definition: Linear Independence
2. Definition: Affine Independence($v_i = p_i - p_0$ are linear indenpendent)


Definition: a k-simplex is the convex hull of $k+1$ affine-independent points, which we call its vertices.

### Barycentric Coordinates

- we can describe a simplex more explicitly using barycentric-coord.

any point $p$ inside simplex can be expressed as a weighted combination of the vertices.

$$
\sigma = \left \{ 
\sum _{i = 0} ^ k t _ i p _ i : \sum _{i = 0} ^ k t_i = 1, t_i \ge 0
\right\}
$$

Definition: **standard** n-simplex(select $p_i = \epsilon _ i$)

### Simplicial Complex

> a bunch of simplicies.

face
: a face of a simplex is any simplex whose vertices are a subset of the vertices of $\sigma$

Simplicial Complex
: a collection of simplicies where:
1. the intersection of any two simplicies is a simplex.
2. every face of every simplex in the complex is also in the complex

