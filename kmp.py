from manimlib.imports import *
from manim_tuan import *

"""
TODO
0: 代码加颜色
1: 完善 frame_variable 的不同情况(s串长度为 5 | 10 | 15 | 20 ) 与优化 frame_code(即任何长度都保持居中动画演示)
2: 补充 bfFind 函数的代码
3: 添加两个版本的代码(冯、考研王道)
4: 调整 move_frame 移动速度
5: 选择性加入s串或t串的长度等于0时(不符合常规)的动画演示
"""

"""
BUG
1: 有时会有莫名其妙的越界(exp: s = "abaacababbaacaacbabc" | t = "ababc" ) (exp2: s = "abcde" | t = "ababc" )
【好像是当t串找不到s串匹配项的时候】
2: 为了缩短 kmp 代码语句，合并了 if 和 else 的部分，因此当 move_frame 移动时会产生歧义
3: Integer 代入 -1 时使用 set_value 数字会莫名其妙的变透明，因此我改用 Transform 代替
"""

"""
整体框架
1: 自定义信息(s串、t串、选择匹配方法)
2: 自定义函数代码
3: 四个函数(bf_find、get_next、get_nextval、kmp) 用于获取目标 next/nextvalue 值
4: 主类kmp的框架一: frame_code
5: 主类kmp的框架二: frame_variable
6: 主类kmp的框架三: frame_animation 的基本图形(S串、T串、T Next、i and j)构造
7: 主类kmp的框架三: frame_animation 的位置
8: 主类kmp的框架三: frame_animation 的演示函数(bfFind、getNext、getNextVal、kmpFind)
"""

"""
主要 VGroup 框架一览(sort)

variable_fixed
|
|__variable_rectangle
|__variable_SZ
|__variable_S_curlength
|__variable_TZ
|__variable_T_curlength

variable_transform
|
|__variable_Next/NextVal
|__variable_i
|__variable_j
|__variable_i_num
|__variable_j_num

s_all / t_all
|
|__s_square
|__s_num
|__s_rectangle
|__s_name

t_up_next_all
|
|__t_up_all
|     |__t_up_square
|     |__t_up_num
|     |__t_up_rectangle
|     |__t_up_name
|__t_next_all
|     |__...
|
|__t_up_next_rectangle
|__t_up_next_line

i_j_all
|
|__i_all
|    |__i_square
|    |__i_triangle
|    |__i_reveal
|           |__i_reveal_front
|           |__i_reveal_value
|
|__j_all
     |__...
"""

"""
语句 * square.get_length() / 0.7 的作用是对图像与动画整体的一个缩放

detail:
一开始，我是以 square = MySquare(.., side_length=0.7, ..) 进行动画绘制
后面为了调整画面整体框架，于是将 kmp 动画部分整体缩小
我采用的策略是将所有移动、对其、缩放等函数的基本单位设置为 square 的长度，即 square.get_length() / 0.7 (= narrow_multiple)
当需要调整 kmp 动画部分整体大小时只需要重设 square = MySquare(.., side_length= x , ..) 即可
"""

# bfFind
# getNext
# getNextVal
# kmpFind

# 自定义串信息( 1 <= len(t) <= len(s) <= 15 )
s = "abaacababcac"
t = "ababc"
chose = 2  # 1:bfFind  2:getNext + kmpFind  3:getNextVal + kmpFind

# 自定义函数代码(若需更改代码，其行数与格式必须保持一致)
getNext_codes = [
    "void String::getNext(const String &t, int *next)",
    "{",
    "   int i = 0, j = -1;",
    "   next[0] = -1;",
    "   while (i < t.curLength - 1)",
    "   {",
    "      if ((j == -1) || (t[i] == t[j]))",
    "      {",
    "         ++i, ++j;",
    "         next[i] = j;",
    "      }",
    "      else",
    "         j = next[j];",
    "   }",
    "}",
]
getNextVal_codes = [
    "void String::getNextVal(const String &t, int *nextVal)",
    "{",
    "   int i = 0, j = -1;",
    "   nextVal[0] = -1;",
    "   while (i < t.curLength - 1)",
    "   {",
    "      if ((j == -1) || (t[i] == t[j]))",
    "      {",
    "         ++i, ++j;",
    "         if (t[i] != t[j])",
    "            nextVal[i] = j;",
    "         else",
    "            nextVal[i] = nextVal[j];",
    "      }",
    "      else",
    "         j = nextVal[j];",
    "   }",
    "}",
]
kmpFind_codes = [
    "int String::kmpFind(const String &t, int pos)",
    "{",
    "   if (t.curLength == 0) return 0;",
    "   if (curLength < t.curLength) return -1;",
    "   int i = 0, j = 0;",
    "   int *next = new int[t.curLength];",
    "   getNextVal(t, next);",
    "   while (i < curLength && j < t.curLength)",
    "   {",
    "      if (j == -1 || data[i] == t.data[j])",
    "         i++, j++;",
    "      else",
    "         j = next[j];",
    "   }",
    "   delete[] next;",
    "   if (j >= t.curLength) return (i - t.curLength);",
    "   else return -1;",
    "}",
]


def get_next(t):
    i = 0
    j = -1
    length = len(t)
    result_next = [0] * length
    result_next[0] = -1
    while i < length - 1:
        if j == -1 or t[j] == t[i]:
            i += 1
            j += 1
            result_next[i] = j
        else:
            j = result_next[j]
    return result_next


def get_nextval(t):
    i = 0
    j = -1
    length = len(t)
    result_next = [0] * length
    result_next[0] = -1
    while i < length - 1:
        if j == -1 or t[j] == t[i]:
            i += 1
            j += 1
            if t[i] != t[j]:
                result_next[i] = j
            else:
                result_next[i] = result_next[j]
        else:
            j = result_next[j]
    return result_next


def kmp(s, t, next_list):
    s_length = len(s)
    t_length = len(t)
    i = 0
    j = 0
    while i < s_length and j < t_length:
        if j == -1 or s[i] == t[j]:
            i += 1
            j += 1
        else:
            j = next_list[j]
    if j >= t_length:
        return i - j
    else:
        return -1


class bf(Scene):
    def construct(self):
        pass


class 供bf参考的gn(Scene):
    def construct(self):
        # S 串
        s = "abaacababcac"
        length_s = len(s)
        square = Square(color=BLUE, side_length=0.7, stroke_opacity=0)
        s_square = VGroup()
        s_num = VGroup()
        for i in range(length_s):
            s_square.add(square.copy())
            s_num.add(Text("{}".format(s[i])).scale(0.6))
        s_square.arrange(RIGHT, buff=0)
        for i in range(length_s):
            s_num[i].move_to(s_square[i])
        s_rectangle = (
            Rectangle(color=RED, height=0.9, width=0.7 * length_s + 1.8)
            .move_to(s_square.get_center())
            .align_to(s_square, RIGHT)
            .shift(RIGHT * 0.1)
        )
        s_name = (
            Text("SZ |")
            .scale(0.7)
            .move_to(s_rectangle.get_center())
            .align_to(s_rectangle, LEFT)
            .shift(RIGHT * 0.425)
        )
        s_all = VGroup(s_square, s_num, s_rectangle, s_name)
        s_all.move_to(np.array([0, 0, 0]))  # reference
        # self.add(s_all)

        # T 串
        t = "ababc"
        length_t = len(t)
        t_square = VGroup()
        t_num = VGroup()
        for i in range(length_t):
            t_square.add(square.copy())
            t_num.add(Text("{}".format(t[i])).scale(0.6))
        t_square.arrange(RIGHT, buff=0)
        for i in range(length_t):
            t_num[i].move_to(t_square[i])
        t_rectangle = (
            Rectangle(color=RED, height=0.9, width=0.7 * length_t + 1.8)
            .move_to(t_square.get_center())
            .align_to(t_square, RIGHT)
            .shift(RIGHT * 0.1)
        )
        t_name = (
            Text("TZ |")
            .scale(0.7)
            .move_to(t_rectangle.get_center())
            .align_to(t_rectangle, LEFT)
            .shift(RIGHT * 0.425)
        )
        t_all = VGroup(t_square, t_num, t_rectangle, t_name)
        t_all.next_to(s_all, DOWN, buff=0.5)  # reference
        # self.add(t_all)

        # T Next(t_up + t_next)
        t_up_all = t_all.copy()
        t_next = t
        t_next_square = t_square.copy()
        t_next_num = VGroup()
        next_ = get_next(t)  # T串的Next值列表
        for i in range(length_t):
            t_next_num.add(Text("{}".format(next_[i]), color=BLACK).scale(0.6))
            t_next_num[i].move_to(t_next_square[i])
        t_next_rectangle = (
            Rectangle(color=RED, height=0.9, width=0.7 * length_t + 1.8)
            .move_to(t_next_square.get_center())
            .align_to(t_next_square, RIGHT)
            .shift(RIGHT * 0.1)
        )
        t_next_name = (
            Text("Next|")
            .scale(0.7)
            .move_to(t_next_rectangle.get_center())
            .align_to(t_next_rectangle, LEFT)
            .shift(RIGHT * 0.125)
        )
        t_next_all = VGroup(
            t_next_square, t_next_num, t_next_rectangle, t_next_name
        ).next_to(t_up_all, DOWN, buff=0)

        t_up_next_all = VGroup(t_up_all, t_next_all)
        t_up_next_rectangle = Rectangle(
            color=YELLOW, height=1.8, width=0.7 * length_t + 1.8
        ).move_to(t_up_next_all.get_center())
        t_up_next_all.add(t_up_next_rectangle).move_to(np.array([0, 0, 0]))
        t_up_next_line = Line(
            t_up_next_rectangle.get_vertices()[0],
            t_up_next_rectangle.get_vertices()[1],
            color=YELLOW,
        ).move_to(t_up_next_all.get_center())
        t_up_next_all.add(t_up_next_line)
        # self.add(t_up_next_all)

        # i and j
        i_square = Square(color=PURPLE, side_length=1)
        j_square = i_square.copy()
        i_triangle = (
            Triangle(fill_opacity=1, color=YELLOW)
            .scale(0.12)
            .rotate(PI)
            .move_to(i_square.get_center())
            .shift(DOWN * 0.2)
        )
        j_triangle = (
            Triangle(fill_opacity=1, color=YELLOW)
            .scale(0.12)
            .move_to(j_square.get_center())
            .shift(UP * 0.2)
        )
        i_reveal_front = (
            Text("i:", color=WHITE)
            .scale(0.4)
            .move_to(i_square.get_center())
            .shift(UP * 0.21 + LEFT * 0.13)
        )
        i_reveal_value = (
            Integer(0, color=WHITE)
            .scale(0.4)
            .move_to(i_square.get_center())
            .shift(UP * 0.21 + RIGHT * 0.2)
        )
        i_reveal = VGroup(i_reveal_front, i_reveal_value)
        j_reveal_front = (
            Text("j:", color=WHITE)
            .scale(0.4)
            .move_to(j_square.get_center())
            .shift(DOWN * 0.21 + LEFT * 0.13)
        )
        j_reveal_value = (
            Integer(-1, color=WHITE)
            .scale(0.4)
            .move_to(j_square.get_center())
            .shift(DOWN * 0.21 + RIGHT * 0.3)
        )
        j_reveal = VGroup(j_reveal_front, j_reveal_value)
        i_all = VGroup(i_square, i_triangle, i_reveal)
        j_all = VGroup(j_square, j_triangle, j_reveal)
        i_j_all = VGroup(i_all, j_all)
        # self.add(i_j_all)

        # show get_next
        # position + updater
        t_up_next_all.move_to(np.array([0, 0, 0]))
        t_all.next_to(t_up_next_all, DOWN, buff=0.15).shift(RIGHT * 0.7)
        invision = square.copy().move_to(t_all[0][0])
        i_all.next_to(t_up_next_all[0][0][0], UP, buff=0.35)
        j_all.next_to(t_all[0][0], DOWN, buff=0.35).align_to(i_all, LEFT)
        # MaintainPositionRelativeTo
        self.add(t_all, t_up_next_all, invision, i_j_all)

        # function
        i = 0
        j = -1
        length = len(t)
        result_next = [0] * length
        result_next[0] = -1
        self.play(t_up_next_all[1][1][0].set_color, WHITE)
        self.play(
            t_up_next_all[1][0][i].set_stroke,
            {"opacity": 1},
            t_up_next_all[0][0][i].set_stroke,
            {"opacity": 1},
        )
        while i < length - 1:
            if j == -1 or t[j] == t[i]:
                i += 1
                j += 1
                self.play(
                    MaintainPositionRelativeTo(
                        j_all, i_all), i_all.shift, RIGHT * 0.7
                )
                self.play(i_all[2][1].set_value, i, j_all[2][1].set_value, j)
                if j >= 1:
                    self.play(
                        t_up_next_all[1][0][i - 1].set_stroke,
                        {"opacity": 0},
                        t_up_next_all[0][0][i - 1].set_stroke,
                        {"opacity": 0},
                        t_up_next_all[1][0][i].set_stroke,
                        {"opacity": 1},
                        t_up_next_all[0][0][i].set_stroke,
                        {"opacity": 1},
                        t_all[0][j - 1].set_stroke,
                        {"opacity": 0},
                        t_all[0][j].set_stroke,
                        {"opacity": 1},
                    )
                else:
                    self.play(
                        t_up_next_all[1][0][i - 1].set_stroke,
                        {"opacity": 0},
                        t_up_next_all[0][0][i - 1].set_stroke,
                        {"opacity": 0},
                        t_up_next_all[1][0][i].set_stroke,
                        {"opacity": 1},
                        t_up_next_all[0][0][i].set_stroke,
                        {"opacity": 1},
                        t_all[0][j].set_stroke,
                        {"opacity": 1},
                    )
                result_next[i] = j
                self.play(t_up_next_all[1][1][i].set_color, WHITE)
            else:
                if j != -1:
                    self.play(t_all[0][j].set_stroke, {"opacity": 0})
                self.play(
                    MaintainPositionRelativeTo(t_all, invision),
                    invision.shift,
                    RIGHT * 0.7 * (j - result_next[j]),
                )
                j = result_next[j]
                if j >= 0:
                    self.play(
                        t_all[0][j].set_stroke, {"opacity": 1},
                    )
                self.play(j_all[2][1].set_value, j)
        # return result_next


class 供bf参考的gnv(Scene):
    def construct(self):
        # S 串
        s = "abaacababcac"
        length_s = len(s)
        square = Square(color=BLUE, side_length=0.7, stroke_opacity=0)
        s_square = VGroup()
        s_num = VGroup()
        for i in range(length_s):
            s_square.add(square.copy())
            s_num.add(Text("{}".format(s[i])).scale(0.6))
        s_square.arrange(RIGHT, buff=0)
        for i in range(length_s):
            s_num[i].move_to(s_square[i])
        s_rectangle = (
            Rectangle(color=RED, height=0.9, width=0.7 * length_s + 1.8)
            .move_to(s_square.get_center())
            .align_to(s_square, RIGHT)
            .shift(RIGHT * 0.1)
        )
        s_name = (
            Text("SZ |")
            .scale(0.7)
            .move_to(s_rectangle.get_center())
            .align_to(s_rectangle, LEFT)
            .shift(RIGHT * 0.425)
        )
        s_all = VGroup(s_square, s_num, s_rectangle, s_name)
        s_all.move_to(np.array([0, 0, 0]))  # reference
        # self.add(s_all)

        # T 串
        t = "ababc"
        length_t = len(t)
        t_square = VGroup()
        t_num = VGroup()
        for i in range(length_t):
            t_square.add(square.copy())
            t_num.add(Text("{}".format(t[i])).scale(0.6))
        t_square.arrange(RIGHT, buff=0)
        for i in range(length_t):
            t_num[i].move_to(t_square[i])
        t_rectangle = (
            Rectangle(color=RED, height=0.9, width=0.7 * length_t + 1.8)
            .move_to(t_square.get_center())
            .align_to(t_square, RIGHT)
            .shift(RIGHT * 0.1)
        )
        t_name = (
            Text("TZ |")
            .scale(0.7)
            .move_to(t_rectangle.get_center())
            .align_to(t_rectangle, LEFT)
            .shift(RIGHT * 0.425)
        )
        t_all = VGroup(t_square, t_num, t_rectangle, t_name)
        t_all.next_to(s_all, DOWN, buff=0.5)  # reference
        # self.add(t_all)

        # T NextValue(t_up + t_next)
        t_up_all = t_all.copy()
        t_next = t
        t_next_square = t_square.copy()
        t_next_num = VGroup()
        next_ = get_nextval(t)  # T串的NextValue值列表
        for i in range(length_t):
            t_next_num.add(Text("{}".format(next_[i]), color=BLACK).scale(0.6))
            t_next_num[i].move_to(t_next_square[i])
        t_next_rectangle = (
            Rectangle(color=RED, height=0.9, width=0.7 * length_t + 1.8)
            .move_to(t_next_square.get_center())
            .align_to(t_next_square, RIGHT)
            .shift(RIGHT * 0.1)
        )
        t_next_name = (
            Text("Next|")
            .scale(0.7)
            .move_to(t_next_rectangle.get_center())
            .align_to(t_next_rectangle, LEFT)
            .shift(RIGHT * 0.125)
        )
        t_next_all = VGroup(
            t_next_square, t_next_num, t_next_rectangle, t_next_name
        ).next_to(t_up_all, DOWN, buff=0)

        t_up_next_all = VGroup(t_up_all, t_next_all)
        t_up_next_rectangle = Rectangle(
            color=YELLOW, height=1.8, width=0.7 * length_t + 1.8
        ).move_to(t_up_next_all.get_center())
        t_up_next_all.add(t_up_next_rectangle).move_to(np.array([0, 0, 0]))
        t_up_next_line = Line(
            t_up_next_rectangle.get_vertices()[0],
            t_up_next_rectangle.get_vertices()[1],
            color=YELLOW,
        ).move_to(t_up_next_all.get_center())
        t_up_next_all.add(t_up_next_line)
        # self.add(t_up_next_all)

        # i and j
        i_square = Square(color=PURPLE, side_length=1)
        j_square = i_square.copy()
        i_triangle = (
            Triangle(fill_opacity=1, color=YELLOW)
            .scale(0.12)
            .rotate(PI)
            .move_to(i_square.get_center())
            .shift(DOWN * 0.2)
        )
        j_triangle = (
            Triangle(fill_opacity=1, color=YELLOW)
            .scale(0.12)
            .move_to(j_square.get_center())
            .shift(UP * 0.2)
        )
        i_reveal_front = (
            Text("i:", color=WHITE)
            .scale(0.4)
            .move_to(i_square.get_center())
            .shift(UP * 0.21 + LEFT * 0.13)
        )
        i_reveal_value = (
            Integer(0, color=WHITE)
            .scale(0.4)
            .move_to(i_square.get_center())
            .shift(UP * 0.21 + RIGHT * 0.2)
        )
        i_reveal = VGroup(i_reveal_front, i_reveal_value)
        j_reveal_front = (
            Text("j:", color=WHITE)
            .scale(0.4)
            .move_to(j_square.get_center())
            .shift(DOWN * 0.21 + LEFT * 0.13)
        )
        j_reveal_value = (
            Integer(-1, color=WHITE)
            .scale(0.4)
            .move_to(j_square.get_center())
            .shift(DOWN * 0.21 + RIGHT * 0.3)
        )
        j_reveal = VGroup(j_reveal_front, j_reveal_value)
        i_all = VGroup(i_square, i_triangle, i_reveal)
        j_all = VGroup(j_square, j_triangle, j_reveal)
        i_j_all = VGroup(i_all, j_all)
        # self.add(i_j_all)

        # show get_nextval
        # position + updater
        t_up_next_all.move_to(np.array([0, 0, 0]))
        t_all.next_to(t_up_next_all, DOWN, buff=0.15).shift(RIGHT * 0.7)
        invision = square.copy().move_to(t_all[0][0])
        i_all.next_to(t_up_next_all[0][0][0], UP, buff=0.35)
        j_all.next_to(t_all[0][0], DOWN, buff=0.35).align_to(i_all, LEFT)
        # MaintainPositionRelativeTo
        self.add(t_all, t_up_next_all, invision, i_j_all)

        # function
        i = 0
        j = -1
        length = len(t)
        result_next = [0] * length
        result_next[0] = -1
        self.play(t_up_next_all[1][1][0].set_color, WHITE)
        self.play(
            t_up_next_all[1][0][i].set_stroke,
            {"opacity": 1},
            t_up_next_all[0][0][i].set_stroke,
            {"opacity": 1},
        )
        while i < length - 1:
            if j == -1 or t[j] == t[i]:
                i += 1
                j += 1
                self.play(
                    MaintainPositionRelativeTo(
                        j_all, i_all), i_all.shift, RIGHT * 0.7,
                )
                self.play(i_all[2][1].set_value, i, j_all[2][1].set_value, j)
                if t[i] != t[j]:
                    if j >= 1:
                        self.play(
                            t_up_next_all[1][0][i - 1].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[0][0][i - 1].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[1][0][i].set_stroke,
                            {"opacity": 1},
                            t_up_next_all[0][0][i].set_stroke,
                            {"opacity": 1},
                            t_all[0][j - 1].set_stroke,
                            {"opacity": 0},
                            t_all[0][j].set_stroke,
                            {"opacity": 1},
                        )
                    else:
                        self.play(
                            t_up_next_all[1][0][i - 1].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[0][0][i - 1].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[1][0][i].set_stroke,
                            {"opacity": 1},
                            t_up_next_all[0][0][i].set_stroke,
                            {"opacity": 1},
                            t_all[0][j].set_stroke,
                            {"opacity": 1},
                        )
                    result_next[i] = j
                    self.play(t_up_next_all[1][1][i].set_color, WHITE)
                else:
                    self.play(
                        t_up_next_all[1][0][i - 1].set_stroke,
                        {"opacity": 0},
                        t_up_next_all[0][0][i - 1].set_stroke,
                        {"opacity": 0},
                        t_up_next_all[1][0][i].set_stroke,
                        {"opacity": 1},
                        t_up_next_all[0][0][i].set_stroke,
                        {"opacity": 1},
                        t_all[0][j - 1].set_stroke,
                        {"opacity": 0},
                        t_all[0][j].set_stroke,
                        {"opacity": 1},
                    )
                    # 让 result_next[j] 移动到 result_next[i]
                    temp_t_next_num = t_up_next_all[1][1][j].copy()
                    temp_t_next_square = (
                        square.copy()
                        .set_stroke(opacity=0)
                        .move_to(t_up_next_all[1][0][j])
                    )
                    temp_t_next_num_square = VGroup(
                        temp_t_next_num, temp_t_next_square)
                    # temp_t_next_square 先出现
                    self.play(temp_t_next_square.set_stroke, {"opacity": 1})
                    self.play(
                        temp_t_next_num_square.shift, RIGHT * 0.7 * (i - j), run_time=1
                    )
                    result_next[i] = result_next[j]
                    self.play(
                        t_up_next_all[1][1][i].set_color, WHITE,
                    )
                    # temp_t_next_num_square 消失
                    self.play(FadeOut(temp_t_next_num_square), run_time=0.5)
            else:
                if j != -1:
                    self.play(t_all[0][j].set_stroke, {"opacity": 0})
                    self.play(
                        MaintainPositionRelativeTo(t_all, invision),
                        invision.shift,
                        RIGHT * 0.7 * (j - result_next[j]),
                    )
                    j = result_next[j]
                    if j >= 0:
                        self.play(
                            t_all[0][j].set_stroke, {"opacity": 1},
                        )
                    self.play(j_all[2][1].set_value, j)
        # return result_next


class 供bf参考的kmp(Scene):
    def construct(self):
        # S 串
        s = "abaacababcac"
        length_s = len(s)
        square = Square(color=BLUE, side_length=0.7, stroke_opacity=0)
        s_square = VGroup()
        s_num = VGroup()
        for i in range(length_s):
            s_square.add(square.copy())
            s_num.add(Text("{}".format(s[i])).scale(0.6))
        s_square.arrange(RIGHT, buff=0)
        for i in range(length_s):
            s_num[i].move_to(s_square[i])
        s_rectangle = (
            Rectangle(color=RED, height=0.9, width=0.7 * length_s + 1.8)
            .move_to(s_square.get_center())
            .align_to(s_square, RIGHT)
            .shift(RIGHT * 0.1)
        )
        s_name = (
            Text("SZ |")
            .scale(0.7)
            .move_to(s_rectangle.get_center())
            .align_to(s_rectangle, LEFT)
            .shift(RIGHT * 0.425)
        )
        s_all = VGroup(s_square, s_num, s_rectangle, s_name)
        s_all.move_to(np.array([0, 0, 0]))  # reference
        # self.add(s_all)

        # T 串
        t = "ababc"
        length_t = len(t)
        t_square = VGroup()
        t_num = VGroup()
        for i in range(length_t):
            t_square.add(square.copy())
            t_num.add(Text("{}".format(t[i])).scale(0.6))
        t_square.arrange(RIGHT, buff=0)
        for i in range(length_t):
            t_num[i].move_to(t_square[i])
        t_rectangle = (
            Rectangle(color=RED, height=0.9, width=0.7 * length_t + 1.8)
            .move_to(t_square.get_center())
            .align_to(t_square, RIGHT)
            .shift(RIGHT * 0.1)
        )
        t_name = (
            Text("TZ |")
            .scale(0.7)
            .move_to(t_rectangle.get_center())
            .align_to(t_rectangle, LEFT)
            .shift(RIGHT * 0.425)
        )
        t_all = VGroup(t_square, t_num, t_rectangle, t_name)
        t_all.next_to(s_all, DOWN, buff=0.5)  # reference
        # self.add(t_all)

        # T Next(t_up + t_next)
        t_up_all = t_all.copy()
        t_next = t
        t_next_square = t_square.copy()
        t_next_num = VGroup()
        next_ = get_next(t)  # T串的Next值列表
        # next_ = get_nextval(t)  # T串的NextValue值列表
        for i in range(length_t):
            t_next_num.add(Text("{}".format(next_[i]), color=WHITE).scale(0.6))
            t_next_num[i].move_to(t_next_square[i])
        t_next_rectangle = (
            Rectangle(color=RED, height=0.9, width=0.7 * length_t + 1.8)
            .move_to(t_next_square.get_center())
            .align_to(t_next_square, RIGHT)
            .shift(RIGHT * 0.1)
        )
        t_next_name = (
            Text("Next|")
            .scale(0.7)
            .move_to(t_next_rectangle.get_center())
            .align_to(t_next_rectangle, LEFT)
            .shift(RIGHT * 0.125)
        )
        t_next_all = VGroup(
            t_next_square, t_next_num, t_next_rectangle, t_next_name
        ).next_to(t_up_all, DOWN, buff=0)

        t_up_next_all = VGroup(t_up_all, t_next_all)
        t_up_next_rectangle = Rectangle(
            color=YELLOW, height=1.8, width=0.7 * length_t + 1.8
        ).move_to(t_up_next_all.get_center())
        t_up_next_all.add(t_up_next_rectangle).move_to(np.array([0, 0, 0]))
        t_up_next_line = Line(
            t_up_next_rectangle.get_vertices()[0],
            t_up_next_rectangle.get_vertices()[1],
            color=YELLOW,
        ).move_to(t_up_next_all.get_center())
        t_up_next_all.add(t_up_next_line)
        # self.add(t_up_next_all)

        # i and j
        i_square = Square(color=PURPLE, side_length=1)
        j_square = i_square.copy()
        i_triangle = (
            Triangle(fill_opacity=1, color=YELLOW)
            .scale(0.12)
            .rotate(PI)
            .move_to(i_square.get_center())
            .shift(DOWN * 0.2)
        )
        j_triangle = (
            Triangle(fill_opacity=1, color=YELLOW)
            .scale(0.12)
            .move_to(j_square.get_center())
            .shift(UP * 0.2)
        )
        i_reveal_front = (
            Text("i:", color=WHITE)
            .scale(0.4)
            .move_to(i_square.get_center())
            .shift(UP * 0.21 + LEFT * 0.13)
        )
        i_reveal_value = (
            Integer(0, color=WHITE)
            .scale(0.4)
            .move_to(i_square.get_center())
            .shift(UP * 0.21 + RIGHT * 0.2)
        )
        i_reveal = VGroup(i_reveal_front, i_reveal_value)
        j_reveal_front = (
            Text("j:", color=WHITE)
            .scale(0.4)
            .move_to(j_square.get_center())
            .shift(DOWN * 0.21 + LEFT * 0.13)
        )
        j_reveal_value = (
            Integer(0, color=WHITE)
            .scale(0.4)
            .move_to(j_square.get_center())
            .shift(DOWN * 0.21 + RIGHT * 0.2)
        )
        j_reveal = VGroup(j_reveal_front, j_reveal_value)
        i_all = VGroup(i_square, i_triangle, i_reveal)
        j_all = VGroup(j_square, j_triangle, j_reveal)
        i_j_all = VGroup(i_all, j_all)
        # self.add(i_j_all)

        # show kmp
        # position + updater
        s_all.move_to(np.array([0, 0, 0]))
        t_up_next_all.next_to(s_all, DOWN, buff=0.15).align_to(s_all, LEFT)
        invision = square.copy().move_to(t_up_next_all[0][0][0])
        i_all.next_to(s_all[0][0], UP, buff=0.35)
        j_all.next_to(t_up_next_all[1][0][0], DOWN,
                      buff=0.35).align_to(i_all, LEFT)
        # MaintainPositionRelativeTo
        self.add(s_all, t_up_next_all, invision, i_j_all)

        # function
        next_list = next_
        s_length = len(s)
        t_length = len(t)
        i = 0
        j = 0
        self.play(
            s_all[0][i].set_stroke,
            {"opacity": 1},
            t_up_next_all[1][0][i].set_stroke,
            {"opacity": 1},
            t_up_next_all[0][0][i].set_stroke,
            {"opacity": 1},
        )
        while i < s_length and j < t_length:
            if j == -1 or s[i] == t[j]:
                i += 1
                j += 1
                self.play(
                    MaintainPositionRelativeTo(
                        j_all, i_all), i_all.shift, RIGHT * 0.7
                )
                self.play(i_all[2][1].set_value, i, j_all[2][1].set_value, j)
                if j < t_length:
                    self.play(
                        s_all[0][i - 1].set_stroke,
                        {"opacity": 0},
                        s_all[0][i].set_stroke,
                        {"opacity": 1},
                        t_up_next_all[1][0][j - 1].set_stroke,
                        {"opacity": 0},
                        t_up_next_all[0][0][j - 1].set_stroke,
                        {"opacity": 0},
                        t_up_next_all[1][0][j].set_stroke,
                        {"opacity": 1},
                        t_up_next_all[0][0][j].set_stroke,
                        {"opacity": 1},
                    )
            else:
                if j != -1:
                    self.play(
                        t_up_next_all[1][0][j].set_stroke,
                        {"opacity": 0},
                        t_up_next_all[0][0][j].set_stroke,
                        {"opacity": 0},
                    )
                self.play(
                    MaintainPositionRelativeTo(t_up_next_all, invision),
                    invision.shift,
                    RIGHT * 0.7 * (j - next_list[j]),
                )
                j = next_list[j]
                self.play(j_all[2][1].set_value, j)
                if j != -1:
                    self.play(
                        t_up_next_all[1][0][j].set_stroke,
                        {"opacity": 1},
                        t_up_next_all[0][0][j].set_stroke,
                        {"opacity": 1},
                    )
        if j >= t_length:
            pass
            # return i - j
        else:
            pass
            # return -1


class Scene_White(Scene):
    CONFIG = {"camera_config": {
        "background_color": WHITE, "use_plot_depth": True, }}


class kmp(Scene_White):
    def construct(self):
        # Frame 整体框架
        # height: 8  *  width: 14.2
        frame_code = Rectangle(
            color=BLUE, stroke_opacity=0, height=4.5, width=(7.1 + 1),
        ).to_corner(DL, buff=0)
        frame_variable = Rectangle(
            color=RED, stroke_opacity=0, height=4.5, width=(7.1 - 1),
        ).to_corner(DR, buff=0)
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_color=WHITE,
            fill_opacity=1,
            height=3.5,
            width=14.2,
        ).to_corner(UP, buff=0)
        self.add(frame_code, frame_variable, frame_animation)
        self.wait()

        # 代码背景框
        background = RoundedRectangle(
            stroke_width=1,
            stroke_color=GRAY,
            fill_color="#EBEBEB",
            fill_opacity=0.95,
            plot_depth=-1,
            corner_radius=0.05,
            sheen_factor=0.1,
            sheen_direction=UR,
        )
        background.set_height(4, stretch=True).set_width(6.5, stretch=True)
        background.move_to(frame_code)
        self.add(background)

        # frame_code 背景 + 代码 + 移动框
        class codeline_kmp(Text):
            CONFIG = {
                "t2c": {".": WHITE, "t.": BLACK},  # t. 需要和 . 区分开
                "size": 0.37,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        class codeline_gn(Text):
            CONFIG = {
                "t2c": {".": WHITE, "t.": BLACK},  # t. 需要和 . 区分开
                "size": 0.45,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        class codeline_gnv(Text):
            CONFIG = {
                "t2c": {".": WHITE, "t.": BLACK},  # t. 需要和 . 区分开
                "size": 0.37,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        def ignore_space_len(code, str, num):
            origin_len = len(code)
            begin = origin_len - 1
            record = 0
            if str == "bf":
                pass
            elif str == "gn":
                temp_codes = getNext_codes
            elif str == "gnv":
                temp_codes = getNextVal_codes
            elif str == "kmp":
                temp_codes = kmpFind_codes
            for index in range(begin, 0, -1):
                if temp_codes[num][index] == " " and record == 1:
                    if str == "gn":
                        return (origin_len - index - 2) * 0.13
                    elif str == "gnv":
                        return (origin_len - index - 2) * 0.11
                    else:
                        return (origin_len - index - 2) * 0.105
                elif temp_codes[num][index] == " " and record == 0:
                    record = 1
                elif temp_codes[num][index] != " ":
                    record = 0
            if str == "gn":
                return origin_len * 0.13
            elif str == "gnv":
                return origin_len * 0.11
            else:
                return origin_len * 0.105

        background = RoundedRectangle(
            stroke_opacity=0, fill_opacity=0, corner_radius=0.05,
        )
        background.set_height(4.4, stretch=True).set_width(6.5, stretch=True).move_to(
            frame_code
        )

        codes_getNext = (
            VGroup(*[codeline_gn(code) for code in getNext_codes])
            .arrange(DOWN, aligned_edge=LEFT, buff=0.05)
            .next_to(background.get_top(), DOWN, buff=0.2)
            .shift(LEFT * 0.05 + DOWN * 0.15)
        )
        codes_getNextVal = (
            VGroup(*[codeline_gnv(code) for code in getNextVal_codes])
            .arrange(DOWN, aligned_edge=LEFT, buff=0.05)
            .next_to(background.get_top(), DOWN, buff=0.1)
            .shift(LEFT * 0.1 + DOWN * 0.15)
        )
        codes_kmpFind = (
            VGroup(*[codeline_kmp(code) for code in kmpFind_codes])
            .arrange(DOWN, aligned_edge=LEFT, buff=0.05)
            .next_to(background.get_top(), DOWN, buff=0.1)
            .shift(LEFT * 0.1 + DOWN * 0.15)
        )

        # codeline_gn    height: 0.20  *  width: 0.1 * x
        # codeline_gnv   height: 0.25  *  width: 0.1 * x
        # codeline_kmp   height: 0.30  *  width: 0.1 * x
        move_frame = RoundedRectangle(
            stroke_width=2.5,
            stroke_color=BLUE,
            # fill_color=BLUE,
            # fill_opacity=1,
            corner_radius=0.05,
        )

        if chose == 1:
            pass
        elif chose == 2:
            self.add(background)
            self.add(codes_getNext)
        elif chose == 3:
            self.add(background)
            self.add(codes_getNextVal)

        # frame_variable ( SZ | TZ | S.curlength | T.curlength | Next/NextVal | i | j ) 【这个版本是面向过程】
        t2c = {
            "S串": BLUE,
            "T串": BLUE,
            "S.curlength": GOLD,
            "T.curlength": GOLD,
            "Next": PURPLE,
            "NextVal": PURPLE,
            "i": "#ff4e00",
            "j": "#01cd74",
        }
        """
        variable_tittle = (
            Text("变量", font="思源宋体 Heavy", color="#b35c44")
            .scale(1)
            .move_to(frame_variable)
            .align_to(frame_variable, UP)
            .shift(DOWN * 0.2)
        )
        variable_rectangle = Rectangle(color="#003472", height=3.5, width=5.5).next_to(
            variable_tittle, DOWN, buff=0.15
        )
        """
        variable_rectangle = Rectangle(
            color="#003472", height=3.5, width=5.5, stroke_opacity=0).move_to(frame_variable)
        variable_SZ = (
            Text("S串:  " + s, font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(0.7)
            .next_to(variable_rectangle.get_top(), DOWN, buff=0.1)
            .align_to(variable_rectangle, LEFT)
            .shift(RIGHT * 0.2)
        )
        variable_TZ = (
            Text("T串:  " + t, font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(0.7)
            .next_to(variable_SZ, DOWN, buff=0.2)
            .align_to(variable_rectangle, LEFT)
            .shift(RIGHT * 0.2)
        )
        variable_S_curlength = (
            Text(
                "S.curlength:  " + str(len(s)), font="思源宋体 Heavy", t2c=t2c, color=BLACK
            )
            .scale(0.7)
            .next_to(variable_TZ, DOWN, buff=0.2)
            .align_to(variable_rectangle, LEFT)
            .shift(RIGHT * 0.2)
        )
        variable_T_curlength = (
            Text(
                "T.curlength:  " + str(len(t)), font="思源宋体 Heavy", t2c=t2c, color=BLACK
            )
            .scale(0.7)
            .next_to(variable_S_curlength, DOWN, buff=0.2)
            .align_to(variable_rectangle, LEFT)
            .shift(RIGHT * 0.2)
        )
        variable_Next = (
            Text(
                "Next:  " + "".join([(str(x) + " ") for x in get_next(t)]),
                font="思源宋体 Heavy",
                t2c=t2c,
                color=BLACK,
            )
            .scale(0.7)
            .next_to(variable_T_curlength, DOWN, buff=0.2)
            .align_to(variable_rectangle, LEFT)
            .shift(RIGHT * 0.2)
        )
        variable_NextVal = (
            Text(
                "NextVal:   " + "".join([(str(x) + "  ")
                                         for x in get_nextval(t)]),
                font="思源宋体 Heavy",
                t2c=t2c,
                color=BLACK,
            )
            .scale(0.7)
            .next_to(variable_T_curlength, DOWN, buff=0.2)
            .align_to(variable_rectangle, LEFT)
            .shift(RIGHT * 0.2)
        )
        variable_line = (
            Rectangle(color="#003472", height=0.7, width=5.5, stroke_opacity=0)
            .align_to(variable_rectangle, DOWN)
            .align_to(variable_rectangle, LEFT)
        )
        variable_i = (
            Text("i: ", font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(0.8)
            .next_to(variable_NextVal, DOWN, buff=0.35)
            .align_to(variable_rectangle, LEFT)
            .shift(RIGHT * 1.2)
        )
        variable_i_num = (
            Integer(0, color=BLACK).scale(0.8).next_to(
                variable_i, RIGHT, buff=0.1)
        )
        variable_j = (
            Text("j: ", font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(0.8)
            .next_to(variable_i_num, RIGHT, buff=1.5)
        )
        variable_j_num = (
            Integer(-1, color=BLACK).scale(0.8).next_to(variable_j,
                                                        RIGHT, buff=0.1)
        )
        variable_fixed = VGroup(
            variable_rectangle,
            variable_SZ,
            variable_S_curlength,
            variable_TZ,
            variable_T_curlength,
            variable_line,
        )
        if chose == 1:
            pass
        elif chose == 2:
            variable_transform = VGroup(
                variable_Next, variable_i, variable_j, variable_i_num, variable_j_num,
            )
        elif chose == 3:
            variable_transform = VGroup(
                variable_NextVal,
                variable_i,
                variable_j,
                variable_i_num,
                variable_j_num,
            )
        self.add(variable_fixed, variable_transform)

        # frame_animation
        # S 串
        length_s = len(s)
        square = MySquare(
            color=BLUE, side_length=0.45, stroke_opacity=0
        )  # 决定 kmp 动画部分整体大小
        narrow_multiple = square.get_length() / 0.7
        s_square = VGroup()
        s_num = VGroup()
        for i in range(length_s):
            s_square.add(square.copy())
            s_num.add(
                Text("{}".format(s[i]), font="思源宋体 Heavy", color=BLACK).scale(
                    1 * narrow_multiple
                )
            )
        s_square.arrange(RIGHT, buff=0)
        for i in range(length_s):
            s_num[i].move_to(s_square[i])
        s_rectangle = (
            Rectangle(
                color="#f20c00",
                height=0.9 * narrow_multiple,
                width=(0.7 * length_s + 1.8) * narrow_multiple,
            )
            .move_to(s_square.get_center())
            .align_to(s_square, RIGHT)
            .shift(RIGHT * 0.1 * narrow_multiple)
        )
        s_name = (
            Text("S串 |", font="思源宋体 Heavy", color=BLACK)
            .scale(0.95 * narrow_multiple)
            .move_to(s_rectangle.get_center())
            .align_to(s_rectangle, LEFT)
            .shift(RIGHT * 0.425 * narrow_multiple)
        )
        s_all = VGroup(s_square, s_num, s_rectangle, s_name)
        s_all.move_to(np.array([0, 0, 0]))  # reference
        # self.add(s_all)

        # T 串
        length_t = len(t)
        t_square = VGroup()
        t_num = VGroup()
        for i in range(length_t):
            t_square.add(square.copy())
            t_num.add(
                Text("{}".format(t[i]), font="思源宋体 Heavy", color=BLACK).scale(
                    1 * narrow_multiple
                )
            )
        t_square.arrange(RIGHT, buff=0)
        for i in range(length_t):
            t_num[i].move_to(t_square[i])
        t_rectangle = (
            Rectangle(
                color="#f20c00",
                height=0.9 * narrow_multiple,
                width=(0.7 * length_t + 1.8) * narrow_multiple,
            )
            .move_to(t_square.get_center())
            .align_to(t_square, RIGHT)
            .shift(RIGHT * 0.1 * narrow_multiple)
        )
        t_name = (
            Text("T串 |", font="思源宋体 Heavy", color=BLACK)
            .scale(0.95 * narrow_multiple)
            .move_to(t_rectangle.get_center())
            .align_to(t_rectangle, LEFT)
            .shift(RIGHT * 0.425 * narrow_multiple)
        )
        t_all = VGroup(t_square, t_num, t_rectangle, t_name)
        t_all.next_to(s_all, DOWN, buff=0.5 * narrow_multiple)  # reference
        # self.add(t_all)

        # T Next(t_up + t_next)
        t_up_all = t_all.copy()
        t_next = t
        t_next_square = t_square.copy()
        t_next_num = VGroup()
        if chose == 2:
            next_ = get_next(t)  # T串的Next值列表
        elif chose == 3:
            next_ = get_nextval(t)  # T串的NextValue值列表
        for i in range(length_t):
            t_next_num.add(
                Text("{}".format(next_[i]), font="思源宋体 Heavy", color=WHITE).scale(
                    1 * narrow_multiple
                )
            )
            t_next_num[i].move_to(t_next_square[i])
        t_next_rectangle = (
            Rectangle(
                color="#4b5cc4",
                height=0.9 * narrow_multiple,
                width=(0.7 * length_t + 1.8) * narrow_multiple,
            )
            .move_to(t_next_square.get_center())
            .align_to(t_next_square, RIGHT)
            .shift(RIGHT * 0.1 * narrow_multiple)
        )
        t_next_name = (
            Text("Next|", font="思源宋体 Heavy", color=BLACK)
            .scale(1 * narrow_multiple)
            .move_to(t_next_rectangle.get_center())
            .align_to(t_next_rectangle, LEFT)
            .shift(RIGHT * 0.125 * narrow_multiple)
        )
        t_next_all = VGroup(
            t_next_square, t_next_num, t_next_rectangle, t_next_name
        ).next_to(t_up_all, DOWN, buff=0)

        t_up_next_all = VGroup(t_up_all, t_next_all)
        t_up_next_rectangle = Rectangle(
            color="#4b5cc4",
            height=1.8 * narrow_multiple,
            width=(0.7 * length_t + 1.8) * narrow_multiple,
        ).move_to(t_up_next_all.get_center())
        t_up_next_all.add(t_up_next_rectangle).move_to(np.array([0, 0, 0]))
        t_up_next_line = Line(
            t_up_next_rectangle.get_vertices()[0],
            t_up_next_rectangle.get_vertices()[1],
            color="#4b5cc4",
        ).move_to(t_up_next_all.get_center())
        t_up_next_all.add(t_up_next_line)
        # self.add(t_up_next_all)

        # i and j
        i_square = Square(color=PURPLE, side_length=1 * narrow_multiple)
        j_square = i_square.copy()
        i_triangle = (
            Triangle(fill_opacity=1, color="#FFAA00")
            .scale(0.12 * narrow_multiple)
            .rotate(PI)
            .move_to(i_square.get_center())
            .shift(DOWN * 0.2 * narrow_multiple)
        )
        j_triangle = (
            Triangle(fill_opacity=1, color="#FFAA00")
            .scale(0.12 * narrow_multiple)
            .move_to(j_square.get_center())
            .shift(UP * 0.2 * narrow_multiple)
        )
        i_reveal_front = (
            Text("i:", font="思源宋体 Heavy", color=BLACK)
            .scale(0.6 * narrow_multiple)
            .move_to(i_square.get_center())
            .shift(UP * 0.21 * narrow_multiple + LEFT * 0.13 * narrow_multiple)
        )
        i_reveal_value = (
            Integer(0, color=BLACK)
            .scale(0.6 * narrow_multiple)
            .move_to(i_square.get_center())
            .shift(UP * 0.21 * narrow_multiple + RIGHT * 0.15 * narrow_multiple)
        )
        i_reveal = VGroup(i_reveal_front, i_reveal_value)
        j_reveal_front = (
            Text("j:", font="思源宋体 Heavy", color=BLACK)
            .scale(0.6 * narrow_multiple)
            .move_to(j_square.get_center())
            .shift(DOWN * 0.21 * narrow_multiple + LEFT * 0.13 * narrow_multiple)
        )
        if next_[0] == -1:
            j_reveal_value = (
                Integer(-1, color=BLACK)
                .scale(0.6 * narrow_multiple)
                .move_to(j_square.get_center())
                .shift(DOWN * 0.21 * narrow_multiple + RIGHT * 0.25 * narrow_multiple)
            )
        else:
            j_reveal_value = (
                Integer(0, color=BLACK)
                .scale(0.6 * narrow_multiple)
                .move_to(j_square.get_center())
                .shift(DOWN * 0.21 * narrow_multiple + RIGHT * 0.15 * narrow_multiple)
            )
        j_reveal = VGroup(j_reveal_front, j_reveal_value)
        i_all = VGroup(i_square, i_triangle, i_reveal)
        j_all = VGroup(j_square, j_triangle, j_reveal)
        i_j_all = VGroup(i_all, j_all)
        # self.add(i_j_all)

        # position
        kmp_begin_all = VGroup(t_all, t_up_next_all, i_j_all)
        if chose == 1:
            pass
        else:
            kmp_begin_all.move_to(frame_animation.get_center()).align_to(
                frame_animation, LEFT
            ).shift(
                RIGHT * 6 * narrow_multiple + UP * 0
            )  # .shift(RIGHT * 0.5 * narrow_multiple)
            t_all.next_to(t_up_next_all, DOWN, buff=0.15 * narrow_multiple).shift(
                RIGHT * 0.7 * narrow_multiple
            )
            invision = square.copy().move_to(t_all[0][0])
            i_all.next_to(t_up_next_all[0][0][0],
                          UP, buff=0.25 * narrow_multiple)
            j_all.next_to(t_all[0][0], DOWN, buff=0.25 * narrow_multiple).align_to(
                i_all, LEFT
            )
            # MaintainPositionRelativeTo
            self.add(t_all, t_up_next_all, invision, i_j_all)
            self.wait()

        # show getNext and getNextVal function
        if chose == 1:
            pass
        elif chose == 2:

            the_codes = codes_getNext[2]
            move_frame.set_width(
                ignore_space_len(the_codes, "gn", 2), stretch=True
            ).set_height(0.3, stretch=True).move_to(the_codes).align_to(
                the_codes, RIGHT
            ).shift(
                RIGHT * 0.05
            )
            # arrow = SVGMobject(r"D:\manim2\arrow.svg", color=BLACK).scale(0.2)
            arrow = (
                Triangle(stroke_opacity=0, fill_opacity=1, fill_color=RED)
                .scale(0.1)
                .rotate(90 * DEGREES, axis=IN)
            )
            arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))
            self.play(ShowCreation(move_frame), Write(arrow))

            the_codes = codes_getNext[3]
            self.play(
                move_frame.set_width,
                ignore_space_len(the_codes, "gn", 3),  # stretch=True
                move_frame.move_to,
                the_codes,
                move_frame.align_to,
                the_codes,
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.3, "stretch": True},
                run_time=1.5,
            )

            i = 0
            j = -1
            length = len(t)
            result_next = [0] * length
            result_next[0] = -1
            self.play(t_up_next_all[1][1][0].set_color, BLACK)
            self.play(
                t_up_next_all[1][0][i].set_stroke,
                {"opacity": 1},
                t_up_next_all[0][0][i].set_stroke,
                {"opacity": 1},
                t_up_next_all[0][1][0].set_color,
                "#ff7500",
                t_up_next_all[1][1][0].set_color,
                "#ff7500",
            )
            while i < length - 1:
                the_codes = codes_getNext[4]
                self.play(
                    move_frame.set_width,
                    ignore_space_len(the_codes, "gn", 4),
                    move_frame.move_to,
                    the_codes,
                    move_frame.align_to,
                    the_codes,
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.3, "stretch": True},
                    run_time=1.5,
                )
                the_codes = codes_getNext[6]
                self.play(
                    move_frame.set_width,
                    ignore_space_len(the_codes, "gn", 6),
                    move_frame.move_to,
                    the_codes,
                    move_frame.align_to,
                    the_codes,
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.3, "stretch": True},
                    run_time=1.5,
                )
                if j == -1 or t[j] == t[i]:
                    the_codes = codes_getNext[8]
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(the_codes, "gn", 8),
                        move_frame.move_to,
                        the_codes,
                        move_frame.align_to,
                        the_codes,
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.3, "stretch": True},
                        run_time=1.5,
                    )
                    i += 1
                    j += 1
                    self.play(
                        MaintainPositionRelativeTo(j_all, i_all),
                        i_all.shift,
                        RIGHT * 0.7 * narrow_multiple,
                    )
                    # ----------- Integer bug 迫使我加的 -----------
                    if j == -1:
                        j_move_tmp = (
                            Integer(j, color=BLACK)
                            .scale(0.6 * narrow_multiple)
                            .move_to(j_square.get_center())
                            .shift(
                                DOWN * 0.21 * narrow_multiple
                                + RIGHT * 0.25 * narrow_multiple
                            )
                        )
                    else:
                        j_move_tmp = (
                            Integer(j, color=BLACK)
                            .scale(0.6 * narrow_multiple)
                            .move_to(j_square.get_center())
                            .shift(
                                DOWN * 0.21 * narrow_multiple
                                + RIGHT * 0.15 * narrow_multiple
                            )
                        )
                    # ----------- Integer bug 迫使我加的 -----------
                    j_stand_tmp = (
                        Integer(j, color=BLACK)
                        .scale(0.8)
                        .next_to(variable_j, RIGHT, buff=0.1)
                    )
                    # ----------- Integer bug 迫使我加的 -----------
                    self.play(
                        i_all[2][1].set_value,
                        i,
                        i_all[2][1].set_color,
                        BLACK,
                        Transform(j_all[2][1], j_move_tmp),
                        variable_transform[3].set_value,
                        i,
                        variable_transform[3].set_color,
                        BLACK,
                        Transform(variable_transform[4], j_stand_tmp),
                    )
                    the_codes = codes_getNext[9]
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(the_codes, "gn", 9),
                        move_frame.move_to,
                        the_codes,
                        move_frame.align_to,
                        the_codes,
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.3, "stretch": True},
                        run_time=1.5,
                    )
                    if j != 0:
                        self.play(
                            t_up_next_all[1][0][i - 1].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[0][0][i - 1].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[1][0][i].set_stroke,
                            {"opacity": 1},
                            t_up_next_all[0][0][i].set_stroke,
                            {"opacity": 1},
                            t_all[0][j - 1].set_stroke,
                            {"opacity": 0},
                            t_all[0][j].set_stroke,
                            {"opacity": 1},
                            t_up_next_all[0][1][i].set_color,
                            "#ff7500",
                            t_up_next_all[1][1][i].set_color,
                            "#ff7500",
                            t_all[1][j].set_color,
                            "#ff7500",
                            t_up_next_all[0][1][:i].set_color,
                            BLACK,
                            t_up_next_all[0][1][i - j : i].set_color,
                            "#0c8918",
                            t_up_next_all[1][1][:i].set_color,
                            BLACK,
                            t_all[1][:j].set_color,
                            "#9b4400",
                        )
                    else:
                        self.play(
                            t_up_next_all[1][0][i - 1].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[0][0][i - 1].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[1][0][i].set_stroke,
                            {"opacity": 1},
                            t_up_next_all[0][0][i].set_stroke,
                            {"opacity": 1},
                            t_all[0][j].set_stroke,
                            {"opacity": 1},
                            t_up_next_all[0][1][i].set_color,
                            "#ff7500",
                            t_up_next_all[1][1][i].set_color,
                            "#ff7500",
                            t_all[1][j].set_color,
                            "#ff7500",
                            t_up_next_all[0][1][:i].set_color,
                            BLACK,
                            t_up_next_all[0][1][i - j : i].set_color,
                            "#0c8918",
                            t_up_next_all[1][1][:i].set_color,
                            BLACK,
                            t_all[1][:j].set_color,
                            "#9b4400",
                        )
                    result_next[i] = j
                    # self.play(t_up_next_all[1][1][i].set_color, BLACK)
                else:
                    the_codes = codes_getNext[11]
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(the_codes, "gn", 11),
                        move_frame.move_to,
                        the_codes,
                        move_frame.align_to,
                        the_codes,
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.3, "stretch": True},
                        run_time=1.5,
                    )
                    the_codes = codes_getNext[12]
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(the_codes, "gn", 12),
                        move_frame.move_to,
                        the_codes,
                        move_frame.align_to,
                        the_codes,
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.3, "stretch": True},
                        run_time=1.5,
                    )
                    if j != -1 and result_next[j] != -1:
                        self.play(
                            t_all[0][j].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[0][1][i - j : i - result_next[j]].set_color,
                            BLACK,
                            t_all[1][:].set_color,
                            BLACK,
                        )
                    elif j != -1:
                        self.play(
                            t_all[0][j].set_stroke,
                            {"opacity": 0},
                            t_all[1][:].set_color,
                            BLACK,
                        )
                    self.play(
                        MaintainPositionRelativeTo(t_all, invision),
                        invision.shift,
                        RIGHT * 0.7 * (j - result_next[j]) * narrow_multiple,
                    )
                    j = result_next[j]
                    if j >= 0:
                        self.play(
                            t_all[0][j].set_stroke,
                            {"opacity": 1},
                            t_all[1][j].set_color,
                            "#ff7500",
                            t_all[1][:j].set_color,
                            "#9b4400",
                        )
                    # ----------- Integer bug 迫使我加的 -----------
                    if j == -1:
                        j_move_tmp = (
                            Integer(j, color=BLACK)
                            .scale(0.6 * narrow_multiple)
                            .move_to(j_square.get_center())
                            .shift(
                                DOWN * 0.21 * narrow_multiple
                                + RIGHT * 0.25 * narrow_multiple
                            )
                        )
                    else:
                        j_move_tmp = (
                            Integer(j, color=BLACK)
                            .scale(0.6 * narrow_multiple)
                            .move_to(j_square.get_center())
                            .shift(
                                DOWN * 0.21 * narrow_multiple
                                + RIGHT * 0.15 * narrow_multiple
                            )
                        )
                    # ----------- Integer bug 迫使我加的 -----------
                    j_stand_tmp = (
                        Integer(j, color=BLACK)
                        .scale(0.8)
                        .next_to(variable_j, RIGHT, buff=0.1)
                    )
                    # ----------- Integer bug 迫使我加的 -----------
                    self.play(
                        Transform(j_all[2][1], j_move_tmp),
                        Transform(variable_transform[4], j_stand_tmp),
                    )
            # return result_next
            t_all_position = t_all.copy()
            self.play(t_all.shift, RIGHT * 20, run_time=0.5)
            # ----------- Integer bug 迫使我加的 -----------
            i_move_tmp = (
                Integer(0, color=BLACK)
                .scale(0.6 * narrow_multiple)
                .move_to(i_square.get_center())
                .shift(UP * 0.21 * narrow_multiple + RIGHT * 0.15 * narrow_multiple)
            )
            j_move_tmp = (
                Integer(0, color=BLACK)
                .scale(0.6 * narrow_multiple)
                .move_to(j_square.get_center())
                .shift(DOWN * 0.21 * narrow_multiple + RIGHT * 0.15 * narrow_multiple)
            )
            # ----------- Integer bug 迫使我加的 -----------
            i_stand_tmp = (
                Integer(0, color=BLACK).scale(0.8).next_to(variable_i, RIGHT, buff=0.1)
            )
            j_stand_tmp = (
                Integer(0, color=BLACK).scale(0.8).next_to(variable_j, RIGHT, buff=0.1)
            )
            # ----------- Integer bug 迫使我加的 -----------
            if chose == 1:
                pass
            elif chose == 2:
                self.play(
                    Transform(i_all[2][1], i_move_tmp),
                    Transform(j_all[2][1], j_move_tmp),
                    Transform(variable_transform[3], i_stand_tmp),
                    Transform(variable_transform[4], j_stand_tmp),
                    FadeOut(codes_getNext),
                    FadeOut(move_frame),
                    FadeOut(arrow),
                    run_time=0.5,
                )
            elif chose == 3:
                self.play(
                    Transform(i_all[2][1], i_move_tmp),
                    Transform(j_all[2][1], j_move_tmp),
                    Transform(variable_transform[3], i_stand_tmp),
                    Transform(variable_transform[4], j_stand_tmp),
                    FadeOut(codes_getNextVal),
                    FadeOut(move_frame),
                    FadeOut(arrow),
                    run_time=0.5,
                )
            self.play(
                FadeOut(i_j_all),
                FadeOut(variable_transform[3]),
                FadeOut(variable_transform[4]),
                t_up_next_all[1][0][length - 1].set_stroke,
                {"opacity": 0},
                t_up_next_all[0][0][length - 1].set_stroke,
                {"opacity": 0},
                t_up_next_all[0][1][:].set_color,
                BLACK,
                t_up_next_all[1][1][:].set_color,
                BLACK,
            )
            self.play(FadeIn(codes_kmpFind), run_time=0.5)
            self.play(
                t_up_next_all.align_to, t_all_position, DOWN,
            )
        elif chose == 3:

            the_codes = codes_getNextVal[2]
            move_frame.set_width(
                ignore_space_len(the_codes, "gnv", 2), stretch=True
            ).set_height(0.25, stretch=True).move_to(the_codes).align_to(
                the_codes, RIGHT
            ).shift(
                RIGHT * 0.05
            )
            # arrow = SVGMobject(r"D:\manim2\arrow.svg", color=BLACK).scale(0.2)
            arrow = (
                Triangle(stroke_opacity=0, fill_opacity=1, fill_color=RED)
                .scale(0.1)
                .rotate(90 * DEGREES, axis=IN)
            )
            arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))
            self.play(ShowCreation(move_frame), Write(arrow))

            the_codes = codes_getNextVal[3]
            self.play(
                move_frame.set_width,
                ignore_space_len(the_codes, "gnv", 3),  # stretch=True
                move_frame.move_to,
                the_codes,
                move_frame.align_to,
                the_codes,
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.25, "stretch": True},
                run_time=1.5,
            )

            i = 0
            j = -1
            length = len(t)
            result_next = [0] * length
            result_next[0] = -1
            self.play(t_up_next_all[1][1][0].set_color, BLACK)
            self.play(
                t_up_next_all[1][0][i].set_stroke,
                {"opacity": 1},
                t_up_next_all[0][0][i].set_stroke,
                {"opacity": 1},
                t_up_next_all[0][1][0].set_color,
                "#ff7500",
                t_up_next_all[1][1][0].set_color,
                "#ff7500",
            )
            while i < length - 1:
                the_codes = codes_getNextVal[4]
                self.play(
                    move_frame.set_width,
                    ignore_space_len(the_codes, "gnv", 4),
                    move_frame.move_to,
                    the_codes,
                    move_frame.align_to,
                    the_codes,
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.25, "stretch": True},
                    run_time=1.5,
                )
                the_codes = codes_getNextVal[6]
                self.play(
                    move_frame.set_width,
                    ignore_space_len(the_codes, "gnv", 6),
                    move_frame.move_to,
                    the_codes,
                    move_frame.align_to,
                    the_codes,
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.25, "stretch": True},
                    run_time=1.5,
                )
                if j == -1 or t[j] == t[i]:
                    the_codes = codes_getNextVal[8]
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(the_codes, "gnv", 8),
                        move_frame.move_to,
                        the_codes,
                        move_frame.align_to,
                        the_codes,
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.25, "stretch": True},
                        run_time=1.5,
                    )
                    i += 1
                    j += 1
                    self.play(
                        MaintainPositionRelativeTo(j_all, i_all),
                        i_all.shift,
                        RIGHT * 0.7 * narrow_multiple,
                    )
                    # ----------- Integer bug 迫使我加的 -----------
                    if j == -1:
                        j_move_tmp = (
                            Integer(j, color=BLACK)
                            .scale(0.6 * narrow_multiple)
                            .move_to(j_square.get_center())
                            .shift(
                                DOWN * 0.21 * narrow_multiple
                                + RIGHT * 0.25 * narrow_multiple
                            )
                        )
                    else:
                        j_move_tmp = (
                            Integer(j, color=BLACK)
                            .scale(0.6 * narrow_multiple)
                            .move_to(j_square.get_center())
                            .shift(
                                DOWN * 0.21 * narrow_multiple
                                + RIGHT * 0.15 * narrow_multiple
                            )
                        )
                    # ----------- Integer bug 迫使我加的 -----------
                    j_stand_tmp = (
                        Integer(j, color=BLACK)
                        .scale(0.8)
                        .next_to(variable_j, RIGHT, buff=0.1)
                    )
                    # ----------- Integer bug 迫使我加的 -----------
                    self.play(
                        i_all[2][1].set_value,
                        i,
                        i_all[2][1].set_color,
                        BLACK,
                        Transform(j_all[2][1], j_move_tmp),
                        variable_transform[3].set_value,
                        i,
                        variable_transform[3].set_color,
                        BLACK,
                        Transform(variable_transform[4], j_stand_tmp),
                    )
                    the_codes = codes_getNextVal[9]
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(the_codes, "gnv", 9),
                        move_frame.move_to,
                        the_codes,
                        move_frame.align_to,
                        the_codes,
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.25, "stretch": True},
                        run_time=1.5,
                    )
                    if t[i] != t[j]:
                        the_codes = codes_getNextVal[10]
                        self.play(
                            move_frame.set_width,
                            ignore_space_len(the_codes, "gnv", 10),
                            move_frame.move_to,
                            the_codes,
                            move_frame.align_to,
                            the_codes,
                            RIGHT,
                            move_frame.shift,
                            RIGHT * 0.05,
                            move_frame.set_height,
                            {"height": 0.25, "stretch": True},
                            run_time=1.5,
                        )
                        if j != 0:
                            self.play(
                                t_up_next_all[1][0][i - 1].set_stroke,
                                {"opacity": 0},
                                t_up_next_all[0][0][i - 1].set_stroke,
                                {"opacity": 0},
                                t_up_next_all[1][0][i].set_stroke,
                                {"opacity": 1},
                                t_up_next_all[0][0][i].set_stroke,
                                {"opacity": 1},
                                t_all[0][j - 1].set_stroke,
                                {"opacity": 0},
                                t_all[0][j].set_stroke,
                                {"opacity": 1},
                                t_up_next_all[0][1][i].set_color,
                                "#ff7500",
                                t_up_next_all[1][1][i].set_color,
                                "#ff7500",
                                t_all[1][j].set_color,
                                "#ff7500",
                                t_up_next_all[0][1][:i].set_color,
                                BLACK,
                                t_up_next_all[0][1][i - j : i].set_color,
                                "#0c8918",
                                t_up_next_all[1][1][:i].set_color,
                                BLACK,
                                t_all[1][:j].set_color,
                                "#9b4400",
                            )
                        else:
                            self.play(
                                t_up_next_all[1][0][i - 1].set_stroke,
                                {"opacity": 0},
                                t_up_next_all[0][0][i - 1].set_stroke,
                                {"opacity": 0},
                                t_up_next_all[1][0][i].set_stroke,
                                {"opacity": 1},
                                t_up_next_all[0][0][i].set_stroke,
                                {"opacity": 1},
                                t_all[0][j].set_stroke,
                                {"opacity": 1},
                                t_up_next_all[0][1][i].set_color,
                                "#ff7500",
                                t_up_next_all[1][1][i].set_color,
                                "#ff7500",
                                t_all[1][j].set_color,
                                "#ff7500",
                                t_up_next_all[0][1][:i].set_color,
                                BLACK,
                                t_up_next_all[0][1][i - j : i].set_color,
                                "#0c8918",
                                t_up_next_all[1][1][:i].set_color,
                                BLACK,
                                t_all[1][:j].set_color,
                                "#9b4400",
                            )
                        result_next[i] = j
                        # self.play(t_up_next_all[1][1][i].set_color, BLACK)
                    else:
                        the_codes = codes_getNextVal[11]
                        self.play(
                            move_frame.set_width,
                            ignore_space_len(the_codes, "gnv", 11),
                            move_frame.move_to,
                            the_codes,
                            move_frame.align_to,
                            the_codes,
                            RIGHT,
                            move_frame.shift,
                            RIGHT * 0.05,
                            move_frame.set_height,
                            {"height": 0.25, "stretch": True},
                            run_time=1.5,
                        )
                        the_codes = codes_getNextVal[12]
                        self.play(
                            move_frame.set_width,
                            ignore_space_len(the_codes, "gnv", 12),
                            move_frame.move_to,
                            the_codes,
                            move_frame.align_to,
                            the_codes,
                            RIGHT,
                            move_frame.shift,
                            RIGHT * 0.05,
                            move_frame.set_height,
                            {"height": 0.25, "stretch": True},
                            run_time=1.5,
                        )
                        self.play(
                            t_up_next_all[1][0][i - 1].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[0][0][i - 1].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[1][0][i].set_stroke,
                            {"opacity": 1},
                            t_up_next_all[0][0][i].set_stroke,
                            {"opacity": 1},
                            t_all[0][j - 1].set_stroke,
                            {"opacity": 0},
                            t_all[0][j].set_stroke,
                            {"opacity": 1},
                        )
                        self.play(
                            t_up_next_all[0][1][i].set_color,
                            "#ff7500",
                            t_all[1][j].set_color,
                            "#ff7500",
                            t_up_next_all[0][1][:i].set_color,
                            BLACK,
                            t_up_next_all[0][1][i - j : i].set_color,
                            "#0c8918",
                            t_up_next_all[1][1][:i].set_color,
                            BLACK,
                            t_all[1][:j].set_color,
                            "#9b4400",
                        )
                        # 让 result_next[j] 移动到 result_next[i]
                        temp_t_next_num = t_up_next_all[1][1][j].copy()
                        temp_t_next_square = (
                            square.copy()
                            .set_stroke(opacity=0)
                            .move_to(t_up_next_all[1][0][j])
                        )
                        temp_t_next_num_square = VGroup(
                            temp_t_next_num, temp_t_next_square
                        )
                        # temp_t_next_square 先出现
                        self.play(
                            temp_t_next_square.set_stroke,
                            {"opacity": 1},
                            temp_t_next_num.set_color,
                            "#ff7500",
                        )
                        self.play(
                            temp_t_next_num_square.shift,
                            RIGHT * 0.7 * (i - j) * narrow_multiple,
                            run_time=1,
                        )
                        result_next[i] = result_next[j]
                        self.play(
                            t_up_next_all[1][1][i].set_color, "#ff7500",
                        )
                        # temp_t_next_num_square 消失
                        self.play(FadeOut(temp_t_next_num_square), run_time=0.5)
                else:
                    the_codes = codes_getNextVal[14]
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(the_codes, "gnv", 14),
                        move_frame.move_to,
                        the_codes,
                        move_frame.align_to,
                        the_codes,
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.25, "stretch": True},
                        run_time=1.5,
                    )
                    the_codes = codes_getNextVal[15]
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(the_codes, "gnv", 15),
                        move_frame.move_to,
                        the_codes,
                        move_frame.align_to,
                        the_codes,
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.25, "stretch": True},
                        run_time=1.5,
                    )
                    if j != -1 and result_next[j] != -1:
                        self.play(
                            t_all[0][j].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[0][1][i - j : i - result_next[j]].set_color,
                            BLACK,
                            t_all[1][:].set_color,
                            BLACK,
                        )
                    elif j != -1:
                        self.play(
                            t_all[0][j].set_stroke,
                            {"opacity": 0},
                            t_all[1][:].set_color,
                            BLACK,
                        )
                    self.play(
                        MaintainPositionRelativeTo(t_all, invision),
                        invision.shift,
                        RIGHT * 0.7 * (j - result_next[j]) * narrow_multiple,
                    )
                    j = result_next[j]
                    if j >= 0:
                        self.play(
                            t_all[0][j].set_stroke,
                            {"opacity": 1},
                            t_all[1][j].set_color,
                            "#ff7500",
                            t_all[1][:j].set_color,
                            "#9b4400",
                        )
                    # ----------- Integer bug 迫使我加的 -----------
                    if j == -1:
                        j_move_tmp = (
                            Integer(j, color=BLACK)
                            .scale(0.6 * narrow_multiple)
                            .move_to(j_square.get_center())
                            .shift(
                                DOWN * 0.21 * narrow_multiple
                                + RIGHT * 0.25 * narrow_multiple
                            )
                        )
                    else:
                        j_move_tmp = (
                            Integer(j, color=BLACK)
                            .scale(0.6 * narrow_multiple)
                            .move_to(j_square.get_center())
                            .shift(
                                DOWN * 0.21 * narrow_multiple
                                + RIGHT * 0.15 * narrow_multiple
                            )
                        )
                    # ----------- Integer bug 迫使我加的 -----------
                    j_stand_tmp = (
                        Integer(j, color=BLACK)
                        .scale(0.8)
                        .next_to(variable_j, RIGHT, buff=0.1)
                    )
                    # ----------- Integer bug 迫使我加的 -----------
                    self.play(
                        Transform(j_all[2][1], j_move_tmp),
                        Transform(variable_transform[4], j_stand_tmp),
                    )
            # return result_next
            t_all_position = t_all.copy()
            self.play(t_all.shift, RIGHT * 20, run_time=0.5)
            # ----------- Integer bug 迫使我加的 -----------
            i_move_tmp = (
                Integer(0, color=BLACK)
                .scale(0.6 * narrow_multiple)
                .move_to(i_square.get_center())
                .shift(UP * 0.21 * narrow_multiple + RIGHT * 0.15 * narrow_multiple)
            )
            j_move_tmp = (
                Integer(0, color=BLACK)
                .scale(0.6 * narrow_multiple)
                .move_to(j_square.get_center())
                .shift(DOWN * 0.21 * narrow_multiple + RIGHT * 0.15 * narrow_multiple)
            )
            # ----------- Integer bug 迫使我加的 -----------
            i_stand_tmp = (
                Integer(0, color=BLACK).scale(0.8).next_to(variable_i, RIGHT, buff=0.1)
            )
            j_stand_tmp = (
                Integer(0, color=BLACK).scale(0.8).next_to(variable_j, RIGHT, buff=0.1)
            )
            # ----------- Integer bug 迫使我加的 -----------
            if chose == 1:
                pass
            elif chose == 2:
                self.play(
                    Transform(i_all[2][1], i_move_tmp),
                    Transform(j_all[2][1], j_move_tmp),
                    Transform(variable_transform[3], i_stand_tmp),
                    Transform(variable_transform[4], j_stand_tmp),
                    FadeOut(codes_getNext),
                    FadeOut(move_frame),
                    FadeOut(arrow),
                    run_time=0.5,
                )
            elif chose == 3:
                self.play(
                    Transform(i_all[2][1], i_move_tmp),
                    Transform(j_all[2][1], j_move_tmp),
                    Transform(variable_transform[3], i_stand_tmp),
                    Transform(variable_transform[4], j_stand_tmp),
                    FadeOut(codes_getNextVal),
                    FadeOut(move_frame),
                    FadeOut(arrow),
                    run_time=0.5,
                )
            self.play(
                FadeOut(i_j_all),
                FadeOut(variable_transform[3]),
                FadeOut(variable_transform[4]),
                t_up_next_all[1][0][length - 1].set_stroke,
                {"opacity": 0},
                t_up_next_all[0][0][length - 1].set_stroke,
                {"opacity": 0},
                t_up_next_all[0][1][:].set_color,
                BLACK,
                t_up_next_all[1][1][:].set_color,
                BLACK,
            )
            self.play(FadeIn(codes_kmpFind), run_time=0.5)
            self.play(
                t_up_next_all.align_to, t_all_position, DOWN,
            )

        # show kmpFind function
        if chose == 2 or chose == 3:
            # position
            s_all.next_to(t_up_next_all, UP, buff=0.15 * narrow_multiple).align_to(
                t_up_next_all, LEFT
            )
            invision = square.copy().move_to(t_up_next_all[0][0][0])
            i_all.next_to(s_all[0][0], UP, buff=0.25 * narrow_multiple)
            j_all.next_to(
                t_up_next_all[1][0][0], DOWN, buff=0.25 * narrow_multiple
            ).align_to(i_all, LEFT)
            self.play(
                FadeIn(variable_transform[3]),
                FadeIn(variable_transform[4]),
                FadeIn(s_all, LEFT),
                FadeIn(invision),
                FadeIn(i_j_all),
            )

            # function
            the_codes = codes_kmpFind[2]
            move_frame.set_width(
                ignore_space_len(the_codes, "kmp", 2), stretch=True
            ).set_height(0.25, stretch=True).move_to(the_codes).align_to(
                the_codes, RIGHT
            ).shift(
                RIGHT * 0.05
            )
            self.play(ShowCreation(move_frame), Write(arrow))

            the_codes = codes_kmpFind[3]
            self.play(
                move_frame.set_width,
                ignore_space_len(the_codes, "kmp", 3),  # stretch=True
                move_frame.move_to,
                the_codes,
                move_frame.align_to,
                the_codes,
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.25, "stretch": True},
                run_time=1.5,
            )
            the_codes = codes_kmpFind[4]
            self.play(
                move_frame.set_width,
                ignore_space_len(the_codes, "kmp", 4),
                move_frame.move_to,
                the_codes,
                move_frame.align_to,
                the_codes,
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.25, "stretch": True},
                run_time=1.5,
            )

            next_list = next_
            s_length = len(s)
            t_length = len(t)
            i = 0
            j = 0
            self.play(
                s_all[0][i].set_stroke,
                {"opacity": 1},
                t_up_next_all[1][0][i].set_stroke,
                {"opacity": 1},
                t_up_next_all[0][0][i].set_stroke,
                {"opacity": 1},
                t_up_next_all[0][1][0].set_color,
                "#ff7500",
                t_up_next_all[1][1][0].set_color,
                "#ff7500",
                s_all[1][0].set_color,
                "#ff7500",
            )
            the_codes = codes_kmpFind[5]
            self.play(
                move_frame.set_width,
                ignore_space_len(the_codes, "kmp", 5),
                move_frame.move_to,
                the_codes,
                move_frame.align_to,
                the_codes,
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.25, "stretch": True},
                run_time=1.5,
            )
            the_codes = codes_kmpFind[6]
            self.play(
                move_frame.set_width,
                ignore_space_len(the_codes, "kmp", 6),
                move_frame.move_to,
                the_codes,
                move_frame.align_to,
                the_codes,
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.25, "stretch": True},
                run_time=1.5,
            )
            while i < s_length and j < t_length:
                the_codes = codes_kmpFind[7]
                self.play(
                    move_frame.set_width,
                    ignore_space_len(the_codes, "kmp", 7),
                    move_frame.move_to,
                    the_codes,
                    move_frame.align_to,
                    the_codes,
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.25, "stretch": True},
                    run_time=1.5,
                )
                the_codes = codes_kmpFind[9]
                self.play(
                    move_frame.set_width,
                    ignore_space_len(the_codes, "kmp", 9),
                    move_frame.move_to,
                    the_codes,
                    move_frame.align_to,
                    the_codes,
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.25, "stretch": True},
                    run_time=1.5,
                )
                if j == -1 or s[i] == t[j]:
                    the_codes = codes_kmpFind[10]
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(the_codes, "kmp", 10),
                        move_frame.move_to,
                        the_codes,
                        move_frame.align_to,
                        the_codes,
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.25, "stretch": True},
                        run_time=1.5,
                    )
                    i += 1
                    j += 1
                    self.play(
                        MaintainPositionRelativeTo(j_all, i_all),
                        i_all.shift,
                        RIGHT * 0.7 * narrow_multiple,
                    )
                    # ----------- Integer bug 迫使我加的 -----------
                    if j == -1:
                        j_move_tmp = (
                            Integer(j, color=BLACK)
                            .scale(0.6 * narrow_multiple)
                            .move_to(j_square.get_center())
                            .shift(
                                DOWN * 0.21 * narrow_multiple
                                + RIGHT * 0.25 * narrow_multiple
                            )
                        )
                    else:
                        j_move_tmp = (
                            Integer(j, color=BLACK)
                            .scale(0.6 * narrow_multiple)
                            .move_to(j_square.get_center())
                            .shift(
                                DOWN * 0.21 * narrow_multiple
                                + RIGHT * 0.15 * narrow_multiple
                            )
                        )
                    # ----------- Integer bug 迫使我加的 -----------
                    j_stand_tmp = (
                        Integer(j, color=BLACK)
                        .scale(0.8)
                        .next_to(variable_j, RIGHT, buff=0.1)
                    )
                    # ----------- Integer bug 迫使我加的 -----------
                    self.play(
                        i_all[2][1].set_value,
                        i,
                        i_all[2][1].set_color,
                        BLACK,
                        Transform(j_all[2][1], j_move_tmp),
                        variable_transform[3].set_value,
                        i,
                        variable_transform[3].set_color,
                        BLACK,
                        Transform(variable_transform[4], j_stand_tmp),
                    )
                    if j < t_length:
                        self.play(
                            s_all[0][i - 1].set_stroke,
                            {"opacity": 0},
                            s_all[0][i].set_stroke,
                            {"opacity": 1},
                            t_up_next_all[1][0][j - 1].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[0][0][j - 1].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[1][0][j].set_stroke,
                            {"opacity": 1},
                            t_up_next_all[0][0][j].set_stroke,
                            {"opacity": 1},
                            t_up_next_all[0][1][j].set_color,
                            "#ff7500",
                            t_up_next_all[1][1][j].set_color,
                            "#ff7500",
                            s_all[1][i].set_color,
                            "#ff7500",
                            t_up_next_all[0][1][:j].set_color,
                            "#0c8918",
                            t_up_next_all[1][1][:j].set_color,
                            BLACK,
                            s_all[1][: i - j].set_color,
                            BLACK,
                            s_all[1][i - j : i].set_color,
                            "#9b4400",
                        )
                else:
                    the_codes = codes_kmpFind[11]
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(the_codes, "kmp", 11),
                        move_frame.move_to,
                        the_codes,
                        move_frame.align_to,
                        the_codes,
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.25, "stretch": True},
                        run_time=1.5,
                    )
                    the_codes = codes_kmpFind[12]
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(the_codes, "kmp", 12),
                        move_frame.move_to,
                        the_codes,
                        move_frame.align_to,
                        the_codes,
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.25, "stretch": True},
                        run_time=1.5,
                    )
                    if j != -1 and next_list[j] != -1:
                        self.play(
                            t_up_next_all[1][0][j].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[0][0][j].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[0][1][:].set_color,
                            BLACK,
                            t_up_next_all[1][1][:].set_color,
                            BLACK,
                            s_all[1][i - j : i - next_list[j]].set_color,
                            BLACK,
                        )
                    elif j != -1:
                        self.play(
                            t_up_next_all[1][0][j].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[0][0][j].set_stroke,
                            {"opacity": 0},
                            t_up_next_all[0][1][:].set_color,
                            BLACK,
                            t_up_next_all[1][1][:].set_color,
                            BLACK,
                        )
                    self.play(
                        MaintainPositionRelativeTo(t_up_next_all, invision),
                        invision.shift,
                        RIGHT * 0.7 * (j - next_list[j]) * narrow_multiple,
                    )
                    j = next_list[j]
                    # ----------- Integer bug 迫使我加的 -----------
                    if j == -1:
                        j_move_tmp = (
                            Integer(j, color=BLACK)
                            .scale(0.6 * narrow_multiple)
                            .move_to(j_square.get_center())
                            .shift(
                                DOWN * 0.21 * narrow_multiple
                                + RIGHT * 0.25 * narrow_multiple
                            )
                        )
                    else:
                        j_move_tmp = (
                            Integer(j, color=BLACK)
                            .scale(0.6 * narrow_multiple)
                            .move_to(j_square.get_center())
                            .shift(
                                DOWN * 0.21 * narrow_multiple
                                + RIGHT * 0.15 * narrow_multiple
                            )
                        )
                    # ----------- Integer bug 迫使我加的 -----------
                    j_stand_tmp = (
                        Integer(j, color=BLACK)
                        .scale(0.8)
                        .next_to(variable_j, RIGHT, buff=0.1)
                    )
                    # ----------- Integer bug 迫使我加的 -----------
                    self.play(
                        Transform(j_all[2][1], j_move_tmp),
                        Transform(variable_transform[4], j_stand_tmp),
                    )
                    if j != -1:
                        self.play(
                            t_up_next_all[1][0][j].set_stroke,
                            {"opacity": 1},
                            t_up_next_all[0][0][j].set_stroke,
                            {"opacity": 1},
                            t_up_next_all[0][1][j].set_color,
                            "#ff7500",
                            t_up_next_all[1][1][j].set_color,
                            "#ff7500",
                            t_up_next_all[0][1][:j].set_color,
                            "#0c8918",
                        )
            the_codes = codes_kmpFind[14]
            self.play(
                move_frame.set_width,
                ignore_space_len(the_codes, "kmp", 14),
                move_frame.move_to,
                the_codes,
                move_frame.align_to,
                the_codes,
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.25, "stretch": True},
                run_time=1.5,
            )
            the_codes = codes_kmpFind[15]
            self.play(
                move_frame.set_width,
                ignore_space_len(the_codes, "kmp", 15),
                move_frame.move_to,
                the_codes,
                move_frame.align_to,
                the_codes,
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.25, "stretch": True},
                run_time=1.5,
            )
            if j >= t_length:
                # the_codes = codes_kmpFind[15]
                # self.play(
                #     move_frame.set_width,
                #     ignore_space_len(the_codes, "kmp", 15),
                #     move_frame.move_to,
                #     the_codes,
                #     move_frame.align_to,
                #     the_codes,
                #     RIGHT,
                #     move_frame.shift,
                #     RIGHT*0.05,
                #     move_frame.set_height,
                #     {"height": 0.25, "stretch": True},
                #     run_time=1.5,
                # )
                pass
                # return i - j
            else:
                the_codes = codes_kmpFind[16]
                self.play(
                    move_frame.set_width,
                    ignore_space_len(the_codes, "kmp", 16),
                    move_frame.move_to,
                    the_codes,
                    move_frame.align_to,
                    the_codes,
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.25, "stretch": True},
                    run_time=1.5,
                )
                # the_codes = codes_kmpFind[16]
                # self.play(
                #     move_frame.set_width,
                #     ignore_space_len(the_codes, "kmp", 16),
                #     move_frame.move_to,
                #     the_codes,
                #     move_frame.align_to,
                #     the_codes,
                #     RIGHT,
                #     move_frame.shift,
                #     RIGHT*0.05,
                #     move_frame.set_height,
                #     {"height": 0.25, "stretch": True},
                #     run_time=1.5,
                # )
                pass
                # return -1
