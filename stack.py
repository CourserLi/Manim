from manimlib.imports import *
from manim_tuan import *

# seqStack
# a_push
# a_pop
# a_getTop
# resize
# clear
# size
# b_push
# b_pop
# b_getTop

seqStack_codes = [
    "if (initSize <= 0)",
    "    throw badSize();",
    "data = new T[initSize];",
    "maxSize = initSize;",
    "top = -1;",
]

a_push_codes = [
    "if (top == maxSize - 1)",
    "    resize();",
    "data[++top] = value;",
]

a_pop_codes = [
    "if (empty())",
    "    throw outOfRange();",
    "return data[top--];",
]

a_getTop_codes = [
    "if (empty())",
    "    throw outOfRange();",
    "return data[top];",
]

resize_codes = [
    "T *tmp = data;",
    "data = new T[2 * maxSize];",
    "for (int i = 0; i < maxSize; ++i)",
    "    data[i] = tmp[i];",
    "maxSize *= 2;",
    "delete[] tmp;",
]

clear_codes = [
    "Node *p;",
    "while (top != NULL) {",
    "    p = top;",
    "    top = top->next;",
    "    delete p;",
    "}",
]

size_codes = [
    "Node *p = top;",
    "int count = 0;",
    "while (p) {",
    "    count++;",
    "    p = p->next;",
    "}",
    "return count;",
]

b_push_codes = [
    "Node *p = new Node(value, top);",
    "top = p;",
]

b_pop_codes = [
    "if (empty())",
    "    throw outOfRange();",
    "Node *p = top;",
    "T value = p->data;",
    "top = top->next;",
    "delete p;",
    "return value;",
]

b_getTop_codes = [
    "if (empty())",
    "    throw outOfRange();",
    "return top->data;",
]


class Scene_White(Scene):
    CONFIG = {"camera_config": {
        "background_color": WHITE, "use_plot_depth": True, }}


class CodeLine_func(Text):
    CONFIG = {
        "t2c": {
            "seqStack": "#44cef6",
            "a_push": "#ff461f",
            "a_pop": "#00bc12",
            "a_getTop": "#ff7500",
            "resize": "#eacd76",
            "clear": "#725e82",
            "size": "#801dae",
            "b_push": "#9b4400",
            "b_pop": "#75878a",
            "b_getTop": "#003371",
        },
        "font": "Consolas",
        "size": 0.8,
        "color": DARK_GRAY,
        "plot_depth": 2,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class CodeLine_large(Text):
    CONFIG = {
        "t2c": {
            "initSize": BLUE_D,
            "maxSize": BLUE_D,
            "delete": PINK,
            "next": BLUE_D,
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
            "-1": RED_D,
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
            "initSize": BLUE_D,
            "maxSize": BLUE_D,
            "delete": PINK,
            "next": BLUE_D,
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
            "-1": RED_D,
        },
        "font": "Consolas",
        "size": 0.55,
        "color": DARK_GRAY,
        "plot_depth": 2,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class seqStack(Scene_White):
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
        background.set_height(3, stretch=True).set_width(6, stretch=True)
        background.to_corner(UP * 1.8)
        seqStack_function = CodeLine_func(
            "seqStack(6)", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.25)
        codes_seqStack = VGroup(
            *[CodeLine_large(code) for code in seqStack_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_seqStack.next_to(background.get_top(), DOWN,
                               buff=0.2).shift(RIGHT * 0.2)

        self.add(background, seqStack_function, codes_seqStack)

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
        # 整体 1(方块中的数字)
        base_1 = VGroup()
        # 方块中的数字 n
        for i in range(6):
            if i < 0:
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
        # 整体 2(maxSize)
        base_2 = VGroup(maxSize.copy(), maxSize_value.copy())
        # top
        top = TextMobject("top = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # top_value
        top_value = (
            Integer(-1, color=RED)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(top, RIGHT)
        )
        # 整体 3(top)
        base_3 = VGroup(top.copy(), top_value.copy())
        # 整体 4(蓝色方块)
        base_4 = square_base.copy()
        base_4.set_opacity(0.5).set_color(
            BLUE).set_height(0.75).set_width(0.75)
        # initSize
        initSize_index = TextMobject("initSize = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8))
        # initSize_value
        initSize_value = (
            Integer(6, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(initSize_index, RIGHT)
        )
        # 整体 5(initSize)
        base_5 = VGroup(initSize_index.copy(), initSize_value.copy())

        # 各整体的位置
        """
        整体 1(方块中的数字)
        整体 2(maxSize)
        整体 3(top)
        整体 4(蓝色方块)
        整体 5(initSize)
        """
        # maxSize 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 * (narrow_multiple / 0.8) + UP *
            0.5 * (narrow_multiple / 0.8)
        )
        # top 在 maxSize 下边
        base_3.next_to(base_2, DOWN, buff=0.35 * (narrow_multiple / 0.8)).align_to(
            base_2, LEFT
        )
        # initSize 在 maxSize 上面
        base_5.next_to(base_2, UP, buff=0.35 * (narrow_multiple / 0.8))
        # 方块中的数字 在 maxSize 右边
        base_1.next_to(base_2, RIGHT, buff=0.6 * (narrow_multiple / 0.8)).shift(
            RIGHT * 1 * (narrow_multiple / 0.8)
        )
        # 蓝色方块 在第一个方块中间
        base_4.move_to(base_1[4])

        # self.add(frame_animation, base_1, base_2, base_3, base_5)
        self.add(frame_animation, base_5)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(seqStack_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if seqStack_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif seqStack_codes[num][index] == " " and record == 0:
                    record = 1
                elif seqStack_codes[num][index] != " ":
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
        ).move_to(codes_seqStack[0]).align_to(codes_seqStack[0], RIGHT).shift(RIGHT * 0.1)
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

        # --------------- 正式开始 ---------------
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_seqStack[2],
            move_frame.align_to,
            codes_seqStack[2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 先将其(方块)右移
        base_1.shift(RIGHT)
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
        self.play(FadeIn(base_data))
        self.wait(0.5)
        self.play(ShowCreation(base_1))
        self.wait()
        # 再将其(方块)左移
        self.play(base_1.shift, LEFT, FadeOut(base_data))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(3),
            move_frame.move_to,
            codes_seqStack[3],
            move_frame.align_to,
            codes_seqStack[3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(Transform(base_5.copy(), base_2))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(4),
            move_frame.move_to,
            codes_seqStack[4],
            move_frame.align_to,
            codes_seqStack[4],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(Write(base_3))
        self.wait()


class a_push(Scene_White):
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
        background.set_height(2, stretch=True).set_width(5.5, stretch=True)
        background.to_corner(UP * 2.1)
        a_push_function = CodeLine_func(
            "push(3)", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.3)
        codes_a_push = VGroup(
            *[CodeLine_large(code) for code in a_push_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_a_push.next_to(background.get_top(), DOWN,
                             buff=0.2).shift(RIGHT * 0.2)

        self.add(background, a_push_function, codes_a_push)

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
        # 整体 1(方块中的数字)
        base_1 = VGroup()
        # 方块中的数字 n
        for i in range(6):
            if i < 3:
                n = (
                    Integer(i, color=BLACK)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            else:
                n = (
                    Integer(i, color=BLACK)
                    .set_opacity(0)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            base_1_tmp = VGroup(square_base.copy(), n.copy())
            base_1.add(base_1_tmp.copy())
        base_1.arrange(RIGHT, buff=0)
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
        # 整体 2(maxSize)
        base_2 = VGroup(maxSize.copy(), maxSize_value.copy())
        # top
        top = TextMobject("top = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # top_value
        top_value = (
            Integer(2, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(top, RIGHT)
        )
        # 整体 3(top)
        base_3 = VGroup(top.copy(), top_value.copy())
        # 整体 4(蓝色方块)
        base_4 = square_base.copy()
        base_4.set_opacity(0.5).set_color(
            BLUE).set_height(0.75).set_width(0.75)
        # value
        value_index = TextMobject("value = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8))
        # value_value
        value_value = (
            Integer(3, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(value_index, RIGHT)
        )
        # 整体 5(value)
        base_5 = VGroup(value_index.copy(), value_value.copy())

        # 各整体的位置
        """
        整体 1(方块中的数字)
        整体 2(maxSize)
        整体 3(top)
        整体 4(蓝色方块)
        整体 5(value)
        """
        # maxSize 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 * (narrow_multiple / 0.8) + UP *
            1 * (narrow_multiple / 0.8)
        )
        # top 在 maxSize 下边
        base_3.next_to(base_2, DOWN, buff=0.35 * (narrow_multiple / 0.8)).align_to(
            base_2, LEFT
        )
        # value 在 maxSize 上面
        base_5.next_to(base_2, UP, buff=0.35 * (narrow_multiple / 0.8)).align_to(
            base_2, LEFT
        )
        # 方块中的数字 在 maxSize 右边
        base_1.next_to(base_2, RIGHT, buff=0.6 * (narrow_multiple / 0.8)).shift(
            RIGHT * 1 * (narrow_multiple / 0.8)
        )
        # 蓝色方块 在第一个方块中间
        base_4.move_to(base_1[2])

        self.add(frame_animation, base_1, base_2, base_3, base_5)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(a_push_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if a_push_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif a_push_codes[num][index] == " " and record == 0:
                    record = 1
                elif a_push_codes[num][index] != " ":
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
        ).move_to(codes_a_push[0]).align_to(codes_a_push[0], RIGHT).shift(RIGHT * 0.1)
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

        # --------------- 正式开始 ---------------
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_a_push[2],
            move_frame.align_to,
            codes_a_push[2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 箭头(i_up)
        vec_i_up = Arrow(
            np.array([0, -1, 0]),
            np.array([0, 1, 0]),
            buff=0.6 * (narrow_multiple / 0.8),
            color=BLACK,
        ).scale(0.7 * (narrow_multiple / 0.8))
        # i
        i_index = TextMobject("data[top] = ", color=BLACK).scale(
            0.8 * (narrow_multiple / 0.8))
        # i_value
        i_value = (
            Integer(2, color=BLUE)
            .scale(0.8 * (narrow_multiple / 0.8))
            .next_to(i_index, RIGHT, buff=0.17)
        )
        base_i = VGroup(i_index.copy(), i_value.copy()).next_to(
            vec_i_up, DOWN, buff=0.1 * (narrow_multiple / 0.8)
        )
        # 整体 data[top]
        base_ii = VGroup(vec_i_up.copy(), base_i.copy()).next_to(
            base_1[2], DOWN, buff=0.15 * (narrow_multiple / 0.8))
        self.play(FadeInFrom(base_ii, UP), FadeIn(base_4))
        self.wait(0.5)
        self.play(
            base_ii.shift,
            RIGHT * 0.8 * (narrow_multiple / 0.8),
            base_4.move_to,
            base_1[3]
        )
        self.play(base_ii[1][1].set_value, 3,
                  base_3[1].set_value, 3,
                  base_1[3][1].set_opacity, 1, run_time=0.5)
        self.wait()


class a_pop(Scene_White):
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
        background.set_height(2, stretch=True).set_width(5.5, stretch=True)
        background.to_corner(UP * 2.1)
        a_pop_function = CodeLine_func(
            "pop()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.3)
        codes_a_pop = VGroup(
            *[CodeLine_large(code) for code in a_pop_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_a_pop.next_to(background.get_top(), DOWN,
                            buff=0.2).shift(RIGHT * 0.2)

        self.add(background, a_pop_function, codes_a_pop)

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
        # 整体 1(方块中的数字)
        base_1 = VGroup()
        # 方块中的数字 n
        for i in range(6):
            if i < 3:
                n = (
                    Integer(i, color=BLACK)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            else:
                n = (
                    Integer(i, color=BLACK)
                    .set_opacity(0)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            base_1_tmp = VGroup(square_base.copy(), n.copy())
            base_1.add(base_1_tmp.copy())
        base_1.arrange(RIGHT, buff=0)
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
        # 整体 2(maxSize)
        base_2 = VGroup(maxSize.copy(), maxSize_value.copy())
        # top
        top = TextMobject("top = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # top_value
        top_value = (
            Integer(2, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(top, RIGHT)
        )
        # 整体 3(top)
        base_3 = VGroup(top.copy(), top_value.copy())
        # 整体 4(蓝色方块)
        base_4 = square_base.copy()
        base_4.set_opacity(0.5).set_color(
            BLUE).set_height(0.75).set_width(0.75)

        # 各整体的位置
        """
        整体 1(方块中的数字)
        整体 2(maxSize)
        整体 3(top)
        整体 4(蓝色方块)
        """
        # maxSize 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 * (narrow_multiple / 0.8) + UP *
            1.5 * (narrow_multiple / 0.8)
        )
        # top 在 maxSize 下边
        base_3.next_to(base_2, DOWN, buff=0.35 * (narrow_multiple / 0.8)).align_to(
            base_2, LEFT
        )
        # 方块中的数字 在 maxSize 右边
        base_1.next_to(base_2, RIGHT, buff=0.6 * (narrow_multiple / 0.8)).shift(
            RIGHT * 1 * (narrow_multiple / 0.8) + DOWN *
            0.3 * (narrow_multiple / 0.8)
        )
        # 蓝色方块 在第一个方块中间
        base_4.move_to(base_1[2])

        self.add(frame_animation, base_1, base_2, base_3)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(a_pop_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if a_pop_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif a_pop_codes[num][index] == " " and record == 0:
                    record = 1
                elif a_pop_codes[num][index] != " ":
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
        ).move_to(codes_a_pop[0]).align_to(codes_a_pop[0], RIGHT).shift(RIGHT * 0.1)
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

        # --------------- 正式开始 ---------------
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
        background_tmp.set_height(2, stretch=True).set_width(3.5, stretch=True)
        background_tmp.align_to(frame_animation, UP).shift(
            UP * 0.5 * (narrow_multiple / 0.8)
        )
        # empty 代码
        empty_codes = [
            "bool empty() const",
            "{",
            "   return top == -1;",
            "}",
        ]
        codes_empty = VGroup(
            *[CodeLine_small(code) for code in empty_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_empty.next_to(background_tmp.get_top(), DOWN, buff=0.1)
        # empty 整体
        base_empty = VGroup(background_tmp, codes_empty)
        # empty 整体出现
        self.play(
            GrowFromCenter(base_empty),
            base_2.shift,
            DOWN * 1 * (narrow_multiple / 0.8) + LEFT *
            1.1 * (narrow_multiple / 0.8),
            base_3.shift,
            DOWN * 1 * (narrow_multiple / 0.8) + LEFT *
            1.1 * (narrow_multiple / 0.8),
            base_1.shift,
            DOWN * 1.4 * (narrow_multiple / 0.8)
            + RIGHT * 1 * (narrow_multiple / 0.8),
            run_time=1.5,
        )
        self.wait()
        # empty 整体消失
        self.play(
            FadeOutAndShift(base_empty, UP),
            base_2.shift,
            UP * 1 * (narrow_multiple / 0.8) + RIGHT *
            1.1 * (narrow_multiple / 0.8),
            base_3.shift,
            UP * 1 * (narrow_multiple / 0.8) + RIGHT *
            1.1 * (narrow_multiple / 0.8),
            base_1.shift,
            UP * 1.4 * (narrow_multiple / 0.8) + LEFT *
            1 * (narrow_multiple / 0.8),
        )
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_a_pop[2],
            move_frame.align_to,
            codes_a_pop[2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 箭头(i_up)
        vec_i_up = Arrow(
            np.array([0, -1, 0]),
            np.array([0, 1, 0]),
            buff=0.6 * (narrow_multiple / 0.8),
            color=BLACK,
        ).scale(0.7 * (narrow_multiple / 0.8))
        # i
        i_index = TextMobject("data[top] = ", color=BLACK).scale(
            0.8 * (narrow_multiple / 0.8))
        # i_value
        i_value = (
            Integer(2, color=BLUE)
            .scale(0.8 * (narrow_multiple / 0.8))
            .next_to(i_index, RIGHT, buff=0.17)
        )
        base_i = VGroup(i_index.copy(), i_value.copy()).next_to(
            vec_i_up, DOWN, buff=0.1 * (narrow_multiple / 0.8)
        )
        # 整体 data[top]
        base_ii = VGroup(vec_i_up.copy(), base_i.copy()).next_to(
            base_1[2], DOWN, buff=0.15 * (narrow_multiple / 0.8))
        self.play(FadeInFrom(base_ii, UP), FadeIn(base_4))
        self.wait(0.5)
        self.play(
            base_ii.shift,
            LEFT * 0.8 * (narrow_multiple / 0.8),
            base_4.move_to,
            base_1[1]
        )
        self.wait(0.5)
        self.play(base_ii[1][1].set_value, 1,
                  base_3[1].set_value, 1)
        self.wait()


class a_getTop(Scene_White):
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
        background.set_height(2, stretch=True).set_width(5.5, stretch=True)
        background.to_corner(UP * 2.1)
        a_getTop_function = CodeLine_func(
            "getTop()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.3)
        codes_a_getTop = VGroup(
            *[CodeLine_large(code) for code in a_getTop_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_a_getTop.next_to(background.get_top(), DOWN,
                               buff=0.2).shift(RIGHT * 0.2)

        self.add(background, a_getTop_function, codes_a_getTop)

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
        # 整体 1(方块中的数字)
        base_1 = VGroup()
        # 方块中的数字 n
        for i in range(6):
            if i < 3:
                n = (
                    Integer(i, color=BLACK)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            else:
                n = (
                    Integer(i, color=BLACK)
                    .set_opacity(0)
                    .scale(1 * (narrow_multiple / 0.8))
                    .move_to(square_base)
                )
            base_1_tmp = VGroup(square_base.copy(), n.copy())
            base_1.add(base_1_tmp.copy())
        base_1.arrange(RIGHT, buff=0)
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
        # 整体 2(maxSize)
        base_2 = VGroup(maxSize.copy(), maxSize_value.copy())
        # top
        top = TextMobject("top = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # top_value
        top_value = (
            Integer(2, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(top, RIGHT)
        )
        # 整体 3(top)
        base_3 = VGroup(top.copy(), top_value.copy())
        # 整体 4(蓝色方块)
        base_4 = square_base.copy()
        base_4.set_opacity(0.5).set_color(
            BLUE).set_height(0.75).set_width(0.75)

        # 各整体的位置
        """
        整体 1(方块中的数字)
        整体 2(maxSize)
        整体 3(top)
        整体 4(蓝色方块)
        """
        # maxSize 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 * (narrow_multiple / 0.8) + UP *
            1.5 * (narrow_multiple / 0.8)
        )
        # top 在 maxSize 下边
        base_3.next_to(base_2, DOWN, buff=0.35 * (narrow_multiple / 0.8)).align_to(
            base_2, LEFT
        )
        # 方块中的数字 在 maxSize 右边
        base_1.next_to(base_2, RIGHT, buff=0.6 * (narrow_multiple / 0.8)).shift(
            RIGHT * 1 * (narrow_multiple / 0.8) + DOWN *
            0.3 * (narrow_multiple / 0.8)
        )
        # 蓝色方块 在第一个方块中间
        base_4.move_to(base_1[2])

        self.add(frame_animation, base_1, base_2, base_3)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(a_getTop_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if a_getTop_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif a_getTop_codes[num][index] == " " and record == 0:
                    record = 1
                elif a_getTop_codes[num][index] != " ":
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
        ).move_to(codes_a_getTop[0]).align_to(codes_a_getTop[0], RIGHT).shift(RIGHT * 0.1)
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

        # --------------- 正式开始 ---------------
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
        background_tmp.set_height(2, stretch=True).set_width(3.5, stretch=True)
        background_tmp.align_to(frame_animation, UP).shift(
            UP * 0.5 * (narrow_multiple / 0.8)
        )
        # empty 代码
        empty_codes = [
            "bool empty() const",
            "{",
            "   return top == -1;",
            "}",
        ]
        codes_empty = VGroup(
            *[CodeLine_small(code) for code in empty_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_empty.next_to(background_tmp.get_top(), DOWN, buff=0.1)
        # empty 整体
        base_empty = VGroup(background_tmp, codes_empty)
        # empty 整体出现
        self.play(
            GrowFromCenter(base_empty),
            base_2.shift,
            DOWN * 1 * (narrow_multiple / 0.8) + LEFT *
            1.1 * (narrow_multiple / 0.8),
            base_3.shift,
            DOWN * 1 * (narrow_multiple / 0.8) + LEFT *
            1.1 * (narrow_multiple / 0.8),
            base_1.shift,
            DOWN * 1.4 * (narrow_multiple / 0.8)
            + RIGHT * 1 * (narrow_multiple / 0.8),
            run_time=1.5,
        )
        self.wait()
        # empty 整体消失
        self.play(
            FadeOutAndShift(base_empty, UP),
            base_2.shift,
            UP * 1 * (narrow_multiple / 0.8) + RIGHT *
            1.1 * (narrow_multiple / 0.8),
            base_3.shift,
            UP * 1 * (narrow_multiple / 0.8) + RIGHT *
            1.1 * (narrow_multiple / 0.8),
            base_1.shift,
            UP * 1.4 * (narrow_multiple / 0.8) + LEFT *
            1 * (narrow_multiple / 0.8),
        )
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_a_getTop[2],
            move_frame.align_to,
            codes_a_getTop[2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 箭头(i_up)
        vec_i_up = Arrow(
            np.array([0, -1, 0]),
            np.array([0, 1, 0]),
            buff=0.6 * (narrow_multiple / 0.8),
            color=BLACK,
        ).scale(0.7 * (narrow_multiple / 0.8))
        # i
        i_index = TextMobject("data[top] = ", color=BLACK).scale(
            0.8 * (narrow_multiple / 0.8))
        # i_value
        i_value = (
            Integer(2, color=BLUE)
            .scale(0.8 * (narrow_multiple / 0.8))
            .next_to(i_index, RIGHT, buff=0.17)
        )
        base_i = VGroup(i_index.copy(), i_value.copy()).next_to(
            vec_i_up, DOWN, buff=0.1 * (narrow_multiple / 0.8)
        )
        # 整体 data[top]
        base_ii = VGroup(vec_i_up.copy(), base_i.copy()).next_to(
            base_1[2], DOWN, buff=0.15 * (narrow_multiple / 0.8))
        self.play(FadeInFrom(base_ii, UP), FadeIn(base_4))
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
        background.set_height(3.1, stretch=True).set_width(5.8, stretch=True)
        background.to_corner(UP * 1.5)
        resize_function = CodeLine_func(
            "resize()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.18)
        codes_resize = VGroup(
            *[CodeLine_small(code) for code in resize_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_resize.next_to(background.get_top(), DOWN,
                             buff=0.2).shift(RIGHT * 0.2)

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
            if i < 6:
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
        # top
        top = TextMobject("top = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.8)
        )
        # top_value
        top_value = (
            Integer(4, color=BLUE)
            .scale(1 * (narrow_multiple / 0.8))
            .next_to(top, RIGHT)
        )
        # 整体 2
        base_2 = VGroup(top.copy(), top_value.copy())
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
        i_index = TextMobject("i = ", color=BLACK).scale(
            0.8 * (narrow_multiple / 0.8))
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
        base_5.set_opacity(0.5).set_color(
            BLUE).set_height(0.75).set_width(0.75)

        # 各整体的位置
        # 整体 2 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 * (narrow_multiple / 0.8) + UP *
            1 * (narrow_multiple / 0.8)
        )
        # 整体 3 在整体 2 下边
        base_3.next_to(base_2, DOWN, buff=0.5 * (narrow_multiple / 0.8)).align_to(
            base_2, LEFT
        )
        # 整体 1 在整体 2 右边
        base_1.next_to(base_2, RIGHT, buff=0.6 * (narrow_multiple / 0.8)).shift(
            DOWN * 0.4 * (narrow_multiple / 0.8) + RIGHT *
            1 * (narrow_multiple / 0.8)
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

        # --------------- 正式开始 ---------------
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
        # 箭头(tmp)
        vec_tmp = Arrow(
            np.array([-1, 0, 0]), np.array([1, 0, 0]), buff=0.6, color=BLACK
        ).scale(0.7)
        # data
        tmp = TextMobject("tmp", color=BLACK).scale(
            0.7).next_to(vec_tmp, LEFT, buff=0.1)
        # 整体 7
        base_tmp = VGroup(tmp, vec_tmp)
        base_tmp.next_to(base_1[0], LEFT, buff=0.15).shift(UP * 0.2)
        # 建立一个临时的整体 6
        base_data_tmp = base_data.copy()
        self.play(
            ReplacementTransform(
                base_data_tmp, base_tmp), base_data.shift, DOWN * 0.2
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
        # 整体 1 整体 6 整体 7 向左下移动
        base_move_down = VGroup(base_1, base_data, base_tmp)
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
        self.play(base_data.move_to,
                  base_turn_out[0], base_tmp.shift, DOWN * 0.2)
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
        for circles in range(6):
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
            if circles == 0:
                base_4.next_to(base_8[0], DOWN,
                               buff=0.15 * (narrow_multiple / 0.8))
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
            # 上面方块的数字移动到下面方块的数字里面
            base_1_n_tmp = base_1[circles][1].copy()
            self.play(base_1_n_tmp.move_to, base_8[circles])
            self.add(base_1_n_tmp)
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
        self.play(base_4.shift, RIGHT * 0.8 *
                  (narrow_multiple / 0.8), FadeOut(base_5))
        self.play(base_4[1][1].set_value, 6, run_time=0.5)
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
        self.play(base_3[1].set_value, 12)
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
            FadeOut(base_tmp),
            base_2.shift,
            DOWN * 0.5,
        )
        self.wait()


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
        background.set_height(3.5, stretch=True).set_width(5.35, stretch=True)
        background.to_corner(UP * 1.7)
        clear_function = CodeLine_func(
            "clear()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.21)
        codes_clear = VGroup(
            *[CodeLine_large(code) for code in clear_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_clear.next_to(background.get_top(), DOWN,
                            buff=0.2).shift(RIGHT * 0.2)

        self.add(background, clear_function, codes_clear)
        # 代码脚注线
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=3.7,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        rectangle_base = MySquare(
            color=BLACK, side_length=0.5, stroke_opacity=1)
        # 基准大小
        narrow_multiple = rectangle_base.get_width()
        assert rectangle_base.get_width() * 2 == 1
        # 前后方块，合并为长方块
        rectangle_front = rectangle_base.copy()
        rectangle_later = rectangle_base.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        # 箭头
        vec_base = (
            Arrow(color=BLACK, buff=narrow_multiple, fill_color=BLACK)
            .scale(0.75)
            .move_to(rectangle_later)
            .shift(RIGHT * 0.8 * narrow_multiple)
        )
        # 整体 base
        base = VGroup(rectangle_front.copy(),
                      rectangle_later.copy(), vec_base.copy())
        # 箭头(top)
        vec_top = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # top
        top = (
            TextMobject("top", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_top, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(top.copy(), vec_top.copy())
        # 整体 2
        base_2 = VGroup()
        # 方块中的数字 n
        for i in range(5):
            n = (
                Integer(i, color=BLACK)
                .scale(0.7 * (narrow_multiple / 0.5))
                .move_to(base[0])
            )
            base_2_tmp = VGroup(base.copy(), n.copy())
            base_2.add(base_2_tmp.copy())
        base_2.arrange(RIGHT, buff=0.1 * (narrow_multiple / 0.5))
        # 整题 3 (NULL)
        base_3 = TextMobject("NULL", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5))
        # count
        count = TextMobject("count = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # count_value
        count_value = (
            Integer(4, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(count, RIGHT)
        )
        # 整体 4
        base_4 = VGroup(count.copy(), count_value.copy())
        #
        vec_tmp = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
        )
        # tmp
        tmp = (
            TextMobject("tmp", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_tmp.copy(), DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 5
        base_5 = VGroup(vec_tmp.copy(), tmp.copy())
        # 箭头(p)
        vec_p = vec_tmp.copy()
        # p
        p = (
            TextMobject("P", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_p, DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 6
        base_6 = VGroup(vec_p.copy(), p.copy())

        # 各整体的位置
        """
        整体 1(top)
        整体 2(长方块)
        整体 3(NULL)
        整体 4(count)
        整体 5(tmp)
        整体 6(p)
        """
        # 整体 2 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3 * (narrow_multiple / 0.5) + UP *
            0.2 * (narrow_multiple / 0.5)
        )
        # 整体 1 在整体 2 上面
        base_1.next_to(base_2[0][0][0], UP, buff=0.1 * (narrow_multiple / 0.5))
        # 整体 3 在整体 2 右边
        base_3.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))

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
        ).move_to(codes_clear[0]).align_to(codes_clear[0], RIGHT).shift(
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

        # --------------- 正式开始 ---------------
        for circle in range(5):
            self.play(
                move_frame.set_width,
                ignore_space_len(1),
                move_frame.move_to,
                codes_clear[1],
                move_frame.align_to,
                codes_clear[1],
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
                ignore_space_len(2),
                move_frame.move_to,
                codes_clear[2],
                move_frame.align_to,
                codes_clear[2],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            base_6.next_to(base_2[circle][0][0], DOWN, buff=0.1)
            self.play(FadeInFrom(base_6, UP))
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(3),
                move_frame.move_to,
                codes_clear[3],
                move_frame.align_to,
                codes_clear[3],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            self.play(base_2[circle][0][2].set_color, BLUE)
            self.wait()
            if circle != 4:
                self.play(base_1.shift, RIGHT*1.625)
            else:
                self.play(base_1.shift, RIGHT*2.0)
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(4),
                move_frame.move_to,
                codes_clear[4],
                move_frame.align_to,
                codes_clear[4],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            self.play(FadeOut(base_2[circle]), FadeOut(base_6))
            self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(1),
            move_frame.move_to,
            codes_clear[1],
            move_frame.align_to,
            codes_clear[1],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()


class size(Scene_White):
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
        background.set_height(4, stretch=True).set_width(4.5, stretch=True)
        background.to_corner(UP * 1.7)
        size_function = CodeLine_func(
            "size()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.21)
        codes_size = VGroup(
            *[CodeLine_large(code) for code in size_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_size.next_to(background.get_top(), DOWN,
                           buff=0.2).shift(RIGHT * 0.2)

        self.add(background, size_function, codes_size)
        # 代码脚注线
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=3.7,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        rectangle_base = MySquare(
            color=BLACK, side_length=0.5, stroke_opacity=1)
        # 基准大小
        narrow_multiple = rectangle_base.get_width()
        assert rectangle_base.get_width() * 2 == 1
        # 前后方块，合并为长方块
        rectangle_front = rectangle_base.copy()
        rectangle_later = rectangle_base.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        # 箭头
        vec_base = (
            Arrow(color=BLACK, buff=narrow_multiple, fill_color=BLACK)
            .scale(0.75)
            .move_to(rectangle_later)
            .shift(RIGHT * 0.8 * narrow_multiple)
        )
        # 整体 base
        base = VGroup(rectangle_front.copy(),
                      rectangle_later.copy(), vec_base.copy())
        # 箭头(top)
        vec_top = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # top
        top = (
            TextMobject("top", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_top, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(top.copy(), vec_top.copy())
        # 整体 2
        base_2 = VGroup()
        # 方块中的数字 n
        for i in range(5):
            n = (
                Integer(i, color=BLACK)
                .scale(0.7 * (narrow_multiple / 0.5))
                .move_to(base[0])
            )
            base_2_tmp = VGroup(base.copy(), n.copy())
            base_2.add(base_2_tmp.copy())
        base_2.arrange(RIGHT, buff=0.1 * (narrow_multiple / 0.5))
        # 整题 3 (NULL)
        base_3 = TextMobject("NULL", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5))
        # count
        count = TextMobject("count = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # count_value
        count_value = (
            Integer(0, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(count, RIGHT)
        )
        # 整体 4
        base_4 = VGroup(count.copy(), count_value.copy())
        #
        vec_tmp = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
        )
        # tmp
        tmp = (
            TextMobject("tmp", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_tmp.copy(), DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 5
        base_5 = VGroup(vec_tmp.copy(), tmp.copy())
        # 箭头(p)
        vec_p = vec_tmp.copy()
        # p
        p = (
            TextMobject("P", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_p, DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 6
        base_6 = VGroup(vec_p.copy(), p.copy())

        # 各整体的位置
        """
        整体 1(top)
        整体 2(长方块)
        整体 3(NULL)
        整体 4(count)
        整体 5(tmp)
        整体 6(p)
        """
        # 整体 4 靠左
        base_4.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.7 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 4 右边
        base_2.next_to(base_4, RIGHT, buff=1 * (narrow_multiple / 0.5))
        # 整体 1 在整体 2 上边
        base_1.next_to(base_2[0][0][0], UP, buff=0.1 * (narrow_multiple / 0.5))
        # 整体 3 在整体 2 右边
        base_3.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))

        self.add(frame_animation, base_1, base_2, base_3)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(size_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if size_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif size_codes[num][index] == " " and record == 0:
                    record = 1
                elif size_codes[num][index] != " ":
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
        ).move_to(codes_size[0]).align_to(codes_size[0], RIGHT).shift(
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

        # --------------- 正式开始 ---------------
        base_6.next_to(base_2[0][0][0], DOWN, buff=0.1)
        self.play(FadeInFrom(base_6, UP))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(1),
            move_frame.move_to,
            codes_size[1],
            move_frame.align_to,
            codes_size[1],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(Write(base_4))
        for circle in range(5):
            self.play(
                move_frame.set_width,
                ignore_space_len(2),
                move_frame.move_to,
                codes_size[2],
                move_frame.align_to,
                codes_size[2],
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
                codes_size[3],
                move_frame.align_to,
                codes_size[3],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            self.play(base_4[1].set_value, circle+1)
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(4),
                move_frame.move_to,
                codes_size[4],
                move_frame.align_to,
                codes_size[4],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            if circle != 4:
                self.play(base_6.shift, RIGHT*1.625)
            else:
                self.play(base_6.shift, RIGHT*2.0)
            self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_size[2],
            move_frame.align_to,
            codes_size[2],
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
            ignore_space_len(6),
            move_frame.move_to,
            codes_size[6],
            move_frame.align_to,
            codes_size[6],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()


class b_push(Scene_White):
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
        background.set_height(1.3, stretch=True).set_width(7, stretch=True)
        background.to_corner(UP * 2.7)
        b_push_function = CodeLine_func(
            "push(10)", font="思源宋体 Heavy", b_push=0.8
        ).to_corner(UP, buff=0.5)
        codes_b_push = VGroup(
            *[CodeLine_large(code) for code in b_push_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_b_push.next_to(background.get_top(), DOWN,
                             buff=0.2).shift(RIGHT * 0.2)

        self.add(background, b_push_function, codes_b_push)
        # 代码脚注线
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=3.7,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        rectangle_base = MySquare(
            color=BLACK, side_length=0.5, stroke_opacity=1)
        # 基准大小
        narrow_multiple = rectangle_base.get_width()
        assert rectangle_base.get_width() * 2 == 1
        # 前后方块，合并为长方块
        rectangle_front = rectangle_base.copy()
        rectangle_later = rectangle_base.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        # 箭头
        vec_base = (
            Arrow(color=BLACK, buff=narrow_multiple, fill_color=BLACK)
            .scale(0.75)
            .move_to(rectangle_later)
            .shift(RIGHT * 0.8 * narrow_multiple)
        )
        # 整体 base
        base = VGroup(rectangle_front.copy(),
                      rectangle_later.copy(), vec_base.copy())
        # 箭头(top)
        vec_top = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # top
        top = (
            TextMobject("top", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_top, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(top.copy(), vec_top.copy())
        # 整体 2
        base_2 = VGroup()
        # 方块中的数字 n
        for i in range(4):
            n = (
                Integer(i, color=BLACK)
                .scale(0.7 * (narrow_multiple / 0.5))
                .move_to(base[0])
            )
            base_2_tmp = VGroup(base.copy(), n.copy())
            base_2.add(base_2_tmp.copy())
        base_2.arrange(RIGHT, buff=0.1 * (narrow_multiple / 0.5))
        # 整题 3 (NULL)
        base_3 = TextMobject("NULL", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5))
        # value
        value = TextMobject("value = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # value_value
        value_value = (
            Integer(10, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(value, RIGHT)
        )
        # 整体 4
        base_4 = VGroup(value.copy(), value_value.copy())
        #
        vec_tmp = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
        )
        # tmp
        tmp = (
            TextMobject("tmp", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_tmp.copy(), DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 5
        base_5 = VGroup(vec_tmp.copy(), tmp.copy())
        # 箭头(p)
        vec_p = vec_tmp.copy()
        # p
        p = (
            TextMobject("P", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_p, DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 6
        base_6 = VGroup(vec_p.copy(), p.copy())

        # 各整体的位置
        """
        整体 1(top)
        整体 2(长方块)
        整体 3(NULL)
        整体 4(value)
        整体 5(tmp)
        整体 6(p)
        """
        # 整体 4 靠左
        base_4.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.7 * (narrow_multiple / 0.5) + UP *
            1.2 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 4 右边
        base_2.next_to(base_4, RIGHT, buff=1 * (narrow_multiple / 0.5))
        # 整体 1 在整体 2 上边
        base_1.next_to(base_2[0][0][0], UP, buff=0.1 * (narrow_multiple / 0.5))
        # 整体 3 在整体 2 右边
        base_3.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))

        self.add(frame_animation, base_1, base_2, base_3, base_4)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(b_push_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if b_push_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif b_push_codes[num][index] == " " and record == 0:
                    record = 1
                elif b_push_codes[num][index] != " ":
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
        ).move_to(codes_b_push[0]).align_to(codes_b_push[0], RIGHT).shift(
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

        # --------------- 正式开始 ---------------
        # 建立新的方块
        n = (
            Integer(10, color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .move_to(base[0])
        )
        insert_base = VGroup(base.copy(), n.copy()).move_to(base_2[0]).shift(
            DOWN * 1.2 * (narrow_multiple / 0.5)
            + LEFT * 0.5 * (narrow_multiple / 0.5)
        )
        insert_base[0][2].rotate(
            angle=90 * DEGREES, about_point=insert_base[0][2].get_start()
        )
        base_6.add_updater(lambda a: a.next_to(
            insert_base[0][0][0], DOWN, buff=0.1))
        self.play(FadeInFrom(insert_base, RIGHT))
        self.play(FadeInFrom(base_6, UP))
        self.wait()
        to_RightUp = VGroup(insert_base, base_6)
        to_Right = VGroup(base_1, base_2, base_3)
        self.play(to_RightUp.shift, UP * 1.2 * (narrow_multiple / 0.5) +
                  RIGHT * 0.5 * (narrow_multiple / 0.5), to_Right.shift, RIGHT*1.625)
        self.play(insert_base[0][2].rotate, {
                  "angle": -90 * DEGREES, "about_point": insert_base[0][2].get_start()})
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(1),
            move_frame.move_to,
            codes_b_push[1],
            move_frame.align_to,
            codes_b_push[1],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(base_1.shift, LEFT*1.625)
        self.wait()


class b_pop(Scene_White):
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
        background_left.set_height(
            2.5, stretch=True).set_width(6, stretch=True)
        background_right = background_left.copy()
        background_left.to_corner(UP * 1.5 + LEFT * 2.15)
        background_right.to_corner(UP * 1.5 + RIGHT * 2.15)
        background = VGroup(background_left, background_right)
        b_pop_function = CodeLine_func(
            "pop()", font="思源宋体 Heavy", b_pop=0.8
        ).to_corner(UP, buff=0.18)
        codes_b_pop_1 = VGroup(
            *[CodeLine_large(code) for code in b_pop_codes[:4]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_b_pop_1.next_to(background_left.get_top(), DOWN, buff=0.2).shift(
            LEFT * 0.4
        )
        codes_b_pop_2 = VGroup(
            *[CodeLine_large(code) for code in b_pop_codes[4:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_b_pop_2.next_to(background_right.get_top(), DOWN, buff=0.2).shift(
            RIGHT * 0.1 + LEFT * 1
        )
        codes_b_pop = VGroup(codes_b_pop_1, codes_b_pop_2)

        self.add(background, b_pop_function, codes_b_pop)
        # 代码脚注线
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=3.7,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        rectangle_base = MySquare(
            color=BLACK, side_length=0.5, stroke_opacity=1)
        # 基准大小
        narrow_multiple = rectangle_base.get_width()
        assert rectangle_base.get_width() * 2 == 1
        # 前后方块，合并为长方块
        rectangle_front = rectangle_base.copy()
        rectangle_later = rectangle_base.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        # 箭头
        vec_base = (
            Arrow(color=BLACK, buff=narrow_multiple, fill_color=BLACK)
            .scale(0.75)
            .move_to(rectangle_later)
            .shift(RIGHT * 0.8 * narrow_multiple)
        )
        # 整体 base
        base = VGroup(rectangle_front.copy(),
                      rectangle_later.copy(), vec_base.copy())
        # 箭头(top)
        vec_top = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # top
        top = (
            TextMobject("top", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_top, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(top.copy(), vec_top.copy())
        # 整体 2
        base_2 = VGroup()
        # 方块中的数字 n
        for i in range(5):
            n = (
                Integer(i, color=BLACK)
                .scale(0.7 * (narrow_multiple / 0.5))
                .move_to(base[0])
            )
            base_2_tmp = VGroup(base.copy(), n.copy())
            base_2.add(base_2_tmp.copy())
        base_2.arrange(RIGHT, buff=0.1 * (narrow_multiple / 0.5))
        # 整题 3 (NULL)
        base_3 = TextMobject("NULL", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5))
        # value
        value = TextMobject("value = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # value_value
        value_value = (
            Integer(0, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(value, RIGHT)
        )
        # 整体 4
        base_4 = VGroup(value.copy(), value_value.copy())
        #
        vec_tmp = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
        )
        # tmp
        tmp = (
            TextMobject("tmp", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_tmp.copy(), DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 5
        base_5 = VGroup(vec_tmp.copy(), tmp.copy())
        # 箭头(p)
        vec_p = vec_tmp.copy()
        # p
        p = (
            TextMobject("P", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_p, DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 6
        base_6 = VGroup(vec_p.copy(), p.copy())

        # 各整体的位置
        """
        整体 1(top)
        整体 2(长方块)
        整体 3(NULL)
        整体 4(value)
        整体 5(tmp)
        整体 6(p)
        """
        # 整体 4 靠左
        base_4.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.7 * (narrow_multiple / 0.5) + UP *
            0.7 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 4 右边
        base_2.next_to(base_4, RIGHT, buff=1 * (narrow_multiple / 0.5))
        # 整体 1 在整体 2 上边
        base_1.next_to(base_2[0][0][0], UP, buff=0.1 * (narrow_multiple / 0.5))
        # 整体 3 在整体 2 右边
        base_3.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))

        self.add(frame_animation, base_1, base_2, base_3)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(b_pop_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if b_pop_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif b_pop_codes[num][index] == " " and record == 0:
                    record = 1
                elif b_pop_codes[num][index] != " ":
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
        ).move_to(codes_b_pop[0][0]).align_to(codes_b_pop[0][0], RIGHT).shift(
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

        # --------------- 正式开始 ---------------
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
        background_tmp.set_height(2, stretch=True).set_width(3.5, stretch=True)
        background_tmp.align_to(frame_animation, UP).shift(
            UP * 1.2 * (narrow_multiple / 0.8)
        )
        # empty 代码
        empty_codes = [
            "bool empty() const",
            "{",
            "   return top == NULL;",
            "}",
        ]
        codes_empty = VGroup(
            *[CodeLine_small(code) for code in empty_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_empty.next_to(background_tmp.get_top(), DOWN, buff=0.1)
        # empty 整体
        base_empty = VGroup(background_tmp, codes_empty)
        # empty 整体出现
        to_Down = VGroup(base_1, base_2, base_3)
        self.play(
            GrowFromCenter(base_empty),
            to_Down.shift,
            DOWN * 1.5 * (narrow_multiple / 0.8),
            run_time=1.5,
        )
        self.wait()
        # empty 整体消失
        self.play(
            FadeOutAndShift(base_empty, UP),
            to_Down.shift,
            UP * 1.5 * (narrow_multiple / 0.8),
            run_time=1.5,
        )
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_b_pop[0][2],
            move_frame.align_to,
            codes_b_pop[0][2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        base_6.next_to(base_2[0][0][0], DOWN, buff=0.1)
        self.play(FadeInFrom(base_6, UP))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(3),
            move_frame.move_to,
            codes_b_pop[0][3],
            move_frame.align_to,
            codes_b_pop[0][3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        base_blue = rectangle_base.copy()
        base_blue.set_opacity(0.5).set_color(
            BLUE).set_height(0.45).set_width(0.45).move_to(base_2[0][0][0])
        self.play(Write(base_4), FadeIn(base_blue))
        self.wait()
        self.play(
            FadeOut(base_blue),
            move_frame.set_width,
            ignore_space_len(4),
            move_frame.move_to,
            codes_b_pop[1][0],
            move_frame.align_to,
            codes_b_pop[1][0],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(base_2[0][0][2].set_color, BLUE)
        self.wait()
        self.play(base_1.shift, RIGHT*1.625)
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(5),
            move_frame.move_to,
            codes_b_pop[1][1],
            move_frame.align_to,
            codes_b_pop[1][1],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(FadeOut(base_2[0]), FadeOut(base_6))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(6),
            move_frame.move_to,
            codes_b_pop[1][2],
            move_frame.align_to,
            codes_b_pop[1][2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()


class b_getTop(Scene_White):
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
        background.set_height(2, stretch=True).set_width(5.35, stretch=True)
        background.to_corner(UP * 2.1)
        b_getTop_function = CodeLine_func(
            "getTop()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.3)
        codes_b_getTop = VGroup(
            *[CodeLine_large(code) for code in b_getTop_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_b_getTop.next_to(background.get_top(), DOWN,
                               buff=0.2).shift(RIGHT * 0.2)

        self.add(background, b_getTop_function, codes_b_getTop)
        # 代码脚注线
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=3.7,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        rectangle_base = MySquare(
            color=BLACK, side_length=0.5, stroke_opacity=1)
        # 基准大小
        narrow_multiple = rectangle_base.get_width()
        assert rectangle_base.get_width() * 2 == 1
        # 前后方块，合并为长方块
        rectangle_front = rectangle_base.copy()
        rectangle_later = rectangle_base.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        # 箭头
        vec_base = (
            Arrow(color=BLACK, buff=narrow_multiple, fill_color=BLACK)
            .scale(0.75)
            .move_to(rectangle_later)
            .shift(RIGHT * 0.8 * narrow_multiple)
        )
        # 整体 base
        base = VGroup(rectangle_front.copy(),
                      rectangle_later.copy(), vec_base.copy())
        # 箭头(top)
        vec_top = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # top
        top = (
            TextMobject("top", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_top, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(top.copy(), vec_top.copy())
        # 整体 2
        base_2 = VGroup()
        # 方块中的数字 n
        for i in range(5):
            n = (
                Integer(i, color=BLACK)
                .scale(0.7 * (narrow_multiple / 0.5))
                .move_to(base[0])
            )
            base_2_tmp = VGroup(base.copy(), n.copy())
            base_2.add(base_2_tmp.copy())
        base_2.arrange(RIGHT, buff=0.1 * (narrow_multiple / 0.5))
        # 整题 3 (NULL)
        base_3 = TextMobject("NULL", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5))
        # count
        count = TextMobject("count = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # count_value
        count_value = (
            Integer(4, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(count, RIGHT)
        )
        # 整体 4
        base_4 = VGroup(count.copy(), count_value.copy())
        #
        vec_tmp = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
        )
        # tmp
        tmp = (
            TextMobject("tmp", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_tmp.copy(), DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 5
        base_5 = VGroup(vec_tmp.copy(), tmp.copy())
        # 箭头(p)
        vec_p = vec_tmp.copy()
        # p
        p = (
            TextMobject("P", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_p, DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 6
        base_6 = VGroup(vec_p.copy(), p.copy())

        # 各整体的位置
        """
        整体 1(top)
        整体 2(长方块)
        整体 3(NULL)
        整体 4(count)
        整体 5(tmp)
        整体 6(p)
        """
        # 整体 2 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3 * (narrow_multiple / 0.5) + UP *
            1 * (narrow_multiple / 0.5)
        )
        # 整体 1 在整体 2 上面
        base_1.next_to(base_2[0][0][0], UP, buff=0.1 * (narrow_multiple / 0.5))
        # 整体 3 在整体 2 右边
        base_3.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))

        self.add(frame_animation, base_1, base_2, base_3)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(b_getTop_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if b_getTop_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif b_getTop_codes[num][index] == " " and record == 0:
                    record = 1
                elif b_getTop_codes[num][index] != " ":
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
        ).move_to(codes_b_getTop[0]).align_to(codes_b_getTop[0], RIGHT).shift(
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

        # --------------- 正式开始 ---------------
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
        background_tmp.set_height(2, stretch=True).set_width(3.5, stretch=True)
        background_tmp.align_to(frame_animation, UP).shift(
            UP * 1.5 * (narrow_multiple / 0.8)
        )
        # empty 代码
        empty_codes = [
            "bool empty() const",
            "{",
            "   return top == NULL;",
            "}",
        ]
        codes_empty = VGroup(
            *[CodeLine_small(code) for code in empty_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_empty.next_to(background_tmp.get_top(), DOWN, buff=0.1)
        # empty 整体
        base_empty = VGroup(background_tmp, codes_empty)
        # empty 整体出现
        to_Down = VGroup(base_1, base_2, base_3)
        self.play(
            GrowFromCenter(base_empty),
            to_Down.shift,
            DOWN * 1.5 * (narrow_multiple / 0.8),
            run_time=1.5,
        )
        self.wait()
        # empty 整体消失
        self.play(
            FadeOutAndShift(base_empty, UP),
            to_Down.shift,
            UP * 1.5 * (narrow_multiple / 0.8),
            run_time=1.5,
        )
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_b_getTop[2],
            move_frame.align_to,
            codes_b_getTop[2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 蓝色方块
        base_blue = rectangle_base.copy()
        base_blue.set_opacity(0.5).set_color(
            BLUE).set_height(0.45).set_width(0.45).move_to(base_2[0][0][0])
        self.play(FadeIn(base_blue))
        self.wait()
