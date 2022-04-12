---
title: Collision Detection 整理 6 - 综述
date: 2022-04-12
categories: 计算机图形学
tags:
  - 几何
  - 计算机图形学
math: true
plugins:
  - mathjax
  - katex
hide: false
---

终于到了综述了。

<!-- more -->

这一篇的思路很清楚，从最核心的CCD开始说起，一步步解决碰撞检测的问题。

## Narrow-phase 

### Preliminaries

沿用IPC中的记号。对于碰撞检测而言，最基本的模型是假设其在两个迭代步骤之间是线性的，即

$$
\mathbf x(t) = t \cdot \mathbf x ^{i + 1}  + (1 - t) \cdot \mathbf x ^{i}
$$

其中：

- $t$ 为归一化后的时间，即 $t = (t - t_{i}) / (t_{i + 1} - t _i )$ 其中右侧的 $t$ 是模拟运行时间
- $\mathbf x$ 是坐标，是关于时间的函数。上标表示迭代代数

为了简单期间，用 $\mathcal A = \mathbf x_1\cdots \mathbf x_i$ 来表示一个 $n$ 维单纯形，用 $\mathbf x_{ij}$ 来表示 $\mathbf x_{i} - \mathbf x_{j}$。

在这样的记号下，碰撞可以用 $t$ 来描述，即：

单纯形 $\mathcal A = \{\mathbf x_1 \cdots\mathbf x_n\}$ 和 $\mathcal B = \{\mathbf x_1 \cdots \mathbf x_m\}$ 碰撞，当且仅当：

$$
\exists t\in[0, 1]\quad s.t. \  \mathcal A(t) \cap \mathcal B(t) \ne \emptyset
$$

这个公式仅仅是一个定义，并没有很大的计算价值，因此我们需要对于这样的问题进行适当的简化。主要有几种思路：

1. 和求出凸包交点的思路一致，进行 Minkowski 差操作，然后二分查找一下根的情况。
2. 二分搜索，找可能的碰撞时间 $t$
3. 约束为三角网格再：
   1. 求解重心坐标$(u,v)$ 和 $t$
   2. 简化为三次方程求根
4. 光线投射方法
5. 基于法向量简化

### CCD



## Broad-Phase

实际上这个没啥好讲的，主要思路就是建立空间数据结构，然后加速计算。

1. BVHs
2. Spatial Hashing

好吧实际上还有一些，在这个的基础上还有一些 local 的加速方法，但这也不能算是 Broad-Phase 的方法，因为这个方法针对于 *Deformed* 的物体进行计算的效率较高。这些方法在曲面上进行划分，相当于在曲面上定义了一个空间划分。比如通过形变能量来指导在其上的空间划分，最后精细化求解使用三次方程法求解。