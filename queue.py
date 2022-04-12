from manimlib.imports import *
from manim_tuan import *

# seqQueue
# a_enQueue
# a_deQueue
# a_getHead
# resize
# clear
# size
# b_enQueue
# b_deQueue
# b_getHead

seqQueue_codes = [
    "if (initSize <= 0)",
    "    throw badSize();",
    "data = new T[initSize];",
    "maxSize = initSize;",
    "front = rear = -1;",
]

a_enQueue_codes = [
    "if ((rear + 1) % maxSize == front)",
    "    resize();",
    "rear = (rear + 1) % maxSize;",
    "data[rear] = x;",
]

a_deQueue_codes = [
    "if (empty())",
    "    throw outOfRange();",
    "front = (front + 1) % maxSize;",
    "return data[front];",
]

a_getHead_codes = [
    "if (empty())",
    "    throw outOfRange();",
    "return data[(front + 1) % maxSize];",
]

resize_codes = [
    "T *p = data;",
    "data = new T[2 * maxSize];",
    "for (int i = 1; i <= size(); ++i)",
    "    data[i] = p[(front + i) % maxSize];",
    "front = 0;",
    "rear = size();",
    "maxSize *= 2;",
    "delete p;",
]

clear_codes = [
    "node *p;",
    "while (front != NULL) {",
    "    p = front;",
    "    front = front->next;",
    "    delete p;",
    "}",
    "rear = NULL;",
]

size_codes = [
    "node *p = front;",
    "int count = 0;",
    "while (p) {",
    "    count++;",
    "    p = p->next;",
    "}",
    "return count;",
]

b_enQueue_codes = [
    "if (rear == NULL)",
    "    front = rear = new node(x);",
    "else {",
    "    rear->next = new node(x);",
    "    rear = rear->next;",
    "}",
]

b_deQueue_codes = [
    "if (empty())",
    "    throw outOfRange();",
    "node *p = front;",
    "T value = front->data;",
    "front = front->next;",
    "if (front == NULL)",
    "    rear = NULL;",
    "delete p;",
    "return value;",
]

b_getHead_codes = [
    "if (empty())",
    "    throw outOfRange();",
    "return front->data;",
]


class Scene_White(Scene):
    CONFIG = {"camera_config": {
        "background_color": WHITE, "use_plot_depth": True, }}


class CodeLine_func(Text):
    CONFIG = {
        "t2c": {
            "seqQueue": "#44cef6",
            "a_enQueue": "#ff461f",
            "a_deQueue": "#00bc12",
            "a_getHead": "#ff7500",
            "resize": "#eacd76",
            "clear": "#725e82",
            "size": "#801dae",
            "b_enQueue": "#9b4400",
            "b_deQueue": "#75878a",
            "b_getHead": "#003371",
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
            "node": TEAL_D,
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
            "node": TEAL_D,
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


class seqQueue(Scene_White):
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
        seqQueue_function = CodeLine_func(
            "seqQueue()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.25)
        codes_seqQueue = VGroup(
            *[CodeLine_large(code) for code in seqQueue_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_seqQueue.next_to(background.get_top(), DOWN,
                               buff=0.2).shift(RIGHT * 0.2)

        self.add(background, seqQueue_function, codes_seqQueue)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=4,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准 ⚪
        base_circle = Circle(color=BLACK, radius=2.0, stroke_opacity=1)
        # 满同心圆
        full_circle = Circle(color=BLACK, fill_color=WHITE, fill_opacity=1,
                             radius=1.0, stroke_opacity=1)
        # 直径
        lines = VGroup()
        degrees = 60
        for i in range(3):
            base_line = Line(
                np.array([0, -2, 0]), np.array([0, 2, 0]), color=BLACK, stroke_opacity=1)
            base_line.rotate(angle=i * 60 * DEGREES)
            lines.add(base_line)
        # 数值
        # math.sqrt(3)
        a = Integer(0, color=BLACK)
        b = Integer(1, color=BLACK)
        c = Integer(2, color=BLACK)
        d = Integer(3, color=BLACK)
        a.shift(LEFT*1.5)
        b.shift(UP*1.25+LEFT*1.25/math.sqrt(3))
        c.shift(UP*1.25+RIGHT*1.25/math.sqrt(3))
        d.shift(RIGHT*1.5)
        nums = VGroup(a, b, c, d)
        # 坐标
        index_a = Integer(0, color=BLACK).scale(0.5)
        index_b = Integer(1, color=BLACK).scale(0.5)
        index_c = Integer(2, color=BLACK).scale(0.5)
        index_d = Integer(3, color=BLACK).scale(0.5)
        index_e = Integer(4, color=BLACK).scale(0.5)
        index_f = Integer(5, color=BLACK).scale(0.5)
        index_a.shift(LEFT*2.3)
        index_b.shift(UP*2+LEFT*2/math.sqrt(3))
        index_c.shift(UP*2+RIGHT*2/math.sqrt(3))
        index_d.shift(RIGHT*2.3)
        index_e.shift(DOWN*2+RIGHT*2/math.sqrt(3))
        index_f.shift(DOWN*2+LEFT*2/math.sqrt(3))
        indexs = VGroup(index_a, index_b, index_c, index_d, index_e, index_f)
        # 整体 1(基准 ⚪)
        base_1 = VGroup(base_circle, lines, full_circle,
                        nums, indexs).scale(0.75)
        # maxSize
        maxSize = TextMobject("maxSize = ", color=BLACK).scale(
            0.7
        )
        # maxSize_value
        maxSize_value = (
            Integer(6, color=BLUE)
            .scale(1)
            .next_to(maxSize, RIGHT)
        )
        # 整体 2(maxSize)
        base_2 = VGroup(maxSize.copy(), maxSize_value.copy())
        # front
        front = TextMobject("front = ", color=BLACK).scale(
            0.7
        )
        # front_value
        front_value = (
            Integer(-1, color=RED)
            .scale(1)
            .next_to(front, RIGHT)
        )
        # 整体 3(front)
        base_3 = VGroup(front.copy(), front_value.copy())
        # rear
        rear = TextMobject("rear = ", color=BLACK).scale(
            0.7
        )
        # rear_value
        rear_value = (
            Integer(-1, color=RED)
            .scale(1)
            .next_to(rear, RIGHT)
        )
        # 整体 4(rear)
        base_4 = VGroup(rear.copy(), rear_value.copy())
        # initSize
        initSize_index = TextMobject("initSize = ", color=BLACK).scale(
            0.7)
        # initSize_value
        initSize_value = (
            Integer(6, color=BLUE)
            .scale(1)
            .next_to(initSize_index, RIGHT)
        )
        # 整体 5(initSize)
        base_5 = VGroup(initSize_index.copy(), initSize_value.copy())

        # 各整体的位置
        """
        整体 1(⚪)
        整体 2(maxSize)
        整体 3(front)
        整体 4(rear)
        整体 5(initSize)
        """
        # maxSize 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 + UP *
            0.5
        )
        # initSize 在 maxSize 上边
        base_5.next_to(base_2, UP, buff=0.35).align_to(
            base_2, LEFT
        )
        # front 在 maxSize 下边
        base_3.next_to(base_2, DOWN, buff=0.35).align_to(
            base_2, LEFT
        )
        # rear 在 front 上面
        base_4.next_to(base_3, DOWN, buff=0.35).align_to(
            base_2, LEFT
        )
        # ⚪ 在 maxSize 右边
        base_1.next_to(base_2, RIGHT, buff=0.35).shift(RIGHT*1.3+DOWN*0.3)

        # self.add(frame_animation, base_1[:-2], base_2, base_3, base_4, base_5)
        self.add(frame_animation, base_5)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(seqQueue_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if seqQueue_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif seqQueue_codes[num][index] == " " and record == 0:
                    record = 1
                elif seqQueue_codes[num][index] != " ":
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
        ).move_to(codes_seqQueue[0]).align_to(codes_seqQueue[0], RIGHT).shift(RIGHT * 0.1)
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
            codes_seqQueue[2],
            move_frame.align_to,
            codes_seqQueue[2],
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
        self.play(ShowCreation(base_1[:-2]))
        self.wait()
        # 再将其(方块)左移
        self.play(base_1[:-2].shift, LEFT, FadeOut(base_data))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(3),
            move_frame.move_to,
            codes_seqQueue[3],
            move_frame.align_to,
            codes_seqQueue[3],
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
            codes_seqQueue[4],
            move_frame.align_to,
            codes_seqQueue[4],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(Write(base_3), Write(base_4))
        self.wait()


class a_enQueue(Scene_White):
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
        background.set_height(2.5, stretch=True).set_width(7.5, stretch=True)
        background.to_corner(UP * 1.8)
        a_enQueue_function = CodeLine_func(
            "enQueue(3)", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.25)
        codes_a_enQueue = VGroup(
            *[CodeLine_large(code) for code in a_enQueue_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_a_enQueue.next_to(background.get_top(), DOWN,
                                buff=0.2).shift(RIGHT * 0.2)

        self.add(background, a_enQueue_function, codes_a_enQueue)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=4,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准 ⚪
        base_circle = Circle(color=BLACK, radius=2.0, stroke_opacity=1)
        # 满同心圆
        full_circle = Circle(color=BLACK, fill_color=WHITE, fill_opacity=1,
                             radius=1.0, stroke_opacity=1)
        # 直径
        lines = VGroup()
        degrees = 60
        for i in range(3):
            base_line = Line(
                np.array([0, -2, 0]), np.array([0, 2, 0]), color=BLACK, stroke_opacity=1)
            base_line.rotate(angle=i * 60 * DEGREES)
            lines.add(base_line)
        # 数值
        # math.sqrt(3)
        a = Integer(0, color=BLACK)
        b = Integer(1, color=BLACK)
        c = Integer(2, color=BLACK)
        d = Integer(3, color=BLACK)
        a.shift(LEFT*1.5)
        b.shift(UP*1.25+LEFT*1.25/math.sqrt(3))
        c.shift(UP*1.25+RIGHT*1.25/math.sqrt(3))
        d.shift(RIGHT*1.5)
        nums = VGroup(a, b, c, d)
        # 坐标
        index_a = Integer(0, color=BLACK).scale(0.5)
        index_b = Integer(1, color=BLACK).scale(0.5)
        index_c = Integer(2, color=BLACK).scale(0.5)
        index_d = Integer(3, color=BLACK).scale(0.5)
        index_e = Integer(4, color=BLACK).scale(0.5)
        index_f = Integer(5, color=BLACK).scale(0.5)
        index_a.shift(LEFT*2.3)
        index_b.shift(UP*2+LEFT*2/math.sqrt(3))
        index_c.shift(UP*2+RIGHT*2/math.sqrt(3))
        index_d.shift(RIGHT*2.3)
        index_e.shift(DOWN*2+RIGHT*2/math.sqrt(3))
        index_f.shift(DOWN*2+LEFT*2/math.sqrt(3))
        indexs = VGroup(index_a, index_b, index_c, index_d, index_e, index_f)
        # 整体 1(基准 ⚪)
        base_1 = VGroup(base_circle, lines, full_circle,
                        nums, indexs).scale(0.75)
        # maxSize
        maxSize = TextMobject("maxSize = ", color=BLACK).scale(
            0.7
        )
        # maxSize_value
        maxSize_value = (
            Integer(6, color=BLUE)
            .scale(1)
            .next_to(maxSize, RIGHT)
        )
        # 整体 2(maxSize)
        base_2 = VGroup(maxSize.copy(), maxSize_value.copy())
        # front
        front = TextMobject("front = ", color=BLACK).scale(
            0.7
        )
        # front_value
        front_value = (
            Integer(-1, color=RED)
            .scale(1)
            .next_to(front, RIGHT)
        )
        # 整体 3(front)
        base_3 = VGroup(front.copy(), front_value.copy())
        # rear
        rear = TextMobject("rear = ", color=BLACK).scale(
            0.7
        )
        # rear_value
        rear_value = (
            Integer(2, color=BLUE)
            .scale(1)
            .next_to(rear, RIGHT)
        )
        # 整体 4(rear)
        base_4 = VGroup(rear.copy(), rear_value.copy())

        # 各整体的位置
        """
        整体 1(⚪)
        整体 2(maxSize)
        整体 3(front)
        整体 4(rear)
        """
        # maxSize 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 + UP *
            1.2
        )
        # front 在 maxSize 下边
        base_3.next_to(base_2, DOWN, buff=0.35).align_to(
            base_2, LEFT
        )
        # rear 在 front 上面
        base_4.next_to(base_3, DOWN, buff=0.35).align_to(
            base_2, LEFT
        )
        # ⚪ 在 maxSize 右边
        base_1.next_to(base_2, RIGHT, buff=0.35).shift(RIGHT*1.3+DOWN*0.7)

        # self.add(frame_animation, base_1, base_2, base_3, base_4)
        self.add(frame_animation, base_1[:-2],
                 base_1[3][:-1], base_2, base_3, base_4)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(a_enQueue_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if a_enQueue_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif a_enQueue_codes[num][index] == " " and record == 0:
                    record = 1
                elif a_enQueue_codes[num][index] != " ":
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
        ).move_to(codes_a_enQueue[0]).align_to(codes_a_enQueue[0], RIGHT).shift(RIGHT * 0.1)
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
            codes_a_enQueue[2],
            move_frame.align_to,
            codes_a_enQueue[2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(base_4[1].set_value, 3)
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(3),
            move_frame.move_to,
            codes_a_enQueue[3],
            move_frame.align_to,
            codes_a_enQueue[3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(FadeIn(base_1[4]))
        self.wait()
        # i
        i_index = TextMobject("data[rear] = ", color=BLACK).scale(
            0.6)
        # i_value
        i_value = (
            Integer(3, color=BLUE)
            .scale(0.6)
            .next_to(i_index, RIGHT, buff=0.17)
        )
        # vec_i
        vec_i = Arrow(
            np.array([1, 0, 0]),
            np.array([-1, 0, 0]),
            buff=0.65,
            color=BLACK,
        ).scale(0.7).next_to(i_index, LEFT, buff=0.1)
        # 整体 data[rear]
        base_i = VGroup(i_index.copy(), i_value.copy(), vec_i.copy()).next_to(
            base_1[4][3], RIGHT, buff=0.12)
        # 变蓝扇形
        fan = AnnularSector(outer_radius=2*0.75, inner_radius=1*0.75, arc_center=base_1.get_center(),
                            start_angle=-PI/6, angle=PI/3, fill_color=BLUE, fill_opacity=0.8)
        self.play(FadeInFrom(base_i, RIGHT), FadeIn(fan))
        self.wait()
        self.play(FadeIn(base_1[3][3]))
        self.wait()


class a_deQueue(Scene_White):
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
        background.set_height(2.5, stretch=True).set_width(7.5, stretch=True)
        background.to_corner(UP * 1.8)
        a_deQueue_function = CodeLine_func(
            "deQueue()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.25)
        codes_a_deQueue = VGroup(
            *[CodeLine_large(code) for code in a_deQueue_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_a_deQueue.next_to(background.get_top(), DOWN,
                                buff=0.2).shift(RIGHT * 0.2)

        self.add(background, a_deQueue_function, codes_a_deQueue)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=4,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准 ⚪
        base_circle = Circle(color=BLACK, radius=2.0, stroke_opacity=1)
        # 满同心圆
        full_circle = Circle(color=BLACK, fill_color=WHITE, fill_opacity=1,
                             radius=1.0, stroke_opacity=1)
        # 直径
        lines = VGroup()
        degrees = 60
        for i in range(3):
            base_line = Line(
                np.array([0, -2, 0]), np.array([0, 2, 0]), color=BLACK, stroke_opacity=1)
            base_line.rotate(angle=i * 60 * DEGREES)
            lines.add(base_line)
        # 数值
        # math.sqrt(3)
        a = Integer(0, color=BLACK)
        b = Integer(1, color=BLACK)
        c = Integer(2, color=BLACK)
        d = Integer(3, color=BLACK)
        a.shift(LEFT*1.5)
        b.shift(UP*1.25+LEFT*1.25/math.sqrt(3))
        c.shift(UP*1.25+RIGHT*1.25/math.sqrt(3))
        d.shift(RIGHT*1.5)
        nums = VGroup(a, b, c, d)
        # 坐标
        index_a = Integer(0, color=BLACK).scale(0.5)
        index_b = Integer(1, color=BLACK).scale(0.5)
        index_c = Integer(2, color=BLACK).scale(0.5)
        index_d = Integer(3, color=BLACK).scale(0.5)
        index_e = Integer(4, color=BLACK).scale(0.5)
        index_f = Integer(5, color=BLACK).scale(0.5)
        index_a.shift(LEFT*2.3)
        index_b.shift(UP*2+LEFT*2/math.sqrt(3))
        index_c.shift(UP*2+RIGHT*2/math.sqrt(3))
        index_d.shift(RIGHT*2.3)
        index_e.shift(DOWN*2+RIGHT*2/math.sqrt(3))
        index_f.shift(DOWN*2+LEFT*2/math.sqrt(3))
        indexs = VGroup(index_a, index_b, index_c, index_d, index_e, index_f)
        # 整体 1(基准 ⚪)
        base_1 = VGroup(base_circle, lines, full_circle,
                        nums, indexs).scale(0.75)
        # maxSize
        maxSize = TextMobject("maxSize = ", color=BLACK).scale(
            0.7
        )
        # maxSize_value
        maxSize_value = (
            Integer(6, color=BLUE)
            .scale(1)
            .next_to(maxSize, RIGHT)
        )
        # 整体 2(maxSize)
        base_2 = VGroup(maxSize.copy(), maxSize_value.copy())
        # front
        front = TextMobject("front = ", color=BLACK).scale(
            0.7
        )
        # front_value
        front_value = (
            Integer(-1, color=RED)
            .scale(1)
            .next_to(front, RIGHT)
        )
        # 整体 3(front)
        base_3 = VGroup(front.copy(), front_value.copy())
        # rear
        rear = TextMobject("rear = ", color=BLACK).scale(
            0.7
        )
        # rear_value
        rear_value = (
            Integer(3, color=BLUE)
            .scale(1)
            .next_to(rear, RIGHT)
        )
        # 整体 4(rear)
        base_4 = VGroup(rear.copy(), rear_value.copy())

        # 各整体的位置
        """
        整体 1(⚪)
        整体 2(maxSize)
        整体 3(front)
        整体 4(rear)
        """
        # maxSize 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 + UP *
            1.2
        )
        # front 在 maxSize 下边
        base_3.next_to(base_2, DOWN, buff=0.35).align_to(
            base_2, LEFT
        )
        # rear 在 front 上面
        base_4.next_to(base_3, DOWN, buff=0.35).align_to(
            base_2, LEFT
        )
        # ⚪ 在 maxSize 右边
        base_1.next_to(base_2, RIGHT, buff=0.35).shift(RIGHT*1.3+DOWN*0.7)

        # self.add(frame_animation, base_1, base_2, base_3, base_4)
        self.add(frame_animation, base_1[:-1], base_2, base_3, base_4)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(a_deQueue_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if a_deQueue_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif a_deQueue_codes[num][index] == " " and record == 0:
                    record = 1
                elif a_deQueue_codes[num][index] != " ":
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
        ).move_to(codes_a_deQueue[0]).align_to(codes_a_deQueue[0], RIGHT).shift(RIGHT * 0.1)
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
        background_tmp.set_height(2, stretch=True).set_width(4, stretch=True)
        background_tmp.align_to(frame_animation, UP).shift(
            DOWN * 0
        )
        # empty 代码
        empty_codes = [
            "bool empty() const",
            "{",
            "   return front == rear;",
            "}",
        ]
        codes_empty = VGroup(
            *[CodeLine_small(code) for code in empty_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_empty.next_to(background_tmp.get_top(), DOWN, buff=0.1)
        # empty 整体
        base_empty = VGroup(background_tmp, codes_empty)
        # empty 整体出现
        to_LEFT = VGroup(base_2, base_3, base_4)
        to_RIGHT = VGroup(base_1[:-1])
        self.play(
            GrowFromCenter(base_empty),
            to_LEFT.shift,
            LEFT * 1.5,
            to_RIGHT.shift,
            RIGHT * 1.7,
            run_time=1.5,
        )
        self.wait()
        # empty 整体消失
        self.play(
            FadeOutAndShift(base_empty, UP),
            to_LEFT.shift,
            RIGHT * 1.5,
            to_RIGHT.shift,
            LEFT * 1.7,
            run_time=1.5,
        )
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_a_deQueue[2],
            move_frame.align_to,
            codes_a_deQueue[2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        front_value = (
            Integer(0, color=BLUE)
            .scale(1)
            .next_to(base_3[0], RIGHT)
        )
        self.play(Transform(base_3[1], front_value))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(3),
            move_frame.move_to,
            codes_a_deQueue[3],
            move_frame.align_to,
            codes_a_deQueue[3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(FadeIn(base_1[-1]))
        self.wait()
        self.play(base_1.shift, RIGHT*1.5, to_LEFT.shift, LEFT*0.5)
        self.wait()
        # i
        i_index = TextMobject("data[front] = ", color=BLACK).scale(
            0.6)
        # i_value
        i_value = (
            Integer(0, color=BLUE)
            .scale(0.6)
            .next_to(i_index, RIGHT, buff=0.17)
        )
        # vec_i
        vec_i = Arrow(
            np.array([-1, 0, 0]),
            np.array([1, 0, 0]),
            buff=0.65,
            color=BLACK,
        ).scale(0.7).next_to(i_value, RIGHT, buff=0.1)
        # 整体 data[rear]
        base_i = VGroup(i_index.copy(), i_value.copy(), vec_i.copy()).next_to(
            base_1[4][0], LEFT, buff=0.12)
        # 变蓝扇形
        fan = AnnularSector(outer_radius=2*0.75, inner_radius=1*0.75, arc_center=base_1.get_center(),
                            start_angle=PI-PI/6, angle=PI/3, fill_color=BLUE, fill_opacity=0.8)
        self.play(FadeInFrom(base_i, LEFT), FadeIn(fan))
        self.wait()


class a_getHead(Scene_White):
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
        background.set_height(2, stretch=True).set_width(7.5, stretch=True)
        background.to_corner(UP * 1.8)
        a_getHead_function = CodeLine_func(
            "getHead()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.25)
        codes_a_getHead = VGroup(
            *[CodeLine_large(code) for code in a_getHead_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_a_getHead.next_to(background.get_top(), DOWN,
                                buff=0.2).shift(RIGHT * 0.2)

        self.add(background, a_getHead_function, codes_a_getHead)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=4,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准 ⚪
        base_circle = Circle(color=BLACK, radius=2.0, stroke_opacity=1)
        # 满同心圆
        full_circle = Circle(color=BLACK, fill_color=WHITE, fill_opacity=1,
                             radius=1.0, stroke_opacity=1)
        # 直径
        lines = VGroup()
        degrees = 60
        for i in range(3):
            base_line = Line(
                np.array([0, -2, 0]), np.array([0, 2, 0]), color=BLACK, stroke_opacity=1)
            base_line.rotate(angle=i * 60 * DEGREES)
            lines.add(base_line)
        # 数值
        # math.sqrt(3)
        a = Integer(0, color=BLACK)
        b = Integer(1, color=BLACK)
        c = Integer(2, color=BLACK)
        d = Integer(3, color=BLACK)
        a.shift(LEFT*1.5)
        b.shift(UP*1.25+LEFT*1.25/math.sqrt(3))
        c.shift(UP*1.25+RIGHT*1.25/math.sqrt(3))
        d.shift(RIGHT*1.5)
        nums = VGroup(a, b, c, d)
        # 坐标
        index_a = Integer(0, color=BLACK).scale(0.5)
        index_b = Integer(1, color=BLACK).scale(0.5)
        index_c = Integer(2, color=BLACK).scale(0.5)
        index_d = Integer(3, color=BLACK).scale(0.5)
        index_e = Integer(4, color=BLACK).scale(0.5)
        index_f = Integer(5, color=BLACK).scale(0.5)
        index_a.shift(LEFT*2.3)
        index_b.shift(UP*2+LEFT*2/math.sqrt(3))
        index_c.shift(UP*2+RIGHT*2/math.sqrt(3))
        index_d.shift(RIGHT*2.3)
        index_e.shift(DOWN*2+RIGHT*2/math.sqrt(3))
        index_f.shift(DOWN*2+LEFT*2/math.sqrt(3))
        indexs = VGroup(index_a, index_b, index_c, index_d, index_e, index_f)
        # 整体 1(基准 ⚪)
        base_1 = VGroup(base_circle, lines, full_circle,
                        nums, indexs).scale(0.75)
        # maxSize
        maxSize = TextMobject("maxSize = ", color=BLACK).scale(
            0.7
        )
        # maxSize_value
        maxSize_value = (
            Integer(6, color=BLUE)
            .scale(1)
            .next_to(maxSize, RIGHT)
        )
        # 整体 2(maxSize)
        base_2 = VGroup(maxSize.copy(), maxSize_value.copy())
        # front
        front = TextMobject("front = ", color=BLACK).scale(
            0.7
        )
        # front_value
        front_value = (
            Integer(-1, color=RED)
            .scale(1)
            .next_to(front, RIGHT)
        )
        # 整体 3(front)
        base_3 = VGroup(front.copy(), front_value.copy())
        # rear
        rear = TextMobject("rear = ", color=BLACK).scale(
            0.7
        )
        # rear_value
        rear_value = (
            Integer(3, color=BLUE)
            .scale(1)
            .next_to(rear, RIGHT)
        )
        # 整体 4(rear)
        base_4 = VGroup(rear.copy(), rear_value.copy())

        # 各整体的位置
        """
        整体 1(⚪)
        整体 2(maxSize)
        整体 3(front)
        整体 4(rear)
        """
        # maxSize 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 + UP *
            1.2
        )
        # front 在 maxSize 下边
        base_3.next_to(base_2, DOWN, buff=0.35).align_to(
            base_2, LEFT
        )
        # rear 在 front 上面
        base_4.next_to(base_3, DOWN, buff=0.35).align_to(
            base_2, LEFT
        )
        # ⚪ 在 maxSize 右边
        base_1.next_to(base_2, RIGHT, buff=0.35).shift(RIGHT*1.3+DOWN*0.7)

        # self.add(frame_animation, base_1, base_2, base_3, base_4)
        self.add(frame_animation, base_1[:-1], base_2, base_3, base_4)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(a_getHead_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if a_getHead_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif a_getHead_codes[num][index] == " " and record == 0:
                    record = 1
                elif a_getHead_codes[num][index] != " ":
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
        ).move_to(codes_a_getHead[0]).align_to(codes_a_getHead[0], RIGHT).shift(RIGHT * 0.1)
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
        background_tmp.set_height(2, stretch=True).set_width(4, stretch=True)
        background_tmp.align_to(frame_animation, UP).shift(
            DOWN * 0
        )
        # empty 代码
        empty_codes = [
            "bool empty() const",
            "{",
            "   return front == rear;",
            "}",
        ]
        codes_empty = VGroup(
            *[CodeLine_small(code) for code in empty_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_empty.next_to(background_tmp.get_top(), DOWN, buff=0.1)
        # empty 整体
        base_empty = VGroup(background_tmp, codes_empty)
        # empty 整体出现
        to_LEFT = VGroup(base_2, base_3, base_4)
        to_RIGHT = VGroup(base_1[:-1])
        self.play(
            GrowFromCenter(base_empty),
            to_LEFT.shift,
            LEFT * 1.5,
            to_RIGHT.shift,
            RIGHT * 1.7,
            run_time=1.5,
        )
        self.wait()
        # empty 整体消失
        self.play(
            FadeOutAndShift(base_empty, UP),
            to_LEFT.shift,
            RIGHT * 1.5,
            to_RIGHT.shift,
            LEFT * 1.7,
            run_time=1.5,
        )
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_a_getHead[2],
            move_frame.align_to,
            codes_a_getHead[2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(FadeIn(base_1[-1]))
        self.wait()
        self.play(base_1.shift, RIGHT*1.5, to_LEFT.shift, LEFT*0.5)
        self.wait()
        # i
        i_index = TextMobject("data[front+1] = ", color=BLACK).scale(
            0.6)
        # i_value
        i_value = (
            Integer(0, color=BLUE)
            .scale(0.6)
            .next_to(i_index, RIGHT, buff=0.17)
        )
        # vec_i
        vec_i = Arrow(
            np.array([-1, 0, 0]),
            np.array([1, 0, 0]),
            buff=0.65,
            color=BLACK,
        ).scale(0.7).next_to(i_value, RIGHT, buff=0.1)
        # 整体 data[rear]
        base_i = VGroup(i_index.copy(), i_value.copy(), vec_i.copy()).next_to(
            base_1[4][0], LEFT, buff=0.12)
        # 变蓝扇形
        fan = AnnularSector(outer_radius=2*0.75, inner_radius=1*0.75, arc_center=base_1.get_center(),
                            start_angle=PI-PI/6, angle=PI/3, fill_color=BLUE, fill_opacity=0.8)
        self.play(FadeInFrom(base_i, LEFT), FadeIn(fan))
        self.wait()


class resize(Scene_White):
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
            2.5, stretch=True).set_width(8.5, stretch=True)
        background_right = background_left.copy().set_height(
            2.5, stretch=True).set_width(3.5, stretch=True)
        background_left.to_corner(UP * 1.5 + LEFT * 2.15)
        background_right.to_corner(UP * 1.5 + RIGHT * 2.15)
        background = VGroup(background_left, background_right)
        resize_function = CodeLine_func(
            "resize()", font="思源宋体 Heavy", resize=0.8
        ).to_corner(UP, buff=0.18)
        codes_resize_1 = VGroup(
            *[CodeLine_large(code) for code in resize_codes[:4]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_resize_1.next_to(background_left.get_top(), DOWN, buff=0.2).shift(
            LEFT * 0
        )
        codes_resize_2 = VGroup(
            *[CodeLine_large(code) for code in resize_codes[4:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_resize_2.next_to(background_right.get_top(), DOWN, buff=0.2).shift(
            RIGHT * 0.3 + LEFT * 0.1
        )
        codes_resize = VGroup(codes_resize_1, codes_resize_2)

        self.add(background, resize_function, codes_resize)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=4,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准 ⚪
        base_circle = Circle(color=BLACK, radius=2.0, stroke_opacity=1)
        # 满同心圆
        full_circle = Circle(color=BLACK, fill_color=WHITE, fill_opacity=1,
                             radius=1.0, stroke_opacity=1)
        # 直径
        lines = VGroup()
        degrees = 60
        for i in range(3):
            base_line = Line(
                np.array([0, -2, 0]), np.array([0, 2, 0]), color=BLACK, stroke_opacity=1)
            base_line.rotate(angle=i * 60 * DEGREES)
            lines.add(base_line)
        # 数值
        # math.sqrt(3)
        a = Integer(0, color=BLACK)
        b = Integer(1, color=BLACK)
        c = Integer(2, color=BLACK)
        d = Integer(3, color=BLACK)
        a.shift(LEFT*1.5)
        b.shift(UP*1.25+LEFT*1.25/math.sqrt(3))
        c.shift(UP*1.25+RIGHT*1.25/math.sqrt(3))
        d.shift(RIGHT*1.5)
        nums = VGroup(a, b, c, d)
        # 坐标
        index_a = Integer(0, color=BLACK).scale(0.5)
        index_b = Integer(1, color=BLACK).scale(0.5)
        index_c = Integer(2, color=BLACK).scale(0.5)
        index_d = Integer(3, color=BLACK).scale(0.5)
        index_e = Integer(4, color=BLACK).scale(0.5)
        index_f = Integer(5, color=BLACK).scale(0.5)
        index_a.shift(LEFT*2.3)
        index_b.shift(UP*2+LEFT*2/math.sqrt(3))
        index_c.shift(UP*2+RIGHT*2/math.sqrt(3))
        index_d.shift(RIGHT*2.3)
        index_e.shift(DOWN*2+RIGHT*2/math.sqrt(3))
        index_f.shift(DOWN*2+LEFT*2/math.sqrt(3))
        indexs = VGroup(index_a, index_b, index_c, index_d, index_e, index_f)
        # 整体 1(基准 ⚪)
        base_1 = VGroup(base_circle, lines, full_circle,
                        nums, indexs).scale(0.75)
        # maxSize
        maxSize = TextMobject("maxSize = ", color=BLACK).scale(
            0.7
        )
        # maxSize_value
        maxSize_value = (
            Integer(6, color=BLUE)
            .scale(1)
            .next_to(maxSize, RIGHT)
        )
        # 整体 2(maxSize)
        base_2 = VGroup(maxSize.copy(), maxSize_value.copy())
        # front
        front = TextMobject("front = ", color=BLACK).scale(
            0.7
        )
        # front_value
        front_value = (
            Integer(0, color=BLUE)
            .scale(1)
            .next_to(front, RIGHT)
        )
        # 整体 3(front)
        base_3 = VGroup(front.copy(), front_value.copy())
        # rear
        rear = TextMobject("rear = ", color=BLACK).scale(
            0.7
        )
        # rear_value
        rear_value = (
            Integer(3, color=BLUE)
            .scale(1)
            .next_to(rear, RIGHT)
        )
        # 整体 4(rear)
        base_4 = VGroup(rear.copy(), rear_value.copy())

        # 各整体的位置
        """
        整体 1(⚪)
        整体 2(maxSize)
        整体 3(front)
        整体 4(rear)
        """
        # maxSize 靠左
        base_2.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 3.5 + UP *
            1.2
        )
        # front 在 maxSize 下边
        base_3.next_to(base_2, DOWN, buff=0.35).align_to(
            base_2, LEFT
        )
        # rear 在 front 上面
        base_4.next_to(base_3, DOWN, buff=0.35).align_to(
            base_2, LEFT
        )
        # ⚪ 在 maxSize 右边
        base_1.next_to(base_2, RIGHT, buff=0.35).shift(RIGHT*1.3+DOWN*0.7)

        # self.add(frame_animation, base_1, base_2, base_3, base_4)
        self.add(frame_animation, base_1[:-1], base_2, base_3, base_4)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(resize_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if resize_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif resize_codes[num][index] == " " and record == 0:
                    record = 1
                elif resize_codes[num][index] != " ":
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
        ).move_to(codes_resize[0][0]).align_to(codes_resize[0][0], RIGHT).shift(RIGHT * 0.1)
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
        # 整体 data
        base_data = VGroup(data, vec_data)
        base_data.next_to(base_1[0][0], LEFT, buff=0.15)
        self.play(FadeInFrom(base_data, direction=LEFT))
        self.wait()
        # 箭头(p)
        vec_p = Arrow(
            np.array([-1, 0, 0]), np.array([1, 0, 0]), buff=0.6, color=BLACK
        ).scale(0.7)
        # p
        p = TextMobject("p", color=BLACK).scale(
            0.7).next_to(vec_p, LEFT, buff=0.1)
        # 整体 p
        base_p = VGroup(p, vec_p)
        base_p.next_to(base_1[0][0], LEFT, buff=0.15).shift(UP * 0.2)
        base_data_tmp = base_data.copy()
        self.play(
            ReplacementTransform(
                base_data_tmp, base_p), base_data.shift, DOWN * 0.2
        )
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(1),
            move_frame.move_to,
            codes_resize[0][1],
            move_frame.align_to,
            codes_resize[0][1],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        to_LEFT = VGroup(base_1[:-1], base_2, base_3,
                         base_4, base_p, base_data)
        self.play(to_LEFT.shift, LEFT*2.2)
        base_1[-1].shift(LEFT*2.2)
        self.wait()
        # 新的二倍基准 ⚪
        base_circle = Circle(color=BLACK, radius=2.0, stroke_opacity=1)
        # 满同心圆
        full_circle = Circle(color=BLACK, fill_color=WHITE, fill_opacity=1,
                             radius=1.0, stroke_opacity=1)
        # 直径
        lines = VGroup()
        degrees = 30
        for i in range(6):
            base_line = Line(
                np.array([0, -2, 0]), np.array([0, 2, 0]), color=BLACK, stroke_opacity=1)
            base_line.rotate(angle=i * 30 * DEGREES)
            lines.add(base_line)
        # 数值
        # 2-math.sqrt(3)
        tan = 2-math.sqrt(3)
        a = Integer(0, color=BLACK)
        b = Integer(1, color=BLACK)
        c = Integer(2, color=BLACK)
        d = Integer(3, color=BLACK)
        a.shift(LEFT*1.5+UP*1.5*tan)
        b.shift(UP*1.1+LEFT*1.1)
        c.shift(LEFT*1.5*tan+UP*1.5)
        d.shift(RIGHT*1.5*tan+UP*1.5)
        nums = VGroup(a, b, c, d)
        # 坐标
        index_a = Integer(0, color=BLACK).scale(0.5)
        index_b = Integer(1, color=BLACK).scale(0.5)
        index_c = Integer(2, color=BLACK).scale(0.5)
        index_d = Integer(3, color=BLACK).scale(0.5)
        index_e = Integer(4, color=BLACK).scale(0.5)
        index_f = Integer(5, color=BLACK).scale(0.5)
        index_g = Integer(6, color=BLACK).scale(0.5)
        index_h = Integer(7, color=BLACK).scale(0.5)
        index_i = Integer(8, color=BLACK).scale(0.5)
        index_j = Integer(9, color=BLACK).scale(0.5)
        index_k = Integer(10, color=BLACK).scale(0.5)
        index_l = Integer(11, color=BLACK).scale(0.5)
        index_a.shift(LEFT*2.1+UP*2.1*tan)
        index_b.shift(UP*1.6+LEFT*1.6)
        index_c.shift(LEFT*2.1*tan+UP*2.1)
        index_d.shift(RIGHT*2.1*tan+UP*2.1)
        index_e.shift(UP*1.6+RIGHT*1.6)
        index_f.shift(RIGHT*2.1+UP*2.1*tan)

        index_g.shift(RIGHT*2.1+DOWN*2.1*tan)
        index_h.shift(DOWN*1.6+RIGHT*1.6)
        index_i.shift(RIGHT*2.1*tan+DOWN*2.1)
        index_j.shift(LEFT*2.1*tan+DOWN*2.1)
        index_k.shift(LEFT*1.6+DOWN*1.6)
        index_l.shift(LEFT*2.1+DOWN*2.1*tan)
        indexs = VGroup(index_a, index_b, index_c, index_d, index_e,
                        index_f, index_g, index_h, index_i, index_j, index_k, index_l)
        # 整体 1(基准 ⚪)
        base_new = VGroup(base_circle, lines, full_circle,
                          nums, indexs).scale(0.75)
        base_new.move_to(base_1).shift(RIGHT*5)
        self.play(base_p.shift, DOWN*0.2, base_data.next_to,
                  base_new[0], LEFT, buff=0)
        self.wait()
        self.play(Write(base_new[:-2]))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_resize[0][2],
            move_frame.align_to,
            codes_resize[0][2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # remind
        remind = TextMobject("size() = ", color=BLACK).scale(
            0.7
        )
        # remind_define
        remind_define = TextMobject(
            "rear - front", color=BLACK).scale(0.7).next_to(remind, RIGHT).align_to(remind, UP)
        # remind_value
        remind_value = (
            Integer(3, color=BLUE)
            .scale(1)
        )
        # 整体 remind
        base_remind = VGroup(remind.copy(), remind_define.copy())
        base_remind.next_to(base_4, DOWN).align_to(base_4, LEFT)
        self.play(FadeInFrom(base_remind, DOWN))
        self.wait()
        remind_value.next_to(base_remind[0], RIGHT)
        self.play(Transform(base_remind[1], remind_value))
        self.wait()
        self.play(base_p.shift, LEFT*0.1, base_data.shift, LEFT*0.05)
        self.play(base_p.rotate, {"angle": (PI / 3.2),
                                  "about_point": base_1.get_center()}, base_data.rotate, {"angle": (PI / 3), "about_point": base_new.get_center()})
        self.play(base_p[0].rotate, -(PI / 3.2),
                  base_data[0].rotate, -(PI / 3))
        self.play(base_p[0].shift, UP*0, base_data[0].shift, UP*0.2)
        self.wait()
        self.play(FadeIn(base_1[-1]), FadeIn(base_new[-1]))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(3),
            move_frame.move_to,
            codes_resize[0][3],
            move_frame.align_to,
            codes_resize[0][3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 变蓝扇形
        fan = AnnularSector(outer_radius=2*0.75, inner_radius=1*0.75, arc_center=base_1.get_center(),
                            start_angle=PI-3*PI/6, angle=PI/3, fill_color=BLUE, fill_opacity=0.8)
        self.play(FadeIn(fan))
        self.wait()
        self.play(Transform(base_1[-2][1].copy(), base_new[-2][1]))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_resize[0][2],
            move_frame.align_to,
            codes_resize[0][2],
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
            codes_resize[0][3],
            move_frame.align_to,
            codes_resize[0][3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(fan.rotate, {"angle": -(PI / 3),
                               "about_point": base_1.get_center()})
        self.wait()
        self.play(Transform(base_1[-2][2].copy(), base_new[-2][2]))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_resize[0][2],
            move_frame.align_to,
            codes_resize[0][2],
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
            codes_resize[0][3],
            move_frame.align_to,
            codes_resize[0][3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(fan.rotate, {"angle": -(PI / 3),
                               "about_point": base_1.get_center()})
        self.wait()
        self.play(Transform(base_1[-2][3].copy(), base_new[-2][3]))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_resize[0][2],
            move_frame.align_to,
            codes_resize[0][2],
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
            ignore_space_len(4),
            move_frame.move_to,
            codes_resize[1][0],
            move_frame.align_to,
            codes_resize[1][0],
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
            ignore_space_len(5),
            move_frame.move_to,
            codes_resize[1][1],
            move_frame.align_to,
            codes_resize[1][1],
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
            codes_resize[1][2],
            move_frame.align_to,
            codes_resize[1][2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(base_2[1].set_value, 12)
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(7),
            move_frame.move_to,
            codes_resize[1][3],
            move_frame.align_to,
            codes_resize[1][3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(FadeOut(base_1), FadeOut(base_p), FadeOut(fan))
        self.wait()
        to_RIGHT = VGroup(base_2, base_3, base_4, base_remind)
        self.play(to_RIGHT.shift, RIGHT*3+UP*0.5, base_data.rotate,
                  {"angle": -(PI / 3), "about_point": base_new.get_center()})
        self.play(base_data[0].rotate, (PI / 3))
        self.play(base_data[0].shift, LEFT*0.15+DOWN*0.05)
        self.wait()


class clear(Scene_White):
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
        clear_function = CodeLine_func(
            "clear()", font="思源宋体 Heavy", clear=0.8
        ).to_corner(UP, buff=0.18)
        codes_clear_1 = VGroup(
            *[CodeLine_large(code) for code in clear_codes[:4]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_clear_1.next_to(background_left.get_top(), DOWN, buff=0.2).shift(
            LEFT * 0.3
        )
        codes_clear_2 = VGroup(
            *[CodeLine_large(code) for code in clear_codes[4:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_clear_2.next_to(background_right.get_top(), DOWN, buff=0.2).shift(
            LEFT * 1.2
        )
        codes_clear = VGroup(codes_clear_1, codes_clear_2)

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
        # 箭头(front)
        vec_front = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # front
        front = (
            TextMobject("front", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(front.copy(), vec_front.copy())
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
        # 箭头(rear)
        vec_rear = vec_front.copy()
        # rear
        rear = (
            TextMobject("rear", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_rear, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 7
        base_7 = VGroup(rear.copy(), vec_rear.copy())

        # 各整体的位置
        """
        整体 1(front)
        整体 2(长方块)
        整体 3(NULL)
        整体 4(value)
        整体 5(tmp)
        整体 6(p)
        整体 7(rear)
        """
        # 整体 4 靠左
        base_4.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.3 * (narrow_multiple / 0.5) + UP *
            0.7 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 4 右边
        base_2.next_to(base_4, RIGHT, buff=1 * (narrow_multiple / 0.5))
        # 整体 1 在整体 2 上边
        base_1.next_to(base_2[0][0][0], UP, buff=0.1 * (narrow_multiple / 0.5))
        # 整体 7 在整体 2 上边
        base_7.next_to(base_2[4][0][0], UP, buff=0.1 * (narrow_multiple / 0.5))
        # 整体 3 在整体 2 右边
        base_3.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))

        self.add(frame_animation, base_1, base_2, base_3, base_7)
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
        ).move_to(codes_clear[0][0]).align_to(codes_clear[0][0], RIGHT).shift(
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
                codes_clear[0][1],
                move_frame.align_to,
                codes_clear[0][1],
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
                codes_clear[0][2],
                move_frame.align_to,
                codes_clear[0][2],
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
                codes_clear[0][3],
                move_frame.align_to,
                codes_clear[0][3],
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
            if circle < 3:
                self.play(base_1.shift, RIGHT*1.625)
            elif circle == 3:
                self.play(base_1[0].shift, RIGHT*1.625 + UP *
                          0.35, base_1[1].shift, RIGHT*1.625)
            elif circle == 4:
                self.play(base_1[0].shift, RIGHT*2.0 + DOWN *
                          0.5, base_1[1].shift, RIGHT*2.0)
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(4),
                move_frame.move_to,
                codes_clear[1][0],
                move_frame.align_to,
                codes_clear[1][0],
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
            codes_clear[0][1],
            move_frame.align_to,
            codes_clear[0][1],
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
            codes_clear[1][2],
            move_frame.align_to,
            codes_clear[1][2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 箭头(rear)
        rear_tmp_vec = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
        )
        # rear
        rear_tmp = (
            TextMobject("rear", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(rear_tmp_vec, DOWN, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 rear_tmp
        base_rear_tmp = VGroup(rear_tmp.copy(), rear_tmp_vec.copy()).next_to(
            base_3, DOWN, buff=0.2)
        self.play(Transform(base_7, base_rear_tmp))
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
        # 箭头(front)
        vec_front = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # front
        front = (
            TextMobject("front", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(front.copy(), vec_front.copy())
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
        # 箭头(rear)
        vec_rear = vec_front.copy()
        # rear
        rear = (
            TextMobject("rear", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_rear, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 7
        base_7 = VGroup(rear.copy(), vec_rear.copy())

        # 各整体的位置
        """
        整体 1(front)
        整体 2(长方块)
        整体 3(NULL)
        整体 4(value)
        整体 5(tmp)
        整体 6(p)
        整体 7(rear)
        """
        # 整体 4 靠左
        base_4.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.7 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 4 右边
        base_2.next_to(base_4, RIGHT, buff=1 * (narrow_multiple / 0.5))
        # 整体 1 在整体 2 上边
        base_1.next_to(base_2[0][0][0], UP, buff=0.1 * (narrow_multiple / 0.5))
        # 整体 7 在整体 2 上边
        base_7.next_to(base_2[4][0][0], UP, buff=0.1 * (narrow_multiple / 0.5))
        # 整体 3 在整体 2 右边
        base_3.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))

        self.add(frame_animation, base_1, base_2, base_3, base_7)
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


class b_enQueue(Scene_White):
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
        background.set_height(3.5, stretch=True).set_width(6.5, stretch=True)
        background.to_corner(UP * 1.7)
        b_enQueue_function = CodeLine_func(
            "enQueue(4)", font="思源宋体 Heavy", b_enQueue=0.8
        ).to_corner(UP, buff=0.21)
        codes_b_enQueue = VGroup(
            *[CodeLine_large(code) for code in b_enQueue_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_b_enQueue.next_to(background.get_top(), DOWN,
                                buff=0.2).shift(RIGHT * 0.2)

        self.add(background, b_enQueue_function, codes_b_enQueue)
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
        # 箭头(front)
        vec_front = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # front
        front = (
            TextMobject("front", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(front.copy(), vec_front.copy())
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
        # 箭头(rear)
        vec_rear = vec_front.copy()
        # rear
        rear = (
            TextMobject("rear", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_rear, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 7
        base_7 = VGroup(rear.copy(), vec_rear.copy())

        # 各整体的位置
        """
        整体 1(front)
        整体 2(长方块)
        整体 3(NULL)
        整体 4(value)
        整体 5(tmp)
        整体 6(p)
        整体 7(rear)
        """
        # 整体 4 靠左
        base_4.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.7 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 4 右边
        base_2.next_to(base_4, RIGHT, buff=1 * (narrow_multiple / 0.5))
        # 整体 1 在整体 2 上边
        base_1.next_to(base_2[0][0][0], UP, buff=0.1 * (narrow_multiple / 0.5))
        # 整体 7 在整体 2 上边
        base_7.next_to(base_2[3][0][0], UP, buff=0.1 * (narrow_multiple / 0.5))
        # 整体 3 在整体 2 右边
        base_3.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))

        self.add(frame_animation, base_1, base_2, base_3, base_7)

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(b_enQueue_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if b_enQueue_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif b_enQueue_codes[num][index] == " " and record == 0:
                    record = 1
                elif b_enQueue_codes[num][index] != " ":
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
        ).move_to(codes_b_enQueue[0]).align_to(codes_b_enQueue[0], RIGHT).shift(
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

        # --------------- 正式开始 ---------------
        # data
        data = TextMobject("data = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # data_value
        data_value = (
            Integer(4, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(data, RIGHT)
        )
        # 整体 4
        base_data = VGroup(data.copy(), data_value.copy()).move_to(base_4)
        self.add(base_data)
        self.wait()
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_b_enQueue[2],
            move_frame.align_to,
            codes_b_enQueue[2],
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
            codes_b_enQueue[3],
            move_frame.align_to,
            codes_b_enQueue[3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(base_2[3][0][2].set_color, BLUE)
        # 建立新的方块
        self.wait()
        n = (
            Integer(4, color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .move_to(base[0])
        )
        insert_base = VGroup(base.copy(), n.copy()).move_to(base_2[0]).shift(
            DOWN * 1.2 * (narrow_multiple / 0.5)
            + LEFT * 0.5 * (narrow_multiple / 0.5)
        )
        insert_base.next_to(base_2, RIGHT, buff=0.1)
        base_null = TextMobject("NULL", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)).next_to(insert_base, RIGHT, buff=0.2)
        self.play(FadeInFrom(insert_base, RIGHT), FadeInFrom(
            base_null, RIGHT), FadeOut(base_3))
        self.wait()
        self.play(
            base_2[3][0][2].set_color, BLACK,
            move_frame.set_width,
            ignore_space_len(4),
            move_frame.move_to,
            codes_b_enQueue[4],
            move_frame.align_to,
            codes_b_enQueue[4],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(base_7.shift, RIGHT*1.625)
        self.wait()


class b_deQueue(Scene_White):
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
            3, stretch=True).set_width(6, stretch=True)
        background_right = background_left.copy()
        background_left.to_corner(UP * 1.5 + LEFT * 2.15)
        background_right.to_corner(UP * 1.5 + RIGHT * 2.15)
        background = VGroup(background_left, background_right)
        b_deQueue_function = CodeLine_func(
            "deQueue()", font="思源宋体 Heavy", b_deQueue=0.8
        ).to_corner(UP, buff=0.18)
        codes_b_deQueue_1 = VGroup(
            *[CodeLine_large(code) for code in b_deQueue_codes[:5]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_b_deQueue_1.next_to(background_left.get_top(), DOWN, buff=0.2).shift(
            LEFT * 0.2
        )
        codes_b_deQueue_2 = VGroup(
            *[CodeLine_large(code) for code in b_deQueue_codes[5:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_b_deQueue_2.next_to(background_right.get_top(), DOWN, buff=0.2).shift(
            RIGHT * 0.3 + LEFT * 1
        )
        codes_b_deQueue = VGroup(codes_b_deQueue_1, codes_b_deQueue_2)

        self.add(background, b_deQueue_function, codes_b_deQueue)
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
        # 箭头(front)
        vec_front = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # front
        front = (
            TextMobject("front", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(front.copy(), vec_front.copy())
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
        # 箭头(rear)
        vec_rear = vec_front.copy()
        # rear
        rear = (
            TextMobject("rear", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_rear, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 7
        base_7 = VGroup(rear.copy(), vec_rear.copy())

        # 各整体的位置
        """
        整体 1(front)
        整体 2(长方块)
        整体 3(NULL)
        整体 4(value)
        整体 5(tmp)
        整体 6(p)
        整体 7(rear)
        """
        # 整体 4 靠左
        base_4.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.7 * (narrow_multiple / 0.5)+UP *
            0.45 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 4 右边
        base_2.next_to(base_4, RIGHT, buff=1 * (narrow_multiple / 0.5))
        # 整体 1 在整体 2 上边
        base_1.next_to(base_2[0][0][0], UP, buff=0.1 * (narrow_multiple / 0.5))
        # 整体 7 在整体 2 上边
        base_7.next_to(base_2[4][0][0], UP, buff=0.1 * (narrow_multiple / 0.5))
        # 整体 3 在整体 2 右边
        base_3.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))

        self.add(frame_animation, base_1, base_2, base_3, base_7)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(b_deQueue_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if b_deQueue_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif b_deQueue_codes[num][index] == " " and record == 0:
                    record = 1
                elif b_deQueue_codes[num][index] != " ":
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
        ).move_to(codes_b_deQueue[0][0]).align_to(codes_b_deQueue[0][0], RIGHT).shift(
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
        self.play(Write(arrow), Write(move_frame))
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
        background_tmp.set_height(2, stretch=True).set_width(4, stretch=True)
        background_tmp.align_to(frame_animation, UP).shift(
            UP * 0.5 * (narrow_multiple / 0.8)
        )
        # empty 代码
        empty_codes = [
            "bool empty() const",
            "{",
            "   return front == NULL;",
            "}",
        ]
        codes_empty = VGroup(
            *[CodeLine_small(code) for code in empty_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_empty.next_to(background_tmp.get_top(), DOWN, buff=0.1)
        # empty 整体
        base_empty = VGroup(background_tmp, codes_empty)
        # empty 整体出现
        to_Down = VGroup(base_1, base_2, base_3, base_7)
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
            codes_b_deQueue[0][2],
            move_frame.align_to,
            codes_b_deQueue[0][2],
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
            codes_b_deQueue[0][3],
            move_frame.align_to,
            codes_b_deQueue[0][3],
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
            codes_b_deQueue[0][4],
            move_frame.align_to,
            codes_b_deQueue[0][4],
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
            base_2[0][0][2].set_color, BLACK,
            move_frame.set_width,
            ignore_space_len(5),
            move_frame.move_to,
            codes_b_deQueue[1][0],
            move_frame.align_to,
            codes_b_deQueue[1][0],
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
            ignore_space_len(7),
            move_frame.move_to,
            codes_b_deQueue[1][2],
            move_frame.align_to,
            codes_b_deQueue[1][2],
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
            ignore_space_len(8),
            move_frame.move_to,
            codes_b_deQueue[1][3],
            move_frame.align_to,
            codes_b_deQueue[1][3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()


class b_getHead(Scene_White):
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
        background.to_corner(UP * 2)
        b_getHead_function = CodeLine_func(
            "getHead()", font="思源宋体 Heavy", b_getHead=0.8
        ).to_corner(UP, buff=0.25)
        codes_b_getHead = VGroup(
            *[CodeLine_large(code) for code in b_getHead_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_b_getHead.next_to(background.get_top(), DOWN,
                                buff=0.2).shift(RIGHT * 0.2)

        self.add(background, b_getHead_function, codes_b_getHead)
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
        # 箭头(front)
        vec_front = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # front
        front = (
            TextMobject("front", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(front.copy(), vec_front.copy())
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
        # 箭头(rear)
        vec_rear = vec_front.copy()
        # rear
        rear = (
            TextMobject("rear", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_rear, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 7
        base_7 = VGroup(rear.copy(), vec_rear.copy())

        # 各整体的位置
        """
        整体 1(front)
        整体 2(长方块)
        整体 3(NULL)
        整体 4(value)
        整体 5(tmp)
        整体 6(p)
        整体 7(rear)
        """
        # 整体 4 靠左
        base_4.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.5 * (narrow_multiple / 0.5) + UP *
            1 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 4 右边
        base_2.next_to(base_4, RIGHT, buff=1 * (narrow_multiple / 0.5))
        # 整体 1 在整体 2 上边
        base_1.next_to(base_2[0][0][0], UP, buff=0.1 * (narrow_multiple / 0.5))
        # 整体 7 在整体 2 上边
        base_7.next_to(base_2[4][0][0], UP, buff=0.1 * (narrow_multiple / 0.5))
        # 整体 3 在整体 2 右边
        base_3.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))

        self.add(frame_animation, base_1, base_2, base_3, base_7)

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(b_getHead_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if b_getHead_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif b_getHead_codes[num][index] == " " and record == 0:
                    record = 1
                elif b_getHead_codes[num][index] != " ":
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
        ).move_to(codes_b_getHead[0]).align_to(codes_b_getHead[0], RIGHT).shift(
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

        # --------------- 正式开始 ---------------
        self.wait()
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()
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
        background_tmp.set_height(2, stretch=True).set_width(4, stretch=True)
        background_tmp.align_to(frame_animation, UP).shift(
            UP * 1.3 * (narrow_multiple / 0.8)
        )
        # empty 代码
        empty_codes = [
            "bool empty() const",
            "{",
            "   return front == NULL;",
            "}",
        ]
        codes_empty = VGroup(
            *[CodeLine_small(code) for code in empty_codes[:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_empty.next_to(background_tmp.get_top(), DOWN, buff=0.1)
        # empty 整体
        base_empty = VGroup(background_tmp, codes_empty)
        # empty 整体出现
        to_Down = VGroup(base_1, base_2, base_3, base_7)
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
            codes_b_getHead[2],
            move_frame.align_to,
            codes_b_getHead[2],
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
        self.play(FadeIn(base_blue))
        self.wait()
