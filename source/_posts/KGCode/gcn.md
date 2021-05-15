---
title: GCN introduction
date: 2020-11-4
category: Deep Learning
tags:
- Deep Learning
- GCN
hide: true
---


图卷积神经网络

<!-- more -->

# Graph Convolutional Network

> 翻译自：[Graph Convolutional Networks | Thomas Kipf | University of Amsterdam](http://tkipf.github.io/graph-convolutional-networks/)

### 概述

现实世界中许多重要的数据（集）常常以图和网络的形式呈现，例如：社交网络，知识图谱，蛋白质相互作用网络，万维网等等（只举几例）。但是，直到最近，注意力很少放在对这些结构化的数据，建立泛化的神经网络模型之上。

最近几年，一些论文重新考虑了这些问题（统一的神经网络，去处理任意的结构化图数据） [Bruna et al.](http://arxiv.org/abs/1312.6203), ICLR 2014; [Henaff et al.](http://arxiv.org/abs/1506.05163), 2015; [Duvenaud et al.](http://papers.nips.cc/paper/5954-convolutional-networks-on-graphs-for-learning-molecular-fingerprints), NIPS 2015; [Li et al.](https://arxiv.org/abs/1511.05493), ICLR 2016; [Defferrard et al.](https://arxiv.org/abs/1606.09375), NIPS 2016; [Kipf & Welling](http://arxiv.org/abs/1609.02907), ICLR 2017，其中一些，现在已经在他们主导的领域，取得了非常可喜的成果。

在这篇文章中，我将对近些年在这方面的研究给出一个概要，并且指出不同方法的优缺点。这些讨论主要聚焦于最近发表的这两篇论文：

- Kipf & Welling (ICLR 2017), [Semi-Supervised Classification with Graph Convolutional Networks](http://arxiv.org/abs/1609.02907) (disclaimer: I'm the first author)
- Defferrard et al. (NIPS 2016), [Convolutional Neural Networks on Graphs with Fast Localized Spectral Filtering](https://arxiv.org/abs/1606.09375)

以及 Ferenc Huszar 写的一篇回顾/讨论的文章：[How powerful are Graph Convolutions?](http://www.inference.vc/how-powerful-are-graph-convolutions-review-of-kipf-welling-2016-2/) ，这篇文章主要讨论了这几类模型的一些限制。我[在这里](http://tkipf.github.io/graph-convolutional-networks/#the-issue-with-regular-graphs)写了一点对这篇文章的评论（在文章的末尾）。

### 大纲

- 对GNN的简单描述
- 谱域卷积与GCNs
- Demo：简单一阶GCN模型的图嵌入
- 将 GCNs 作为 *Weisfeiler-Lehman* 算法的可微分

如果你已经熟悉了 GCNs 与相关的方法，你可以直接跳到[Embedding the karate club network](http://tkipf.github.io/graph-convolutional-networks/#gcns-part-iii-embedding-the-karate-club-network)。

