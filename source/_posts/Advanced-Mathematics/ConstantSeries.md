---
title: 无穷级数
date: 2020-5-25
categories: 高等数学
tags:
  - 高等数学
  - 级数
mathjax: true
---

级数部分相关定理。

<!--more-->

## 常数项级数

### 常数项级数的概念、性质、原理

**Def**：（级数）我们把一个形如 $\sum\limits_{k=0}^{\infty}a_n$ 的式子称为无穷级数

**Def**：级数的部分和、级数的敛散性、级数和的定义

**Thm**：性质，若 $a_n$ 和 $b_n$ 级数收敛，则

- 线性性质
- $\sum\limits_{k=0}^{\infty}(a_k+b_k) =\sum\limits_{k=0}^{\infty} a_k+ \sum\limits_{k=0}^{\infty}b_k$
- 若 $a_n\le b_n$ 则 $\sum\limits_{k=0}^{\infty}a_n\le\sum\limits_{k=0}^{\infty}b_n$
- 任意更改有限项不改变敛散性
- 在不改变次序的情况下，任意添加括号所得到的新的级数敛散性不变，和不变

**Thm**：（Cauchy 收敛原理）级数$\sum\limits_{k=0}^{\infty}a_n$ 收敛的充要条件是 $\forall\varepsilon>0,\exists N\in \mathbf{N}_+\forall p\in \mathbf{N}_+(n>N \rightarrow |\sum\limits_{k=n+1}^{n+p}a_k|<\varepsilon)$

### 正项级数的审敛准则

**Thm**：正项级数$\sum\limits_{k=0}^{\infty}a_n$ 收敛的充要条件是其部分和数列 $\{S_n\}$ 有上界

**Thm**：（比较准则 1 ）设$\sum\limits_{k=0}^{\infty}a_n$ 和 $\sum\limits_{k=0}^{\infty}b_n$ 是正项级数，且 $\forall n\in \mathbf N_+,a_n\le b_n$，则

1. $\sum\limits_{k=0}^{\infty}b_n$ 收敛，则 $\sum\limits_{k=0}^{\infty}a_n$ 收敛
2. $\sum\limits_{k=0}^{\infty}a_n$ 发散，则 $\sum\limits_{k=0}^{\infty}b_n$ 发散

**Thm**：（比较准则 2 极限形式）设$\sum\limits_{k=0}^{\infty}a_n$ 和 $\sum\limits_{k=0}^{\infty}b_n$ 是正项级数，且有$\lim \frac{a_n}{b_n} =\lambda$ 则：

1. $\lambda>0$ 则两个级数有相同的敛散性
2. $\lambda = 0$ 若 $\sum\limits_{k=0}^{\infty}b_n$ 收敛，则 $\sum\limits_{k=0}^{\infty}a_n$ 收敛
3. $\lambda = \infty$ 若 $\sum\limits_{k=0}^{\infty}a_n$ 发散，则 $\sum\limits_{k=0}^{\infty}b_n$ 发散

**Thm**：（达朗贝尔判别法、D'Alembert 准则）若正项级数$\sum\limits_{k=0}^{\infty}a_n$ 满足 $\lim\limits_{n\rightarrow \infty} \frac{u_{n+1}}{u_n} = l$ 则

1. $l<1$，收敛
2. $l>1$，发散
3. $l=1$，敛散性不定

**Thm**：（柯西判别法、Cauchy 准则）若正项级数$\sum\limits_{k=0}^{\infty}a_n$ 满足 $\lim\limits_{n\rightarrow \infty} \sqrt[n]{a_n} = \lambda$ 则

1. $\lambda<1$，收敛
2. $\lambda>1$，发散
3. $\lambda=1$，敛散性不定

\***Thm**：（拉阿伯判别法）若正项级数满足：$\lim\limits_{n\rightarrow \infty} n(\frac{u_n}{u_{n+1}} -1)=R$ 则

1. $R>1$，收敛
2. $R<1$，发散
3. $R=1$，敛散性不定

> 例：讨论 $\displaystyle\sum\limits_{k=0}^{\infty}\frac{(2n-1)!!}{2n!!}\cdot\frac{1}{2n+1}$ 的敛散性
>
> 解：应用拉阿伯判别法 $R = \frac 3 2$ 故级数收敛

**Thm**：（积分判别准则）若存在一个单调下降的非负函数 $f(x)$ 使得 $f(n) = u_n$，则无穷积分与无穷级数有相同的敛散性

### 任意项级数

**Def**：交错级数 $\sum\limits_{k=0}^{\infty}(-1)^n\cdot a_n$

**Thm**：（Leibniz 准则）若交错级数满足

1. $u_n\ge u_{n+1}$
2. $\lim\limits_{n\rightarrow \infty} u_n = 0$

则该交错级数收敛

**Def**：绝对收敛，条件收敛

**Thm**：（绝对收敛准则）若级数 $\sum\limits_{n=1}^{\infty} |a_n|$ 收敛，则级数 $\sum\limits_{n=1}^{\infty} a_n$ 收敛

**Thm**：若级数绝对收敛，则其的任何一个重排绝对收敛，且和相等

**Thm**：若级数 $\sum\limits_{n=1}^{\infty} a_n = A$ 和 $\sum\limits_{n=1}^{\infty} b_n = B$ 绝对收敛，则各项相乘得到的乘积项按任何次序排列得到的级数 $\sum\limits_{n=1}^{\infty} c_n$ 绝对收敛于 $AB$

**Lemma**：（Abel 变换式）$\sum\limits_{k =1}^{m}\alpha_k\beta_k = \sum\limits_{k=1}^{m-1}(\alpha_k-\alpha_k+1)B_k +a_mB_m$

**Lemma**：（Abel 引理）若数组$\{\alpha_k\}$ 是单调的，又有数组 $\{\beta_k\}$ 的部分和为 $B_n$ 满足不等式 $|B_n| = |\sum\limits_{k=1}^{n}\beta_k|\le M$，则有 $\sum\limits_{k=1}^m \alpha_k\beta_k\le M(|\alpha_1|+2|\alpha_m|)$

**Thm**：（狄利克雷判别法）若 $\{a_n\}$ 单调且 $\lim\limits_{k\rightarrow\infty} a_k=0$ 级数 $\sum\limits_{k=1}^\infty b_k$ 部分和序列有界，则级数 $\sum\limits_{k=1}^\infty a_kb_k$ 收敛

**Thm**：（Abel 判别法）若 $\{a_k\}$ 单调有界，且 $\sum\limits_{k=1}^\infty$ 级数收敛，则级数 $\sum\limits_{k=1}^\infty a_kb_k$ 收敛
