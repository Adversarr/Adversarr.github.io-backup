---
title: Hexo 建站实录
author: Jerry Yang
tag:
- 杂记
categories:
- 编程
date: 2020-8-13
---

建站实录

<!-- more -->

# Hexo

### 前言

需要准备的材料：

1. vscode
   - VSCode 的终端内，要换成`cmd.exe`，按下 `ctrl + ,` 进入设置，找到 `terminal.external.windowsExec`这个，修改为 `C:\Windows\System32\cmd.exe`
2. Node.js

   > 安装完成后需要执行：`npm config set registry https://registry.npm.taobao.org`，来重新定向源。

3. Git客户端、以及一个配置好的 Github 账号

### 站点建立

> https://docs.github.com/en/github/working-with-github-pages

- 安装Git
  - Git 的配置
- 安装Node.js
- 安装Hexo
- GitHub创建个人仓库

Git：在[Mirror](https://npm.taobao.org/mirrors/git-for-windows/v2.28.0.windows.1/)中下载，并安装 `Git-2.28.0-64-bit.exe`（中间都是直接点击下一步即可）

Node.js：在[Mirror](https://npm.taobao.org/mirrors/node/latest-v14.x/)中下载，并安装 `node-v14.8.0-x64.msi`。



第一步，为你的站点设置一个代码仓库：

> [Ref](https://docs.github.com/en/github/working-with-github-pages/creating-a-github-pages-site#creating-a-repository-for-your-site)

第二步，站点初始化

> [Ref](https://docs.github.com/en/github/working-with-github-pages/creating-a-github-pages-site#creating-your-site)
>
> Note: It can take up to 20 minutes for changes to your site to publish after you push the changes to GitHub. If your don't see your changes reflected in your browser after an hour, see "About Jekyll build errors for GitHub Pages sites."
>
> 部署需要时间、每小时最多部署10次，站点大小最多1G（图片不能太多太大，搞大型个人相册就免了）

第三步，找一个地方，专门存放你的这个站点，例如：`D:/repos/` 在这个文件夹中 clone 下你的这个仓库。并且在 VScode 中打开这个**仓库**

在这里，按照：

> [Ref](https://hexo.io/zh-cn/docs) 安装 Hexo。

> [Ref](https://hexo.io/zh-cn/docs/setup) 在本机上建立站点

注意，因为直接在git下的目录中打开code，所以其中的folder就是 `.` （当前文件夹）不用执行cd切换工作文件夹，也就是（在VScode 终端中执行）：

```bash
hexo init .
npm install
```

- 初次尝试

``` BASH
hexo s --debug # 显示debug反馈
hexo s # 精简模式
```

应当显示：

```bash
...

INFO  Hexo is running at http://localhost:4000 . Press Ctrl+C to stop.
```

`ctrl + 鼠标左键` 点击链接看看？

deploy 配置

```yaml
deploy:
  type: git
  repository: git@github.com:Jerryyang2001/Jerryyang2001.github.io.git
  branch: master # 注意是 master 分支
  message: Site updated:{{ now('YYYY-MM-DD HH:mm:ss') }})
```

- 站点配置
  - `_config.yml`
  - 实际上就按照 readme 走就行。

- 更换主题（以我现在用的 `Fluid` 为例）
  - 注意看文档就行
  - 主题配置

- 发布文章
  - Hexo 工作流
  - `yaml`
  - `<!-- more -->`用法

- 个性化设置
  - 搜索器
  - Mathjax
  - Valine
  - 思维导图

- 其他
  - code Snippet

- 附录

> 参考了部分：[Ref](https://zhuanlan.zhihu.com/p/26625249)