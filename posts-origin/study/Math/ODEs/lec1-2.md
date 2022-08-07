---
title: MIT 微分方程 01-02
author: Clover
date: 2022/7/27 # yyyy-mm-dd
# categories: {random}
# tags:
#  - {random}
math: false # true
# plugins:
#   - mathjax
#   - katex
---

{random}

<!-- more -->

## First Order ODE

形式如下
$$
y' = f(x, y)
$$
例如：

1. $y' = x - y ^ 2$
2. $y' = x/y$

两个方程的解的难度完全不同：`1`没有初等函数解。

## Geometry View of ODE

$$
y' = f(x, y)
$$

设$y_1$是其中一个解，在微分几何中：

- $y'$ 对应到一个方向场
- $y$ 对应一个积分曲线 – 在方向场中，切线方向始终与该处方向向量平行。

> 即微分方程解的图像。

我们有：

- $y_0$ 是解 当且仅当 $y_0$ 是一个积分曲线

结论：

1. 两个积分曲线互不相交（不能有不同的斜率）
2. 两个积分曲线甚至不能相切：存在+唯一

## 数值方法

IVP：初值问题
:
$$
y' = f(x, y) \quad y(x_0) = y _ 0
$$
使用Euler方法进行计算：（一阶方法）

1. 根据 $x_0, y _0$ 算出 $y'_0$
2. 递增$(x_0+h, y_0+y_0'\cdot h)$
3. 递推即可

例如：

```python
def f(x, y): return x**2 - y**2

def euler(x0, y0, h, n):
   x = [x0, ]
   y = [y0, ]
   for i in range(n):
       x.append(x[-1] + h)
       y.append(y[-1] + h * f(x[-1], y[-1]))
   return x, y

plt.plot(*euler(0, 1, 0.1, 10)); plt.show()
```

改进：

1. 采用更小的步长

> Having the step size, having the error.

### 更好的方法

龙哥库塔-RK2

Standard Method：RK4！

## 数值计算中的常见问题

1. $y'=y^2$ – 存在极点。

