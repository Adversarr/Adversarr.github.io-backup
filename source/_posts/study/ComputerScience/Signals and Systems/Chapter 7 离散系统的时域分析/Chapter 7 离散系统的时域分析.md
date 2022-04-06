---
title: 离散系统的时域分析
date: 2021-6-13
categories: 专业课
tags:
  - 信号与系统
math: true
plugins:
  - mathjax
  - katex
group: group-signals-and-systems
sidebar: [group-signals-and-systems, toc]
---


信号与系统- 离散系统的时域分析

<!-- more -->
# Chapter 7 离散系统的时域分析

重点：

1. 抽样定理
2. 零输入相应
3. 卷积和

## 引言-离散时间信号的描述

### 离散信号的描述

1. 定义：只在离散时刻 $t_k$ 才有定义 $f(t_k)$只讨论等间隔的情况
	1. 离散信号→时间离散
	2. 量化信号→幅度量化
	3. 数字信号→时间离散&幅度离散
2. 描述方式
	1. 闭式：写成时刻$t_k$的函数（等间隔的情况下，写成$k$的函数）
		例如：$f(k) = \frac 1 {2^k}$
	2. 数值序列：${1, .5, .25, ...}$
		→ 离散信号也被称为一个序列
	3. 时域波形

### 常用序列

1. 单位阶跃：
	$$
	\varepsilon(k)=\begin{cases} 1&k\ge 0\\0&k<0 \end{cases}
	$$
	
2. 单位（样值）函数：
	$$
	\delta(k)=\begin{cases} 1&k=0\\0&k\ne0 \end{cases}
	$$
	
	关系：
	1. $\delta(k) = \varepsilon(k) - \varepsilon(k-1)$一阶向后差分[Chapter 4 多项式插值和函数最佳逼近](https://www.wolai.com/8PKrK2QpGt2gcpE8jq38tb)
		
	2. $\varepsilon(k) = \delta(k) + \delta(k-1) + \delta(k-2)+\cdots$
3. （单边）指数序列
	$$
	\nu^k\varepsilon(k),\quad \nu\in R
	$$
	
	收敛、发散、等幅
4. 变幅正弦震荡：($\nu,\nu^*$是共轭根）
	$$
	(C\nu^k+C^*(v^*)^k)\varepsilon(k)= 2|C||\nu|^k\cos(k\varphi+\theta)
	$$
	

## 抽样定理

### 理想抽样

$$
\delta_T(t)=\sum_{n=-\infty}^{\infty} \delta(t-nT)\rightarrow f_s(t) = f(t)\delta_T(t)\\
F_S(j\omega) = \frac 1 {2\pi} F(j\omega) * \delta_{ws}(\omega)=\sum _{n=-\infty}^\infty F(j(\omega - n\omega_s))
$$


- 低频信号的抽样定理（带限信号，最高频率为$\omega_m$）
- 理想抽样
- 奈奎斯特抽样定理：
	当$\omega_s \ge 2 \omega_m$ 则$F_s$无混叠，可以完全恢复
- 内插公式：
	$$
	f(t) = \sum_{k=-\infty}^\infty f(kT)Sa\left[{\frac{(t-kT)\omega_s}{2}}\right]
	$$
	
- 工程上，若有效带宽为 $\omega_m$则一般取3-5倍频率采样
- 实际上可以采用开关函数（窄脉冲序列）
	→ **平顶抽样** $f(t)$→ 采样 → 保持 → 

## 离散时间系统的描述和模拟

|系统表示|连续|离散|
|---|---|---|
|IO|微分方程|差分方程|
|框图|三个基本单元|三个基本单元|
|系统函数|$H(s)$|$H(z)$|



LTI中：

1. 线性常系数微分方程
2. （也可以称为 线性移不变系统LSI）线性常系数差分方程

### 差分方程描述的离散系统

- Def（差分）[Chapter 4 多项式插值和函数最佳逼近](https://www.wolai.com/8PKrK2QpGt2gcpE8jq38tb) [差分和等距节点的Newton插值多项式](https://www.wolai.com/jGpcPho7C8HwPLjqMbJFko)
- $\Phi\{k,y(k),...,\Delta^ny(k),e(k),...,\Delta^n(k)\}=0$
- 定义移序算子 $S$， $S^i[y(k)]=y(k+i)$
	$$
	(S^n+a_{n-1} S^{n-1} + \cdots + a_0)y(k) = (b_mS^m + \cdots + b_0)e(k)
	$$
	
	简记为：
	$$
	D(S)y(k) = N(S)e(k)\\
	y(k) \mathop{=}\limits^\Delta  H(S)e(k)
	$$
	
	- 若 $\forall a_i=0$→ 非递归系统 → FIR有限冲激响应
	- 若 $\exist a_i\ne 0$→ 递归系统 → IIR 无限冲激响应

### 差分方程描述的LTI离散系统的框图模拟

1. 基本运算单元
	1. 加法器
	2. 标量乘法器
	3. 延时器
2. 框图
	引入中间变量 $q(k)$
	令 $D(S) q(k) = e(k)$ 则 $y(k) = N(S) q(k)$

## 离散系统的零输入响应

### $y_{zi}(k)$ 求法

1. 一阶系统：
	$$
	y(k+1)+a_0y(k) = 0
	$$
	
	$$
	\Rightarrow (S+a_0) y(k) = 0
	$$
	
	特征根为： $-a_0$
	零输入响应为： $y(k) = (-a)^ky(0)$
2. n 阶系统：
	根据特征多项式求出特征根，从而求出解：
	1. 特征根均为单根：
		$$
		y_{zi}(k) = \sum_i c_i\nu_i^k
		$$
		
	2. 有一个$l$重根：
		$$
		y_{zi}(k) = (c_1+c_2k+\cdots+c_lk^{l-1})\nu_1^k+\sum_{j = l+1} ^ n c_j \nu_j^k
		$$
		
		共轭根需要配对！

## 离散系统的零状态响应

### 时域卷和法

$$
e(k) = \sum_{j=-\infty}^\infty e(j) \delta(k-j)\mathop=\limits^\Delta e(k)*\delta(k)
$$


则：

$$
y_{zs}(k) = \sum_{j=-\infty}^\infty e(j ) h(k-j) = e(k) * h(k)
$$


### 卷积和的计算

图解法，长乘法（列表法），解析法，性质，Z变换

1. 解析法：针对无限长序列的卷积
	$$
	e(k) = a^k\varepsilon(k)\quad h(k) = b^k\varepsilon(k)\\
	\begin{aligned}
	
	a = b&\Rightarrow (k+1) a^k \varepsilon(k)\\
	a\ne b&\Rightarrow \frac {1}{b-a} [b^{k+1}- a^{k+1}]\varepsilon(k)
	\end{aligned} 
	$$
	

### 卷积和的性质

1. 代数运算：
	1. 交换律
	2. 结合律
	3. 分配律
2. 有限长序列卷积： $A(k)$ $B(k)$  项数为 $N_A,N_B$
	1. 项数为： $N_C=N_A+N_B$
	2. 上下限为：两个上下限之和
	3. $\sum C(j) = (\sum A(j))(\sum B(j))$ 
3. $e*\delta = e$
4. 延时： $y(k-n_1-n_2) = e(k-n_1) * h(k-n_2)$

### 求 h(k)

→ 求出 $H(S)$ 的部分分式分解，然后利用：

$$
\frac 1 {S-v}\leftrightarrow v^{k-1} \varepsilon(k-1)
$$




