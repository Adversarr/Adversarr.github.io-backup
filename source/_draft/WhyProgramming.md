---
title: Programming
hide: true
---

占坑

<!-- more -->

## 为什么要研究语言

很多时候，我们会在网络上看到一些没有意义的问题：

> Q: 什么是世界上最好的语言？

{% folding anwser %}

肯定不是php。

{% endfolding %}

这类问题是怎么产生的呢？我们日常开发中经常见到的一个场景是：

{% noteblock::Why???? %}

1. 写 C++：
   1. 为什么这个文件无法通过编译！
   2. 为什么别人的代码无法在我的机器上运行！
   3. 为什么别人的代码和我学过的完全不是一个东西！
   4. xxxx……
2. 写 Python：
   1. 为什么这个变量传递进去就是错的！
   2. 为什么没有自动补全
   3. 为什么这么慢！
   4. 这是个什么神奇的语法？
   5. 为什么这个变量不变/变了！！！
3. 写函数式：
   1. 为什么我要写/学这个东西？！
4. 写 Java / C#：
   1. 为什么能够有人不用ide就开发！
5. 写 Swift：
   1. 为什么这个语法如此的丑陋！

{% endnoteblock %}

诸如此类，这些乱七八糟问题都会促使工程师们（码农们）去想要用别的语言来处理当前/原有的业务。

回到最开始的那个问题，为什么人们会孜孜不倦的讨论世界上最好的语言这个问题？实际上问题在于，对于一个极其复杂的业务，一种编程语言，或者说一种编程范式，其始终无法满足需求。而当一个新的语言，在当前的业务逻辑上，相交于之前的语言的实现上更加简单且高效的时候，程序员一定会破口大骂，为什么自己没有早点发现/学习这个语言。

> 最经典的场景莫过于绝大多数的同学，在大二开始接触Python/Java的时候，疯狂抱怨自己为什么要学习 C/C++，为什么学校还要墨守陈规得继续教授C++。

从上面的问题中，我们不难看到几个关键词：

1. 编程范式：什么是面向对象/数据/过程/函数式
2. 效率：简单、高效的实现/程序加速

这些东西我们分开来一个个谈吧。

### 到底程序是个啥

> 程序 = 方法 + 数据
>
> （一般在设计 Class 的时候，人们更倾向于把成员函数称为一个`方法`，而对于一些其他的函数，我们就叫做`函数`。 Anyway，如果你和我一样只是把函数和方法都看作数据上的操作的话，实际上也没有必要特别区分方法和函数，因此在我考虑问题、设计程序算法的时候，我通常不区分`方法`和`函数`）


这几乎就是我们进行所谓的**程序设计**的一个起点！很大程度上，我在程序设计的起点，我需要搞明白的很少的一些东西：

1. 这个程序的输入是什么
2. 这个程序的输出是什么
3. 这个程序会对外部（例如操作系统状态）产生什么影响

举一些🌰：

1. 一个矩阵乘法程序，就是拿到两个矩阵的数据，对它们进行矩阵乘法这个方法，然后吐出来一个矩阵
2. 一个计算器，就是监听用户的输入，并记录下来，使用内置的一些固定的方法，在记录的数据上做操作，然后给用户一个输出
3. ……（你也可以再想想自己写过的啥程序）


对于其中的`数据`我们再熟悉不过了，在你见到的几乎所有的语言中，他们就是你直接操作的常/变量。对于这些量而言，在**设计**算法的初期，我们几乎不考虑它具体的值，我们更加关心的是它的类型！（有关类型，会在后面进行介绍）但是对于程序而言，一个运行时的程序，通常更加关注它的值。







正如SICP中对于程序设计的描述上，其关键点有：

1. 定义出这个程序的**输入**和**输出**
2. 定义出这个程序所需要的数据，例如 `Point{ int x; int y; }`
3. 根据我们拿到的数据、输入，来设计我们程序的大体框架（画流程图、伪代码等等）
4. 设计函数：把上面的框架做拆解，通常我习惯于类似于做一个广度遍历，逐步把上面流程图中涉及的一些方法做一个实现。
5. 开始你的实现。



### 语言逻辑、表达能力

好吧，我们这里根本不考虑所谓**程序**，因为我们绝大多数人从来都不是直接写二进制程序的！因此我们这里考虑的是语言的**表达能力**。（虽然我们在后文中不太考虑程序和代码的区别）

实际上我们已经知道答案了 —— **图灵完备**：

> In computability theory, a system of data-manipulation rules (such as a computer's instruction set, a programming language, or a cellular automaton) is said to be Turing-complete or computationally universal if it can be used to simulate any Turing machine (devised by English mathematician and computer scientist Alan Turing). This means that this system is able to recognize or decide other data-manipulation rule sets. Turing completeness is used as a way to express the power of such a data-manipulation rule set. Virtually all programming languages today are Turing-complete.

TLDR：从理论上说，我们使用的所有语言都有相同的表达能力！

那么问题是，为什么我们还需要考虑一个编程语言的表达能力呢？从我的理解来看，回答这个问题就和 Hello World 一样简单：

对于 Python：

```python
print "Hello World"  # py2
print("Hello World") # py3
```

对于 C：

```c
#include<stdio.h>
int main() {
  printf("Hello World\n");
  return 0;
}
```

或者 C++：
```c++
#include <iostream>
using namespace std;
int main() {
  cout << "Hello World" << endl;
  return 0;
}
```

对于 Racket（一种函数式编程语言）：

```racket
(print "Hello World")
```

从这里我们就能看出问题了，为了实现相同的功能，三种语言体现出完全不同的复杂、直观程度。

1. Python：直观的、简单 -- 很简单
2. C：直观的、不简单 -- 至少函数叫做 `print`
3. C++：不直观的、不简单 -- 什么是 `cout`？什么是 `<<`？为什么是 `<<`？
4. Racket：不直观、简单 -- 问题在于为什么需要这个括号？



<!-- TODO -->

### 程序=数据+函数

### 范式

函数是第一公民


ASYNC

### 词法、语法、解析与执行

### NFL

1. 简单 + 舒适
2. 复杂 + 舒适
3. 简单 + 难受
4. 复杂 + 难受




