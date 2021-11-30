---
title: 「概率统计与随机过程」 4 - 随机向量的数字特征
date: 2020-12-2
categories: 数学
tags:
  - 概率论
  - 统计
math: true
plugins:
  - mathjax
hide: false
---

随机向量的数字特征

<!-- more -->

## 随机向量的数字特征

### 随机变量的数学期望

#### 数学期望的定义

**Def**（离散型随机变量期望的定义）设离散随机变量的分布列为：$P(X=x_i)=p_i$ 若级数 $\sum x_ip_i$ *绝对收敛*，则称该级数为 $X$ 的数学期望，记为 $E(X)=\sum x_ip_i$

> - 与项的排列顺序无关
> - 有限个值 → 必然存在

#### 连续型随机变量

**Def**（连续型随机变量期望的定义）设连续型随机变量，其密度函数为：$f(x)$ 若积分 $\int_{-\infty}^\infty xf(x)\mathrm dx$ *绝对收敛*，则称该积分为 $X$ 的数学期望，记为$E(X)=\int_{-\infty}^{+\infty}xf(x)\mathrm dx$

- 例如柯西分布：$F(x)=\frac{1}{\pi}(\arctan x+\frac{\pi}{2})$ 不存在数学期望

#### 随机变量函数的数学期望

**Thm**：若 $Y$ 是 $X$ 的函数 $Y=g(X)$，绝对收敛的情况下：

1. $E(Y)=\sum g(x_i)P(X=x_i)$
2. $E(Y)=\int g(x)f(x)\mathrm dx$

**Thm**：若 $Z=g(X,Y)$，则：

1. $Eg(X,Y)=\sum\sum g(x _ i,y _ j)p_{ij}$
2. $Eg(X,Y)=\iint g(x,y)f(x,y)\mathrm dx\mathrm dy$

*期望的性质*：

- $E(·)$是线性的：$E(aX+bY+c)=aEX+bEY+c$
- $X,Y$ 独立 则：$E(XY) = E(X)E(Y)$

### 随机变量的方差

#### 方差的定义

**Def**（方差）若随机变量 $X$ 的数学期望存在，则 $E(X-EX)^2$ 为 $X$ 的方差随机变量偏离中心的程度 $DX=Var(X)=E(X-EX)^2$

1. 标准差：$\sigma(X)$
2. 计算方法：$DX=EX^2-(EX)^2$

##### 方差的性质

1. 对于常数 c $Dc=0$
2. $D(aX+b)=a^2DX$
3. $X,Y$ 独立，则 $D(X\pm Y)=DX+DY$
   - $D(\sum c_iX_i)=\sum c_i^2DX_i$
4. $DX=E(X^2)-(EX)^2$
5. $DX=0\iff P(X=EX=c)=1$
6. $X_i\sim N(\mu_i,\sigma_i^2)$ 则：$\sum c_iX_i\sim N(\sum c_iu_i, \sum c_i^2 \sigma_i^2)$

**Thm** 切比雪夫不等式：$\forall\varepsilon>0, E(X)=\mu,DX=\sigma^2\Rightarrow P(|X-\mu|>\varepsilon)\le \sigma^2/\varepsilon^2$

### 协方差与相关系数

#### 定义

**Def**（协方差）设 $X，Y$ 是两个随机变量，$E(X-EX)(Y-EY)$ 存在，则$\displaystyle Cov(x,y)=E(X-EX)(Y-EY)$
**Def**（相关系数）$\displaystyle\rho_{XY}=\frac{Cov(X,Y)}{\sqrt{DX}\sqrt{DY}}$

**Thm**：$D(X\pm Y)=DX+DY+2Cov(X,Y)$

- 推广至 n 个：$D(\sum c_iX_i)=\sum c_i^2DX_i+2\sum c_ic_jCov(X_i,X_j)$
- 常用计算公式：$Cov(X,Y)=EXY-EX\cdot EY$

#### 性质

- $Cov(X,Y)=Cov(Y,X)$
- $DX=Cov(X,X)$
- $Cov(X,const)=0$
- $Cov(X+Y,Z)=Cov(X,Z)+Cov(Y,Z)$
  - $Cov(\sum c_iX_i,Y)=\sum c_i Cov(X_i,Y)$
- $Y_i=a_iX+b_i\rightarrow \rho_{Y_1Y_2}=\frac{a_1a_2}{|a_1a_2|}\rho_{X_1X_2}$ 
- $Y=aX+b\rightarrow \rho_{XY}=\pm1$
- $|\rho_{XY}|=1$ 的充要条件为 $X$ 与 $Y$ 以概率 $1$ 线性相关：
  存在常数 $a,b,a\ne0$ 使得 $P(Y=aX+b)=1$

#### 独立与不相关的关系

- **Def**（不相关）：若$\rho_{XY}=0$ （$Cov(X,Y)=0$） 则称 $X,Y$ 不相关。
- **Thm**：相互独立 则 不相关 （反之不一定成立）

*特殊的*：

1. 二维正态随机变量：相关$\iff$独立$\iff\rho=0$
2. $(0-1)$ 分布：相关$\iff$独立$\iff\rho=0$

### 协方差矩阵

#### 矩

**Def**（矩）若 $X,Y$ 为随机变量
1. $\alpha_k=EX^k$ 称为 $X$ 的 $k$ 阶原点矩

   $\alpha_1=EX$

2. $\beta_k=E(X-EX)^k$ 称为 $X$ 的 $k$ 阶中心矩

   $\beta_1=0,\quad\beta_2=DX$

3. $k,l\in N_+$ 则 $\gamma_{kl} = E(X-EX)^k(Y-EY)^l$ 称为 $X$ 与 $Y$ 的 $k+l$ 阶混合中心矩

   $\gamma_{11} = Cov(X,Y)$

#### 协方差矩阵

- **Def**（协方差矩阵）$\mathbf X=(X_1,X_2,\dots,X_n)^T$ 为 n 维随机向量
  1. $\mu=(\mu_1,\mu_2,\dots)^T$ 为随机向量 $X$ 的数学期望
  2. $\sigma^2=(\sigma_1^2, \sigma_2^2,\dots)^T$为随机向量 $X$ 的方差
  3. 协方差矩阵为：

$$
\varSigma=\left(\begin{matrix}
  \sigma_{11}& \sigma_{12}&\dots& \sigma_{1n}\\
  \sigma_{21}& \sigma_{22}&\dots& \sigma_{2n}\\
  \vdots&\vdots&\ddots&\vdots\\
  \sigma_{n1}& \sigma_{n2}&\dots& \sigma_{nn}\\
\end{matrix}\right)
$$

##### 性质

- $\mathbf{diag}\varSigma=\sigma^2$
- 半正定的对称阵，即$\varSigma\in S_+$
- $\sigma^2_{ij}\le \sigma_{ii}\sigma_{jj}$
- n 维正态分布：$f(\mathbb{x})=\frac{1}{(2\pi)^{n/2}|\sigma|^{1/2}}\exp\{-\frac{1}{2} (x-\mu)^T\Sigma^{-1}(x-\mu)\}$

{% noteblock quote %}

### Summary

#### 0 - 1 分布

1. 形式：$P(X=0)=1-p, P(X=1)=p$
2. 期望：$EX=p$
3. 方差：$DX=p(1-p)$

#### 二项分布 $b(n,p)$

1. 形式：$P(X=k) = C_n^kp^k(1-p)^k$
2. 期望：$EX=np$
3. 方差：$DX=np(1-p)$

#### 泊松分布 $P(\lambda)$

1. 形式：$P(X=k)=\frac{\lambda^k e^{-\lambda}}{k!}$
2. 期望：$EX=\lambda$
3. 方差：$DX=\lambda$

#### 超几何分布 $H(N,M,n)$ `-- not important`

1. 形式：$P(X=k)=\frac{C_M^kC_{N-M}^{N-k}}{C_N^n}$
2. 期望：$EX=nM/N$
3. 方差：$DX=\frac{nM(N-n)(N-M)}{N^2(N-1)}$

#### 均匀分布 $U(a,b)$

1. 形式：$P(X=x) = 1/(b-a)\quad if ~  ~ x \in [a,b]$
2. 期望：$EX=\frac{1}{2}(a+b)$
3. 方差：$DX=\frac{(b-a)^2}{12}$

#### 指数分布 $e(\lambda)$

1. 形式：$P(X=x)=\lambda e^{-\lambda x}$
2. 期望：$EX=1/\lambda$
3. 方差：$DX=1/\lambda^2$

#### 高斯分布（正态分布） $N(\mu,\sigma^2)$

1. 形式：$P(X=x)=\frac{1}{\sqrt{2\pi}\sigma}\exp[-\frac{(x-\mu)^2}{2\sigma^2}]$
2. 期望：$EX=\mu$
3. 方差：$DX=\sigma^2$

#### 卡方分布 $\chi^2(n)$

1. 形式（自由度为 n）：$\chi^2=\sum_{i=1}^nX_i^2,~X_i\sim N(0,1)$
2. 期望：$E\chi^2=n$
3. 方差：$E\chi^2=2n$

#### t-分布

1. 形式（自由度为 n）：$T=\frac{X}{\sqrt{Y/n}},~X\sim N(0,1),~Y\sim \chi^2(n)$

#### F-分布

1. 形式（自由度为 m, n）：$F=\frac{X/m}{Y/n},~X\sim \chi^2(m),~Y\sim\chi^2(n)$

{% endnoteblock %}

