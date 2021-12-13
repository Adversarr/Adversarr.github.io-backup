# 离散时间信号与系统

## 离散时间信号

### 常用序列

1. 单位脉冲序列 $\delta(n)$
2. 单位阶跃序列 $u(n)$
3. 矩形序列 $R_N(n)$
4. 实指数序列 $x(n) = a^nu(n)$
5. 正弦序列 $x(n) = \sin(n\omega_0)$
6. 复指数序列 $x(n) = r^n(\cos(\omega_0 n) + j\sin (\omega_0 n))$

### 离散周期序列

一般用
$$
\tilde x(n) = \tilde x(n+kN)
$$
来表示一个周期为 $N$ 的周期序列。

### 序列运算

1. 序列相加
2. 序列相乘
3. 序列的移位

序列的能量和序列的绝对值：

1. 序列能量定义为序列样本值的平方和
2. 平方可和序列
3. 绝对可和序列
4. 有界序列
5. 实序列的偶部和奇部
6. 任意序列的单位脉冲序列表示

$$
x(n) = \sum_{m = -\infty}^{\infty} x(m) \delta(n-m)
$$

## 离散时间信号的傅里叶变换和z变换

### DTFT

$$
X(e^{j\omega}) = DTFT[x(n)] = \sum_{n=-\infty}^\infty X(e^{j\omega})e^{jwn} \mathrm d \omega
$$

其中的 $\omega$ 是数字角频率，单位为 rad。其计算方法是：
$$
\omega = \frac{2 \pi f}{f_s}
$$
IDTFT的定义为：
$$
x(n) = \frac{1}{2\pi}\int_{-\pi} ^\pi X(e^{j\omega}) e^{j\omega n}\mathrm d\omega
$$

#### DTFT 的性质

1. 线性
2. 共轭性质
3. 移位
4. 频率移位
5. 奇偶部

## z变换

$$
X(z) = \sum_{n = -\infty} ^ \infty x(n) z ^ {-n}
$$

其中的z是一个复变量。ROC为一个环形带状区域。

### 求逆z变换

1. 长除法
2. 部分分式法
3. 留数法

### z 变换和 DTFT 的关系

$$

$$

## 离散时间系统

分类：

1. 线性系统
2. 时不变系统
3. 线性时不变系统
   1. 离散线性卷积的计算步骤
   2. 系统函数
   3. 稳定性 - 充要条件为单位脉冲响应绝对可和/Hz收敛域包含单位圆
   4. 差分方程描述

## 频率相应、系统函数

频率相应的定义：
$$
H(e^{j\omega}) = DTFT[h(n)] = \frac{Y(e^{j\omega})}{X(e^{j\omega})}
$$
频响和系统函数的关系：
$$
H(e^{j\omega}) = H(z)|_{z = \exp(j \omega)}
$$
IIR系统和FIR系统的定义

