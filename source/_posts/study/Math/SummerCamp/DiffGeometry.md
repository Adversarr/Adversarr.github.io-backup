---
title: 面向夏令营的微分几何整理
categories: 数学
tags:
  - 微分几何
  - 数学
  - 夏令营

plugins:
  - mathjax
mathjax: true
hide: false
group: group-adv-math
sidebar: [group-adv-math, toc]
---

*待完善*

<!-- more -->

TODO

## 测地曲率和测地线

根据 Gauss 绝妙定理，$K$ 只决定于曲面的第一基本形式，在保长对应下不变， 是曲面的内蕴性质。在这里继续研究曲面内蕴几何的主要研究对象。

### 测地曲率和测地线

我们考虑正则曲面$S:\mathbf r = \mathbf r(u^1, u^2)$，设有曲线$u^\alpha = u^\alpha (s)$ 是一条弧长参数曲线。其作为空间中的曲线参数方程为：
$$
\mathbf r = \mathbf r(s) = \mathbf r (u^1, u^2)
$$
建立新的正交标架：
$$
\begin{aligned}
\mathbf e_1  &= \frac {d\mathbf r(s)}{ds} = \alpha(s)\\
\mathbf e_2 &= \mathbf n(s)\times \alpha(s) \\
\mathbf  e_3 &= \mathbf n(s)
\end{aligned}
$$
对于该曲线来考察原曲面的性质：
$$
\begin{cases}
\frac{d\mathbf r}{ds} &= \mathbf e_1&\\
\frac{d\mathbf e_1}{ds} &= & +\kappa _g\mathbf e_2 & + \kappa_n\mathbf e_3\\
\frac{d\mathbf e_2}{ds} &= -\kappa_g\mathbf e_1 &&+\tau_g \mathbf e_3 \\
\frac{d\mathbf e_3}{ds} &= -\kappa_n \mathbf e_1 & +\tau_g \mathbf e_2\\
\end{cases}
$$
显然，式中的：

- $\kappa_n$ 就是曲面$S$沿着曲线$C$的切方向的法曲率；

而也可以求解出其他的参数：
$$
\kappa_g = \left( \mathbf n, \mathbf r', \mathbf r'' \right)
$$
是曲面上曲线 $C$ 的**测地曲率**；
$$
\tau_g = \left( \mathbf n, \mathbf n',\mathbf r'\right)
$$
是曲面上曲线 $C$ 的**测地挠率**。

下面的定理描述了测地曲率和测地挠率的几何意义：

**Theo**
: 设 $C$ 是曲面 $S$ 上的一条正则曲线，其在 $p$ 处的测地曲率等于将其投影到切平面上的曲线的相对曲率，其平面的正向由曲面 $S$ 在点 $p$ 的法向量给出。

**Theo**
: 曲面$S$上任一条曲线$C$的测地曲率是保长对应的不变量，即：**测地曲率是内蕴量**。

在取正交参数系的情况下，计算测地曲率有如下的**Liouville 公式**：

**Theo**
: 设$(u,v)$是$S$上的正交参数系，从而$S$的第一基本形式为
$$
I = E(du)^2 + G(dv)^2
$$
假设$C$与$u$曲线的夹角为$\theta$，那么其测地曲率是
$$
\kappa_g = \frac{d\theta}{ds} - \frac{1}{2\sqrt G} \frac{\partial \log E}{\partial v} \cos \theta + \frac{1}{2\sqrt E} \frac{\partial \log G}{\partial u}\sin \theta
$$


最后我们讨论测地挠率，从自然标架的运动公式可以得出：
$$
\tau _ g = \frac{1} {\sqrt g}
\begin{vmatrix}
&\left(\frac{du^2}{ds} \right)^2 & - \frac{du^1du^2}{dsds} & \left(\frac{du^1}{ds} \right)^2 \\
&g_{11} &g_{12} & g_{22}\\
&b_{11} &b_{22} & b_{22}
\end{vmatrix}
$$
故测地挠率和测地曲率一样，是$S$上切方向的函数，反映的是曲面$S$本身的性质，但其不是内蕴量。

对比主方向的方程，主方向恰好是测地挠率为 0 的切方向。同时也有如下定理成立：

Theo
: 在曲面上非直线的渐进曲线$C$ 的挠率是$S$沿着曲面$C$的切方向的测地挠率。