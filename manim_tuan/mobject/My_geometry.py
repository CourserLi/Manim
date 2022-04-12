# 在语句后面写了 + + 的表示在 manim 源代码函数中额外添加
# 并会标注在 manim 源代码函数中修改或新添的函数

"""
-----修改记录-----
2021.05.02
MyRectangle 添加了 get_width() | get_height() 作用: 返回长方形的宽和长
MySquare 添加了 get_length() 作用: 返回正方形的边长

"""

from manimlib import *
import numpy as np


class MyRectangle(Polygon):
    CONFIG = {
        "color": WHITE,
        "width": 4.0,
        "height": 2.0,
        "mark_paths_closed": True,
        "close_new_points": True,
        "sheen_factor": 0.0,  # + +
        "sheen_direction": UL,  # + +
    }
    width_ = 0  # + +
    height_ = 0  # + +

    def __init__(self, width=None, height=None, **kwargs):
        Polygon.__init__(self, UR, UL, DL, DR, **kwargs)

        if width is None:
            width = self.width
        else:  # + +
            self.width_ = width  # + +

        if height is None:
            height = self.height
        else:  # + +
            self.height_ = height  # + +

        self.set_width(width, stretch=True)
        self.set_height(height, stretch=True)

    # 下列函数为在源码的基础上修改

    # 下列函数为在源码的基础上添加

    def get_width(self):
        return self.width_

    def get_height(self):
        return self.height_


class MySquare(MyRectangle):
    CONFIG = {
        "side_length": 2.0,
    }
    length = 0  # + +

    def __init__(self, side_length=None, **kwargs):
        digest_config(self, kwargs)

        if side_length is None:
            side_length = self.side_length
        else:  # + +
            self.length = side_length  # + +

        super().__init__(side_length, side_length, **kwargs)

    # 下列函数为在源码的基础上添加
    def get_length(self):
        return self.length
