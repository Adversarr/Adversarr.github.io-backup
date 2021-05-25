---
title: 日程
date: 2020-05-26 09:57:51
---

{% checkbox 并查集和图论 %}

```bash Dependencies
# npm install hexo-renderer-pandoc
npm install hexo-renderer-kramed
npm install hexo-renderer-mathjax
npm install searchdb
npm install hexo-asset-image
npm install hexo-deployer-git
npm i hexo-simple-mindmap
```

同时，更改了 Fluid 主题的部分内容

`tag_plugin.styl` 中：`.label: font-size 100%`

```js
// kramed/lib/rules/inline.js
var inline = {
  // escape: /^\\([\\`*{}\[\]()#$+\-.!_>])/,
  escape: /^\\([`*\[\]()#$+\-.!_>])/,
  autolink: /^<([^ >]+(@|:\/)[^ >]+)>/,
  url: noop,
  html: /^<!--[\s\S]*?-->|^<(\w+(?!:\/|[^\w\s@]*@)\b)*?(?:"[^"]*"|'[^']*'|[^'">])*?>([\s\S]*?)?<\/\1>|^<(\w+(?!:\/|[^\w\s@]*@)\b)(?:"[^"]*"|'[^']*'|[^'">])*?>/,
  link: /^!?\[(inside)\]\(href\)/,
  reflink: /^!?\[(inside)\]\s*\[([^\]]*)\]/,
  nolink: /^!?\[((?:\[[^\]]*\]|[^\[\]])*)\]/,
  reffn: /^!?\[\^(inside)\]/,
  strong: /^__([\s\S]+?)__(?!_)|^\*\*([\s\S]+?)\*\*(?!\*)/,
  // em: /^\b_((?:__|[\s\S])+?)_\b|^\*((?:\*\*|[\s\S])+?)\*(?!\*)/,
  em: /^\*((?:\*\*|[\s\S])+?)\*(?!\*)/,
  code: /^(`+)\s*([\s\S]*?[^`])\s*\1(?!`)/,
  br: /^ {2,}\n(?!\s*$)/,
  del: noop,
  text: /^[\s\S]+?(?=[\\<!\[_*`$]| {2,}\n|$)/,
  math: /^\$\$\s*([\s\S]*?[^\$])\s*\$\$(?!\$)/,
};
```

update to 1.8.6 Fluid.：

in `fluid/languages/zh-CN.yaml`

```
schedule:
  title: 日程
  subtitle: 近期日程安排
```