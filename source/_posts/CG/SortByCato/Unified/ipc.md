---
title: 论文阅读：Incremental Potential Contact 大杂烩
author: Clover
date: 2022/11/30 # yyyy-mm-dd
categories: Physical Simlation
tags:
  - IPC
  - Paper Reading
  - Computer Graphics
plugins:
  - mathjax
---

Incremental Potential Contact

<!-- more -->

## C-IPC

### Related Works

#### Shell and Rods

#### Strain Limiting

目的：对于膜(Shell)的形变进行限制。

主要四个技术：

1. 施加约束（Eq, In-Eq）
2. DoF限制
3. Splitting Model
4. Solver

#### Modeling Thickness: 厚度建模

#### CCD

#### 对于多维度物体的统一建模

### Formulation

Elasto Dynamics: Implicit Time(Optimize-based) Integration.

$$
E = \frac{1}{2} \| x - \hat{x}^n \|^2 + \alpha h^2 \Psi (\beta x + \gamma x^n)
$$

