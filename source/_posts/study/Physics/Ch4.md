---
title: 角动量守恒
author: Clover
date: 2020-6-8
categories: Course
tags:
  - 物理
math: true
plugins:
  - mathjax
  - katex
---

基础物理学Ch4 角动量守恒

<!-- more -->

## 角动量、角动量守恒定律

**{% kbd 「角动量」 %}**：$\vec L = \vec r \times \vec p = \vec r \times m \vec v$（角动量、动量矩）

在圆周运动中：$L = mr^2 w$

{% noteblock quote %}

**角动量守恒定律**：$L_1+L_2 = const$

> 一个系统由两个质点组成，若两个质点只受到它们之间的相互作用，则这个系统的总角动量保持恒定。

{% endnoteblock %}

## 力矩 、角动量定理

#### 力矩、质点的角动量定理

- $L = r\times p\Rightarrow$ (对t微分) $\displaystyle\frac{\mathrm d L}{\mathrm d t} = r\times F$ 定义为$M$（力矩）
- 反之，对上式积分，$\int \vec M \mathrm d t = \vec L _ 2 - \vec L _ 1$（角冲量）（或者写成 $\mathrm d \vec L = \vec M \mathrm d t$ ）地方

**{% kbd 「角动量定理」 %}**：质点对任一固定点的角动量的时间变化率，等于外力对该点的力矩。

#### 质点系的角动量定理

> $L = \sum L = \sum r \times p=\sum r\times mv$
>
> 对 $t$ 求导：$\frac{\mathrm d L}{\mathrm d t} = M^{ex}+M^{in}$
>
> 而在质点系中，由牛顿第三定律：$M^{in}=0$

**{% kbd 「质点系的角动量定理」 %}**：
- 质点系对惯性系中某个参考点的角动量的时间变化率，等与作用在该质点系上的所有外力对该给定参考点的总力矩。
- $\frac {\mathrm d L}{\mathrm d t} = M^{ex}$

**{% kbd 「质点系的角动量守恒定律」 %}**：（总外力矩为零时）$L = const , \mathrm dL =0$

#### 质心系的角动量定理

**{% kbd 「质点组相对于质心的角动量」 %}**：

- $L = \vec r_c \times m\vec v_c+\sum \vec r_i \times m_i \vec v_i' = L_c+m\boldsymbol r_c\times\boldsymbol a_c$
- 质点系对固定点 O 的角动量 L，等于质点系对其质心 C 的角动量 $L_c$ 加上质量集中在质心上随之运动时对 O 点的角动量 $m\boldsymbol r_c\times\boldsymbol a_c$

**{% kbd 「质心系角动量定理」 %}**

- $M_c^{ex} = \frac{\mathrm dL_c}{\mathrm dt}$
- 质点系对质心的角动量的时间变化率，等与作用在该质点系上的所有外力对质心的总力矩。

**{% kbd 「质点组对质心的角动量守恒」 %}**

## 质点在有心力场中的运动

#### 质心在有心力场中运动的一般描述

$$
\begin{cases}
  e_r方向\qquad m(\ddot{r} - r\dot\theta^2)=F(r)\\
  e_\theta 方向\qquad m(2\dot r\dot\theta + r\ddot\theta)=0
\end{cases}
$$

#### 机械能守恒和角动量守恒 离心势能和有效势

机械能守恒定律可以改写为：$\displaystyle\tilde{E}_p(r)=E_p(r)+\frac{L^2}{2mr^2}$

- 有效势能
- 离心势能

> 将二维问题，化为一维问题。

{% noteblock quote %}

**{% kbd 「守恒定律」 %}**

1. 动量
2. 能量
3. 角动量
4. 质量
5. 电荷
6. 宇称守恒定律

{% endnoteblock %}
