---
title: 「复变函数」
date: 2020-11-20
tags:
  - 复变函数
math: true
categories: 数学
---

复数与复变函数

<!-- more -->


## Ch1 复数与复变函数

### 复数的概念与运算

#### 复数的概念

**Def**（复数）$(x,y)$ -> $z=x+iy,i^2=-1$

1. $\mathrm{Re}(z)$
2. $\mathrm{Im}(z)$
3. 相等：实部虚部对应相等

##### 复数的代数运算

1. 加减
2. 乘除

满足的运算规律：

1. 交换
2. 结合
3. 分配

##### 共轭复数

$\bar z = x - iy$

**共轭复数的性质**：

1. $z \bar z = |z|$
2. $\overline{z_1\pm z_2} = \bar{z_1}\pm\bar{z_2}$
3. $\overline{z_1z_2} = \bar{z_1}\bar{z_2}$
4. $z+\bar z = \mathrm{Re}(z)$
5. $(z-\bar z)/i = \mathrm{Im}(z)$

#### 复数的几何表示

1. 点表示：$z=x+iy\leftrightarrow (x,y)$
   复平面、实轴、虚轴

2. 向量表示

3. 三角表达：$z=r(\cos\theta+i\sin \theta)$

##### 复数的模和辐角

1. 模 $|z| = r = \sqrt{x^2+y^2}$
2. 辐角 $\mathrm{Arg}~z = \theta$

> 利用欧拉公式：
>
> - $z = re^{i\theta}$
>
> $z = 0$ 辐角不确定
>
> 辐角的主值 $-\pi<\theta_0\le\pi$

辐角主值计算：

1. 求 $\arctan \frac y x$
2. 求 $\theta_0$，注意：$\theta_0\in(-\pi,\pi]$

{% noteblock quote %}

- $\mathrm{Arg}(z_1z_2)=\mathrm{Arg}z_1+\mathrm{Arg}z_2$
- $\mathrm{Arg}(z_1/z_2)=\mathrm{Arg}z_1-\mathrm{Arg}z_2$

注意这里指的是集合相等

- $|z_1z_2|=|z_1||z_2|$
- $|z_1/z_2|=|z_1|/|z_2|$

{% endnoteblock %}

#### 复数的乘幂和方根

##### 复数的乘幂

$$
\begin{aligned}
&z=re^{i\theta} = r(\cos\theta+i\sin\theta)\\
&z^n = z\cdot z\cdot z\cdot\dots\cdot z\\
&z^n=re^{in\theta}=r(\cos n\theta+i\sin n\theta)
\end{aligned}
$$

**Thm**（棣莫弗公式）$|z|=r=1$ 时：$(\cos \theta+i\sin \theta)^n=\cos n\theta + i \sin n\theta$

##### 复数的方根

$$
\begin{aligned}
&z=re^{i\theta} = r(\cos\theta+i\sin\theta)\\
&\sqrt[n]z= \sqrt[n]r(\cos\frac{\theta + 2k\pi}n+i\sin\frac{\theta + 2k\pi}n)\\
\end{aligned}
$$

#### 复数在几何上的应用举例

{% noteblock quote %}

求解：$z^n=1$

{% endnoteblock %}

{% noteblock quote %}

复数表示复平面上的过$z_1,~z_2$的直线方程：$z-z_1=t(z_2-z_1)$

{% endnoteblock %}

{% noteblock quote %}

复数表示圆方程：$|z-z_0| = R$

{% endnoteblock %}

{% noteblock quote %}

1. 中垂线：$|z-z_1|=|z-z_2|$
2. 特殊直线：$\mathrm{Im}(i+z)=4$

{% endnoteblock %}

#### 复球面与无穷远点

- 引入无穷远点，表达复数：扩充复平面

## 复变函数的极限与连续性

### 复平面上的区域

#### 区域的概念

**Def**（开集）所有点都是集合的内点

**Def**（区域）连通的开集

> 开集：$\forall z\in A,\exists U(z)\subset A$，即$\mathrm{int}A = A$
>
> - 内点、外点、边界点
>   连通：折线连接
> - 单连通、复连通（用闭曲线包围部分是否都在原集合内定义）
>
> $z_0$ 的 $\delta$ 邻域
>
> 去心邻域
>
> 同理定义 $\infin$的邻域和去心邻域

##### 简单曲线、单连通、多连通

**简单曲线**：

- 连续
- 导函数连续，且 $(x')^2+(y')^2 \ne 0$
- 不相交（没有重点）：$t_1=t_2\Leftrightarrow z(t_1)=z(t_2)$

**连通区域**：

- 单连通
- 多连通

#### 复变函数的概念

**Def**（复变函数）*可以是多值的*

- 映射下的象和原象
- 复变函数的集合表示

### 复变函数的极限和连续性

**Def**（极限）

**Thm**：设$f$在$z_0$的某个去心领域有定义，则：

$$
\lim f(z) = A\iff \begin{cases}
   \lim u = \mathrm{Re}(A)\\
   \lim v = \mathrm{Im}(A)
\end{cases}
$$

极限的性质：

- 唯一性
- 局部有界性
- 有理运算法则

**Def**（连续、在区域内连续）

**Thm**：$f$ 在 $z_0$ 连续. $\iff$ $u$，$v$ 在 $(x_0,y_0)$ 同时连续

- 有理运算不改变连续性
- 函数复合不改变连续性
