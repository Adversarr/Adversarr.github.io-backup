---
layout: post
title: 多项式插值和函数最佳逼近
group: NumericRecipies
categories: [数学]
tags:
  - 数值分析
---

数值分析 ch 4 多项式插值和函数最佳逼近

<!-- more -->

# Chapter 4 多项式插值和函数最佳逼近

1. 给定一个函数： $f(x)\in[a,b]$

在离散点处的值，能否给出一个近似？

## 函数近似和函数逼近

### 函数近似表示：可能性

**Def**（插值函数）设函数 $y=f(x)$在区间$[a,b]$上有定义，且已知在$a\le x_0<\cdots<x_n\le b$上的值，若存在一个简单函数$P(x)$使

$$
P(x_i)=f(x_i)\quad (i=0,1,\dots,n)
$$


成立，则称$P(x)$为$f(x)$的**插值函数**，上式称为**插值条件**，点$x_0,x_1,\dots,x_n$称为插值节点，$[a,b]$称为**插值区间**。求$P(x)$的方法称为差值法。

**Thm**（存在n次多项式插值）满足插值条件的n次多项式$p_n(x)$存在且唯一。

> 存在性：可以构造出Lagrange表示
唯一性：代数基本定理


 ```Markdown
 存在性：
 - 构造范德蒙矩阵
 - 范德蒙矩阵的行列式 |X| ≠ 0
 ```


范德蒙行列式：

$$
|X| = \prod_{0\le i<j\le n} (x_i-x_j)
$$


### 基本插值**多项式**

求n次多项$l_k(x)$满足：

$$
$l_k(x_j)=(j==k)$
$$


由条件4知道$x_0,x_1...,x_{k-1},x_{k+1},...,x_n$是$l_k(x)$的零点。所以$l_k(x)$有n个因子：$x-x_0,...x-x_{k-1},...,x_{k+1},...,x-x_n$，所以

$$
l_k=A_k \prod _{i\ne k} (x-x_i)
$$


其中：

$$
A_k=\cfrac{1}{\prod_{i\ne k}(x_i-x_k)}
$$


则$l_k(x)$称为n次（第$k$个）**基本插值多项式**（也就是**Lagrange插值基函数**）

### Lagrange插值多项式

**Thm**：设$x_0, x_1, \cdots,x_n$是互异节点，则存在唯一的次数不超过$n$次的多项式$L_n(x)$，使得$L_n(x_i)=f(x_i)$

用Lagrange（选择$l_k(x)$为基函数），组合后的系数即为$f(x_i)$：

$$
L_n(x)=\sum_{k=0}^nf(x_k)l_k(x)=\sum _{k=0} ^ nf(x_k)\prod_{i\ne k,i=0}\frac{x-x_i}{x_k-x_i}
$$


称为**n次Lagrange插值多项式**

### 插值余项和误差估计

**Def**（余项）$R_n(x)=f(x)-L_n(x)$为插值多项式的**余项**（一般的为$R_n(x)=f(x)-p_n(x)$）

**Thm**：设$f(x)$在$(a,b)$内有$f^{(n+1)}(x)$存在，$L_n(x)$为Lagrange插值多项式，则对于任意$x\in [a,b]$，$\exists \xi\in (a,b),s.t. R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}W_{n+1}(x)$，其中$W_{n+1} (x) = \prod_{i=0}^n(x-x_i)$

注：

1. $\xi$依赖于$x$

2. 一般不能求出，只能估计误差

## 差商和牛顿插值

Lagrange插值的缺点：节点增加或减少时，所有插值基函数的系数都可能变化（计算不变）

设$L_{k}(x)$时以$x_0,x_1,...,x_{k}$为插值节点的多项式，考察$L_k$和$L_{k-1}$的关系：

$$
let\quad g(x)=L_k(x) - L_{k-1} (x)
$$


从而：$g$时一个次数不超过$k$的多项式，也就是说，$L$可以写成

$$
L_k(x) = a_0+a_1(x-x_0) + \cdots + a_k(x-x_0)(x-x_1)\cdots(x-x_{k-1})
$$


求出 $a_k$：

$$
a_k = \sum_{m=0}^k\frac{f(x_m)}{\prod\limits_{i\ne m,i=0}^k(x-x_i)}
$$


### 差商和Newton插值公式

**Def**：设已知函数$f(x)$在$n+1$个互异节点上的值为$f(x_0),...,f(x_n)$称：

$$
f[x_i,x_j] =\frac{f(x_j)-f(x_i)}{x_j-x_i}
$$


为节点$x_i,x_j$的一阶差商，其一阶差商的差商：

$$
f[x_i,x_j,x_k]=\frac{f[x_j,x_k] - f[x_i,x_j]}{x_k-x_i}
$$


为二阶差商，以此类推。约定零阶差商为函数值。

**Thm**：k阶差商可以表示成$f(x_0),f(x_1),...,f(x_k)$的线性组合。

$$
f[x_0,x_1,\cdots,x_k] = \sum_{m=0}^k \frac{f(x_m)}{\prod_{i=0,i\ne m}^k(x_m-x_i)} =a_k
$$


则：

$$
L_n(x) = f(x_0) + f[x_0,x_1](x-x_0) + ...+f[x_0,x_1,...,x_n](x-x_0)(x-x_1)...(x-x_{n-1})
$$


**Thm**：k阶差商与节点的次序无关。

**Thm**：k阶差商和k阶导数有如下关系$f[x_0,...,x_k]=\frac{f^{(k)}(\eta)}{k!}\quad \eta \in (\min\{x_0,...,x_k\}, \max\{x_0,...,x_k\} )$

### 差分和等距节点的Newton插值多项式

**Def**：若已知函数$f(x)$在等距节点$x_i$上的函数值为$f(x_i) = f_i(i = 0, 1, ...,n)$则称 $f_{i+1} - f_i$为$f(x)$在$x_i$处以$h$为步长的1阶**向前**差分$\Delta f_i$。$\Delta^k f_i = \Delta^{k-1} f_{i+1} -\Delta^{k-1} f_{i}$为k阶差分。

可以证明，差分和差商有如下关系 ：

$$
f[x_i,x_{i+1},\cdots,x_{i+k}]=\frac{\Delta^k f_i}{k!h^k}
$$


从而可以得到Newton插值多项式：

$$
\begin{aligned}

N_n(x)&=\sum_{k=0}^n f[x_0, x_1,\cdots, x_k]\prod_{j=0}^{k-1}(x-x_j)\\
N_n(x_0+th)&=\sum_{k=0}^n \frac{\Delta^kf_0}{k!} \prod_{j=0}^{k-1} (t-j)
\end{aligned}
$$


第二个式子称为n次Newton前插公式。

## 高次插值的缺点、分段低次插值

### 埃尔米特插值(Hermite)

**Def**：给定$[a,b]$中的$n+1$个互异的节点及其函数值和直到$m_i$阶导数$f(x_i),f'(x_i),...,f^{(m_i)}(x_i)$，令$m=\sum_{i=0}^n(m_i+1)-1$若存在一个次数不超过$m$次的多项式$H_m(x)$，满足所有条件，则称$H_m(x)$为$f(x)$的$m$次Hermite插值多项式。

**Thm**：满足该插值条件的$m$次多项式$H_m(x)$是存在且唯一的。

**Thm**：设$H_m(x)$是满足条件的m次插值多项式，$f(x)$在包含$n+1$个互异节点$x_0,x_1,\dots,x_n$的区间$[a,b]$上有m阶连续导数，且在$(a,b)$上有$m+1$阶导数 ，则对于其中每一个点，一定存在$\xi$使得：

$$
R_m(x) = \frac{f^{(m+1)}(\xi)}{(m+1)!}\prod _{i=0}^n (x-x_i)^{m_i+1} 
$$


**Thm**：（Hermite-Gennochi）若 $f\in C^n[a,b],x_i\in [a,b],i = 0, 1, ...,n$且互异，则：

$$
f[x_0,\dots,x_n]=\int\mathop\cdots\limits_{\tau_n}\int f^{(n)}(t_0x_0+ t_1x_1+\cdots + t_nx_n)\mathrm dt_1\cdots\mathrm dt_n
$$


其中 $\\tau _ n = \left\{ { (t _ 1,\dots,t _ n) |t_i\ge 0, \sum t _ i \le 1 }\right\}$为n维单纯形，而$t _ 0 = 1- \sum_{i=1} ^n t _ i$ .

扩展差商的定义（**重节点插值**）：

$$
f[x_0,x_0] = \lim _{x\rightarrow x_0} f[x_0, x] =f'(x_0)\\
f[x_0,...,x_0] = \frac{f^{(k)}(x_0) }{k!}
$$


从而：

$$
\begin{aligned}
H_m(x) = &f(x_0) + f[x_0,x_0](x-x0) + \cdots + f[x_0, \cdots,x_0](x-x_0)^{m_0}\\
&+f[x_0,\cdots,x_0,x_1] (x-x_0)^{m_0+1} + \cdots +\\
&f[x_0,\cdots, x_0, x_1\cdots x_1](x-x_0)^{m_0+1} (x-x_1)^{m_1}+\cdots\\
&+f[x_0,\cdots,x_n](x-x_0)^{m_0+1}\cdots(x-x_{n-1})^{m_{n-1}+1}(x-x_n)^{m_n}
\end{aligned} 
$$


插值余项为：

$$
f(x)-H_m(x)=\frac{f^{(m+1)}(\xi)}{(m+1)!}\prod_{i=0}^n(x-x_i)^{m_i+1}
$$


## 高次插值的缺点和分段线性插值

常见的问题：个数多→误差大

> 在[数值分析](https://www.wanweibaike.com/wiki-数值分析)领域中，**龙格现象**是在一组等间插值点上使用具有高次多项式的多项式插值时出现的区间边缘处的振荡问题。 它是由[卡尔·龙格](https://www.wanweibaike.com/wiki-卡爾·龍格)（Runge）在探索使用多项式插值逼近某些函数时的错误行为时发现的。[[1]](https://www.wanweibaike.com/wiki-龙格现象#cite_note-1)这一发现非常重要，因为它表明使用高次多项式插值并不总能提高准确性。 该现象与傅里叶级数近似中的吉布斯现象相似。——Wikipedia


### 分段线性插值

> 在[数值分析](https://www.wanweibaike.com/wiki-数值分析)这个数学分支中，**样条插值**是使用一种名为[样条](https://www.wanweibaike.com/wiki-样条)的特殊[分段](https://www.wanweibaike.com/wiki-分段)[多项式](https://www.wanweibaike.com/wiki-多项式)进行插值的形式。

在[数学](https://www.wanweibaike.com/wiki-数学)学科[数值分析](https://www.wanweibaike.com/wiki-数值分析)中，**样条**（Spline）是一种特殊的[函数](https://www.wanweibaike.com/wiki-函数)，由[多项式](https://www.wanweibaike.com/wiki-多项式)分段定义。


若给出$f(x)$在n+1个节点上的数据表，则线性插值：

$$
L_{1,i} (x) = f(x_i) + f[x_i, x_{i+1}](x-x_i)\\
\tilde L_1(x) = \begin{cases}
L_{1,0}(x),&x\in[x_0,x_1)\\
L_{1,1}(x),&x\in[x_1,x_2)\\
\vdots\\
L_{1,n-1}(x),&x\in [x_{n-1},x_n]
\end{cases} 
$$


其插值误差为：

$$
\max_{a\le x\le b}|f(x) - \tilde L_1(x)| \le \frac 1 8 h^2 \max_{a\le x\le b}|f''(x)|
$$


→产生了**尖点**（不光滑）

需要的：

1. 小区间上是多项式

2. 两个相邻区间内光滑连接

→ 三次样条插值

## 三次样条插值

**Def**：设在区间$[a,b]$上的n+1个插值节点

$$
a=x_0<x_1<\cdots<x_n=b
$$


及其函数在节点上的值$y_i$，若存在函数$S(x)$满足：

1. $S(x_j)=y_j$

2. $S(x)$在每个小区间上都是三次多项式

3. $S\in C^2[a,b]$

则称为三次样条插值函数

由于在边界上缺少边界条件，通常在端点上2个附加条件（**边界条件**）：

1. （第一型）已知一阶导数

2. （第二型）已知二阶导数

3. （第三型）周期边界条件

### 三次样条插值函数的求法

从二阶导数入手：

$$
S''(x_j)=M_j, S''(x_{j+1})=M_{j+1}
$$


令$h_j = x_{j+1}-x_j$则：

$$
S(x) =y_j+c_j(x-x_j)+\frac 1 2 M_j(x-x_j)^2+ \frac 1 {6h_j}(M_{j+1} - M_j)(x-x_j)^3,x\in [x_j,x_{j+1}]
$$


代入一次导数连续：

$$
S'(x_j)=S'(x_{j+1})
$$


则

$$
\mu_j M_{j-1} +2M_j+\lambda _jM_{j+1}=d_j\\
\mu_j = \frac{h_{j-1}}{h_{j-1}+h_j},\quad\lambda_j = 1 - \mu_j,\quad d_j=6f[x_{j-1}, x_j,x_{j+1}]
$$


即可构造出三对角矩阵，若给出第一型条件$d_0 = 6f[x_0,x_0,x_1]$, $d_1 = 6f[x_{n-1}, x_n,x_n]$：

$$
\left[\begin{matrix}
2&1\\
\mu_1&2&\lambda_1\\
&\mu_2&2&\lambda_2\\
&&\ddots&\ddots&\ddots\\
&&&\mu_{n-1}& 2& \lambda_{n-1}\\
&&&&1 &2
\end{matrix}\right]

\left[\begin{matrix}
M_0\\M_1\\M_2\\\vdots\\M_{n-1}\\M_n
\end{matrix}\right] =
\left[\begin{matrix}
d_0\\d_1\\d_2\\\vdots\\d_{n-1}\\d_n
\end{matrix}\right]  
$$


### 三次样条插值函数的收敛性

**Thm**：设被插值函数四阶连续，则在插值区间上有

$$
||f^{(k)}-S^{(k)}||_\infty \le c_kh^{4-k}||f^{(4)}||_\infty,\quad k = 0, 1, 2\\h = \max_{0\le j\le n-1}h_j,c_0 = 1/16, c_1=c_2=1/2
$$


## 最佳一致逼近

### 线性赋范空间

**Def**（线性空间）若$\forall x,y\in X, \lambda x\in R,\lambda x\in X, x+y\in X$则称$X$为线性空间。

[Def（范数）一个函数，满足：非负性、齐次性、三角不等式](https://www.wolai.com/aUj4aLWYjNtp7jA2QAGq6w)←[Chapter 3 线性方程组的数值解](https://www.wolai.com/hF3aUaiBe35x1FMpgPX15q)

**Def**（线性赋范空间）对应的空间称线性赋范空间

**Def**（距离）$X$是线性赋范空间，$x,y\in X$则称$||x-y||$为$x$$y$之间的距离

**Def**（最佳逼近元）$X$是线性赋范空间，$M\sube X$若存在$\varphi \in M$使得$\forall \psi\in M$有

$$
||f-\varphi||\le ||f-\psi||
$$


则称$\varphi$是$f$在$M$中的最佳逼近元

### 最佳一致逼近多项式

**Def**（最佳一致逼近多项式）若$\exist p_n\in M_n$使得$\forall q_n\in M_n$

$$
||f-p_n||_\infty \le ||f-q_n||_\infty
$$


**Thm**：n次最佳一致逼近多项式是存在且唯一的

**Def**（偏差点）$|g(x_0)|=||g||_\infty = \max_{a\le x\le b}|g(x)|$（又分正偏差点、负偏差点）

**引理1**：对于最佳一致逼近多项式，$f-p_n$必存在正负误差点。

**Thm**：设$f\in C[a,b]$，$p_n(x)$是n次多项式，则$p_n(x)$是$f(x)$的$n$次最佳一致逼近多项式$\iff$$f(x)-p_n(x)$在$[a,b]$上至少有n+2个交错偏差点。$a\le x_0 < x_1 < \cdots < x_{n + 1} \le b$

$$
f(x_i)-p_n(x_i)=(-1)^i\sigma ||f-p_n || _\infty
$$


**推论1**：若$f^{(n+1)} $在$(a,b)$上存在且保号，则$f(x)-p_n(x)$在$[a,b]$内恰好有$n+2$个交错偏差点，且两端点都是偏差点。

**推论2**：$p_n(x)$是$f(x)$的某一个n次插值多项式

## 最佳平方逼近

### 内积空间

**Def**（内积空间和内积）：若$X$是一个线性空间，若$\forall x,y$有实数与之对应$(x,y)$，且

1. $\forall x,y \in X,~(x,y)=(y,x)$

2. $\forall x,y \in X,\lambda\in R,~(\lambda x,y)=\lambda(x,y)$

3. $\forall x,y,z\in X,(x,y+z)=(x,y)+(y,z)$

4. $\forall x\in X, (x,x)\ge 0, (x,x)=0\iff x=0$

**Def**（正交）：$(x,y)=0$

**Thm**：柯西-施瓦茨不等式

### 最佳平方逼近

设$X$是内积空间，$(\cdot,\cdot)$是内积，M是X的有限维子空间，$\varphi_0,...,\varphi_m$是M的一组基。求$\varphi\in M$使得：$\varphi = \arg\min_{\psi\in M} ||f-\psi||$，则称$\varphi$为$f$在$M$中的最佳平方逼近元

记：$\varphi = \sum c_i \varphi _i,\quad\psi = \sum a_i\varphi _i$，问题变为求解$c$

$$
\left[
(\varphi_i, \varphi_j)
\right][c_0,c_1,...,c_m]^T = [(f, \varphi_0), (f,\varphi_1),...,(f,\varphi_m)]

$$


上述方程组称为正规方程组。

**引理**：正规方程组是对称正定的。

**Thm**：正规方程组存在唯一解，且为$||f-\sum a_i\varphi_i||^2$的最小点。

### 超定线性方程组的最小二乘解

$$
\left[a_{i,j}\right] [x_1,x_2,\dots,x_n]^T = [b_1,b_2,\dots,b_m]^T
$$


其中：$m>n$

$$
A^TAx=A^Tb
$$



