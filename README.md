等视频全部做完再细写......



介绍：数据结构演示动画

B站地址：[《数据结构》算法模拟动画](https://www.bilibili.com/video/BV12v411K7pZ?spm_id_from=333.999.0.0)



docs 文件夹是放 assets（图片）和 fonts（字体）的

mobject 文件夹是基于 manimlib（官方库）写的自用库

```python
__init__.py 是调用需要的东西，不用管它就好
```

LICENSE 是开源协议

README.md 就是你看的这个东西啦~

- [x] 教学 docker 配置运行（提醒这是旧版）



PS：采用的是 Manim 旧版，即用  `python -m manim example.py test -pl` 运行

而新版是用 `manimgl example.py test` 运行（由于新版存在某些 BUG，我使用的是旧版）



PS：记得写 `setup.py` 、 `setup.cfg` 和 `requirements.txt`，并用 `pip install -e .` 下载所需的py包（最好在anaconda的一个环境中进行）
