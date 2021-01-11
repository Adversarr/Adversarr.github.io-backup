---
title: 对偶
hide: true
---

凸优化

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

- 通过 Lagrange 对偶函数获取 $p^*$ 的最佳下界
- 凸优化问题：$d^*\le p^*$

例如线性规划问题：

$$
\begin{aligned}
\min.&c^Tx\\
s.t.&Ax=b\\&x\succeq 0
\end{aligned}
$$

对偶问题为：

$$
\begin{aligned}
  \max.&-b^Tv\\
  s.t.&A^Tv+c\succeq0
\end{aligned}
$$

> 对于一个线性规划问题，其对偶问题也是线性规划问题

#### 弱对偶与强对偶

（弱对偶）对于凸优化和非凸优化都有：$d^*\le p^*$

（强对偶）对偶间隙 $p^*-d^* =0$

凸优化问题中保证强对偶的条件称为**约束准则**。

#### Slater 约束准则

**Thm**：若某个凸优化问题中，存在一点 $x\in \mathrm{relint}~D=\{x\in D|B(x,r)\cap \mathrm{aff}D\subset D\}$ 使得该问题是**严格可行**的（$x\in relint~D,f_i(x)<0,Ax=b$）则为强对偶问题。

### KKT 最优性条件

（互补松弛性）$\lambda^*_if_i(x^*)=0$

（原始可行性）$f_i(x)\le 0$

（对偶可行性）$\lambda_i\ge 0$

（稳定性条件）$\displaystyle\frac{\partial}{\partial x}L(x,\lambda,\nu)=0$
