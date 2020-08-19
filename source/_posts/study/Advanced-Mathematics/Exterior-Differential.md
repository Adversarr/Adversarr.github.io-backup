---
title: 外微分形式与微积分
author: Clover
date: 2020-5-24
categories: 高等数学
tags:
  - 高等数学
  - 外微分形式
  - 向量空间
math: true
---

些些写累了，准备 ~~白嫖~~ 维基百科。关于外微分形式与场论中几个公式，在教材中并没有给出完整的说明，在这里简单记录一下。

<!--more-->

> 以下内容收集自 Wikipedia

## 外微分形式

### 定义

一个 $k$ 阶的微分形式的外微分是 $k+1$ 阶的微分形式。对于一个 $k$ 阶形式的 $ω = f_I\mathrm dx_I$，其外微分形式为${\displaystyle \mathrm d{\omega }=\sum _{i=1}^{n}{\frac {\partial f_{I}}{\partial x_{i}}}\mathrm dx_{i}\wedge \mathrm dx_{I}}$。

对于一般的*k*-形式 $\sum f_I dx_I$ （其中多重指标 $I$ 取遍所有$\{1, ..., n\}$的为 $k$ 基数的有序子集），我们只作了线性推广。注意如果上面有 $i=I$ 则 $\mathrm dx_{i}\wedge\mathrm dx_{I}=0$。

### 性质

外微分满足：

- 线性

- 楔积法则：$\displaystyle{ d(\omega \wedge \eta )=d\omega \wedge \eta +(-1)^{ {\rm {deg\,} }\omega }(\omega \wedge d\eta )}$

- $\mathrm d^2 =0$

## 微积分中的外微分

### 梯度

对于一个 0-形式，也就是一个光滑函数 $f: R^n\rightarrow R$，我们有 ${\displaystyle df=\sum _{i=1}^{n}{\frac {\partial f}{\partial x_{ i } } }\,dx_{i}}$，所以对于向量场 $\boldsymbol V$ 而言：${\displaystyle df(V)=\langle {\mathrm{grad} }f,V\rangle }$

### 旋度

对于一个 1-形式，${\displaystyle \omega =\sum _{i}f_{i}\,dx_{i}}$ 在 $R^3$ 上，有：

$$
{\displaystyle \omega =\sum _{i}f_{i}\,dx_{i}}
$$

它限制到三维情况 ${\displaystyle \omega =u\,dx+v\,dy+w\,dz}$ 就是

$$
{\displaystyle d\omega =\left({\frac {\partial v}{\partial x}}-{\frac {\partial u}{\partial y}}\right)dx\wedge dy+\left({\frac {\partial w}{\partial y}}-{\frac {\partial v}{\partial z}}\right)dy\wedge dz+\left({\frac {\partial u}{\partial z}}-{\frac {\partial w}{\partial x}}\right)dz\wedge dx.}
$$

因此，对于向量场 ${\displaystyle U}, {\displaystyle V=[u,v,w]}$ 和 ${\displaystyle W}$ 我们有 ${\displaystyle d\omega (U,W)=\langle {\mathrm{curl}}\,V\times U,W\rangle }$

其中 $\mathrm {curl} V$ 代表*V*的旋度，$\times$ 是向量积，而 $<,>$ 是标量积。

### 散度

对于一个 2-形式 ${\displaystyle \omega =\sum _{i,j}h_{i,j}\,dx_{i}\wedge dx_{j},}$

对于三维，若${\displaystyle \omega =p\,dy\wedge dz+q\,dz\wedge dx+r\,dx\wedge dy}$

${\displaystyle d\omega} {\displaystyle =\left({\frac {\partial p}{\partial x}}+{\frac {\partial q}{\partial y}}+{\frac {\partial r}{\partial z}}\right)dx\wedge dy\wedge dz}{\displaystyle ={\mathrm{div}}V\,dx\wedge dy\wedge dz,}$

其中 $V$ 是一个向量场定义为 **${\displaystyle V=[p,q,r].}$**
