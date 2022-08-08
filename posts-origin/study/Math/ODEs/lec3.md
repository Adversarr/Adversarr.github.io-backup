---
title: MIT-微分方程-03
author: Clover
date: 2022/8/4 # yyyy-mm-dd
# categories: {random}
# tags:
#  - {random}
math: false # true
# plugins:
#   - mathjax
#   - katex
---

一阶线性微分方程

<!-- more -->

## 一阶线性微分方程

标准形式：
$$
y' + p(x) y = q(x)
$$

### 在建模中的应用

- Temp-conc. （温度扩散）
- Mixing
- Decay, bank account.
- …

传导方程（Conduction）：

设$T$为温度，$t$为时间：
$$
\frac {d T}{dt} = k(T_e - T)
$$


扩散模型（Diffusion）

设$C$为浓度，$C_e$ 是环境浓度：
$$
\frac{dC}{dt} = k (C_e - C)
$$

## 求解方法

### 积分因子法

利用 Integrating factor（积分因子） $u(x)$

同乘$u$

$$
uy' + puy = qu
$$

希望：

$$
uy'+puy=(...)'
$$

如果$...=uy$，则要求$u' = pu$

那么$u = e ^{\int p\cdot\mathrm dx}$

例如：$xy' - y = x^3$

1. $y'-y/x = x^2$
2. $u = \frac 1 x$
3. $(y/x)' = x$
4. $y = x ^ 3 / 2 + Cx$

方法总结:

1. Standard Form
2. 计算 $u = e ^{\int p dx}$ 积分因子
3. 两侧同乘 $u$

### Linear with k constant（线性常系数微分方程）

例如：

$$
\frac{dT}{dt} + kT = k T_e(t)
$$

$$
u = e ^ { k T }
$$

$$
T = e^{-kt} \int_0^{t'} k T_e(t') \mathrm dt'  + Ce^{-kt}
$$

- $C$ 取决于 $T_0$：体现为暂态解



