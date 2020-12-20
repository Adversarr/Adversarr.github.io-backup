---
title: 「概率统计与随机过程」 5 - 极限定理
date: 2020-12-11
categories: 数学
tags:
  - 概率论
  - 统计
math: true
hide: false
---

极限定理

<!-- more -->

# Chapter 5 - 极限定理

- **Def**(依概率收敛):设 $X_1, X_2, X_3, ...$ 为一随机变量序列，若存在随机变量 X，使得对于任意整数 $\varepsilon > 0$ 总有: $\lim_{n\rightarrow \infty} P(|X_n-X|\ge \varepsilon)=0$ 则称随机变量序列 $\\{X_n\\}_{n\ge 1}$ 依概率收敛于 $X$
    - $\lim_{n\rightarrow \infty} X_n=X,(P)~or~X_n\rightarrow^PX.$

- **Thm**(大数定律):设 $X_1, X_2, \dots$ 为一随机变量序列，数学期望 $EX_n$ 存在，记 $\bar X = \frac 1 n \sum X_i$ 若 $\lim_{n\rightarrow\infty}\bar X_n=E\bar X_n\quad(P)$则称随机变量序列 $\{X_n\}$ 服从大数定律，或者说大数法则成立

- 随机变量的算术平均值 -> 数学期望的算术平均值

### 5.1 大数定律

1. **Thm**（切比雪夫大数定律） 设 $X_1, X_2, \dots$ 为一相互独立的随机变量序列，数学期望 $EX_n$，方差 $DX_n$ 存在，且方差一致有界，则 $\{X_n\}$ 服从大数定律，对于任意的 $\varepsilon>0,\lim P(|\frac 1 n \sum X_i - \frac 1 n \sum EX_i|\ge \varepsilon)=0$

2. **Thm**（辛钦大数定律）:设 $X_i$ 是独立**同分布**的随机变量序列，公共数学期望为$\mu$ 则其满足大数定律:$\lim_{n\rightarrow \infty}P(|\frac 1 n \sum X_i-\mu|\ge \varepsilon)=0$

3. **Thm**(伯努利大数定律):设 $n_A$ 是 $n$ 次独立重复试验中 $A$ 发生的次数，$p$为发生概率，则对于任意正数 $\varepsilon > 0$ 有 $\lim_{n\rightarrow \infty}P(|\frac{n_A}{n}-p|<\varepsilon)=1$

### 5.2 中心极限定理

- **Thm**(中心极限定理):设 $X_i$ 为相互独立的随机变量序列，数学期望 $EX_n=\mu_n$ 方差 $DX_n=\sigma_n^2, n= 1, 2, ...$都存在，记:$B_n^2=\sum_{i=1}^2\sigma_i^2,\quad Y_n=\sum_{i=1}^n \frac{X_i-\mu_i}{B_n},\quad n = 1,2,...$则 $Y_n$收敛到标准正态分布 $N(0,1)$：$\lim_{n\rightarrow \infty} P(Y_n\le x)=\lim_{n\rightarrow \infty}P((\sum X_i-\sum EX_i)/\sqrt{\sum DX_i}\le x)=\varPhi(x)$

- **Thm**（林德伯格定理）设 $X_1, X_2,...$ 为相互独立的随机变量序列，且满足：$\forall \varepsilon,\displaystyle\lim _{n\rightarrow \infty}\frac 1 {B_n^2}\sum\int_{|x-\mu_k|\ge \varepsilon B_n}(x-\mu_k)^2dF_k(x)$ 其中 $F_k(x)$ 为分布函数，$\mu_k=EX_k,\sigma_k^2=DX_k,B_n^2=\sum \sigma_k^2$，则 $\{X_n\}$ 服从中心极限定理
- **Thm**（列维-林德伯格定理）设 $X_1,...$ 为相互独立同分布的随机变量序列，且 $EX_n=\mu, DX_n=\sigma^2<+\infty$ 则随机变量序列 $\{X_n\}$ 服从中心极限定理：$\displaystyle\lim P((\sum X_i-n\mu)/\sigma\sqrt n \le x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^xe^{x-\frac{x^2}{2}}\mathrm dx=\varPhi(x)$

从而：$n$ 充分大时：$\displaystyle P(x_1<\sum X_i\le x_2)\approx\varPhi(\frac{x_2-n\mu}{\sigma\sqrt n})-\varPhi(\frac{x_1-n\mu}{\sigma\sqrt n})$

- **Thm**（棣莫弗-拉普拉斯中心极限定理）若 $\mu_1, ...$ 服从二项分布 $b(n,p),q=1-p$ 则 $\displaystyle\lim_{n\rightarrow \infty}P(\frac{\mu_n-np}{\sqrt{npq}}\le x)=\varPhi(x)$
