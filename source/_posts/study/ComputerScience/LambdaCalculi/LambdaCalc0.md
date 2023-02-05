---
title: 编程语言和 Lambda 演算叙旧
date: 2020-6-9
tags:
  - 编程
  - Lambda演算
categories: Computer Science
mathjax: false
---

摘自Wikipedia，知乎等。

<!--more-->

## Lambda 演算历史

在 20 世纪 60 年代中期的一系列论文中，Landin[^1]阐述了关于编程语言的两个重要观察。首先，他认为所有编程语言都共享一套用于指定计算的基本工具，但在数据和数据原语的选择上存在差异。这组通用工具包含名称、过程、应用程序、异常机制、可变数据结构，以及其他形式的非局部控制（non-local control）。用于数值计算的应用程序的语言通常包括几种形式的数值常量和大型数值原语集，而用于字符串操作的语言通常提供高效的字符串匹配和操作原语。

其次，Landin 敦促程序员和实现者（implementors）都应该把编程语言看作是一种先进的、符号形式的算术和代数。由于我们在幼儿园和高中的时候就已经习惯了用数字、布尔值和更复杂的数据结构进行计算，用程序进行计算应该也很容易。程序评估、许多形式的程序编辑、程序转换和优化只是简单的、更复杂的计算形式。这种计算处理的不是简单的算术表达式，而是程序和程序片段。

Landin 定义了编程语言 `Iswim`。他设计的基础是 Church[^2] 的 Lambda 演算。Church 提出 Lambda 演算作为一种函数的演算（calculus of functions）。鉴于 Landin 对于在程序中，过程（Procedure）起到核心作用，并且作为所有语言的通用工具的理解，Lambda 演算是一个十分自然的构建起点（a nature starting point）。然而，为了支持基本数据和相关原语以及赋值和控制构造， Landin 使用适当的构造扩展了 Lambda 演算。他将扩展后的编程语言的语义与一台抽象机进行了类比，因为他不知道如何将 Lambda 演算理论扩展为完整的编程语言理论。实际上，（Landin 提出的）Lambda 演算甚至没有解释纯函数子语言的语义，因为 `Iswim` 总是对过程（Procedure）中的参数进行计算（意为执行该 Procedure 中的计算操作）。因此，Landin 并没有完成他的目标，即建立所有编程语言的一个理想的核心，并定义其语义的等式演算方法。

从 Plotkin[^3] 在 20 世纪 70 年代中期关于抽象机器与等式计算器的关系的研究开始，Landin 的研究未完成的部分由许多研究者共同填补，包括 Felleisen、Mason、Talcott 和他们的合作者。Plotkin 的工作包括创建一个实现了 `Iswim` 的基本功能的子语言，这需要在此基础上采用一种名为 Lambda 演算的“值代入”（call-by-value variant of the lambda-calculus）的计算方法。Felleisen 和他的同事用公理扩展了等式理论，这些公理解释了几种不同类型的命令式语言工具。梅森和塔尔科特研究了将等式理论用于完全类似 `Iswim` 的语言，作为程序验证和转换编程（Transformational Programming）的工具。

尽管 `Iswim` 并未成为一个被广泛应用的语言，`Iswim` 的设计哲学依旧体现在现代编程语言中，最值得注意的是 Scheme 和 ML，和它的语言（语义？）分析（langurage analysis）和设计方法基本上适用于所有编程语言。

这本书的目的是为了说明设计、分析和使用的等式理论像 Lambda 演算在编程语言内容（content of programming langurage）中的设计与分析。着眼于 ML 和 Scheme，但针对的是一般的高阶语言。

Landin 的 `ISWIM` 的功能核心是对 Church 的纯 Lambda 演算的扩展，使用原始数据及其相关的原始函数。Church 以一种函数的演算，提出了 Lambda 演算。Lambda 演算提供了一个简单且规范的语法来编写 donw 函数，以及一个简单的等式系统（指等式理论）来指定程序的行为。由于在编程语言中，由用户定义的过程是函数的直观对等物（intuitive counterpart of functions），所以对于希望仅基于数据和用户定义过程定义编程语言的 Landin 来说，该系统是一个自然的选择。与纯演算不同，`ISWIM` 包含基本常量和函数常量来模拟原始数据；为了避免特殊化（Specialization），我们的 `ISWIM` 变体包含用于原始数据操作的通用子语言。

[^1]: [Peter John Landin](https://www.wanweibaike.com/wiki-Peter J. Landin)
[^2]: [Alonzo Church](https://www.wanweibaike.com/wiki-Alonzo Church)
[^3]: [Gordon Plotkin](https://popl18.sigplan.org/profile/gordonplotkin)
