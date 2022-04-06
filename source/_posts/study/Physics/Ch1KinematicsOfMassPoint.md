---
title: 质点运动学
author: Clover
date: 2020-6-8
categories: 课程
tags:
  - 物理
  - 运动学
math: true
plugins:
  - mathjax
  - katex
---

想当初，我还做了这么多笔记？

<!-- more -->

## 质点运动的描述

> **力学**：研究机械运动(宏观物体之间或物体内各部分之间的相对位置的变动)。
>
> **运动学**：研究物体运动的描述及运动学量间的关系。
>
> **动力学**：研究物体运动与物体间相互作用间的联系。
>
> **静力学**：研究物体在相互作用下的平衡问题。

### 质点、参考系和坐标系

#### 质点 (理想化的模型)

若物体的形状和大小可以忽略，则可视为一个**具有一定质量的几何点**。

物体可看作质点来处理的条件：

- 作平动的物体
- 两物体间的距离远大于物体本身的线度

#### 参考系 (运动具有相对性)

研究物体运动时所选定的参照物体。

> 运动具有相对性(relativity)，为此研究运动时需选定参考系(reference system)，为确定各时刻物体相对参考系的位置需建立坐标系(coordinate system)。

#### 坐标系

定量表示物体的位置。

### 质点运动的矢量描述（位移、速度、加速度）

#### 位置矢量(位矢、径矢 Position Vector)

从坐标原点$O$指向质点所在位置$P$的有向线段，表征在空间某个质点 $ P $ 的位置的矢量$\vec{r}=\vec{OP}$.

**大小（模）：**$r=\sqrt{x^{2}+y^{2}+z^{2}}$

**方向：**$\cos \alpha=\frac{x}{r} ,\quad \cos \beta=\frac{y}{r} ,\quad \cos \gamma=\frac{z}{r}$

#### 运动方程

$\pmb{r}=\pmb{r}(t)=x(t) \pmb{i}+y(t) \pmb{j}+z(t) \pmb{k}$

参数方程：$x=x(t) \quad y=y(t) \quad z=z(t)$ 从中小区参数$t$可以得到质点运动的轨道方程

#### 位移（反映位置的变化）

> 时间间隔内质点位置的变化 $\Delta \pmb{r} = \pmb{r}(t+\Delta t) - \pmb{r}(t).$
>
> 当质点在空间运动时，位矢$r$ 是时间$t$的函数，$\pmb{r}=\pmb{r}(t).$ (1,1)

在时刻$t$，质点位矢为$\pmb{r}_A = \pmb{r}(t)$;

在时刻$t+\Delta t$,质点位矢为$\pmb{r}_B=\pmb{r}(t+\Delta t)$

于是，质点在时间间隔$\Delta t$内的位置变化，可以用自 A 到 B 的矢量$\Delta \pmb{r}$来表示，即$\Delta \pmb{r} = \pmb{r}(t+\Delta t) - \pmb{r}(t).$

![png](01a_1.png)

在直角坐标系中：

$$
\begin{aligned}
\Delta \pmb{r}&=\Delta x \pmb{i}+\Delta \pmb{y}+\Delta z \pmb{k}
\\
|\Delta \pmb{r}|&=\sqrt{\Delta x^{2}+\Delta y^{2}+\Delta z^{2}}
\end{aligned}
$$

**注意：**

1. $\widehat{A B}$ 路程（标量）
   $\Delta \pmb{r}$​ 位移（矢量）
2. ${\pmb{r}}$ 位矢、与坐标原点有关
   ${\Delta \pmb{r}}$ 位移、与坐标原点无关
3. ${|\Delta \pmb{r}|} $ 位矢增量的大小
   ${|\Delta r|}$ 位矢大小的增量

#### 速度（Velocity）——反映质点运动的快慢和方向

**平均速度**（单位时间内质点的位移）：$\bar{v}=\frac{\Delta \pmb{r}}{\Delta t}.$

**瞬时速度**（质点某时刻的速度）：$v=\lim \limits_{\Delta t \to 0}\frac{\Delta \pmb{r}}{\Delta t}$

> 直角坐标系中 $\vec{v}=v_{x} \vec{i}+v_{y} \vec{j}+v_{z} \vec{k}$
>
> 大小：$v=|\vec{v}|=\sqrt{v_{x}^{2}+v_{y}^{2}+v_{z}^{2}}$
>
> 方向：为轨道上质点所在处切线方向并指向前进的一侧

**速率**：

- 平均速率：$\bar{v}=\frac{\Delta s}{\Delta t}$

- 瞬时速率：$v=|v|=\lim\limits_{\Delta t \to 0} \frac{|\Delta \pmb{r}|}{\Delta t}=\lim\limits_{\Delta t \to 0} \frac {\Delta s}{\Delta t}=\frac{ds}{dt}$

  注意：一般情况下：$|\Delta \pmb{r}| \neq \Delta s \quad |\pmb{v}| \neq  \bar{v}$

  ​ 当$\Delta t \to 0$ 时：$|\Delta \vec{r}| \rightarrow|\mathrm{d} \vec{r}|=\mathrm{d} s \quad|\vec{v}|=v$

#### 加速度（Acceleration）——反映瞬时速度的变化

平均加速度：$\bar{a}=\frac{\pmb{v}_2-\pmb{v}_1}{\Delta t}=\frac{\Delta \pmb{v}}{\Delta t}$

瞬时加速度：$a=\lim\limits_{\Delta t \to 0}\frac{v_b-v_a}{\Delta t}=\lim\limits_ {\Delta t \to 0} \frac{\Delta \pmb{v}}{\Delta t}=\frac{d^2 r}{dt^2}$

- 加速度的方向：速度增量的方向

- 加速度的大小：$|\pmb{a}|=\sqrt{a_{x}^{2}+a_{y}^{2}+a_{z}^{2}}$

- 直角坐标系中：$\pmb{a}=a_{x} \pmb{i}+a_{y} \pmb{j}+a_{z} \pmb{k}$

**注意**：一般而言，加速度与同一时刻速度的方向之间并没有一定的关联。

**思考**：

1. 位矢、速度和加速度，与参考系的选择是否有关？
2. 一旦参考系选定了，它们就与参考点的选择是否有关？

#### 矢量描述质点运动的优点

矢量描述与具体坐标系的选择无关，因此便于作一般性的定义陈述和公式推导。

#### 坐标系的适当选择

具体计算时，根据具体问题的特点选择。例如：

1. 质点的加速度为常矢量时，可选用直角坐标系；
2. 质点作平面运动的加速度总是指向空间某一固定点时，可选用平面极坐标系；
3. 质点的运动轨迹固定或已知时，可选用自然坐标系。

### 速度、加速度在不同坐标系中的分量表示

#### 直角坐标系的特点

各单位矢量$(e_x,e_y,e_z)$ 或$(i,j,k)$都是不随时间变化的常矢量，即：$\frac{e_x}{dt}=\frac{e_y}{dt}=\frac{e_z}{dt}=\frac{i}{dt}=\frac{j}{dt}=\frac{k}{dt}=0$

因此有：

$$
\begin{aligned}
r&=x\pmb{i}+y\pmb{j}+z\pmb{k}
\\
v&=\frac{dx}{dt}\pmb{i}+\frac{yx}{dt}\pmb{j}+\frac{dz}{dt}\pmb{k}=v_x\pmb{i}+v_y\pmb{j}+v_z\pmb{k}
\\
a&=\frac{d^2x}{dt}\pmb{i}+\frac{d^2y}{dt}\pmb{j}+\frac{d^2z}{dt}\pmb{k}=a_x\pmb{i}+a_y\pmb{j}+a_z\pmb{k}
\end{aligned}
$$

**注意**：$v_x,v_y,v_z$和 $a_x,a_y,a_z$ 都是可正可负的量。

![a的方向](01a_4.png)

**正负号的含义**：如图所示，当质点在$P$点处时， $a_x$与$v_x$的符号相同，说明质点在$x$轴上的投影是在作加速运动；而$a_y$与$v_y$的符号相反，说明质点在$y$轴上的投影是在作减速运动。

#### 实例

在地球表面附近不太大的范围内，重力加速度 g 可以看成是常量。在忽略空气阻力的情况下，二维抛体运动的水平分量和竖直分量将互相独立。这时可选取平面直角坐标系，如图所示。[missing Pic]

$$
\begin{cases}
\frac{dx}{dt}=v_0\cos{\theta_0}
\\
\frac{dy}{dt}=v_0\sin{\theta_0}-gt
\end{cases}
$$

积分后可得：

$$
\begin{cases}
x=(v_0\cos\theta_0) t
\\
y=(v_0\sin\theta_0) t
\end{cases}
$$

消去时间$t$可得描写抛体运动轨迹的**抛物线方程**

$$
y=x\tan\theta_0 - \frac{gx^2}{2v_0^2\cos^{2}{\theta_0}}
$$

**射高**：由$v_y=0$可得$t=v_0\sin\theta_0/g$，由此可确定：

$$
y_{max}=\frac{v_0^2\sin^2\theta_0}{2g}
$$

**射程**：由$y=0$可得$t=2v_9\sin\theta_0/g$，由此可确定

$$
x_{max}=\frac{v_0^2\sin2\theta_0}{g}
$$

#### 平面极坐标系、横向速度和径向速度

![微分](01a_6.png)

如图所示，在一选定的参考系上选取一点$O$为**原点**，并从它出发引一条有刻度的射线$Ox$ 为**极轴**，即建立起了一个**平面极坐标系**。

该平面上任意一点 $A$ 的位矢的长度为$\overline{OA}= r$，它与极轴间的夹角为$\theta$，称为**辐角**。只要 $r$ 和 $\theta$ 给定，$A$点的位置就确定了。

$$
\bar{e}_{\theta}\quad \frac{\mathrm{d} \pmb{e}_{\theta}}{\mathrm{d} t}=-\frac{\mathrm{d} \theta}{\mathrm{d} t} \pmb{e}_{r} \\
\pmb{v} =\dot{r} \pmb{e}_{r}+r \dot{\theta} \pmb{e}_{\theta}\\
\pmb{a}=\left(\ddot{r}-r \dot{\theta}^{2}\right) \pmb{e}_{r}+(r \ddot{\theta}+2 \dot{r} \dot{\theta}) \pmb{e}_{\theta}
$$

在平面极坐标系中，两个互相垂直的单位矢量$e_r$和$e_\theta$，分别沿着 $r$ 和 $\theta $ 增加的方向，它们都不是常矢量。

$$
A(r, \theta) \quad \vec{r}= r \vec{e}_{r}
\\
\frac{\mathrm{d} \pmb{e}_{r}}{\mathrm{d} t}=\frac{\mathrm{d} \theta}{\mathrm{d} t} \pmb{e}_{\theta}
\quad
\frac{\mathrm{d} \pmb{e}_{\theta}}{\mathrm{d} t} =-\frac{\mathrm{d} \theta}{\mathrm{d} t} \pmb{e}_{r}
$$

关于各物理量的表达式，可用以下两种方法得到：

（a）图解法

![01a_6b](01a_6b.png)

**位矢**：$\pmb{r}=r\pmb{e}_r$

**位移**：$\Delta \boldsymbol{r}=\Delta \boldsymbol{r}_{1}+\Delta \boldsymbol{r}_{2}$

**横向位移**：$\Delta \boldsymbol{r}_{1}=\overline{AC}$

**径向位移**:$\Delta r_{2}=\overline{C B}$

当$\Delta t$很小时，由

$$
\begin{cases}
&|O A|=|O C|=r\\
&|O B|-|O C|=\Delta r
\end{cases}
$$

可得：

$$
\begin{aligned}
\Delta \boldsymbol{r}_{1} & \approx r \Delta \theta \boldsymbol{e}_{\theta} \\
\Delta \boldsymbol{r}_{2} & \approx \Delta r \boldsymbol{e}_{r} \\
\boldsymbol{v}&=\lim _{\Delta t \rightarrow 0} \frac{\Delta \boldsymbol{r}}{\Delta t}=\lim_{\Delta t \rightarrow 0} \frac{r \Delta \theta \boldsymbol{e}_{\theta}}{\Delta t}+\lim_{\Delta t \rightarrow 0} \frac{\Delta r \boldsymbol{e}_{r}}{\Delta t} \\
&=r \dot{\theta} \boldsymbol{e}_{\theta}+\dot{r} \boldsymbol{e}_{r}=v_{\theta} \boldsymbol{e}_{\theta}+v_{r} \boldsymbol{e}_{r}
\end{aligned}
$$

**横向速度**：$v_{\theta} e_{\theta}=r \dot{\theta} e_{\theta}$

**径向速度**：$v_{r} \boldsymbol{e}_{r}=\dot{r} \boldsymbol{e}_{r}$

​ 其中：$\dot{\theta}=\mathrm{d} \theta / \mathrm{d} t, \quad \dot{r}=\mathrm{d} r / \mathrm{d} t$

（b）矢量微分法

根据$\pmb{e}_r$和$\pmb{e}_{\theta}$与$\pmb{i}$和$\pmb{j}$之间的关系式：$\pmb{e}_{r}=\pmb{i} \cos \theta+\pmb{j} \sin \theta \quad \pmb{e}_{\theta}=-\pmb{i} \sin \theta+\pmb{j} \cos \theta$

按照矢量求导规则，可得：

$$
\begin{aligned}
\frac{\mathrm{d} \pmb{e}_{r}}{\mathrm{d}t}&=\lim\limits_{\Delta t \rightarrow 0} \frac{\Delta e_{r}}{\Delta t}=\lim\limits_{\Delta t \rightarrow 0} \frac{\Delta \theta}{\Delta t} \pmb{e}_{\theta}=\dot{\theta} \pmb{e}_{\theta} \\
\frac{\mathrm{d} \pmb{e}_{\theta}}{\mathrm{d} t}&=\lim_{\Delta t \rightarrow 0} \frac{\Delta \pmb{e}_{\theta}}{\Delta t}=\lim_{\Delta t \rightarrow 0} \frac{\Delta \theta}{\Delta t}\left(-e_{r}\right)=-\dot{\theta} e_{r}
\\
\boldsymbol{v} &=\frac{\mathrm{d} \boldsymbol{r}}{\mathrm{d} t}=\frac{\mathrm{d}\left(r \boldsymbol{e}_{r}\right)}{\mathrm{d} t}=\dot{r} \boldsymbol{e}_{r}+r \frac{\mathrm{d} \boldsymbol{e}_{r}}{\mathrm{d} t}=\dot{r} \boldsymbol{e}_{r}+r \dot{\theta} \boldsymbol{e}_{\theta} \\
\boldsymbol{a} &=\frac{\mathrm{d} \boldsymbol{v}}{\mathrm{d} t}=\frac{\mathrm{d}\left(\dot{\boldsymbol{r}} \boldsymbol{e}_{r}\right)}{\mathrm{d} t}+\frac{\mathrm{d}\left(r \dot{\theta} \boldsymbol{e}_{\theta}\right)}{\mathrm{d} t} \\
&=\dot{r}^{*} \boldsymbol{e}_{r}+\dot{r} \dot{\theta} \boldsymbol{e}_{\theta}+\dot{r} \dot{\theta} \boldsymbol{e}_{\theta}+r \ddot{\theta} \boldsymbol{e}_{\theta}-r \dot{\theta}^{2} \boldsymbol{e}_{r} \\
&=\left(\ddot{r}-r \dot{\theta}^{2}\right) \boldsymbol{e}_{r}+(r \ddot{\theta}+2 \dot{r} \dot{\theta}) \boldsymbol{e}_{\theta}
\end{aligned}
$$

**径向加速度**：$a_{r} \boldsymbol{e}_{r}=\left(\ddot{r}-r \dot{\theta}^{2}\right) \boldsymbol{e}_{r}$

**横向加速度**：$a_{\theta} \boldsymbol{e}_{\theta}=(r \ddot{\theta}+2 \dot{r} \dot{\theta}) \boldsymbol{e}_{\theta}$

#### 自然坐标系、切向加速度和法向加速度（在质点运动轨迹已知的情况下选用）$S=S(t)$

**自然坐标系**：选定轨迹上任一点$O$为原点，用轨迹的长度$s$描写质点位置，并规定两个正交单位矢量——**切向**单位矢量$\pmb{e}_t$和**法向**单位矢量$\pmb{e}_n$.

**曲率圆**：通过曲线上的一点$A$及其两个邻近的点作一个圆，在这三个点无限趋近的极限情况下，这个圆称为$A$点的曲率圆，其半径称为曲率半径$\rho$。

![曲率](01b_7.png)

**速度**：$\boldsymbol{v}=\boldsymbol{v} \boldsymbol{e}_{t}=\frac{\mathrm{d}s}{\mathrm{d}t}\pmb{e}_t$（只有切向）

**速率**：$v=\frac{\mathrm{d} s}{\mathrm{d} t}$

**加速度**：$\vec{a}=\dot{v} \vec{e}_{t}+\frac{v^{2}}{\rho} \vec{e}_{n}$

- 切向加速度：$a_t=\frac{\mathrm{d}v}{\mathrm{d}t}$
- 法向加速度：$a_n=\frac{v^2}{\rho}$

当$\Delta t$很小时，$\Delta \pmb {e}_{t} \approx \pmb{e}_{n} \Delta \varphi$，利用

$$
\begin{cases}
&\frac{1}{\rho}=\lim _{\Delta s \rightarrow 0} \frac{\Delta \varphi}{\Delta s}=\frac{\mathrm{d} \varphi}{\mathrm{d} s}\\
&\mathrm{d} e_{\mathrm{t}}=e_{\mathrm{n}} \mathrm{d} \varphi=e_{\mathrm{n}} \frac{\mathrm{d} s}{\rho}
\end{cases}
$$

可得：

$$
\begin{aligned}
a &=\frac{\mathrm{d} v}{\mathrm{d} t}=\frac{\mathrm{d}}{\mathrm{d} t}\left(v \boldsymbol{e}_{\mathrm{t}}\right)=\frac{\mathrm{d} v}{\mathrm{d} t} \boldsymbol{e}_{\mathrm{t}}+v \frac{\mathrm{d} \boldsymbol{e}_{\mathrm{t}}}{\mathrm{d} t} \\
&=\frac{\mathrm{d} v}{\mathrm{d} t} \boldsymbol{e}_{\mathrm{t}}+v \frac{\mathrm{d} s}{\mathrm{d} t} \frac{1}{\rho} \boldsymbol{e}_{\mathrm{n}} \\
&=\frac{\mathrm{d} v}{\mathrm{d} t} \boldsymbol{e}_{\mathrm{t}}+\frac{v^{2}}{\rho} \boldsymbol{e}_{\mathrm{n}}=a_{\mathrm{t}} \boldsymbol{e}_{\mathrm{t}}+a_{\mathrm{n}} \boldsymbol{e}_{\mathrm{n}}
\end{aligned}
$$

## 相对运动

> 在解决实际问题时，常常需要处理参考系与参考系之间变换的问题。

如图 1 - 10 所示，参考系$S'$相对于参考系$S$作平移。

![坐标系变换](01b_10.png)

设参考系 相对于参考系$S$的位矢为$R$，则参考系$S'$和参考系$S$间的

相对运动速度(牵连速度)：$\pmb{v}_r=\frac{\mathrm{d} \pmb{R}}{\mathrm{d}t}$

加速度$\pmb{a}_r$(牵连加速度)：$\pmb{a}_r=\frac{\mathrm{d} \pmb{v}_r}{\mathrm{d}t}=\frac{\mathrm{d}^2 \pmb{R}}{\mathrm{d}t^2}$

若质点 P 在参考系$S$和$S'$中的位矢、速度和加速度分别为$r,v,a$和$r',v',a'$, 则它们间的变换关系分别为：

$$
\begin{aligned}
\pmb{r}'&=\pmb{r}-\pmb{R}
\\
\pmb{v}'&=\frac{\mathrm{d}\pmb{r}}{\mathrm{d} t}=\frac{\mathrm{d}\pmb{R}}{\mathrm{d}t}=\pmb{v} -\pmb{v}_r
\\
\pmb{a}'&=\frac{\mathrm{d}\pmb{v}}{\mathrm{d}t}-\frac{\mathrm{d}\pmb{v}_r}{\mathrm{d}t}=\pmb{a}-\pmb{a}_r
\end{aligned}
$$

这些变换关系式是建立在绝对时空观基础上的，在相对论中它们将被建立在相对论时空观基础上的洛伦兹变换所取代。

**经典力学时空观：**

在两个作相对运动的参考系中，时间的测量是绝对的，空间的测量也是绝对的，与参考系无关。时间和长度的的绝对性是经典力学或牛顿力学的基础。

## 习题

{% noteblock quote %}

**坐标系变换**

一般是飞机在空中飞行的风速和飞机速度，或者水中的行船问题等类似的问题

> 画个图就 vans

当然坐标系变换也可以是证明题，例如：

> 证明：把两个物体以不同的速度抛出，则二者的相对速度是常矢量

**坐标系的互化**

常用的坐标系有：

- 直角坐标系

> 在一个倾角为$\alpha$的山坡上开炮，相同的速度大小情况下，当发射角为多少时最远。（真的就高中题目呗）

- 极坐标系

> 一根细棒在水平面内以恒定角速度 $\omega$ 旋转，有一只昆虫从圆心出发，以恒定速率 $u$ 向外爬，求爬行速度和加速度。
>
> **径向加速度**：$a_{r} \boldsymbol{e}_{r}=\left(\ddot{r}-r \dot{\theta}^{2}\right) \boldsymbol{e}_{r}$
>
> **横向加速度**：$a_{\theta} \boldsymbol{e}_{\theta}=(r \ddot{\theta}+2 \dot{r} \dot{\theta}) \boldsymbol{e}_{\theta}$
>
> **速度**：$v=r \dot{\theta} \boldsymbol{e}_{\theta}+\dot{r} \boldsymbol{e}_{r}$
>
> _实际上只需要记住：_$\dot e_\theta =-\dot \theta e_r,\dot e_r = \dot\theta e_\theta$

{% endnoteblock %}
