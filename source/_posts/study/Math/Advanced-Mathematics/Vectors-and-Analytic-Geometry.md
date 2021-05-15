---
title: 向量空间与解析几何
author: Clover
date: 2020-5-22
tag:
  - 高等数学
  - 向量空间
  - 解析几何
categories: 数学
math: true
---

临近期末，来一波概念回顾。

<!--more-->

## 向量及其运算

### 向量的概念

- **Def**：（向量）一个既有大小又有方向的量
- **Def**：向量的模（或长度），范数 $|a|$，零向量 $\mathbf 0$，单位向量

### 向量的线性运算

- 向量的加法和减法
  - 交换律
  - 结合律
  - 存在幺元 $\mathbf 0$
  - 存在逆元 $- a$
  - （模的）三角不等式
- 向量的数乘

### 向量的数量积和数量积

- 向量在轴上的投影
  - **Def**：向量夹角
  - **Def**：（向量在轴上的投影） $(\vec{AB})_l = |\vec{AB}| \cos (\vec {AB}, l)$
- 向量的数量积
  - **Def**：数量积
  - **Thm**：数量积的性质
    - $ a \cdot  a = | a|^2$
    - $\cos ( a,  b) =\frac{ a \cdot  b}{| a|| b|}$
    - $ a \perp  b \Leftrightarrow  a \cdot  b = 0$
    - 交换律、数乘的结合律、分配律
- 向量的向量积
  - **Def**：向量积
  - **Thm**：向量积的性质
    - $ a \times  b =  0\Leftrightarrow  a \parallel  b$
    - 反交换律
    - 分配律
    - 数乘的结合律
- 向量的混合积
  - **Def**：（混合积）$[{abc}] =  a \cdot ( b \times  c)$
  - 几何意义：是以 ${a,b,c}$ 为相邻棱构成的平行六面体的体积
  - **Thm**：混合积的性质
    - $ a, b, c 共面 \Leftrightarrow [{abc}]=0$

## 空间直角坐标系及向量运算的坐标表示

### 空间直角坐标系

- 空间直角坐标系的建立：
  - **Def**：**坐标轴**、**坐标原点**、**坐标平面**、**卦限**
- 点的坐标：
  - **Def**：**横坐标**、**纵坐标**、**竖坐标**
- 坐标轴的平移

### 向量的坐标表示

- 向量的坐标
  - **Def**：基向量
  - **Def**：坐标表示式
- 向量的模和方向余弦
  - **Def**：$a$ 的方向角
  - **Def**：（$a$ 的方向余弦）$\cos \alpha = \frac x {| a|},\cos \beta = \frac y {| a|},\cos \gamma = \frac z {| a|}$

### 向量运算的坐标表示

- 向量加减法和数乘的坐标表示
- 数量积的坐标表示
- 向量积的坐标表示（行列式）
- 混合积的坐标表示

## 平面与直线

### 平面方程

1. 点法式方程
2. 一般方程
3. 截距式方程
4. 三点式方程

### 直线方程

1. 一般方程（两平面的交）
2. 标准方程
3. 两点式方程
4. 参数方程
5. 向量式方程

### 相关问题

{% note primary %}

**夹角**

1. 直线与直线
2. 直线与平面
3. 平面与平面

{% endnote %}


{% note secondary %}

**距离**

1. 点到平面
2. 点到直线 $\displaystyle d = \frac{|\vec{M_0M_1}\times a|}{|a|}$
3. 异面直线的距离 $\displaystyle d = \frac{|[\vec{M_0M_1}a_1a_2]|}{|a_1\times a_2|}$

{% endnote %}

**{% label info  @直线与平面的交点 %}**

**{% label success  @过直线的平面束 %}**

## 空间曲面和空间曲线

### 球面和柱面

1. 球面方程
2. 柱面方程

### 空间曲线

1. 一般方程（两个平面的交线）
2. 参数方程
3. **空间曲线在坐标面上的投影**

### 锥面

1. 母线、准线、顶点
2. 如何通过母线、准线、顶点构造

### 旋转曲面

如何构造？

### 几种常见的二次曲面

{% note info %}

![椭圆锥面](https://pic3.zhimg.com/80/v2-2f9167b3a6014ae1db97a646450038e7_720w.jpg)

![椭球面](https://picb.zhimg.com/80/v2-7fdb424b614f185fd9f5d94d8108297d_720w.jpg)

![单叶双曲面](https://pic2.zhimg.com/80/v2-1b4cebaa0cf266408ed391542339f705_720w.jpg)


![双叶双曲面](https://pic3.zhimg.com/80/v2-61bc076dab1f7eed8316381a5c65c721_720w.jpg)

![椭圆抛物面](https://pic2.zhimg.com/80/v2-70b021de8960867ee4b4e9c06dcac6cb_720w.jpg)

![双曲抛物面](https://pic4.zhimg.com/80/v2-b7c91cce5f10d1ac258a45ae8a204c8e_720w.jpg)

![椭圆柱面](https://pic1.zhimg.com/80/v2-b84d818035a2a3654f9937a4d664080d_720w.jpg)

![双曲柱面](https://pic4.zhimg.com/80/v2-cd0e151a5ccf836a6e9f1edb683b40d5_720w.jpg)

![抛物柱面](https://pic1.zhimg.com/80/v2-8f6a7089275ec0d89c28fa6a611a2175_720w.jpg)

{% endnote %}


