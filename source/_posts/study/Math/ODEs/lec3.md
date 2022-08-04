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