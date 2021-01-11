---
title: 「复变函数」复变函数积分
date: 2021-01-11
tags:
  - 复变函数
  - 高等数学
math: true
categories: 数学
---

## 复数项级数的概念和性质

### 复数项级数

**Def**：无穷复数列 $\{c_n\}\rightarrow_{n\rightarrow \infty} A \iff \forall \varepsilon>0,\exist N,n>N\rightarrow |c_n-A|<\varepsilon$

**Thm**（判别法则）$c_n=a_n+ib_n$ 收敛于 $a+bi~\iff~a_n\rightarrow a, b_n\rightarrow b$

**Def**（复数项级数）$\sum_{n=1}^\infty c_n$，通项 $c_n$。

**Def**（前 n 项之和）$\sum_{k=1}^n c_k$

**Thm**：（必要条件）级数 $\sum c_n$ 收敛，则 $\lim_{n\rightarrow \infty} c_n=0$

**Thm**：（柯西收敛准则）$\sum c_n$ 收敛 $\iff \forall \varepsilon>0,\exist N,\forall p\in N_+, n>N\rightarrow|S_{n+p} - S_n|\le \varepsilon$

#### 按模收敛

**Def**（按模收敛）$\sum |c_n|$

**Thm**（绝对收敛准则）当 $\sum |c_n|$ 收敛时，$\sum c_n$ 收敛

**Def**（条件收敛）$\sum |c_n|$ 不收敛，$\sum c_n$ 收敛

**性质**：

- $\sum c_n=s$，$k$为任意常数，则$\sum kc_n=k\sum c_n$
- 线性性质
- 去掉或加上有限项不改变级数的敛散性。
- 收敛级数添加括号或改变次序不改变敛散性
  - 逆命题不成立

### 幂级数

#### 函数项级数

若存在$\sum u_n(z_0)$ 收敛，则称$z_0$ 为收敛点；收敛点的全体为收敛域 $D$。

对于任一 $z\in D$，有一个确定的和 $S(z)$ 称为和函数。

如等比级数：$\sum z_n$ 当 $|z|<1$ 时，$|z|=1,~\theta = 2k\pi$ 时收敛，其他情况下发散。

#### 幂级数的收敛性

**Def**（$(z-z_0)$ 的幂级数）$\sum c_i(z-z_0)^i$

**Thm**（Abel 定理）

- 若$\sum c_i(z-z_0)^i$ 在 $z=z_0\ne 0$ 收敛，则对$\forall |z|< |z_0|$ 绝对收敛
- 若$\sum c_i(z-z_0)^i$ 在 $z=z_0\ne 0$ 发散，则对$\forall |z|> |z_0|$ 发散

**Thm**：若$\lim |c_{n+1}/c_n|=\lambda \ne 0$ or $\lim |c_n|^{1/n}=\lambda \ne 0$ 则 $R=1/\lambda$

**性质**：

1. 代数运算（线性性质）
2. 柯西乘积

#### 幂级数的收敛圆和收敛半径

仅有三种情况：

1. 在 $z=0$ 收敛
2. 在圆域内收敛
3. 在复平面内收敛

##### 求法

**Thm**：若：

$$
\begin{aligned}
&\lim_{n\rightarrow \infty}\left|\frac{c_{n+1}}{c_n}\right|=\lambda\ne 0\\
&\quad or\\
&\lim_{n\rightarrow \infty}\sqrt[n]{|c_n|}=\lambda\ne 0
\end{aligned}
$$

则其收敛半径为$\displaystyle R=\frac{1}{\lambda}$

**Thm**：设$\sum c_nz^n$的收敛半径为 $R>0$ 和函数为 $S(z)$ 则：

1. 和函数在 $|z|<R$ 解析
2. $S(z)$ 可以逐项求导、逐项积分

### Taylor 级数

**Def**（展开为幂级数）若 $f$ 在 $z_0$ 邻域内有任意阶导数，则$\sum \frac{f^{(n)}(z_0)}{n!}(z-z_0)^n$ 为 $f$ 在 $z_0$ 的 Taylor 级数，当 $z_0=0$ 时，为麦克劳林级数。

**Thm**：$f$ 在 $D$ 内解析，$z_0\in D$ 则当 $|z-z_0|<R$ 时，$f(z)$ 都可以唯一的展开为 $z-z_0$ 的幂级数。（$R$ 为 $x_0$ 到边界的最小距离）

**Thm**：$f$ 在 $D$ 内解析，$z_0\in D$，$d$为到边界上各个点的最短距离，当 $|z-z_0|<d$ 时，$f(z)$ 可以唯一的展开为幂级数

*Inference*：$f$ 在 $D$ 内解析，$z_0\in D$，$\alpha$ 为距离 $z _ 0$ 最近的一个奇点，则使得展开成立的 $R=|\alpha-z_0|$

### 洛朗级数

#### 解析函数的洛朗展开定理

**Def**（双边幂级数）$\sum_{-\infty}^{\infty}c_n(z-z_0)^n$ （其在收敛圆环域$R_1<|z-z_0|<R_2$ 内解析）

**Thm**：$f(z)$ 在圆环域内解析，则在圆域内 $f(z)$ 可以唯一的表示为双边幂级数 $f(z)=\sum_{-\infty}^{\infty}c_n(z-z_0)^n$

其中：$\displaystyle c_n=\frac{1}{2\pi i}\int\frac{f(z)}{(z-z_0)^{n+1}}\mathrm dz \quad(n=0,\pm 1, \pm 2,...)$

**求展开的方法**：

1. 直接展开法
2. 简介展开法
