---
title: Introduction to PBA 笔记
author: Clover
date: 2022/12/1 # yyyy-mm-dd
categories: Computer Graphics
tags:
  - Physics Based Animation
plugins:
  - mathjax
---

siggraph 2021 course -- An Introduction to Physics-based Animation

<!-- more -->

## A simple start: Particle Dynamics

### Passive Particle in Velocity Field

问题：给定速度场$v(x, t)$，求运动

本质上：I.V.P（初值问题）

$$
\begin{aligned}
x_p(0) = x_0 \\
\dot{x}_p = v(x_p, t)
\end{aligned}
$$

常微分方程 -- 只有 $t$。且是一阶 ODE。用有限差分法求。

### Particle with mass

$$
\begin{aligned}
x_p(0) = x_0 \\
\ddot{x}_p = f / m
\end{aligned}
$$

或者替换为两个一阶ODE耦合的形式：

$$
\begin{aligned}
x_p(0) = x_0 \\
\dot{x}_p = v_p
\dot{v}_p = f/m
\end{aligned}
$$

最简单的，我们可以直接用差分代替微分，实现Symplectic Euler方法。（以及显式欧拉）

> 区别于半隐式欧拉。

```cpp
class Particle {
  mass
  position
  velocity
  force_accumulator
  ...
  (i.e. color size age type)
};
```

### Mass Spring

$$
f_p = k(\| x_q - x_p \|/ r - 1) (x_q - x_p) / \| x_q - x_p \|
$$

## Mathematical Models

> Continuum Mechanics: Assume the underlying materials are continuous.

### Physics Law

主要是两大部分：

1. 牛顿力学 -- 第一定律、第二定律
2. 分析力学(变分原理等)

#### Newton's Law of Motion

> 1, 2, 3 定律

#### 质量守恒、动量守恒、能量守恒

$$
\frac{d}{dt} \int_\Omega \rho dV = - \oint _{\partial \Omega} \rho v(x, t) \cdot n(x) dS
$$
利用散度定理

$$
\int_{\Omega} \frac{\partial \rho}{\partial t} + \nabla \cdot (\rho v) dV = 0
$$

### Materials

#### Rigids

##### 6DoF 模型

1. 质心位置
2. 三维旋转


1. 质心计算：质量加权的平均位置

（刚体上某点的）速度方程：

$$
v(t) = \dot{x}(t) + \dot{R} (t) r_0
$$

##### 线速度、角速度

Euler 旋转定理：任意旋转是沿某轴进行的。

$$
\dot{R} (t) r_0 = \omega(t) \times r(t)
$$

$\omega(t)$ 称为角速度。

**动量(Linear Momentum)**：

$$
P(t) = \sum_{i=1}^{N} m_i v_i(t) = 
\sum_{i = 1}^N  m_i \dot{x}(t) + \omega(t) \times\sum_{i=1}^N m_i r_i(t)
$$

**角动量(Angular Momentum)**:

$$
L(t) = \sum_{i = 1}^{N} m_i r_i \times(\dot{x}(t) + \omega(t) \times r_i(t))
= \left( \sum_i m_i r_i^{*} r_i^{*T}\right) \omega(t)
$$

因为：
$$
r \times \omega = r^* \omega = 
\left(\begin{matrix}
0 & -r_z & r_y\\
r_z & 0 & -r_x\\
-r_y & r_x & 0
\end{matrix}\right) \omega
$$

所以有：

$$
L(t) = (\sum_i m_i r_i^{*} r_i^{*T}) \omega(t)
$$

**Force and Torque**:

$$
\frac{d}{dt} \left(P L\right) = \left(f \tau\right)
$$

其中$\tau = r \times f$

> quaternion

### Soft Bodies

> Central: deformation gradient

$$
K(d) + D(\dot{d}) + M\ddot{d} = f_{ext}
$$

其中 $d$ 是位移（指形变函数），$K$表示弹性力（内部），$D$表示衰减力，$M$是质量矩阵。

形变梯度的引入：

$u$ 是 Rest-Space，$x$ 是 World-Space，最简单的情况是

$$
x(u) = x(u_0) + A(u - u_0)
$$

$A$ 是任意矩阵。如果是更复杂的情况，可以局部线性化为上面的形式。

即：$\Psi$ （形变函数）局部线性近似 -> $F = \partial x / \partial u$ -> SVD, RS, ... (Strain Measuring)

直觉上 SVD（$F = U \Sigma V^T$）：

1. $V^T$：Rest->Aligned
2. $\Sigma$：拉伸收缩
3. $U$：Aligned->World

避免 Global Rotation后：RS 分解。

#### Strain

> Dimension-less Quantity: measures the amount of deformation.
>
> Strain represents the displacement between particles in the body relative to a reference length.

仅仅是**某一种**刻画形变程度的方式！

$$
Strain(x_r) = 0
$$

例如：Mass-Spring: $l / l_0$

常用的应变

1. Green's Finite Strain, -> Right Cauchy-Green Strain
2. Cauchy infinitesimal strain,
3. co-rotated strain.

E.g. Right Cauchy-Green Strain:

$$
\epsilon_{ij} = \frac{1}{2} (F^T F - I)
$$

Cauchy infinitesimal strain:

$$
\begin{aligned}
\epsilon & = \frac{1}{2} (F^T + F + D^TD) -I & \mathrm{(Green)}\\
  & \approx \frac{1}{2} (F + F^T) - I & \mathrm{(Cauchy~infinitesimal)}
\end{aligned}
$$

在图形学中最常用的是 co-rotated strain metric:

$$
\epsilon = \frac{1}{2} \left( \tilde{F} + \tilde{F}^T \right) - I
$$

- 在式子中显式地丢掉了无关的旋转，$F=Q\tilde{F}$

#### Stress

> 描述单位面积上的力

常用模型是为线性的

$$
\sigma = C \epsilon
$$

其中 $C$ 是一个3x3x3x3的**张量**，但是！考虑到：

1. $\sigma, \epsilon$ 对称
2. Iso-tropic （各向同性）

只有两个参数，Lame Coefficients:

$$
\sigma_{ij} = \lambda \epsilon_{kk}\delta_{ij} + 2\mu \epsilon_{ij}
$$

Or in matrix notation...

$$
\sigma = \lambda Tr(\epsilon) I + 2 \mu \epsilon
$$

#### 弹性能量、力

势能密度：(Einstein Notation)

$$
\eta = \frac{1}{2} \sigma_{ij} \epsilon_{ij} 
= \frac{1}{2} \sigma : \epsilon 
$$

总能量是势能密度的积分。

Traction（切向力？）：

$$
\tau = \sigma n
$$

- 其中 $n$ 是单位法向。

> $F$ 始终让总势能减少。

$$
f_i = -\frac{\partial \eta}{\partial x_i}
$$

也可以被定义区域积分：

$$
f = \int_{\partial R} \sigma n \mathrm{d}S
$$

#### Stress Revisit

Definition of Stress: Maps *normal* to *force*

问题在于定义的空间是 世界/物体

如果是世界坐标系下的法向和Stress -- Cauchy Stress -- $\sigma$

如果是material space->material space， --  PK2 -- $S$

常用的是 PK1: Material Space Normal -> World Space Force

$$
P = J \sigma F^{-T} = FS
$$

好处在于，PK1 给出的是从参考到世界坐标的映射。

#### 塑性形变

$$
F = F_e F_p
$$

### 流体

$$
\begin{aligned}
\rho(u_t + u \cdot \nabla u) = - \nabla p + \mu \Delta u + f \\
\nabla \cdot u = 0
\end{aligned}
$$

- $u$ 为速度场 - 欧拉视角
- $u_t$ 为加速度场 - 欧拉视角
- $p$ 为压强 - 欧拉视角
- $\mu$ 描述粘性
- $f$ 为外力

#### Material Derivative

欧拉视角下，流体的加速度是

$$
a_p = \frac{d}{dt} v_p(t) = \frac{d}{dt} u(x_p(t), t) =u_t + u \cdot \nabla u
$$

拉格朗日视角下的量 $u$，材料导数（拉格朗日视角的）定义为

$$
Du / Dt = u_t + u \cdot \nabla u
$$

#### Forces

$$
\rho(u_t + u \cdot \nabla u) = - \nabla p + \mu \Delta u + f
$$

- 压强 -- 用于抵消压缩
  - 在某些情况下，也被称为不可压缩流体的 Lagrange Multiplier -> Divergence-Free Constraint
- 粘性力 -- Penalizes Velocity Differences
- 外力 $f$

#### Incompressibility

从质量守恒方程：

$$
\rho_t + \Delta \cdot (\rho u) = 0
$$

Apply Product Rule，Spartial Derivative term gives:

$$
\nabla \cdot (\rho u) = u\cdot \nabla \rho + \rho \nabla \cdot u
$$

## Discretization

1. Lagrange or Eulerian
2. Spatial data Structures.
3. FDM & FEM

### Lagrangian v.s. Eulerian







