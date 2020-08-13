---
title: 多元函数积分学及其应用
author: Clover
date: 2020-5-23
tag:
  - 高等数学
  - 向量空间
  - 多元函数
categories: 高等数学
math: true
---

多元函数积分学复习提纲。些些在 5.20 被强行塞了一大把狗粮之后，才知道下个星期就要考试，现在才开始预习...

<!--more-->

## 多元数量值函数积分的概念和性质

### 质量的计算

### 多元数量值函数积分的概念

- **Def**：多元数量值函数积分

### 积分存在的条件和性质

1. 线性性质
2. 对积分域的可加性
3. 积分不等式
4. 中值定理

## 二重积分的计算

1. 二重积分的几何意义
2. 直角坐标系下二重积分的计算法
3. 极坐标系下二重积分的计算法
4. 曲线坐标下二重积分的计算法

## 三重积分的计算

1. 化三重积分为单积分与二重积分的累次积分
2. 柱面、球面坐标下的三重积分计算法
   1. 曲线坐标下的三重积分
   2. 柱面坐标及柱面坐标下的三重积分计算法
   3. 球面坐标和球面坐标下的三重积分计算法

## 含参变量的积分和反常重积分

### 含参变量的积分

- **Def**：含参变量$y$的积分

- **Thm**：（连续性）$f\in C(D) \rightarrow F(y) = \int^b_af(x,y)\mathrm d x 在[c,d]上连续$

- **Inf**：（连续性的极限形式表达）$\displaystyle\lim \limits_{y\rightarrow y_0} \int_a^bf(x,y)\mathrm d x = \int_a^b f(x,y_0)\mathrm d x = \int_a^b[\lim\limits_{y\rightarrow y_0} f(x,y)]\mathrm dx$

- **Thm**：（可导性）$f,f_y\in C(C)$，则 $F(y) = \int f(x,y) \mathrm dx $有连续导数，且积分和求导运算可交换

- **Thm**：（积分顺序交换性）$f \in C, F(y) = \int f\mathrm dx ,G(x) = \int f\mathrm dy\rightarrow \int F(y) \mathrm d y = \int G(x) \mathrm dx$

- **Thm**：设 $f(x,y)\in C(D), x_i (y) \in C[c,d]$ 则，$F(y) = \int_{x_1(y)}^ {x_2(y)}f(x,y)\mathrm dx$ 在$[c,d]$上连续

- **Thm**：$F'(y) = \int _{x_1(y)}^ {x_2(y)}f_y(x,y)\mathrm dx+ f(x_2, y]x_2' - f(x_1,y) x_1'$

### 反常重积分

- 无界区域的二重积分
  - **Thm**：（收敛判别法）$f(x,y)$ 在无界区域上连续，若存在$\rho_0>0$，使当$\rho \ge \rho_0$ 有$|f|\le \frac {M}{\rho^\alpha}$，且 $M,\alpha$为常数，则当$\alpha >2$时反常二重积分$\int\int f \mathrm d \sigma$收敛
- 无界函数的二重积分
  - **Def**：无界函数的二重积分$\lim\limits_{d\rightarrow 0} \int\int f\mathrm d \sigma$
  - **Thm**：（收敛判别法）设 $f(x,y)$ 在有界区域上除了$P_0$外处处连续，若 $|f|\le \frac {M}{\rho ^\alpha}$在除 $P_0$ 外的区域上处处成立，则当 $\alpha <2$时，反常二重积分收敛

## 第一型线积分与面积分

### 第一型线积分

- 第一型线积分的计算公式 $r = r(t)\rightarrow \int_{(C)}f ds = \int_f \sqrt{\dot x^2+\dot y^2+\dot z^2}\mathrm d t$

### 第一型面积分

- 曲面的面积
  
  - **Thm**：（用 $u,v$ 变量表示曲面）$S = \int\int\limits_{(\sigma)}||\boldsymbol r_u \times \boldsymbol r_v|| \mathrm d u \mathrm d v$
  - **Thm**：（用 $z = f(x,y)$ 表示曲面）$S = \iint \limits_{(\sigma)} ||\boldsymbol r_x \times \boldsymbol r_y || \mathrm dx\mathrm dy = \iint\limits_{(S)} \sqrt{1+f_x^2+f_y^2}\mathrm dx \mathrm dy$

- 第一型曲面积分的计算
  
  - **Thm**：（用 $u,v$ 变量表示曲面）$I = \iint\limits_{(S)} f(x,y,z)\mathrm dS = \iint\limits_{(\sigma)}f||\boldsymbol r_u \times \boldsymbol r_v|| \mathrm d u \mathrm d v$
  - **Thm**：（用 $z = f(x,y)$ 表示曲面）$I = \iint\limits_{(S)} f \sqrt{1+f_x^2+f_y^2}\mathrm dx \mathrm dy$

## 第二型线积分和面积分

### 场的概念

- **Def**：数量场、向量场、场函数
- 场的几何描述

### 第二型线积分

- **Def**：第二型线积分$\int_{(C)} \boldsymbol A(M)\cdot \boldsymbol{\mathrm d s} = \lim\limits_{d\rightarrow 0} \sum\limits_{k=1}^n \boldsymbol{A}(\overline {M_k})\cdot \overrightarrow{M_{k-1}M_k}$

- 第二型线积分的性质
  
  - 积分结果与方向有关
  - 可加性

- 第二型线积分的计算 $\int_{(C)}\boldsymbol A(M)\cdot \boldsymbol{\mathrm ds} = \int_{(C)}P\mathrm dx +Q\mathrm dy +R\mathrm dz =\int P\dot x+Q\dot y+R\dot z \mathrm dt$

- 两类线积分的联系 $\int_{(C)}\boldsymbol A(M) \cdot \boldsymbol{\mathrm ds} = \int \boldsymbol A(M)\cdot \boldsymbol e_r \mathrm ds$

### 第二型面积分

- **Def**：第二型面积分 $\iint\limits_{(S)} \boldsymbol A(M)\cdot \boldsymbol {\mathrm dS} = \lim\limits_{d\rightarrow 0}\sum\limits_{k=1}^n \boldsymbol A(M_k)\cdot \boldsymbol e_n(M_k) \Delta S_k$

- **Thm**：（用外微分形式表示）$\iint A(M)\cdot \boldsymbol{\mathrm dS} = \iint\limits_{(S)}P\mathrm dy \wedge \mathrm dz +Q\mathrm dz \wedge dx + R\mathrm dx\wedge \mathrm dy$

- 两种面积分的联系 $\iint_{(S)} \boldsymbol A(M)\cdot \mathrm d \boldsymbol S = \iint (P\cos\alpha + Q\cos\beta + R\cos\gamma)\mathrm dS$

- 第二型面积分的计算 $\iint_{(S)} R(x,y,z) \mathrm dx\wedge \mathrm dy = \pm \iint\limits_{(\sigma_{xy})} R(x,y,z(x,y))\mathrm dx\mathrm dy$ 其余式同理。其中当曲面法向量与 $z+$ 同向时取 $+$ 号，反之取 $-$ 号

## 各种积分的联系及其在场论中的应用

### Green 公式

- **Def**：单连通域，复连通域

- **Thm**：Green 公式 $\iint_{(\sigma)}(\frac{\delta Q}{\delta x} - \frac{\delta P}{\delta y} \mathrm d \sigma = \oint_{(\pm C)} P\mathrm dx + Q\mathrm dy$

- **Inf**：任何一条分段光滑的闭曲线所围成的平面区域的面积为 $A = \frac 1 2 \oint_{(+C)} x\mathrm dy - y\mathrm dx= \oint_{(+C)} x\mathrm dy = -\oint_{(+C)} y\mathrm dx$

### 平面线积分与路径无关的条件

- **Thm**：TFAE
  
  1. 沿区域内任何一条分段光滑的简单闭曲线的线积分 $\oint P\mathrm dx+Q\mathrm dy = 0$
  2. 线积分 $\int P\mathrm dx +Q\mathrm dy$ 的值在区域内与积分路径无关
  3. 被积表达式$P\mathrm dx +Q\mathrm dy$ 是某个二元函数的全微分

- **Def**：（环流量、环量）称眼闭曲线 $C$ 的第二型线积分为向量场 $A$ 沿闭曲线 $C$ 的环量。

- **Def**：（势函数、位函数、有势场）

- 该结论表明，对于一个连续向量场而言，无旋、保守、有势是等价的。

- 势函数的求法
  
  - 用线积分求解
  - 用偏积分求解
  - 用凑全微分法求解

### Gauss 公式和散度

- Gauss 公式
  
  - **Thm**：（Gauss 公式）$\iiint_{(V)} (\frac{\partial P}{\partial x} +\frac{\partial Q}{\partial y} +\frac{\partial R}{\partial z})\mathrm dV = \iint P \mathrm dy\wedge \mathrm dz +Q\mathrm dz\wedge \mathrm dx+R\mathrm dx\wedge \mathrm dy$
  - **Thm**：（Gauss 公式）$\iiint_{(V)}\nabla \cdot \boldsymbol A \mathrm dV = \iint_{(S)} \boldsymbol A\cdot \mathrm d \boldsymbol S$

- 通量和通量密度
  
  - **Def**：（通量）$\boldsymbol A(M)$ 对曲面 $(S)$ 的第二型面积分 $\iint\limits_{(S)} \boldsymbol A \cdot \mathrm d \boldsymbol S$

- 散度的定义及其计算
  
  - **Def**：（散度）$\mathrm{div} \boldsymbol A(M) = \lim\limits_{(\Delta V)\rightarrow M}\frac{1}{\Delta V} \iint \boldsymbol A(M)\cdot \mathrm d\boldsymbol S$
  - **Thm**：（散度的计算公式）$\mathrm{div} A = \nabla \cdot \boldsymbol A = \frac{\partial P}{\partial x} +\frac{\partial Q}{\partial y} +\frac{\partial R} {\partial z}$
  - **Inf**：（用散度表示 Gauss 公式）$\iiint\limits_{(V)} \mathrm{div} \mathrm A \mathrm d V = \iint\boldsymbol A\cdot \mathrm d \boldsymbol S$

- 散度的运算法则和公式
  
  - $\mathrm{div}(C\boldsymbol A) = C\mathrm{div} \boldsymbol A$
  - $\mathrm{div}(\boldsymbol A\pm\boldsymbol B) = \mathrm{div}(\boldsymbol A) \pm \mathrm{div}(\boldsymbol B)$
  - $\mathrm{div}(u\boldsymbol A) = u\mathrm{div} \boldsymbol A + \nabla u \cdot \boldsymbol A$

### Stokes 公式和旋度

- Stokes 公式
  
  - **Thm**：（Stokes 公式）$\oint_{(C)} P\mathrm dx + Q\mathrm dy +R\mathrm dz = \iint\limits_{(S)}(\frac{\partial R}{\partial y} -\frac{\partial Q}{\partial z})\mathrm dy\wedge \mathrm dz +(\frac{\partial p}{\partial z}-\frac{\partial R}{\partial x}) \mathrm dz\wedge \mathrm dx + (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\mathrm dx\wedge \mathrm dy$
  - **Inf**：（利用 nabla 算子表示的 Stokes 公式）$\oint_{(C)} \boldsymbol A\cdot \mathrm d \boldsymbol s = \iint_{(S)} (\nabla \times  \boldsymbol A)\cdot \mathrm d \boldsymbol S = \iint_{(S)} (\nabla \times  \boldsymbol A)\cdot \boldsymbol e_n \mathrm dS$

- 环量和环量密度
  
  - 环量密度 $\lim\limits_{(\Delta )\rightarrow M } \frac {1} {\Delta S}\oint_{(\Delta C)}\boldsymbol A\cdot \mathrm d \boldsymbol s$

- 旋度的定义及其计算公式
  
  - **Def**：（旋度）$\mathrm{rot} \boldsymbol A$ 用行列式表示
  - **Thm**：（旋度的计算公式）$\oint_{(C)}\boldsymbol A\cdot \mathrm d \boldsymbol s=\iint\limits_{(S)} \mathrm{rot}\boldsymbol A \cdot \mathrm d \boldsymbol S$

- 旋度的运算法则
  
  - $\mathrm{rot} (C\boldsymbol A) = C\mathrm{rot} \boldsymbol A$
  - $\mathrm{rot} (\boldsymbol A\pm \boldsymbol B) =\mathrm{rot}\boldsymbol A\pm \mathrm{rot} \boldsymbol B $
  - $\mathrm {rot}(u\boldsymbol A) = u\mathrm{rot} \boldsymbol A +(\nabla u)\times \boldsymbol A$

### 场的其他计算公式

- $\mathrm{div}(\boldsymbol A\times \boldsymbol B) =\boldsymbol B\cdot \mathrm{rot}\boldsymbol A$

- $\mathrm{div}(\mathrm{rot} \boldsymbol A) = 0$

- $\mathrm{rot} (\nabla u) = 0$

- $\mathrm{div}(\nabla u)=\Delta u$ 其中 $\Delta=\frac{\partial}{\partial x^2} +\frac{\partial}{\partial y^2} +\frac{\partial}{\partial z^2} $

- $\mathrm{rot}(\mathrm{rot} \boldsymbol A) =\mathbf{grad}(\mathrm{div} A)-\Delta \boldsymbol A$

### 几种重要的特殊向量场

- **Def**：一维单连域、二维单连域

- 无旋场
  
  - **Def**：（保守场）积分与路径无关
  - **Def**：（无旋场）$\nabla \times \boldsymbol A = \boldsymbol 0$
  - **Def**：（有势场，势函数）$\boldsymbol A = \nabla u$
  - **Thm**：在一维单连域上，$A = (P,Q,R) \in C^{(1)}$，TFAE
    - 无旋场
    - 闭曲线上的环量恒为 0
    - 保守场
    - 有势场

- 无源场
  
  - **Def**：（无源场）$\nabla \cdot \boldsymbol A = 0$
  - **Def**：向量管
  - **Thm**：在二维单连域上，$A\in C^{(1)}$，TFAE
    - 无源场
    - $A$ 沿任何一个不子交的闭曲面的通量为零
    - 存在一个向量函数 $\boldsymbol B$ 使得 $\boldsymbol A = \nabla \times \boldsymbol B$

- 调和场
  
  - **Def**：（调和场）既无源、也无旋的场
  - 满足 Laplace 方程
  - 满足 Posisson 方程

<!--TODO: 添加外微分形式！！！ -->

## 补录

### 重积分

- **Def**：（大和，小和）$M_i = \sup\limits_{x\in\Omega_i}\{f(\boldsymbol{x})\},\quad m_i =\inf\limits_{x\in\Omega_i }\{f(\boldsymbol{ x})\}$
  $S^+= \sum M_iV_i,S^-=\sum m_iV_i$

- **Thm**：TFAE
  
  - 可积
  - 大和与小和差的极限为 0 （ $||\Delta||\rightarrow 0$ ）
  - 振幅充分小
  - （积分）大和 = （积分）小和

### 重积分变换

- **Def**：（正则变换）如果一个变换满足
  
  1. $T\in C^{(1)}(G)$
  2. 单射
  3. $\det DT(\boldsymbol u)\neq 0$ 对任一 $\boldsymbol u$成立

- **Def**：（重积分的变换公式）若 $G,T$ 满足以下条件之一：
  
  1. $G$ 是 $R^m$ 中的开集，$T$ 是正则变换， $\Omega$ 是 $G$ 内的闭可测图形，$f\in C(T(\Omega))$
  2. $G$ 同上，$T\in C^1(G)$，$\Omega \in G$ 是闭可测区域，$T$ 是 $\Omega$ 上的正则变换，$f\in C(T(\Omega))$
  
  则：$\int_{T(\varOmega)}f\mathrm dV = \int_\varOmega f\circ T|\det DT|\mathrm dV$

### 外微分形式

### 场论总结

- **Def**：（梯度） $\mathrm{grad} u = \nabla u$，其中 $\nabla$ 算子为 $(\frac{\partial}{\partial x},\frac{\partial}{\partial y},\frac{\partial}{\partial z})$

- **Def**：向量线

- **Def**：（通量、散度）给定向量场 $F$ 和双侧曲面 $S$
  
  - 通量：$\iint_S \boldsymbol{F}\cdot \mathrm d \boldsymbol{s}$
  - 散度：$\mathrm{div} \boldsymbol{F} = \lim\limits_{S\rightarrow M}\frac{\iint_S \boldsymbol{F}\cdot \mathrm d \boldsymbol{s}}{V} = \nabla \cdot \boldsymbol{F}$

- **Def**：（环量、旋度）给定向量场和定向曲线
  
  - 环量：$\oint \boldsymbol{F}\cdot \mathrm d \boldsymbol{s}$
  - 方向旋量：$h_n = \mathrm{rot} \boldsymbol{F}\cdot \boldsymbol{n}$
  - 旋度：$(\frac{\partial R}{\partial y} -\frac{\partial Q}{\partial z})\boldsymbol{i} +(\frac{\partial p}{\partial z}-\frac{\partial R}{\partial x}) \boldsymbol{j} + (\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y})\boldsymbol k$
