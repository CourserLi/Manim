from manimlib.imports import *
from manim_tuan import *

"""
TODO
1: 全部函数皆没有考虑特殊情况
"""

# clear
# traverse
# resize
# insert
# remove
# search
# visit
# inverse

# 自定义串信息()
clear_recs = 4
traverse_recs = 4
resize_recs = 4
insert_recs = 1
remove_recs = 1
search_recs = 1
visit_recs = 1
inverse_recs = 4

clear_codes = [
    "curLength = 0;",
]
traverse_codes = [
    "if (empty())",
    '   cout << "Sequence list is empty";',
    "else {",
    '   cout << "result:";',
    "   for (int i = 0; i < curLength; ++i)",
    "      cout << data[i] << ' ';",
    "   cout << endl;",
    "}",
]
resize_codes = [
    "elemType *p = data;",
    "maxSize *= 2;",
    "data = new elemType[maxSize];",
    "for (int i = 0; i < curLength; ++i)",
    "   data[i] = p[i];",
    "delete[] p;",
]
insert_codes = [
    "if (i < 0 || i > curLength)",
    "    throw outOfRange();",
    "if (curLength == maxSize)",
    "    resize();",
    "for (int j = curLength; j > i; --j)",
    "    data[j] = data[j - 1];",
    "data[i] = value;",
    "++curLength;",
]
remove_codes = [
    "if (i < 0 || i > curLength)",
    "   throw outOfRange();",
    "for (int j = i; j < curLength - 1; ++j)",
    "   data[j] = data[j + 1];",
    "--curLength;",
]
search_codes = [
    "for (int i = 0; i < curLength; ++i)",
    "   if (value == data[i])",
    "      return i;",
    "return -1;",
]
visit_codes = [
    "if (i < 0 || i > curLength)",
    "   throw outOfRange();",
    "return data[i];",
]
inverse_codes = [
    "elemType tmp;",
    "for (int i = 0; i < curLength / 2; ++i) {",
    "   tmp = data[i];",
    "   data[i] = data[curLength - 1 - i];",
    "   data[curLength - 1 - i] = tmp;",
    "}",
]


def skip():
    # 代表运行到一行代码，但动画不发生演示
    whatever = 1


class Scene_White(Scene):
    CONFIG = {"camera_config": {"background_color": WHITE, "use_plot_depth": True,}}


class CodeLine_large(Text):

    CONFIG = {
        "t2c": {
            "linkList": TEAL_D,
            "Node": TEAL_D,
            "head": BLUE_D,
            "while": PINK,
            "NULL": DARK_BLUE,
            "template": DARK_BLUE,
            "void": DARK_BLUE,
            "class": DARK_BLUE,
            "tmp": BLUE_D,
            "p": BLUE_D,
            "q": BLUE_D,
            "next": BLUE_D,
            "delete": PINK,
            "tail": BLUE_D,
            "curLength": BLUE_D,
            "elemType": TEAL_D,
            "clear": YELLOW_B,
            "0": RED_D,
            "1": average_color(BLUE, PINK),
            "2": average_color(BLUE, PINK),
            "3": average_color(BLUE, PINK),
            "4": average_color(BLUE, PINK),
            "5": average_color(BLUE, PINK),
            "6": average_color(BLUE, PINK),
            "7": average_color(BLUE, PINK),
            "8": average_color(BLUE, PINK),
            "9": average_color(BLUE, PINK),
        },
        "font": "Consolas",
        "size": 0.7,
        "color": DARK_GRAY,
        "plot_depth": 2,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class CodeLine_small(Text):

    CONFIG = {
        "t2c": {
            "linkList": TEAL_D,
            "Node": TEAL_D,
            "head": BLUE_D,
            "while": PINK,
            "NULL": DARK_BLUE,
            "template": DARK_BLUE,
            "void": DARK_BLUE,
            "class": DARK_BLUE,
            "tmp": BLUE_D,
            "next": BLUE_D,
            "delete": PINK,
            "tail": BLUE_D,
            "curLength": BLUE_D,
            "elemType": TEAL_D,
            "clear": YELLOW_B,
            "empty": "#9b4400",
            "0": RED_D,
            "1": average_color(BLUE, PINK),
            "2": average_color(BLUE, PINK),
            "3": average_color(BLUE, PINK),
            "4": average_color(BLUE, PINK),
            "5": average_color(BLUE, PINK),
            "6": average_color(BLUE, PINK),
            "7": average_color(BLUE, PINK),
            "8": average_color(BLUE, PINK),
            "9": average_color(BLUE, PINK),
        },
        "font": "Consolas",
        "size": 0.55,
        "color": DARK_GRAY,
        "plot_depth": 2,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class CodeLine_func(Text):

    CONFIG = {
        "t2c": {
            "clear": "#44cef6",
            "traverse": "#ff461f",
            "insert": "#00bc12",
            "remove": "#ff7500",
            "search": "#eacd76",
            "visit": "#725e82",
            "inverse": "#801dae",
            "empty": "#9b4400",
            "size": "#75878a",
            "ally": "#003371",
            "Union": "#cb3a56",
            "resize": "#1bd1a5",
            "getposition": "#725e82",
        },
        "font": "Consolas",
        "size": 0.8,
        "color": DARK_GRAY,
        "plot_depth": 2,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class clear(Scene_White):
    def construct(self):
        # --------------- 代码框架 ---------------
        # 背景板
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
        background.set_height(0.7, stretch=True).set_width(4, stretch=True)
        background.to_corner(UP * 3)
        clear_function = CodeLine_func(
            "clear()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.5)
        codes_clear = VGroup(*[CodeLine_large(code) for code in clear_codes[:]])
        codes_clear.next_to(background.get_top(), DOWN, buff=0.2)

        self.add(background, clear_function, codes_clear)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=5.8,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        square_base = MySquare(color=BLACK, side_length=0.8, stroke_opacity=1)
        # 基准大小
        narrow_multiple = square_base.get_width()
        assert square_base.get_width() * 1.25 == 1
        # 整体 1
        base_1 = VGroup()
        # 方块中的数字 n
        for i in range(6):
            if i < clear_recs:
                n = (
                    Integer(i, color=BLACK)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            else:
                n = (
                    Integer(i, color=WHITE)
                    .set_opacity(0)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            base_1_tmp = VGroup(square_base.copy(), n.copy())
            base_1.add(base_1_tmp.copy())
        base_1.arrange(RIGHT, buff=0)
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # curLength_value
        curLength_value = (
            Integer(clear_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(curLength, RIGHT)
        )
        # 整体 2
        base_2 = VGroup(curLength.copy(), curLength_value.copy())
        # maxSize
        maxSize = TextMobject("maxSize = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # maxSize_value
        maxSize_value = (
            Integer(6, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(maxSize, RIGHT)
        )
        # 整体 3
        base_3 = VGroup(maxSize.copy(), maxSize_value.copy())

        # 各整体的位置
        # 整体 2 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 * (narrow_multiple / 0.8) + UP * 1 * (narrow_multiple / 0.8)
        )
        # 整体 3 在整体 2 下边
        base_3.next_to(base_2, DOWN, buff=0.5 * (narrow_multiple / 0.8)).align_to(
            base_2, LEFT
        )
        # 整体 1 在整体 2 右边
        base_1.next_to(base_2, RIGHT, buff=0.6 * (narrow_multiple / 0.8)).shift(
            DOWN * 0.4 * (narrow_multiple / 0.8) + RIGHT * 1 * (narrow_multiple / 0.8)
        )

        self.add(frame_animation, base_1, base_2, base_3)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(clear_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if clear_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif clear_codes[num][index] == " " and record == 0:
                    record = 1
                elif clear_codes[num][index] != " ":
                    record = 0
            # 返回的单位 不确定
            return origin_len * 0.20

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=3, stroke_color=GOLD, corner_radius=0.05,
        )
        # 代码框移动到第一行代码处
        move_frame.set_width(ignore_space_len(0), stretch=True).set_height(
            0.45, stretch=True
        ).move_to(codes_clear[0]).align_to(codes_clear[0], RIGHT).shift(RIGHT * 0.1)
        # 代码框左边的小三角
        arrow = (
            Triangle(stroke_opacity=0, fill_opacity=1, fill_color=RED)
            .scale(0.13)
            .rotate(90 * DEGREES, axis=IN)
        )
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()

        # 第一行代码
        self.play(base_2[1].set_value, 0)
        self.wait()


class traverse(Scene_White):
    def construct(self):
        # --------------- 代码框架 ---------------
        # 背景板
        background_left = RoundedRectangle(
            stroke_width=1,
            stroke_color=GRAY,
            fill_color="#EBEBEB",
            fill_opacity=0.95,
            plot_depth=-1,
            corner_radius=0.05,
            sheen_factor=0.1,
            sheen_direction=UR,
        )
        background_left.set_height(2.2, stretch=True).set_width(6, stretch=True)
        background_right = background_left.copy()
        background_left.to_corner(UP * 1.5 + LEFT * 2.15)
        background_right.to_corner(UP * 1.5 + RIGHT * 2.15)
        background = VGroup(background_left, background_right)
        traverse_function = CodeLine_func(
            "traverse()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.18)
        codes_traverse_1 = VGroup(
            *[CodeLine_small(code) for code in traverse_codes[:4]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_traverse_1.next_to(background_left.get_top(), DOWN, buff=0.2).shift(
            RIGHT * 0.1
        )
        codes_traverse_2 = VGroup(
            *[CodeLine_small(code) for code in traverse_codes[4:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_traverse_2.next_to(background_right.get_top(), DOWN, buff=0.2).shift(
            RIGHT * 0
        )
        codes_traverse = VGroup(codes_traverse_1, codes_traverse_2)

        self.add(background, traverse_function, codes_traverse)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=5,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        square_base = MySquare(color=BLACK, side_length=0.8, stroke_opacity=1)
        # 基准大小
        narrow_multiple = square_base.get_width()
        assert square_base.get_width() * 1.25 == 1
        # 整体 1
        base_1 = VGroup()
        # 方块中的数字 n
        for i in range(6):
            if i < traverse_recs:
                n = (
                    Integer(i, color=BLACK)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            else:
                n = (
                    Integer(i, color=WHITE)
                    .set_opacity(0)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            base_1_tmp = VGroup(square_base.copy(), n.copy())
            base_1.add(base_1_tmp.copy())
        base_1.arrange(RIGHT, buff=0)
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # curLength_value
        curLength_value = (
            Integer(traverse_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(curLength, RIGHT)
        )
        # 整体 2
        base_2 = VGroup(curLength.copy(), curLength_value.copy())
        # maxSize
        maxSize = TextMobject("maxSize = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # maxSize_value
        maxSize_value = (
            Integer(6, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(maxSize, RIGHT)
        )
        # 整体 3
        base_3 = VGroup(maxSize.copy(), maxSize_value.copy())
        # 箭头(i_up)
        vec_i_up = Arrow(
            np.array([0, -1, 0]),
            np.array([0, 1, 0]),
            buff=0.6 * (narrow_multiple / 0.8),
            color=BLACK,
        ).scale(0.7 * (narrow_multiple / 0.8))
        # i
        i_index = TextMobject("i = ", color=BLACK).scale(0.8 * (narrow_multiple / 0.8))
        # i_value
        i_value = (
            Integer(0, color=BLUE)
            .scale(0.8 * (narrow_multiple / 0.8))
            .next_to(i_index, RIGHT, buff=0.17)
        )
        base_i = VGroup(i_index.copy(), i_value.copy()).next_to(
            vec_i_up, DOWN, buff=0.1 * (narrow_multiple / 0.8)
        )
        # 整体 4
        base_4 = VGroup(vec_i_up.copy(), base_i.copy())
        # 整体 5
        base_5 = square_base.copy()
        base_5.set_opacity(0.5).set_color(BLUE).set_height(0.75).set_width(0.75)

        # 各整体的位置
        # 整体 2 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 * (narrow_multiple / 0.8) + UP * 1 * (narrow_multiple / 0.8)
        )
        # 整体 3 在整体 2 下边
        base_3.next_to(base_2, DOWN, buff=0.5 * (narrow_multiple / 0.8)).align_to(
            base_2, LEFT
        )
        # 整体 1 在整体 2 右边
        base_1.next_to(base_2, RIGHT, buff=0.6 * (narrow_multiple / 0.8)).shift(
            DOWN * 0.4 * (narrow_multiple / 0.8) + RIGHT * 1 * (narrow_multiple / 0.8)
        )
        # 整体 4 在第一个方块的下面
        base_4.next_to(base_1[0], DOWN, buff=0.15 * (narrow_multiple / 0.8))
        # 整体 5 在第一个方块中间
        base_5.move_to(base_1[0])

        self.add(frame_animation, base_1, base_2, base_3)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(traverse_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if traverse_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.16
                elif traverse_codes[num][index] == " " and record == 0:
                    record = 1
                elif traverse_codes[num][index] != " ":
                    record = 0
            # 返回的单位 不确定
            return origin_len * 0.16

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=3, stroke_color=GOLD, corner_radius=0.05,
        )
        # 代码框移动到第一行代码处
        move_frame.set_width(ignore_space_len(0), stretch=True).set_height(
            0.45, stretch=True
        ).move_to(codes_traverse_1[0]).align_to(codes_traverse_1[0], RIGHT).shift(
            RIGHT * 0.1
        )
        # 代码框左边的小三角
        arrow = (
            Triangle(stroke_opacity=0, fill_opacity=1, fill_color=RED)
            .scale(0.13)
            .rotate(90 * DEGREES, axis=IN)
        )
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()

        # 第一行代码
        # empty 代码展示框
        background_tmp = RoundedRectangle(
            stroke_width=1,
            stroke_color=GRAY,
            fill_color="#EBEBEB",
            fill_opacity=0.95,
            plot_depth=-1,
            corner_radius=0.05,
            sheen_factor=0.1,
            sheen_direction=UR,
        )
        background_tmp.set_height(2.2, stretch=True).set_width(4, stretch=True)
        background_tmp.align_to(frame_animation, UP).shift(
            DOWN * 0.3 * (narrow_multiple / 0.8)
        )
        # empty 代码
        empty_codes = [
            "bool empty() const",
            "{",
            "   return curLength == 0;",
            "}",
        ]
        codes_empty = VGroup(
            *[CodeLine_small(code) for code in empty_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_empty.next_to(background_tmp.get_top(), DOWN, buff=0.2)
        # empty 整体
        base_empty = VGroup(background_tmp, codes_empty)
        # empty 整体出现
        self.play(
            GrowFromCenter(base_empty),
            base_2.shift,
            DOWN * 1 * (narrow_multiple / 0.8) + LEFT * 1.4 * (narrow_multiple / 0.8),
            base_3.shift,
            DOWN * 1 * (narrow_multiple / 0.8) + LEFT * 1.4 * (narrow_multiple / 0.8),
            base_1.shift,
            DOWN * 1.2 * (narrow_multiple / 0.8)
            + RIGHT * 0.5 * (narrow_multiple / 0.8),
            run_time=1.5,
        )
        self.wait()
        # empty 整体消失
        self.play(
            FadeOutAndShift(base_empty, UP),
            base_2.shift,
            UP * 1 * (narrow_multiple / 0.8) + RIGHT * 1.4 * (narrow_multiple / 0.8),
            base_3.shift,
            UP * 1 * (narrow_multiple / 0.8) + RIGHT * 1.4 * (narrow_multiple / 0.8),
            base_1.shift,
            UP * 1.2 * (narrow_multiple / 0.8) + LEFT * 0.5 * (narrow_multiple / 0.8),
        )
        self.wait()
        # 第三行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_traverse[0][2],
            move_frame.align_to,
            codes_traverse[0][2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(3),
            move_frame.move_to,
            codes_traverse[0][3],
            move_frame.align_to,
            codes_traverse[0][3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        result = (
            TextMobject("result: ", color=BLACK)
            .next_to(base_3, DOWN, buff=0.1)
            .shift(LEFT * 0.8)
            .scale(0.7)
        )
        self.play(
            Write(result),
            ApplyMethod(base_3.shift, UP * 0.5),
            ApplyMethod(base_2.shift, UP * 0.5),
            run_time=1.5,
        )
        self.wait()
        for circles in range(traverse_recs):
            self.play(
                move_frame.set_width,
                ignore_space_len(4),
                move_frame.move_to,
                codes_traverse[1][0],
                move_frame.align_to,
                codes_traverse[1][0],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            if circles == 0:
                self.play(FadeInFrom(base_4, UP), FadeIn(base_5))
            else:
                self.play(
                    base_4.shift,
                    RIGHT * 0.8 * (narrow_multiple / 0.8),
                    base_5.move_to,
                    base_1[circles],
                )
                self.play(base_4[1][1].set_value, circles, run_time=0.5)
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(5),
                move_frame.move_to,
                codes_traverse[1][1],
                move_frame.align_to,
                codes_traverse[1][1],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            # 方块的数字移动到 result 旁边
            base_1_n_tmp = base_1[circles][1].copy()
            number_result = (
                Integer(circles, color=BLACK)
                .scale(0.85 * (narrow_multiple / 0.8))
                .next_to(result, RIGHT, buff=0.25)
                .shift(RIGHT * 0.55 * circles * (narrow_multiple / 0.8))
            )
            self.play(ReplacementTransform(base_1_n_tmp, number_result))
            self.add(number_result)
            self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(4),
            move_frame.move_to,
            codes_traverse[1][0],
            move_frame.align_to,
            codes_traverse[1][0],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(base_4.shift, RIGHT * 0.8 * (narrow_multiple / 0.8), FadeOut(base_5))
        self.play(base_4[1][1].set_value, traverse_recs, run_time=0.5)
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(6),
            move_frame.move_to,
            codes_traverse[1][2],
            move_frame.align_to,
            codes_traverse[1][2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()


class resize(Scene_White):
    def construct(self):
        # --------------- 代码框架 ---------------
        # 背景板
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
        background.set_height(3.1, stretch=True).set_width(6, stretch=True)
        background.to_corner(UP * 1.5)
        resize_function = CodeLine_func(
            "resize()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.18)
        codes_resize = VGroup(
            *[CodeLine_small(code) for code in resize_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_resize.next_to(background.get_top(), DOWN, buff=0.2).shift(RIGHT * 0.2)

        self.add(background, resize_function, codes_resize)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=4.1,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        square_base = MySquare(color=BLACK, side_length=0.8, stroke_opacity=1)
        # 基准大小
        narrow_multiple = square_base.get_width()
        assert square_base.get_width() * 1.25 == 1
        # 整体 1
        base_1 = VGroup()
        # 方块中的数字 n
        for i in range(6):
            if i < resize_recs:
                n = (
                    Integer(i, color=BLACK)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            else:
                n = (
                    Integer(i, color=WHITE)
                    .set_opacity(0)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            base_1_tmp = VGroup(square_base.copy(), n.copy())
            base_1.add(base_1_tmp.copy())
        base_1.arrange(RIGHT, buff=0)
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # curLength_value
        curLength_value = (
            Integer(resize_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(curLength, RIGHT)
        )
        # 整体 2
        base_2 = VGroup(curLength.copy(), curLength_value.copy())
        # maxSize
        maxSize = TextMobject("maxSize = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # maxSize_value
        maxSize_value = (
            Integer(6, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(maxSize, RIGHT)
        )
        # 整体 3
        base_3 = VGroup(maxSize.copy(), maxSize_value.copy())
        # 箭头(i_up)
        vec_i_up = Arrow(
            np.array([0, -1, 0]),
            np.array([0, 1, 0]),
            buff=0.6 * (narrow_multiple / 0.8),
            color=BLACK,
        ).scale(0.7 * (narrow_multiple / 0.8))
        # i
        i_index = TextMobject("i = ", color=BLACK).scale(0.8 * (narrow_multiple / 0.8))
        # i_value
        i_value = (
            Integer(0, color=BLUE)
            .scale(0.8 * (narrow_multiple / 0.8))
            .next_to(i_index, RIGHT, buff=0.17)
        )
        base_i = VGroup(i_index.copy(), i_value.copy()).next_to(
            vec_i_up, DOWN, buff=0.05 * (narrow_multiple / 0.8)
        )
        # 整体 4
        base_4 = VGroup(vec_i_up.copy(), base_i.copy())
        # 整体 5
        base_5 = square_base.copy()
        base_5.set_opacity(0.5).set_color(BLUE).set_height(0.75).set_width(0.75)

        # 各整体的位置
        # 整体 2 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 * (narrow_multiple / 0.8) + UP * 1 * (narrow_multiple / 0.8)
        )
        # 整体 3 在整体 2 下边
        base_3.next_to(base_2, DOWN, buff=0.5 * (narrow_multiple / 0.8)).align_to(
            base_2, LEFT
        )
        # 整体 1 在整体 2 右边
        base_1.next_to(base_2, RIGHT, buff=0.6 * (narrow_multiple / 0.8)).shift(
            DOWN * 0.4 * (narrow_multiple / 0.8) + RIGHT * 1 * (narrow_multiple / 0.8)
        )
        # 整体 4 在第一个方块的下面
        base_4.next_to(base_1[0], DOWN, buff=0.15 * (narrow_multiple / 0.8))
        # 整体 5 在第一个方块中间
        base_5.move_to(base_1[0])

        self.add(frame_animation, base_1, base_2, base_3)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(resize_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if resize_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.16
                elif resize_codes[num][index] == " " and record == 0:
                    record = 1
                elif resize_codes[num][index] != " ":
                    record = 0
            # 返回的单位 不确定
            return origin_len * 0.16

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=3, stroke_color=GOLD, corner_radius=0.05,
        )
        # 代码框移动到第一行代码处
        move_frame.set_width(ignore_space_len(0), stretch=True).set_height(
            0.45, stretch=True
        ).move_to(codes_resize[0]).align_to(codes_resize[0], RIGHT).shift(RIGHT * 0.1)
        # 代码框左边的小三角
        arrow = (
            Triangle(stroke_opacity=0, fill_opacity=1, fill_color=RED)
            .scale(0.13)
            .rotate(90 * DEGREES, axis=IN)
        )
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()

        # 第一行代码
        self.play(
            base_1.shift,
            RIGHT * 0.7 * (narrow_multiple / 0.8),
            base_2.shift,
            LEFT * 0.7 * (narrow_multiple / 0.8),
            base_3.shift,
            LEFT * 0.7 * (narrow_multiple / 0.8),
        )
        self.wait(0.5)
        # 箭头(data)
        vec_data = Arrow(
            np.array([-1, 0, 0]), np.array([1, 0, 0]), buff=0.6, color=BLACK
        ).scale(0.7)
        # data
        data = (
            TextMobject("data", color=BLACK)
            .scale(0.7)
            .next_to(vec_data, LEFT, buff=0.1)
        )
        # 整体 6
        base_data = VGroup(data, vec_data)
        base_data.next_to(base_1[0], LEFT, buff=0.15)
        self.play(FadeInFrom(base_data, direction=LEFT))
        self.wait()
        # 箭头(p)
        vec_p = Arrow(
            np.array([-1, 0, 0]), np.array([1, 0, 0]), buff=0.6, color=BLACK
        ).scale(0.7)
        # data
        p = TextMobject("p", color=BLACK).scale(0.7).next_to(vec_p, LEFT, buff=0.1)
        # 整体 7
        base_p = VGroup(p, vec_p)
        base_p.next_to(base_1[0], LEFT, buff=0.15).shift(UP * 0.2)
        # 建立一个临时的整体 6
        base_data_tmp = base_data.copy()
        self.play(
            ReplacementTransform(base_data_tmp, base_p), base_data.shift, DOWN * 0.2
        )
        self.wait()
        # 第二行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(1),
            move_frame.move_to,
            codes_resize[1],
            move_frame.align_to,
            codes_resize[1],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(base_3[1].set_value, 12)
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_resize[2],
            move_frame.align_to,
            codes_resize[2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 整体 1 整体 6 整体 7 向左下移动
        base_move_down = VGroup(base_1, base_data, base_p)
        self.play(
            base_2.shift,
            UP * 0.5 + RIGHT * 1.3,
            base_3.shift,
            UP * 1.35 + RIGHT * 5,
            base_move_down.move_to,
            frame_animation,
            base_move_down.shift,
            UP * 0.5,
        )
        self.wait()
        # 整体 8
        base_8 = VGroup()
        for i in range(12):
            base_8.add(square_base.copy())
        base_8.arrange(RIGHT, buff=0)
        base_turn_out = VGroup(base_data.copy(), base_8.copy()).arrange(
            RIGHT, buff=0.15
        )
        base_turn_out.move_to(frame_animation).shift(DOWN * 0.5)
        self.play(base_data.move_to, base_turn_out[0], base_p.shift, DOWN * 0.2)
        base_8.move_to(base_turn_out[1])
        self.play(ShowCreation(base_8))
        self.wait(0.5)
        # 展示方格下面的数字
        display_numbers = VGroup()
        for i in range(12):
            n = (
                Integer(i, color=BLACK)
                .scale(0.5 * (narrow_multiple / 0.8))
                .move_to(square_base)
                .next_to(base_8[i], DOWN, buff=0.2)
            )
            display_numbers.add(n.copy())
        self.play(FadeIn(display_numbers))
        self.wait()
        self.play(FadeOutAndShiftDown(display_numbers))
        self.wait()
        for circles in range(resize_recs):
            self.play(
                move_frame.set_width,
                ignore_space_len(3),
                move_frame.move_to,
                codes_resize[3],
                move_frame.align_to,
                codes_resize[3],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            if circles == 0:
                base_4.next_to(base_8[0], DOWN, buff=0.15 * (narrow_multiple / 0.8))
                base_5.move_to(base_1[0])
                self.play(FadeInFrom(base_4, UP), FadeIn(base_5))
            else:
                self.play(
                    base_4.shift,
                    RIGHT * 0.8 * (narrow_multiple / 0.8),
                    base_5.move_to,
                    base_1[circles],
                )
                self.play(base_4[1][1].set_value, circles, run_time=0.5)
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(4),
                move_frame.move_to,
                codes_resize[4],
                move_frame.align_to,
                codes_resize[4],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            # 上面方块的数字移动到下面方块的数字里面
            base_1_n_tmp = base_1[circles][1].copy()
            self.play(base_1_n_tmp.move_to, base_8[circles])
            self.add(base_1_n_tmp)
            self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(3),
            move_frame.move_to,
            codes_resize[3],
            move_frame.align_to,
            codes_resize[3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(base_4.shift, RIGHT * 0.8 * (narrow_multiple / 0.8), FadeOut(base_5))
        self.play(base_4[1][1].set_value, resize_recs, run_time=0.5)
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(5),
            move_frame.move_to,
            codes_resize[5],
            move_frame.align_to,
            codes_resize[5],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 整体 1 整体 4 整体 5 整体 7 消失
        self.play(
            base_3.shift,
            DOWN * 0.5,
            FadeOut(base_1),
            FadeOut(base_4),
            FadeOut(base_p),
            base_2.shift,
            DOWN * 0.5,
        )
        self.wait()


class insert(Scene_White):
    def construct(self):
        # --------------- 代码框架 ---------------
        # 背景板
        background_left = RoundedRectangle(
            stroke_width=1,
            stroke_color=GRAY,
            fill_color="#EBEBEB",
            fill_opacity=0.95,
            plot_depth=-1,
            corner_radius=0.05,
            sheen_factor=0.1,
            sheen_direction=UR,
        )
        background_left.set_height(2.2, stretch=True).set_width(5.5, stretch=True)
        background_right = background_left.copy()
        background_right.set_height(2.2, stretch=True).set_width(6.5, stretch=True)
        background_left.to_corner(UP * 1.5 + LEFT * 2.65)
        background_right.to_corner(UP * 1.5 + RIGHT * 1.65)
        background = VGroup(background_left, background_right)
        insert_function = CodeLine_func(
            "insert(1, 10)", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.18)
        codes_insert_1 = VGroup(
            *[CodeLine_small(code) for code in insert_codes[:4]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_insert_1.next_to(background_left.get_top(), DOWN, buff=0.2).shift(
            LEFT * 0.1
        )
        codes_insert_2 = VGroup(
            *[CodeLine_small(code) for code in insert_codes[4:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_insert_2.next_to(background_right.get_top(), DOWN, buff=0.2).shift(
            RIGHT * 0
        )
        codes_insert = VGroup(codes_insert_1, codes_insert_2)

        self.add(background, insert_function, codes_insert)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=5,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        square_base = MySquare(color=BLACK, side_length=0.8, stroke_opacity=1)
        # 基准大小
        narrow_multiple = square_base.get_width()
        assert square_base.get_width() * 1.25 == 1
        # 整体 1
        base_1 = VGroup()
        # 方块中的数字 n
        for i in range(6):
            if i < 4:
                n = (
                    Integer(i, color=BLACK)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            else:
                n = (
                    Integer(i, color=WHITE)
                    .set_opacity(0)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            base_1_tmp = VGroup(square_base.copy(), n.copy())
            base_1.add(base_1_tmp.copy())
        base_1.arrange(RIGHT, buff=0)
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # curLength_value
        curLength_value = (
            Integer(4, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(curLength, RIGHT)
        )
        # 整体 2
        base_2 = VGroup(curLength.copy(), curLength_value.copy())
        # maxSize
        maxSize = TextMobject("maxSize = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # maxSize_value
        maxSize_value = (
            Integer(6, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(maxSize, RIGHT)
        )
        # 整体 3
        base_3 = VGroup(maxSize.copy(), maxSize_value.copy())
        # 箭头(j_up)
        vec_j_up = Arrow(
            np.array([0, -1, 0]),
            np.array([0, 1, 0]),
            buff=0.6 * (narrow_multiple / 0.8),
            color=BLACK,
        ).scale(0.7 * (narrow_multiple / 0.8))
        # j
        j_index = TextMobject("j = ", color=BLACK).scale(0.8 * (narrow_multiple / 0.8))
        # j_value
        j_value = (
            Integer(4, color=BLUE)
            .scale(0.8 * (narrow_multiple / 0.8))
            .next_to(j_index, RIGHT, buff=0.17)
        )
        base_j = VGroup(j_index.copy(), j_value.copy()).next_to(
            vec_j_up, DOWN, buff=0.1 * (narrow_multiple / 0.8)
        )
        # 整体 4
        base_4 = VGroup(vec_j_up.copy(), base_j.copy())
        # 整体 5
        base_5 = square_base.copy()
        base_5.set_opacity(0.5).set_color(BLUE).set_height(0.75).set_width(0.75)
        # i
        i_index = TextMobject("i = ", color=BLACK).scale(0.7 * (narrow_multiple / 0.8))
        # i_value
        i_value = (
            Integer(1, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(i_index, RIGHT)
        )
        # 整体 6
        base_6 = VGroup(i_index.copy(), i_value.copy())

        # 各整体的位置
        # 整体 2 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 * (narrow_multiple / 0.8) + UP * 0.5 * (narrow_multiple / 0.8)
        )
        # 整体 3 在整体 2 下边
        base_3.next_to(base_2, DOWN, buff=0.35 * (narrow_multiple / 0.8)).align_to(
            base_2, LEFT
        )
        # 整体 6 在整体 2 上面
        base_6.next_to(base_2, UP, buff=0.35 * (narrow_multiple / 0.8))
        # 整体 1 在整体 2 右边
        base_1.next_to(base_2, RIGHT, buff=0.6 * (narrow_multiple / 0.8)).shift(
            RIGHT * 1 * (narrow_multiple / 0.8)
        )
        # 整体 4 在第一个方块的下面
        base_4.next_to(base_1[4], DOWN, buff=0.15 * (narrow_multiple / 0.8))
        # 整体 5 在第一个方块中间
        base_5.move_to(base_1[4])

        self.add(frame_animation, base_1, base_2, base_3, base_6)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(insert_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if insert_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.16
                elif insert_codes[num][index] == " " and record == 0:
                    record = 1
                elif insert_codes[num][index] != " ":
                    record = 0
            # 返回的单位 不确定
            return origin_len * 0.16

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=3, stroke_color=GOLD, corner_radius=0.05,
        )
        # 代码框移动到第一行代码处
        move_frame.set_width(ignore_space_len(0), stretch=True).set_height(
            0.45, stretch=True
        ).move_to(codes_insert_1[0]).align_to(codes_insert_1[0], RIGHT).shift(
            RIGHT * 0.1
        )
        # 代码框左边的小三角
        arrow = (
            Triangle(stroke_opacity=0, fill_opacity=1, fill_color=RED)
            .scale(0.13)
            .rotate(90 * DEGREES, axis=IN)
        )
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()

        # 第三行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_insert[0][2],
            move_frame.align_to,
            codes_insert[0][2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 右边第一行代码
        for circles in range(4, insert_recs, -1):
            self.play(
                move_frame.set_width,
                ignore_space_len(4),
                move_frame.move_to,
                codes_insert[1][0],
                move_frame.align_to,
                codes_insert[1][0],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            if circles == 4:
                self.play(FadeInFrom(base_4, UP))
            else:
                self.play(base_4.shift, LEFT * 0.8 * (narrow_multiple / 0.8))
                self.play(base_4[1][1].set_value, circles, run_time=0.5)
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(5),
                move_frame.move_to,
                codes_insert[1][1],
                move_frame.align_to,
                codes_insert[1][1],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            base_5.move_to(base_1[circles - 1])
            # 建立一个临时的整体 1 的 n
            base_1_n_tmp = base_1[circles - 1][1].copy()
            self.play(FadeIn(base_5))
            self.play(
                FadeOut(base_1[circles][1]),
                base_1_n_tmp.move_to,
                base_1[circles][1],
                base_5.move_to,
                base_1[circles][1],
            )
            self.play(FadeOut(base_5))
            self.add(base_1_n_tmp)
            self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(4),
            move_frame.move_to,
            codes_insert[1][0],
            move_frame.align_to,
            codes_insert[1][0],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(base_4.shift, LEFT * 0.8 * (narrow_multiple / 0.8))
        self.play(base_4[1][1].set_value, insert_recs, run_time=0.5)
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(6),
            move_frame.move_to,
            codes_insert[1][2],
            move_frame.align_to,
            codes_insert[1][2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 箭头(j_up)
        vec_i_up = Arrow(
            np.array([0, -1, 0]),
            np.array([0, 1, 0]),
            buff=0.6 * (narrow_multiple / 0.8),
            color=BLACK,
        ).scale(0.7 * (narrow_multiple / 0.8))
        # 整体 7
        base_7 = VGroup()
        # i_move
        i_index_2 = TextMobject("i = ", color=BLACK).scale(
            0.8 * (narrow_multiple / 0.8)
        )
        base_7.add(vec_j_up.copy())
        base_7.add(i_index_2.copy())
        base_7.add(j_value.copy())
        base_7[2].set_value(insert_recs).next_to(base_7[1], RIGHT, buff=0.17)
        base_i = VGroup(base_7[1], base_7[2]).next_to(
            base_7[0], DOWN, buff=0.1 * (narrow_multiple / 0.8)
        )
        base_7.next_to(base_1[insert_recs], DOWN, buff=0.15 * (narrow_multiple / 0.8))
        base_5.move_to(base_1[insert_recs])
        # 整体 4 消失  整体 5 整体 7 出现
        self.play(FadeOut(base_4))
        self.play(FadeInFrom(base_7, UP), FadeIn(base_5))
        self.wait()
        # 建立一个临时的整体 1 的 n
        base_1_n_tmp = (
            base_1[insert_recs][1].copy().set_value(10).move_to(base_1[insert_recs])
        )
        self.play(Transform(base_1[insert_recs][1], base_1_n_tmp))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(7),
            move_frame.move_to,
            codes_insert[1][3],
            move_frame.align_to,
            codes_insert[1][3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(base_2[1].set_value, 5)
        self.wait()
        self.play(FadeOut(base_5), FadeOut(base_7))
        self.wait()


class remove(Scene_White):
    def construct(self):
        # --------------- 代码框架 ---------------
        # 背景板
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
        background.set_height(3.1, stretch=True).set_width(8.2, stretch=True)
        background.to_corner(UP * 1.5)
        remove_function = CodeLine_func(
            "remove(1)", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.18)
        codes_remove = VGroup(
            *[CodeLine_large(code) for code in remove_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_remove.next_to(background.get_top(), DOWN, buff=0.2).shift(RIGHT * 0.2)

        self.add(background, remove_function, codes_remove)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=4.1,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        square_base = MySquare(color=BLACK, side_length=0.8, stroke_opacity=1)
        # 基准大小
        narrow_multiple = square_base.get_width()
        assert square_base.get_width() * 1.25 == 1
        # 整体 1
        base_1 = VGroup()
        # 方块中的数字 n
        for i in range(6):
            if i < 4:
                n = (
                    Integer(i, color=BLACK)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            else:
                n = (
                    Integer(i, color=WHITE)
                    .set_opacity(0)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            base_1_tmp = VGroup(square_base.copy(), n.copy())
            base_1.add(base_1_tmp.copy())
        base_1.arrange(RIGHT, buff=0)
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # curLength_value
        curLength_value = (
            Integer(4, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(curLength, RIGHT)
        )
        # 整体 2
        base_2 = VGroup(curLength.copy(), curLength_value.copy())
        # maxSize
        maxSize = TextMobject("maxSize = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # maxSize_value
        maxSize_value = (
            Integer(6, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(maxSize, RIGHT)
        )
        # 整体 3
        base_3 = VGroup(maxSize.copy(), maxSize_value.copy())
        # 箭头(j_up)
        vec_j_up = Arrow(
            np.array([0, -1, 0]),
            np.array([0, 1, 0]),
            buff=0.6 * (narrow_multiple / 0.8),
            color=BLACK,
        ).scale(0.7 * (narrow_multiple / 0.8))
        # j
        j_index = TextMobject("j = ", color=BLACK).scale(0.8 * (narrow_multiple / 0.8))
        # j_value
        j_value = (
            Integer(remove_recs, color=BLUE)
            .scale(0.8 * (narrow_multiple / 0.8))
            .next_to(j_index, RIGHT, buff=0.17)
        )
        base_j = VGroup(j_index.copy(), j_value.copy()).next_to(
            vec_j_up, DOWN, buff=0.1 * (narrow_multiple / 0.8)
        )
        # 整体 4
        base_4 = VGroup(vec_j_up.copy(), base_j.copy())
        # 整体 5
        base_5 = square_base.copy()
        base_5.set_opacity(0.5).set_color(BLUE).set_height(0.75).set_width(0.75)
        # i
        i_index = TextMobject("i = ", color=BLACK).scale(0.7 * (narrow_multiple / 0.8))
        # i_value
        i_value = (
            Integer(remove_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(i_index, RIGHT)
        )
        # 整体 6
        base_6 = VGroup(i_index.copy(), i_value.copy())

        # 各整体的位置
        # 整体 2 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 * (narrow_multiple / 0.8) + UP * 0.5 * (narrow_multiple / 0.8)
        )
        # 整体 3 在整体 2 下边
        base_3.next_to(base_2, DOWN, buff=0.35 * (narrow_multiple / 0.8)).align_to(
            base_2, LEFT
        )
        # 整体 6 在整体 2 上面
        base_6.next_to(base_2, UP, buff=0.35 * (narrow_multiple / 0.8))
        # 整体 1 在整体 2 右边
        base_1.next_to(base_2, RIGHT, buff=0.6 * (narrow_multiple / 0.8)).shift(
            RIGHT * 1 * (narrow_multiple / 0.8)
        )
        # 整体 4 在第一个方块的下面
        base_4.next_to(base_1[remove_recs], DOWN, buff=0.15 * (narrow_multiple / 0.8))
        # 整体 5 在第一个方块中间
        base_5.move_to(base_1[4])

        self.add(frame_animation, base_1, base_2, base_3, base_6)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(remove_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if remove_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif remove_codes[num][index] == " " and record == 0:
                    record = 1
                elif remove_codes[num][index] != " ":
                    record = 0
            # 返回的单位 不确定
            return origin_len * 0.20

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=3, stroke_color=GOLD, corner_radius=0.05,
        )
        # 代码框移动到第一行代码处
        move_frame.set_width(ignore_space_len(0), stretch=True).set_height(
            0.45, stretch=True
        ).move_to(codes_remove[0]).align_to(codes_remove[0], RIGHT).shift(RIGHT * 0.1)
        # 代码框左边的小三角
        arrow = (
            Triangle(stroke_opacity=0, fill_opacity=1, fill_color=RED)
            .scale(0.13)
            .rotate(90 * DEGREES, axis=IN)
        )
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()

        # 开局 for 循环
        for circles in range(remove_recs, 3):
            self.play(
                move_frame.set_width,
                ignore_space_len(2),
                move_frame.move_to,
                codes_remove[2],
                move_frame.align_to,
                codes_remove[2],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            if circles == remove_recs:
                self.play(FadeInFrom(base_4, UP))
            else:
                self.play(base_4.shift, RIGHT * 0.8 * (narrow_multiple / 0.8))
                self.play(base_4[1][1].set_value, circles, run_time=0.5)
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(3),
                move_frame.move_to,
                codes_remove[3],
                move_frame.align_to,
                codes_remove[3],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            base_5.move_to(base_1[circles + 1])
            # 建立一个临时的整体 1 的 n
            base_1_n_tmp = base_1[circles + 1][1].copy()
            self.play(FadeIn(base_5))
            self.play(
                FadeOut(base_1[circles][1]),
                base_1_n_tmp.move_to,
                base_1[circles][1],
                base_5.move_to,
                base_1[circles][1],
            )
            self.play(FadeOut(base_5))
            self.add(base_1_n_tmp)
            self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_remove[2],
            move_frame.align_to,
            codes_remove[2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(base_4.shift, RIGHT * 0.8 * (narrow_multiple / 0.8))
        self.play(base_4[1][1].set_value, 3, run_time=0.5)
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(4),
            move_frame.move_to,
            codes_remove[4],
            move_frame.align_to,
            codes_remove[4],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(base_2[1].set_value, 3)
        self.wait()


class search(Scene_White):
    def construct(self):
        # --------------- 代码框架 ---------------
        # 背景板
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
        background.set_height(2.3, stretch=True).set_width(7.5, stretch=True)
        background.to_corner(UP * 2)
        search_function = CodeLine_func(
            "search(1)", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.3)
        codes_search = VGroup(
            *[CodeLine_large(code) for code in search_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_search.next_to(background.get_top(), DOWN, buff=0.2).shift(RIGHT * 0.2)

        self.add(background, search_function, codes_search)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=4.7,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        square_base = MySquare(color=BLACK, side_length=0.8, stroke_opacity=1)
        # 基准大小
        narrow_multiple = square_base.get_width()
        assert square_base.get_width() * 1.25 == 1
        # 整体 1
        base_1 = VGroup()
        # 方块中的数字 n
        for i in range(6):
            if i < 4:
                n = (
                    Integer(i, color=BLACK)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            else:
                n = (
                    Integer(i, color=WHITE)
                    .set_opacity(0)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            base_1_tmp = VGroup(square_base.copy(), n.copy())
            base_1.add(base_1_tmp.copy())
        base_1.arrange(RIGHT, buff=0)
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # curLength_value
        curLength_value = (
            Integer(4, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(curLength, RIGHT)
        )
        # 整体 2
        base_2 = VGroup(curLength.copy(), curLength_value.copy())
        # maxSize
        maxSize = TextMobject("maxSize = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # maxSize_value
        maxSize_value = (
            Integer(6, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(maxSize, RIGHT)
        )
        # 整体 3
        base_3 = VGroup(maxSize.copy(), maxSize_value.copy())
        # 箭头(i_up)
        vec_i_up = Arrow(
            np.array([0, -1, 0]),
            np.array([0, 1, 0]),
            buff=0.6 * (narrow_multiple / 0.8),
            color=BLACK,
        ).scale(0.7 * (narrow_multiple / 0.8))
        # i
        i_index = TextMobject("i = ", color=BLACK).scale(0.8 * (narrow_multiple / 0.8))
        # i_value
        i_value = (
            Integer(0, color=BLUE)
            .scale(0.8 * (narrow_multiple / 0.8))
            .next_to(i_index, RIGHT, buff=0.17)
        )
        base_i = VGroup(i_index.copy(), i_value.copy()).next_to(
            vec_i_up, DOWN, buff=0.1 * (narrow_multiple / 0.8)
        )
        # 整体 4
        base_4 = VGroup(vec_i_up.copy(), base_i.copy())
        # 整体 5
        base_5 = square_base.copy()
        base_5.set_opacity(0.5).set_color(BLUE).set_height(0.75).set_width(0.75)
        # value
        value_index = TextMobject("value = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # value_value
        value_value = (
            Integer(search_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(value_index, RIGHT)
        )
        # 整体 6
        base_6 = VGroup(value_index.copy(), value_value.copy())

        # 各整体的位置
        # 整体 2 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 * (narrow_multiple / 0.8) + UP * 0.5 * (narrow_multiple / 0.8)
        )
        # 整体 3 在整体 2 下边
        base_3.next_to(base_2, DOWN, buff=0.35 * (narrow_multiple / 0.8)).align_to(
            base_2, LEFT
        )
        # 整体 6 在整体 2 上面
        base_6.next_to(base_2, UP, buff=0.35 * (narrow_multiple / 0.8)).align_to(
            base_2, LEFT
        )
        # 整体 1 在整体 2 右边
        base_1.next_to(base_2, RIGHT, buff=0.6 * (narrow_multiple / 0.8)).shift(
            RIGHT * 1 * (narrow_multiple / 0.8)
        )
        # 整体 4 在第一个方块的下面
        base_4.next_to(base_1[0], DOWN, buff=0.15 * (narrow_multiple / 0.8))
        # 整体 5 在第一个方块中间
        base_5.move_to(base_1[0])

        self.add(frame_animation, base_1, base_2, base_3, base_6)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(search_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if search_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif search_codes[num][index] == " " and record == 0:
                    record = 1
                elif search_codes[num][index] != " ":
                    record = 0
            # 返回的单位 不确定
            return origin_len * 0.20

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=3, stroke_color=GOLD, corner_radius=0.05,
        )
        # 代码框移动到第一行代码处
        move_frame.set_width(ignore_space_len(0), stretch=True).set_height(
            0.45, stretch=True
        ).move_to(codes_search[0]).align_to(codes_search[0], RIGHT).shift(RIGHT * 0.1)
        # 代码框左边的小三角
        arrow = (
            Triangle(stroke_opacity=0, fill_opacity=1, fill_color=RED)
            .scale(0.13)
            .rotate(90 * DEGREES, axis=IN)
        )
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()

        # 开局 for 循环
        for circles in range(search_recs + 1):
            if circles != 0:
                self.play(
                    move_frame.set_width,
                    ignore_space_len(0),
                    move_frame.move_to,
                    codes_search[0],
                    move_frame.align_to,
                    codes_search[0],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.1,
                    move_frame.set_height,
                    {"height": 0.45, "stretch": True},
                    run_time=1,
                )
                self.wait()
            if circles == 0:
                self.play(FadeInFrom(base_4, UP), FadeIn(base_5))
            else:
                self.play(
                    base_4.shift,
                    RIGHT * 0.8 * (narrow_multiple / 0.8),
                    base_5.move_to,
                    base_1[circles],
                )
                self.play(base_4[1][1].set_value, circles, run_time=0.5)
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(1),
                move_frame.move_to,
                codes_search[1],
                move_frame.align_to,
                codes_search[1],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            if circles == search_recs:
                self.play(
                    move_frame.set_width,
                    ignore_space_len(2),
                    move_frame.move_to,
                    codes_search[2],
                    move_frame.align_to,
                    codes_search[2],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.1,
                    move_frame.set_height,
                    {"height": 0.45, "stretch": True},
                    run_time=1,
                )
                self.wait()


class visit(Scene_White):
    def construct(self):
        # --------------- 代码框架 ---------------
        # 背景板
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
        background.set_height(2, stretch=True).set_width(6, stretch=True)
        background.to_corner(UP * 2)
        visit_function = CodeLine_func(
            "visit(1)", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.35)
        codes_visit = VGroup(
            *[CodeLine_large(code) for code in visit_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_visit.next_to(background.get_top(), DOWN, buff=0.2).shift(RIGHT * 0.2)

        self.add(background, visit_function, codes_visit)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=5,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        square_base = MySquare(color=BLACK, side_length=0.8, stroke_opacity=1)
        # 基准大小
        narrow_multiple = square_base.get_width()
        assert square_base.get_width() * 1.25 == 1
        # 整体 1
        base_1 = VGroup()
        # 方块中的数字 n
        for i in range(6):
            if i < 4:
                n = (
                    Integer(i, color=BLACK)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            else:
                n = (
                    Integer(i, color=WHITE)
                    .set_opacity(0)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            base_1_tmp = VGroup(square_base.copy(), n.copy())
            base_1.add(base_1_tmp.copy())
        base_1.arrange(RIGHT, buff=0)
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # curLength_value
        curLength_value = (
            Integer(4, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(curLength, RIGHT)
        )
        # 整体 2
        base_2 = VGroup(curLength.copy(), curLength_value.copy())
        # maxSize
        maxSize = TextMobject("maxSize = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # maxSize_value
        maxSize_value = (
            Integer(6, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(maxSize, RIGHT)
        )
        # 整体 3
        base_3 = VGroup(maxSize.copy(), maxSize_value.copy())
        # 箭头(j_up)
        vec_j_up = Arrow(
            np.array([0, -1, 0]),
            np.array([0, 1, 0]),
            buff=0.6 * (narrow_multiple / 0.8),
            color=BLACK,
        ).scale(0.7 * (narrow_multiple / 0.8))
        # j
        j_index = TextMobject("j = ", color=BLACK).scale(0.8 * (narrow_multiple / 0.8))
        # j_value
        j_value = (
            Integer(visit_recs, color=BLUE)
            .scale(0.8 * (narrow_multiple / 0.8))
            .next_to(j_index, RIGHT, buff=0.17)
        )
        base_j = VGroup(j_index.copy(), j_value.copy()).next_to(
            vec_j_up, DOWN, buff=0.1 * (narrow_multiple / 0.8)
        )
        # 整体 4
        base_4 = VGroup(vec_j_up.copy(), base_j.copy())
        # 整体 5
        base_5 = square_base.copy()
        base_5.set_opacity(0.5).set_color(BLUE).set_height(0.75).set_width(0.75)
        # i
        i_index = TextMobject("i = ", color=BLACK).scale(0.7 * (narrow_multiple / 0.8))
        # i_value
        i_value = (
            Integer(visit_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(i_index, RIGHT)
        )
        # 整体 6
        base_6 = VGroup(i_index.copy(), i_value.copy())

        # 各整体的位置
        # 整体 2 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 * (narrow_multiple / 0.8) + UP * 0.5 * (narrow_multiple / 0.8)
        )
        # 整体 3 在整体 2 下边
        base_3.next_to(base_2, DOWN, buff=0.35 * (narrow_multiple / 0.8)).align_to(
            base_2, LEFT
        )
        # 整体 6 在整体 2 上面
        base_6.next_to(base_2, UP, buff=0.35 * (narrow_multiple / 0.8))
        # 整体 1 在整体 2 右边
        base_1.next_to(base_2, RIGHT, buff=0.6 * (narrow_multiple / 0.8)).shift(
            RIGHT * 1 * (narrow_multiple / 0.8)
        )
        # 整体 4 在第一个方块的下面
        base_4.next_to(base_1[visit_recs], DOWN, buff=0.15 * (narrow_multiple / 0.8))
        # 整体 5 在第一个方块中间
        base_5.move_to(base_1[visit_recs])

        self.add(frame_animation, base_1, base_2, base_3, base_6)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(visit_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if visit_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif visit_codes[num][index] == " " and record == 0:
                    record = 1
                elif visit_codes[num][index] != " ":
                    record = 0
            # 返回的单位 不确定
            return origin_len * 0.20

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=3, stroke_color=GOLD, corner_radius=0.05,
        )
        # 代码框移动到第一行代码处
        move_frame.set_width(ignore_space_len(0), stretch=True).set_height(
            0.45, stretch=True
        ).move_to(codes_visit[0]).align_to(codes_visit[0], RIGHT).shift(RIGHT * 0.1)
        # 代码框左边的小三角
        arrow = (
            Triangle(stroke_opacity=0, fill_opacity=1, fill_color=RED)
            .scale(0.13)
            .rotate(90 * DEGREES, axis=IN)
        )
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()

        # 第三行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_visit[2],
            move_frame.align_to,
            codes_visit[2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(FadeIn(base_5))
        self.wait()


class inverse(Scene_White):
    def construct(self):
        # --------------- 代码框架 ---------------
        # 背景板
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
        background.set_height(3.1, stretch=True).set_width(7.2, stretch=True)
        background.to_corner(UP * 1.5)
        inverse_function = CodeLine_func(
            "inverse()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.18)
        codes_inverse = VGroup(
            *[CodeLine_small(code) for code in inverse_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_inverse.next_to(background.get_top(), DOWN, buff=0.2).shift(RIGHT * 0.2)

        self.add(background, inverse_function, codes_inverse)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=4.1,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        square_base = MySquare(color=BLACK, side_length=0.8, stroke_opacity=1)
        # 基准大小
        narrow_multiple = square_base.get_width()
        assert square_base.get_width() * 1.25 == 1
        # 整体 1
        base_1 = VGroup()
        # 方块中的数字 n
        for i in range(6):
            if i < inverse_recs:
                n = (
                    Integer(i, color=BLACK)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            else:
                n = (
                    Integer(i, color=WHITE)
                    .set_opacity(0)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            base_1_tmp = VGroup(square_base.copy(), n.copy())
            base_1.add(base_1_tmp.copy())
        base_1.arrange(RIGHT, buff=0)
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # curLength_value
        curLength_value = (
            Integer(inverse_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(curLength, RIGHT)
        )
        # 整体 2
        base_2 = VGroup(curLength.copy(), curLength_value.copy())
        # maxSize
        maxSize = TextMobject("maxSize = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # maxSize_value
        maxSize_value = (
            Integer(6, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(maxSize, RIGHT)
        )
        # 整体 3
        base_3 = VGroup(maxSize.copy(), maxSize_value.copy())
        # 箭头(i_up)
        vec_i_up = Arrow(
            np.array([0, -1, 0]),
            np.array([0, 1, 0]),
            buff=0.6 * (narrow_multiple / 0.8),
            color=BLACK,
        ).scale(0.7 * (narrow_multiple / 0.8))
        # i
        i_index = TextMobject("i = ", color=BLACK).scale(0.8 * (narrow_multiple / 0.8))
        # i_value
        i_value = (
            Integer(0, color=BLUE)
            .scale(0.8 * (narrow_multiple / 0.8))
            .next_to(i_index, RIGHT, buff=0.17)
        )
        base_i = VGroup(i_index.copy(), i_value.copy()).next_to(
            vec_i_up, DOWN, buff=0.05 * (narrow_multiple / 0.8)
        )
        # 整体 4
        base_4 = VGroup(vec_i_up.copy(), base_i.copy())
        # 整体 5
        base_5 = square_base.copy()
        base_5.set_opacity(0.5).set_color(BLUE).set_height(0.75).set_width(0.75)
        # tmp
        tmp = TextMobject("tmp = ", color=BLACK).scale(0.7 * (narrow_multiple / 0.8))
        # tmp_value
        tmp_value = (
            Integer(0, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(tmp, RIGHT)
        )
        # 整体 6
        base_6 = VGroup(tmp.copy(), tmp_value.copy())

        # 各整体的位置
        # 整体 2 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 * (narrow_multiple / 0.8) + UP * 1 * (narrow_multiple / 0.8)
        )
        # 整体 3 在整体 2 下边
        base_3.next_to(base_2, DOWN, buff=0.5 * (narrow_multiple / 0.8)).align_to(
            base_2, LEFT
        )
        # 整体 1 在整体 2 右边
        base_1.next_to(base_2, RIGHT, buff=0.6 * (narrow_multiple / 0.8)).shift(
            DOWN * 0.4 * (narrow_multiple / 0.8) + RIGHT * 1 * (narrow_multiple / 0.8)
        )
        # 整体 4 在第一个方块的下面
        base_4.next_to(base_1[0], DOWN, buff=0.15 * (narrow_multiple / 0.8))
        # 整体 5 在第一个方块中间
        base_5.move_to(base_1[0])
        # 整体 6 在所有方块中间下面
        base_6.next_to(base_1, UP, buff=0.4 * (narrow_multiple / 0.8))

        self.add(frame_animation, base_1, base_2, base_3)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(inverse_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if inverse_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.16
                elif inverse_codes[num][index] == " " and record == 0:
                    record = 1
                elif inverse_codes[num][index] != " ":
                    record = 0
            # 返回的单位 不确定
            return origin_len * 0.16

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=3, stroke_color=GOLD, corner_radius=0.05,
        )
        # 代码框移动到第一行代码处
        move_frame.set_width(ignore_space_len(0), stretch=True).set_height(
            0.45, stretch=True
        ).move_to(codes_inverse[0]).align_to(codes_inverse[0], RIGHT).shift(RIGHT * 0.1)
        # 代码框左边的小三角
        arrow = (
            Triangle(stroke_opacity=0, fill_opacity=1, fill_color=RED)
            .scale(0.13)
            .rotate(90 * DEGREES, axis=IN)
        )
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()

        # 第一行代码
        # 整体 7
        tmp_tmp = TextMobject("tmp", color=BLACK).scale(0.7 * (narrow_multiple / 0.8))
        tmp_tmp.next_to(base_1, UP, buff=0.4)
        self.play(Write(tmp_tmp))
        self.wait()
        # for 循环
        for circles in range((int)(inverse_recs / 2)):
            self.play(
                move_frame.set_width,
                ignore_space_len(1),
                move_frame.move_to,
                codes_inverse[1],
                move_frame.align_to,
                codes_inverse[1],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            if circles == 0:
                self.play(FadeInFrom(base_4, UP))
            else:
                self.play(base_4.shift, RIGHT * 0.8 * (narrow_multiple / 0.8))
                self.play(base_4[1][1].set_value, circles, run_time=0.5)
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(2),
                move_frame.move_to,
                codes_inverse[2],
                move_frame.align_to,
                codes_inverse[2],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            if circles == 0:
                self.play(ReplacementTransform(tmp_tmp, base_6))
            else:
                base_5.move_to(base_1[circles])
                self.play(FadeIn(base_5))
                self.wait()
                self.play(base_6[1].set_value, circles)
                self.wait()
                self.play(FadeOut(base_5))
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(3),
                move_frame.move_to,
                codes_inverse[3],
                move_frame.align_to,
                codes_inverse[3],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            base_5.move_to(base_1[inverse_recs - 1 - circles])
            # 建立一个临时的整体 1 的 n
            base_1_n_tmp = base_1[inverse_recs - 1 - circles][1].copy()
            self.play(FadeIn(base_5))
            self.play(
                FadeOut(base_1[circles][1]),
                base_1_n_tmp.move_to,
                base_1[circles][1],
                base_5.move_to,
                base_1[circles][1],
            )
            self.play(FadeOut(base_5))
            self.add(base_1_n_tmp)
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(4),
                move_frame.move_to,
                codes_inverse[4],
                move_frame.align_to,
                codes_inverse[4],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            base_5.move_to(base_1[inverse_recs - 1 - circles])
            self.play(FadeIn(base_5))
            self.play(base_1[inverse_recs - 1 - circles][1].set_value, circles)
            self.play(FadeOut(base_5))
            self.add(base_1_n_tmp)
            self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(1),
            move_frame.move_to,
            codes_inverse[1],
            move_frame.align_to,
            codes_inverse[1],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(base_4.shift, RIGHT * 0.8 * (narrow_multiple / 0.8))
        self.play(base_4[1][1].set_value, (int)(inverse_recs / 2), run_time=0.5)
        self.wait()
