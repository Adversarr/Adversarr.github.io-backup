---
title: 群与环
date: 2020-5-27
tags:
  - 代数结构
  - 离散数学
categories: 数学
math: true
---

期末复习了 qwwww

<!--more-->

## 群的定义和性质

**Def**：群

1. 设 $V = <S,\circ>$ 是代数系统，$\circ$ 是二元运算，且是可结合的，则称 $V$ 是半群
2. 设 $V$ 是一个半群，存在关于 $\circ$ 运算的单位元，则称 $V$ 是幺半群，也称为独异点
3. 若 $V$ 是一个独异点，$e\in S$ 是其单位元，若 $\forall a \in S,a^{-1}\in S$ 则称 $V$ 为群，通常用 $G$ 代表

> 常见的群有：整数加群、有理数加群、实数加群、复数加群
>
> Klein 四元群：
>
> |     | e   | a   | b   | c   |
> | --- | --- | --- | --- | --- |
> | e   | e   | a   | b   | c   |
> | a   | a   | e   | c   | b   |
> | b   | b   | c   | e   | a   |
> | c   | c   | b   | a   | e   |

**Def**：平凡群、有限群、无限群、交换群

1. 若群 $G$ 是有穷集，则称 $G$ 为有限群，反之称为无限群。其中 $G$ 的基数称为群 $G$ 的阶
2. 若 $G$ 中只含有单位元，称之为平凡群
3. 若二元运算 $\circ$ 是可交换的，则称 $G$ 为交换群或是 Abel 群。

**Def**：幂运算

$$
a^n=
\begin{cases}
e,\qquad &n = 0\\
a^{n-1}a,& n >0\\
(a^{-1})^m,& n>0,n = -m
\end{cases}
$$

**Def**：（元素的阶）将使得 $a^k = e$ 成立的最小正整数 $k$ 称为 $a$ 的阶。有 $k$ 阶元，也有无限阶元。

**Thm**：幂运算满足

1. $(a^{-1})^{-1} = a$
2. $(ab)^{-1} = b^{-1}a^{-1}$
3. $a^na^m = a^{m+n}$
4. $(a^n)^m = a^{mn}$
5. 交换群中，$(ab)^n = a^nb^n$

**Thm**：群中满足消去律

**Thm**：设群 $G$ 中有元素 $a$ 满足 $|a|$ 为 $r$ 则：

1. $a^k = e\iff r|k$
2. $|a^{-1}|=|a|$

## 子群和群的陪集分解

**Def**：子群、真子群

**Def**：（判定定理 1）设 $G$ 为群，$H$ 是 $G$ 的非空子集，则 $H$ 是 $G$ 的子群，当且仅当下列条件同时成立

1. $\forall a,b\in H,ab\in H$
2. $\forall a\in H, a^{-1}\in H$

**Thm**：（判定定理 2）设 $G$ 为群，$H$ 是 $G$ 的非空子集，则 $H$ 是 $G$ 的子群，当且仅当 $\forall a,b\in H, ab^{-1}\in H$

**Thm**：（判定定理 3）设 $G$ 为群，$H$ 是 $G$ 的非空子集，则 $H$ 是 $G$ 的有穷子群，当且仅当 $\forall a,b\in H,ab\in H$

**Def**：（中心）设 $G$ 是群，令 $C$ 是与 $G$ 中所有元素都可交换的元素构成的集合，$C=\{a|a\in G\wedge \forall x\in G(ax=xa)\}$ 则称 $C$ 为 $G$ 的中心，且是 $G$ 的一个子群。

**Def**：（由 $B$ 生成的子群）设 $B$ 是 $G$ 的子集，将所有包含 $B$ 的子群的交记作 $<B>$。

{% note caution %}

**Caution**

未知正确性：

- $<B>$ 中只含有 $B$ 中的元素或其逆元。

{% endnote %}

**Def**：设 $H$ 是群 $G$ 的子群，$a\in G$，令$Ha =\{ha|h\in H\}$ 称之为子群 $H$ 在 $G$ 中的右陪集，并称 $a$ 为 $Ha$ 的代表元素。

**Thm**：设 $H$ 是 $G$ 的子群，则

1. $He =H$
2. $\forall a\in G, a\in Ha$

**Thm**：设 $H$ 是 $G$ 的子群，则 $\forall a,b\in G$ TFAE

1. $a\in Hb$
2. $ab^{-1}\in H$
3. $Ha=Hb$

**Thm**：设 $H$ 是 $G$ 的子群，在 $G$ 上定义二元关系：$\forall a,b\in G <a,b>\in R\iff ab^{-1}\in H$ 则 $R$ 是 $G$ 上的等价关系，且 $[a]_R =Ha$

**Inf**：设 $H$ 是 $G$ 的子群，则

1. $\forall a,b\in G, Ha = Hb 或 Ha\cap Hb =\emptyset$
2. $\cup\{Ha|a\in G\} = G$

{% note primary %}

**Tips**

于此同时，$H$ 的所有右陪集的集合 $\{Ha|a\in G\}$ 恰好构成 G 的一个划分，并且，这个划分的所有划分快都和 $H$ 等势。

用同样的方法可以定义 $H$ 的左陪集。
{% endnote %}

**Def**：（指数）$H$ 在 $G$ 中的左右陪集数相等，记作 $H$ 在 $G$ 中的指数 $[G:H]$

**Thm**：（Lagrange 定理）设 $G$ 是一个有限群，$H$ 是 $G$ 的子群，则 $|G| = |H|\cdot [G:H]$

**Inf**：设 $G$ 是 $n$ 阶群，则 $\forall a\in G$，$|a|$ 是 $n$ 的因子，且 $a^n =e$

**Inf**：设 $G$ 是素数阶的群，则存在 $a\in G$，使得$G=<a>$

## 循环群和置换群

**Def**：（循环群）若存在 $a\in G$ 使得 $G = <a>$ 则称 $G$ 为循环群，称 $a$ 为 $G$ 的生成元

其中，若 $a$ 是 $n$ 阶元，则 $|G| = n$ 则称 $G$ 为 $n$ 阶循环群，若 $a$ 是无限阶元，则称 $G$ 是无限循环群

**Thm**：设 $G=<a>$ 是循环群，

1. $G$ 是无限循环群，则 $G$ 只有两个生成元，即为 $a$ 和 $a^{-1}$
2. $G$ 是 $n$ 阶循环群，则 $G$ 含有 $\phi(n)$ 个生成元，对于任何小于且与 $n$ 互素的自然数 $r$，$a^r$ 是 $G$ 的生成元

**Thm**：

1. 设 $G$ 是循环群，则 $G$ 的子群是循环群
2. $G$ 是无限循环群，则 $G$ 的子群除了 $\{e\}$ 之外都是无限循环群
3. 若 $G$ 是 $n$ 阶循环群，则对于 $n$ 的每一个正因子 $d$，$G$ 恰好含有一个 $d$ 阶子群

<!-- TODO: to complete -->