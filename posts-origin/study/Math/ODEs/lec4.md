---
title: MIT 微分方程 04 - 换元法
author: Clover
date: 2022/8/8 # yyyy-mm-dd
# categories: {random}
# tags:
#  - {random}
math: true
plugins:
- mathjax
- katex
---

MIT 微分方程 04 - 换元法

<!-- more -->

## 换元法

### 1-Scaling-尺度变换

$$
x_1 = \frac x a, y_1 = \frac{y}{b}
$$

场景：

1. 更换单位
2. 无量纲化（Dimensionless, without units)
3. Reduce / Simplify Constants.

## 直接换元法

### 伯努利方程

$$
y' = p(x) y + q(x) y ^ n
$$

- $n = 0$：线性方程
- $n \ne 0$：伯努利方程

$$
\frac{y'}{y^n} = p(x) \frac{1}{y^{n-1}} + q(x)
$$

换元：

$$
v = y^{1 - n}
$$

转化为线性方程求解。

### 齐次ODE

形式：

$$
y' = F(y / x)
$$

例如：

$$
y' = \frac{x^2 y}{x^3 + y ^3}
$$

换元

$$
z = y / x
$$

则有：

$$
z'x + z = F(z)
$$

即为线性ODE。