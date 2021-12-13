---
title: 「概率统计与随机过程」 2 - 随机变量及其概率分布
date: 2020-11-18
categories: 数学
tags:
  - 概率论
  - 统计
math: true
plugins:
  - mathjax
hide: false
---

随机变量及其概率分布

<!-- more -->

## 随机变量及其概率分布

### 随机变量

**Def**：设 $E$ 时一个随机试验，$\varOmega$ 是其样本空间，如果对于每一个试验的结果 $\omega\in \varOmega$，由唯一的实数$X(\omega)$与之对应，这个定义在试验样本空间上的实值函数$X(\omega)$称为$E$的随机变量。

### 随机变量的分布函数

**Def**（随机变量的分布函数）设 $X(\omega)$是随机变量，称 $F(x) = P(X\le x),~-\infty<x<\infty$

**Thm**：一些定义

- $P(x_1 < X\le x_2) = F(x_2) - F(x_1)$
- $P(x_1\le X< x2) = F(x_2-0) - F(x_1-0)$
- $P(x_1 < X< x2) = F(x_2-0) - F(x_1)$
- $P(x_1\le X\le x2) = F(x_2) - F(x_1-0)$

**Thm**：分布函数的性质

1. $0\le F(x) \le 1$
2. 单调不降
3. 右连续函数：$F(x+0)=F(x)$
4. 有*可数*个间断点

### 离散型随机变量

#### 离散型随机变量的分布律

**Def**（概率函数）设离散随机变量$X$可能取得一切之为 $x_1, x_2,\dots, x_n$ 称为 $X$ 分布律（列），也称为 $X$ 的概率函数。

> 分布律也可以用表格的形式表示：
> |X|x1|x2|x3|...|
> |---|---|---|---|---|
> |P|p1|p2|p3|...|

$X$ 的分布函数 $F(x) = \sum\limits_{x_k\le x} p_k$

#### 常见的离散分布

##### 0 - 1 分布

**Def**：$0 - 1$分布：$X$ 只取 $0$ 和 $1$ 两个值，且$P(X=1)=p,~P(X=0)=1-p$，则称 $X$ 服从 $(0-1)$ 分布。

##### 二项分布

**Def**：n次独立试验概型

> **伯努利试验**只有两个可能结果，$A,~\bar A$，且$P(A)=p$
> - $n$ 重伯努利试验是指将试验独立重复 $n$ 次。
> - $X$ 表示 $n$ 重伯努利试验中事件 $A$ 发生的次数
> 
> 称随机变量$X$服从参数为$n,~p$ 的二项分布，$X\sim B(n,p)$
> - $P(X=k) = C_n^k p^k (1-p)^{n-k}$

**Thm**：$X$是伯努利试验中$A$发生的次数，$p$是每次试验中 $A$ 发生的概率，则 $X\sim b(n,p)$

**Def**：最可能成功次数$k = \lfloor (n+1)p \rfloor~(n+1)p不是整数$

##### 泊松分布

**Def**（泊松分布）$\displaystyle P(X=k) = \frac{\lambda^ke^{-\lambda}}{k!},~X\sim P(\lambda)$

**Thm**（泊松定理）设 $\lambda >0$是一个常数，$n$ 是任意正整数，设$np_n=\lambda$。则对于任意固定的非负整数$k$有 $\displaystyle\lim_{n\rightarrow \infty}C_n^kp_n^k(1-p_n)^{n-k}=\frac{\lambda^ke^{-\lambda}}{k!}$

##### 几何分布

$\displaystyle P(X=k) = q^{k-1} p, k=1,2,\dots$

##### 超几何分布

$\displaystyle P(X=k) = \frac{C_M^k\cdot C_{N-M}^{n-k}}{C_N^n}, k = 0, 1, 2, \dots, l=\min\{n,M\}$

- $X\sim H(N,M,n)$

##### 负二项分布**

$\displaystyle P(X=k) = C_{k-1}^{r-1}p^r(1-p)^{k-r}$
- $X\sim Nb(r,p)$

#### 连续型随机变量

**Def**（连续性随机变量）$F(x) = \int_{-\infty}^xf(x)\mathrm dx,-\infty < x < \infty$
- 其中$f(x)$ 是非负可积函数，称为$X$的概率分布密度函数（概率密度函数`Probability Density Function`）
- 规范性：$\displaystyle\int_R f(x) \mathrm dx =1$
- $P(x< X \le x+\Delta x)\approx f(x)\Delta x$
- 连续性，$F(-\infty) = 0$，$F(\infty)=1$

**Def**（累积分布函数）$\displaystyle P(a<X\le b) = \int_a^bf(x)\mathrm dx$

##### 均匀分布

$$
f(x)=\begin{cases}
  \displaystyle\frac{1}{b-a},&a\le x\le b,\\
  0,&otherwise
\end{cases}\\
\\
F(x) = P(X\le x) = \begin{cases}
  0,&x < a\\
  \displaystyle\frac{x-a}{b-a}, &a\le x \le b\\
  1, &x>b
\end{cases}
$$

- $X\sim U[a,b]$

##### 指数分布

$$
f(x) = \begin{cases}
  \lambda e^{-\lambda x}, &x>0\\
  0, & x\le 0
\end{cases}
\\
F(x) = \begin{cases}
  1- e^{-\lambda x}, &x>0\\
  0, &x\le 0
\end{cases}
$$

- $X\sim e(\lambda)$

##### 正态分布

**Def**：$\displaystyle f(x) = \frac{1}{\sqrt{2\pi}\sigma}e^{-\frac{(x-\mu)^2}{2\sigma^2}}$
- $X\sim N(\mu, \sigma^2)$
- $\mu$ 为位置参数，$\sigma$ 为尺度参数
- 关于$\mu$对称，最大值
- $\sigma$固定，形状保持不变
- 拐点为：$x=\mu\pm\sigma$
- $erf(x)=F(x)= \int_{-\infty}^{x}\frac{1}{\sqrt{2\pi}}e^{-\frac{(x-\mu)^2}{2\sigma^2}}\mathrm dx$
- $3\sigma,~6\sigma$理论


**Def**（标准正态分布）$N(0,1)$

- $\mu = 0, \sigma = 1$ 的正态分布称为标准正态分布
- 密度函数和分布函数通常用 $\varphi(x),\Phi(x)$ 表示
- $\Phi(0)=0.5,~\Phi(-x) = 1-\Phi(x)$

$$
\begin{aligned}
  &\varphi(x) = \frac{1}{\sqrt{2\pi}}e^{\frac{-x^2}{2}}\\
  &\Phi(x) = \int_{-\infty}^x\varphi(x)\mathrm dx
\end{aligned}
$$

**Thm**（一般正态分布的标准化）：若$X\sim N(\mu, \sigma^2)$，则$U=\frac{X-\mu}{\sigma}\sim N(0,1)$

**Def**：（$\alpha$分位点）$P(X>\mu_\alpha) = \alpha,\quad0<\alpha<1$

### 随机变量函数的分布

#### 已知离散随机变量X的分布，求函数 Y = g(X) 的分布

$$
P(Y=y_j) = P(g(X)=y_j) = \sum_{\{x_k|g(x_k) = y_j\}}P(X=x_k), j = 1, 2, \dots,
$$

离散型均匀分布：

$$
Y = [NX+1],\quad where~X\sim U(0, 1)
$$

#### 一致连续型随机变量X的概率密度，求 g(X) 的概率密度

- **分布函数法**
- Key Point：$F_Y(y)=P(Y\le y)=P(g(x)\le y)=\displaystyle\int_{\{x|g(x)<y\}}f_X(x)\mathrm dx$

$$
Y = aX+b\Rightarrow
f_Y(y)=\frac{\mathrm d}{\mathrm dy}F_Y(y) =\begin{cases}
  \frac 1 a f_X(\frac{y-b}{a}),&a>0\\
  -\frac{1}{a} f_X(\frac{y-b}{a}),&a<0\\
\end{cases}
$$

「例」：$X\sim N(0,1),~Y=X^2$

$$
f_Y(y) = F'_Y(y) =\begin{cases}
  \frac{1}{\sqrt{2\pi y}}e^{-\frac{y}{2}},& y>0\\
  0,&y\le 0
\end{cases}
$$
