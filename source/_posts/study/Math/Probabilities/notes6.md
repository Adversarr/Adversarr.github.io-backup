---
title: 「概率统计与随机过程」 6 - 抽样分布
date: 2020-12-18
categories: 数学
tags:
  - 概率论
  - 统计
math: true
plugins:
  - mathjax
hide: false
---

Chapter 6 抽样分布

<!-- more -->

## 抽样分布

### 基本概念

1. **总体**：在一个统计问题中，研究对象的全体。（所研究对象的某个（某些）数量指标的全体，一个随机变量（多维随机变量）记为 $X$）

2. **样本**：
   - 分组样本
   - 完全样本

**Def**（简单随机样本）设总体 $X$ 的分布为 $F(X)$，$X_1, X_2,...,X_n$ 是是相互独立和总体同分布的随机变量，则称其为来自总体 X 容量为 n 的简单随机样本。

*性质*：

- 样本联合分布函数为 $F(x_1,\dots,x_n)=\prod F(x_i)$
- 简单随机样本的联合分布律：$P(X_1=x^{(1)}, \dots, X_n=x^{(n)})=\prod P(X_i=x^{(i)})$

#### 统计量

**Def**（统计量）设 $X_1, \dots, X_n$ 为取自总体的样本，若样本函数 $T=T(X_1, \dots, X_n)$ 不含有任何未知的参数。则称 $T$ 为统计量。统计量的分布称为抽样分布。

*例如*：

- **Def**（样本均值）$\bar X=\frac{1}{n}\sum_1^nX_i$ 为样本均值
- **Def**（样本方差）$S_n^2=\frac{1}{n-1}\sum_{i=1}^n(X_i-\bar X)^2$ 为样本方差。$S=\sqrt{S_n^2}$ 为样本标准差
- **Def**（偏差平方和）：$\sum(X_i-\bar X)^2=\sum X_i^2-\frac{1}{n}(\sum X_i)^2=\sum X_i^2-n\bar X^2$
- **Def**（原点矩、中心矩）$A_k=\frac{1}{n}\sum X_i^k,~B_k=\frac{1}{n}\sum (X_i-\bar X)^k$

**Thm**：对于总体 $X$，均值为 $\mu=EX$ 方差 $\sigma^2$ 都存在，$X_1,\dots,X_n$ 是来自总体容量为 $n$ 的简单随机样本。则
 - $E\bar X=\mu$
 - $D\bar X=\sigma^2/n$
 - $ES_n^2=\sigma^2$


### 常用分布

#### 卡方分布

**Def**：设$X_1,\dots,X_n$ iid，$N(0,1)$ 的随机变量，则 $\chi^2=\sigma_{i=1}^nX_i^2$ 服从自由度为 $n$ 的 $\chi^2$-分布。

**Thm**：$\chi^2\sim \chi^2(n)$ 则：$f(x)=\frac{1}{2^{n/2}\Gamma(n/2)}e^{n/2-1}e^{-x/2},~x>0$

**Thm**（可加性）若$X_1\sim \chi^2(n),~X_2\sim \chi^2(n)$ 且 $X_1,X_2$ 独立，则$X_1+X_2\sim\chi^2(m+n)$ 

**Thm**（数字特征）若$X\sim \chi^2(m)$ 则：$EX=n,DX=2n$

**Def**（上侧 $\alpha$ 分位点）：$P(\chi^2\ge\chi^2_\alpha(n))=\alpha$ 则称 $\chi^2(n)$ 为自由度为 n 的 $\chi^2$-分布的上侧$\alpha$-分位点

#### t-分布

**Def**：$X$ 是标准正态分布，$Y$服从自由度为 $n$ 的 $\chi^2$ 分布且相互独立，称随机变量 $T=\frac{X}{\sqrt{Y/n}}$ 服从自由度为 $n$ 的 t-分布。

**Thm**：概率密度为

$$
f(t)=\frac{\Gamma(\frac{n+1}{2})}{\Gamma(\frac{n}{2})\sqrt{n\pi}}(1+\frac{t^2}{n})^{-\frac{n+1}{2}}
$$

**Def**（分位点）上侧$\alpha$-分位点

#### F-分布

$X\sim \chi^2(m),~Y\sim\chi^2(n)$ idd. 称$F=\frac{X/m}{Y/n}$服从自由度为 F-分布

**Thm**：密度函数、分位点 $F_{1-\alpha}(m,n)=1/F_\alpha(n,m)$

### 正态总体中统计量的分布

**Thm**（单个正态总体统计量的分布）：设$X$ 服从正态
分布 $N(\mu,\sigma^2),X_1,\dots,X_n$ 是来自总体 $X$ 容量为 $n$ 的简单随机样本：

1. $\displaystyle U=\frac{\bar X-\mu}{\sigma/\sqrt{n}}\sim N(0,1)$
2. $\displaystyle\bar X$ 与 $S^2$ 独立
3. $\displaystyle W=\frac{(n-1)S^2}{\sigma^2}=\sum (\frac{X-\bar X}{\sigma})^2\sim \chi^2(n-1)$
4. $\displaystyle T=\frac{\bar X-\mu}{S}\sqrt{n}\sim t(n-1)$

**Thm**（两个正态总体统计量的分布）：

1. $\displaystyle\frac{\bar X-\bar Y-(\mu_1-\mu_2)}{\sqrt{\sigma_1^2/m+\sigma_2^2/n}}\sim N(0,1)$
2. $\displaystyle\frac{(m-1)S_{1m}^2}{\sigma^2_1}+\frac{(n-1)S_{2n}^2}{\sigma^2_2}\sim\chi^2(m+n-2)$
3. $\displaystyle\sigma_1=\sigma_2=\sigma$ 则 $\frac{\bar X-\bar Y-(\mu_1-\mu_2)}{S_\omega\sqrt{1/m+1/n}}\sim t(m+n-2)$ 其中 $S_\omega=\frac{(m-1)S_{1m}^2+(n-1)S_{2n}^2}{m+n-2}$
4. $\displaystyle\frac{S_{1m}^2/\sigma_1^2}{S^2_{2n}/\sigma_2^2}\sim F(m-1,n-1)$
