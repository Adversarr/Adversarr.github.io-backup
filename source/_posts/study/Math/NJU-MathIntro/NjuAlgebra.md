---
title: NJU - 群论初步
author: Clover
date: 2022/7/10 # yyyy-mm-dd
categories: 数学
tags:
 - 近世代数
math: true
plugins:
  - mathjax
  # - katex
---

群论

<!-- more -->

## 群论初步

### 基本概念

> 例子 – 数、多项式、矩阵、函数
>
> 共同特点– 加法、乘法
>
> 结合律和交换律

代数运算
: 设$A$ 是非空集合，在其上定义了一个法则，使得$A$中任意两个元素与$A$中的另一元素对应。

> 例如
>
> 1. $\mathbb R$ 对 加法、乘法
> 2. 函数的复合、加减乘法
>
> 不是代数运算的例子：
>
> 1. 向量的数乘 – $\alpha \in V, k \in P: \alpha k$ 
> 2. 向量的内积

群
: $G$ 非空，有代数运算（一般称作乘法），若满足
1. 结合律
2. 存在幺元
3. （每一个元素都）存在逆元

> 按照$G$满足1/2/3的情况，分别定义为半群、幺半群、群

记为 $(G, \cdot)$

> 如果满足交换律 -- 称作Abel群（交换群）
>
> - 一般记作加法

### 群的基本例子

1. $(\mathbb Z, +)$
2. $(\mathbb R^*, \times)$
3. $(\mathbb R, +)$
4. $n \in \mathbb N, U_n := $ 全体 n 次单位根
5. 多项式对于加法 -- 群
   1. 对于乘法 -- 半群
6. 同阶矩阵对加法，方阵对乘法，同阶可逆矩阵对乘法
7. 连续函数，对加法
8. 仿射变换全体
9. $\mathbb Z_p = \{0, 1, 2, ... , p - 1\}$
10. $GL(n, \mathbb C)$ -- n阶复的非奇异矩阵

### 群的基本性质

Prop
: 设$(G, \cdot)$ 是群，若$ba=e$，则$ab=e$

Prop
: 设$(G, \cdot)$ 是群，则对于任意$a\in G$，$ea=ae=a$

Prop
: 群的单位元是唯一的。

Prop
: 群中任意元素的逆元是唯一的。

可以定义出：

幂
: $a^n := a \circ \cdots \circ a$

Prop
: 群中满足消去律

Prop
: 方程 $ax = y$ 和 $xa = y$ 都有唯一解

### 群同构

元素的阶
: $a \in G$，使得$a^m = 0$的最小正整数称为$a$的阶。

同态
: $G$ 和 $H$ 是两个群，若存在映射保持运算，则称该映射是同态。

根据该同态的性质：
1. 单
2. 满
3. 双的 -- **同构**

> 例如：
> 
> 1. ${\mathbb R}^* \rightarrow {\mathbb R}, \log$
> 2. 平凡同态 -- $Id: \alpha \rightarrowtail \alpha$

Prop
: 群的同构作为群的关系是等价关系。

#### 变换群

集合的变换
: A是非空集合，称由$A$到自身的映射$\tau: A\rightarrow A$是集合上的变换。

例如
1. 单的 -- $A = {\mathbb R}$ 而 $\tau : x \rightarrowtail e ^ x$
2. 满的 -- $\mathbb Z$ 中 $a \rightarrowtail \lfloor a / 2\rfloor$

全变换群 $S$
: 集合 $A$ 上全体变换作成的集合，定义代数运算为复合运算：
$$
\tau, \mu \rightarrow \tau \circ \mu
$$

子群
: 记作$H \le G$。

Cayley表示定理
: 任何一个群都与一个变换群同构。

> $\sigma$ 保持了代数结构。

### 置换群

置换
: 有限集合上的一一变换叫做一个置换，构成的群称为置换群。

Prop
: 有限集合上的全体置换构成群$S_n$。

表示置换的方法有两种：

1. $\pi: a _ i \rightarrow a_{ki}$
   $(1, k_1) (2, k_2) ....(n, k_n)$
2. 写成两行的表

例如 $S_3$ ，显然不是交换群！

 







