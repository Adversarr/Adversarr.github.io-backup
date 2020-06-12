---
title: 格和布尔代数
date: 2020-05-28 08:51:05
tags:
  - 代数结构
  - 离散数学
categories: 离散数学
mathjax: true
---

半个上午的时间，回顾一下上章的内容，呼

在现实中的许多的问题都可以抽象为代数问题，还是要好好学吖~

<!--more-->

## 格的定义和性质

**Def**：（格）设$<S,\preccurlyeq>$ 是偏序集，若 $\forall x,y\in S,\{x,y\}$ 都有最小上界和最大下界，则称 $S$ 关于偏序 $\preccurlyeq$ 成一个格

{% note default %}
由于最小上界和最大下界的唯一性，可以把求 $\{x,y\}$ 的最小上界和最大下界看成二元运算，$\wedge$ 为最大下界，$\vee$ 为最小上界
{% endnote %}

**Thm**：（格的对偶原理）设 $f$ 是含有格中元素以及符号 $=,\preccurlyeq,\succcurlyeq,\vee,\wedge$ 的命题，若 $f$ 对于一切格为真，则 $f$ 的对偶命题 $f'$ 也对一切格为真

**Thm**：格中的 $\wedge,\vee$运算满足交换律，结合律，幂等律，吸收律

**Thm**：设 $<S,*,\circ>$是一个具有两个二元运算的代数系统，且对于两个运算满足交换律，结合律，吸收律，则可以适当的定义 $S$ 中的偏序 $\preccurlyeq$ 使之成为一个格。

**Def**：设 $<S,*,\circ>$ 是代数系统，如果 $*$ 和 $\circ$ 满足结合律，分配律，吸收律，则该代数系统构成一个格

{% note default %}
注意：这里的幂等律在上面三个运算律满足时自然满足
{% endnote %}

**Thm**：设 $L$ 是格，则 $\forall a,b\in L$ 有 $a\preccurlyeq b\iff a\wedge b =a\iff a\vee b=b$

**Thm**：设 $L$ 是格，$\forall a,b,c,d\in L,(a\preccurlyeq b 且 c\preccurlyeq d)\rightarrow(a\wedge c\preccurlyeq b\wedge d,a\vee c\preccurlyeq b\vee d)$

**Def**：子格

## 分配格、有补格、布尔代数

**Def**：（分配格）设 $<L,\wedge,\vee>$ 是格，若 $\forall a,b,c\in L$ 有

$$
a\wedge(b\vee c) =(a\wedge b)\vee (a\wedge c)\\
a\vee(b\wedge c) = (a\vee b)\wedge (a\vee c)
$$

则称 $L$ 为分配格。

{% note default %}
两类特殊的格结构：钻石格和五角格
{% asset_img TwoSpecialLattice.png 钻石格和五角格 %}
{% endnote %}

**Thm**：若 $L$ 是格，则 $L$ 是分配格，iff $L$ 中不含有与钻石格或五角格同构的子格

**Inf**：小于 5 元的格都是分配格

**Inf**：任何一条链都是分配格

**Def**：（全下界，全上界）设 $L$ 是格，若存在 $a\in L$ 使得 $\forall x\in L,a\preccurlyeq x$ 则称为 $L$ 的全下界；对称的定义 $L$ 的全上界

**Def**：设 $L$ 是格，若 $L$ 存在全下界和全上界，则称 $L$ 为有界格，记作 $<L,\wedge,\vee,0,1>$

**Def**：（补元）在有界格中，$a\in L$，若存在 $b\in L$ 使得 $a\wedge b =0$ 且 $a\vee b =1$，则称 $b$ 为 $a$ 的补元

**Thm**：在有界分配格中，若 $a\in L$ 且对于 $a$ 存在补元 $b$ 则 $b$ 是 $a$ 唯一的补元 记作 $b = a'$

**Def**：（布尔格、布尔代数）如果一个格是有补分配格，则称之为布尔格或布尔代数

**Thm**：在布尔代数中

1. $\forall a\in B,(a')' = a$
2. $\forall a,b\in B,(a\wedge b)' =(a'\vee b'),(a\vee b)' = (a'\wedge b')$

{% note default %}
在这个定理中，第一条称作 **双重否定律**，第二条称作**德摩根律**，在命题代数和集合代数中的双重否定律，实则是该定理的特例
{% endnote %}

**Def**：设$<B,*,\circ>$是代数系统，若运算满足：

1. 交换律
2. 分配律（$*$ 对 $\circ$ $\circ$ 对 $*$ 都有分配律）
3. 同一律 $a*1=a,a\circ 0=a$
4. 补元律（所有元素的补元存在且唯一）

则称之为一个布尔代数

**Def**：（原子）在格中，若 $0\prec b\preccurlyeq a\iff b=a$ 则称 $a$ 是 L 中的原子

**Thm**：（有限布尔代数的表示定理）设 $B$ 是有限布尔代数，$A$ 是由 $B$ 的全体原子构成的集合，则 $B$ 同构于 $A$ 的幂集代数 $P(A)$

**Inf**：任何有限布尔代数的基数为 $2^n$

**Inf**：任何等势的有限布尔代数都是同构的
