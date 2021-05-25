---
title: 函数项级数
date: 2020-06-01 18:07:35
tags:
  - 高等数学
  - 级数
categories: 数学
math: true
---

函数项级数

<!--more-->

**Def**：将无穷多项的一列函数依次用加号得到的表达式称为函数项级数$\displaystyle\sum\limits_{n=1}^{\infty}u_n(x_0)$

## 函数项级数的处处收敛性

**Def**：（函数项级数的处处收敛性和和函数）若级数 $\displaystyle\sum\limits_{n=1}^{\infty}u_n(x_0)$ 收敛，则称 $x_0$ 为**收敛点**，收敛点全体构成的集合称为**收敛域**，相对应的定义**发散点**，**发散域**。如果 $\forall x\in D$ 级数收敛则称为在 $D$ 上处处收敛。称收敛处的极限值为**和函数** $S(x)$

与常数项级数相似，**余项** $R_n(x) = S(x) -S_n(x) \rightarrow 0 (n\rightarrow \infty)$

{% noteblock quote %}

**Tips**

需要注意的是，有限个可导函数的和为可导函数，可积函数的和为可积函数，但是在无穷多个时此结论不一定成立

{% endnoteblock %}

## 函数项级数的一致收敛性与判别法

**Def**：（一致收敛性）$\forall \varepsilon >0,\exists N(\varepsilon)\in \mathrm N_+,\forall n>N(\varepsilon)\forall x\in D,|S_n(x)-S(x)|<\varepsilon$

**Thm**：（Cauchy 一致收敛原理）函数项级数一致收敛的充要条件是 $\forall \varepsilon>0,\exists N(\varepsilon)i\in \mathrm N,\forall n,p\in\mathrm N_+,n>N时\forall x\in D,|S_{n+p}-S_n|<\varepsilon$

> 这个结论是显然的，我们需要更多的准敛法则

**Thm**：（M 判别法、Weierstrass 准则）如果存在一个收敛的正项级数，恒大于一个函数项级数的绝对值，则该函数项级数收敛。

> 这个结论也是显然的，用三角不等式和柯西判别法判断即可。

## 一致收敛级数的性质

**Thm**：（和函数的连续性）原函数连续且一致收敛则和函数连续

**Thm**：（和函数的可积性）原函数可积且一致收敛则和函数可积

**Thm**：（和函数的可导性）原函数导函数且连续一致收敛则和函数可导

> 在幂级数和傅里叶级数中，这三个定理有极大的作用