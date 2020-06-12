---
title: Lambda 演算（2）
tags:
  - 编程
  - Lambda演算
categories: 程序设计
mathjax: true
date: 2020-06-11 00:00:00
---


Lambda 演算中的常见概念

<!--more-->

## 布尔、函数、列表等基本数据类型

### 布尔值的表示与运算

| 概念           | Lambda 表达式                    | 记法                  |
| -------------- | -------------------------------- | --------------------- |
| `f(x) = expr`  | $\mathrm{\lambda x.expr}$        | `lambda x.expr`       |
| `true`         | $\mathrm{\lambda x.\lambda y.x}$ | `lambda x.lambda y.x` |
| `false`        | $\mathrm{\lambda x.\lambda y.y}$ | `lambda x.lambda y.y` |
| `e1 and e2`    | $\mathrm{[e1][e2][false]}$       | `[e1][e2][false]`     |
| `e1 or e2`     | $\mathrm{[e1][true][e2]}$        | `[e1][true][e2]`      |
| `not e1`       | $\mathrm{[e1][false][true]}$     | `[e1][false][true]`   |
| `(if q tp fp)` | $\mathrm{[q][tp][fp]}$           | `[q][tp][fp]`         |

毫无疑问，这是一个联结词完备集，现在来简单验证一下这个定义是正确的：

`true and false => (lambda x.lambday.y) = false`

当然，读者也可以尝试着写出 `not and or` 的表达式，证明其正确性。在此略去。

这样看 Lambda 表达式并不是很直观，但是如果认为这些 Lambda 表达式是柯里化后的表达式，则可以给出：

- `true <=> lambda x y.x`
- `false <=> lambda x y.y`
- `(if q tp fp) <=> lambda q tp fp.(q tp fp)`（注意结合 `true` 和 `false` 的定义看）

### 多元函数、列表的递归定义

| 概念              | Lambda 表达式                                          | 记法                                       |
| ----------------- | ------------------------------------------------------ | ------------------------------------------ |
| `f(x, y) = expr`  | $\mathrm{\lambda x.\lambda y.expr}$                    | `lambda x.lambda y.expr`（柯里化）         |
| `cons e1 e2`      | $\mathrm{\lambda a.\lambda b.(\lambda s.s~a~d)~e1~e2}$ | `lambda a.lambda d.(lambda s.s a d) e1 e2` |
| `car expr`        | $\mathrm{[expr][true]}$                                | `[expr] [true]`                            |
| `cdr expr`        | $\mathrm{[expr]~[false]}$                              | `[expr] [false]`                           |
| `empty`           | $\mathrm{\lambda x.[true]}$                            | `lambda x.[true]`                          |
| `empty? expr`     | $\mathrm{[expr](\lambda x.\lambda y.[false])}$         | `[expr](lambda x.lambda y.[false])`        |
| `(list e1 e2...)` | $\mathrm{[cons][e1][cons][e2]\dots[empty]}$            | `[cons][e1][cons][e2]...[empty]`           |

其中：

- `car cons e1 e2` $\mathop {\rightarrow}\limits^\beta$ `e1`
- `cdr cons e1 e2` $\mathop {\rightarrow}\limits^\beta$ `e2`

{% note info %}

#### 演算提示

不得不说，这个代数定义实在精彩，希望读者能拿纸笔算一算。在这里给出一定的提示

- `cons = lambda a.lambda d.(lambda s.s a d)` 一式中：

  - `a` 为 `car`（二元组的第一元素）
  - `d` 为 `cdr`（二元组的第二元素）
  - `s` 为 选择器（selector），注意 `true` 和 `false` 的定义。

  `cons` 实则返回的是一个选择器（也就是一个函数）。

- 请读者计算`empty? (cons e1 e2)` 和 `empty? empty`。

{% endnote %}
