---
title: Lambda 演算简介（3）
tags:
  - 编程
  - Lambda演算
categories: 程序设计
math: true
date: 2020-06-11
---

Lambda 演算中的 Y 组合子

<!--more-->

## Y 组合子：递归实现

在之前，我们都在做一些简单的操作，例如实现了分支结构 `s e1 e2` ，现在我们要考虑如何实现第二种结构：循环与递归（recursion）。

在 Lambda 演算的世界里，递归是容易实现的，利用如下的 Y 组合子：

`Y = lambda y.(lambda x.y (x x)) (lambda x.y (x x))`

即：$\mathrm{Y = \lambda y.(\lambda x.y~(x~x))~(\lambda x.y~(x~x))}$

我们试着计算 `Y Y` 的值：

```racket
         Y Y
(beta) =>(lambda x.Y (x x)) (lambda x.Y (x x))
(alpha)=>(lambda x.Y (x x)) (lambda z.Y (z z))
(beta) =>Y ((lambda z.Y (z z)) (lambda z.Y (z z)))
(alpha)=>(lambda a. (lambda b . a (b b)) (lambda b. a (b b)))
         ((lambda z. Y (z z)) (lambda z. Y (z z)))
(beta) =>Y (Y Y)
...... =>Y (Y (Y Y))
......
```

可以发现，Y 组合子通过 `Y Y` 创造了自身！这似乎是一个无穷递归，我们换一个例子看一看：假定 `f` 是一个关于 `x` 的函数，例如`f = (lambda x.add1 x)`

```racket
         (Y f) x
(beta) =>(lambda y.(y (lambda x.y (x x) lambda x.y(x x))) f) x
(alpha)=>(f ((lambda x.f (x x)) (lambda x.f (x x)))) x
(beta) <=(f (Y f)) x
...... <=(f (f ( ... f(Y f))...) x
```

这还不够，因为 `f` 是一个一元的函数，按照这个形式，即使给 `f` 一定的条件，使之在某处停下，我们也无法使之**停下的条件**与任何一个 `x` 有关。就以上面的表达式为例：

`(Y f) => add1 (add1 (add1 ... )) x` 内部的 `add1` 并不会停下！

例如：`f (f (f)) x` 在这里，前面是先演算的内容，但是很明显在第三层停下递归并不是 `x` 所控制的。这并不是我们想要的，但是已经十分接近了！给这个形式做一些改变，则需要一个形式保留下来这个结构，并且将 `add1` 换为一个二元运算 `mult`：

```racket
         (Y (lambda t.lambda x.mult x (t x)))) a
...... =>(lambda t.lambda x.mult x (t x) (Y lambda t.lambda x.mult(t x)) x) a
(alpha)=>(lambda t.lambda x'.mult x' (t x') (Y lambda t.lambda x.mult(t x)) x) a
(beta) =>(lambda x'. mult x' (Y (lambda t.lambda x.mult x (t x))) x)) a
(beta) =>mult a (Y (lambda t.lambda x.mult x (t x))) a)
...... =>mult a (mult a (mult a ( ... )))
```

最后我们加上一些判断，使之在某个地方停下，以及对于 `x` 的变换：

```racket
LET: metafact = lambda fact . (lambda n . IsZero n 1 (Mult n (fact (Pred n))))

   metafact (Y metafact) n
=> lambda n. zero? n 1 (mult n (Y metafact (Pred n))) n
=> mult n (Y metafact (Pred n))
=> mult n (metafact ((lambda x.metafact (x x)) (lambda x.metafact (x x))) (Pred n))
=> mult n (metafact (Y metafact) (Pred n))
```

{% note primary %}

**一点思考**

读者应分析结构：`lambda t.lambda x.f (t x) x `，指出其中 `f` 和 `t` 的作用：（在此仅给出个人的理解）

- `f` 为函数算子
- `t` 为传入形式的复制

如果从柯里化的角度看 Y 组合子是否更好？

{% endnote %}

## SKI组合子

先给出 SKI 组合子的定义：

- `S = (lambda x y z.(x z (y z)))` 
- `K = (lambda x y. x)`
- `I = (lambda x.x)`

这个定义时很奇怪的，如何说呢，请看：

```racket
  S K K x
=>(K x) (K x)
=>(lambda x y. x) x (K x)
=>x
```

也就是说 `I = S K K`，其中 `=` 表示**外延等价**（extensional equivalence），当 `E x` 和 `E' x` **总是**有相同的约化结果恒成立，则称 `E = E'`。（另一种等价指**内涵等价**（intensional equivalence），当`E` 与 `E` 完全相同或经过 $\alpha$-转换后有相同的结果）。

> 在此略去 **组合子演算** 部分，这一部分可以参考[这篇文章](http://cgnail.github.io/academic/lambda-5/)

