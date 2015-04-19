---
layout: default
---

<div class="home">

Title: Blogging
Date: 2013-09-02 16:28
<hr>

一直以为写博客是一件很有趣的事。旅行也是。想来也去了不少地方，故萌发了写这个旅行博客的想法。

在路上累得/困得/冻得半死的时候往往会想为什么要出来折腾自己。现在（28岁）的时候的想法是：旅行大致分为两种：一为探索世界，二为放松心情。前者需要用心了解诸如景点信息、交通路线、食宿天气等信息，适合精力旺盛而没钱的时候；后者则大可报个旅行团，上车睡觉下车拍照，适合有钱而没精力的时候。我的多数旅行属于前者，因而积攒了不少旅行经验和对世界的看法，故记于此。

生活本身也是一场旅行：阳台上种的小蕃茄，不经意做出的美食，甚至工作中发表的论文，此类人生趣事，亦值得一记。

原来的博客从2008年开始，记录了关于自己的生活、工作、技术、感悟等等。内容多为想到就写，读者寥寥。而如今若能战胜自己的惰性，将旅行中的种种记录下来，也不失为一件乐事。


搭建博客的方案，则陆陆续续经过了 Windows Live -> Google Blogger -> Wordpress -> Octopress -> Pelican 几个阶段。希望现在这个方案能用一辈子。


> So we beat on, boats against the current, borne back ceaselessly into the past.
> 
> <cite>F. Scott Fitzgerald</cite>
 

  <ul class="post-list">
    {% for post in site.posts %}
      <li>
        <span class="post-meta">{{ post.date | date: "%b %-d, %Y" }}</span>

        <h2>
          <a class="post-link" href="{{ post.url | prepend: site.baseurl }}">{{ post.title }}</a>
        </h2>
      </li>
    {% endfor %}
  </ul>

</div>
