---
title: 谈谈编程
date: 2020-06-24
tags:
  - 杂谈
  - 编程
categories: 杂谈
math: true
plugins:
  - mathjax
---

编程十载。

<!-- more -->

笔者江苏南京人，小学听人说编程有点意思随便学了点 `Basic`，觉着程序设计挺有趣，便一直没有放下编程的学习。当时挺自信，用 `Basic` 也能写点东西，虽然看上去不怎样，却能解决点实际问题：

> Q：解不定方程：2 x + 3 y = 100, x y 是正整数。

```vba
FOR I = 1 TO 50
    FOR J = 1 TO 33
        IF 2*I+3*J = 100 THEN
            PRINT I
            PRINT J
        END IF
    NEXT J
NEXT I
```

Well，写的不好，但是至少我知道怎样去解决一些问题。要解这个方程实际上不需要这么麻烦。但是当时学到的确实是解决问题的方法：编一个程序、枚举各种情况、得到答案。

当然，如果我们仔细看一看这一个程序，实则三种最基础的程序结构都有：

1. 顺序：`PRINT I PRINT J`
2. 分支：`IF ... THEN ... (ELSE ...) END IF`
3. 循环：`FOR I = 1 TO 50 NEXT I`

确实，我们需要这三种结构就能创建整个程序了，至少当时的我，还能记得，这三个程序足以撑起你需要的一切。

上了初中，接触的是 `Pascal`，勉强写了两年，就跳去学“高大上”的 `C++` 了，做点对比：

```pascal
var a,b,c: int;

Procedure foo(para: int)
begin
    writeln(para+1)
end;

begin
    readln(a, b, c);
    foo(a);
    foo(b);
    foo(c);
end.
```

```c++
#include <iostream>
using namespace std;
void foo(int para) { cout << para; }

int main()
{
    int a, b, c;
    cin >> a >> b >> c;
    foo(a);foo(b);foo(c);
    return 0;
}
```

当时写的也是懵懵懂懂的，但也能说出些道道来：什么是函数，什么是形参实参之类的。当然，这些只是为了应付当年的 `NOIP` 比赛（现`csp`），写的程序里面大多是这样的：

```c++
int main()
{
  int a[10000000];
  int n;
  for(int i = 1;i<=n;++i) cin>> a[i];
  ......
}
```

当时还是挺自信，这玩意挺好啊，能解决问题，在赛场上也能拿点分。但是到了大学就不一样了。`c++` 程设这门课主要难点在于 `OOP` 与动态内存部分，各种 bug 都来了，我还记得，当时上的最多的网站：[Docs](https://docs.microsoft.com/zh-cn/)，是微软的技术文档，每天沉浸在理解、记忆如何去写一个可以编译的程序之中，觉得生活确实充实。

但是如果你问我，到底学到了什么，我只能说，我学会了如何写出一个能够编译的 cpp。

疫情期间，有更多的时间看了看国外的开放课程（MIT Open Course），例如：

`Intro to EECS 6.01I MIT`：计科、电子方向的导论课

讲的很浅显易懂，大概涉及以下几个方面

> **Topics**
>
> - State Machine
> - Differential Equations and Operations
> - Circuit
> - ... ...

在第一节课，教授指出了这门课的目的：形成思维方法，从以下几个方面去思考问题和知识。

- Primitives（原语）
- Combination（组合）
- Abstractions（抽象）
- Patterns（模式）

以电路为例

> **Example (Circuit)**
>
> - Primitives
>   - Ohm's Law
>   - Node
> - Combination
>   - KVL KCL Equations
>   - Node method, Loop method
> - Abstractions
>   - Parallel Combinations
>   - Series Combinations
> - Patterns
>   - in Series Combinations: $I = V / (R_1 + R_2)$
>   - in Parallel Combinations: $V_1 = R_1 I,\dots$

{% include_code lang:lua RandomTalks/AboutProgramming1/FunctionalProgramming.lua %}
