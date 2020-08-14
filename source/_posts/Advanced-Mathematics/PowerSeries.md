---
title: 幂级数
date: 2020-06-01 21:33:24
tags:
  - 级数
  - 高等数学
categories: 高等数学
math: true
---

幂级数

<!-- more -->

## 幂级数的收敛半径与收敛区间

**Thm**：（幂级数的收敛情况）幂级数的收敛情况有且仅有以下三种：

1. 收敛范围是整个实轴
2. 收敛范围是一个对称区间
3. 仅在 $x=0$ 收敛

**Thm**：（幂级数的收敛半径）对于幂级数的系数 $a_n$，若 $\rho =\overline{\lim\limits_{n\rightarrow \infty}}\sqrt[n]{|a_n|}$ 则

1. 当 $0\le \rho<+\infty,|x|<\frac 1 \rho$ 幂级数绝对收敛
2. 当 $0<\rho<\infty, |x|>\frac 1 \rho$ 幂级数发散

其中 $R=\frac 1 \rho$ 称作**收敛半径**，称 $(-R,R)$ 为**收敛区间**

{% note primary  %}

**Tips**

收敛区间和收敛域是不同的，区别在于端点处可能条件收敛

{% endnote %}

**Thm**：幂级数在 $x =x_1$ 处收敛，则在 $(-|x_1|,|x_1|)$ 上绝对收敛。若 $x=x_2$ 发散，则它在 $|x|>|x_2|$ 处也发散

> 这个定理很好证明，用 M 判别法即可

**Thm**：对于幂级数的系数 $a_n$ 满足 $\lim\limits_{n\rightarrow\infty}|\frac{a_{n+1}}{a_n}|=l$ 则 $R=\frac 1 l$（包含 0 和无穷的情况）

## 幂级数的性质

**Thm**：（内闭一致收敛）设一个幂级数的收敛半径为 $R>0$，在收敛区间内，幂级数内闭一致收敛

> 如果在 R 处也收敛，则可以补全一致收敛到 R 处，也就是说 $在R处收敛\rightarrow 在[0,R]一致收敛$

**Thm**：幂级数的和函数是在收敛区间内是一个连续函数

**Thm**：幂级数的和函数是在收敛区间内的可微函数，且可以逐项求微，收敛区间不变

**Thm**：幂级数在积分后，收敛区间不变

**Thm**：在可导的情况下，幂级数可以逐项求导任意多次。

**Thm**：在 $x=R$ 处收敛，则和函数在 $[0,R]$ 连续

> 通过函数项级数的判定即可得到这些定理

## 斯特林公式

公式：$\displaystyle n!=\sqrt{2\pi n} (\frac n e)^ne^{\frac{\theta}{12n}}\approx\sqrt{2\pi n} (\frac n e)^n,\theta\in(0,1)$

沃利斯公式：$\displaystyle \frac \pi 2=\lim\limits_{n \to \infty}\frac{[(2n)!!]^2}{[(2n-1)!!]^2(2n+1)}$