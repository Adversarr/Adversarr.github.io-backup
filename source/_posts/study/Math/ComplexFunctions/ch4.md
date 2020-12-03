---
title: 「复变函数」复数项级数
date: 2020-11-20
tags:
  - 复变函数
  - 高等数学
math: true
categories: 数学
---

复数项级数的概念和性质

<!-- more -->

# 复数项级数的概念和性质

### 复数项级数

- **Def**：无穷复数列 $\{c_n\}\rightarrow_{n\rightarrow \infty} A \iff \forall \varepsilon>0,\exists N,n>N\rightarrow |c_n-A|<\varepsilon$
- **Thm**：（判别法则）$c_n=a_n+ib_n$收敛于$a+bi$ iff $a_n\rightarrow a, b_n\rightarrow b$
- **Def**：复数项级数$\sum_{n=1}^\infty c_n$，通项 $c_n$。
- **Def**：前 n 项之和$\sum_{k=1}^n c_k$

##### Thms

- **Thm**：（必要条件）级数$\sum c_n$收敛，则 $\lim_{n\rightarrow \infty} c_n=0$
- **Thm**：（柯西收敛准则）$\sum c_n$ 收敛 $\iff \forall \varepsilon>0,\exists N,\forall p\in N_+, n>N\rightarrow|S_{n+p} - S_n|\le \varepsilon$

##### 按模收敛

- **Def**：（按模收敛）$\sum |c_n|$
- **Def**：（条件收敛）$\sum |c_n|$ 不收敛，$\sum c_n$ 收敛

##### 性质

- $\sum c_n=s$，$k$为任意常数，则$\sum kc_n=k\sum c_n$
- 线性性质
- 去掉或加上有限项不改变级数的敛散性。
- 收敛级数添加括号或改变次序不改变敛散性
  - 逆命题不成立

> - P78: 15 23 28(1) 29(3)
> - P104: 1 2 4 3(2 3 5)
> 
> 下次习题课
