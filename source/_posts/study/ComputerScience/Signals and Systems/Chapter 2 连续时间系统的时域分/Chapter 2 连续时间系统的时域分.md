---
title: 连续时间系统的时域分析
date: 2021-6-13
categories: Course
tags:
  - 信号与系统
math: true
plugins:
  - mathjax
  - katex
group: group-signals-and-systems
sidebar: [group-signals-and-systems, toc]
---

信号与系统-连续时间系统的时域分析

<!-- more -->

# Chapter 2 连续时间系

## 引言

- 时域：变量为$t$→ 连续时间
- 模型：线性常系数微分方程组
- 求解：
	- 零输入（直接求解齐次方程；初态→等效源）
	- 零状态相应（间接法、叠加积分）

## 算子方程

### 算子定义

- **微分**算子$p=\frac{d}{dt}$
- **积分**算子$\frac 1 p = \int _{-\infty}^t (\cdot)d\tau$
- 电感和电容可以看作是**算子阻抗**：$pL,\displaystyle\frac 1{pC}$

### 算子运算法则

- 可以进行**代数运算**：如$(p+1)(p+2)=p^2+3p+2$
→[Chapter 3向量空间的线性映射](https://www.wolai.com/aKHL15uhaisjNYUwW5tKjk)
- 可以**消去**：在等式两端同时乘以$p$
- $pf=pg\Rightarrow f(t) =g(t) +\mathrm C$
	- 求**零输入**时，一般不能随便消去
	- 求**零状态**时，可以消去 → 线性完全满足的情况



- 例：一般的系统，有：$(p^n+a_{n-1}p^{n-1} + \cdots+a_0)r(t)=(b_mp^m+\cdots + b_0)e(t)$
	简记为：$D(p)r(t)=N(p)e(t)$ 
	或 $r(t)=\frac{N(p)}{D(p)}e(t)=H(p)e(t)$
	- $H(p)$ → **算子形式系统函数（转移算子）**
	- $D(p)$→ **特征多项式**（其根为**特征根**「自由频率、固有频率」→体现了系统响应的特征）

## 零输入相应的求法

> 转化为 $D(p)r(t)=0$ 的求解。


### 直接求解齐次方程

- 一阶系统
	→ 设 $\lambda$→ $(p-\lambda)r(t)=0$→ $r_{zi}(t)=ce^{\lambda t},c=r(0^-),t\ge 0$
- n 阶系统
	→ 令特征方程=0，求出特征根
	→ 通解为 $r_{zi}(t)=\sum_{i=1}^nC_ie^{\lambda_it}$
	→ 定解条件 $r(0^-),r'(0^-),r^{(n-1)}(0^-)$
	- 共轭根处理 → $e^t \cos t$
	- k重根的处理： $r_{zi}=(c_1+c_2t+\cdots+c_kt^{k-1})e^{\lambda_1t}+\cdots$

### 初态转化为等效源

`pass`

## 奇异函数

- 定义：一个本身或其微、积分在某处不连续的函数
- 单位阶跃函数：$\varepsilon(t)$
- 单位冲激函数：$\delta(t)$

### 单位冲激函数

1. 工程定义：
	$$
	\delta(t)=\begin{cases}\infty, &t=0 \\0,&t\ne 0\end{cases},\int _{-\infty}^\infty\delta(t)dt=1
	$$
	
2. 狄拉克定义：**抽样**性，**筛选**性
	$$
	\forall \varphi(t)在t=0连续,\int_{-\infty}^\infty\varphi(t)\delta(t)\mathrm dt =\varphi(0)
	$$
	
3. 数学定义：
	$$
	\delta (t)=\frac{\mathrm d}{\mathrm dt}\varepsilon(t)
	$$
	
4. 极限定义：
	$$
	\lim_{c\rightarrow 0}\int_{-\infty}^\infty f_c(t)\mathrm dt = \varphi(0)\rightarrow f_c(t)\rightarrow \delta(t)(c\rightarrow0)
	$$
	
5. 广义定义[广义傅立叶变换（广义谱）](https://www.wolai.com/v6uFU5Gko8cTJxuCQpMqip)

**常用性质**：

1. **抽样性**→[狄拉克定义：抽样性，筛选性](https://www.wolai.com/9tGv7bkJyWgLDSpqkudVoP)
2. **偶函数**$\delta(t)=\delta(-t)$
3. **尺度变换**性质：$\delta(at)=\frac 1{|a|}\delta(t),a\ne0$

**冲激偶**：$\delta'(t)$

## 信号的时域分解

### 例子

门函数

$$
G\tau(t)=\varepsilon(t+\frac \tau 2)-\varepsilon(t-\frac \tau 2)
$$


### 信号分解为$\delta(t)$的组合

若$f(t)$有始：

$$
\begin{aligned}f(t)&=\lim_{\Delta t\rightarrow 0}\sum_{k=0}^nf(k\Delta t)G_{\Delta t}(t-k\Delta t)\\&=\lim_{\Delta t\rightarrow 0}\sum_{k=0}^nf(k\Delta t)\frac{G_{\Delta t}(t-k\Delta t)}{\Delta t}\Delta t\\&=\int_0^tf(\tau)\delta(t-\tau)\mathrm d\tau\\&=f(t)*\delta(t)\end{aligned}
$$


### 信号分解为单位阶跃

$$
f(t) = \int_{-\infty}^tf'(\tau)\varepsilon(t-\tau)\mathrm d\tau=f'(t)*\varepsilon(t)
$$


## 冲激响应和阶跃响应

### H(t) 的求法

1. 拉氏反变换：$h(t)=L^{-1}H(s)$
2. $H(p)$分解法
3. 系数平衡法
4. 将$\delta (t)$的作用转化为$t=0^+$的初态，于是求$h(t)$就是求相应初态作用下的零输入相应$r_{zi}(t)$
5. 状态方程法（Ch9 TODO）

## 叠加积分

- $\varepsilon(t),\delta(t)$→`LTI`→$r_{\varepsilon}(t),h(t)$

$$
r_{zs}(t)=e(t)*h(t)
$$


1. $\tau$：冲激分量出现的时刻
2. $t$：观察的时刻
3. $t-\tau$：记忆时间
4. $r_{zs}(t)=\int_{-\infty}^\infty e(\tau)h(t-\tau)d\tau,-\infty<t<\infty$

## 卷积及其性质

### 定义

两个函数 $f_1(t)$ $f_2(t)$，则其卷积为：

$$
f_1(t)*f_2(t)=\int_{-\infty}^{\infty}f_1(\tau) f_2(t-\tau)\mathrm d\tau
$$


### 卷积图解

图解法求卷积

### 卷积的性质

1. 代数运算性质
	1. 交换律$f_1(t)*f_2(t)=f_2(t)*f_1(t)$→ 系统串联和子系统次序无关（理想情况下）
	2. 分配律$f_1(t)*(f_2(t)+f_3(t))=f_1(t)*f_2(t)+f_1(t)*f_3(t)$→ 系统并联等效
	3. 结合律$(f_1*f_2)*f_3=f_1*(f_2*f_3)$→ 系统串联等效
2. **微积分**性质
	1. 微分 $\frac d {dt}(f_1*f_2)=(\frac {d}{dt}f_1)*f_2=(\frac {d}{dt}f_2)*f_1$
	2. 积分 $\int_{-\infty}^t f_1(x)*f_2(x)\mathrm dx =[\int_{-\infty}^tf_1(x)\mathrm dx]*f_2(t)=[\int_{-\infty}^tf_2(x)\mathrm dx]*f_1(t)$
	3. 微积分综合 $f_1(t)*f_2(t)=\frac{\mathrm d}{\mathrm dx}f_1(t)*\int _{-\infty}^tf_2(x)\mathrm dx=\frac{\mathrm d}{\mathrm dx}f_2(t)*\int _{-\infty}^tf_1(x)\mathrm dx$
		注意被求导函数在 -∞ 必须为0
3. 延时性： $f_1(t)*f_2(t)=r(t)\rightarrow f_1(t-t_1)*f_2(t-t_2)=r(t-t_1-t_2)$
4. 与$\delta (t)$的卷积：$f(t)*\delta (t)=f(t)$
	1. $f(t)*\delta ^{(n)}(t) = f^{(n)}(t)*\delta(t)$
	2. $f(t)*(\int_{-\infty}^t)^n\delta (t) = (\int_{-\infty}^t)^nf(t)*\delta(t)$
	- $f(t)*\varepsilon(t)=\int_0^tf(\tau)\mathrm d\tau$
	- $\varepsilon(t)*\varepsilon(t)=t\varepsilon(t)$
5. 有限区间上的卷积：
	若$f_1(t):t\in(t_1,t_2),f_2(t):t\in(t_3,t_4)$则$y(t)=f_1(t)*f_2(t),t\in(t_1+t_3,t_2+t_4)$
6. **卷积定理**：
	$$
	f_1(t)*f_2(t)=\mathcal L^{-1}[F_1\cdot F_2]
	$$
	

## 线性时不变系统响应的求解

1. $r_{zi}$：特征方程→特征根
2. $r_{zs}(t)=e(t)*h(t)$



