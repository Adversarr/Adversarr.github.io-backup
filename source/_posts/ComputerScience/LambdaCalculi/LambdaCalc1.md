---
title: Lambda 演算简介（1）
date: 2020-6-9
tags:
  - 编程
  - Lambda演算
categories: 程序设计
math: true
---

摘自 Wikipedia，知乎等。

<!-- more -->

## 何为 Lambda 演算

Lambda 演算（Lambda Calculus）是一套从数理逻辑中发展，以变量绑定和替换的规则，来研究函数如何抽象化定义、函数如何被应用，以及以递归的形式定义、实现一个系统。它由数学家阿隆佐·邱奇在 20 世纪 30 年代首次发表。Lambda 演算作为一种广泛用途的计算模型，可以清晰地定义什么是一个可计算函数，而任何可计算函数都能以这种形式表达和求值，它能模拟单一磁带图灵机的计算过程；尽管如此，Lambda 演算强调的是变换规则的运用，而非实现它们的具体机器。

Lambda 演算可比拟是最根本的编程语言，它包括了一条变换规则（变量替换）和一条将函数抽象化定义的方式。因此普遍公认是一种更接近软件而非硬件的方式。对函数式编程语言造成很大影响，比如`Lisp`、`ML`语言和`Haskell`语言。在 1936 年邱奇利用 Lambda 演算给出了对于判定性问题（Entscheidungs problem）的否定：关于两个 Lambda 表达式是否等价的命题，无法由一个“通用的算法”判断，这是不可判定性能够证明的头一个问题，甚至还在停机问题之先。

{% note info %}

### 后文中使用的一些 Racket 语义

$\sum\limits_{i=0}^ni$：`(define (sumto n) (/ (* n (+ n 1)) 2))`

求整数的位数：`(define (crunch n) (if (< n 10) 1 (+ 1 (crunch (/ n 10)))))`

断言：`posn?`，`number?`，`zero?`，`positive?`...

多分支判断：`cond`相当于 c 中的 `switch-case` 语句（等价 `(if p a1 a2)` 递归）

#### 复杂数据类型

复杂数据类型构成：`make-posn p q`，`posn?`，`posn-x`，`posn-y`

元组化：`(define (bunchify n) (if (= n 1) 1 (make-posn n (bunchify (- n 1))))))`

元组个数：`bunch-size`

```racket
(define (bunch-size b)
  (if (number? b)
  1
  (+ (bunch-size (posn-x b)) (bunch-size (posn-y b)))))
```

从 `bunch` 中删除 `e`：`delete-es b e`

#### 高级数据结构

二元组：`cons` （`(define-struct cons (car cdr))`）

取第一个：`car`

取第二个：`cdr`

列表：`list`

{% endnote %}

## 计算模型（Computation Models）

图灵机是一种**抽象机器**，它在无限长磁带上进行计算。如果一个问题可以用图灵机解决，我们说它是**可计算的**。否则，它是**不可计算的**。

{% note info %}

### 停机问题

不可计算的一个例子：**停机问题**。它询问是否存在一个程序，该程序接受一个程序作为输入，并决定它是否停止。现在思考这样的 Racket 函数：

```racket
(define (doesnthalt x) (doesnthalt x))

(define (foo x)
  (if (halts? x) (doesnthalt 10) true))
```

这里的 `doesnthalt` 函数形成无穷递归。

进而我们证明 `(foo foo)` 是不可确定的

> 1. 如果 `(foo foo)` 停机，则 `foo` 停机，则`(foo foo) => (doesnthalt 10)`
>
>    `(foo foo)` 是不可计算的，形成矛盾。
>
> 2. 如果 `(foo foo)` 不停机，则 `(foo foo) => true` ，`foo` 停机，形成矛盾。
>
> 在两种情况下，都产生了矛盾，故停机问题是不可计算的。

{% endnote %}

## Lambda 演算语法

Lambda 演算包括了建构 Lambda 项，和对 Lambda 项运行归约的操作。Lambda 演算只有三类表达式：

1. 变量（Variable）：$\mathrm{x,y,a,b}$
2. 抽象（Abstraction）：$\mathrm{(\lambda x.~expression)}$ $\mathrm{expression}$ 是一个 Lambda 表达式
3. 应用（Application）：$\mathrm{(e_1,e_2)}$ 其中 $e_1,e_2$ 为 Lambda 表达式

{% note info %}

### 常用表示法

$\mathrm{(\lambda x . expression)}$：`(lambda x. expression)`

$\mathrm{(\lambda x.plus~x~x)~y}$：`(lambda x. plus x x) y`（前缀表达式）

在后文中都使用这种记法，并且采用前缀表达式。下面介绍一些速记：

| 表达式                   | 等价记法               |
| ------------------------ | ---------------------- |
| `(lambda x. expression)` | `lambda x. expression` |
| `(e)`                    | `e`                    |
| `e1 e2 e3`               | `(e1 e2) e3`           |
| `lambda x.e1 e2`         | `lambda x. (e1 e2)`    |

这里给出一些 Lambda 表达式的例子：

1. `x`
2. `x x`
3. `x y z`
4. `lambda x. x`
5. `lambda x. x x`
6. `lambda x.(lambda y. x)`
7. `(lambda x. x) (lambda y. y)`

### Lambda 演算技巧：柯里化

如果仔细看 Lambda 演算的定义，便会发现，Lambda 演算只接受一个参数，这似乎是一个极大的问题，因为我们连加法都无法合理的处理，因而我们将其使用柯里化。

柯里化（Currying）是把接受多个参数的函数变换成接受一个单一参数(最初函数的第一个参数)的函数，并且返回接受余下的参数且返回结果的新函数的技术。在直觉上，柯里化声称：

{% note info %} “如果你固定某些参数，你将得到接受余下参数的一个函数”{% endnote %}

由这个理论，我们来构建一个加法运算：`lambda x.(lambda y. plus x y)`

如果我们可以简化运算、并且提升可阅读性的话，我们也可以用前一种记法，即 `lambda x y. plus x y`。这就是柯里化的最简单使用方法，也就是说，一个复杂的多参数函数可以柯里化为一个函数。添加多个参数的函数并没有真正添加任何东西，只不过简化了语法，所以下面继续介绍的时候，在方便的时候用到多参数函数。

{% endnote %}

### 自由变量

我们在此给出自由变量的严格定义：

> 用 $\mathrm{FV[exp]}$ 表示一个集合，表示在一个 Lambda 表达式 $\mathrm{exp}$ 中的所有自由变量：
>
> 1. $\mathrm{exp}$ 是变量，则 $\mathrm{FV(exp) = \{exp\}}$
> 2. $\mathrm{exp}$ 是应用 $\mathrm{(e1~e2)}$，则 $\mathrm{FV(exp) = FV[e1]\cup FV[e2]}$
> 3. $\mathrm{exp}$ 是抽象 $\lambda \mathrm{x.~deri}$，则 $\mathrm{FV(exp) = FV(deri) \backslash \{x\}}$

例如：

- `lambda x . plus x y`：在这个表达式中，`y` 和 `plus` 是自由的，而 `x` 不是自由的。
- `lambda x y . y x`：在这个表达式中`x`和`y`都不是自由的。
- `lambda y . (lambda x . plus x y)`：在内层演算`lambda x . plus x y`中，`y`和`plus`是自由的，`x`不是自由的。在完整表达中，`x`和`y`不是自由的，`plus` 是自由的

我们会经常使用`free(x)`来表示在表达式`x`中自由的标识符。

## Lambda 演算中的代换法

$\mathrm{e1[x\leftarrow e2]}$ 表示代换。代换可以不严谨地理解为：将 $\mathrm{e1}$ 中的所有出现的**自由变量** $\mathrm x$ 替换为 $\mathrm{e2}$。

严格的定义如下：

1. $\mathrm{x[x\leftarrow e]}\Longrightarrow\mathrm e$
2. $\mathrm{(e1,e2)[x\leftarrow e3]}\Longrightarrow \mathrm{(e1[x\leftarrow e3],e2[x\leftarrow e3])}$
3. $\mathrm{(\lambda x.e1)[x\leftarrow e2]}\Longrightarrow \mathrm{(\lambda x.e1)}$ （在其中，$\mathrm x$ 不是自由变量）
4. $\mathrm{(\lambda y.e1)[x\leftarrow e2]}\Longrightarrow \mathrm{(\lambda y.e1[x\leftarrow e2])}$

### Lambda 演算原则

为了推广这个代换法，我们引入 $\alpha$-转化和 $\beta$-规约的概念：

#### alpha-转化

如果两个 Lambda 表达式$(\mathrm{\lambda x.e1}),(\mathrm{\lambda y.e2})$满足$\mathrm y\not\in\mathrm{FV[e1]}$ 并且 $\mathrm{e2=e1[x\leftarrow y]}$ 则称这两个表达式是 $\alpha$-等价（$\alpha$-equivalent）的。用符号 $\mathop{\rightarrow}\limits^\alpha$ 表示这一转化。

> $\alpha$-转化翻译成 **转化** 一词，是因为其注重了其转化的语义。
>
> 在英文中我们使用：_equivalent_ 表示该关系，实则描述的是一种等价关系。

#### beta-规约

$\beta$-规约是一个操作：将$\mathrm{(\lambda x.e1)~e2}$，转化为 $\mathrm{e1[x\leftarrow e2]}$。用符号 $\mathop {\rightarrow}\limits^\beta$ 表示这一操作。

> 规约来自：_reduction_ 一词，个人认为翻译为 **约化** 更为准确。

{% note info %}

#### alpha-转化和 beta-规约的实例

$$
\begin{aligned}
\mathrm{(\lambda x.a~x~b)~(\lambda y.y)}&\mathop {\rightarrow}\limits^\beta\mathrm{a~(\lambda y.y)~b}\\
\mathrm{(\lambda x.a~x~b)~(\lambda y.x)}&\mathop {\rightarrow}\limits^\alpha\mathrm{(\lambda q.a~q~b)~(\lambda y.x)}\\
&\mathop{\rightarrow}\limits^\beta \mathrm{a~(\lambda y.x)~b}
\end{aligned}
$$

{% endnote %}

#### 约化

若给出一个从 $\mathrm {e1}$ 到 $\mathrm{e2}$ 演算序列，且 $\mathrm e2$ 无法继续演算，则称 $\mathrm e1$ 约化为 $\mathrm{e2}$。

如果一个表达式 $\mathrm e1$ 存在一个约化，则称其为**可约化的**（called redex）

### 开始我们的演算

以 $\mathrm{(\lambda x.a~x~b)~((\lambda y.y)~z)}$ 为例，下面给出两种可能的方案去约化 Lambda 表达式。

**普通（惯常）顺序（Normal Order）**：从最外层的可约化的式子开始，先化为$\mathrm{a~((\lambda y.y)~z)~b}$

**应用（调用）顺序（Applicative Order）**：也从最外层开始，但先化为 $\mathrm{(\lambda x.a~x~b)~z}$

> 请读者指出这两种顺序的区别：（注：在 non-lazy 非惰性计算时使用的是第二种顺序）

一个**完全约化**（fully-reduced）的 Lambda 表达式形式没有可约化的表达式。同时，若给出从 $\mathrm {e1}$ 到 $\mathrm{e2}$ 演算序列，则 $\mathrm e2$ 不可约化，且在该演算序列中的所有表达式都约化为 $\mathrm e2$（存在且唯一）。

{% note warning 一个无穷递归的例子 %}

$\mathrm{(\lambda x.x~x)~(\lambda x.x~x)}$

毫不夸张的说，这是世界上最小的无穷循环（递归）。

但是，思考这样的例子：

$\mathrm{(\lambda x.y)~((\lambda x.x~x)~(\lambda x.x~x))}$

对于普通顺序演算，结果为 $y$ ，对于应用顺序演算，结果则是无穷递归。

更一般的说，若一个 Lambda 表达式可以（可能）被约化为一个完全约化的表达式，则普通顺序**一定**能演算到该形式，但应用顺序可能无法导出答案。

{% endnote %}

## 惰性计算（Lazy-Evaluation）

惰性计算需要我们对可约化的表达式进行注释（annotate）。以下面一个表达式为例，我们对表达式进行约化：

$$
\mathrm{(\lambda x.f~x~x)~((\lambda y.y)~z)}
$$

使用**普通顺序**：

$$
\begin{aligned}
&\mathrm{(\lambda x.f~x~x)~((\lambda y.y)~z)}\\
\Rightarrow&\mathrm{f~((\lambda y.y)~z)~((\lambda y.y)~z)}\\
\Rightarrow&\mathrm{f~z~((\lambda y.y)~z)}\\
\Rightarrow&\mathrm{f~z~z}
\end{aligned}
$$

**普通顺序**先对第一个抽象（abstraction）使用 $\beta$-规约

使用**应用顺序**：

$$
\begin{aligned}
&\mathrm{(\lambda x.f~x~x)~((\lambda y.y)~z)}\\
\Rightarrow&\mathrm{(\lambda x.f~x~x)~z}\\
\Rightarrow&\mathrm{f~z~z}
\end{aligned}
$$

**应用顺序**先对第二个抽象（abstraction）使用 $\beta$-规约

使用**惰性计算**：

$$
\begin{aligned}
&\mathrm{(\lambda x.f~x~x)~((\lambda y.y)~z)}\\
\Rightarrow&\mathrm{f~((\lambda y.y)~z)~((\lambda y.y)~z)}\\
\Rightarrow&\mathrm{f~z~z}
\end{aligned}
$$

看似惰性计算很像普通顺序，但是，除了在后台运算时，所有等价的可约化表达式，在约化后会同时被替换。
