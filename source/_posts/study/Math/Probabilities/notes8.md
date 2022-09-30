---
title: 「随机数学与数理统计」8 - 假设检验
date: 2020-12-23
categories: 数学
tags:
  - 概率论
math: true
plugins:
  - mathjax
  - katex
hide: false
group: group-probabilites
sidebar: [group-probabilites, toc]
---

假设检验

<!-- more -->

## 假设检验

### 假设检验的基本概念

*假设检验的基本步骤*：

1. 建立假设：
   - 在假设检验中，通常把一个被检验的假设称为原假设 $H_0$，将不应轻易加以否定的假设作为原假设。当 $H_0$ 被拒绝时而接受的假设称为备择假设 $H_1$，它们常常成对出现。
   - 例如：$H_0:\theta \ge 10,H_1:\theta < 10$
2. 选择检验统计量，给出拒绝域形式
   - 由样本对原假设进行判断总是通过一个统计量完成的，该统计量被称为检验统计量。使得原假设被拒绝的样本观测值所在的区域称为拒绝域 $W$。例如：$W=\{(x_1,x_2,...,x_n):\bar x \le c\}$
3. 选择显著性水平 $\alpha$
   - 预先给定数 $\alpha$（显著性水平），根据：$P(reject~H_0|H_0~right)\le\alpha$
4. 给出拒绝域，确定显著性水平后，可以给出检验的拒绝域 $W$
5. 做出判断
   - 给出了观察值 $x_1,...,x_n$ 若 $(x_1,...,x_n)\in W$ 则拒绝 $H_0$；反之接受 $H_0$

*两类错误*：

1. 第一类错误（$H_0$ 成立，而样本满足拒绝域）的概率 $\alpha$
2. 第二类错误（$H_0$ 不成立，而样本不满足拒绝域）的概率 $\beta$

### 单个正态总体参数的假设检验

#### 均值 μ 的检验 （σ 已知）

检验统计量：$\displaystyle U=\frac{\bar x-\mu_0}{\sigma/\sqrt n}$

*双边检验*：$H_0:\mu=\mu_0\leftrightarrow H_1:\mu\ne\mu_0$

$$
\begin{aligned}
    &U=\frac{\bar{X}-\mu_0}{\sigma/\sqrt n}\sim N(0,1)\\
    &P(reject~H_0|H_0~right)\le \alpha
\end{aligned}
$$

$\bar X$ 为 $\mu$ 的无偏估计则：$\displaystyle P(reject~H_0|H_0~right)=P(\frac{|\bar{X}-\mu_0|}{\sigma/\sqrt n}\ge \frac{k}{\sigma/\sqrt n})$

拒绝域为：

$$
W=\left\{ (x_1,...,x_n)||\bar x-\mu_0|\ge \frac{\sigma}{\sqrt n}u_{\alpha/2} \right\}
$$

*单边右检验*：$H_0:\mu\le \mu_0$

$$
P(\frac{\bar X-\mu_0}{\sigma /\sqrt n}\ge \frac{k}{\sigma /\sqrt n})\le \alpha
$$

拒绝域为：

$$
S=\left\{ (x_1,...,x_n)|\bar x-\mu_0 \ge \frac{\sigma}{\sqrt n}u_\alpha \right\}
$$

*单边左检验*：$H_0:\mu\ge \mu_0$ 拒绝域为 $\displaystyle S=\left\{  (x_1,...,x_n)|\bar x-\mu_0 \le -\frac{\sigma}{\sqrt n}u_\alpha\right\}$

#### 均值 μ 的检验 （σ 未知）

使用 t 检验法，将上述的 $\sigma$ 替换为 $S_n=\sqrt{\frac{1}{n-1}\sum(x_i-\bar x)^2}$，正态分布替换为自由度为 n-1 的 t - 分布，检验统计量为：$\displaystyle T=\frac{\bar x-\mu_0}{s_n/\sqrt n}$

双侧检验，拒绝域为：

$$
W=\left\{ (x_1,...,x_n)||\bar x-\mu_0|\ge \frac{s_n}{\sqrt n}t_{\alpha/2}(n-1) \right\}
$$

单侧右检验，拒绝域为：

$$
S=\left\{ (x_1,...,x_n)|\bar x-\mu_0 \ge \frac{s_n}{\sqrt n}t_\alpha(n-1) \right\}
$$

单侧左检验，拒绝域为：

$$
S=\left\{ (x_1,...,x_n)|\bar x-\mu_0 \le -\frac{s_n}{\sqrt n}t_\alpha(n-1) \right\}
$$

#### 方差 σ2 的检验

##### μ未知

利用：

$$
\frac{(n-1)S_n^2}{\sigma_0^2}\sim \chi^2(n-1)
$$

##### μ已知

$$
\frac{\sum(X_i-\mu)^2}{\sigma_0^2}\sim\chi^2(n)
$$

#### Summary

|情况|分布|
|--|--|
|σ已知|U~N(0,1)|
|σ未知|T~t(n-1)|
|μ已知|χ2~χ2(n)|
|μ未知|χ2~χ2(n-1)|

### 两个正态总体参数的假设检验

#### 均值μ1，μ2的检验（σ12 σ22已知）

> 检验 $μ_1~\underline{~~}~μ_2$

$$
U=\frac{\bar X-\bar Y}{\sqrt{\sigma_1^2/m+\sigma_2^2/n}}\sim N(0,1)
$$

#### 均值μ1，μ2的检验（σ12 σ22未知）

$$
T=\frac{\bar X-\bar Y}{S_w\sqrt{1/m+1/n}}\sim t(m+n-2),\\
S_w=\sqrt{\frac{(m-1)S_{1m}^2+(n-1)S_{2n}^2}{m+n-2}}
$$

| $H_0$  | 拒绝域  |
|---|---|
|  $\sigma_1, \sigma_2$ 已知  |
| $\mu_1 =\mu_2$ | $abs(u)\ge u_{\alpha/2}$ |
| $\mu_1 =\mu_2$ | $u\ge u_{\alpha}$ |
| $\mu_1 \ge\mu_2$ | $u\le u_{1-\alpha}=u_{-\alpha}$ |
|  $\sigma_1, \sigma_2$ 未知  |
| $\mu_1=\mu_2$ |$abs(t) \ge t_{\alpha/2}(m+n-2)$|
|$\mu_1\le \mu_2$|$t\ge t_\alpha(m+n-2)$|
|$\mu_1\ge \mu_2$|$t\le -t_\alpha(m+n-2)$|

#### 方差 σ12，σ22 的检验（μ1，μ2未知）

> 检验 $\sigma_1^2 ~ \mathrm{\underline{~~~}} ~\sigma_2^2$

$$
F=\frac{S_{1m}^2}{S_{2n}^2}\sim F(m-1, n-1)
$$

#### 方差 σ12，σ22 的检验（μ1，μ2已知）

$$
F=\frac{\sum_{i=1}^m (x_i-\mu_1)^2/m}{\sum_{i=1}^n (y_i-\mu_1)^2/n}\sim F(m, n)
$$

**Summary:**

| $H_0$ | 拒绝域  |
|---|---|
|$\mu_1,\mu_2$ 已知|
| $\sigma_1^2=\sigma_2^2$  | $f\le F_{1-\alpha/2}(m,n)$ 或 $f\ge F_{\alpha/2}(m,n)$ |
|$\sigma_1^2\le \sigma_2^2$|$f\ge F_\alpha(m,n)$|
|$\sigma_1^2\ge \sigma_2^2$|$f\le F_{1-\alpha}(m,n)$|
|$\mu_1,\mu_2$ 未知|
| $\sigma_1^2=\sigma_2^2$  | $f\le F_{1-\alpha/2}(m,n)$ 或 $f\ge F_{\alpha/2}(m,n)$ |
|$\sigma_1^2\le \sigma_2^2$|$f\ge F_\alpha(m,n)$|
|$\sigma_1^2\ge \sigma_2^2$|$f\le F_{1-\alpha}(m,n)$|

### 总体分布的 χ2-拟合优度检验

#### 理论分布完全已知

##### 理论分布 F0 是取有限个值的离散分布

**Thm**（K · 皮尔逊）若假设 $H_0$ 成立，则当样本容量 $n\rightarrow \infty$ 时，则 $\chi^2=\sum_{i=1}^2\frac{(\gamma_i-np_i)^2}{np_i}
$ 渐进分布为 $\chi^2(r-1)$。

若理论分布律为：$P(X=a_i)=p_i$，原假设可以写为：$H_0:P(X=a_i)=p_i$，$r$ 为x取值的个数

使用：

$$
\chi^2=\sum_{i=1}^2\frac{(\gamma_i-np_i)^2}{np_i}
$$

拟合优度：$p(\chi^2_0)=P(\chi^2\ge \chi^2_0)$

利用：$\chi^2=\sum\frac{(\gamma_i-np_i)^2}{np_i}$ 在 $n\rightarrow \infin$ 时，其渐进分布为 $\chi^2(r-1)$


当 $\chi^2\ge\chi^2_\alpha(r-1)$ 则拒绝假设。

##### 理想分布为一般情况

假设可以写为：$H_0:F(x)=F_0(x)$

1. 选择常数，将区间分割成：$(-\infty, a_1],...,(a_{i-1},a_i],...,...(a_r-1,\infty]$
2. 计算 $p_i=F_0(a_i)-F_0(a_{i-1})$
3. 计算统计量 $\chi^2=\sum\frac{(\gamma_i-np_i)^2}{np_i}$
4. 计算出观察值 $\chi^2$
   - 若 $\chi^2\ge\chi^2_\alpha(r-1)$ 则拒绝假设。

#### 理论分布 F0 含有未知参数的情况

我们的假设为：

$$
H_0:F(x)=F_0(x:\theta_1,...,\theta_k)\leftrightarrow
H_0:F(x)\ne F_0(x:\theta_1,...,\theta_k)
$$

1. 使用最大似然估计确定参数
2. 统计量 $\chi^2=\sum\frac{(\gamma_i-np_i)^2}{np_i}\sim \chi^2(r-k-1)$ k 为未知参数个数
3. 当 $\chi^2\ge\chi^2_\alpha(r-1)$ 则拒绝假设。