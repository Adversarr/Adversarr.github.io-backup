---
title: 基础物理学Ch7 狭义相对论
author: Clover
date: 2020-6-8
categories: 基础物理学
tags:
  - 物理
mathjax: true
---

TODO: ND complete

<!-- more -->
## 狭义相对论的基本假设

### 绝对时空观与伽利略相对性原理

1. 长度、时间间隔、质量、相互作用力与参考系无关
2. 速度、位移、加速度满足伽利略变换关系（速度变换式、时空变换式）

### 电磁学发展及其与绝对时空观的规律

1. 电磁学规律：
   + Maxwell方程组
   + $c = \frac{1}{\sqrt{\epsilon_0 \mu_0}}$
2. 电磁学规律与绝对时空观的矛盾
   + 光速与参考系无关
3. 矛盾解决
   + 伽利略速度变换正确，而光速只适用于特殊的参考系：`以太参考系`
   + 相对性原理对电磁学规律也适用，为了保持光速不变，需要建立新的时空变换关系

### 狭义相对论的基本内容

+ 事件何时发生？在哪里发生？
+ 事件之间相隔多远？相隔多久？
+ 时间和空间是否有关联？
+ 时间和长度的测量与参考系是否有关？
+ 物体的质量与运动是否有关？

### 两个基本假设

1. 相对性原理（The Relativity Postulate）：物理性质在所有惯性系中具有相同的表达形式
2. 光速不变原理（The Speed of Light Postulate）

### 相对论时空观

$S$系观测，$S'$系运动

1. 同时具有相对意义。
2. 时间延缓（Time Dilation）
   **固有时**：某个参考系中同一个地点发生的两事件的时间间隔
   在$S$系中观测：$\Delta t=\frac{\Delta t_0}{ \sqrt{1-(v/c)^2}}$
   *运动的钟走得慢*
   时间间隔是**相对的**，与参考系有关。
3. 长度收缩（length contraction）
   **固有长度**：静止棒在一个静止的坐标系中的长度
   在$S$系中观测：$l = l' \sqrt{1-(v/c)^2}$
   运动的棒长度变短或收缩，长度或时间间隔是**相对**的，与参考系有关。

## 洛伦兹变换

$$
\begin{cases}
    （S观测\rightarrow S'观测）已知P在S系中的时空坐标t,x:
    \\ \qquad x = vt+x'\sqrt{1-\beta^2} \rightarrow x' = \frac{x- vt}{\sqrt{1-\beta ^2}}\\
    （S观测\rightarrow S'观测）已知P在S系中的时空坐标t,x：
    \\ \qquad x' = x\sqrt{1-\beta^2} - vt'\rightarrow t' = \frac{t-\frac v c^2 x}{\sqrt{1-\beta^2}}
\end{cases}
$$
$$
\Rightarrow
\begin{cases}
    x' = \gamma (x- vt)\\
    y' = y\\
    z' = z\\
    t' = \gamma(t -\frac{v}{c^2}x)\\
    \gamma = \frac{1}{\sqrt{1 - \beta ^2}}
\end{cases}
$$

做全微分：

$$
\begin{aligned}
   &dx' =\gamma({dx - vdt}),\\
   &dt' = \gamma(dt - (v/c^2)dx)\\
   \Rightarrow &u_x' = \frac{dx}{dt} = \frac{u_x -v}{1-\frac v {c^2}u_x }\\
\end{aligned}
$$

类似的，可以得到：

正变换：

$$
\left\{
   \begin{aligned}
      u_{x}^{\prime}&=\frac{u_{x}-v}{1-\frac{v}{c^{2}} u_{x}} \\
      u_{y}^{\prime}&=\frac{u_{y}}{\gamma\left(1-\frac{v}{c^{2}} u_{x}\right)} \\
      u_{z}^{\prime}&=\frac{u_{z}}{\gamma\left(1-\frac{v}{c^{2}} u_{x}\right)}
   \end{aligned}
\right.
$$

逆变换：

$$
\left\{
   \begin{aligned}
      u_{x} &=\frac{u_{x}^{\prime}+v}{1+\frac{v}{c^{2}} u_{x}^{\prime}} \\
      u_{y}&= \frac{u_{y}^{\prime}}{\gamma\left(1+\frac{v}{c^{2}} u_{x}^{\prime}\right)} \\
      u_{z} &=\frac{u_{z}^{\prime}}{\gamma\left(1+\frac{v}{c^{2}} u_{x}^{\prime}\right)}
   \end{aligned}
\right.
$$

### 同时的相对性

在S'系中观测S系的事件：$\Delta t' = \frac{\Delta t - \frac{v}{c^2}\Delta x}{\sqrt{1-\beta^2}}$

1. 因果律不变
2. 两件事有因果关系，则$\Delta x/ \Delta t<c$
3. 两件事没有因果关系，则可能$\Delta x /\Delta t > c$

## 相对论动力学

### 动量与质量

$m = \frac{m}{\sqrt{1-\beta^2}}$

**相对论动量**：$\vec p = m\vec v = \gamma m_0\vec v$

其中$m_0$称为**静质量**。

### 力、功、动能

$\vec F = \frac{d\vec p}{dt} = m \frac{d\vec{ v}}{dt}+\vec v \frac{dm}{dt}$

相对论动能：$E_k -0 = \sum_0^v \vec v\cdot d\vec p = \frac{m_0v^2}{\sqrt{1-v^2/c^2}}+m_0c^2\sqrt{1-v^2/c^2} -m_0c^2=mc^2-m_0c^2$

### 能量、质能关系

**静质量**：$E_0 = m_0c^2$

**质量亏损**：$B = \sum m_{0i} -m_0 = \Delta m$

**结合能**：$E_B = Bc^2=\Delta m c^2$

**相对论质能关系**：$E = mc^2 = m_0c^2 +E_k $

**总能量**：$E = mc^2$

### 能量、动量的关系

$E^2-p^2c^2 = m_0^2 c^4,\qquad E^2 = E_0^2 +p^2c^2$

光的波粒二象性$E = h\mu ,\quad p = h/\lambda$

### 能量、动量、力的相对论变换

#### 动量、能量的相对论变换

1. E，p关系：$E^2/c^2 - p^2$和时空变换：$c^2t^2 -r^2$是洛伦兹不变量。
2. 对应关系

$$
\left\{\begin{aligned}
   p'_{x'} &= \gamma (p_x - u \frac{E}{c^2})\\
   p'_{y'} &= p_y\\
   p'_{z'} &= p_z\\
   E' &= \gamma (E - up_x)
\end{aligned}\right.
$$

#### 力的相对论变换

$F_x =F_x'$

$F_y = F_y' /\gamma$

$F_z = F_z' /\gamma$

## 广义相对论

1. 等效原理
2. 广义协变性原理
3. 马赫原理

#### 广义相对论的数学基础
