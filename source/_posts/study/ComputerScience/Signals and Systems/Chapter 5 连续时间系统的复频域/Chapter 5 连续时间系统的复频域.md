---
title: 连续时间系统的复频域分析
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

信号与系统- 连续时间系统的复频域分析

<!-- more -->

# Chapter 5 连续时间系统的复频域分析

## Introduction

拉普拉斯变换Laplace Transform(LT)

重点：

1. 正反LT及其性质
2. LT求响应
3. 系统函数→框图

## 拉普拉斯变换

$$
F_d(s) = \int_{-\infty}^\infty f(t)e^{-st}\mathrm dt\\f(t) = \frac1{2\pi j}\int _{\sigma -j\infty}^{\sigma + j\infty}F_d(s)e^{st}\mathrm ds
$$


- $s$取值要在收敛域中（ROC）
- 收敛区不包含虚轴→LT存在而FT不存在。

对于有始信号： $f(t)=f(t)\varepsilon(t)\leftrightarrow F(s)$

$$
  F(s)=\int_{0^-}^{+\infty}f(t)e^{-st}\mathrm dt,\quad s\in ROC\\f(t)=\frac 1{2\pi j}\int_{\sigma-j\infty}^{\sigma+j\infty}F(s)e^{st}\mathrm ds\cdot \varepsilon (t)
$$


1. LT的含义：分解成无穷多个复指数分量的叠加
2. 复频率和单元信号$e^{st}$的关系
	1. $\sigma$决定了信号幅度比那花的快慢
	2. $\omega$决定了振荡的频率
	3. 一对共轭根变为变幅正弦振荡

## LT的收敛区

**Def**（指数阶）若$f(t)$仅有有限个极值点，$t\rightarrow \pm\infty$$f(t)$是$\sigma_0$指数阶的，即：

1. 对于有始信号 $\lim_{t\rightarrow\infty}f(t)e^{-\sigma t}=0$→$\sigma>\sigma_{0^+}$
2. 对于左边信号 $\lim_{t\rightarrow-\infty}f(t)e^{-\sigma t}=0$→$\sigma < \sigma_{0^-}$
3. 对于双边信号 $\lim_{t\rightarrow\pm\infty}f(t)e^{-\sigma t}=0$→$\sigma_{0^+}<\sigma < \sigma_{0^-}$

则其LT在以上区域（ROC）内收敛，称 $s=\sigma_0$是收敛轴。（ROC不包含边界）

### 分析

1. $f(t)=e^{\alpha t}\varepsilon(t)$→ $F(s)=\frac 1{s-\alpha}$, $Re[s]>Re[\alpha]$
	一个有始信号的ROC的收敛轴由最右边极点决定，ROC在收敛轴右侧。
2. 对于左边信号，其结论相反。如 $f(t)=e^{\beta t}\varepsilon(-t)\leftrightarrow F(s) = \frac{1}{s-\beta}$
	一个左边信号的ROC的收敛轴由最左边极点决定，ROC在收敛轴左侧。
3. 对于双边信号，一般是带状区域：如何通过极点图反求原信号（注意分析左右边信号）
	若 $\sigma_{0^-}\le \sigma_{0^+}$，双边LT不存在，例如： $\cos$和 $\sin$
4. **双边变换一定要标出ROC**，否则原信号不能判断
	$\varepsilon(t)\leftrightarrow \frac 1 s,\quad ROC:Re[s]>0$
	$-\varepsilon(-t)\leftrightarrow \frac 1 s,\quad ROC:Re[s]<0$
5. ROC内没有极点
6. 一般的信号为指数阶的有始信号
7. 对于有始信号而言，
	1. $\sigma_{0^+}<0$→ FT存在
	2. $\sigma_{0^+}>0$→ FT不存在
	3. $\sigma_{0^+}=0$，经典FT不存在，但广义FT存在：
		$$
		\sum\frac{k_i}{s-\lambda_i} \rightarrow \sum \pi k_i\delta(\omega-\omega_i)+k_i\frac{1}{-\alpha+j\omega}
		$$
		

## 常用LT

1. 指数类
	1. $e^{\alpha t}\varepsilon(t) \leftrightarrow 1 /(s-\alpha),\sigma>Re[\alpha],p_1=\alpha$
	2. $\displaystyle \cos(\omega_ct)\varepsilon(t)\leftrightarrow \frac{s}{s^2+\omega_c^2},\sigma >0,p_{1,2}=\pm j\omega_c$（单边，余弦）
		$\displaystyle \sin(\omega_ct)\varepsilon(t)\leftrightarrow \frac{\omega_c}{s^2+\omega_c^2},\sigma >0,p_{1,2}=\pm j\omega_c$（单边，正弦）
	3. $\displaystyle e^{\alpha t}\cos (\omega_c t)\varepsilon(t)\leftrightarrow \frac{s-\alpha}{(s-\alpha)^2+\omega_c^2},\sigma >Re[\alpha],p_{1,2}=\alpha \pm j\omega_c$
		$\displaystyle e^{\alpha t}\sin (\omega_c t)\varepsilon(t)\leftrightarrow \frac{\omega_c}{(s-\alpha)^2+\omega_c^2}, \sigma >Re[\alpha],p_{1,2}=\alpha \pm j\omega_c$
	4. $\ch \beta t,\sh\beta t$
2. t的正幂函数类
	1. $t^n\varepsilon(t)\leftrightarrow \frac{n!}{s^{n+1}},\sigma>0,p=0$
	2. $t^{nt}e^{\alpha t}\varepsilon(t)\leftrightarrow \frac{n!}{(s-\alpha)^{n+1}},\sigma>Re[\alpha],p=\alpha$
3. $\delta(t)$有关
	1. $\delta(t)\leftrightarrow1$
	2. $\delta^{(n)}(t)\leftrightarrow s^n$

## LT反变换

### 查表+性质

### 部分分式展开法

1. $m\ge n$$F(s)=$真分式+多项式
2. $m<n$$F(s)$真分式分解
	1. 单根：
		$$
		F(s) = \sum _{i=1}^n{K_i\over s-s_i} \leftrightarrow f(t) \sum_{i=1}^nK_ie^{-s_it}\varepsilon(t),\quad K_i=(s-s_i)F(s)|_{s=s_i}
		$$
		
	2. 重根：
		$$
		F(s) = {K_{11}\over (s-s_1)^l} + {K_{12}\over (s-s_1)^{l-1}}+\cdots
		$$
		

### 围线积分法（留数法）

$$
f(t) = \frac 1 {2\pi j} \int_{\sigma - j\infty}^{\sigma + j\infty} F(s) e^{st} \mathrm ds,\quad t > 0
$$


1. 留数定理：
	$$
	\oint G(s) \mathrm ds = 2\pi j\sum_i\mathrm{Res} [G(s_i)]
	$$
	
2. 约当引理：布洛维奇围道
	$\lim _{z\rightarrow \infty} g(z) = 0\Rightarrow \lim_{R\rightarrow \infty} \oint_{CR}g(z)e^{azi}\mathrm dz =0$
3. 围线积分法：对于有始信号：$f(t) = \sum \mathrm{Res} [F(s), s_i]$
4. 留数计算：
	1. $s=s_i$单根：$\mathrm {Res}[s_i] = (s-s_i)F(s) e^{st}|_{s=s_i}$
	2. $l$重根：$\mathrm{Res}= \frac 1 {(l-1)!}\frac{\mathrm d^{l-1} }{\mathrm ds^{l-1}}[(s-s_1)^lF(s)e^{st}]|_{s=s_i}$

## LT的主要性质

let $f(t)\varepsilon(t)\leftrightarrow F(s)\quad Re(s)\ge \sigma_0$

1. 线性性质
	$$
	a_1f_1(t)+a_2f_2(t)\leftrightarrow a_1F_1(s) + a_2F_2(s)
	$$
	
	收敛域一般来说是公共部分
2. 尺度变换
	$$
	f(at)\varepsilon(t)\quad a>0\leftrightarrow \frac 1 a F(\frac s a)\quad Re(s/a)>\sigma_0
	$$
	
3. 延时特性
	$$
	f(t-t_0)\varepsilon(t-t_0)\mathop{\leftrightarrow}F(s)e^{-st_0}
	$$
	
4. 频率平移
	$$
	\mathcal L\{f(t)e^{s_0t}\}=F(s-s_0)
	$$
	
5. 时域微分
	$$
	f'(t)\varepsilon(t)\leftrightarrow sF(s)-f(0^-)\\f^{(n)}(t)\varepsilon(t) \leftrightarrow s^nF(s)- s^{n-1} f(0^-)-s^{n-2}f'(0^-)-......s^0f^{(n-1)}(0^-)
	$$
	
6. 时域积分
	$$
	\left(\int_{-0^-}^tf(\tau)\mathrm d\tau \right) \varepsilon(t)\leftrightarrow F(s)/s
	$$
	
7. 复频域微积分
	$$
	(-t)f(t)\varepsilon(t)\leftrightarrow \frac{dF(s)}{ds}\\(-t)^nf(t)\varepsilon(t)\leftrightarrow \frac{d^nF(s)}{ds^n}
	$$
	
	$$
	{f(t)\over t}\varepsilon(t)\leftrightarrow \int_{s}^\infty F(x)\mathrm dx,\quad\mathrm{given}~\lim_{t\rightarrow 0}f(t)=0
	$$
	
8. 初值和终值定理
	已知 $F(s)$求 $f(0^+)$ 条件： $F(s)$ 是真分式，否则去除多项式部分
	$$
	f(0^+)=\lim_{s\rightarrow \infty}sF(s)
	$$
	
	求 $f(\infty)$条件： $f(t)$存在终值，即$F(s)$的极点都在左半开平面上，则有终值
	$$
	f(\infty)=\lim_{s\rightarrow 0}sF(s)
	$$
	
9. 卷积定理
	$$
	[f_1*f_2]\varepsilon(t)\leftrightarrow F_1(s)\cdot F_2(s)\quad ROC一般为公共部分
	$$
	
	$$
	f_1*f_2\leftrightarrow F_{1d}(s)\cdot F_{2d}(s)\quad ROC一般为公共区域
	$$
	

## LT分析法

### 求响应

1. 元器件→s域阻抗
2. 信号→象函数
3. 初态→等效源

### 由方程求响应

对于系统

$$
D(p)r(t) = N(p)e(t)
$$


有初态：

$$
r(0^-),r'(0^-)\cdots
$$


1. 直接求全响应：两边求LT，引入初态
	$$
	D(s)R(s)-P(s) = N(s) E(s)
	$$
	
	即：
	$$
	R(s) = \frac{P(s)}{D(s)} + \frac{N(s)}{D(s)}E(s)\leftrightarrow r(t)
	$$
	
2. 分别求零输入和零状态：
	零输入：$R_{zi}(s) = \frac {P(s)} {D(s)}\leftrightarrow r_{zi}(t)$
	零状态：$R_{zs}(s) =\frac{N(s)}{D(s)}E(s)$
3. LT求ZS的含义：
	e(t)→ZS→r(t)
	$e^{st}\rightarrow H(s) e^{st}$
4. 系统函数$H(s)$
	$H(s) =R(s)/E(S)\quad ZS$
	1. 由I/O方程求解
	2. 由电路：$H(s) = H(p)$
	3. 由响应分解：$H(s) = \mathcal L\{r_{zs}(t)\}/\mathcal L\{e(t)\}$
	4. 由框图/流图求
	5. 由状态方程求
	$H(s) = \mathcal L \{h(t)\}$（包括双边变换）
	$H(s) = \frac{e^{st}作用下的响应}{e^{st}}$

## 双边LT

### 双边LT

1. 正变换
	对于一个双边信号，可以分解为
	$$
	  f(t)=f(t)\varepsilon(-t)+f(t)\varepsilon(t)=f_l(t)+f_r(t)\\
	\Rightarrow F_d(s) = F_{dl} (s) + F_{dr} (s),\sigma_1< \sigma < \sigma_2
	$$
	
	- 对于$F_{dr}(s) = \int _{0^-}^\infty f_r(t)e^{-st}\mathrm dt = F_r(s),\sigma >\sigma _ 1$
	- 对于$F_{dl}(s) = F_l(-s) =\int_{0}^\infty f_l(-t)e^{-st}\mathrm dt, \sigma <\sigma_2$
2. 反变换
	根据ROC分解$F_d(s) $，$f=f_l+f_r$

### 双边LT的零状态响应

$$
R_{zs}(s) = E_d(s) H_d(s)
$$


## 线性系统的（框图）模拟

系统表示法：四种

对于单输入单输出系统：

1. IO方程：$D(p)r(t) = N(p) e(t)$
2. 系统函数：$H(s) = \frac{N(s)}{D(s)}$
3. 框图/流图：

对于多输入多输出系统：

1. 状态方程

### 框图模拟的基本运算单元

用基本运算构成：

1. 加法（加法器）
	用圆形符号（中间为$\Sigma$）
	1. 时域上：$y = x_1+x_2$
	2. $s$域上：$Y= X_1 + X_2$
2. 数乘（标量乘法器）
	方框
3. 积分
	方框，中间为 $\int$或 $1/s$，注意初始条件（在积分器后面紧接一个加法器，定义初态）

### 线性系统的框图

1. 一阶系统：
	$$
	y'(t) + a_0 y(t) = x(t) \Rightarrow y'(t) = x(t) - a_0 y(t)
	$$
	
	→ 反馈支路
2. 二阶系统：
	找到最高阶导数项，假设为加法器输出，然后依次构造各次导数作为反馈
3. n阶系统：（全奇点）
4. 一般的n阶系统：（$m\le n$）
	$$
	y^{(n)} + a_{n-1}y ^{(n-1)} + \cdots + a_0 y = x^{(m)} + b_{m-1} + \cdots + b_0 x
	$$
	
	添加前向部分。

### 框图的形式

1. $H(s) = \prod_i H_i(s)$串联
2. $H(s) = \sum_i H_i(s)$并联
	> 共轭根转化为二次实系数多项式
	
3. 混联（非标准连接）



