---
title: 「概率统计与随机过程」 10 - 马尔科夫链
date: 2020-12-11
categories: Mathematics
tags:
  - 概率论
math: true
plugins:
  - mathjax
  - katex
hide: false
---

马尔科夫链
<!-- more -->

## 马尔科夫链

### 马尔科夫链的基本概念

**Def**（马尔科夫链）随机过程 $\{X_n,n\ge 0\}$ 如果满足如下条件：

1. 状态空间 $I=\{x_0, x_1, ..., x_n,...\}$ 为可数集
2. 对于一切 $n\ge 1$ 和所有的 $x$, $x_{i_0}, x_{i_1},...,x_{i_{n-1}}\in I$ 都有

$$
P(X_n=x|X_0=x_{i_0},X_1=X_{i_1},...,X_{n-1}=x_{i_{n-1}})=P(X_n=x|X_{n-1}=x_{n-1})
$$

则称 $\{X_n,n\ge 0\}$ 是马尔科夫链。

**Def**（n 步转移概率）设 $\{X_n,n\ge 0\}$ 是一个马尔科夫链，称 $p_{ij}(m,m+n)=P(X_{m+n}=j|X_m=i)$ 为马氏链的 n 步转移概率（$\forall i,j\in I$）。

由 $p_{ij}(m,m+n)$ 组成的矩阵 $P(m,m+n)=(p_{ij}(m,m+n))$ 称为 $\{X_n,n\ge 0\}$ 的 **n 步转移概率矩阵**。

**Def**（齐次的马尔科夫链）设 $\{X_n,n\ge 0\}$ 为一马尔科夫链，如果对所有的 $m\ge 0$，$n\ge 1, i,j\in I$ 有 $P(X_{m+n}=j|X_m=i)=P(X_n=j|X_0=i)$ 则称为齐次的马氏链。

此时，一步转移概率矩阵记为 $P=P(1)=(p_{ij})$。

**Thm**：若对于一切的 $n$ 和 $i,j\in I$ 有：

$$
P(X_{n+1}=j|X_n=i)=P(X_1=j|X_0=i)
$$

则 $\{X_n,n\ge 0\}$ 是齐次的马氏链

**Thm**：齐次的马氏链的 $P(n)$ 有：

$$
\begin{cases}
    p_{ij}\ge 0,\\
    \sum p_{ij}=1
\end{cases}
$$

### 齐次马尔科夫链的有限维分布

**Def**（分布律）设 $\{X_n,n\ge0\}$ 是一个齐次的马尔科夫链，状态空间为 $I=\{0,1,2,...\}$ 对于任意时刻 $n\ge 0$，称离散型随机变量的分布律为齐次马氏链的一维分布律，记为 $\mathbb p(n)=(p_0(n),....)$

当 $n=0$ 时，称为初始分布律。

**Thm**：$p(n)=p(0)P(n)$，其中 $P(n)$ 为多步转移概率矩阵。

### 多步转移概率的确定

**Pre**（条件的全概率公式）设随机事件 $A_1,...A_n,...$ 构成完备事件组：

$$
\bigcup_{i=1}^\infty A_i=\Omega,A_iA_j=\varnothing
$$

则：$P(B|C)=\sum_{i=1}^\infty P(A_i|C)P(B|A_iC)$

**Thm**：设 $\{X_n,n\ge 0\}$ 是齐次马尔科夫链，其状态空间为 $I=\{0,1,...\}$ n 步转移矩阵为 $P(n)$。则对于任意时刻 $m,n\ge 1$，有$P(m+n)=P(m)P(n)$（C-K 方程）

根据 C-K 方程：$P(n)=P^n$

### 遍历性

**Def**（极限分布）设 $\{X_n,n\ge 0\}$ 是齐次马氏链，状态空间为 $I=\{0, 1,2,...\}$，对于所有的 $i,j$ 而言，n 步转移概率极限存在且与 $i$ 无关，

$$
P(n)=P^n\rightarrow^{n\rightarrow\infty}\left[
\begin{matrix}
    \pi_0&\pi_1&\cdots&\pi_j&\cdots\\
    \pi_0&\pi_1&\cdots&\pi_j&\cdots\\
    \vdots&\vdots&\ddots&\vdots\\
    \pi_0&\pi_1&\cdots&\pi_j&\cdots\\
    \vdots&\vdots&&\vdots
\end{matrix}
\right]
$$

则称此链具有遍历性。

$P^n$ 求法：

1. 求出矩阵的特征值分解 $A=V\Lambda V^{-1}$
2. 求 $P^n$

**Thm**：若 $\{X_n,n\ge 0\}$ 是齐次马氏链，一部转移概率为 $P$ 若存在 n 步转移概率矩阵 $P(n)$ 无零元，则此链具有遍历性，其极限分布 $\pi$ 是：

$$
\pi P=\pi
$$

满足归一性条件（$\mathbf 1^T\pi=1$）的唯一解。
