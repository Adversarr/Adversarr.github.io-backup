---
title: 数据结构复习
date: 2020-8-19
categories: 程序设计
tags:
  - 数据结构
  - 编程
math: true
hide: false
---

数据结构复习

<!-- more -->

### 0、绪论

#### 碎碎念

四种基本的逻辑结构：

1. 集合结构
2. 线性结构
3. 树结构
4. 图结构

`ADT`的概念：

```cpp
ADT 数据类型 {
  数据对象：<Definition>
  数据关系：<Definition>
    基本操作：<Definition>
}
```

注意C和C++的区别，以及常用的语句

1. 没有 template，没有 class
2. `#define` 的使用
3. `typedef`、`union` 的使用
4. 异常处理：用的是 `Status` 表示（就是 `int` ），也有用 `exit` 的

简单提一下 `#define` 和 `typedef`：

```cpp
#define IDENTIFIER expr
// 在编译时会被直接替换成 expr
#define IDENTIFIER(x,y,z) expr
// 在编译时会被直接替换成expr，并且将expr中的 x y z 替换
// 例如

#define PI 1.57 + 1.57
cout << PI; // 编译时替换成 cout << 1.57 + 1.57;
// 想一想 PI*PI 是什么
#define ISROOT(node) (node->father == nullptr)
cout << ISROOT(tree._root_ptr);
// 编译时替换成 cout << (tree._root_ptr -> father == nullptr);
typedef int Status;
Status x; // 等价于 int x;
// 注意：不能有 template<
```

{% noteblock quote %}

*{% kbd 「再碎碎念一下」 %}*

`template` 还记得多少。

`new` `delete` 填程序可能考的（释放空间，析构函数）

万一出卷老师一时兴起，和我一样作死用 `virtual` 写 `avl::bst` 咋办

`typedef` 和 `#define` 定义的顺序不一样

我慌了。

{% endnoteblock %}

#### 时间复杂度

**{% kbd 「全场暴毙」 %}**：写出下面这个算法的时间复杂度

```cpp
// n 为 str 长度
// 则 func 是 o(?)
int func(char *str, char c)
{
  int cnt = 0;
  for (size_t i = 0; i < strlen(str); ++i)
    if (str[i] == c) cnt ++;
  return cnt;
}
```

> Ans：$O(n^2)$

#### 评估算法

**{% kbd 「算法的特性」 %}**：

1. 有穷性
2. 确定性
3. 可行性
4. 输入
5. 输出

**{% kbd 「算法的评估」 %}**：

1. 高效性
2. 正确性
3. 健壮性
4. 可读性

{% noteblock quote %}

**{% kbd 「要点：」 %}**

> 1. 时间复杂度如何？
> 2. 空间复杂度如何？
> 3. 相比其他算法的优缺点？
> 4. 如何实现？（注意细节）
> 5. 能手算吗？

{% endnoteblock %}


### 1、线性表

**{% kbd 「顺序表」 %}**


1. 静态 `#define MAXSIZE 100`
2. 动态 `new` or `malloc`

内存中的特点如何？

- 插入o(n)：
  - 思考：能不能用 `memcpy` 函数？
- 删除o(n)：
  - 这两个都要注意：表的长度要减少1
- 搜索o(n)：
  - 成功的平均比较次数 ASL = ？
  - 失败的比较次数？
- 合并
  - 无序：$O(na*nb)$
  - 有序：$O(na+nb)$

**{% kbd 「链表」 %}**

1. 单链表存储、插入、删除、合并
2. 循环链表
3. 双向链表

> 应用
>
> 1. 多项式的表示

### 2、栈与队列

链式存储！

1. **{% kbd 「栈」 %}**：LIFO
  1. 定义
  2. 初始化
  3. 压栈
  4. 出栈
Q：一个 n 元素序列依次进栈，则其不同的出栈队列有多少种
A：卡特兰数
2. **{% kbd 「队列」 %}**：FIFO
  1. 链式表示
  2. 循环队列（这个定义是啥？）
    1. 重点是如何判断 overflow
    2. 入队？出队？

### 3、串


如何定义？

1. 截止符 `\0`
2. 编码方式：Unicode or ASCII ？「这个考到就离谱」
3. 子串
4. 定长存储表示（堆分配）

操作：

1. 连接
2. 求子串
3. 插入（类似顺序表）
4. 链式存储（块链）

模式匹配算法

1. BF算法（一个个找）
2. KMP算法（跳转表）「如何求 `next` 表」
  - 类似于有限状态自动机状态转移
  - KMP的时间复杂度（求 `next` 表）

### 4、数组和广义表

- 一维数组
- 多维数组
  - 【写给自己】记得别再傻傻的用 `new int **` 了！

特殊矩阵压缩：

1. 对称：只存储对角线及以上（下）
  - 行号、列号的计算？
2. 三对角矩阵： `k = 2 * i + j`
3. 稀疏矩阵：
  1. 存放方式（三元组法）
  2. 快速转置算法
  3. 矩阵乘法
  4. 十字链表存储

广义表：

1. 都是指针、链式！
2. 表头表尾如何定义（链表结点）
   1. 原子节点：tag=0+原子的值
   2. 表节点：tag = 1 + `表头指针 hp` + `表尾指针 tp`
3. 第二种定义：
   1. 分三个：`utype`，`info`，`tp`

| utype | info | tp |
|---|---|---|
| 0 | 被引用次数 | 表头 |
| 1 | 数据值（atom） | 下一个节点 |
| 2 | （子）表 | 下一个节点 |

### 5、树

1. 定义（高度、兄弟、……）
   1. 性质
   2. 完全二叉树、满二叉树

2. 存储方式
   1. （完全）二叉树的顺序存储：有可能编号从 1 开始
   2. 链表存储：
      1. 二叉链表：`lc` + `data` + `rc`
      2. 三叉链表：`lc` + `data` + `father` + `rc`

3. 二叉树深度优先遍历（先中后）
   1. 表达式求值 【危】
4. 二叉树层次遍历
   1. 其中使用了____（线性数据结构）？
5. 线索化
   1.  `prec` + `lc` + `data` + `rc` + `suss`
   2. 中序遍历建立
6. 树的存储方式
   1. 双亲法、
   2. 指针法、
   3. 链表法、
   4. 孩子兄弟法
7. 树和二叉树的转换
8. 树的各种遍历法
9.  森林化为二叉树

{% noteblock quote %}

**应用**

1. **{% kbd 「堆」 %}**：上浮下沉
   1. 用的是完全二叉树的顺序存储
2. **{% kbd 「Huffman编码树」 %}**

{% endnoteblock %}


### 6、查找

1. **查找表**
  1. 关键字
  2. 属性
2. （无序）顺序表查找
  1. 检查哨？（这玩意的意义到现在也没懂）
  2. `ASL = (n + 1) / 2`
  3. `ASL = n + 1 (fail)`

```cpp
int search(SeqTable st, KeyTp key)
{
  int i = 0;
  st.elem[0].key = key;
  for (i = st.length; st.elem[i].key != key; --i);
  return i;
}
```

3. （有序）顺序表查找「二分查找法」
  1. 可以得到「判定树`Decision Tree`」
4. 索引顺序表（分块查找）
  1. 特点：块间有序，块内无序
  2. 附加索引表（关键字有序）

【顺序表查找方法比较】

| | 顺序查找 | 折半查找 | 分块查找 |
|---|---|---|---|
| ASL | 最大 | 最小 | 折中 |
| 表结构 | 有序、无序 | 有序 | 分块有序 |
| 存储结构 | 顺序存储结构、线性链表 | 顺序存储 | 顺序存储结构线性链表 |

#### 二叉搜索树（BST）

定义：`lc.key <= self.key <= rc.key (lc, rc exists)`

1. 如何搜索？
   1. 递归
   2. **注意宏定义！！！**（不清楚看：§1.碎碎念）
      1. `#define EQ(a, b) ((a) == (b))` *（没必要）*
2. 插入
   1. **先搜索，看这个元素存不存在！**
      1. 搜索成功，已经有这个元素（不插入？替换？看题目）
      2. 不成功，插入这个元素（作为叶子）
3. 通过无序表构造二叉搜索树
4. 删除结点
   1. 叶子？
   2. 左右子女有一个为空？
   3. 都非空？（直接后继：右子树“最左侧”的结点）
5. 这边莫名q了一下「卡特兰数」：对于有 n 个关键字的集合，其关键字有 n! 种不同排列，可构成的不同的二叉搜索树有 $\frac{1}{n-1}C^n_{2n}$ 颗。  
6. “匀称”？AVL
   1. 平衡条件：`-1 <= lc.height - rc.height <= 1` 其中：`lc.height - rc.height` 被称为「平衡因子」。
   2. 维持平衡方法：旋转
      1. 单旋：
         1. `right(node)`
         2. `left(node)`
      2. 双旋：
         1. 左右 `leftright(node) = left(node->lc) + right(node)`
         2. 右左 `rightleft(node) = right(node -> rc) + left(node)`
     3. 什么时候用？
         1. `left` ：`node->lc->lc` 高
         2. `right`：`node->rc->rc` 高
         3. `leftright`：`node->lc->rc` 高
         4. `rightleft`：`node->rc->lc` 高
   3. 插入：
      1. 先按BST插入
      2. 检查、维持平衡

**{% kbd 「B 树」 %}**

> 盲猜会考【迷之自信】  

1. 定义
   1. 实际上和BST(AVL)很像（算是BST(AVL)的推广？）
   2. BST(AVL)在每个结点上都是用一个 `key` 把原来的有序表分成了两块，例如：`(key=1, lc = {key < 1}, rc = {key > 1})` 【意会一下】
   3. B树（思想上）就是分成了k块（`m/2 <= k <= m`）：`(ptr[0] = {key < key[1]}, key[1], ptr[1] = {key[1] < key < key[2]}, key[2], ... , ptr[k] = {key[k] < key < key[k+1]}, key[k+1], ptr[k+1] = {key[k+1] < key])`（还是提一下：分成k块只要切k-1刀，所以key从1开始索引）
   4. 细节看ppt。（平衡因子 = 0、叶子结点为 F 的作用）
2. 查找`targ_key`：
   1. 从根结点开始 `current_node = root`
   2. 如果`current_node` 是 F（叶子），返回`not found`，否则在这个结点上找`targ_key`（顺序查找！就那么几个点，二分很可能效率更低！）
      1. 找到：返回
      2. 没找到，在 `ptr[next]` 中继续找，其中 ：
         1. next = x `(key[x] < targ_key < key[x+1])`
         2. next = k `(key[k] < targ_key && 该结点只有 k+1 个key)`
         3. next = 0 `(targ_key < key[0])` 
   3. 转 2
   4. 【类比二叉搜索树的查找】
3. 插入：
   1. 平衡维持：分裂
   2.  看ppt吧，我也写不清楚，画图比较好，也就几种情况：
      1. father 的 ptr 数目（度）< m？
      2. father 的 ptr 数目（度）= m？
      3. 这个分裂的结点是root？
4. 构造：不断插入

**{% kbd 「B+」 %}**
1. 注意和B树的区别：
   1. m 还是 m + 1？
   2. 看清楚上一层的key实则是子树的key的最大值
   3. 最底层从左到右排列就是原表（有序）
2. 插入：
   1. 平衡维持：分裂
   2. 看ppt吧，我也写不清楚，画图比较好，也就几种情况：
      1. father 的 ptr 数目（度）< m？
      2. father 的 ptr 数目（度）= m？
      3. 这个分裂的结点是root？

**{% kbd 「Hash」 %}**

1. 两个问题：
   1. 均匀的散列函数（简单快速）
   2. 解决冲突的方案
2. Hash函数：
   1. 「直接定址法」：`Hash(key) = a * key + b`（适合相对连续的数字）
   2. 「数字分析法」：选择近乎随机的某几位（书上讲的好点）
   3. 「除留余数法」：`Hash(key) = key % p`
   4. 「平方取中法」：一般取散列地址总数为 8 的 r 次幂，则取平方数中间的 r 位
   5. 「折叠法」：`123456789` -> `123+456+789`
3. 冲突解决：
   1. 「开放地址法」：线性探测法、二次探测法、伪随机探测法（书上例子挺好的，摘在下面）
   2. 「再哈希法」
   3. 「链地址法」：每一个 key 都对应一个链表
   4. 「公共区溢出法」（书上没有）

```python
Hash(key) = key % 11;
[\ \ \ \ \ 60 17 29 \ \ \]
# 插入 38， 且产生随机数 9
# 线性探测：(d = 3)
[\ \ \ \ \ 60 17 29 38 \ \]
# 二次：（d = -1)
[\ \ \ \ 38 60 17 29 \ \ \]
# 伪随机：(d = 9)
[\ \ \ 38 \ 60 17 29 \ \ \]
```


|  方法  |  ASL(success)  |  ASL(fail)  |
| --- | --- | --- |
|  线性探测  |  $\frac 1 2(1+\frac 1{1-\alpha})$  | $\frac 1 2(1+\frac 1{(1-\alpha})^2)$ |
|  二次/伪随机  |  $-\frac 1 \alpha \ln(1-\alpha)$  | $\frac 1 {1-\alpha}$   |
|  链地址法  |  $1 + \frac \alpha 2$  |  $\alpha + e^{-\alpha}$  |

### 7、图

基础概念：自己看离散「超凶」：{% btn 2020/05/28/study/ComputerScience/DiscreteMath/GraphTheory/, 图的基本概念, 图的基本概念 %}

1. 存储方式
   1. 「邻接矩阵」：`A[i, j] = ( < i, j > in E) ? weight(i, j) : ((i == j) ? 0 : UNDEFINED)`
      1. 稀疏时严重的空间浪费！
   2. 「邻接表」：`adj[i]` 为 i 的出边（无向图：相临边）
      1. 逆临接表
2. 遍历（~~不会吧不会吧，不会真的有人不会吧~~）
   1. 「DFS」
   2. 「BFS」
3. 「MST」
   1. 「Prim」：增加点
   2. 「Kruskal」：不断连接连通分支
4. AOV
   1. 「拓扑排序」：O(n+e)
5. AOE
   1. 关键路径：
      1. 路径上的点都是关键活动点 是 该路径为关键路径的 _____ 条件？
      2. 最早可能开始时间 `e[k]` = 最迟允许开始时间 `l[k]` 
      3. 有点像DP（拓扑）？怎么手算？
6. 最短路径
   1. **「Dijkstra算法」**
      1. 念叨一句使用条件：『无负权边』
   2. **「Floyd算法」**（ppt 里面没有）
   3. 「SPFA」！！（书上 ppt 都没有）：无负边的时候，绝对是最快的


### 8、排序


简单提几句就行了、叭、、

|  alg  |  时间复杂度  |  稳定？  |  描述  |
| --- | --- | --- | --- |
|  插入  | $O(n^2)$   |  y  |  想想打牌的时候理牌的过程  |
|  选择  | $O(n^2)$  |  n  |  选剩下的最大的扔到最后  |
|  希尔  |  $O(n log n)$ |  n  |  玄学算法复杂度（缩小增量）  |
|  冒泡  | $O(n^2)$  |  y  |  冒泡赛  |
| 「快排」   |  $O(n log n)$  | n  |  重点  |
|  堆排  |  $O(n log n)$  |  n  |  建立（升序建立大根堆）堆，抽堆顶，维护堆  |
|  归并  |  $O(n log n)$  | y |  常见（C++ STL）  |
|  基数  |  $O(n log n)$  |  n  |  分配、收集  |

**{% kbd 「快速排序」 %}**：主要思想是选一个数，做交换，让序列中左边的数都比这个数小，右边的数都比这个数大。

q一下以前见过的一个讲的很好的解释【找不到链接了，如果找到了请评论区发一下】：

> 快排可以用挖坑 + 填坑来理解（这个看ppt上有一个图）
>
> 1. 记住pivot，然后把pivot的位置上挖个坑，并且设置 `i, j = l, r`
> 2. 在右侧（j 从右向左）找一个比pivot大的，填到坑里，并且把 j 这里挖个坑【此时若出现 i >= j 转 4 】
> 3. 在左侧（i 从左向右）找一个比pivot小的，填到坑里，并且把 i 这里挖个坑【此时若出现 i >= j 转 4 】
> 4. 这个时候 i == j，而且在这里有个坑可以填，将pivot填进去
> 5. 对左侧序列，右侧序列执行快排。

```python
# 第一个是 Pivot
def qsort(seq : list, l : int, r : int):
    if l >= r:
        return
    pivot = seq[l]
    i, j = l, r
    while (i < j):
        while (i < j and seq[j] >= pivot):
            j--
        seq[i] = seq[j]
        while(i < j and seq[i] <= pivot):
            i++
        seq[j] = seq[i]
    # 此时 i == j
    seq[i] = pivot
    # 对左右两侧的表分别排序
    qsort(seq, l, i - 1)
    qsort(seq, i + 1, r)
    

# 随机 Pivot
def qsort(seq: list, l: int, r: int):
    if l == r:
        return
    p = randint(l, r)
    pivot = seq[p] # 随便选一个 pivot
    i, j = l, r
    while (i<j):
        while (pivot <= seq[r] and l < r):
            r--
        p, seq[p] = r, seq[r]
        while (pivot >= seq[l] and l < r):
            l++
        p, seq[p] = l, seq[l]
    seq[i] = pivot
    qsort(seq, l, i - 1)
    qsort(seq, i + 1, r)
```

> 不保证正确。嘿嘿😶

插入排序

![插入排序](https://www.runoob.com/wp-content/uploads/2019/03/insertionSort.gif)

希尔排序

![希尔排序](https://www.runoob.com/wp-content/uploads/2019/03/Sorting_shellsort_anim.gif)

冒泡排序

![冒泡排序](https://www.runoob.com/wp-content/uploads/2019/03/bubbleSort.gif)

快速排序

![快速排序](https://www.runoob.com/wp-content/uploads/2019/03/quickSort.gif)

选择排序

![选择排序](https://www.runoob.com/wp-content/uploads/2019/03/selectionSort.gif)

堆排序

![堆排序1](https://www.runoob.com/wp-content/uploads/2019/03/heapSort.gif)

![堆排序2](https://www.runoob.com/wp-content/uploads/2019/03/Sorting_heapsort_anim.gif)

归并排序

![归并排序](https://www.runoob.com/wp-content/uploads/2019/03/mergeSort.gif)

基数排序

![基数排序](https://www.runoob.com/wp-content/uploads/2019/03/radixSort.gif)
