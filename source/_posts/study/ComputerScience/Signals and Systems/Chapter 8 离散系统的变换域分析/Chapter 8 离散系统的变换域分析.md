---
title: 离散系统的变换域分析
date: 2021-6-13
categories: 专业课
tags:
  - 信号与系统
math: true
plugins:
  - mathjax
  - katex
group: group-signals-and-systems
sidebar: [group-signals-and-systems, toc]
---

信号与系统- 离散系统的变换域分析

<!-- more -->

# Chapter 8 离散系统的变换域分析

## 引言

1. 时域**卷和**→z域乘法
2. 差分方程→z域代数方程
3. 重点：
	1. （双边）正反z变换
	2. （单边）z变换**性质**
	3. z域分析法
	4. DTFT

## z变换定义及其收敛区

### z变换的定义

$f(k) \leftrightarrow F_d(z) \mathop=\limits^\Delta \sum_{k=-\infty}^\infty f(k) z^{-k} = Z[h(k)]$

1. 如果$f(k)$本身是单边的，则$k$可以从0开始取
2. $z=e^{sT}$：z域到s域上的基本映射 $F(z)|_{z=e^{sT}} = F_s(s)$（理想抽样信号的LT）

### z变换的收敛区

1. 有限长序列：$f(k)\leftrightarrow F(z) = \sum_{k = n_1}^{n_2} f(k) z^{-k}$→在整个z平面上收敛（可能不含$z=0,\infty$）
2. 单边序列（以右边为例）：$a^k\varepsilon(k)\leftrightarrow F(z) =\frac z{z-a}\quad |z|>|a|$
	1. 如果是左边序列：$b^k\varepsilon(-k-1) \leftrightarrow F(z) = -\frac{z}{z-b}$

### 常见的z变换

1. 单位样本函数：$\delta(k)\leftrightarrow 1$ ROC为整个z平面
2. 单边指数序列：$a^k\varepsilon(k)\leftrightarrow \frac {z} {z-a}$ROC为$|z|>|a|$
3. 单位阶跃序列：$\varepsilon(k) \leftrightarrow \frac z {z-1}$ROC: $|z|>1$
4. 单位正弦：
	1. $\cos \beta^k \varepsilon(k) \leftrightarrow \frac{z^2-z\cos\beta}{z^2-2z\cos\beta + 1}$ROC: $|z|>1$
	2. $\sin \beta^k \varepsilon(k) \leftrightarrow \frac{z^2-z\sin\beta}{z^2-2z\cos\beta + 1}$ROC: $|z|>1$
	3. 特别的：$\cos\frac{k\pi}{2}\varepsilon(k)\leftrightarrow \frac{z^2}{z^2+1}$，$\sin\frac{k\pi}{2}\varepsilon(k)\leftrightarrow \frac{z}{z^2+1}$
5. 斜变序列：$k\varepsilon(k) \leftrightarrow \frac z {(z-1)^2}$

## 单边 z 变换的性质

1. 线性性质：
2. **移序性质**：
	1. $f(k+n)\varepsilon(k) \leftrightarrow z^nF(z) -z^{n}f(0) - z^{n-1} f(1) - \cdots -zf(n-1)$
	2. $f(k-n) \varepsilon(k-n) \leftrightarrow z^{-n} F(z)$
	3. $f(k-n)\varepsilon(k) \leftrightarrow z^{-n}F(z) + z^0f(-n) + \cdots + z^{-(n-2)} f(-2) + z^{-(n-1)}f(-1)$
	4. 对于**单边变换**：$f(k\pm n) \leftrightarrow z^{\pm n}F_d(z)$
3. z 域尺度变换（序列指数加权）：$a^kf(k)\leftrightarrow F(z/a)\quad(a\ne 0)$
4. 卷积定理：$f*g\leftrightarrow F\cdot G$
5. z 域微分（序列线性加权）：$kf(k) \leftrightarrow (-z)\frac{\mathrm dF(z)}{\mathrm dz}$
6. 初值和终值定理：$F(z) = f(0) + f(1) z ^ {-1} + f(2) z ^{-2} + \cdots$
	1. 初值：$f(0) = F(z) |_{z=\infty},~f(1) = (zF(z) - zf(0)) |_{z=\infty}, \cdots$
	2. 终值：$f(+\infty)=\lim _{z\rightarrow 1}(z-1)F(z)$ （条件：$f(k)$存在终值、$F(z)$ 的极点都在单位圆内，或者为$1$

## 反z变换

### 幂级数展开

借助泰勒公式：

$$
f(x) = f(0) + f'(0) x + \cdots\quad(\mathrm {by~Taylor~Series})
$$


长除法：

1. 对**右边序列**：分子分母**降序**排列相除
2. 对**左边序列**：分子分母**升序**排列相除

### 部分分式法

将$F(z)/z$展开，设$F(z)$极点都是单阶的：

$$
\frac{F(z)}z=\frac{K_0}z+\frac{K_1} {z-v_1}\cdots + \frac{K_n}{z-v_n}
$$


若有重根存在，可以考虑留数法

### 留数法

因为：

$$
F(z) = f(0) + f(1)z^{-1} + \cdots
$$


从而：

$$
f(k) = \frac{1}{2\pi j}\oint_cF(z)z^{k-1}\mathrm dz
$$


## 双边正反Z变换

### 双边z变换

$$
F_r(z)=F_{br}(z) = \sum_{k=-\infty}^{\infty} f_r(k) z^{-k},\\ F_{bl}(z) = \sum_{k=-1}^{-\infty} f_l(k) z^{-k}=\sum_{k=1}^\infty f_l(-k)\left(\frac1 z\right)^{-k}=\mathcal Z\{f_l(-k)\}[1/z]
$$


### 双边反z变换

$$
F_b(z) = F_{br}(z) + F_{bl}(z)
$$


## z变换和LT的关系

1. $f(t)$ 时间离散化为 $f(k)$<br />则$f_s(t) = f(t) \delta_T(t)$<br />$F(z)|_{z=e^{j\omega T}}=F_s(j\omega)$
2. $z=e^{sT}$ 映射关系<br />设 $s=\sigma + j\omega$ ，若 $z=re^{j\theta}$ 其中 $r = e^{\sigma T},~\theta = \omega T$
3. $F(z)$和$F(s)$的关系（只考虑单边）<br />$f(k) = f(t) |_{t=kT}$，$F(z)=\frac 1 {2\pi j} \int_{\sigma-j\infty}^{\sigma + j\infty} F(s)\frac{z}{z-e^{sT}}\mathrm ds$

## z 变换分析法

对于$n$阶系统：

### 零输入相应

对齐次方程取单边 z 变换

$$
Y_{zi}(z) \leftrightarrow y_{zi}(k)
$$


然后使用**移序性质**求解。

### 零状态响应

$$
y_{zs}(k) = e(k) * h(k)\leftrightarrow H(z) E(z)
$$


### 全响应

**法 1:** ZS+ZI

**法 2:** 对差分方程直接求单边 Z 变换

## 离散时间系统的频率响应特性

### 定义

### 离散系统频响的特点

1. $\omega$的连续函数
2. 幅频$\omega$的偶函数，相频$\omega$的奇函数（共轭对称）
3. 以$\omega_s$为周期

### 离散系统频响的图解

$$
H(z) = b_m \frac{\prod_i (z-z_i)}{\prod_r (z-p_r)}
$$


如果 Z 变换的零点或极点落在原点上，它们对 H 的幅值**没有影响**。

## 离散系统的系统函数和稳定性判据

### 系统函数

1. $H(z) = \frac{N(S)}{D(S)}|_{S=z}$
2. $H(z) = Y(z) / E(z) |_{ZS}$
3. $H(z) = Y_{zs}(z) / E(z)$
4. $H(z) = z^k 作用下的（零状态）响应/z^k$

### 框图（数字滤波器的结构）

1. 并联型：注意共轭根配对
2. 串联型
3. 混联

> 通用方法：设 W 为中间变量，列方程求解


### 稳定性判据（因果系统）

1. BIBO
2. $h(k)$ 绝对可和；（放宽到渐进条件：$\lim_{k\rightarrow\infty}h(k)=0$）
3. $H(z)$ 极点在单位圆内；
4. R-H 准则：使用双线性变换$z=\frac{s+1}{s-1}$代入$D(z)$

### 信号与频谱的关系

