---
title: 傅里叶级数
date: 2020-06-07 19:40:12
tags:
  - 级数
  - 傅里叶
categories: 高等数学
mathjax: true
---

傅里叶级数，真的就看上去简单。

<!-- more -->

## 三角函数系及其正交性

在这里就直接给出这个单位正交系：

$1,\frac{1}{\sqrt{2\pi}}\cos x,\frac{1}{\sqrt{2\pi}}\sin x,\frac{1}{\sqrt{2\pi}}\cos 2x,\frac{1}{\sqrt{2\pi}}\sin 2x,\dots$

但是我们用的更多的是：

$1,\cos x,\sin x,\cos 2x,\sin 2x,\dots$

> 这里正交指的是**积分**：$\displaystyle<f,g>=\int_a^b f\cdot g$

## 周期为 2pi 的函数的傅里叶级数及其收敛性

### 周期函数的傅氏系数和傅氏级数

- **Def**：（傅里叶系数、傅里叶级数）将

$$
a_n=\frac 1 \pi\int_{-\pi}^{\pi}f(x)\cos nx\mathrm dx(n=0,1,2,\dots)\\
b_n=\frac 1 \pi\int_{-\pi}^{\pi}f(x)\sin nx\mathrm dx(n=1,2,3,\dots)
$$

称为函数$f$ 的**傅里叶系数**，而

$$
\frac {a_0} 2+\sum\limits_{n=1}^\infin(a_n\cos nx+b_n\sin nx)
$$

称为**傅里叶级数**

> 问题在于，这个级数的和函数不一定和原函数相等，因而，我们用$\displaystyle f\sim \frac {a_0} 2+\sum\limits_{n=1}^\infin(a_n\cos nx+b_n\sin nx)$ 来表示。

### 傅氏级数的收敛性定理和傅氏展开式

> 吐槽一下工科数分，人家高等数学讲的炒鸡清楚！

- **Def**：（分段连续）$f(x)$ 在 $[a,b]$ 上除了**有限个**第一类间断点外处处连续。

- **Def**：（分段单调）$f(x)$ 在 $[a,b]$ 上有**有限个**单调区间。

- **Def**：（`Dirichlet` 条件）$f(x)$ 分段连续且分段单调

- **Thm**：（傅里叶级数的收敛性定理）如果 $f$ 在 $[-\pi,\pi]$ 满足 `Dirichlet` 条件，则其傅氏级数在$[-\pi,\pi]$任意一点都收敛，且和函数为

$$
\displaystyle S(x) =\begin{cases}f(x),&连续点\\
\frac{f(x+0)+f(x-0)}{2},&间断点
\end{cases}
$$

- **Thm**：（傅里叶级数的收敛性原理2）若 $f(x)$ 以 $2\pi$ 为周期，且在区间 $[-\pi,\pi]$ 上分段可微，则该傅里叶级数在任一点处收敛到和函数 $\displaystyle S(x) =\frac 1 2(f(x+0)+f(x-0)),-\infin<x<\infin$

> 这个时候，我们才能用 $=$ 替换 $\sim$

{% note info TODO: %}

有了这个定理之后，就有一系列的骚操作了

TODO:

{% endnote %}

### 奇偶周期函数的傅氏级数

- 偶函数：$b_n=0,~f(x)=\frac {a_0}{2}+\sum\limits_{n=1}^{\infin} a_n\cos nx$ 称为**傅氏余弦函数**

- 奇函数：$a_n=0,~f(x) \sim \sum\limits_{n=1}^\infin b_n\sin nx$ 称为**傅氏正弦函数**

> 这个结论是显然的，只是给个定义

### 任意周期函数的傅氏级数

我们替换$a_n,b_n$ 中的系数做一些替换即可，若定义在$[-l,l]$，周期为$2l$
$$
a_n=\frac 1 l\int_{-l}^{l}f(x)\cos nx\mathrm dx(n=0,1,2,\dots)\\
b_n=\frac 1 l\int_{-l}^{l}f(x)\sin nx\mathrm dx(n=1,2,3,\dots)
$$
但是重点在于，傅氏级数不仅仅可以用于讨论周期函数，也可以拿来讨论任意一个函数。

**周期延拓函数** $F(x)$：$F(x)=f(x-2kl)$

又如在 $[0,l]$ 上的函数：

- **奇延拓**：
  $$
  F_1(x)=\begin{cases}
  f(x),&0<x\le l\\
  0,&x=0\\
  -f(-x),&-l\le x<0
  \end{cases}
  $$
  

- **偶延拓**：
  $$
  F_2(x)=\begin{cases}
  f(x),&0\le x\le l\\
  f(-x),&-l\le x<0
  \end{cases}
  $$
  