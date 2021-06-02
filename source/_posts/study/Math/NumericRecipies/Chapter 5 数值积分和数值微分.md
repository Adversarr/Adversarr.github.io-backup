---
layout: post
title: 数值积分和数值微分
group: group-numeric-recipies
order: 5
categories: [数学]
tags:
  - 数值分析
sidebar: [group-numeric-recipies, toc]
---

数值分析 ch 5 - 数值积分和数值微分

<!-- more -->

# Chapter 5 数值积分和数值微分

1. 插值型求积公式

2. 复化求积公式

3. Romberg求积法

4. Gauss求积公式

5. 数值微分

---

## 数值积分的基本概念

$$
\int_{a}^bf(x) \mathrm dx\approx \sum_{k=0}^n A_k f(x_k
$$


其中：

1. $x_k$称为插值节点

2. $A_k$为求积系数

## 插值型求积公式

记 $I(f) = \int_a^bf(x)\mathrm dx$，则$f$的一个插值多项式为 $L_n(x)$，其中 $l_k(x)$ 是插值基函数。则用 $L_n(x)$ 替代被积函数，一个求积公式为：

$$
I_n(f) = \sum_k A_kf(x_k)\\
A_k = \int _a^b l_k(x)\mathrm dx 
$$

### 插值型求积公式

**Def**：（插值型求积公式）设有计算$I(f)$的求积公式
$$
I _ n(f)=\sum _ {k=0}^nA _ k f(x _ k)
$$
若其求积系数$A _ k=\int _  a ^ bl _ k (x)\mathrm dx$，则称该求积公式为插值型求积公式。

截断误差为：

$$
R(f) = \int_a^b \frac{f^{(n+1)}(x_0)}{(n+1)!} \prod_k(x-x_k)\mathrm dx
$$

**Def**：（Newton-Cotes公式）若求积节点是等间距的，即 $x_k = a+kh$，则该插值型求积公式称为 Newton-Cotes 公式。

记：
$$
C_{n,k} = \frac{(-1)^{n-k} h}{k!(n-k)!} \int _ {0} ^ n\prod _ {j=0\\j\ne k}^n(t-j)\mathrm dt
$$
N-C公式可转化为：
$$
I _ n(f) = \sum _ {k=0} ^ n C _{n, k} f(x_k)
$$
常用的三种插值求积公式：

1. 梯形公式：$T(f) = \frac{b-a} 2 [f(a) + f(b)]$
2. Simpson公式：$S(f) = \frac{b-a}{6}[f(a)+4f(\frac{a+b} 2)] + f(b)]$
3. Cotes公式：$C(f) = \frac{b-a}{90} [7f(a) +32f(\frac{3a+b} 4) + 12 f(\frac{a+b} 2) + 32f(\frac{a+3b}4)+7f(b)]$

### 代数精度

当$f(x)$为多项式时，考虑截断误差：
$$
R(f) = \int _ a ^ b \frac{f^{(n+1)}(\xi)}{(n+1)!} \prod _ {k=0} ^ n (x-x _ k) \mathrm dx = 0
$$
则 $I _ n(f) = I(f)$，求积公式是精确的

**Def**（代数精度）计算 $I_n(f)$ 的求积公式，若对于所有$m$次多项式是精确的，但至少对一个$(m+1)$次数的多项式是不精确的，则称该求积公式具有$m$次代数精度。

**Thm**：求积公式 $I_n(f)$ 至少有$n$次代数精度的充分必要条件是该公式是插值型的。

**Thm**：求积公式 $I_n(f)$ 至少有$m$次代数精度的充分必要条件是该公式对$f(x)=x^i,~i=0, 1, ...,m$都精确成立，但对$f(x)=x^{m+1}$不精确成立

常用三种插值求积公式的代数精度：

1. 梯形公式：截断误差为$-\frac{(b-a)^3}{12} f''(\eta)$，代数精度为 1
2. Simpson公式：截断误差为$-\frac{(b-a)^5}{2880}f^{(4)}(\eta)$，代数精度为3
3. Cotes公式：代数精度为5

## 复化求积公式

### 复化梯形求积公式

对每个小区间上的积分 $\int _ {x _ k} ^{x _ {k+1} }f(x)\mathrm dx$ 都应用梯形公式：
$$
T _ n(f) = \sum _ {k=0}^{n-1} \frac h 2 [f(x _ k) + f(x _ { k + 1 })]
$$
截断误差为：
$$
I(f) - T_n (f) = - \frac {h^3} {12} \sum _ {k = 0} ^{ n - 1} f''(\eta _ k )
$$
其**先验误差估计**为：
$$
I(f) - T _ n (f) = \frac{b - a} {12} h^ 2|f''(\eta) | \le \frac{b - a} {12} M_2 h^2\le \varepsilon\\
M_2=\max_{a\le x \le b} |f''(x)||
$$
其**后验误差估计**为：
$$
|I(f) - T _ {2n} (f) | \approx \frac 1 3 |T _ {2n} - T _ n (f)|< \varepsilon
$$

### 复化Simpson公式

对每个小区间上的积分 $\int _ {x _ k} ^{x _ {k+1} }f(x)\mathrm dx$ 都应用Simpson公式：
$$
S _ n(f) = \sum _ {h=0} ^ { n - 1} \frac h 6 [f(x _ k) + 4 f(x _ {k + 1/2}) + f( x _ {k+1})]\\
x _ {k + 1/ 2} = \frac 1 2(x_k + x _ { k + 1})
$$
其截断误差为：$-\frac{b-a}{180}(\frac{h}2)^4\sum_{k = 0} ^ {n-1} f^{(4)}(\eta_k)$

