---
title: 面向夏令营的实变函数整理
date: 2022-03-28
categories: 数学
tags:
  - 实变函数
  - 数学
  - 夏令营
mathjax: true
hide: false
plugins:
  - mathjax
group: group-adv-math
sidebar: [group-adv-math, toc]
---

谁能想到呢。

<!-- more -->


{% folding 目录 %}

- [集合论](#集合论)
  - [集合](#集合)
    - [集合运算：](#集合运算)
    - [上极限和下极限相关内容：](#上极限和下极限相关内容)
  - [映射](#映射)
  - [Rn空间](#rn空间)
    - [闭集、开集、Borel集](#闭集开集borel集)
    - [开集结构、连续性](#开集结构连续性)
    - [基本定理](#基本定理)
- [勒贝格测度](#勒贝格测度)
  - [外测度、可测集](#外测度可测集)
    - [外测度](#外测度)
    - [Lebesgue可测集](#lebesgue可测集)
    - [测度空间](#测度空间)
  - [可测函数](#可测函数)
    - [基本性质](#基本性质)
    - [测度空间上的可测函数](#测度空间上的可测函数)
  - [Lesbegue可测函数列的收敛性](#lesbegue可测函数列的收敛性)
    - [几乎处处收敛/几乎一致收敛](#几乎处处收敛几乎一致收敛)
    - [依测度收敛](#依测度收敛)
    - [可测函数和连续函数的关系](#可测函数和连续函数的关系)
- [Lebesgue 积分](#lebesgue-积分)
  - [Lebesgue 可测函数的积分](#lebesgue-可测函数的积分)
    - [非负可测函数的积分](#非负可测函数的积分)
    - [一般可测函数](#一般可测函数)
    - [Riemann积分和Lebesgue积分的关系](#riemann积分和lebesgue积分的关系)
    - [测度空间上的可测函数积分](#测度空间上的可测函数积分)
  - [极限定理](#极限定理)
    - [Riemann 可积的刻画](#riemann-可积的刻画)
  - [重积分和累次积分](#重积分和累次积分)
    - [Fubini 定理](#fubini-定理)
- [微分和不定积分](#微分和不定积分)
  - [单调函数的可微性](#单调函数的可微性)
  - [有界变差函数](#有界变差函数)
  - [不定积分的微分](#不定积分的微分)
    - [绝对连续函数和微积分基本定理](#绝对连续函数和微积分基本定理)
  - [分部积分公式和积分中值定理](#分部积分公式和积分中值定理)
- [L^p^空间](#lp空间)
  - [定义和基本性质](#定义和基本性质)
  - [Lp 空间的结构](#lp-空间的结构)
    - [完备空间](#完备空间)
    - [可分空间](#可分空间)
  - [L2内积空间](#l2内积空间)
    - [内积和正交系](#内积和正交系)
    - [广义 Fourier 级数](#广义-fourier-级数)
  - [Lp中的范数公式](#lp中的范数公式)

{% endfolding %}

## 集合论

### 集合

#### 集合运算：

1. 代数 -- 交并补差
2. 分析 -- 上下极限
3. 直积

上下极限可以有两种定义方式：

$$
\lim\sup _{n\rightarrow \infty} A_n =\lim _{ n \rightarrow \infty}\bigcup_{k = n}  ^ \infty A_n  = \bigcap _ { n = 1} ^ \infty\bigcup_{k = n}  ^ \infty A_n 
$$

对于下极限同样定义。

#### 上极限和下极限相关内容：

集合的上下确界 $\sup, \inf$

Theo
: 确界存在定理


上下极限也可以通过上下界定义：

$$
\lim \sup = \inf \sup \quad \lim \inf = \sup \inf
$$

> 类比点列、函数的上下极限定义

### 映射

1. 映射
2. 集合势

研究可列：

1. 任何无穷集合中包含可列的子集
2. 可列集的无穷子集可列
3. 可列集的交并都可列

### Rn空间

1. 定义${\mathbb R}^n$
2. 线性空间、范数、柯西不等式、距离、球

考察点集：

1. 点：内点、边界点、聚点
2. 诱导集合：闭包、边界
3. 相互关系：稠密

#### 闭集、开集、Borel集

1. 闭集、开集的定义

极限性质：
1. 开集的并始终是开的，两个开集的交是开的
2. 闭集的交始终是闭的，两个闭集的并是闭的
3. 从而定义$F_\sigma$型集（可数闭集并）和$G_\delta$型集（可数开集的交）

推广上述性质：$\sigma$-代数

#### 开集结构、连续性

Theo
: ${\mathbb R}$ 上任意非空开集是至多可数个开集的并

Theo
: ${\mathbb R}^n$ 上的任意非空开集是之多可数个互不相交的半开矩体的并。

通过这两个定理，我们来观察函数的连续性：

Theo
: 设 $f:{\mathbb R}^n \rightarrow {\mathbb R}$ 则TFAE：
1. $f\in C$
2. $\forall \lambda, \{f < \lambda\}, \{f > \lambda \}$ 是开的
2. $\forall \lambda, \{f <= \lambda\}, \{f >= \lambda \}$ 是闭的

#### 基本定理

1. Cauchy-收敛原理
2. 有限覆盖定理
3. 闭区间套定理
4. 魏尔斯特拉斯定理

关于紧集：

1. 定义：任意开覆盖有有限子覆盖
2. 性质：在 ${\mathbb R} ^ n$ 中就是有界闭集

## 勒贝格测度

### 外测度、可测集

#### 外测度

外测度
: 设 $E$ 是 ${\mathbb R} ^ n$ 中的点集，若$\{I_k\}$是一列开矩体，且为$E$的一个开覆盖，确定了一个实数：$u = \sum _{k} I_k$，令：
$$
m^*(E) = \inf \{u\}
$$
称为其的$Lebesgue$外测度。

关于外测度的性质：
1. 非负性
2. 单调性
3. 次可加性
4. 平移不变性

> 1. 单点集、可数点集的外测度都为 0
> 2. $n-1$ 维超平面测度为0
> 3. 康托集外测度为0

{% folding 题目 %}

1. 求证$m^* = \sup / \inf$ 这一类
   1. 一般一边好证明（直接用单调性）
   2. 另一边用次可加性+$\varepsilon$的任意性来描述
2. 求证有子集满足 xxx 条件
   1. 设函数，利用连续性


{% endfolding %}





#### Lebesgue可测集

外测度不符合可加性！因此在集合上加Carathedory条件：

可测
: 设 $E \subseteq {\mathbb R} ^ n$ 如果$\forall T \subset {\mathbb R} ^ n$，有
$$
m^*(T) = m^*(T \cap E) + m^*(T\cap E^c)
$$
则称之为 Lebesgue 可测，全体记为 $\mathcal M$ 测度即其外侧度

> 上述条件中实际上只需要$\ge$成立即可（另一侧自然成立）

考虑原来的简单集合：

Theo
: 
1. 外测度的零测集是可测的，即为零测集。
2. 对开矩体而言，其测度为其“长度”

对于可测集，其具有如下性质：

1. 空集可测，测度为0
2. 可测集的交并补差都是可测集
3. **可数可加性**：对于互不相交的可测集$E_i$，取并和取测度可换
4. 平移不变性

进一步考察和极限的关系：

Theo
: 可测集合的可数交是可测的

考虑极限和测度交换：

Theo
: 对于递增的可测集列$E_i$，则其极限可测，且有极限和测度可换

Theo
: 对于递减的可测集列$E_i$，若存在$m(E_i) < +\infty$，则其极限可测，且有极限和测度可换

> 上式要求存在一个集合测度有限：考察$E_i = [i, \infty)$的极限的测度和其测度的极限

下面的定理表述了可测集和 Borel 集的关系

Theo
: 若$E$可测，则存在 Borel 集$G, F$，使得$F\subset E\subset G$ 且 $m(F) = m(E) = m(G)$
换句话说，对于任意可测集，存在 Borel 集来从两侧（在测度意义上）逼近。

{% folding 题目 %}

TODO

{% endfolding %}


#### 测度空间

> TODO

### 可测函数

对于函数，正如我们一开始用开集闭集来表征连续性一样，考察用可测集来表述可测性。

可测函数
: 设 $E \subseteq \mathbb R^n$ 可测，$f$ 是 $E$ 上的函数，若对于任何$t\in {\mathbb R}$有
$$
E(f>t) := \{x\in E| f(x) > t\}
$$
都可测，则称函数在$E$上可测，用$M(E)$表示。

1. 对于上述定理中的$t\in E$，只需要考察稠密的$t\in E'\subset E$即可
2. 对于 $>$，可以等价替换为 $\ge, \le , <$

对于以上的定义，我们还有一些基础的结论：

1. 可测函数列的收敛点集和发散点集是可测的。
2. 若$f,g$都可测，则$E[f>g], E[f\ne g]$可测（用有理数集插在$f,g$之间）



我们考察在这个定义下的简单函数，他们通过特征函数来定义：

简单函数
: 设有互不相交的$E_i$是$E$的一个分划，称
$$
\varphi (x) = \sum_{i = 1} ^ m \alpha _ i \chi _{E_i} (x)
$$
是简单函数，当$E_i$是矩体时，$\varphi$是阶梯函数

显然，简单函数是可测的。而下面的定理说明了简单函数能够构建出一个可测函数：

#### 基本性质

Theo
: 对于可测函数集，
1. 是线性空间（对非零除法也是）
2. 连续函数都可测

下面考察其极限性质：

Theo
: 对于可测函数列的 $f_k$的 上确界，下确界，上极限，下极限 都是可测函数

Theo
: 对于可测函数列，若$f_k \rightarrow f$，则 $f$ 可测。

下面考虑取绝对值前后的可测性：

Theo
: 对于实值函数，可测的充要条件是正部和负部都是可测的，且若$f$可测，则$|f|$可测

考虑复合函数的可测性：

Theo
: 对于 $f\in C$ 和 $g\in M$ 有 $h=f\circ g$可测

下面引入几乎处处的概念：

几乎处处
: 称E在$A$几乎处处满足P(E)，是指存在一个固定的零测的$Z$使得对$A - Z$满足P(E)

从而，我们有：

Theo
: 对于实函数，若$f = g\quad a.e.$则$f$与$g$有相同的可测性。

从上面的描述中不难看出，相比于**连续性**，可测性在极限运算下具有良好的性质（保持、交换），这也是我们需要可测的原因。

#### 测度空间上的可测函数

> TODO

### Lesbegue可测函数列的收敛性

这一节，我们详细讨论收敛的概念。

#### 几乎处处收敛/几乎一致收敛

几乎处处收敛
: （直接从几乎处处收敛的定义得到）

相对于几乎处处收敛，我们有稍弱一些的几乎一致收敛，其描述的是定义域极限意义下的收敛性。（即我们不需要得到零测集，而得到测度充分小的集合）

几乎一致收敛
: $\forall \delta > 0, \exists E_\delta \subset E$ 使得（测度充分小）$m(E_\delta) < \delta$，且在 $E - E_\delta$上满足一直收敛到$f$。

下面的定理说明了这两个收敛行的关系：

叶戈罗夫定理
: 对于**有限测度集**上的几乎处处**有限**的可测函数列，若函数列几乎处处收敛，则函数列几乎一致收敛

有限和有界是不同的：$y = 1/x$ 在$(0, 1)$无界，但其是有限的。有界是对于区间而言，而有限是对于点（$< +\infty$而言）

#### 依测度收敛

条件更弱，去掉的集合甚至不一定“稳定”，即该集合只需要测度的极限为0，而不需要考虑其极限是否存在。

依测度收敛
: 对于几乎处处有限的可测函数，对于给定的$\epsilon>0$，其能够满足
$$
m(E(|f_k - f| > \epsilon)) \rightarrow 0
$$
则其是在$E$上依测度收敛到$f$（$f_k\rightarrow_m f$）

显然，几乎处处收敛和几乎一致收敛蕴含了依测度收敛。但依测度收敛给出了收敛到什么函数的本质问题。

Theo
: 若函数列 $f_k$ 依测度收敛于$f, g$ ，则 $f= g \quad a.e.$

Theo — 勒贝格定理
: 对于有限测度集上的几乎处处有限的可测函数，则其依测度收敛到该极限函数

> 如果我们将几乎处处相等作为等价关系，实变函数考察的始终是这个等价关系下对于可测函数集的划分。

考虑从依测度收敛到几乎处处收敛的条件：

Theo — Riesz 引理
: 若 $f_k \rightarrow _m f$，则存在子列几乎处处收敛到$f$

依测度收敛意义下，我们可以类比柯西收敛准则：

依测度基本列
: 设有$f_k$为$E$上几乎处处有限的可测函数列，若
$$
\forall \varepsilon > 0, \quad \lim_{k , j \rightarrow \infty} m(E(|f_i - f_j| > \varepsilon)) = 0
$$
则称其为$E$上的依测度基本列

类似柯西收敛准则：

Theo
: 对于几乎处处有限的可测函数列，依测度收敛当且仅当它是依测度基本列

#### 可测函数和连续函数的关系

连续函数在数学分析中具有重要的作用（特别是一致连续的函数）。因此我们考察连续和可测之间是否有一定的联系。

下面的定理描述了函数可测和连续之间的差别。

Theo — 鲁金定理
: 设$f$是**有限测度集**上几乎处处有限的可测函数，对于任一（充分小的）$\delta > 0$，存在$E$中的闭集$F$，满足$m(E \backslash F) < \delta$ 使$f$在$F$上连续。

下面的定理描述了如何从连续函数构造一个可测函数：

Theo
: 对于任意可测函数$f$，存在连续函数列$g_k$，使得$g_k \rightarrow f\quad a.e.$

上面的定理可以推广为：

Theo
: 对于几乎处处有限的函数$f$，$f$可测，当且仅当$\exists g_k\in C$使得$g_k \rightarrow f\quad a.e.$


## Lebesgue 积分

至此，我们得到了可测函数优秀的极限性质，我们开始考虑一类特殊的极限 -- 积分，这也是实变函数论目的：给积分 - 极限之间的互换关系一个完备的解释。

### Lebesgue 可测函数的积分

#### 非负可测函数的积分

非负简单函数的积分
: 设 $h(x)$ 是可测集 $E$ 上的非负可测函数，定义
$$
h(x) = \sum_{j = 1} ^ m a_j m(E_j) \Longrightarrow \int _ E h(x) \mathrm dx = \sum _{j = 1} ^ m a_j m ( E _ j )
$$
为 $h(x)$ 在可测集$E$傻姑娘的积分。

关于上面定义的积分，其满足：

1. 线性性质
2. 对定义域的连续性：
$$
\lim E_k = E \Rightarrow \lim \int _{E_k} h(x)\mathrm dx = \int _ E h(x) \mathrm dx
$$

其中的 $\mathrm d$仅仅是一个记号，并不代表自变量的微元。

从而我们可以定义：

非负可测函数的积分
: 对于 $f\in \mathcal M ( E)$ 定义
$$
\int _ E f(x) \mathrm dx = \sup \left\{ \int _ E h(x) \mathrm dx | h(x) \le f(x), h(x) 是简单函数 \right\}
$$
若上式有限，则称$f$在$E$上可积。

综合上面的定义可以看出：

1. 对于一个零测集，任何函数的积分都为 0 （因为在实变函数中我们是中认为$0 \cdot \infty = 0$）
2. 对于一个非负可测函数，我们通过和特征函数内积来确定在子集上的积分：
   $$
   \int _A f = \int _E f \cdot \chi _ A
   $$
3. 积分具有保序性

同时，由于上述的定义中 **可积** 这个条件实际上非常宽泛，所以我们很容易得到这样的结论：

Theo
: 有限测度集上的几乎处处有界函数必可积。

这是区别于 Riemann 积分很大的一个地方，因为在 Riemann 积分中，我们甚至连 dirichlet 函数的积分都无法定义！

下面介绍一个著名的定理，它揭示了可测函数积分在极限过程中体现出的性质：

Levi Theo
: 设$\{ f _ k \}$是可测集$E$上的非负可测函数，满足 $f_1 \le f_2 \le \cdots$ 且有
$$
\lim _ {k \rightarrow \infty} f_k ( x) = f(x), \quad \forall x \in E
$$
则有
$$
\lim _ {k \rightarrow \infty} \int _ E f_k (x)\mathrm dx = \int _ E f(x) \mathrm dx
$$

这个定理说明，对于单调、收敛的可测函数，其积分的极限就是极限的积分。

#### 一般可测函数

通过非负可测函数的积分、将可测函数分为正负两部分，我们可以定义：

可测函数积分
: 设 $f$ 是可测函数，$f^+$和$f^-$至少有一个是可积的，则称
$$
\int_E f(x) \mathrm dx = \int _ E f ^+ (x)\mathrm dx - \int _ E f ^ - (x) \mathrm dx
$$
是$f$在$E$上的积分，如果右端两个积分都有限，则称该函数可积$f\in \mathcal L(E)$。

显然，其具有这样的简单性质：
$$
f\in \mathcal L ( E ) \rightarrow | \int_E f(x)\mathrm dx| \le \int _ E | f(x) | \mathrm dx
$$

Theo Lebesgue可测函数积分性质
: 对于积分：
1. $|f| < \infty,\quad a.e.$
2. 如果其中一个可积，$f = g\quad a.e.\implies \int f = \int g$
3. （控制性）若存在 $|f| < |g|\in \mathcal L$，则 $f\in \mathcal L$，且$|\int f| \le \int |g|$
4. 对于有限测度集，有界函数都可积

Theo
: Lebesgue积分具有线性性

下面给出 Lebesgue 积分的等价描述

Theo 可积/积分的等价描述
: 设 $f$ 是**有限测度集**上的**有界可测**函数，$|f| \le M$，作$[-M, M]$的划分，
$$
-M = \alpha_0 < \cdots < \alpha_k = M
$$
设$E_j= E(\alpha_{j-1} < f < \alpha_j)$，对于任意的
$$
\eta_j \in [\alpha_{j - 1}, \alpha _ j]
$$
极限
$$
\lim_{\max \alpha_j - \alpha_{j-1} \rightarrow 0} \sum_{j = 1} ^ k \eta_j m(E_j)
$$
存在，则该极限就是Lebesgue积分。

对于Lebesgue积分，其具有绝对连续性（定义域测度充分小，则积分值充分小）：

Theo 绝对连续性
: 设$f\in \mathcal L$，则对于任意的$\varepsilon > 0$，存在$\delta > 0$，使得对于**任何**的子集$A$，当$m(A) < \delta$时，
$$
|\int_A f(x) \mathrm dx | \le \int_A |f(x)|\mathrm dx \le \varepsilon
$$

当然，对于Lebesgue积分，也有平移不变性。

我们之前考察了可测和连续的关系，在这里我们也有类似的结论：

Theo
: 对于任意Lebesgue可积函数，对于任意 $\varepsilon > 0$，存在一个具有紧支集的连续函数$g$使得
$$
\int_ E| f(x) - g(x) | \mathrm dx < \varepsilon
$$
。因此，可以构造具有紧支集的连续函数列$g_k$，使得
$$
\lim_{k\rightarrow \infty}\int_ E| f(x) - g_k(x) | \mathrm dx < \varepsilon, \quad 即 g_k \rightarrow f\quad a.e.
$$

#### Riemann积分和Lebesgue积分的关系

Theo Riemann积分和Lebesgue积分值的相等性
: 闭区间上有界函数$f(x)$ Riemann 可积，则它时 Lebesgue 可积的且其积分值相等。

#### 测度空间上的可测函数积分

### 极限定理

这一节我们考虑极限和Lebesgue积分的互换关系。

Lebesgue 基本定理
: 设$f_n$是可测集$E$上的非负可测函数列，
$$
f(x) = \sum_{n = 1} ^ \infty f_n(x) 
$$
则
$$
\int _ E f(x) \mathrm dx = \sum _ {n = 1} ^ \infty \int _ E f_n (x) \mathrm dx
$$

> 正函数项级数，和函数积分为积分的和。（积分与求和交换）

从上述定理，我们可以应用到定义域上：

Col
: 设 $E = \bigsqcup E_n$，若$f(x)$在$E$上有积分时，$f(x)$在每一个子集$E_n$时有积分的，且
$$
\int _ E f(x) \mathrm dx = \sum _ {n = 1} ^ \infty \int _{E_n} f(x) \mathrm dx
$$

我们始终不希望只考虑单调的函数列

Fatou 引理
: 对于非负可测函数列$f_n$，有
$$
\int _ E \lim \inf f_n(x) \mathrm dx \le \lim \inf \int _ E f_n(x)\mathrm dx
$$

得到这样一个定理是不够的，我们希望得到更好的结论，而不局限于下确界和不等号：

控制收敛定理
: 给定可测集$E$，设$f_n\subset \mathcal M$，且有
$$
f_n (x) \rightarrow f(x)\quad a.e.[E]
$$
如果存在函数 $F(x) \in \mathcal L(E)$，控制了$|f_n| \le F\quad, a.e.[E]$，那么，$f\in \mathcal L(E)$且
$$
\lim _ {n \rightarrow \infty} \int_{E} f_n (x) \mathrm dx = \int_ E f(x) \mathrm dx
$$

从而，我们有如下几个定理：

Theo
: 设$E$是可测集，$f_n$是 $E$上的可测函数列，该函数列依测度收敛到 $f$ ，若存在$F\in \mathcal L(E)$使得$|f_n| \le F, a.e.[E]$ 则$f_n, f$都在$E$上 Lebesgue可积，且积分和极限可换。

当然，对于有界函数，其在有限测度集上积分有很好的性质：

Theo 有界收敛原理
: 设$m(E)< \infty$，$\{f_n\} \subset L(E)$且一致有界，则当其依测度收敛时，其积分和极限可换。

对于函数项级数，有类似的定理：

Theo
: 对于可积函数列，若
$$
\sum _ {n = 1} ^ \infty \int _ E | f_n ( x ) | \mathrm dx < \infty
$$
则级数$\sum f_n (x)$ 在 $E$上几乎处处收敛，且和函数的积分是各函数积分的和。

#### Riemann 可积的刻画

首先，我们使用振幅函数来入手描述 Riemann 可积性

Theo
: 对于区间上的有界函数$f$，有
$$
\int _ I \omega _f (x) \mathrm dx = \bar \int _ a ^ b f - 
\underline{\int}_{a}^b f
$$

与此同时，我们揭示了Riemann可积的充要条件：

Riemann可积
: 对闭区间上的有界函数 $f$ ：Riemann可积，当且仅当不连续点集是零测的

### 重积分和累次积分

> 重积分的交换就是极限过程的交换。

#### Fubini 定理

截口
: 设$E\subset {\mathbb R}^{p+q}$，对于任意的$x\in {\mathbb R}^p$，令
$$
E_x = \{ y \in {\mathbb R}^ q| (x, y) \in E\}
$$
对于任意的$y$，对应定义$E_y$。其中，$E_x$称为$E$的$x$截口

显然：
$$
m(E) = \int _ {\mathbb R ^ p} m(E_x)\mathrm dx = \int _ {\mathbb R ^ q} m(E_y)\mathrm dy 
$$

Theo
: 设$n = p + q$，$E \in \mathcal M _ n$则
1. 对几乎处处的$x\in \mathbb R ^ p$，有$E_x \in \mathbb R^q$
2. $m(E_x)$在$\mathbb R^q$上几乎处处有定义，且是非负可测函数

借助截口，我们一步步引入Fubini定理，来解决重积分和累次积分关系的问题：

Theo
: 假设$E_1$和$E_2$是$\mathbb R^p$和$\mathbb R^q$中的可测集则$E_1\times E_2 \in M_n$ 且有
$$
m(E_1\times E_2) = m(E_1)m(E_2)
$$

借助该定理，以及测度、积分在极限下的交换关系，我们有：

Toneli
: 设$n = p + q$，$f(x,y)\in \mathcal M (\mathbb R ^ {p + q})$且非负，则
1. 对于几乎处处的$x\in \mathbb R ^ p$，$f(x, \cdot )$是非负可测函数；
2. 积分$F_f(x) = \int _ {\mathbb R^q}f(x, y) \mathrm dy$ 几乎处处有定义，是非负可测函数；
3. 重积分和累次积分相等。

对于上述定理，我们可以将条件加强为`可积`，得到：

Fubini 定理
: 设$n = p + q$，$f(x,y)\in \mathcal L (\mathbb R ^ {p + q})$，则
1. 对于几乎处处的$x\in \mathbb R ^ p$，$f(x, \cdot )$可积；
2. 积分$F_f(x) = \int _ {\mathbb R^q}f(x, y) \mathrm dy$ 几乎处处有定义，且可积；
3. 重积分和累次积分相等。

至此，我们已经几乎研究完了定积分的极限性质，下面将研究微积分基本定理的成立条件

## 微分和不定积分

### 单调函数的可微性

我们先研究单调函数，它是一个性质好（有界变差）的函数！

Vitali 覆盖
: 设$E \subset \mathbb R$，设$\tau = \{ I _ \alpha \}$是一个区间族，若对于任意的$x\in E$和$\varepsilon > 0$，存在一个$I_\alpha \in \tau$，使得$x\in I _ \alpha$ 且 $|I_\alpha| < \varepsilon$，则称$E$是在Vitali意义下的覆盖。

研究Vitali覆盖，一方面是因为其对于任意点都可以找到充分小的区间覆盖，另一方面是其可以任意有限外测度集合，都能找到误差充分笑的有限覆盖：

Vitali 覆盖定理
: 设$E \subset \mathbb{R}$，且$m^*(E)<\infty$，则对于任意的$\varepsilon > 0$存在有限个互不相交的$I_j\in \tau$使得
$$
m^*(E -\cup_{j=1}^n I_j) < \varepsilon
$$

srds，这个东西用的也不多。我们下面先考虑微分的问题：

Dini 导数
: 记如下的
$$
D^+f(x_0):= \limsup_{h\rightarrow 0 ^ +} \frac{f(x_0 + h) - f(x_0)}{h}
$$
同理定义$D^-,D_+,D_-$为 Dini 导数。

显然，函数可导（左右同理），当且仅当Dini导数全部存在且相等。

Lebesgue定理
: 设$f(x)$是$[a,b]$上的递增函数，那么$f$的不可微点集为零测集，且有
$$
\int_ a ^ b f'(x) \mathrm dx \le f(b) - f(a)
$$

例如，
$$
f(x) = I(x>0)
$$
满足上述不等号（因为$0\cdot \infty = 0$）

Fubini 逐项积分定理
: 设$f_n$是$[a,b]$上的递增函数列，且$\sum_{n = 1} ^ \infty f_n$在$[a,b]$上收敛，那么有：
$$
\frac{d}{dx} \left( 
\sum_{n = 1}^\infty f_n(x) 
\right)= \sum_{n = 1}^\infty \frac{d}{dx}f_n(x) \quad a.e.
$$

至此，我们已经解决了一些问题，至少对于单调函数而言是这样的。

### 有界变差函数

这里我们引入有界变差函数，用于描述这个函数的在充分小的区间里**变化**的能力。

有界变差函数
: 设$f$是$[a,b]$上的实函数，做定义域的分划，则：
$$
V_\Delta = \sum_{i = 1}^n | f(x_i) - f(x_{i-1}|)
$$
是$f$在$[a,b]$上的一个变差。对上式取上极限：
$$
\bigvee_{a}^b (f)  := \sup\{V_\Delta\}
$$
是函数在该区间上的**全变差**，若上式有限，那么$f$是$[a,b]$上的有界变差函数。

显然：

1. 单调函数是有界变差函数
2. 可微函数是有界变差函数
3. 有界变差函数空间是线性空间。

有界变差函数对于函数做出了一定的限制，即全区间上的绝对变化是有界的。显然：

Theo
: 设 $f(x)$ 是一个实函数，$a<c<b$，有：
$$
\bigvee_{a}^b (f) = \bigvee_{a}^c (f) +\bigvee_{c}^b (f)
$$

直觉告诉我们，一个有界变差函数可能可以拆成两个函数的差：值增加的时候，为正的函数增加，值减少的时候，权为负的函数增加。那么我们有如下的定理成立：

Jordan 分解定理
: $f \in BV([a,b])$ 当且仅当 $f = g - h$，其中 $g, h$是$[a,b]$上的递增函数

### 不定积分的微分

这里我们开始研究不定积分。而所谓不定积分，我们可以认为是一个变上限积分+C：

Lemma
: 设$f\in \mathcal L [a,b]$，令
$$
F_h(x) = \frac{1}{h} \int _ x ^ {x + h} f(t) \mathrm dt
$$
显然：
$$
\lim_ {h\rightarrow 0} \int _ a ^ b |F_h( x) - f(x)| \mathrm dx = 0
$$

因此，我们有如下的性质

Theo
: 设 $f\in \mathcal L$，令 $F(x) = \int _a^x f(t) \mathrm dt$，则有
$$
F'(x) = f(x) \quad a.e. x\in [a,b]
$$

#### 绝对连续函数和微积分基本定理

至此，我们已经非常接近我们要的答案了（即微积分基本定理成立的充要条件）。为此，我们需要观察出变上限积分一些额外的性质

Lemma
: 设$f$在$[a,b]$几乎处处可微，且$f'(x) = 0\quad a.e.$，如果$f(x)$不是常函数，那么存在$\varepsilon>0$对于任意$\delta > 0$存在$[a,b]$上有限个互不相交的区间，使得其测度之和小于$\delta$，但：
$$
\sum_{i = 1} ^ n| f(y_i) - f(x_i)| > \varepsilon
$$

很显然我们之前构造的阶跃函数满足这样的条件。从而我们希望将这一类函数暂时得从我们的考虑范围内去除。

绝对连续函数
: 设$f(x)$是实函数，若$\forall \varepsilon > 0$，存在$\delta > 0$对于任意两个互不相交的开区间$(x_i, y _ i )$满足其$\sum |y_i - x_i| < \delta$且有
$$
\sum_{i = 1} ^ n |f(y _ i ) - f(x_i)| < \varepsilon
$$
则称其为绝对连续函数

这类函数有些简单的结论：
1. 绝对连续函数是连续函数
2. 绝对连续函数构成线性空间

Theo
: 设$f\in L$，那么其变上限积分是绝对连续函数。

至此，我们找到了微积分基本定理成立的一个充分条件，借助上一节推出的结论，对一个函数先进行变上限积分，拿到的这个变上限积分函数是能够满足微积分基本定理的。这让我们不经怀疑，是否这个条件可以更进一步呢，我们直接引入微积分基本定理：

微积分基本定理
: 若 $f(x)$ 是$[a,b]$上的绝对连续函数，那么
$$
f(x) - f(a) = \int _ a ^ x f'(t) \mathrm dt
$$
即绝对连续函数导数的积分就是自身。

综合以上的讨论，我们得出结论：

微积分基本定理成立 $\iff$ 绝对连续

### 分部积分公式和积分中值定理

老朋友了：

分部积分公式
: 对于可积函数（作为被积函数）成立。

积分第一中值定理
: 若 $f(x)$ 是连续函数，且$g$是非负可积函数，则存在一个$\xi \in [a,b]$使得
$$
\int f\cdot g = f(\xi)\int_a^b g(x) \mathrm dx
$$

第二中值定理
: 若$f\int \mathcal L$，$g$单调，啧$\exists \xi \in [a,b]$ 使得
$$
\int _ a ^ b f \cdot g \mathrm dx = g(a) \int _ a ^ \xi f + g(b) \int _ \xi ^ b f
$$

当然还有更多的积分换元公式，不在这里继续讨论，因为我们有更加重要的内容需要引入：

## L^p^空间

### 定义和基本性质

引入$L^p$空间的很大的原因是积分变换（例如傅立叶等）。

Lp空间
: 设 $f(x)$ 是 $E\subseteq \mathbb R ^ n$上的可测函数，记
$$
\|f\|_p = \left(\int _E |f(x)|^p\mathrm dx\right)^{1/p}\quad 0 < p <= \infty
$$
用$L^p$来表示使得上式有限的函数全体，构成$L^p$空间。

显然Lp空间是线性空间。

{% noteblock info::$L^\infty$ %}

显然我们有两种方式定义这个空间：

1. 直接定义：$L^\infty$表示本性有界（$\exists M, |f(x) | \le M, \quad a.e.$）
2. 极限定义：$L^\infty = \lim_{p\rightarrow \infty} L^p$

这两个定义是等价的

{% endnoteblock %}

另一方面，我们要研究两个线性空间之间的关系，两个范数之间的关系：

Holder 不等式
: 设 $p$ 和 $q$ 是共轭指标（$p^-1 + q ^ -1 = 2, p, q  > 1$，另有$f\in L^p, g\in L^q$，那么：
$$
\|f\cdot g\|_1 = \| f \| _p \cdot \| g \| _ q\quad 1\le p \le \infty
$$

> 上述定理的另一方面也成立，即反Holder不等式

Minkowski不等式
: 设$f,g \in L ^ p$，那么：
$$
\|f + g\| _ p \le \| f \| _ p + \| g \| _ p
$$

$p=2$即三角不等式。

借助以上不等关系，我们来研究$L^p$空间的结构！

### Lp 空间的结构

#### 完备空间

定义$d(f, g) = \| f - g\| _ p$，那么$\left(L^p(E), d\right)$是一个距离空间。

依Lp收敛
: 设$\{f_k\}\in L^p$若存在$f\in L^p$使得
$$
\lim _ {k\rightarrow\infty} d(f_k, f) = \lim_{k\rightarrow \infty} \| f_ k - f \|_ p = 0
$$
则称$f_k$依$L^p(E)$意义收敛于$f$。

关于上述极限：

1. 极限函数在几乎处处相等的意义下唯一
2. 保范数性：极限函数的范数等于范数列的极限

完备距离空间
: 若$\forall f_k$是依$L^p$收敛列，且$f_k \rightarrow f$，那么$f\in L^p$，则称$L^p$是完备距离空间。

Theo
: $L^p, p > 1$都是完备的


#### 可分空间

可分
: 设$\tau$是$L^p$的子集，若$\forall f\in L^p$存在$\{g_k\}\in \tau$，使得$g_k\rightarrow f\quad L^p$，那么称$\tau$在$L^p$中稠密。如果$\tau$可数，那么$L^p$可分。

对于$p\ge 1$的情况，我们也有：

Theo
: $1\le p < +\infty$时，$L^p$可分

我们考虑用一个Lp空间来描述另一个Lp空间：

Theo
: 设$1\le p < \infty, 1\le r \le \infty$ 那么 $L^p \cap L^r$在$L^p$中稠密

### L2内积空间

我们希望不仅仅得到距离，我们还希望得到内积，这要求对于两个函数位置都线性，那么两个函数的次数都必须为 1，从而 $p=2$

#### 内积和正交系

L2内积
: 令
$$
\langle f, g \rangle =\int_E f(x) g(x) \mathrm dx
$$
为 $L^2$空间上的内积（对称正定双线性函数）。

不难证明，该内积对于极限过程可交换。

有了内积的概念，我们试图在$L^2$这个线性空间中找标准正交基，来分解所有的函数。

Theo
: $L^2$中的所有正交系都是可数的。

#### 广义 Fourier 级数

从线性代数的知识我们可以知道，广义上说，给定：

1. 内积
2. 标准正交基
3. 向量

我们可以将向量分解到标准正交基上：

$$
c_i = \langle e_i, f\rangle\quad f \sim \sum_{i = 1} ^ \infty c_i e_i
$$

显然，我们还希望有更好的性质，例如我们不希望用 $\sim$ 符号（因为这里并不能直接相等）

Theo
: 对于标准正交基$\{\varphi_i\}$，$f\in L^2$，取定$k$，作
$$
f_k (x) = \sum_{i = 1}^ k a_i \varphi _ i
$$
则当$a_i = c_i$时，$\|f-f_k\|_2$取最小值

> 利用标准正交基来证明

一般情况下，帕斯瓦尔定理不成立，但我们仍有如下的不等式：

Bessel 不等式
: 设$\varphi_k$是$L^2$中的正交基，$c_i$是函数$f$的Fourier系数，那么：
$$
\sum _ {k = 1} ^ \infty c_k ^ 2 \le \|f_k\|^2
$$

如果我们对于一个函数进行Fourier分解，我们考虑是否能够复原这一个函数，下面的定理说明函数的 Fourier 系数一定能够对应 L2 空间中的一个函数。

Riesz-Fisher
: 设$\varphi_k$是标准正交基，若$c_k$是 Fourier 系数且 $\sum_{k =1} ^ \infty c_k^2< +\infty$，存在
$$
g\in L^2\quad \langle g, \varphi_k\rangle = c_k, k = 1, 2, ....
$$

上面还只是考察了正交系（L2的子集），但我们并不知道这个正交基张成的空间的正交补空间的情况（即是否有一个函数不能用这个正交系表出）因此我们定义：

完全正交系
: 我们称一个正交系是完全的，当$L^2$中不存在任何的非零元和任一$\varphi_k$正交。

Theo
: 三角函数系是完全正交系

正如之前提到的，完全正交系的补空间是零。不难理解：

Theo
: 设$\varphi_k$是标准完全正交系，那么
$$
\forall f\in L ^ 2\quad \lim_{k \rightarrow \infty} \| f - \sum_{i = 1}^ k c_i \varphi_i \| _ 2 = 0
$$

### Lp中的范数公式

我们在这里考虑一些Lp中的范数不等式，来帮助我们在一些问题中进行放缩。

Theo
: 若$f\in L ^ p$，且$1\le p < \infty$，那么存在$g\in L ^{p'}$，且$\| g\| _ {p'} = 1$ 使得，
$$
\|f\|_p = \int _ E f(x) g(x) \mathrm dx
$$

当然上式也可以推广到$L^\infty$：

$$
\| f \| _ \infty = \sup _{\| g \| = 1}\{ | \int _ E f(x) g( x) \mathrm dx\}
$$

最后我们研究 Minkowski 不等式的推广

广义 Minkowski
: 设$f(x, y)$可测，若对于几乎处处的$y\in \mathbb R ^ n$有
$$
f(x, y ) \in L ^p\quad \int _{\mathbb R^n}\left[\int _{\mathbb R ^ n}|f(x, y) |^p  \mathrm dx \right] ^{1/p} \mathrm dy = M < \infty
$$
那么
$$
 \int _{\mathbb R^n}\left[\int _{\mathbb R ^ n}|f(x, y) |^p  \mathrm dy \right] ^{1/p} \mathrm dx\le \int _{\mathbb R^n}\left[\int _{\mathbb R ^ n}|f(x, y) |^p  \mathrm dx \right] ^{1/p} \mathrm dy
$$

