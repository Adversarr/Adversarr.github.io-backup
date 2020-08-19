---
title: 振动与波
date: 2020-6-4
tags:
  - 物理
  - 波
categories: 基础物理学
math: true
---

基础物理学第六章-振动与波。后续会把其他这个学期学过的内容补上。

<!-- more -->

## 简谐振动

#### 描述简谐振动的特征量

- **Def**：简谐运动或简谐振动
- 描述简谐振动幅度和时间周期性的特征量
  - 振幅
  - 周期
  - 频率
  - 角频率
- **Def**：（相位）描述简谐振动瞬时运动状态的特征量

#### 简谐振动的合成

- 同方向、同频率的两个简谐振动的合成
  - 矢量图解法
    - $\tan \varphi_0 = \frac{A_1\sin\varphi_{10}+A_2\sin\varphi_{20}}{A_1\cos\varphi_{10}+A_2\cos\varphi_{20}}$
    - $A=\sqrt{A_1^2+A_2^2+2A_1A_2\cos (\varphi_{20}-\varphi_{10})}$
    - $x=A\cos (\omega t+\varphi_0)$
  - 复数法
    - $\displaystyle\tilde x = Ae^{i(\omega t+\varphi_0)}$
- 同方向、不同频率的两个简谐振动的合成
  - 形成**拍**现象
  - $x=2A\cos\frac{(\omega_2-\omega_1)t}{2}\cos\frac{(\omega_2+\omega_1)t}{2}$
- 相互垂直、同频率的两个简谐振动的合成
  - 圆、椭圆
  - 稳定的
- 相互垂直、不同频率的两个简谐振动的合成
  - 利萨如图形
  - 不稳定

#### 振动的分解 Fourier Transformation

- 周期函数的频谱分析和傅里叶级数
  - 傅里叶级数【高等数学】
- 非周期函数的频谱分析和傅里叶变换

## 弹性系统的振动

#### 谐振子的自由振动

- 固有频率、固有角频率
- 谐振子
- $-kx=m\frac{\mathrm d^2x}{\mathrm dt^2}$
- $\omega_0=\sqrt{k/m}=\sqrt{g/l}$
- $E=E_k+E_p=\frac 1 2 kA^2$

#### 谐振子的阻尼振动

- $\boldsymbol F_V=-\gamma\boldsymbol v$
- $2\delta = \gamma/m$ 是表征系统阻尼大小的 changliang
- 欠阻尼振动 $x=A_0e^{-\delta t}\cos(\omega t+\varphi_0)$
- 过阻尼振动 $\displaystyle x(t) = c_1e^{-(-\delta - \sqrt{\delta^2-\omega_0})t}+c_2e^{-(-\delta+ \sqrt{\delta^2-\omega_0})t}$
- 临界阻尼振动 $x(t) = (c_1+c_2)e^{-\delta t}$

#### 谐振子的受迫振动和共振

- 受迫振动的运动方程及其解的可叠加性
  - 受迫振动驱动力为 $F_d= F_{d0}\cos \omega_dt$
  - 受迫振动的解为$x(t) = A_0e^{-\delta t}\cos (\omega t+\varphi_0)+B\cos(\omega_dt+\varphi_d)$，其中第一项称为暂态解，第二项称为定态解
  - （复数法）定态解的振幅$\displaystyle B=|x|=\frac{\alpha}{\sqrt{(\omega_0^2-\omega_d^2)^2+4\delta^2\omega_d^2}}$
  - 定态解的相位$\displaystyle\varphi_d=\arctan\frac{-2\delta \omega_d}{\omega_0^2-\omega_d^2}$
- 共振
  - 当$\omega_d= \sqrt{\omega_0^2-2\delta^2}$ 受迫振动达到极大值

## 机械波的产生和传播

#### 简谐波的描述

- 横波、纵波
- 波速、波长、相速 $u=\frac \lambda T=v\lambda=\frac{\omega\lambda}{2\pi}$
- 振动位移表达式$\xi(x,t) = A\cos[\omega(t-\frac x u)+\varphi_0]$
- 角波数$k=\frac{2\pi}{\lambda},~~\xi(x,t) = A\cos[\omega t-kx+\varphi_0]$

{% note primary %}

**{% label info @「相位落后法」 %}**

{% endnote %}

#### 波动方程

- 波动方程
- 对应函数$\xi(x,t) = A\cos(\omega t-\boldsymbol k\cdot \boldsymbol x+\varphi_0)$

#### 波的能量

- $dV$上的动能 $dE_k=\frac 12 \rho\omega^2A^2\sin^2(\omega t-kx)dV$
- 势能 $dE_k=\frac 12 Ek^2A^2\sin^2(\omega t-kx)dV$
- 平均能量密度 $\overline w=\frac 1 T \int_0^T w\mathrm dt = \frac 1 2 \rho \omega^2A^2$

#### 声波

## 驻波

#### 驻波的形成和特点

- **Def**：（相干波）频率相同、振动方向相同、有固定相位差的两个波源发出的简谐波
- 干涉现象
- 驻波是特殊的干涉，两列波的振幅相同，传播方向相反
- 驻波方程 $y=A\cos(\omega t-kx)+A\cos (\omega t+kx)=2A\cos\frac{2\pi x}{\lambda}\cos \omega t$

#### 两端固定的弦中的驻波、多自由度系统的简正模

#### 半波损失

- 在均匀介质中沿直线传播的波在遇到另外一种介质时，会发生**反射**和**折射**现象，定义**特性阻抗** $Z=\rho u$
- 从波密介质到波疏介质中，相位不变，方向相反
- 从波疏介质到波密介质中，相位改变 $\pi$，方向相反，称为半波损失

## 多普勒效应

- 波源或观测者的运动造成观测频率与波源频率不同的现象

- 波源和观察者同时相对于介质运动时 $\displaystyle\nu'=\frac{u+v_o}{u-v_s}\nu$，其中 $v_o$ 为观察者向波源运动速度，$v_s$ 为波源向观察者运动的速度
