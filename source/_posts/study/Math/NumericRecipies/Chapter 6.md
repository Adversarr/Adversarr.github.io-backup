---
layout: post
title: 数值分析-常微分方程的数值解
group: group-numeric-recipies
order: 5
categories: [数学]
tags:
  - 数值分析
  - 常微分方程
sidebar: [group-numeric-recipies, toc]
plugins:
  - mathjax
---

数值分析 Chapter 6 常微分方程的数值解

<!-- more -->

主要内容：

1. Euler公式、后向Euler公式、梯形公式、改进的Euler公式、局部截断误差和阶数
2. R-K方法
3. 单步的收敛性和稳定性
4. 线性多步法（Adams显式、隐式公式，基于Taylor展开的线性多步法的构造）

主要讨论一阶常微分方程初值问题的数值解：

$$
\begin{cases}
    y' = f(x,y),& a\le x \le b\\
    y(a) = \eta.
\end{cases}
$$

假设其存在唯一解，且充分光滑，在解的邻域内 $f(x, y)$ 和 $\displaystyle \frac{\partial f(x,y)}{\partial y}$ 连续。

将$[a,b]$作$n$等分，作$h=(b-a)/n$和$x_i=a+ih$

在计算$y_i$时，

1. 如果只用到前一步的值$y_{i-1}$：**单步法**
2. 如果用到前$r$步的值：$r$步方法。

---

## Euler方法

### Euler公式的构造

将两边积分：
$$
\int_{x_i}^{x_{i+1}} y'(x) \mathrm dx = \int _{x_i} ^{x_{i+1}} f(x, y(x))\mathrm dx\\
\Rightarrow y(x_{i+1}) = y(x_i)+\int _{x_i} ^{x_{i+1}} f(x, y(x)) \mathrm dx
$$
从而应用**左矩形公式**做近似：
$$
y(x_{i+1}) = y(x_i) +h\cdot f(x_i, y (x _ i)) +R_{i+1}^{(1)}
$$
其中：
$$
R_{i+1}^{(1)}=\frac 1 2 y''(\xi_i) h ^ 2,\quad \xi _i \in (x_i, x_{i+1})
$$
如果忽略$R_{i+1}^{(1)}$可以得到Euler公式。

Euler 公式
: 称下公式为求解初值问题的Euler方法
$$
\begin{cases}
y_0 = \eta \\
y_{i+1} = y_{i} + h f(x_i, y_i)
\end{cases}
$$

Euler公式在计算式只用到了前一步的值来计算，另外，Euler公式给出了$y_{i+1}$和$y_i$的显式依赖关系，直接代入即可得到$y_{i+1}$。因而称为**单步显式公式**

单步显式公式
: 一般形式为，其中$\varphi(x,y,h)$称为**增量函数**
$$
\begin{cases}
y_{i+1} = y_i + h\varphi(x_i, y_i, h)\\
y_0 = \eta
\end{cases}
$$

单步显式公式的局部截断误差
: 一个单步显示公式在$x_{i+1}$处的局部截断误差为
$$
R_{i+1} = y(x_{i+1}) - [y(x_i) + h\varphi(x_i,y(x_i), h)]
$$

### 后退Euler公式

单步隐式公式
: 一般形式如下，其中$\psi$为增量函数，后退Euler公式的增量函数为$\psi(x_i, y_i, y_{i+1}, h)=f(x_i+h, y_{i+1})$
$$
\begin{cases}
  y_{i+1} = y_i + h \psi(x_i, y_i, y_{i+1}, h)\\
  y_0 = \eta
\end{cases}
$$

单步隐式公式的局部截断误差
: 后退Euler公式的局部截断误差为

$$
R_{i+1} = -\frac12 y''(\xi_i)h^2
$$

### 梯形公式

应用梯形公式近似：

$$
y(x_{i+1})=y(x_i) +\frac h2\left[ f(x_i, y_i) + f(x_{i+1},y_{i+1})\right]+R_{i+1}^{(3)}
$$

其中：

$$
R_{i+1}^{(3)} = - \frac{1}{12} y'''(\xi_i) h^3
$$

### 预测校正系统和改进的Euler公式

预测校正公式
: 称侠士为改进的Euler公式，为单步显式公式

$$
\begin{cases}
  y_{i+1}^{(p)}=y_i+hf(x_i, y_i) &预测公式\\
  y_{i+1} = y_i + \frac{h}{2}[f(x_i, y_i) + f(x_{i+1}, y_{i+1}^{(p)})] & 校正公式
\end{cases}
$$

也可以改写为：

$$
\begin{cases}
  y_{i+1}^{(p)} = y_i + h f(x_i , y_i)\\
  y_{i+1}^{(c)} = y_i + hf(x_{i+1}, y_{i+1}^{(p)})\\
  y_{i+1} = (y_{i+1}^{(p)}+ y_{i+1}^{(c)})/2
\end{cases}
$$

局部截断误差为：

$$
R_{i+1} = y(x_{i+1}) - \left\{ y(x_i) + \frac h2 [f(x_i, y(x_i)) + f(x_{i+1}, y(x_i) + hf(x_i, y(x_i)))] \right\}
$$

求解公式的阶数
: 如果一个求解公式的局部截断误差为$R_{i+1}=O(h^{p+1})$则称该求解公式是$p$阶的。

## R-K方法

### R-K方法的基本思想

利用积分中值定理：

$$
y(x_{i+1}) = y(x_i) + hf(x_i+\theta h, y(x_i + \theta h))
$$

称$f(x_i+\theta h, y(x_i + \theta h))$为平均斜率

记：

$$
\begin{aligned}
  &k_1 = f(x_i, y_i)\\
  &k_2 = f(x_{i+1}, y_i + hk_1)
\end{aligned}
$$

若用$k_1$近似$k^*$，则得到一阶Euler公式，若用$\frac{k_1+k_2}{2}$来近似$k^*$，则得到二阶改进的Euler公式。

R-K方法
: 一般的显式r-级Runge-Kutta方法为

$$
\begin{cases}
   y_{i+1} = y_i + h\sum_{j=1}^r \alpha_j k_j\\
   k_1=f(x_i , y_i)\\
   k_j = f(x_i + \lambda_j h, h_i + h\sum_{l=1}^{j-1} \mu_{jl}k_l), &j=2,3,...,r
\end{cases}
$$

例如：$r=\alpha_1=1$ 可得Euler方法。

### 2阶R-K公式

$$
\begin{cases}
  y_{i+1} = y_i + h(\alpha_1k_1+\alpha_2k_2)\\
  k_1 = f(x_i, y_i)\\
  k_2 = f(x_i + \lambda_2h, y_i + h\mu_{21}k_1)
\end{cases}
$$

要使得其具有二阶精度，iff参数 $\alpha_1,\alpha_2,\lambda_2$ 和 $\mu_{21}$满足：

$$
\begin{cases}
1-\alpha_1 - \alpha_2 =0\\
\frac 12 - \alpha_2\lambda_2 = 0\\
\frac{1}{2}-\alpha_2\mu_{21} = 0
\end{cases}
$$

若取 $\alpha_2=1/2$ 则得到**二阶改进的Euler公式**。

若取 $\alpha_2=1$ 则得到**变形的Euler公式**

## 单步法的收敛性和稳定性

### 收敛性

整体截断误差
: 设 $\{y(x_i)\}$ 是微分方程的解，$\{y_i^{[h]}\}$ 是通过某个数值方法近似解。则称 $E(h) = \max|y(x_i) -y_i^{[h]}|$ 为该方法的整体截断误差，若

$$
\lim_{h\rightarrow 0} E(h) = 0
$$

则称该方法收敛。

{% p blue, Theorem %} 若$y(x)$是微分方程的解，$\{y_i\}$是单步显式公式的解，如果存在：

1. $c_0>0$ 使得 $|R_{i+1}|\le c_0h^{p+1}$
2. $h_0>0,L>0$ 使得 $\max|\frac{\partial\varphi}{\partial y}|\le L$

则当 $h<\min\{h_0, (\delta/c)^{1/p}\}$ 有：

$$
E(h) \le ch^p
$$

### 稳定性

对于初值问题$\{y_i\}_{i=0}^n$是由单步法到的的近似解,
$\{z_i\}_{i=0}^n$是扰动后的解, 即满足

$$
\left\{\begin{array}{l}
z_{i+1}=z_i+h[\varphi(x_i,z_i,h)+\delta_{i+1}],\quad i=0,1,\cdots
n-1,\\  z_0=\eta+\delta_0,\end{array}\right.
$$

如果存在正常数 $C, \varepsilon_0, h_0$, 使得对所有 $\varepsilon\in(0,\varepsilon_0]$, $h\in(0,h_0]$, 当 $\max\limits_{0\le i\le n}|\delta_i|\le\varepsilon$ 时, 有 

$$
\max_{0\le i\le n}|y_i-z_i|\le C\varepsilon,
$$

则称单步法稳定.

{% p blue, Theorem 在定理1的条件下，单步公式是稳定的 %}