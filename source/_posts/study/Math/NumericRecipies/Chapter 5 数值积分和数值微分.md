---
layout: post
title: 数值分析-数值积分和数值微分
group: group-numeric-recipies
order: 5
categories: [数学]
tags:
  - 数值分析
sidebar: [group-numeric-recipies, toc]
plugins:
  - mathjax
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

插值型求积公式
: 设有计算$I(f)$的求积公式

$$
I _ n(f)=\sum _ {k=0}^nA _ k f(x _ k)
$$

若其求积系数$A _ k=\int _  a ^ bl _ k (x)\mathrm dx$，则称该求积公式为插值型求积公式。

截断误差为：

$$
R(f) = \int_a^b \frac{f^{(n+1)}(x_0)}{(n+1)!} \prod_k(x-x_k)\mathrm dx
$$

Newton-Cotes公式
: 若求积节点是等间距的，即 $x_k = a+kh$，则该插值型求积公式称为 Newton-Cotes 公式。

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

代数精度
: 计算 $I_n(f)$ 的求积公式，若对于所有$m$次多项式是精确的，但至少对一个$(m+1)$次数的多项式是不精确的，则称该求积公式具有$m$次代数精度。

{% p blue, Theorem %} 求积公式 $I_n(f)$ 至少有$n$次代数精度的充分必要条件是该公式是插值型的。

{% p blue, Theorem  %} 求积公式 $I_n(f)$ 至少有$m$次代数精度的充分必要条件是该公式对$f(x)=x^i,~i=0, 1, ...,m$都精确成立，但对$f(x)=x^{m+1}$不精确成立

常用三种插值求积公式的代数精度：

1. 梯形公式：截断误差为$-\frac{(b-a)^3}{12} f''(\eta)$，代数精度为 1
2. Simpson公式：截断误差为$-\frac{(b-a)^5}{2880}f^{(4)}(\eta)$，代数精度为3
3. Cotes公式：代数精度为5

### 梯形公式、Simpson公式和Cotes公式的截断误差

$$
R_T(f) = -\frac{(b-a)^3}{12}f''(\eta),\quad \eta\in (a,b)
$$

$$
R_S(f) = -\frac{(b-a)^4}{2880}f^{(4)}(\eta),\quad\eta\in (a,b)
$$

$$
R_C(f) = -\frac{2(b-a)}{945}(\frac{(b-a)}4)^6f^{(6)}(\eta),\quad\eta\in (a,b)
$$



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

先验误差估计为：

$$
I(f) - S_n(f) = - \frac{b-a}{180}\left( \frac h 2 \right)^4f^{(4)}(\eta)
\\
|I(f) - S_n (f)| \le \varepsilon
$$

后验误差估计为：

$$
I(f) - S_{2n}(f) \approx \frac 1 {15} (S_{2n}(f) - S_n (f))\\
|I(f) - S _ {2n} (f)|\approx \frac 1 {15} |S_{2n}(f) - S_j(f)|
$$

### 复化 Cotes 公式

记

$$
x_{k+\frac14} = x_k +\frac14 h,\quad  x_{k+\frac12}= x_k + \frac 12 h,\quad \cdots
$$

对于积分$\int_{x_k} ^{x_{k+1}}f(x)\mathrm dx$应用Cotes公式，得到复化Cotes公式

$$
C_n(f) = \sum_{k=0}^{n-1} \frac h{90}[7f(x_k) + 32 f(x_{k+\frac 14}) + 12 f(x_{k+\frac12}) + 32 f(x_{k+\frac34}) + 7f(x_{k+1})]
$$

其截断误差为

$$
I(f) - C_n(f) = -\frac{2(b-a)}{945}\left( \frac h2 \right)^6f^{(6)}(\eta), \quad \eta\in (a,b)
$$

后验误差估计为：

$$
I(f) - C_{2n}(f)\approx \frac1{63} [C_{2n}(f) - C_n(f)]
$$

### 求积公式的阶数

求积公式的阶数
: 如果计算积分$I(f)$的复化求积公式$I_n(f)$，存在正整数$p$和非零常数$C$使得：
$$
\lim_{h\rightarrow 0} \frac{I(f)-I_n(f)}{h^p} = C
$$
则称公式$I_n(f)$是$p$阶的。


{% p blue, Theorem 复化公式的阶数 %}

1. 复化梯形公式 —— 2阶
2. 复化Simpson公式 —— 4阶
3. 复化Cotes公式 —— 6阶

## Romberg 积分法

注意到：

$$
I(f) \approx \frac 43 T_{2n}(f) - \frac13 T_n(f)
$$

实际上：

$$
S_n(f) = \frac43 T_{2n}(f) - \frac13 T_n(f)
$$

$$
C_n(f) = \frac{16}{15} S_{2n}(f) - \frac 1{15} S_n(f)
$$

则：

Romberg公式
: 称

$$
R_n(f) = \frac{64}{63} C_{2n}(f) - \frac{1}{63}C_n(f)
$$

为Romberg公式，且其具有7次代数精度。

Romberg求积法可以通过列表计算

| n | T | S | C | R |
|---|---|---|---|---|
| 1  | $T_1$ | $S_1$|$C_1$| $R_1$|
|2| $T_2$|$S_2$|$C_2$|$R_2$|
|4| $T_4$|$S_4$|$C_4$|$R_4$|
|8| $T_8$|$S_8$|$C_8$|$R_8$|
|...|...|...|...|...|

每一次选择一个n，向右上方计算。

## Gauss求积公式

Gauss-Legendre 公式
: 设 $I_n(f)$ 是求积分$I(f)$的求积公式，其代数精度为$(2n+1)$则称其为 **Gauss-Legendre 公式**，对应的节点为**Gauss点**。

{% p blue, Theorem %} 若有插值型求积公式 $I_n(f)$，$I_n(f)$是Gauss求积公式 当且仅当 $W_{n+1}(x)$ 和让任何一个次数不超过 $n$ 的多项式正交。

### 正交多项式

正交多项式序列
: 设 $g_n(x) = a_{n,0} x^n + a_{n,1}x^{n-1}+\cdots + a_{n,n}$ 对于任意 $i,j$ 有 $(g_i, g_j)=0$ 则称 $\{g_ k(x)\} _{k=0}^\infty$ 是$[a,b]$上的**正交多项式序列**。

{% p blue, Theorem %} 正交多项式序列是线性无关的 

{% p blue, Theorem %} 正交多项式序列中$g_n(x)$在$[a,b]$上有$n$个零点

n次Legendre多项式
: 称

$$
P_n(t) = \frac 1 {2^nn!} \frac{\mathrm d^n(t^2-1)^n}{\mathrm dt^n},\quad n = 0,1,2,\cdots
$$

为Legendre多项式

{% p blue, Theorem Lerandre多项式 %} $\{P_k(t)\}$ 在 $[-1,1]$ 上正交。

### 区间 [-1, 1] 上的Gauss公式

$n+1$ 次 Legendre多项式的零点就是Gauss公式的节点，求积系数为：

$$
\tilde A_k = \int _{-1} ^1 \prod_{j=0,j\ne k} ^n \frac{t-t_j}{t_k-t_j}\mathrm dt
$$

### 区间 [a, b] 上的Gauss公式

转化为 $[-1,1]$ 的Gauss公式求解。

### Gauss 公式的截断误差

截断误差为：

$$
R(f) = \frac{f^{(2n+2)}(\xi)}{(2n+2)!}\int_a^b W_{n+1}^2(x)\mathrm dx
$$

### Gauss 公式的稳定性和收敛性

{% p blue, Theorem %} Gauss公式的求积系数都是正的

求积公式的稳定性
: 若对于任意 $\varepsilon>0$ 存在 $\delta > 0$ 当 $\max_{0\le k \le n}|f(x_k) - \tilde f_k| < \delta$ 时， 有$|I_n(f) - I_n(\tilde{f})|<\varepsilon$ 则该公式是稳定的。

{% p blue, Theorem %}

Gauss公式是稳定的

求积公式的收敛性
: 若对于任意 $\varepsilon>0$ 存在$N$，当$n>N$时，有$|I(f) -I_n(f)|<\varepsilon$ 则称该求积公式收敛。

{% p blue, Theorem Gauss公式的收敛性 %} 若 $f\in C[a,b]$ 则 Gauss公式收敛。

