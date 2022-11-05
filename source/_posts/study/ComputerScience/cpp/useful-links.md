---
title: Useful Links for programming
author: Clover
date: 2022/10/5 # yyyy-mm-dd
categories: Programming
tags:
  - C/C++
  - Programming
plugins:
  - mathjax
---


## Cpp

### C++ Rvalue References Explained

[http://thbecker.net/articles/rvalue_references/section_01.html](http://thbecker.net/articles/rvalue_references/section_01.html)

### Abseil

> Abseil provides a number of containers as alternatives to STL containers. These containers generally adhere to the properties of STL containers, though there are often some associated API differences and/or implementation details which differ from the standard library.

- [Document](https://abseil.io/docs/cpp/)
- 

### Folly

> Folly (acronymed loosely after Facebook Open Source Library) is a library of C++14 components designed with practicality and efficiency in mind. Folly contains a variety of core library components used extensively at Facebook. In particular, it's often a dependency of Facebook's other open source C++ efforts and place where those projects can share code.

- [Github](https://github.com/facebook/folly)

### Coost

> coost 是一个兼具性能与易用性的跨平台 C++ 基础库，其目标是打造一把地表最好用的 C++ 开发神器，让 C++ 编程变得简单、轻松、愉快。
> 
> coost 原名为 co，后改为 cocoyaxi，前者过短，后者过长，取中庸之道，又改为 coost。它曾被称为小型 boost 库，与 boost 相比，coost 小而精美，在 linux 与 mac 上编译出来的静态库仅 1M 左右大小，却包含了不少强大的功能：

- [Document](https://coostdocs.github.io/cn/about/co/)
- [Github](https://github.com/idealvin/coost)

### Thrust

Cuda Algorithm library.

### Taskflow.

Alter to oneTBB.

- [link](https://github.com/taskflow/taskflow)

### Awesome Parallel Computing

- [link](https://github.com/taskflow/awesome-parallel-computing)

### ASSIMP

The official Open-Asset-Importer-Library Repository. Loads 40+ 3D-file-formats into one unified and clean data structure. (by assimp)


## 求解器、线性代数等

### Spectra

Spectra stands for Sparse Eigenvalue Computation Toolkit as a Redesigned ARPACK. It is a C++ library for large scale eigenvalue problems, built on top of Eigen, an open source linear algebra library.

Spectra is implemented as a header-only C++ library, whose only dependency, Eigen, is also header-only. Hence Spectra can be easily embedded in C++ projects that require calculating eigenvalues of large matrices.

https://github.com/yixuan/spectra/

## Vulkan

### VkBootstrap

As Vulkan is a very explicit API that gives very “direct” control, you need to initialize it to do things such as load extensions, select which GPU (or multiple!) you are going to use, and create the initial VkInstance and VkDevice structures that you then use with Vulkan commands.


https://github.com/charles-lunarg/vk-bootstrap
