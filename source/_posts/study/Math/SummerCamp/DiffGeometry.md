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

### 测地线

观察到测地曲率是内蕴量，从而要观察曲面上测地曲率为 0 的曲线（测地线）

Theo
: 曲面上曲线$C$是测地线，当且仅当，它或是一条直线，或者其主法向量处处是曲面的法向量

> 例如：
>
> 1. 旋转面上的经线是测地线
> 2. 若曲面上运动的质点 $p$ 只受到将它约束在曲面上的力的作用，而不受到任何其他外力作用，则$p$的轨迹是测地线

Theo
: 对于曲面上任意一点$p$和曲面在$p$的任意单位切向量$v$，在曲面上存在唯一的一条弧长参数测地线通过$p$且以$v$为切向量

> 平面 – 直线
>
> 曲面 – 测地线

Theo
: 设 $C$ 是曲面 $S$ 上的一条曲线，则$C$的弧长在任意一个有固定端点的变分$C_t$中达到临界值的充分必要条件是$C$是$S$的测地线。

从而我们有：若曲线$C$是连接$p,q$的最短线，则$C$是测地线。

### 测地坐标系和法坐标系

#### 测地线族

在研究了测地线的性质后，我们研究测地线族的性质。

Theo
: 设$\Sigma$是曲面$S$上覆盖了区域$D$的测地线族，$\Sigma_1$是由在区域$D$内与$\Sigma$中的曲线正交的轨线构成的曲线组，则其中任意两条曲线在$\Sigma$中各条测地线上截出的曲线段长度相等。

> 也就是说，测地线族的任意两条正交轨线之间的距离是处处相等的。
>
> 即：测地线族的任意两条正交轨线是**测地平行**的

Theo
: 设$C$是曲面$S$上连接了$p,q$两点的一条测地线，若曲线$C$能够潜入到覆盖了区域$D$的测地线族$\Sigma$中，且$p,q\in D$，则其是区域内连接两点的最短线

#### 测地平行坐标系

Theo
: 在曲面$S$的每一点$p$的一个充分小的邻域内必定存在参数系$(u,v)$使得$p\rightarrow (0, 0)$，而第一基本形式可以写作
$$
I = (du)^2 + G(u,v) (dv)^2
$$
函数 $G$ 满足：$G(0, v)=1 $，$\displaystyle \frac{\part G}{\part u}(0, v) =0$，参数系$(u,v)$是**测地平行坐标系**

#### 测地极坐标系

定义指数映射：
$$
\exp_p : T_pS \rightarrow S\quad \mathbf v\rightarrowtail \gamma(|\mathbf v|, \mathbf v_0)
$$
$\gamma$对于点$p$处的单位切向量$\mathbf v_0$，映射为弧长参数测地线上的参数为$s$的位置。

显然指数映射 $\exp_p$ 是连续可微的。于是有 **法坐标系**：
$$
u^\alpha = u ^ \alpha(\exp_p(\mathbf v)) = u ^ \alpha(v^1, v^2)
$$
从而有**测地圆**（以$p$为中心，$s_0$为半径）

Theo 高斯引理
: 从$p$出发的测地线与以点$p$为中心的测地圆是彼此正交的。（即曲线族$\Sigma_1$中的每一条曲线都是测地线族$\Sigma$的正交轨线。

由此可以推导出测地极坐标系 $（s,\theta)$

Theo
: 在曲面$S$的每一点的$p$邻域内，出去从点$p$出发的一条测地线外，也存在测地极坐标系，使得曲面第一形式为
$$
I = (ds)^2 + G(d\theta)^2\quad \begin{cases}
\lim _{s\rightarrow 0} \sqrt G = 0\\
\lim_{s\rightarrow 0} \frac{\partial }{\partial S} \sqrt{G(s,\theta)} = 1
\end{cases}
$$
对应了平面上的极坐标系

### 常曲率曲面

高斯曲率为常数的曲面为**常曲率曲面**。

由于高斯曲率为内蕴量，我们不难考虑如下的定理：

Theo
: 有相同高斯曲率的任意两块常曲率曲面在局部上有保长对应。

> 从现在的观点来看：
>
> 1. 常曲率曲面的第一基本形式是由其高斯曲率完全决定的
> 2. 非欧几何学：将平面几何学推广到常曲率曲面

### 平行移动

> 考虑切向量场的协变微分和平行移动

### Gauss-Bonnet公式

假定曲线是邮箱曲面上的一条分段光滑简单闭曲线，其包围的区域是曲面 $S$ 的一个单连通区域，则
$$
\oint _C. \kappa _ g \mathrm d s + \iint _D K \mathrm d \sigma = 2 \pi - \sum _ {i = 1} ^ n \alpha _ i
$$

- $\kappa_g$ 是曲线的测地曲率，
- $K$ 是曲面的高斯曲率
- $\alpha _ i $ 表示曲线在角点$i$的外角

