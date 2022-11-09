# 《数据结构》代码可视化

<div align=center><img src="https://s1.ax1x.com/2022/11/10/zSjj10.png"></div>

### 项目介绍

Manim 引擎地址：https://github.com/3b1b/manim

**Manim 是一个数学动画引擎，使用 Python 代码实现基本动画对象和运动轨迹，利用 FFmpeg 对视频进行串流，通过 OpenGL 及其 GLSL 语言来使用 GPU 进行渲染，最终实现各种动画。我在此基础之上，针对 C++ 版的数据结构的代码，进行可视化创作，使得观众能看懂每一行代码的运行过程**

全部视频发布于 B 站：[《数据结构》算法模拟动画](https://www.bilibili.com/video/BV12v411K7pZ?spm_id_from=333.999.0.0)

代码参考书籍：[《算法与数据结构（C++ 版）》](https://item.jd.com/72399479974.html)

**包含数据结构类型：顺序表、单链表、栈、队列、KMP、二叉树、排序、图**

### 部分视频截图（选取自 [KMP 算法](https://www.bilibili.com/video/BV12v411K7pZ?p=6&vd_source=3796e5fb474fd9dc44fdec1da44336f6)、[二叉树](https://www.bilibili.com/video/BV12v411K7pZ?p=7&vd_source=3796e5fb474fd9dc44fdec1da44336f6)、[Prim 算法](https://www.bilibili.com/video/BV12v411K7pZ?p=16)）

<div align=center><img src="https://s1.ax1x.com/2022/11/10/zSj6TH.png" alt="zSj6TH.png"></div>

<div align=center><img src="https://s1.ax1x.com/2022/11/10/zSj2tA.png"></div>

<div align=center><img src="https://s1.ax1x.com/2022/11/10/zSjfpt.png"></div>

### 文件介绍

**此项目的全部代码仅供参考，只包含关键代码片段，而非整体开发环境**

- manimlib（官方类）

- manim_tuan（个人类）
  - animation（扩展动画类）
  - mobject（扩展对象类）
  - docs
    - assets（图片）
    - fonts（字体）
- example（官方提供测试文件）
- seq（顺序表）
- links（单链表）
- stack（栈）
- queue（队列）
- kmp（KMP 算法）
- tree（二叉树）
- sort（排序算法）
- graph（图）
- test（测试集）
- other（其他测试集）

### 注意事项！！！

我采用的是 Manim 旧版（目前已经绝版），即用  `python -m manim example.py test -pl` 运行

新版采用的是 ManimGL（支持即时渲染和键鼠交互），由 `manimgl example.py test` 运行

PS：推荐使用[新版](https://github.com/3b1b/manim)或者[社区版](https://github.com/ManimCommunity/manim)（社区版由 Manim 爱好者共同维护，相对更新得更频繁 ~）