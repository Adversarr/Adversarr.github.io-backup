---
title: 机械能守恒
author: Clover
date: 2020-6-8
categories: 基础物理学
tags:
  - 物理
math: true
---
基础物理学Ch3 机械能守恒 这部分就简单提一句

<!-- more -->

## 功 动能定理

### 功（Work）

> 力对质点所作的功为力在质点位移方向的分量（大小）与位移大小的乘积。（功是标量，过程量）

- 一段位移的功$\mathrm dW=\vec F\cdot \mathrm d {\vec r}$

  注：功的大小和参考系有关。

- 合力的功（第二型曲线积分）

- **功率（Power）**：反应做功快慢程度的物理量

  - 平均功率
  - 瞬时功率
  - 功率单位

{% note primary %}

### 质点的动能定理（Theorem of Kinetic Energy）

- **动能**：$E_\mathrm{k}= \frac{1}{2}mv^2=\frac{p^2}{2m}$

- **动能定理**：合外力对质点所做的功，等于质点动能的增量。

> 功和动能都与参考系有关，动能定理只能适用于惯性系！

{% endnote %}

## 保守力 势能

### 万有引力、重力、弹性力做功的特点

{% note primary %}

#### 万有引力做功

**万有引力：**$\vec F=-G\frac{m'm}{r^3}\vec r$

**做功：**$W=(-G\frac{m'm}{r_A})-(-G\frac{m'm}{r_B})$

#### 重力做功

$\vec P=-mg\vec k$

$W=\int_A^b \vec P \cdot \mathrm d \vec r=mgz_A-mgz_B$

#### 弹性力做功

$W=\frac{1}{2}kx_A^2-\frac{1}{2}kx_B^2$

{% endnote %}

### 保守力和非保守力

**保守力：**力所做的功与路径无关，仅取决于质点的**始末位置**，具有这种特征的力统称为**保守力**。

- 物体沿闭合路径运动一周，保守力对它所做功为零

> 实则是旋度为零

**非保守力**：做功与路径有关

> 旋度不恒为零

有关旋度，参见 {% post_link Advanced-Mathematics/Vectors-and-Analytic-Geometry-Integration %}

### 势能（Potential Energy）

- 保守力做功等于势能的减少或势能增量的负值。

  势能：与物体间相互作用及相对位置有关的能量

- 势能是空间位置的函数

- 势能具有相对性，势能大小与势能零点的选取有关 .

- 势能是属于系统的 ，所以又称为相互作用势能.

- 势能的计算：物体在某位置时的势能

1. **引力势能**，以无穷远处为势能零点
2. **重力势能**，以地面为势能零点
3. **弹性势能**，以物体为势能零点

### 势能函数与保守力的关系

**积分形式：**$W= - \Delta E_p$

**微分形式：**$\vec F \mathrm d\vec r= -\mathrm d E_p$（对$\vec r$的偏导）

$\nabla$算符举例：

$$
\nabla=(
\begin{matrix}
\frac{\mathrm d}{\mathrm d x},
\frac{\mathrm d}{\mathrm d y},
\frac{\mathrm d}{\mathrm d z}
\end{matrix})
$$

**保守体系的平衡及平衡条件**：

![stable](03_0.jpg)

- 稳定平衡
- 不稳定平衡
- 随遇平衡

条件：$\nabla E_p=0$

### 功能原理 机械能守恒定律

#### 质点系的动能定理

$\sum W_i =W_{ext}+W_{int}$

$\Rightarrow W_{ext}+W{int}=\sum E_{ki}+ \sum E_{ki0}$

#### 质点系的功能原理

质点系在运动过程中，所有外力的功和系统内非保守内力的功的总和等于系统机械能够的增量。$W_{ext}+W_{int(非保守力)}=E-E_0$

#### 机械能守恒定律

当$W_{ext}+W_{int(非保守力)}=0$时：$E=E_0$

当作用于质点系的外力和非保守内力都不做功或所做功的代数和等于零时，系统的总机械能保持不变。

- 功总是和能量的变化与转换过程相联系，功是能量变化和转换的一种量度，而能量是代表物体系统在一定条件下所具有的作功本领。
- 守恒定律的特点和优点：不研究过程细节而能对系统的状态下结论。

#### 势能函数

## 质心参考系

### 质心的定义

由 n 个质点组成的质点系，其质心的位矢：$\vec r_C=\frac{\sum m\vec r}{\sum m}$

### 质心运动定理

$\vec F^{ex}=m\vec a_c$

### 质心参考系的特点

**零动量参考系**：

- $\sum p = \sum m\vec v = 0$
- $\sum m\vec r = 0,\quad \sum m\vec a =0$

**克尼希定理**：

- 质点系相对基本参考系的动能（_绝对动能_） 等于质点系在质心参考系中的动能（_相对动能_）加上*质心动能*
- $E_k = \frac{1}{2} mv_c^2 + E_k'= \frac{1}{2} mv_c^2 + \sum \frac{1}{2} m_i v_i ^2$
