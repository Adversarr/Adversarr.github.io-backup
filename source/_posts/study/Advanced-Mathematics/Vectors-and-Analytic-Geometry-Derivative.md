---
title: 多元数量值函数微分学及其应用
date: 2020-6-4
tags:
  - 多元函数
  - 微分
  - 高等数学
math: true
categories: 高等数学
---

到这里，这个学期的内容就大致整理完整了。

<!-- more -->

## n 维 Euclid 空间 R^n 中点集知识

### n 维 Euclid 空间 R^n

- **Def**：n 维实向量
- **Def**：n 维实向量空间（n 维实线性空间）

对加法和数乘满足：(For any a, b in V)

{% note primary %}

1. 交换律
2. 结合律
3. 存在零元（加法）
4. 对任意的 a，存在-a
5. 存在单位元 1 1a=a
6. 对数乘的结合律
7. 对数乘的分配律
8. 对 a, b 的结合律

{% endnote %}

- **Def**：长度（范数）
- **Def**：距离
- **Def**：R^n 中的单位正交基

### R^n 中点列的极限

- **Def**：点列的极限 $\boldsymbol x_i\rightarrow\boldsymbol a$
- **Thm**：点列的极限 iff 点的分量（列）的极限
- **Thm**：点列极限的性质

- 唯一性
- 有界性
- 任一子点列收敛
- $\lim k\times x=ka$
  $\lim x+y=a+b$
  $\lim(x,y)=(a,b)$

- **Thm**：（Bolzano-Weierstrass 定理）有界点列必有收敛子列
- **Thm**：（Cauchy 收敛原理）$x_k$收敛$\iff x_k$为基本列

### 欧式空间中的点集

- **Def**：聚点、导集、闭包、孤立点、闭集

  - **聚点**：存在$A$中不同于$x$的点列，使得以 $x$ 为点列极限
  - **导集**：$A$ 中所有聚点构成的集合 $A'$
  - **闭包**：$\overline A= A\cup A'$
  - **孤立点**：$a\in A-A'$
  - **闭集**：$A'\subseteq A$

- **Thm**：闭集的充要条件

  - $A=\bar A$
  - $\forall \{x_n\} \in A, \lim x_n = x\rightarrow x \in E$
  - $ x \not\in A,\exists U(x)\cap E=\emptyset$

- **Thm**：（聚点原理）有界的无限点集至少有一个聚点

- **Def**：邻域、去心邻域
  - **Thm**：a 是 A 的聚点$\iff \forall U(a), U(a)\cup A\neq \emptyset$
- **Def**：内点、内部（int A）外点、外部（ext A）边界点、边界（\partial A）
- **Def**：开集
  - **Thm**：$A$ 为开集$\iff A^c$为闭集
- **Thm**：开集（闭集）的性质
  - 有限个开集（闭集）的交集（并集）是开集（闭集）
  - 任意个开集（闭集）的并集（交集）是开集（闭集）
- 区域

  - （折线连通）连通开集（开区域）
  - 开区域的闭包=>闭区域

- 紧集
  - **Def**：覆盖（A 的一个覆盖）
  - **Def**：（紧集）A 的任意一个开覆盖必定有一个有限的子覆盖
  - **Thm**：紧集$\iff$有界闭集

## 多元函数的极限和连续性

### 映射

- **Def**：映射
- **Def**：单叶映射
- **Def**：逆映射

### Def：向量函数、数值函数

### 多元数值函数的极限

- **Def**：多元函数的极限
- **Thm**：$\lim f=A\iff \forall S \in U 以a为聚点，都有\lim f= A$
- **Thm**：$\lim x_n=a$ 的点列$x_n->a$
- **Thm**：四则运算法则
- **Thm**：（柯西列扩展）

> **多元函数的重极限**：
>
> 用极坐标变换法求解（需要注意也是对于$\rho\rightarrow0,\theta \in [0,2\pi)$一致成立）

### Def：累次极限

- n 重极限$\Rightarrow$累次极限

> 在这里，翟神某翟给出了一些相关的题目，总结一下：
>
> 1. 累次极限和重极限的关系上，都存在时，几个极限值都必须相等
> 2. 在这里主要是证明重积分不存在。

### 多元连续函数

- **Def**：二元连续函数
  - $x_0$是孤立点
  - $x_0$是聚点，则连续指$\lim f(x)=f(x_0)$
  - **Thm**：四则运算的连续性
  - **Thm**：复合函数的连续性

> 二元连续函数的条件
>
> 1. $f(x, y)$ 在 $I$ 上对 $x$ 的连续性对 $y$ 是一致的.
> 2. $f(x, y)$ 在 $I$ 内任意一点$(x_0, y_0)$ 附近对 $x$ 满足对 $y$ 一致的 Lipschitz 条件.
> 3. $f(x, y)$ 对于变元 $x$ 是单调的.

- 连续函数的性质

  - 有界性
  - 最大值最小值定理
    
    > 紧集上的连续函数有界，并且存在着最大值与最小值.
  - **Thm**：介值定理
  - **Thm**：一致连续性
    
    > Cantor 定理： 紧集上的连续函数是一致连续的.
  - **Def**：道路连通、复合函数的道路连通性

- **Thm**：压缩映射原理

## 偏导数和全微分

### Def：偏导数

- 几何意义
- 可偏导

### Thm：微分中值定理

### Def：全微分

- 矩阵定义
- **Thm**：可微的必要条件

  - 1. 偏导数都存在
  - 2. $L_i(x_0)=$偏导数

- **Thm**：可微的充分条件

  - 偏导数存在且连续

- 全微分的四则运算法则
- 全微分的几何意义

> （翟神某翟的加餐）由上面的叙述，证明函数 f 在点(x0, y0) 处不可微的常用方法有:
>
> 1. 函数 $f$ 在点 $(x_0, y_0)$ 处至少有一个偏导数不存在
> 2. 函数 $f$ 在点 $(x_0, y_0)$ 处不连续
> 3. $\Delta f − f_x(x_0, y_0)\Delta x − f_y(x_0, y_0)\Delta y \neq o(r)$
>
> 例如：$f=\sqrt{|xy|}$在$(0,0)$连续，且偏导都存在，但是不可微。

### 复合函数链式求导法则

- 链式法则矩阵形式 $\mathrm D(\boldsymbol f\circ \boldsymbol g) = \mathrm D\boldsymbol f (\boldsymbol g(\boldsymbol t)) \mathrm D \boldsymbol g(\boldsymbol t)$
- **Thm**：复合函数可微性
- **Thm**：一阶全微分形式不变性

### 方向导数、梯度

- **Def**：方向导数

  - **Thm**：可微=>任意方向导数存在
  - 方向导数的几何意义
  - **Thm**：用偏导数，求方向导数

- **Def**：梯度向量、梯度算子（nabla 算子）
  - **Thm**：若 grad=0，则任何方向导数=0
  - **Thm**：梯度方向，方向导数最大
  - **Thm**：梯度四则运算法则

### 高阶偏导数和高阶全微分

- **Def**：高阶偏导数
- **Def**：混合偏导数

  - **Thm**：混合偏导数和求导顺序无关

- **Def**：高阶全微分
- 复合函数的高阶偏导数
- 一阶全微分形式的不变性
- **Thm**：全微分的有理运算法则

### 隐函数微分法

- **Thm**：隐函数存在唯一性定理
- **Thm**：隐函数可微性定理

## 多元函数的 Taylor 公式和极值问题

**Thm**：多元函数（带拉格朗日余项的）泰勒公式（全微分形式）

- Hessian 矩阵

**Thm**：多元函数（带 Peano 余项的）泰勒公式

## 多元函数几何应用，极值问题

### 曲线表示法

- 空间曲线

  - 参数方程
  - 切线

- 平面曲线
  - 表示法
  - 切线

### 空间曲面表示法

- 切平面方程

### 简单极值问题

- **Def**：（无约束）极值
  - 必要条件：梯度=0
- **Def**：稳定点（梯度 = 0）
- **Thm**：f 在 x_0 取极小值（极大值），则 Hessian 矩阵是正定或半正定的（负定或半负定的）

### 有约束的极值

- **Def**：约束极值
  - Lagrange 乘数法

## 几何应用

### 曲线的切线和法平面

- 曲线的参数方程
- 简单曲线和有向曲线
- 曲线的切线和法平面

> 切线的求法：
>
> 如果给出了 $\boldsymbol x=\boldsymbol{x}(t)\rightarrow \boldsymbol{x}=\dot{\boldsymbol{x}}t+\boldsymbol{x}(t_0)$
>
> 如果给出了：$F=G=0$
>
> 则切向量 $\eta=(\frac{\partial (F,G)}{\partial (y,z)},\frac{\partial (F,G)}{\partial (z,x)},\frac{\partial (F,G)}{\partial (x,y)}) =\nabla F\times \nabla G$
>
> 法平面随之求出

### 弧长

- **Def**：弧长
- **Thm**：弧长的计算公式（参考第一型曲线积分）
- 弧微分和自然参数

### 曲线的切平面和法线

- 曲面的参数方程
- 曲面上曲线的表示
- 曲线的切平面和法线
  - 切平面
  - 法线、法向量
  - 光滑曲面

> 实际上都是求法向量
>
> 1. 显式给出曲面方程
>    假设曲面方程 $z=f(x,y)$ 则在 $P$ 处，$f_x\mathrm dx+f_y\mathrm dy-dz=0$ 则法向量为 $\eta =(f_x,f_y,-1)$
> 2. 由参数方程给出曲面方程 $\boldsymbol{r}=\boldsymbol{r}(u,v)=\boldsymbol{r}(x,y,z)$
>    则法向量 $\eta=\boldsymbol r_u\times \boldsymbol{r}_v=(\frac{\partial (y,z)}{\partial(u,v)},\frac{\partial (z,x)}{\partial(u,v)},\frac{\partial (x,y)}{\partial(u,v)})$
> 3. $F(x,y,z)=0\rightarrow \eta = (F_x,F_y,F_z)$

### 空间曲线的曲率和挠率

- Frenet 标架

  - $T=\boldsymbol{r}'$ 切线、法平面 $(\rho-\boldsymbol{r}(s_0))\cdot r'(s_0)=0$
  - $\displaystyle B=\frac{\boldsymbol{r}'\times\boldsymbol{r}'' }{||\boldsymbol{r}''||}$ 次（负）法线、密切平面 $B\cdot(\rho -\boldsymbol{r}(s_0))=0$
  - $\displaystyle N=\boldsymbol{r}''=\frac{\boldsymbol{r}''}{||\boldsymbol{r}''||}$ 主法线，从切平面

- 曲率

  - **Def**：曲率$\kappa = \lim \limits_{\Delta t \rightarrow 0} |{\frac { \Delta \theta}{\Delta s}}|$
  - **Def**：$\kappa (s) = ||r''(s)||$

- 曲率半径、曲率圆

- 挠率：$\displaystyle\tau=-B'\cdot N =\frac{[r'~r''~r''']}{||r''||^2}$

> $t$ 坐标下的 Frenet 标架
>
> 1. $\displaystyle T=\frac{\dot r}{|\dot r|}$
> 2. $\displaystyle B =\frac{\dot r\times \ddot r}{|\dot r\times \ddot r|}$
> 3. $\displaystyle N = B\times T$
> 4. $\displaystyle \kappa(s)=\kappa(t) =\frac{||\dot r\times\ddot r||}{||\dot r||^3}=\frac{||\dot x\ddot y-\dot y\ddot x||}{||\dot x^2+\dot y^2||^{3/2}}$
>    平面曲线：$\displaystyle\kappa =\frac{|y''|}{(1+y'^2)^{3/2}}$
> 5. $\tau(t)=\frac{[r'(t)~ r''(t)~r'''(t)]}{||r'(t)\times r''(t)||^2}$

最后给出 Frenet 公式的矩阵形式：

$$
\left(\begin{matrix}
T'\\N'\\B'
\end{matrix}\right)=\left(\begin{matrix}
  0&\kappa&0\\
  -\kappa&0&\tau\\
  0&-\tau&0\\
\end{matrix}\right)
\left(\begin{matrix}
	T\\N\\B
\end{matrix}
\right)
$$
