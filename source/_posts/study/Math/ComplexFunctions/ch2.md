---
title: 「复变函数」复变函数的导数和解析函数
date: 2020-11-20
tags:
  - 复变函数
  - 高等数学
math: true
categories: 数学
---

复变函数的导数和解析函数
<!-- more -->

## Ch2 复变函数的导数和解析函数

### 解析函数的概念及其判定

#### 复变函数的导数、微分

**Def**：复变函数的导数、可导、在 D 内可导

求导公式：有理运算求导、反函数求导

**复变函数的可微性**：

**Def**（可微）$\mathrm dw=f'(z_0)\Delta z$

**Thm**：可微 $\iff$ 可导

**Thm**（可导的必要条件）C-R 方程：

$$
\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y},
\frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x},
$$

**Thm**（可导的充要条件）

1. $u,~v$ 在$(x,y)$可微
2. $u,~v$ 在$(x,y)$满足 C-R 方程

#### 解析函数

**Def**（解析、在区域D内解析）在 $z_0\in C$ 及其某个邻域内处处可导-->解析

**Thm** 设函数 $f(z)=u(x,y)+iv(x,y)$ 定义在区域 D 内，若它的任意一点 $z\in D$ 可导，则必有

1. $u,v$ 偏导数在 $(x,y)$ 出存在
2. 满足 C-R 方程

*Inference*：在上述定理的条件下，$f(z)$ 在点 $z$ 处的导数为

$$
f'(z)=\frac{\partial u}{\partial x}+i\frac{\partial v}{\partial x}=
\frac{1}{i}\frac{\partial u}{\partial y} + \frac{\partial v}{\partial y}
$$

**Thm**：在区域 D 内解析 $\iff$

1. $u,~v$ 在 D 可微
2. $u,~v$ 在 D 内任一点处满足 C-R 条件

##### 解析函数和调和函数

> 若二元实函数在D内由二阶连续偏导数，且满足Laplace方程$\displaystyle\frac{\partial^2\varphi}{\partial x^2}+\frac{\partial^2\varphi}{\partial y^2} = 0$，则称其为D内的调和函数。

**Thm**：$f$解析，则$u,~v$ 是 D 内的调和函数

**Def**（共轭调和函数）解析函数的虚部 $v$ 称为实部 $u$ 的共轭调和函数。

> $f = v+iu$不一定解析。

### 基本初等函数

#### 指数函数

$\displaystyle w = e^z = e^x(\cos y + i \sin y)$

**性质**：

- $|e^z| = e^x, Arg~e^z = y+2k\pi$
- 加法定理：$e^{z_1}e^{z_2}=e^{z_1+z_2}$
- 周期性：$e^{z+2k\pi i} = e^z$
- 处处解析：$(e^z)'=e^z$

{% note primary %}

1. $y = 0\Rightarrow w = e^x$
2. $x = 0\Rightarrow w = e^{iy}=\cos y+i\sin y$

{% endnote %}

#### 对数函数

$\displaystyle w=\mathrm{Ln} z = \ln |z| + i \mathrm{Arg}z =\ln |z| + i (\mathrm{arg}z + 2k\pi)$

**性质**：

- $\mathrm{Ln}z$ 为无穷多值函数
- $\mathrm{Ln}(-1) = (2k+1)\pi i$
- 运算同 $\ln$
- 解析性：除**原点**和**负实轴**外的其他点处解析
- （对数函数）主值：$\ln z$

**连续（解析）分支**：使得其成为连续（解析）函数。

> 这里就是选取一个合适的 $k$

#### 幂函数

$w = z^\alpha = e^{a\mathrm{Ln} z}$

- 可能是多值函数：考虑$\alpha$对于$\mathrm{Ln}z = \ln|z| +i(\arg~z+2k\pi)$ 中 $k$ 的影响
  - $\alpha$ 是整数：单值函数
  - $\alpha = p/q$ 是有理数：取$k = 0,1,2,\dots,q-1$的$q$个值
  - 其他：无穷多个
  - $\mathrm{Ln}z = \ln z$ 时，$z^\alpha = e^{\alpha \ln z}$ 称为（幂函数的）主值
- 解析性：除**原点**和**负实轴**外的其他点处解析

#### 三角函数

$\sin z = \frac{e^{iz}-e^{iz}}{2i},\qquad\cos z = \frac{e^{iz}+e^{-iz}}{2}$

- 以 $2\pi$ 为周期
- 三角恒等式成立
- 在复平面上处处解析
- 没有有界性
- 复数的欧拉公式 $e^{iz} = \cos z + i\sin z$ 成立
- $\sin z$ 的零点为 $z= k\pi$ $\cos z$ 的零点为 $z = k\pi + \frac{\pi}{2}$

#### 双曲函数

$\sh z=\frac{e^z-e^{-z}}{2},\qquad\ch z=\frac{e^z+e^{-z}}{2}$

- 周期性、奇偶性、解析性

#### 反三角函数、反双曲函数

$$
\begin{cases}
\mathrm{Arccos}~z =-i\mathrm{Ln}(z+\sqrt{z^2-1})\\
\mathrm{Arcsin}~z =-i\mathrm{Ln}(iz+\sqrt{1-z^2})\\
\mathrm{Arch}~z =\mathrm{Ln}(z+\sqrt{z^2+1})\\
\mathrm{Arsh}~z =\mathrm{Ln}(z+\sqrt{z^2-1})\\
\end{cases}
$$
