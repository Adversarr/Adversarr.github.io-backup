---
layout: post
title: 线性方程组的数值解
group: group-numeric-recipies
order: 3
categories: [数学]
tags:
  - 数值分析
sidebar: [group-numeric-recipies, toc]
---

数值分析 ch 3 - 线性方程组的数值解

<!-- more -->


# Chapter 3 线性方程组的数值解

Content：

1. Gauss 消去法，Gauss列主元消去法

2. 向量和矩阵的范数、方程组性态和误差估计

3. Jacobi迭代，Gauss-Seidel迭代格式，收敛性的判别

4. 幂法和反幂法

---

迭代解法描述：

$$
\begin{aligned}A\vec x=\vec b\iff\vec x&=B\vec x+\vec c\\\vec x_{n+1}&=B\vec x_n+\vec c\\
if~x_n~converge,~\vec x_n&\rightarrow \vec x^*
\end{aligned}
$$


Today's outline:

1. 解线性方程组的可操作的解法

  1. 直接法：不考虑舍入误差，通过有限步运算一定能得到**精确解**

例如：Kramer's law

    - $A=(\vec a_1, \vec a_2,\cdots)$$A_i = (\vec a_1,\cdots,\vec a_{i-1},\vec b,\vec a_{i+1},\cdots,\vec a_n)$$x_i = |A_i|/|A|$

  2. 消元法：Gauss

  3. 间接法：通过有限次运算得到近似解→如何刻画

2. 矩阵/向量的范数 误差估计

3. 迭代法求解（近似解）

  1. 恒等变形：

$$
Ax=b\iff x = Bx+f
$$


  2. 构造迭代序列：（由 $B$和 $x_0$完全决定）

$$
x_{k+1}=Bx_k+f
$$


  3. 如果序列收敛，则：

$$
x^*=Bx^*+f
$$


  4. 对于充分大的$k$，有 $x_k\approx x^*$

4. 计算矩阵A的最大（小）特征值

## Gauss 消元法

> 思想：利用线性代数中学过的初等行变换，将方程组化为等价的三角形方程组


### 三角形方程组的回代法

$$
\begin{aligned}
u_{11}x_1+\cdots +u_{1n}x_n=y_1&\\
\cdots&\\
u_{nn}x_n=y_n&\end{aligned} 
$$


$$
\begin{cases}
x_n=y_n/u _{nn}\\
x_i = (y_{n-1}-\sum _{j=i+1}^n u_{ij}x_j)/u_{ii}
\end{cases}
$$


### Gauss 消去法

1. 将 $Ax=b$化为增广矩阵：$\overline A^{(1)}$

> 同解变换：非零数乘一个方程两边，互换位置，一个方程乘常数+另一个方程


2. 下面用n-1步消元，将$\overline A^{(1)}$转化为上三角矩阵

$\bar A^{(1)}\rightarrow \bar A^{(2)}\rightarrow\cdots\rightarrow \bar A^{(n)}$

3. 三角形方程组回代

→$O(n^3)$

**Thm**：（充分条件）若 A 的各阶顺序主子式非零，则Gauss消去法中各**主元**$a_{kk}^{(k)}$均非零。

### 三对角方程组的追赶法

$$
\left[\begin{matrix}
b_1&c_1\\
a_2&b_2&c_2\\
&a_3&b_3&c_3\\&&&\cdots
\end{matrix}\right]x = d
$$


且对角占优：$|b_i|>|a_i|+|c_i|$

消元过程如下：

$\beta_1=b_1,y_1=d_1,l_i=\frac {a_i} {\beta _{i-1}},\beta_i=b_i-l_ic_{i-1},y_i=d_i-l_iy_{i-1}$

### 列主元Gauss消元

→ $|a_{tk}^{(k)}|=\max_{k\le i\le n}|a_{ik}^{(k)}|$

### LU分解法

Gauss消元→行变换L→$L=(L_k^{-1}L_{k-1}^{-1}\cdots L_1^{-1})$→$LUx=b$→$Ly=b,Ux=y$

**Thm** A的各阶顺序主子式均不为0，则对A可做唯一的LU分解

**Thm**若A是对称矩阵，且各阶顺序主子式不为0，则A可以做LU分解，且

$$
l_{ik}=\frac {u_{ki}}{u_{kk}}

$$


## 方程组的性态和误差分析 #IMPORTANT

如何刻画一个矩阵A的性态→矩阵的条件数（与矩阵的模有关）

### 向量范数

**Def**（范数）一个函数，满足：非负性、齐次性、三角不等式

- 常用的：

  1. 1-范数

  2. ∞-范数

  3. 2-范数←内积

**Thm**：**有限维空间所有的模都是**等价**的**（$\exists c_1,c_2\forall x\in R^n,c_1||x||_p\le ||x||_q\le c_2||x||_p$)

> 定性描述为：两个范数等价是指在一个范数顶一下的向量，在另一个范数下也小


借助这样的理论：我们研究 两个向量之间的绝对误差和相对误差：

> 设$x^*$和$\tilde x$是方程组$Ax=b$的精确解和近似解，则$||x^*-\tilde x||, ||x^*-\tilde x||/||\tilde x||$可以表示其误差


### 矩阵范数

借助向量模定义矩阵模

**Def**（矩阵范数）一个函数，满足

1. 非负性$||A||\ge0 且||A||=0\iff A=0$

2. 齐次性$||\alpha A||=|\alpha|||A||$

3. 三角不等式$||A+B||\le ||A||+||B||$

4. $||AB||\le ||A||~||B||$

5. 相容性$||Ax||\le ||A||~||x||$

> 矩阵的行列式**不可以**作为范数


**Def**（向量范数导出的算子范数） 设 $||\cdot||$是一个范数，称$\max_{x\in R^n} \frac{||Ax||}{||x||}=\max_{x\in R^n,||x||=1}||Ax||$为A的向量范数导出的算子范数$|||A|||$

**Def**（谱Spectrum半径）设$B\in R^{n\times n}$，$\lambda_1,...,\lambda_n$为特征值，谱半径为：

$$
\rho(B)=\max \{\lambda_i\}
$$


**Thm**：常用矩阵范数计算

1. $||A||_1=\max_{1\le j\le n}\sum_{i=1}^n$=最大列绝对值和

2. $||A||_\infty$=最大行绝对值和

3. $||A||_2=\sqrt{\rho(A^TA)}$

4. $||A|_F=\sqrt{\sum_{i,j=1}^na_{ij}^2}$→ 注意！不是算子范数！例如 $||I||\ne 1$

**Thm**：对于对称矩阵，$\rho(A)=||A||_2$

**Thm**：对于**任意**范数$\rho(A)\le ||A||$

> 可用于证明迭代法收敛！


**Thm**： $R^{n\times n}$ 中的任意两个矩阵范数是等价的

> 【推广】有限维空间中的两个范数是等价的。


**Thm**：对于两个矩阵范数，存在常数$d_1$和$d_2$满足：

$$
d_1||A||_p\le ||A||_q\le d_2||A||_p
$$


**Def**（矩阵之间的距离）$||A-B||$

**Def**（矩阵收敛）$\lim_{k\rightarrow \infty} ||A^{(k)}-A||=0\iff \lim_{k\rightarrow \infty} A^{(k)}=A$

**Thm**：$\lim_{k\rightarrow \infty} B^k=0\iff \rho(B)<1$

例如：

$$
\begin{aligned}
\frac 1{1-q}&=1+q+q^2+\cdots\\
(I-A)^{-1}&=I+A+A^2+\cdots
\end{aligned}
$$


### 方程组的性态和条件数

> 矩阵的行列式可以一定程度上的表示误差大小，而用条件数进行精确刻画。


1. 设$b$有一个小的扰动$\delta b$，此时解变为$x^*+\delta^*$

2. 则有$A\delta x^*=\delta b$，也就是$\delta x^*=A^{-1}\delta b$

3. 取范数：

$$
\frac{||\delta x^*||}{||x^*||}\le ||A^{-1}||~||A||\frac{||\delta b||}{||b||}
$$


1. 设$A$有微小变化$\delta A$

2. 则$\delta x^*=-A^{-1} \delta A(x^*+\delta x^*)$

3. 取范数：

$$
\frac{||\delta x^*||}{||x^*+\delta x^*||}\le ||A^{-1}||~||A||~\frac {||\delta A||}{||A||}
$$


**Def**（条件数$\mathrm {cond}A$）$A$为非奇异矩阵，则称 $||A^{-1}||~||A||$为条件数

**Def**（好的方程组）对于Ax=b而言，若

1. A的条件数很大，则为**病态方程组**（误差不一定大）

2. A的条件数很小，则为**良态方程组**（误差一定小）

常用的判断方法：

1. 列主元Gauss消去法出现绝对值很小的pivot

2. 系数矩阵中，某些行（列）近似线性相关

3. 系数矩阵元素间，数量级差距很大，且没有一定的规律

一般的解决方案：

1. 提高计算精度

2. **预处理**：选择合理的非奇异矩阵$D,C$，将方程组化为等价的方程组，$DAC[C^{-1}]=Db$且使得$\mathrm{cond} DAC$较小

例如：正则化方法：$Ax=b,|A|\approx 0$→$x=(\alpha I+A^TA)^{-1}A^Tb$

## 迭代法（Jacobi迭代，Gauss-Seidel迭代）

### 迭代格式的构造

将方程组改写为等价的方程：

$$
x=Bx+f
$$


通过该格式进行迭代，若迭代格式对于任意初始向量产生的迭代序列 $\{x^{(k)}\}$都收敛，则**迭代收敛**

> 对于线性方程组而言，迭代收敛只与$B$有关；对于非线性方程组而言，和 $B,x$ 都有关。


### 三种常用的迭代格式

#### Jacobi迭代法

假设对角线元素都非零，则可以通过该公式得到：

$$
\begin{aligned}
x_1 = (b_1-a_{12}x_2-\cdots - a_{1n}x_n)/a_{11}\\
\cdots\\
x_n = (b_n - a _ {n1} x_1 - \cdots - a_{n,n-1}x_{n-1})/a_{nn}
\end{aligned}
$$


若将原矩阵进行重写：

$$
A=\tilde L+D+\tilde U

$$


- $J = -D^{-1}(L+U)$

- $f_J=D^{-1}b$

#### Gauss-Seidel迭代

我们用已经求出的 $x^{(k)}_{i}$代入后续所有计算，即为Gauss-Seidel格式：

$$
x^{(k+1)}=D^{-1}(b-Lx^{(k+1)}-Ux^{(k)})
$$


最终的迭代格式为：

$$
x^{(k+1)}=Gx^{(k)}+f_G
$$


- $G=-(D+L)^{-1}U$

- $f_G=(D+L)^{-1}b$

#### SOR（逐次超松弛）迭代格式

$$
x^{(k+1)}=(1-\omega )x^{(k)}+\omega D^{-1}(b-Lx^{(k+1)}-Ux^{(k)})
$$


$\omega$称为松弛因子，当 $\omega =1$时，即为Gauss-Seidel迭代。

最终格式为：

$$
x^{(k+1)}=S_\omega x^{(k)}+f_\omega
$$


- $S_\omega =(D+\omega L)^{-1}[(1-\omega)D-\omega U]$

- $f_\omega =\omega (D+\omega L)^{-1}b$

### 迭代格式的收敛性

#### 迭代法基本定理

**Thm**：迭代格式 $x^{(k+1)}=Bx^{(k)}+f$收敛的充分必要条件是 $\rho(B)<1$

**Thm**：若迭代格式 $||B||<1$，则$x^{(k+1)}=Bx^{(k)}+f$收敛。「[Thm：对于任意范数\rho(A)\le ||A||](https://www.wolai.com/4bZTUKfKuKiHhhaEUmhhDC)」同时：（误差的先验估计和后验估计）

1. $||x^*-x^{(k+1)}||\le ||B||~||x^*-x^{(k)}||$

2. $||x^*-x^{(k)}||\le \frac {||B||}{1-||B||} ||x^{(k)} - x^{(k-1)}||$

3. $||x^*-x^{(k)}||\le \frac {||B||^k}{1-||B||} ||x^{(1)} - x^{(0)}||$

#### Jacobi迭代和Gauss-Seidel迭代的收敛性

1. Jacobi迭代法收敛$\iff\rho(J)<1$

2. Gauss-Seidel迭代法收敛$\iff \rho(G)<1$

> 严格行对角占优： $|a_{ii}|\ge\sum_{j,i\ne j}|a_{ij}|$


> 严格列对角占优：$|a_{jj}|\ge\sum_{i,i\ne j}|a_{ij}|$


**引理** 若A是严格对角占优的，则 $|A|\ne0$

**Thm** 如果对于矩阵 $Ax=b$ 是严格对角占优的，则Jacobi迭代和Gauss-Seidel迭代收敛。

#### SOR迭代法的收敛性

**Thm** SOR迭代收敛的必要条件是 $0<\omega<2$

**Thm** 若A对称正定，且 $0<\omega<2$则SOR迭代法收敛

> **Thm** 若A对称正定，则Gauss-Seidel迭代法收敛


> Homework ：P124:28 30 32(1,2) 34


## 幂法和反幂法

> 么


### 求主特征值的方法

**Def**（主特征值）若将$A$线性无关的特征向量对应的特征值$\lambda_j$按模大小排列，有$\max{|\lambda_j|}=|\lambda_1|$为主特征值。

**Thm** 幂法：

$$
\begin{cases} u_0=v_0\\v_k=Au_{k-1}\\m_k=\max(v_k)\\u_k=v_k/m_k \end{cases}
$$


**Thm** 若满足$|\lambda_1|>|\lambda_2|\ge\cdots$，则通过幂法得到的序列有如下极限：

$$
\begin{cases} m_k\rightarrow \lambda_1\\u_k\rightarrow \frac{x_1}{\max x_1} \end{cases}
$$


### 反幂法

求最小特征值：用$A^{-1}$代替$A$计算


