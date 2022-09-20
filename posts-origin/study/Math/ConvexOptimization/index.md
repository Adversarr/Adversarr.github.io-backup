---
title: 最（凸）优化方法 [Overview and Intro]
date: 2020-9-26
categories: 数学
tags:
  - 凸优化
mathjax: true
plugins:
  - mathjax
  - katex
hide: false
---

2020-2021-1 最优化方法

<!-- more -->

## 引言

### 数学优化

数学优化问题：（数学规划）

{% noteblock quote %}
从一个**可行解集合**中,**寻找**出**最优**元素。
{% endnoteblock %}

数学形式：

$$
\begin{aligned}
    &\min . &f_0(x)\\
    &~\mathrm{s.t.} & f_i(x) \leq b_i, i = 1,\dots,m
\end{aligned}
$$

其中：

- 优化变量：$x$
- 目标函数：$f_0:\mathrm{R}^n\rightarrow\mathrm{R}$
- 约束函数：$f_i:\mathrm{R}^n\rightarrow\mathrm{R}$
- 最优解：在**所有满足约束的向量**中，向量 $x^*$ 对应的目标函数值**最小**

### 应用

- 投资组合优化
  - 优化变量：各资产分配的资本数
  - 约束：总预算、每⼀份资产的资本范围、最⼩收益
  - ⽬标：总风险或回报
- 电⼦设计中的器件尺⼨
  - 优化变量：器件的长和宽
  - 约束：⼯程约束、时间要求、最⼤⾯积
  - ⽬标：总功耗
- 数据拟合
  - 优化变量：模型参数
  - 约束：先验信息、参数限制
  - ⽬标：预测误差

### 求解优化问题

- 一般形式的优化问题
  - 难以求解
  - 折中：长时间的计算代价、找不到解
- 特定问题
  - 最小二乘
  - 线性规划
  - 凸优化问题

### 最小二乘

形式：$\displaystyle\min.||Ax-b||_2^2$

- 有解析解 $x* = (A^TA)^{-1}A^Tb$
- 有可靠的求解算法和软件 <!-- TODO -->
- 计算时间：正比于 $n^2k(A\in \mathrm{R}^{k\times n})$
- 技术成熟
- 最⼩⼆乘的使⽤
  - 判别⼗分简单
  - 使⽤标准⽅法增强灵活性（加权、正则化）

### 线性规划问题

$$
\begin{aligned}
    &\min. &c^Tx\\
    &\mathrm{~s.t.} &a_i^Tx\le b_i
\end{aligned}
$$

- 没有解析解
- 具有可靠且有效的求解算法和软件
- 计算时间：正⽐于$n^2m~(if~m \ge n)$，若具有特殊结构，求解更快。
- 成熟技术
- 判别难于最⼩⼆乘
- ⼀些标准的技巧可⽤于将某些问题转化为线性规划（分段线性⽅程、包含范数的问题）

<!-- TODO: ppt p48 -->