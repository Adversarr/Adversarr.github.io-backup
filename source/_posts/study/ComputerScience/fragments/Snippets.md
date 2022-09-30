---
title: 神奇的 C++ 代码片段（模版元编程）
date: 2022-05-27
---

哈希函数

<!-- more -->

### The code

理论上说，把任何类型丢进去都能够直接hash了：

1. vector、map、set等stl容器
2. tuple、pair 等固定长模版容器
3. 定义了 `size_t hash()` 成员函数的任何类/结构体
4. 可变参数模版
5. ……（todo...）

```cpp
struct Hash {
  template <typename T>
  typename enable_if<!is_class<T>::value, size_t>::type
  operator()(const T &v) const {
    return hash<T>{}(v);
  }

private:
  size_t __hash_reduce(size_t h) const { return h; }
  size_t __hash_combine(size_t l, size_t r) const {
    return (l << 1) ^ r;
  }
  size_t __hash_reduce(size_t h, size_t t...) const {
    return __hash_combine(h, __hash_reduce(t));
  }

  template <typename T> size_t comb(const T &t) const { return Hash{}(t); }

  template <typename T, typename... Args>
  size_t comb(const T &t, const Args &...args) const {
    return __hash_reduce(Hash{}(t), comb(args...));
  }

public:
  template <typename T1, typename T2, typename... Args>
  size_t operator()(const T1 &t1, const T2 &t2, const Args &...args) {
    return comb(t1, t2, args...);
  }

  template <typename L, typename R>
  size_t operator()(const pair<L, R> p) const {
    return Hash{}(p.first, p.second);
  }

  template <typename I, typename C = typename I::const_iterator>
  size_t operator()(const I &it) const {
    size_t hv = 0;
    for (const auto &v : it) {
      hv = __hash_combine(hv, Hash{}(v));
    }
    return hv;
  }
  size_t operator()(const vector<bool> &bs) const {
    size_t hv = 0;
    for (int i = 0; i < bs.size(); ++i) {
      hv = __hash_combine(hv, Hash{}((int)bs[i]));
    }
    return hv;
  }

  template <typename... Args> size_t operator()(const tuple<Args...> &tup) {
    return apply([](Args... v) -> size_t { return Hash{}.comb<Args...>(v...); },
                 tup);
  }
  template <typename Hashable,
    typename = is_same<decltype(std::declval<Hashable>().hash()), size_t>>
  size_t operator()(const Hashable &v) {
    return v.hash();
  }
};
```