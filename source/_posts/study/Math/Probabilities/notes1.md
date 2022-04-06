---
title: 「概率统计与随机过程」 1 - 随机事件及其概率
date: 2020-11-18
categories: 数学
tags:
  - 概率论
math: true
plugins:
  - mathjax
  - katex
group: group-probabilites
sidebar: [group-probabilites, toc]
---

随机事件及其概率

<!-- more -->

## 随机事件及其概率

### 随机事件

**Def**：样本空间

**Def**：随机事件

### 随机事件的概率

#### 事件的概率

**Def**：频率

**Thm**：频率满足

- $0\le f_n(A)\le 1$
- $f_n(\varOmega)=1$
- 互不相容的随机事件，$f_n(\cup A_i)=\sum f_n(A_i)$

#### 概率的公理化定义

**Def**：设$E$是随机试验，$\varOmega$ 是 $E$ 的样本空间，对于每一个随机事件，赋予唯一的实数$P(A)$，满足：非负性、规范性、可列可加性，则称集合函数$P(\cdot)$为概率测度。

**Thms**

- 不可能事件的概率为 0
- 有限可加性：不相容的随机事件，和的概率等于概率的和
- 对立事件的概率：$P(\bar A)=1-P(A)$
- 概率的加法公式：$P(A+B)=P(A)+P(B)-P(AB)$
- 概率的减法公式：若 A 包含 B，$P(A-B)=P(A)-P(B)$
- 概率的单调性：若 A 包含于 B，$P(A)\le P(B)$

### 古典概型

**Def**：一个古典概型 $E$ 满足：

1. 样本空间只有有限个基本事件
2. 每个基本事件出现可能性相同

### 条件概率

#### 条件概率的定义

**Def**：（有穷划分）设 $\varOmega$ 是随机试验 $E$ 的样本空间，$A_1,A_2,\dots, A_n$ 是随机事件，若满足：
  1. $A_iA_j = \emptyset,~\forall i\ne j$
  2. $\cup A_j = \varOmega$
则称$A_1,A_2,\dots, A_n$ 是$\varOmega$ 的一个有穷划分。

> 相同定义 {% kbd 可列无穷划分 %}

**Def**（条件概率）设 $A,B$ 是两个随机事件，$P(B)>0$ 则称 $P(A|B)=P(AB)/P(B)$ 为事件 $B$ 发生条件下，事件 $A$ 发生的概率

#### 概率的乘法公式

**Thm**：设 $A_1, ...,A_n$ 为 n 个随机事件，且 $P(\bigcap A_i)>0$，则 $P(\bigcap A_i)=P(A_1)P(A_2|A_1)...P(A_n|\bigcap_{i=1}^{n-1}A_i)$

#### 全概率公式和贝叶斯公式

**Thm**（全概率公式）设随机事件组是 $\varOmega$ 的一组**可列无穷划分** $P(A_i) > 0,\forall i$，则对于任意随机事件 $B$，有：$P(B) = \sum P(A_i)P(B|A_i)$

**Thm**（Bayes 公式）设$A_1, A_2,\dots$ 是样本空间$\varOmega$ 的一组可列无穷划分，$P>0,B\subset \varOmega$ 则：

$$
  P(A_i|B) = \frac{P(A_i)P(B|A_i)}{\sum P(A_i)P(B|A_i)}, i = 1, 2,\dots
$$

### 随机事件的独立性

#### 两个随机事件的独立性

**Def**（独立性）设$A,B$是两个随机事件，若：$P(AB) = P(A)P(B)$则称 $A, B$ 是两个相互独立的随机事件

> $\varOmega,~\emptyset$ 与任一事件相互独立

**Thm**：$P(A),P(B)>0$ 时 $A,B独立\iff P(A|B)=P(A), P(B|A)=P(B)$

**Thm**（独立扩张定理）$A,B独立\iff \bar A,B~A,\bar B~ \bar A,\bar B 独立$

#### 多个随机事件的独立性

**Def**：三个独立的随机事件，满足：
$$
  \begin{cases}
      两两独立\\
      P(ABC) = P(A)P(B)P(C)
  \end{cases}
$$

**Def**（n 个事件的独立性）

> 独立的多个随机事件满足：
>
> 1. $P(\cap A_i) = \prod P(A_i)$
> 2. $P(\cup A_i) = 1 - \prod[1-P(A_i)]$
