---
title: 概率统计与随机过程 1 - 随机事件及其概率
date: 2020-11-18
categories: 数学
tags:
  - 概率论
  - 统计
math: true
hide: false
---

# 随机事件及其概率

### 1.1 随机事件

- Def：样本空间

- Def：随机事件

##### 随机事件的概率

- Def 1.1：频率

- Thm 1.1：频率满足：
  - $0\le f_n(A)\le 1$
  - $f_n(\varOmega)=1$
  - 互不相容的随机事件，$f_n(\cup A_i)=\sum f_n(A_i)$

##### 概率的公理化定义

- 设$E$是随机试验，$\varOmega$ 是 $E$ 的样本空间，对于每一个随机事件，赋予唯一的实数$P(A)$，满足：非负性、规范性、可列可加性，则称集合函数$P(\cdot)$为概率测度

- Thms：
  - $P(\empty)=0$
  - $P(\cup A_i)=\sum P(A_i)$
  - $P(\bar A) = 1-P(A)$
  - $P(A\cup B) + P(AB) = P(A)+P(B)$
  - $A\sub B\rightarrow P(B-A)=P(B)-P(A)$
  - $A\sub B\rightarrow P(A)\le P(B)$

### 1.3 古典概型

- Def 1.3：一个古典概型 $E$ 满足：
  
  1. 样本空间只有有限个基本事件
  2. 每个基本事件出现可能性相同

### 1.4 条件概率

- Def 1.5：设 $\varOmega$ 是随机试验 $E$ 的样本空间，$A_1,A_2,\dots, A_n$ 是随机事件，若满足：
  1. $A_iA_j = \empty,~\forall i\ne j$
  2. $\cup A_j = \varOmega$
  
  则称$A_1,A_2,\dots, A_n$ 是$\varOmega$ 的一个有穷划分。

  > 相同定义 {% label primary  @可列无穷划分 %}

##### 全概率公式和贝叶斯公式

**全概率公式**

- Thm 1.3：设随机事件组是 $\varOmega$ 的一组可列无穷划分 $P(A_i) > 0,\forall i$，则对于任意随机事件 $B$，有：$P(B) = \sum P(A_i)P(B|A_i)$

**Bayes 公式**

- Thm 1.4：设$A_1, A_2,\dots$ 是样本空间$\varOmega$ 的一组可列无穷划分，$P>0,B\subset \varOmega$ 则：

  $$
    P(A_i|B) = \frac{P(A_i)P(B|A_i)}{\sum P(A_i)P(B|A_i)}, i = 1, 2,\dots
  $$


### 1.5 随机事件的独立性

##### 两个随机事件的独立性

- Def 1.6：设$A,B$是两个随机事件，若：$P(AB) = P(A)P(B)$则称 $A, B$ 是两个相互独立的随机事件

> $\varOmega,~\empty$ 与任一事件相互独立

- Thm 1.5：$P(A),P(B)>0$ 时 $A,B独立\iff P(A|B)=P(A), P(B|A)=P(B)$

- Thm 1.6 「独立扩张定理」：$A,B独立\iff \bar A,B~A,\bar B~ \bar A,\bar B 独立$

##### 多个随机事件的独立性


- Def 1.7：三个独立的随机事件，满足：
  $$
    \begin{cases}
        两两独立\\
        P(ABC) = P(A)P(B)P(C)
    \end{cases}
  $$

- Def 1.8：n 个事件的独立性

> 独立的多个随机事件满足：
>
> 1. $P(\cap A_i) = \prod P(A_i)$
> 2. $P(\cup A_i) = 1 - \prod[1-P(A_i)]$
