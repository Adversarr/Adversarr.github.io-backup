---
title: Lambda 演算简介（2）
tags:
  - 编程
  - Lambda演算
categories: 程序设计
mathjax: true
date: 2020-06-11
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

{% note info 演算提示 %}

不得不说，这个代数定义实在精彩，希望读者能拿纸笔算一算。在这里给出一定的提示

- `cons = lambda a.lambda d.(lambda s.s a d)` 一式中：

  - `a` 为 `car`（二元组的第一元素）
  - `d` 为 `cdr`（二元组的第二元素）
  - `s` 为 选择器（selector），注意 `true` 和 `false` 的定义。

  `cons` 实则返回的是一个选择器（也就是一个函数）。

- 请读者计算`empty? (cons e1 e2)` 和 `empty? empty`。

{% endnote %}

### 数

| 概念      | Lambda 表达式                  | 记法              |
| --------- | ------------------------------ | ----------------- |
| `0`       | $\mathrm{[empty]}$             | `[false]`         |
| `1`       | $\mathrm{[cons][true][false]}$ | `[true]`          |
| `add1 n`  | $\mathrm{[cons][true][}n]$     | `[cons][true][n]` |
| `sub1 n`  | $\mathrm{[cdr][n]}$            | `[cdr][n]`        |
| `zero? n` | $\mathrm{[empty?][}n]$         | `[empty?][n]`     |

需要注意的是，如果我们不用 `[true]` 和 `[false]` 表示 `0` 和 `1` ，而将其适当展开，我们可以得到这样的表达式：

- `[0] = lambda x y.y`
- `[n+1] = lambda x y.x [n]`

读者应该发现，在定义集合的势的时候，我们用了类似的处理方法：

> 一个自然数可以定义为集合：
>
> - $0=\emptyset$
> - 后继：$n^+=n\cup\{n\}$
>
> 一个有穷集的势定义为与其等势的一个自然数。

在定义这些运算之后，我们给出加法的定义：

| 概念      | Lambda 表达式                                                | 记法                                  |
| --------- | ------------------------------------------------------------ | ------------------------------------- |
| `add x y` | $\mathrm{\lambda x.\lambda y.\lambda s.\lambda z.(x~s~(y~s~z))}$ | `lambda x y.lambda s z.(x s (y s z))` |

以后在使用时，即可直接使用这些**概念**，进行演算。

## 简单类型的Lambda 演算

回顾前文中所有的Lambda 演算，我们发现，我们所有的演算，都是在Lambda 表达式中进行的，并没有脱开这些表达式，没有用到 `数` `布尔` 等常见的**类型**，在此引入这些概念：

类型化lambda演算的主要变化是增加了一个叫做「基类型」（base types）的概念。在类型化lambda演算中，你可以使用一些由原子值构成的论域（universe）， 这些值分为不同的简单类型。因此，例如，我们可以有一个类型 $N$，它由包含了自然数集合，也可以有一个类型 $B$，对应布尔值`true` / `false`，以及一个对应于字符串类型的类 $S$。

现在我们有了基本类型，接下来我们讨论函数的类型。函数将一种类型（参数的类型）的值映射到的第二种类型（返回值的类型）的值。对于一个接受类型A的输入参数，并且返回类型B的值的函数，我们将它的类型写为$A \rightarrow B$ 。$\rightarrow$叫做函数类型构造器（function type constructor），它是右关联的，所以 $A \rightarrow B \rightarrow C$ 表示 $A \rightarrow (B \rightarrow C)$。

TODO: 未完待续