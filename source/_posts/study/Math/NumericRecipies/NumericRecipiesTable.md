---
title: 数值分析-总结
date: 2021-06-25
layout: post
group: group-numeric-recipies
index: true
sidebar: [group-numeric-recipies, toc, tags]
plugins:
  - mathjax
  - katex
---

2020-2021-3 数值分析（现代数值方法）

<!-- more -->

## 考点概要

### Chapter 1 绪论

1. 误差（误差、误差限、相对误差限的概念）
2. 有效数（位数）

### 非线性方程求根

1. 简单迭代法（构造、收敛性判定）
2. 牛顿迭代法（构造、收敛性判定）
3. 收敛阶、误差估计公式

### 线性方程组的求解

1. 矩阵范数 $\|\cdot\|$
   谱半径 $\rho(A)$
   条件数 $\mathrm{cond}(A)$
2. 三种迭代格式（Jacobi / Gauss-Seidel / SOR）的
   1. 构造（矩阵格式）
   2. {% emp 收敛性判定 %}
   3. （误差估计公式）
3. 非迭代方法
   1. Gauss消元法及其变体（Gauss消元法，列主元消元法）
   2. 三角分解，也就是LU分解（Doolite分解）
   3. 追赶法

### 插值拟合

1. 多项式插值的构造（Lagrange插值、Newton插值）及其误差
2. 分段插值（没见过）
3. {% emp 最小二乘法 %}

### 积分和微分

1. {% emp 插值型求积公式和代数精度 %}
2. 复化求积公式：梯形、Simpson公式的构造
3. 龙贝格积分的构造

### ODE

1. 改进欧拉法
2. 二阶RK方法