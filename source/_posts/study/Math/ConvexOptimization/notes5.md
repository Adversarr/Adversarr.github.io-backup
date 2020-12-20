---
title: 对偶
---

<!-- more -->

# 对偶

### Lagrange 对偶函数

#### Lagrange

考虑标准形式的优化问题，拉格朗日函数定义为：

$$
\begin{aligned}
&L:R^n\times R^m\times R^p\rightarrow R\\
&L(x, \lambda, \nu)=f_0(x)+\sum_{i=1}^m \lambda_if_i(x)+\sum_{i=1}^p \nu_ih_i(x)\\
\end{aligned}
$$

- 定义域为：$D\times R^m\times R^p$
- 目标函数和约束函数的加权和
- $\lambda_i$ 为第 i 个不等式约束的*拉格朗日乘子*
- $\nu_i$ 为第 i 个不等式约束的*拉格朗日乘子*

#### 拉格朗日对偶函数

$$
\begin{aligned}
    &g:R^m\times R^p\rightarrow R\\
    &g=\inf_{x\in D} L(x,\lambda, \nu)
\end{aligned}
$$

- 函数 $g$ 为凹函数（任何优化问题的 Lagrange 对偶函数为凹函数）
  - $\sup L(x,\lambda, \nu)$ 为凸函数

- 最优值下界：若 $\lambda \ge 0$，则 $g(\lambda, \nu)\le p^ *$（$p^ *$ 为原优化问题最优值）

#### 拉格朗日对偶函数与共轭函数

共轭函数 $f^*=\sup_{x\in D}(y^Tx-f(x))$

### 对偶问题

$$
\begin{aligned}
    &\max.g(\lambda,\nu)\\
    &s.t.~~\lambda\succeq 0
\end{aligned}
$$