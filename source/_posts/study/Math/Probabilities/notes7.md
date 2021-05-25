---
title: 「随机数学与数理统计」7 - 参数估计
date: 2020-12-23
categories: 数学
tags:
  - 概率论
  - 统计
math: true
hide: false
---

1. 矩估计
2. 极大似然估计
3. 评判估计量的方法

<!-- more -->

## 参数估计

### 两种常用的参数估计方法

#### 矩估计法

> - 辛钦大数定律：样本较大时，$A_r=\frac{1}{n}\sum_{i=1}^nX_i^r\rightarrow EX_r$
> - 格里汶科定理：格里汶科定理是指当样本容量n→∞时，经验分布函数以概率1一致收敛于总体的分布函数。


**Def**（矩估计）设总体 $X$ 的分布 $f(x;\theta_1,...,\theta_k)$ 中有 $k$ 个位置的参数 $\theta_{1..k}$，$(X_1,...,X_n)$ 时总体 $X$ 的样本。若总体 $X$ 的$k$ 阶原点矩 $EX_k$ 存在，并且 $\alpha_r(\theta_1,...\theta_k)=EX^r$ 时总体 $X$ 的 $r$ 阶原点矩，记 $A_r$ 为样本的 $r$ 阶原点矩，由：

$$
\alpha_r(\theta_1,\dots, \theta_k)=A_r(\theta_1,\dots,\theta_r)\qquad r=1,...,k
$$

解得的 $\hat\theta_r=\hat\theta_r(X_1,...,X_k)$，并以 $\hat\theta_r$ 作为参数的估计量，称 $\hat\theta_r$ 为参数 $\theta_r$ 的估计量。

> 1. 不唯一（依赖于 r）
> 2. $EX^k$ 有限
> 3. 要求 $n$ 比较大

#### 极大似然估计

> 基本思想：$X\sim P(X;\theta)\rightarrow P(X=x)$
> 使得：$\hat\theta$ 能使得出现样本 $X_{1..k}$ 的概率最大

**Def**（似然函数）设总体 $X$ 的分布为 $f(x;\theta_1,\dots,\theta_k)$，其中 $\theta_{1\dots k}$ 为未知参数，$(X_1,\dots,X_n)$ 为简单随机样本，称

$$
L(\theta_1,...,\theta_k)=\prod_{i=1}^nf(x_i;\theta_1,...,\theta_k)
$$

**Def**（MLE-极大似然估计）称 $\hat\theta =\mathrm{argmax} L(\theta)$ 为 $\theta$ 最大似然估计量

> 求法：
> 1. 写似然函数
> 2. 优化似然函数
>
> 例如：假设总体服从参数为 $p$ 的 0-1 分布，$(X_1,...,X_n)$ 为样本，求 $p$ 的最大似然估计
>
> 1. 似然函数为：$L(x_1,...,x_n;p)=p^{n\bar X}(1-p)^{n-n\bar X}$
> 2. 取对数：$\ln L=n\bar X\ln p+n(1-\bar X)\ln (1-p)$
> 3. 对 $p$ 求偏导，取得极值 $\hat p=\bar X$

*常见的有*：

1. $\displaystyle X\sim P(\lambda)\Rightarrow \hat \lambda=\bar X$
2. $\displaystyle X\sim e(\lambda)\Rightarrow \hat \lambda=\frac{1}{\bar{X}}$
3. 0-1 分布：$\hat p = \bar X$
4. $X\sim U(a,b)\Rightarrow,a=\min x_i,b=\max x_i,\quad i = 1,...,n$

*对于正态分布* $\displaystyle X\sim N(\mu, \sigma^2)$，注意对于 $\sigma^2$ 整体求导，得到：

$$
\begin{cases}
\hat \mu=\bar X\\
\hat{\sigma^2} = \frac{1}{n}\sum_{i=1}^n(X_i-\bar X)^2=B_2
\end{cases}
$$

**Thm**（最大似然估计的不变性）

### 评选估计量的标准

1. 无偏性
2. 有效性
3. 相合性

#### 无偏性

**Def**（无偏性）若 $\hat\theta(X_1,...,X_n)$ 为 $\theta$ 的估计量，若$\hat \theta(X_1,..,X_n)$ 的数学期望 $E\hat\theta$ 存在，且对于任一的 $\theta \in \Theta$，$E\hat\theta=\theta$ 则称 $\hat\theta$ 为 $\theta$ 的一个无偏估计量

- $EX$ 为$\mu$ 的无偏估计
- $A_k$ 为 $EX^k$ 的无偏估计
- $ET^2$ 为 $\sigma^2$ 的**渐进**无偏估计
- $ES^2$ 为 $\sigma^2$ 的无偏估计

*注意*：

1. 若 $\hat\theta$ 是 $\theta$ 的无偏估计，$\hat{g(\theta)}$ 不一定是 $g(\theta)$ 的无偏估计。（除非 $g(\theta)$ 是线性的）
2. 同一个参数的无偏估计不一定唯一

#### 有效性

**Def**（有效性）若 $\hat\theta_1,\hat\theta_2$ 都是 $\theta$ 的无偏估计，若$D\hat\theta_1\le D\hat\theta_2$ 则称 $\hat\theta_1$ 比 $\hat\theta_2$ 有效。

#### 相合性

**Def**（相合性）若$\hat\theta(X_1,...,X_n)$ 是 $\theta$ 的一个估计量，若对于任一 $\varepsilon>0$ 有：

$$
\lim_{n\rightarrow\infty}P(|\hat\theta-\theta|\ge \varepsilon)=0
$$

则称 $\hat\theta$ 为 $\theta$ 的相合估计量

**Def**（均方误差）设 $\hat\theta$ 为 $\theta$ 的一个估计量，

- 称 $E(\hat\theta - \theta)^2$ 为 $\hat \theta$ 估计 $\theta$ 时的均方误差
- 称 $b=E(\hat\theta - \theta)$ 为 $\hat \theta$ 估计 $\theta$ 时的偏差

**Thm**：若 $D\hat\theta$ 存在，则 $E(\hat\theta-\theta)^2=D\hat\theta +b(\theta)^2$

**Thm**（Markov 不等式）$E|X|^k$ 则对与任意的 $\varepsilon>0$，有$\displaystyle P(|X|>\varepsilon)\le \frac{E|X|^k}{\varepsilon^k}$

**Thm**（相合性判定定理）若$\lim D\hat\theta=\lim b(\theta)=\lim E(\hat\theta-\theta)=0$ 则称 $\hat\theta$ 是 $\theta$ 的相合估计量

例如：证明 $X_1,...$ 是来自总体$N(\mu,\sigma^2)$ 的容量为 n 的简单随机样本，则$S^2=\frac1{n-1}\sum(X_i-\bar X)^2$ 和 $B_2=\frac1{n}\sum(X_i-\bar X)^2$ 都是 $\sigma$ 的相合估计

**Thm**：用矩估计得到的估计量都具有相合性

### 区间估计

**Def**（置信区间）设 $X_1,...$ 是来自总体$X$ 容量为 n 的简单随机样本，$\theta$ 是一个参数，$\hat\theta_1,\hat\theta_2$ 是两个统计量，若给定$\alpha$ 满足：$P(\hat\theta_1<\theta < \hat\theta_2)=1-\alpha$ 则称区间 $(\hat\theta_1,\hat\theta_2)$ 是参数 $\theta$ 的置信度为 $1-\alpha$ 的区间估计，$\hat\theta_1,\hat\theta_2$ 为置信区间的下限、上限。

- 对于离散型随机变量，若无法达到 $P=1-\alpha$ 则我们找到尽量接近的值使得$P\ge 1-\alpha$

{% noteblock quote %}

#### （已知 σ） 如何求参数 $\theta$ 的置信区间？

> 若 $X\sim N(\mu,\sigma^2)$ $\sigma^2$ 已知，$\mu$ 未知，求 $\mu$ 置信水平为 1-α 的置信区间

注意到：$\displaystyle\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1)$

则：$P(\displaystyle|\frac{\bar X-\mu}{\sigma/\sqrt n}|<z_{\alpha/2})=1-\alpha$

即：$P(\bar X-\frac{\sigma}{\sqrt n}z_{\alpha/2}<\mu<\bar X+\frac{\sigma}{\sqrt n}z_{\alpha/2})=1-\alpha$，其中$z_{\alpha}$ 为上侧 α 分位点

{% endnoteblock %}

> 置信区间越短 → 精度高

{% noteblock quote %}

1. 寻求样本和 $\theta$ 的函数 $W(X_1,...,X_n;\theta)$ 其分布不依赖于 $\alpha$ 和其他位置参数。（*枢轴量*）
2. 构造常数 $a,b$ 使得 $P(a<W<b)=1-\alpha$
3. 从中解出 $\hat\theta_1(X_1,...,X_n),\hat\theta_2(X_1,...,X_n)$ 得到置信区间

{% endnoteblock %}

#### 单个正态总体的置信区间

##### μ 的置信区间

*$\sigma^2$ 已知*，利用 $W=\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1)$ 置信区间为：

$$
\left(\bar X-\frac{\sigma}{\sqrt n}z_{\alpha/2},\bar X+\frac{\sigma}{\sqrt n}z_{\alpha/2}\right)
$$

*$\sigma^2$ 未知*，利用 $W=\frac{\bar X-\mu}{S/\sqrt n}\sim t(n-1)$

$$
\left(\bar{X}-\frac{S}{\sqrt{n}}t_{\alpha/2} (n-1),\bar{X}+\frac{S}{\sqrt{n}}t_{\alpha/2} (n-1)\right)
$$

##### σ2 的置信区间

*μ未知*，利用 $\frac{(n-1)S^2}{\sigma^2}\sim \chi^2(n-1)$，置信区间为：

$$
\left(\frac{(n-1)S^2}{\chi^2_{\alpha/2}(n-1)},\frac{(n-1)S^2}{\chi^2_{1-\alpha/2}(n-1)}\right)
$$

*μ已知*，在上式 $S^2$ 中用 $\mu$ 代替 $\bar X$

$$
\left(\frac{\sum (X_i-\mu)^2}{\chi^2_{\alpha/2}(n-1)},\frac{\sum (X_i-\mu)^2}{\chi^2_{1-\alpha/2}(n-1)}\right)
$$

#### 两个正态总体的均值差和方差比的置信区间

##### μ1-μ2 的置信区间

*σ1, σ2 已知*，利用：

$$
\frac{\bar X-\bar Y-(\mu_1-\mu_2)}{\sqrt{\frac{\sigma_1^2}{m}+\frac{\sigma_2^2}{n}}}\sim N(0,1)
$$

则：

$$
\left(
    \bar X-\bar Y -u_{\alpha/2}\sqrt{\frac{\sigma_1^2}{m}+\frac{\sigma_2^2}{n}},\bar X-\bar Y + u_{\alpha/2}\sqrt{\frac{\sigma_1^2}{m}+\frac{\sigma_2^2}{n}}
\right)
$$

*$\sigma_1^2=\sigma_2^2=\sigma^2$ 未知*，利用：

$$
\frac{\bar X-\bar Y-(\mu_1-\mu_2)}{S_w\sqrt{\frac{1}{m}+\frac{1}{n}}}\sim t(m+n-2)
$$

因而，置信区间为：

$$
\left(\bar X-\bar Y-t_{\frac{\alpha}{2}}(m+n-2)S_w\sqrt{\frac{1}{m}+\frac{1}{n}},\bar X-\bar Y+t_{\frac{\alpha}{2}}(m+n-2)S_w\sqrt{\frac{1}{m}+\frac{1}{n}}\right)
$$

##### 两个正态总体方差比 σ12/σ22 的置信区间

*μ1, μ2 未知*，利用：

$$
\frac{S_{1m}^2}{S^2_{2n}}\frac{\sigma_2^2}{\sigma_1^2}\sim F(m-1,n-1)
$$

置信区间为：

$$
\left(\frac{1}{F_{\alpha/2}(m,n)}\frac{n}{m}\frac{\sum(X_i-\mu_1)^2}{\sum(Y_i-\mu_2)^2},\frac{1}{F_{1-\alpha/2}(m,n)}\frac{n}{m}\frac{\sum(X_i-\mu_1)^2}{\sum(Y_i-\mu_2)^2}\right)
$$

同样的，用$S^2$ 代替其中的 $\sum (X_i-\mu_1)^2$：

*μ1, μ2 已知*，利用：

$$
\frac{S_{1m}^2}{S_{2n}^2}\frac{\sigma_2^2}{\sigma_1^2}\sim F(m-1,n-1)
$$

有：

$$
\left(\frac{1}{F_{\alpha/2}(m-1,n-1)}\frac{n}{m}\frac{S_{1m}^2}{S_{2n}^2},\frac{1}{F_{1-\alpha/2}(m-1,n-1)}\frac{n}{m}\frac{S_{1m}^2}{S_{2n}^2}\right)
$$