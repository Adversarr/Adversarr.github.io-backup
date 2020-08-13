---
title: 基础物理学Ch5 刚体运动学
author: Clover
date: 2020-6-8
categories: 基础物理学
tags:
  - 物理
math: true
---

TODO: ND complete

<!-- more -->

1. 运动
2. 动力学
3. 能量

## 刚体运动学

**刚体**：在外力作用下，形状大小不变的物体（任意两个质点之间的距离保持不变）

_理想模型！_

**运动形式**：

- 平动
- 转动
  - 定轴转动
  - 定点转动
- 滚动（平面平行运动）

### 刚体的平动

**平动**：所有点的运动轨迹都保持完全相同（任意两点连线总平行与初始位置间的连线）

**特点**：各点运动特征相同

变化为质点运动

### 定轴转动（_角速度，角加速度_）

**角坐标**：$\theta(t)$

**角位移**：$\Delta \theta$

**角速度矢量**：$\omega = \lim \frac{\Delta \theta}{\Delta t}$

定轴转动的**特点**：

1. 每个质点均做圆周运动 ，圆面为转动平面。
2. 任一质点运动$\Delta \theta \omega \alpha$相同，但是$v,a$不同
3. 运动描述仅需一个角坐标

**角量$\omega$与线量$v$的关系**：$\vec v = \omega r \vec{e_t} = \vec \omega \times \vec r$

匀变速定轴转动的运动学公式

| 质点平动                     | 刚体绕轴转动                                          |
| ---------------------------- | ----------------------------------------------------- |
| $v=v_0+at$                   | $\omega = \omega_0+\alpha t$                          |
| $x=x_0+v_0t+\frac 1 2 at^2$  | $\theta = \theta_0+\omega_0 t + \frac 1 2 \alpha t^2$ |
| $v^2 = v_0^2 + 2 a (x -x_0)$ | $\omega^2 = \omega_0^2 +2 a (\theta -\theta_0)$       |

### 平面平行运动（滚动）

可以看成：

1. 刚体随着质心的**平动**
   - $\vec v$
   - $\vec a$
2. 刚体绕质心的**转动**
   - $\vec \omega$
   - $\vec \alpha$

只考虑纯滚动的情况下（接触点速度为 0）：

- 平动路程$s = R \theta$
- 质心速度大小$v_c = R\omega$
- 质心加速度大小$a = R \alpha$

## 刚体动力学

### 力对转轴的力矩

对转轴的力矩:$M_z = (\vec r \times \vec F)_z$

### 转动定律

**单个质点**：

1. $M_z = r F_t = mr^2\alpha$

**刚体**：

质量元受外力$\vec F_{je}$，质量元受内力$\vec F_{ji}$

$\sum M = (\sum mr^2)\alpha$

**转动惯量**：$M_z = I \alpha$

### 转动惯量

**意义**：转动惯性的量度

计算方法：

1. 离散点$\sum m r ^2$
2. 连续分布$\int r^2 \mathrm d m$

> 取决于质量、形状、位置。

质量是$m$长度$l$的棒，以中点为轴：$I = \frac{1}{12} ml^2$

质量是$m$长度$l$的棒，以一个端点为轴：$I = \frac{1}{3} ml^2$

质量是$m$半径$R$的圆盘，以中心为轴：$I = \frac{1}{2} mR^2$

**平行轴定理**：质量为 m 的刚体，如果对其质心州的转动惯量为$I_C$则，对于任意与该轴平行，相距为$d$的转轴的转动惯量：$I_O=I_C+md^2$

**垂直轴定理**（对于一个薄板）：$I_z = I_x +I_y$

### 刚体定轴转动的角动量定理和角动量守恒

**刚体定轴转动的角动量**：$L_z = \sum\limits_i m_i r_i^2\omega = I\omega$

**角动量定理**：$\int M_z \mathrm{d}t = I\omega_2 -I \omega_1$

**刚体转动的角动量守恒定律**：$if M_z = 0 ,\ then \  L_z = I\omega = const$

### 刚体定轴转动的动能定理

$\mathrm{ d} W = \vec{F}\cdot \mathrm d \vec{r} = F_t r\mathrm{d} \theta = M_z \mathrm d \theta$

力矩对定轴转动刚体做功：$W = \int _{\theta_1}^{\theta_2}M_z \mathrm{d} \theta$

力矩的功率：$P= \frac{\mathrm{d} W}{\mathrm{ d} t}=M_z \omega$

刚体定轴转动的动能：$E_k = \frac 1 2 I\omega^2$

刚体绕定轴转动的动能定理：$W = \int_{\theta_1}^{\theta_2} I \omega \mathrm{d} \omega = E_{k2} - E_{k1 = }=\frac 1 2 I\omega_2^2-\frac 1 2 I\omega_1^2$

## 刚体动力学：平面平行运动动力学

质心运动定理：$\vec{F}= m\vec{a_c}$

转动定律：$M_c = I_c \alpha ,\quad v_c = R \omega$

平面平行运动能量：（科尼希定理）$E_k = E_{kc} +E_k' = \frac{1}{2} mv_c^2 + \frac{1}{2}I_c \omega^2$

## 刚体的定点转动（进动）（Precession）

进动角速度：$\omega_\mathrm p = \frac {\mathrm d \phi}{\mathrm d t} = \frac{|\mathrm d L|}{\mathrm d t\cdot L\sin \theta} = \frac{mgr_c}{I\omega}$

注意角加速度的方向。

## 守恒定律

动量
能量
角动量
质量
电荷
宇称守恒定律
