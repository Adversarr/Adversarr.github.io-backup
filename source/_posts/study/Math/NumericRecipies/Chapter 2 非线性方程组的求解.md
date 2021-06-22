---
layout: post
title: 数值分析-非线性方程求解
group: group-numeric-recipies
order: 2
categories: [数学]
tags:
  - 数值分析
sidebar: [group-numeric-recipies, toc]
---

数值分析 ch 2 - 非线性方程求解

<!-- more -->

# Chapter 2 非线性方程的求解

1. 一个自变量的非线性方程： $f(x)=0,\quad x\in R'$

2. [NO] 多个自变量的非线性方程组： $\vec F (\vec x) =\vec 0,\quad \vec x\in R^n,\vec F(\vec x)\in R^m$ 

---

Content：

1. 二分法

2. 简单迭代法

3. Newton迭代法

Idea：

$$
线性：f(x)=0\iff x=\varphi(x)\rightarrow x_{n+1}=\varphi(x_n)\\
非线性：x=\psi (x)\Rightarrow x_{n+1}:=\psi(x_n),x_n\rightarrow x^*
$$


重数：$f(x) = (x-x^*)^mg(x),g(x^*)\ne0$ 则m称为重数

一般分为如下2步：

1. 搜索根，分析方程存在多少个实根，每个根存在的区间

图解法、近似方程法、解析法、定步长搜索法

2. 精确化：求满足给定精度的根的近似值

从2项迭代导致的2阶方法。

## 二分法

## 简单迭代法

1. 局部收敛（$x_0$与精确解靠近）

2. 全局收敛（$x_0$未必与精确解靠近）

### 迭代格式的构造

通过方程 $f(x)=0$ 得到的等价形式： $x=\varphi(x)$，得到递推公式。

若根据 $x=\varphi(x)$ 得到的序列收敛， $\lim_{k\rightarrow\infty}x_k=x^*$。（当 $x^*=\varphi(x^*)$时，称为不动点，上述方法称为不动点迭代法）

序列是否收敛，由 $\varphi$和 $x_0$确定。

### 迭代的收敛性

**Thm**若 $\varphi(x)$在 $(a,b)$内有一阶连续导数，且满足，

  1. $x\in [a,b]$时， $\varphi(x)\in [a,b]$

  2. 存在正常数 $L<1$使得当 $x\in[a,b]$， $|\varphi'(x)|\le L <1$

则：

  1. $x=\varphi(x)$在 $[a,b]$上有实根 $x^*$

  2. 对于任意初值 $x_0\in [a,b]$，迭代收敛→**全局收敛**

同时满足：

$|x^*-x_k|\le \frac {L^k}{1-L} |x_1-x_0|$

**Thm** 方程在区间 $[a,b]$上有根，且当 $x\in [a,b]$时， $|\varphi'(x)|\ge 1$则对于任意 $x_0$迭代发散。

**Def**（**局部收敛**）方程 $x=\varphi(x)$，若在 $x^*$ 的某个邻域内，对于任意初值 $x_0\in S$，迭代都收敛，则称迭代法在 $x^*$附近局部收敛。

**Thm**：若方程 $x=\varphi(x)$有根 $x^*$，在某个邻域内一阶连续可导：

  1. $|\varphi'(x^*)|<1$→ 局部收敛

  2. $|\varphi'(x)|>1$→发散

## Newton 迭代法

### 迭代格式

> 基于 $f(x)=0$ 的近似形式 


$$
x_{k+1}=x_k-\frac{f(x_k)}{f'(x_k)}=\psi(x_k)
$$


如果需要计算二重根，Newton迭代法常常不能满足

### Newton 迭代法的收敛性

**Thm** 设函数 $f$在区间 $[a,b]$内二阶连续可导，且：

  1. $f(a)f(b)<0$

  2. 当$x\in[a,b]$时， $f'(x)\ne0$

  3. 当$x\in (a,b)$时， $f''(x)$保号

  4. $a-\frac{f(a)}{f'(a)}\le b,b-\frac{f(b)}{f'(b)}\ge a$ 

则其Newton迭代格式收敛到 $[a,b]$内的唯一实根。

### 重根的处理

若其是$m$重根，则修正为：

$$
x_{k+1}=x_k-m\frac{f(x_k)}{f'(x_k)}
$$


### Newton迭代的变形

1. Newton下山法：

$x_{k+1}=x_k-\lambda\frac{f(x_k)}{f'(x_k)}$

2. 割线法：

$x_{k+1} = x_k-\frac{f(x_k)}{f(x_k)-f(x_{k-1})}(x_k-x_{k-1})$

......ch2: 5 6 11 12 

