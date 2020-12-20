---
title: 「复变函数」复变函数积分
date: 2020-11-20
tags:
  - 复变函数
  - 高等数学
math: true
categories: 数学
---

复变函数的积分

<!-- more -->

# Ch3 复变函数的积分

### 复变函数积分的概念及其计算

##### 定义

- **Def**：同实函数定义：分割求和 $\displaystyle\int_C f(z)\mathrm dz = \lim \limits_{\delta \rightarrow 0}\sum f(\gamma_k)\delta z_k$

- 对应了两个实函数第二型曲线积分

- 性质：
  
  - $\displaystyle\int_Lf\mathrm dz=\int_{L_1}f\mathrm dz+\int_{L_2}f(z)\mathrm dz$
  - 方向性
  - 线性性质
  - $\displaystyle|\int_Lf\mathrm dz| \le \int_L|f||\mathrm dz|\le MS$

##### 计算方法1：**参数方程法**

- $\displaystyle let~z=x(t) + iy(t)\rightarrow \int_Lf\mathrm dz=\int f(z(t)) z'(t)\mathrm dt$

- 例：
  $$\displaystyle\oint_L\frac{1}{(z-z_0)^n}\mathrm dz= \begin{cases}2\pi i,&n=1,\\0,&n\ne 1.\end{cases}$$
  其中 $L$ 为圆
  利用：$z-z_0=\rho\cdot e^{i\theta}$，并且注意方向！（$\theta$的积分方向上）

### Cauchy 积分定理

- 若 $f(z) = u(x,y)+iv(x,y)$在单连通域 $D$ 内解析，$f'$ 连续且$u,v$ 有一节连续偏导数，满足 $C-R$ 方程。则对于任一分段光滑的简单闭曲线 $L_1$：$\displaystyle \int _{L_1} f(z)\mathrm dz = 0$
- $f(z)$ 在单连通域 $D$ 内解析，$f'$ 在 $D$ 内连续时，复积分 $\displaystyle \int _Lf(z)\mathrm dz$ 与路径无关

##### 柯西-古萨基本定理

- **Thm**：设 $f(z)$ 在简单闭曲线 $L$ 上以及它所围的区域 $D$ 内解析，则$\displaystyle \int _{L} f(z)\mathrm dz = 0$
- **Thm**：设 $f(z)$ 在单连通域 $D$ 内解析，对于 $D$ 内任一分段光滑的闭曲线 $L_1$：$\displaystyle \int _{L_1} f(z)\mathrm dz = 0$
- **Thm**：（复合闭路定理）设 $L, L_k$ 为n+1条取逆时针方向的简单闭曲线，$L_k$ 互不相交，互不包含，$L, L_k$ 围成复连通域$D$，$f(z)$ 在$\bar D$ 上解析，则：
  $$\displaystyle\oint_Lf(z)\mathrm dz = \sum_{k=1}^n\oint_{L_k}f(z) \mathrm dz$$

> 注意曲线的性质：简单闭曲线、闭曲线

##### 例

$$\displaystyle\oint_L\frac{1}{(z-z_0)^n}\mathrm dz= \begin{cases}2\pi i,&n=1,\\0,&n\ne 1.\end{cases}$$

其中 $L$ 为圆

> 利用：$z-z_0=\rho\cdot e^{i\theta}$，并且注意方向！（$\theta$的积分方向上）

利用复合闭路定理：$L$ 可以为任意包含$z_0$的闭曲线。

- **Thm**：闭路变形定理

重要结论：

$$
\oint_L\frac{1}{(z-z_0)^n}\mathrm dz= \begin{cases}2\pi i,&n=1,\\0,&n\ne 1,n\in \mathrm Z.\end{cases}
$$

##### review：2020/11/06 星期五

> - $\int_Lf\mathrm dz=0$
> - $\int_Lf\mathrm dz=\sum\int_{L_k}f\mathrm dz$
> - $\int \frac{1}{(z-z_0)^{n}}\mathrm dz$
> - $|z| = 1\Rightarrow|\mathrm dz|=|e^{i\theta}i\mathrm d\theta|=d\theta=\frac{1}{iz}\mathrm dz$

### 原函数与不定积分

- **Thm**：设 $f(z)$ 在单连通域 $D$ 内解析，则复函数 $F(z)=\int_{z_0}^zf(z)\mathrm dz$ 在 $D$ 内解析，且 $F'=f$
- **Def**：（原函数）若存在$\Phi(z),\forall z\in D,\Phi '(z)=f(z)$ 称 $\Phi(z)$ 为 $f(z)$ 在 $D$ 内的一个原函数

##### 性质

1. 单连通域 $D$ 内的解析函数存在原函数

2. 表示全体原函数的表达式：$\int f(z)\mathrm dz$称为$f$的不定积分
- **Thm**：对于解析函数 $f$，$\Phi(z)$ 是其原函数，则$\int_{z_1}^{z_2}=\Phi(z_2)-\Phi(z_1)$

### 柯西积分公式、高阶导数公式

- **Thm**：（Cauchy积分公式）$f(z)$ 在 $D$ 和 $D$ 的边界上解析，则 $\forall z\in D, f(z) = \frac{1}{2\pi i}\oint_L\frac{f(\varsigma)}{\varsigma - z}\mathrm d \varsigma$

> $\displaystyle L:|z-z_0|=R\Rightarrow f(z_0) = \frac{1}{2\pi}\int_0^{2\pi}f(z_0+Re^{i\theta})\mathrm d\theta$

##### 高阶导数公式

- 设 $f$ 在 $D$ 及其边界上解析，则$f$在D内有任意阶导数，且$\forall z\in D$,
  $\displaystyle f^{(n)}(z) = \frac{n!}{2\pi i}\oint_L\frac{f(\varsigma)}{(\varsigma-z)^{n+1}}\mathrm d\varsigma$

##### Thms

- **Thm**（柯西不等式）设 $f$ 在 $D$ 内解析，$z_0\in D$，圆周 $K_R$ 及其内部均含于 $D$，则$|f^{(n)}(z_0)|\le \frac{n! M(R)}{R^n}$，$M(R) = \max_{|z-z_0|=R}|f(z)|$

- **Thm**（柳维尔定理）$f(z)$ 在整个复平面上解析且有界，则 $f(z)$ 在复平面上恒为常数。

- **Thm**（莫雷拉定理）$f(z)$ 在单连通区域 $D$ 内解析且有界，，且对于任一简单闭曲线$L$上：$\int_Lf(z)\mathrm dz =0$，则$f(z)$ 在 $D$ 内解析。