---
title: 「复变函数」留数及其应用
date: 2021-01-11
tags:
  - 复变函数
  - 高等数学
math: true
categories: 数学
---

留数及其应用

<!-- more -->

## 留数及其应用

### 孤立奇点

**Def**（孤立奇点）$f(z)$ 在 $z_0$ 不解析，在其某个去心邻域内解析，则称$z_0$为 $f(z)$ 的孤立奇点

**可去奇点**：Laurent 级数不含有负幂项 -> 令 $f(z_0)=c_0$

- 只需要重新定义 $f(z_0)=c_0$ 就可以解析，例如 $(e^z-1) / z,\quad z=0$

**（m 阶）极点**：负幂项只有有限个。

- $\lim_{z\rightarrow z_0} f(z)=\infin$

**本性奇点**：负幂项有无穷多项。

**Thm**：设函数 $f(z)$ 在 $0<|z-z_0|<\delta$ 内解析，若 $z_0$ 为本性奇点，则 $\forall a,\exists\{z_n\},\lim_{z_n\rightarrow z_0}f(z_0) = a$

#### 零点和极点的关系

**Def**（零点）$f(z_0)=0$ 则称 $z_0$ 为 $f(z_0)$ 的零点

**Def**（m 级零点）若 $f(z)=(z-_0)^m\varphi(z)$ 在 $z_0$ 处解析，且 $\varphi(z)$ 在 $z_0$ 处解析 $\varphi(z_0)\ne0$ 则称 $z_0$ 为 $f(z)$ 的 m 级零点

**Thm**：若 $f$ 在 $z_0$ 解析，则： $z_0$ 为 m 阶零点 $\iff f^{(n)}(z_0)=0, (n < m)~,f^{(m)}\ne 0$

**Thm**：若 $z_0$ 是 $f(z)$ 的 m 阶极点 $\iff$ $z_0$ 是 $1/f(z)$ 的 m 阶零点。

**Thm**：若 $z_0$ 为 $f,g$ 的 $m, n (m<n)$ 级零点，则 $z_0$ 为 $f(z)/g(z)$ 的 $m - n$ 阶零点，为 $f(z)g(z)$ 的 $m+n$ 阶零点。

#### 在无穷远点的形态

**Def**：若 $f(z)$ 在无穷远点$z=\infin$ 的去心邻域 $U(\infty)=\{z|0<R<|z|<\infty\}$ 内解析，则称 $\infin$ 为 f 的孤立奇点。

**Def**：若 $t=0$ 是 $\displaystyle\varphi(t)=f(\frac 1 t)$ 的可去奇点，m 级极点，本性极点，则 $t=\infin$ 是 $f(z)$ 的可去奇点，m 级极点，本性极点。

### 留数和留数定理

**Def**（留数）设$z_0$为 $f(z)$ 的有限孤立奇点，我们把 $f(z)$ 在 $z_0$ 的去心邻域内的洛朗级数展开式两端逐项积分留下的积分值除以 $2\pi i$ 后得到的数称为 $f(z)$ 在 $z_0$ 的留数：$\mathrm{Res}[f(z),z_0]=\frac{1}{2\pi i}\oint f(z) dz=c_{-1}$

**Def**（无穷远处的留数）$Res[f(z),+\infin]=\frac{1}{2\pi i}\oint_{L-}f(z)=-C_{-1}$（f 在圆环域 $0<R<|z|<\infin$ 解析）

*留数计算方法*：

1. 若 $z_0$ 为可去奇点：$Res[f,z_0]=c_{-1}=0$
2. 1 级极点：$Res[f,z_0]=\lim_{z\rightarrow z_0}(z-z_0)f(z)$
3. m 级极点：$Res[f,z_0]=\frac{1}{(m-1)!}]\lim_{z-z_0}\frac{\mathrm d^{m-1}}{\mathrm dz^{m-1}}[(z-z_0)^mf(z)]$
4. 若 $f(z)=P(z)/Q(z)$，$P,Q$ 解析，且 $P(z_0)\ne 0,~Q(z_0) = 0,~Q'(z_0)\ne 0$ 则 $\displaystyle Res=\frac{P(z_0)}{Q'(z_0)}$
5. $\displaystyle Res[f(z),\infty]=-Res[-\frac{1}{z^2}f(\frac{1}{z}),0 ]$

**Thm**（留数定理）设函数 $f(z)$ 在 $D$ 内除了有限个孤立奇点外处处解析，$L$是$D$ 内的一个逆时针的简单闭曲线，则$\displaystyle\oint f(z)\mathrm dz =2\pi i\sum_{k=1}^m\mathrm{Res}[f(z),z_k]$

**Thm**：若函数$f(z)$ 在扩充复平面内处有限个孤立奇点外解析，则 $f(z)$ 在各个极点的留数和为 0：$\displaystyle\mathrm{Res}[f(z),+\infin]+\sum\mathrm{Res}[f(z),z_k]=0$

### 利用留数计算某些实积分

#### ∫R(cos θ, sin θ) dθ

设 $z=e^{i\theta}$ 则：

$$
\oint_{0}^{2\pi}R(\cos \theta,\sin\theta)\mathrm d\theta=\oint_{|z|=1}\frac{1}{iz}R(\frac{z+z^{-1}}{2},\frac{z-z^{-1}}{2i})\mathrm dz
$$

#### ∫R(x) dx

其中

$$
R(x)=\frac{P_m(x)}{Q_n(x)}=\frac{a_0+a_1x+\cdots+a_mx^m}{b_0+b_1x+\cdots+b_nx^n}
$$

满足：

- $n-m\ge2$
- 在实轴上$Q_n(z)\ne 0$

则：

$$
\int_{-\infty}^{\infty}R(x)\mathrm dx =2\pi i\sum Res[R(z),z_k]
$$

其中 $z_k$ 为上半平面内所有奇点

#### ∫ R(x) · exp(i·a·x) dx

$$
R=P(x)/Q(x)
$$

其中 $m-n\ge 1,Q(x)\ne 0$

则：

$$
\int_{-\infty}^{\infty}R(x)e^{iax}\mathrm dx = 2\pi i\sum Res(R(z)e^{iax},z_k)
$$

其中 $z_k$ 为上半平面内所有奇点

也就是：
$$
\int_{-\infty}^{\infty}R(x)\cos ax\mathrm dx+i\int_{-\infty}^{\infty}R(x)\sin ax\mathrm dx = 2\pi i\sum Res(R(z)e^{iax},z_k)
$$