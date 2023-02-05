---
title: 「概率统计与随机过程」 3 - 随机向量及其概率分布
date: 2020-11-18
categories: Mathematics
tags:
  - 概率论
math: true
plugins:
  - mathjax
  - katex
hide: false
group: group-probabilites
sidebar: [group-probabilites, toc]
---

随机向量及其概率分布

<!-- more -->

## 随机向量及其概率分布

### 二维随机向量的联合分布

**Def**（二维随机向量）假设 $\Omega = \{\omega\}$ 是随机试验 E 的样本空间，$X(\omega),~Y(\omega)$ 是定义在$\Omega$ 上的两个随机变量，由他们构成一个二维向量$(X,Y)$称为随机试验 E 的一个二维向量。

**Def**（二维随机变量的联合分布函数）假设$(X,Y)$是二维随机向量，对于任意实数$x,y$，二元函数$F(x,y)=P(X\le x,Y\le y)$ 称为二维随机向量$(X,Y)$ 的联合分布函数（分布函数）。

*联合分布函数的性质*：

1. $0\le F\le 1$
2. $F$ 是变量 $x,~y$ 的不降函数。
3. 右连续性
4. $\forall x_1<x_2, y_ 1 < y _ 2:~P(x\\_1\le X \le x\\_2,y\\_1\le X \le y\\_2) = F(x\\_2,y\\_2) +F(x\\_1, y\\_1) - F(x\\_1,y\\_2) - F(x\\_2, y\\_1)\ge0$

#### 二维离散型随机向量

**Def**（二维离散型随机向量）若随机向量 $(X,Y)$ 最多取可列无穷多个点 $(x_i, y_j), i, j\in \mathrm N$，则称 $P(X=x_i,Y=y_j)=p_{ij}$ 为 $(X,Y)$ 的联合分布律。

*表格表示*：

|X\\Y|y1|...|
|---|---|---|
|x1| p11|...|
|...|...|...|

**Def**（离散型随机向量的联合分布律）$F(x,y) = \sum_{y_j\le y} \sum_{x_j\le x} p_{ij}$

- $p_{ij}\ge 0$
- $\sum_{j=1}^\infty \sum p{ij}=1$

#### 二维随机连续向量

**Def**（连续型随机向量）$F(x,y)$ 是二维随机向量$(X, Y)$ 的联合分布函数，若存在非负可积函数 $f(x,y)$ ，有 $F(x,y)=\int_{-\infty}^y\int_{-\infty}^0$ 则称$(X,Y)$ 的二维连续型随机向量，$f(x,y)$ 称为概率密度函数（`PDF`）

*相关性质*：
1. 非负性
2. 规范性
3. $f(x,y) =\frac{\partial^2}{\partial x\partial y}F(x,y)$
4. $P((X,Y)\in G) = \iint_G f\mathrm dx \mathrm dy$

#### 二维连续型随机向量

**Def**（二维连续型随机向量的联合概率密度函数）设 $F(x,y)$ 是二维随机向量 $(X,Y)$ 的联合分布函数，若存在非负可积函数 $f(x,y)$ 有，$F(x,y)=\int\int f(x,y)dxdy$ 则称 $(X,Y)$ 为二维连续性随机向量 $f$ 为密度函数

*例*：

1. 二维均匀分布：
   - 面积为 $A$ 若 $(X,Y)$ 具有概率密度：$f(x,y) = 1/A~if~(x,y)\in G~else~0$
2. 二维正态分布

$$f(x,y) = \frac{1}{2\pi \sigma_1\sigma_1\sqrt{1-\rho^2}}\exp\{-\frac{1}{2(1-\rho^2)}[\frac{(x-\mu_1)^2}{\sigma_1^2}-2\rho\frac{(x-\mu_1)(y-\mu_2)}{\sigma_1\sigma_2}+\frac{(y-\mu)2)^2}{\sigma_2^2}  ]\}$$

### 边缘分布

**Def**（边缘分布函数）假设二维随机向量$(X,Y)$ 的联合概率分布函数 $F(x,y)$，令$F_1(x) = F(x,+\infty),F_2(y) = F(+\infty, y)$为关于 $X$ 和 $Y$ 的边缘分布函数

**Thm**：二维随机向量的联合分布函数为 $F(x,y)$，分布函数为 $F_X, F_Y$，则 $F_X(x) = F_1(x),~F_Y(y) = F_2(y)$

#### *离散型*-边缘分布律

：

- $\displaystyle F_X(x) = \sum_{x_i\le x}\sum p_{ij}$
- $P(X = x_i) = \sum_{j=1}^\infty p_{ij},~P(X = x_j) = \sum_{i=1}^\infty p_{ij}$
- $p_{i\cdot}=P(X=x_i),~p_{\cdot j}=P(Y=y_j)$

#### *连续型*-边缘分布密度

> 根据 $F_X(x) = F(x, +\infty) = \int_{-\infty}^x\int_{-\infty}^{+\infty}f(x,y)\mathrm dy\mathrm dx=\int_{-\infty}^{x}f_1(x)\mathrm dx$

- $f_X(x) = \int_{-\infty}^\infty f(x,y)\mathrm dy$
- $f_Y(Y) = \int_{-\infty}^\infty f(x,y)\mathrm dx$

### 条件概率

**Def**：(条件分布函数）假设$X,~Y$ 是两个随机变量，

- 若对于固定的 $x$ 有 $P(X=x)\ge 0$ 则对于任意的 $y\in R$ 称：$P(Y\le y|X=x)=\frac{P(X=x, Y\le y)}{P(X = x)}$ 为 $X = x$ 条件下，$Y$ 的条件分布函数，记为 $F_{Y|X}(y|x)$

- 若对于固定的 $y$ 有 $P(Y=y)\ge 0$ 则对于任意的 $x\in R$ 称：$P(X\le x|Y=y)=\frac{P(Y=y, X\le x)}{P(Y = y)}$ 为 $Y = y$ 条件下，$X$ 的条件分布函数，记为 $F_{Y|X}(x|y)$

*连续型随机变量的条件分布函数*：对于连续型随机变量，考虑极限：

- $\displaystyle\lim_{\Delta x\rightarrow 0}\frac{P(x-\Delta x< X\le x,Y\le y)}{P(x-\Delta x < X\le x)}=\frac{\int_{-\infty}^yf(x,y)\mathrm dy}{f_X(x)}~-\infty < y < +\infty$


#### 离散型随机变量的条件分布律

设 $(X,Y)$ 是二维离散型随机变量，联合分布律为$P(X=x_i,Y=y_j)=p_{ij},~i,j=1,2,\dots$

- 可知：$P(Y=y_j|X=x_i)=\displaystyle\frac{p_{ij}}{p_{i\cdot}}$

- 类似地，条件分布律为：$\displaystyle F_{Y|X} (y|x) = \frac{\sum_{y_j\le y}P_{ij}}{p_{i\cdot}}$

##### 连续型随机变量的条件分布、条件分布密度

设二维连续型随机变量$(X,Y)$ 的连续概率密度函数为$f(x,y)$ 对于固定的 $x$，$(X,Y)$ 关于边缘概率密度 $f_X(x)>0$ 则在$X=x$条件下，$Y$ 的*条件分布函数*：

- $\displaystyle\lim_{\Delta x\rightarrow 0}\frac{P(x-\Delta x< X\le x,Y\le y)}{P(x-\Delta x < X\le x)}=\frac{\int_{-\infty}^yf(x,y)\mathrm dy}{f_X(x)}=\int_{-\infty}^y\frac{f(x,y)}{f_X(x)}\mathrm dy=\int_{-\infty}^yf_{Y|X}(y|x)\mathrm dy$

则，*条件分布密度*为：

$$
\displaystyle f_{X|Y}(x|y)=\frac{f(x,y)}{f_Y(y)}\\
\displaystyle f_{Y|X}(y|x)=\frac{f(x,y)}{f_X(x)}
$$

- 类似于*乘法公式*：$f_{X,Y}(x,y)=f_Y(y)f_{X|Y}(x|y)$

### 随机变量的独立性

> 随机变量 X Y 独立是指：与 X 相关的任一事件发生与否与 Y 有关的任一事件发生与否无关。

**Def**（随机变量间的独立性）设随机向量的联合分布函数为$F(x,y)$，而$F_X(x),F_Y(y)$ 分别为随机变量 X, Y 的分布函数，若 $\forall (x,y)\in R^2, F(x,y)=F_X(x)F_Y(y)$ 则 X Y 相互独立

**Thm**：若$(X,Y)$ 为二维离散型随机向量，其联合分布律为：$P(X=x_i,Y=y_i)=p_{ij}$ 则 X Y 相互独立的充要条件是 $\forall (x_i,y_i),p_{ij}=P(X=x_i)P(Y=y_j)$

**Thm**：若$(X,Y)$ 为二维连续型随机向量，其联合概率密度函数为：$f(x,y)$ 则 X Y 相互独立的充要条件是 $\forall (x,y),f(x,y) = f_X(x)f_Y(y)$

##### 例

1. 正态变量 $(X,Y)\sim N(\mu_1,\mu_2,\sigma_1^2,\sigma_2^2,\rho)$
  - $\rho$：相关系数
  - 独立 $\iff\rho=0$
2. 矩形区域的均匀分布 → 独立
3. 若联合密度 $f(x,y)$ 可分离变量，即 $f(x,y)=g(x)h(y)$ 且定义域互不影响，则 $X$ 与 $Y$ 相互独立。
4. 独立 → 条件分布与边缘分布相同。

### n 维随机向量

**Def**（联合分布）n维随机向量的联合分布

**Def**（概率分布律）

**Def**（联合概率密度函数）$F=\int\int\dots\int f$

- **Thm**：规范性

**Def**（k维边缘分布）$F_{X_1,..,X_k}=F(X_1, ..,X_k,+\infty,+\infty,...,+\infty)$

- **Def**（1维边缘分布、密度函数）

**Def**（条件分布）

**Def**（n维随机向量的独立性）$F(x_1,x_2,...,x_n)=\Pi F_{X_i}$

**Def**（独立性）X，Y独立，则$\bar X,S^2, \bar Y,S^2$独立

### 随机向量函数的分布

> 课程中主要考虑：
>
> - $Z=g(X,Y)=X+Y$
> - $Z=XY$
> - $Z=Z/Y$
> - $Z=\min\{X,Y\}~(or~\max\{X,Y\})$
> - $Z=\sqrt{X^2+Y^2}$

#### 二维离散型随机向量函数的分布

$$
P(Z=z_k)=\sum_{Z=z_k}P(X=x_i,Y=y_i)
$$

例如，*一些分布的可加性*：

- $X\sim P(\lambda_1),Y\sim P(\lambda_2)$ 且独立，则 $X+Y\sim P(\lambda_1+\lambda_2)$

- $X\sim b(n,p),Y\sim b(m,p)$ 且独立，则 $X+Y\sim b(n+m,p)$

**Thm**（离散场合的卷积公式）通常的：X，Y 独立，则对于$Z=X+Y$，有$\displaystyle P(Z=z_i)=\sum_{j=1}^\infty P(x=z_j-y_j)P(Y=y_j)$


#### 二维连续型随机向量函数的分布密度

> *review*: $x\sim f(x)$ 求 $Y=h(X)$ 密度：$F_X(y)=P(h(x)\le y) = \int f(y)\mathrm dy$
>
> *solution*: $F_Z(z)=P(Z\le z)=\iint_{g(x,y)\le z} f(x,y)\mathrm dx\mathrm dy$

##### z=x+y

$$
\begin{aligned}
F(z)&=P(X+Y\le Z)&\\
&=\int_{-\infty}^{+\infty}\int^{z-y}_{-\infty} f(x,y)\mathrm dx\mathrm dy\\
\Rightarrow\qquad&
p(z) = \int_{-\infty}^{+\infty} p(x,z-x)\mathrm dx = \int_{-\infty}^{+\infty} p(z-y, y)\mathrm dy
\end{aligned}
$$

**Thm**（卷积公式）X，Y 相互独立，则对于$Z=X+Y$：$p_Z(z)=\int_{-\infty}^{+\infty}p(x)p(z-x)\mathrm dx=\int_{-\infty}^{+\infty}p(z-y)p(y)\mathrm dy$

- 正态分布具有可加性：$X_1\sim N(\mu_1, \sigma_1), X_2\sim N(\mu_2,\sigma_2),...$ 则 $\sum c_iX_i\sim N(\sum c_i\mu_i,\sum c_i^2\sigma_i^2)$

- $\Gamma$ 函数与卡方分布 $X\sim\chi(n) = P(n/2, 1/2)$，$x_1...x_n~\sim N(0,1)$，$\sum x_i^2\sim \chi(n)$
  - $X,Y\sim \Gamma(\alpha_{1,2},\beta)\rightarrow X+Y\sim\Gamma(\alpha_1+\alpha_2,\beta)$

***一般步骤***

1. 先求出分布函数
2. 关于 z 求导数得到结果

##### 最大值最小值函数

*相互独立情况下*：

$$
\begin{aligned}
  &N=\min\{X_i\}, M = \max\{X_i\}\\
  &F_{\min}(z)=1-\Pi[1-F_{X_i}(z)]\\
  &F_{\max}(z)=\Pi F_{X_i}(z)
\end{aligned}
$$

*独立同分布的情况下*：

$$
\begin{aligned}
  &F_{\min}(z)=1-[1-F(z)]^n\\
  &F_{\max}(z)=F(z)^n\\
  &f_{\min}(z) =n[1-F(z)]^{n-1} f(z)\\
  &f_{\max}(z) =nF(z)^{n-1} f(z)
\end{aligned}
$$
