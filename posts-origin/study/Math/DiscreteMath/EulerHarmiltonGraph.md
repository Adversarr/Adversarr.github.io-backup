---
title: 欧拉图和哈密顿图
date: 2020-06-25
tags:
  - 图论
  - 离散数学
categories: 数学
math: true
plugins:
  - mathjax
  - katex
---

<!-- TODO: -->

<!-- more -->

## 欧拉图

**Def**：

- （欧拉通路）经过图中所有边一次且仅一次的通路
- （欧拉回路）经过图中所有边一次且仅一次的回路
- （欧拉图）有欧拉回路
- （半欧拉图）有欧拉通路

**Thm**：无向图 G 是欧拉图，当且仅当其**连通**且**没有奇度顶点**。

**Thm**：无向图 G 是半欧拉图，当且仅当其**连通**且**恰有两个奇度顶点**。

**Thm**：有向图 D 是欧拉图，当且仅当其是**强连通**的且每个顶点的**出度等于入度**。

**Thm**：有向图 D 是半欧拉图，当且仅当其是**单向连通**的且有两个奇度顶点，一个入度比出度大 1，一个入度比出度小 1，其余每个顶点的**出度等于入度**。

**Thm**：G 是非平凡的欧拉图，当且仅当 G 是连通的且为几个不重合的圈的并

{% noteblock quote %}

**Fleury Alg （求欧拉回路）**

1. 任取 $v_0\in V(G)$，令 $P_0=v_0$
2. 设 $P_i = v_0e_1\dots e_i v_i$，若 $E(G) - \{e_1,e_2,\dots,e_i\}$中没有与 $v_i$ 关联的边，则停止，否则按以下条件选下一条边：
   1. $e_{i+1}$ 与 $v_i$ 关联
   2. 优先选：$e_{i+1}$ 不是 $G-\{e_1,\dots,e_i\}$ 中的桥

{% endnoteblock %}

## 哈密顿图

**Def**：

- （哈密顿通路）经过图中所有点一次且仅一次的通路
- （哈密顿回路）经过图中所有点一次且仅一次的回路
- （哈密顿图）有哈密顿回路
- （半哈密顿图）有哈密顿通路

**Thm**：G 是哈密顿图，则$\forall (V_1 \in V\wedge v_1\neq\emptyset)\quad p(G-V_1) \le |V_1|$

**Thm**：G 是半哈密顿图，则$\forall (V_1 \in V\wedge v_1\neq\emptyset)\quad p(G-V_1) \le |V_1|+1$

**Thm**：$\forall v_i,v_j$ 不相邻，则 $d(v_i)+d(v_j)\ge n-1$，则有哈密顿通路

**Thm**：$\forall v_i,v_j$ 不相邻，则 $d(v_i)+d(v_j)\ge n$，则有哈密顿回路

**Thm**：若 $u,v$ 是 n 阶无向简单图的两个不相邻的顶点，且 $d(u)+d(v)\ge n$ 则 $G$ 是哈密顿图当且仅当 $G\cup (u,v)$ 时哈密顿图。

**Thm**：若 $D$ 是竞赛图，则其中有哈密顿通路

## 最短路问题