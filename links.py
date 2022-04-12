from manimlib.imports import *
from manim_tuan import *

"""
TODO
1: getposition 第一行代码的 move_frame 触碰到左边的代码框
1: traverse 代码按照书上写，但我想要添加 "if (p == NULL) cout << \"link list is empty\";" (未添加)，不知王道考研有没有
2: insert 第六行代码 "if (p == tail) tail = q;" 的特殊情况没有考虑
3: remove 第六行代码 "if (p == tail)" 的特殊情况没有考虑
4: remove 加上蓝色箭头
5: search 出场 count 的方式
6: inverse 只考虑了 inverse_recs = 4 的情况
7: inverse 在 tail 出现时的变换有点不对劲
"""

# clear
# traverse
# getposition
# insert
# remove
# search
# visit
# inverse

# 自定义串信息()
clear_recs = 4
traverse_recs = 4
getposition_recs = 2
insert_recs = 1
insert_value = 10
remove_recs = 1
search_recs = 2
visit_recs = 2
inverse_recs = 4

clear_codes = [
    "Node *p, *tmp;",
    "p = head->next;",
    "while (p != NULL)",
    "{",
    "    tmp = p;",
    "    p = p->next;",
    "    delete tmp;",
    "}",
    "head->next = NULL;",
    "tail = head;",
    "curLength = 0;",
]

traverse_codes = [
    "Node *p = head->next;",
    'cout << "result:";',
    "while (p != NULL)",
    "{",
    "    cout << p->data << ' ';",
    "    p = p->next;",
    "}",
    "cout << endl;",
]

getposition_codes = [
    "if (i < -1 || i > curLength-1)",
    "    return NULL;",
    "Node *p = head;",
    "int count = 0;",
    "while (count <= i)",
    "{",
    "    p = p->next;",
    "    count++;",
    "}",
    "return p;",
]

insert_codes = [
    "Node *p, *q;",
    "if (i < 0 || i > curLength)",
    "    throw outOfRange();",
    "p = getPosition(i-1);",
    "q = new Node(value, p->next);",
    "p->next = q;",
    "if (p == tail) tail = q;",
    "++curLength;",
]

remove_codes = [
    "Node *pre, *p;",
    "if (i < 0 || i > curLength-1)",
    "    throw outOfRange();",
    "pre = getPosition(i-1);",
    "p = pre->next;",
    "if (p == tail) {",
    "    tail = pre;",
    "    pre->next = NULL;",
    "    delete p;",
    "}",
    "else {",
    "    pre->next = p->next;",
    "    delete p;",
    "}",
    "--curLength;",
]

search_codes = [
    "Node *p = head->next; ",
    "int count = 0;",
    "while (p != NULL && p->data != value)",
    "{",
    "    p = p->next;",
    "    ++count;",
    "}",
    "if (p == NULL)",
    "    return -1;",
    "else",
    "    return count;",
]

visit_codes = [
    "Node *p = head->next;",
    "int count = 0;",
    "if (i < 0 || i > curLength-1)",
    "    throw outOfRange();",
    "while (count < i)",
    "{",
    "    p = p->next;",
    "    ++count;",
    "}",
    "return p->data;",
]

inverse_codes = [
    "Node *p, *tmp;",
    "p = head->next;",
    "head->next = NULL;",
    "if (p != NULL)",
    "    tail = p;",
    "while (p != NULL)",
    "{",
    "    tmp = p->next;",
    "    p->next = head->next;",
    "    head->next = p;",
    "    p = tmp;",
    "}",
]


def skip():
    # 代表运行到一行代码，但动画不发生演示
    whatever = 1


class Scene_White(Scene):
    CONFIG = {"camera_config": {"background_color": WHITE, "use_plot_depth": True,}}


class CodeLine(Text):

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
            "pre": BLUE_D,
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

    def set_size(self, to_size):
        self.size = to_size


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
        background_left.set_height(3.5, stretch=True).set_width(6, stretch=True)
        background_right = background_left.copy()
        background_left.to_corner(UP * 1.5 + LEFT * 2.15)
        background_right.to_corner(UP * 1.5 + RIGHT * 2.15)
        background = VGroup(background_left, background_right)
        clear_function = CodeLine_func(
            "clear()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.18)
        codes_clear_1 = VGroup(*[CodeLine(code) for code in clear_codes[:6]]).arrange(
            DOWN, aligned_edge=LEFT
        )
        codes_clear_1.next_to(background_left.get_top(), DOWN, buff=0.2).shift(
            LEFT * 0.8
        )
        codes_clear_2 = VGroup(*[CodeLine(code) for code in clear_codes[6:]]).arrange(
            DOWN, aligned_edge=LEFT
        )
        codes_clear_2.next_to(background_right.get_top(), DOWN, buff=0.2).shift(
            LEFT * 0.7
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
        rectangle_base = MySquare(color=BLACK, side_length=0.5, stroke_opacity=1)
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
        base = VGroup(rectangle_front.copy(), rectangle_later.copy(), vec_base.copy())
        # 箭头(head)
        vec_head = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # head
        head = (
            TextMobject("head", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_head, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(base.copy(), head.copy(), vec_head.copy())
        # 整体 2
        base_2 = VGroup()
        # 方块中的数字 n
        for i in range(clear_recs):
            n = (
                Integer(i, color=BLACK)
                .scale(0.7 * (narrow_multiple / 0.5))
                .move_to(base[0])
            )
            base_2_tmp = VGroup(base.copy(), n.copy())
            base_2.add(base_2_tmp.copy())
        base_2.arrange(RIGHT, buff=0.1 * (narrow_multiple / 0.5))
        # tail
        tail = TextMobject("tail", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # 箭头(tail_up)
        vec_tail_up = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 3
        base_3 = VGroup(tail.copy(), vec_tail_up.copy())
        # 箭头(tail_down)
        vec_tail_down = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, DOWN, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 4
        base_4 = VGroup(tail.copy(), vec_tail_down.copy())
        # 整题 5 (NULL)
        base_5 = TextMobject("NULL", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # curLength_value
        curLength_value = (
            Integer(clear_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(curLength, RIGHT)
        )
        # 整体 6
        base_6 = VGroup(curLength.copy(), curLength_value.copy())
        # tmp
        tmp = (
            TextMobject("tmp", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_tail_up.copy(), DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 7
        base_7 = VGroup(vec_tail_up.copy(), tmp.copy())
        # 箭头(p)
        vec_p = vec_tail_up.copy()
        # p
        p = (
            TextMobject("P", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_p, DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 8
        base_8 = VGroup(vec_p.copy(), p.copy())

        # 各整体的位置
        # 整体 6 靠左
        base_6.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.7 * (narrow_multiple / 0.5)
        )
        # 整体 1 在整体 6 右边
        base_1.next_to(base_6, RIGHT, buff=0.6 * (narrow_multiple / 0.5)).shift(
            UP * 0.4 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 1 右边顺序排序
        base_2.next_to(base_1, RIGHT, buff=0.1 * (narrow_multiple / 0.5)).shift(
            DOWN * 0.41 * (narrow_multiple / 0.5)
        )
        # 整体 5 在整体 2 右边
        base_5.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))
        # 整体 4 在整体 2 的最右边的方块的上面
        base_4.next_to(base_2[clear_recs - 1][0][0], UP, buff=0.1)

        self.add(frame_animation, base_6, base_1, base_2, base_5, base_4)
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

        # 第一行代码
        skip()
        # 第二行代码
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
        # 整体 8 出现
        base_8.next_to(base_2[0][0][0], DOWN, buff=0.1)
        self.play(FadeInFrom(base_8, UP))
        # 用 for 循环代替 while
        for circles in range(clear_recs):
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
            self.play(
                move_frame.set_width,
                ignore_space_len(4),
                move_frame.move_to,
                codes_clear[0][4],
                move_frame.align_to,
                codes_clear[0][4],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            # 整体 7 出现，但之后会旋转，因此建立一个临时的整体 7，也建立一个临时的整体 8，用于转换
            base_7_tmp = base_7.copy().next_to(base_2[circles][0][0], DOWN, buff=0.1)
            base_7_tmp[0].rotate(
                angle=(2 * PI - PI / 6), about_point=base_2[circles][0][0].get_center()
            )
            base_7_tmp[1].shift(LEFT * 0.5 * (narrow_multiple / 0.5))
            base_8_tmp = base_8.copy()
            self.play(ReplacementTransform(base_8_tmp, base_7_tmp))
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(5),
                move_frame.move_to,
                codes_clear[0][5],
                move_frame.align_to,
                codes_clear[0][5],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            # 箭头变蓝
            self.play(base_2[circles][0][2].set_color, BLUE)
            self.wait()
            # 整体 7 和 8 都向右移动
            self.play(
                base_8.shift,
                RIGHT * 1.63 * (narrow_multiple / 0.5),
                base_7_tmp[0].rotate,
                {"angle": PI / 6, "about_point": base_2[circles][0][0].get_center()},
                base_7_tmp[1].shift,
                RIGHT * 0.5 * (narrow_multiple / 0.5),
            )
            self.wait()
            # 右边第一行代码
            self.play(
                move_frame.set_width,
                ignore_space_len(6),
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
            # 整体 7 消失
            if circles < clear_recs - 1:
                self.play(FadeOut(base_2[circles]), FadeOut(base_7_tmp))
            else:
                self.play(
                    FadeOut(base_2[circles]), FadeOut(base_7_tmp), FadeOut(base_8)
                )
            self.wait()
            # 右边部分向左平移
            if circles < clear_recs - 1:
                move_left = VGroup()
                move_left.add(base_4, base_5, base_8)
                for circles_ in range(circles + 1, clear_recs):
                    move_left.add(base_2[circles_])
                self.play(move_left.shift, LEFT * 1.625 * (narrow_multiple / 0.5))
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
        # 右边第三行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(8),
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
        self.play(base_5.shift, LEFT * 1.7 * (narrow_multiple / 0.5))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(9),
            move_frame.move_to,
            codes_clear[1][3],
            move_frame.align_to,
            codes_clear[1][3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 整体 4 变成整体 3
        base_3.next_to(base_1[0][0], DOWN, buff=0.1 * (narrow_multiple / 0.5))
        self.play(ReplacementTransform(base_4, base_3))
        self.wait()
        # 右边第五行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(10),
            move_frame.move_to,
            codes_clear[1][4],
            move_frame.align_to,
            codes_clear[1][4],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 整体 6 的数字变成 0
        self.play(base_6[1].set_value, 0)
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
        background_left.set_height(2.5, stretch=True).set_width(6, stretch=True)
        background_right = background_left.copy()
        background_left.to_corner(UP * 1.5 + LEFT * 2.15)
        background_right.to_corner(UP * 1.5 + RIGHT * 2.15)
        background = VGroup(background_left, background_right)
        traverse_function = CodeLine_func(
            "traverse()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.18)
        codes_traverse_1 = VGroup(
            *[CodeLine(code) for code in traverse_codes[:4]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_traverse_1.next_to(background_left.get_top(), DOWN, buff=0.2).shift(
            LEFT * 0.4
        )
        codes_traverse_2 = VGroup(
            *[CodeLine(code) for code in traverse_codes[4:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_traverse_2.next_to(background_right.get_top(), DOWN, buff=0.2).shift(
            RIGHT * 0.1
        )
        codes_traverse = VGroup(codes_traverse_1, codes_traverse_2)

        self.add(background, traverse_function, codes_traverse)
        # 代码脚注线
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

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
        rectangle_base = MySquare(color=BLACK, side_length=0.5, stroke_opacity=1)
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
        base = VGroup(rectangle_front.copy(), rectangle_later.copy(), vec_base.copy())
        # 箭头(head)
        vec_head = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # head
        head = (
            TextMobject("head", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_head, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(base.copy(), head.copy(), vec_head.copy())
        # 整体 2
        base_2 = VGroup()
        # 方块中的数字 n
        for i in range(clear_recs):
            n = (
                Integer(i, color=BLACK)
                .scale(0.7 * (narrow_multiple / 0.5))
                .move_to(base[0])
            )
            base_2_tmp = VGroup(base.copy(), n.copy())
            base_2.add(base_2_tmp.copy())
        base_2.arrange(RIGHT, buff=0.1 * (narrow_multiple / 0.5))
        # tail
        tail = TextMobject("tail", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # 箭头(tail_up)
        vec_tail_up = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 3
        base_3 = VGroup(tail.copy(), vec_tail_up.copy())
        # 箭头(tail_down)
        vec_tail_down = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, DOWN, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 4
        base_4 = VGroup(tail.copy(), vec_tail_down.copy())
        # 整题 5 (NULL)
        base_5 = TextMobject("NULL", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # curLength_value
        curLength_value = (
            Integer(clear_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(curLength, RIGHT)
        )
        # 整体 6
        base_6 = VGroup(curLength.copy(), curLength_value.copy())
        # tmp
        tmp = (
            TextMobject("tmp", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_tail_up.copy(), DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 7
        base_7 = VGroup(vec_tail_up.copy(), tmp.copy())
        # 箭头(p)
        vec_p = vec_tail_up.copy()
        # p
        p = (
            TextMobject("P", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_p, DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 8
        base_8 = VGroup(vec_p.copy(), p.copy())

        # 各整体的位置
        # 整体 6 靠左
        base_6.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.7 * (narrow_multiple / 0.5)
        )
        # 整体 1 在整体 6 右边
        base_1.next_to(base_6, RIGHT, buff=0.6 * (narrow_multiple / 0.5)).shift(
            UP * 0.4 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 1 右边顺序排序
        base_2.next_to(base_1, RIGHT, buff=0.1 * (narrow_multiple / 0.5)).shift(
            DOWN * 0.41 * (narrow_multiple / 0.5)
        )
        # 整体 5 在整体 2 右边
        base_5.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))
        # 整体 4 在整体 2 的最右边的方块的上面
        base_4.next_to(base_2[clear_recs - 1][0][0], UP, buff=0.1)

        self.add(frame_animation, base_6, base_1, base_2, base_5, base_4)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(traverse_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if traverse_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif traverse_codes[num][index] == " " and record == 0:
                    record = 1
                elif traverse_codes[num][index] != " ":
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
        ).move_to(codes_traverse[0][0]).align_to(codes_traverse[0][0], RIGHT).shift(
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
        base_8.next_to(base_2[0][0][0], DOWN, buff=0.1)
        self.play(FadeInFrom(base_8, UP))
        self.wait()
        # 第二行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(1),
            move_frame.move_to,
            codes_traverse[0][1],
            move_frame.align_to,
            codes_traverse[0][1],
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
            .next_to(base_6, DOWN, buff=0.05)
            .shift(UP * 0.35 + LEFT)
            .scale(0.7)
        )
        self.play(Write(result), ApplyMethod(base_6.shift, UP * 0.5), run_time=1.5)
        self.wait()
        # 用 for 循环代替 while
        for circles in range(traverse_recs):
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
            # 方块的数字移动到 result 旁边
            number_tmp = base_2[circles][1].copy()
            number_result = (
                Integer(circles, color=BLACK)
                .scale(0.7 * (narrow_multiple / 0.5))
                .next_to(result, RIGHT, buff=0.25)
                .shift(RIGHT * 0.4 * circles)
            )
            self.play(ReplacementTransform(number_tmp, number_result))
            self.add(number_result)
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
            # 箭头变蓝
            self.play(base_2[circles][0][2].set_color, BLUE)
            self.wait()
            self.play(base_8.shift, RIGHT * 1.63 * (narrow_multiple / 0.5))
            self.wait()
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
            ignore_space_len(7),
            move_frame.move_to,
            codes_traverse[1][3],
            move_frame.align_to,
            codes_traverse[1][3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()


class getposition(Scene_White):
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
        background_left.set_height(3, stretch=True).set_width(6.4, stretch=True)
        background_right = background_left.copy()
        background_left.to_corner(UP * 1.5 + LEFT * 1.36)
        background_right.to_corner(UP * 1.5 + RIGHT * 1.36)
        background = VGroup(background_left, background_right)
        getposition_function = CodeLine_func(
            "getposition(2)", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.18)
        codes_getposition_1 = VGroup(
            *[CodeLine(code) for code in getposition_codes[:5]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_getposition_1.next_to(background_left.get_top(), DOWN, buff=0.2).shift(
            RIGHT * 0.1
        )
        codes_getposition_2 = VGroup(
            *[CodeLine(code) for code in getposition_codes[5:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_getposition_2.next_to(background_right.get_top(), DOWN, buff=0.2).shift(
            LEFT * 1.1
        )
        codes_getposition = VGroup(codes_getposition_1, codes_getposition_2)

        self.add(background, getposition_function, codes_getposition)
        # 代码脚注线
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=4.2,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        rectangle_base = MySquare(color=BLACK, side_length=0.5, stroke_opacity=1)
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
        base = VGroup(rectangle_front.copy(), rectangle_later.copy(), vec_base.copy())
        # 箭头(head)
        vec_head = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # head
        head = (
            TextMobject("head", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_head, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(base.copy(), head.copy(), vec_head.copy())
        # 整体 2
        base_2 = VGroup()
        # 方块中的数字 n
        for i in range(clear_recs):
            n = (
                Integer(i, color=BLACK)
                .scale(0.7 * (narrow_multiple / 0.5))
                .move_to(base[0])
            )
            base_2_tmp = VGroup(base.copy(), n.copy())
            base_2.add(base_2_tmp.copy())
        base_2.arrange(RIGHT, buff=0.1 * (narrow_multiple / 0.5))
        # tail
        tail = TextMobject("tail", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # 箭头(tail_up)
        vec_tail_up = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 3
        base_3 = VGroup(tail.copy(), vec_tail_up.copy())
        # 箭头(tail_down)
        vec_tail_down = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, DOWN, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 4
        base_4 = VGroup(tail.copy(), vec_tail_down.copy())
        # 整题 5 (NULL)
        base_5 = TextMobject("NULL", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # curLength_value
        curLength_value = (
            Integer(clear_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(curLength, RIGHT)
        )
        # 整体 6
        base_6 = VGroup(curLength.copy(), curLength_value.copy())
        # tmp
        tmp = (
            TextMobject("tmp", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_tail_up.copy(), DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 7
        base_7 = VGroup(vec_tail_up.copy(), tmp.copy())
        # 箭头(p)
        vec_p = vec_tail_up.copy()
        # p
        p = (
            TextMobject("P", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_p, DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 8
        base_8 = VGroup(vec_p.copy(), p.copy())
        # i
        i_index = TextMobject("i = ", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # i_value
        i_value = (
            Integer(getposition_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(i_index, RIGHT)
        )
        # 整体 9
        base_9 = VGroup(i_index.copy(), i_value.copy())

        # 各整体的位置
        # 整体 6 靠左
        base_6.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.7 * (narrow_multiple / 0.5)
        )
        # 整体 1 在整体 6 右边
        base_1.next_to(base_6, RIGHT, buff=0.6 * (narrow_multiple / 0.5)).shift(
            UP * 0.4 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 1 右边顺序排序
        base_2.next_to(base_1, RIGHT, buff=0.1 * (narrow_multiple / 0.5)).shift(
            DOWN * 0.41 * (narrow_multiple / 0.5)
        )
        # 整体 5 在整体 2 右边
        base_5.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))
        # 整体 4 在整体 2 的最右边的方块的上面
        base_4.next_to(base_2[clear_recs - 1][0][0], UP, buff=0.1)
        # 整体 9 在整体 6 上面
        base_9.next_to(base_6, UP, buff=0.4).align_to(base_6, LEFT)

        self.add(frame_animation, base_6, base_1, base_2, base_5, base_4, base_9)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(getposition_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if getposition_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif getposition_codes[num][index] == " " and record == 0:
                    record = 1
                elif getposition_codes[num][index] != " ":
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
        ).move_to(codes_getposition[0][0]).align_to(
            codes_getposition[0][0], RIGHT
        ).shift(
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
        skip()
        # 第三行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_getposition[0][2],
            move_frame.align_to,
            codes_getposition[0][2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 整体 8 出现
        base_8.next_to(base_1[0][0], DOWN, buff=0.1)
        self.play(FadeInFrom(base_8, UP))
        self.wait()
        # 第四行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(3),
            move_frame.move_to,
            codes_getposition[0][3],
            move_frame.align_to,
            codes_getposition[0][3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
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
        # 整体 10 出现
        base_10 = (
            VGroup(count.copy(), count_value.copy())
            .next_to(base_6, DOWN, buff=0.05)
            .align_to(base_6, LEFT)
        )
        self.play(
            Write(base_10),
            ApplyMethod(base_6.shift, UP * 0.2),
            ApplyMethod(base_9.shift, UP * 0.1),
            run_time=1.5,
        )
        self.wait()
        # 用 for 循环代替 while
        for circles in range(getposition_recs + 1):
            self.play(
                move_frame.set_width,
                ignore_space_len(4),
                move_frame.move_to,
                codes_getposition[0][4],
                move_frame.align_to,
                codes_getposition[0][4],
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
                codes_getposition[1][1],
                move_frame.align_to,
                codes_getposition[1][1],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            # 箭头变蓝
            if circles != 0:
                self.play(base_2[circles - 1][0][2].set_color, BLUE)
            else:
                self.play(base_1[0][2].set_color, BLUE)
            self.wait()
            # 整体 8 向右移动
            self.play(base_8.shift, RIGHT * 1.63 * (narrow_multiple / 0.5))
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(7),
                move_frame.move_to,
                codes_getposition[1][2],
                move_frame.align_to,
                codes_getposition[1][2],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            self.play(base_10[1].set_value, circles + 1)
            self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(4),
            move_frame.move_to,
            codes_getposition[0][4],
            move_frame.align_to,
            codes_getposition[0][4],
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
            ignore_space_len(9),
            move_frame.move_to,
            codes_getposition[1][4],
            move_frame.align_to,
            codes_getposition[1][4],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
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
        background_left.set_height(2.5, stretch=True).set_width(6.4, stretch=True)
        background_right = background_left.copy()
        background_left.to_corner(UP * 1.5 + LEFT * 1.35)
        background_right.to_corner(UP * 1.5 + RIGHT * 1.35)
        background = VGroup(background_left, background_right)
        insert_function = CodeLine_func(
            "insert(1, 10)", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.18)
        codes_insert_1 = VGroup(*[CodeLine(code) for code in insert_codes[:4]]).arrange(
            DOWN, aligned_edge=LEFT
        )
        codes_insert_1.next_to(background_left.get_top(), DOWN, buff=0.2).shift(
            LEFT * 0.1
        )
        codes_insert_2 = VGroup(*[CodeLine(code) for code in insert_codes[4:]]).arrange(
            DOWN, aligned_edge=LEFT
        )
        codes_insert_2.next_to(background_right.get_top(), DOWN, buff=0.2).shift(
            RIGHT * 0.1
        )
        codes_insert = VGroup(codes_insert_1, codes_insert_2)

        self.add(background, insert_function, codes_insert)
        # 代码脚注线
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

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
        rectangle_base = MySquare(color=BLACK, side_length=0.5, stroke_opacity=1)
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
        base = VGroup(rectangle_front.copy(), rectangle_later.copy(), vec_base.copy())
        # 箭头(head)
        vec_head = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # head
        head = (
            TextMobject("head", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_head, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(base.copy(), head.copy(), vec_head.copy())
        # 整体 2
        base_2 = VGroup()
        # 方块中的数字 n
        for i in range(3):
            n = (
                Integer(i, color=BLACK)
                .scale(0.7 * (narrow_multiple / 0.5))
                .move_to(base[0])
            )
            base_2_tmp = VGroup(base.copy(), n.copy())
            base_2.add(base_2_tmp.copy())
        base_2.arrange(RIGHT, buff=0.1 * (narrow_multiple / 0.5))
        # tail
        tail = TextMobject("tail", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # 箭头(tail_up)
        vec_tail_up = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 3
        base_3 = VGroup(tail.copy(), vec_tail_up.copy())
        # 箭头(tail_down)
        vec_tail_down = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, DOWN, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 4
        base_4 = VGroup(tail.copy(), vec_tail_down.copy())
        # 整题 5 (NULL)
        base_5 = TextMobject("NULL", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # curLength_value
        curLength_value = (
            Integer(3, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(curLength, RIGHT)
        )
        # 整体 6
        base_6 = VGroup(curLength.copy(), curLength_value.copy())
        # tmp
        tmp = (
            TextMobject("tmp", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_tail_up.copy(), DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 7
        base_7 = VGroup(vec_tail_up.copy(), tmp.copy())
        # 箭头(p)
        vec_p = vec_tail_up.copy()
        # p
        p = (
            TextMobject("P", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_p, DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 8
        base_8 = VGroup(vec_p.copy(), p.copy())
        # i
        i_index = TextMobject("i = ", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # i_value
        i_value = (
            Integer(insert_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(i_index, RIGHT)
        )
        # 整体 9
        base_9 = VGroup(i_index.copy(), i_value.copy())
        # value
        value = TextMobject("value = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # value_value
        value_value = (
            Integer(insert_value, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(value, RIGHT)
        )
        # 整体 10
        base_10 = VGroup(value.copy(), value_value.copy())

        # 各整体的位置
        # 整体 6 靠左
        base_6.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.7 * (narrow_multiple / 0.5)
        )
        # 整体 1 在整体 6 右边
        base_1.next_to(base_6, RIGHT, buff=0.6 * (narrow_multiple / 0.5)).shift(
            UP * 0.4 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 1 右边顺序排序
        base_2.next_to(base_1, RIGHT, buff=0.1 * (narrow_multiple / 0.5)).shift(
            DOWN * 0.41 * (narrow_multiple / 0.5)
        )
        # 整体 5 在整体 2 右边
        base_5.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))
        # 整体 4 在整体 2 的最右边的方块的上面
        base_4.next_to(base_2[2][0][0], UP, buff=0.1)
        # 整体 10 在整体 6 上面，整体 6 稍微下调
        base_6.shift(DOWN * 0.4)
        base_10.next_to(base_6, UP, buff=0.25).align_to(base_6, LEFT)
        # 整体 9 在整体 10 上面
        base_9.next_to(base_10, UP, buff=0.25).align_to(base_6, LEFT)

        self.add(
            frame_animation, base_6, base_1, base_2, base_5, base_4, base_9, base_10
        )
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(insert_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if insert_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif insert_codes[num][index] == " " and record == 0:
                    record = 1
                elif insert_codes[num][index] != " ":
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
        ).move_to(codes_insert[0][0]).align_to(codes_insert[0][0], RIGHT).shift(
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
        skip()
        # 第二行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(1),
            move_frame.move_to,
            codes_insert[0][1],
            move_frame.align_to,
            codes_insert[0][1],
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
            codes_insert[0][3],
            move_frame.align_to,
            codes_insert[0][3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 整体 8 出现
        if insert_recs == 0:
            base_8.next_to(base_1[0][0], DOWN, buff=0.1)
        else:
            base_8.next_to(base_2[0][0][0], DOWN, buff=0.1)
        self.play(FadeInFrom(base_8, UP))
        self.wait()
        # 右边第一行代码
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
        # 建立新的方块
        insert_base_base = base.copy()
        insert_base_value = (
            Integer(insert_value, color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .move_to(insert_base_base[0])
        )
        insert_base = (
            VGroup(insert_base_base.copy(), insert_base_value.copy())
            .move_to(base_2[insert_recs])
            .shift(
                DOWN * 1 * (narrow_multiple / 0.5)
                + LEFT * 0.9 * (narrow_multiple / 0.5)
            )
        )
        insert_base[0][2].rotate(
            angle=60 * DEGREES, about_point=insert_base[0][2].get_start()
        )
        # 建立新的整体 11
        # 箭头(q)
        vec_q = vec_tail_up.copy()
        # q
        q = (
            TextMobject("q", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_q, DOWN, buff=0.05 * (narrow_multiple / 0.5))
            # .flip()
        )
        # 整体 11
        base_11 = VGroup(vec_q.copy(), q.copy())
        base_11.add_updater(lambda a: a.next_to(insert_base[0][0][0], DOWN, buff=0.1))
        self.play(FadeInFrom(insert_base, RIGHT))
        self.play(FadeInFrom(base_11, UP))
        self.wait()
        # 右边第二行代码
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
        if insert_recs != 0:
            self.play(
                base_2[insert_recs - 1][0][2].rotate,
                {
                    "angle": -70 * DEGREES,
                    "about_point": base_2[insert_recs - 1][0][2].get_start(),
                },
            )
        else:
            self.play(
                base_1[0][2].rotate,
                {
                    "angle": -70 * DEGREES,
                    "about_point": base_2[insert_recs - 1][0][2].get_start(),
                },
            )
        self.wait()
        # 新方块移到右上方，右边部分向右平移
        base_2_tmp = base_2[insert_recs].copy()
        move_right = VGroup()
        move_right.add(base_4, base_5)
        for index in range(insert_recs, 3):
            move_right.add(base_2[index])
        self.play(
            move_right.shift,
            RIGHT * 1.625 * (narrow_multiple / 0.5),
            insert_base.move_to,
            base_2_tmp,
            insert_base.shift,
            UP * 0.2 * (narrow_multiple / 0.5) + LEFT * 0.19 * (narrow_multiple / 0.5),
        )
        # self.play(move_right.shift, RIGHT *
        #          1.625 * (narrow_multiple / 0.5))
        self.play(
            insert_base[0][2].rotate,
            {"angle": -60 * DEGREES, "about_point": insert_base[0][2].get_start()},
            base_2[insert_recs - 1][0][2].rotate,
            {
                "angle": 70 * DEGREES,
                "about_point": base_2[insert_recs - 1][0][2].get_start(),
            },
        )
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
        self.play(base_6[1].set_value, 4)
        self.wait()


class remove(Scene_White):
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
        background_left.set_height(3.4, stretch=True).set_width(5.5, stretch=True)
        background_right = background_left.copy()
        background_left.to_corner(UP * 1.5 + LEFT * 3.15)
        background_right.to_corner(UP * 1.5 + RIGHT * 3.15)
        background = VGroup(background_left, background_right)
        remove_function = CodeLine_func(
            "remove(1)", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.18)
        codes_remove_1 = VGroup(*[CodeLine(code) for code in remove_codes[:8]]).arrange(
            DOWN, aligned_edge=LEFT, buff=0.1
        )
        for index in range(8):
            codes_remove_1[index].scale(0.7)
            if index != 0:
                codes_remove_1[index].align_to(codes_remove_1[index - 1], LEFT)
        codes_remove_1.next_to(background_left.get_top(), DOWN, buff=0.1).shift(
            LEFT * 0.3
        )
        codes_remove_2 = VGroup(*[CodeLine(code) for code in remove_codes[8:]]).arrange(
            DOWN, aligned_edge=LEFT, buff=0.1
        )
        for index in range(7):
            codes_remove_2[index].scale(0.7)
            if index != 0:
                codes_remove_2[index].align_to(codes_remove_2[index - 1], LEFT)
        codes_remove_2.next_to(background_right.get_top(), DOWN, buff=0.1).shift(
            LEFT * 0.7
        )
        codes_remove = VGroup(codes_remove_1, codes_remove_2)

        self.add(background, remove_function, codes_remove)
        # 代码脚注线
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=3.8,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        rectangle_base = MySquare(color=BLACK, side_length=0.5, stroke_opacity=1)
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
        base = VGroup(rectangle_front.copy(), rectangle_later.copy(), vec_base.copy())
        # 箭头(head)
        vec_head = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # head
        head = (
            TextMobject("head", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_head, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(base.copy(), head.copy(), vec_head.copy())
        # 整体 2
        base_2 = VGroup()
        # 方块中的数字 n
        for i in range(clear_recs):
            n = (
                Integer(i, color=BLACK)
                .scale(0.7 * (narrow_multiple / 0.5))
                .move_to(base[0])
            )
            base_2_tmp = VGroup(base.copy(), n.copy())
            base_2.add(base_2_tmp.copy())
        base_2.arrange(RIGHT, buff=0.1 * (narrow_multiple / 0.5))
        # tail
        tail = TextMobject("tail", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # 箭头(tail_up)
        vec_tail_up = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 3
        base_3 = VGroup(tail.copy(), vec_tail_up.copy())
        # 箭头(tail_down)
        vec_tail_down = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, DOWN, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 4
        base_4 = VGroup(tail.copy(), vec_tail_down.copy())
        # 整题 5 (NULL)
        base_5 = TextMobject("NULL", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # curLength_value
        curLength_value = (
            Integer(clear_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(curLength, RIGHT)
        )
        # 整体 6
        base_6 = VGroup(curLength.copy(), curLength_value.copy())
        # tmp
        tmp = (
            TextMobject("tmp", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_tail_up.copy(), DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 7
        base_7 = VGroup(vec_tail_up.copy(), tmp.copy())
        # 箭头(p)
        vec_p = vec_tail_up.copy()
        # p
        p = (
            TextMobject("P", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_p, DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 8
        base_8 = VGroup(vec_p.copy(), p.copy())
        # i
        i_index = TextMobject("i = ", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # i_value
        i_value = (
            Integer(remove_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(i_index, RIGHT)
        )
        # 整体 9
        base_9 = VGroup(i_index.copy(), i_value.copy())

        # 各整体的位置
        # 整体 6 靠左
        base_6.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.7 * (narrow_multiple / 0.5)
        )
        # 整体 1 在整体 6 右边
        base_1.next_to(base_6, RIGHT, buff=0.6 * (narrow_multiple / 0.5)).shift(
            UP * 0.4 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 1 右边顺序排序
        base_2.next_to(base_1, RIGHT, buff=0.1 * (narrow_multiple / 0.5)).shift(
            DOWN * 0.41 * (narrow_multiple / 0.5)
        )
        # 整体 5 在整体 2 右边
        base_5.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))
        # 整体 4 在整体 2 的最右边的方块的上面
        base_4.next_to(base_2[clear_recs - 1][0][0], UP, buff=0.1)
        # 整体 9 在整体 6 上面
        base_9.next_to(base_6, UP, buff=0.4).align_to(base_6, LEFT)

        self.add(frame_animation, base_6, base_1, base_2, base_5, base_4, base_9)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(remove_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if remove_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.145
                elif remove_codes[num][index] == " " and record == 0:
                    record = 1
                elif remove_codes[num][index] != " ":
                    record = 0
            # 返回的单位 不确定
            return origin_len * 0.145

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=3, stroke_color=GOLD, corner_radius=0.05,
        )
        # 代码框移动到第一行代码处
        move_frame.set_width(ignore_space_len(0), stretch=True).set_height(
            0.36, stretch=True
        ).move_to(codes_remove[0][0]).align_to(codes_remove[0][0], RIGHT).shift(
            RIGHT * 0.1
        )
        # 代码框左边的小三角
        arrow = (
            Triangle(stroke_opacity=0, fill_opacity=1, fill_color=RED)
            .scale(0.10)
            .rotate(90 * DEGREES, axis=IN)
        )
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()

        # 第一行代码
        skip()
        # 第二行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(1),
            move_frame.move_to,
            codes_remove[0][1],
            move_frame.align_to,
            codes_remove[0][1],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.36, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 第三行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(3),
            move_frame.move_to,
            codes_remove[0][3],
            move_frame.align_to,
            codes_remove[0][3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.36, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 建立新的整体 10
        # 箭头(pre)
        vec_pre = vec_tail_up.copy()
        # pre
        pre = (
            TextMobject("pre", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_pre, DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 10
        base_10 = VGroup(vec_pre.copy(), pre.copy())
        if remove_recs != 0:
            base_10.next_to(base_2[remove_recs - 1][0][0], DOWN, buff=0.1)
        else:
            base_10.next_to(base_1[0][0], DOWN, buff=0.1)
        self.play(FadeInFrom(base_10, UP))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(4),
            move_frame.move_to,
            codes_remove[0][4],
            move_frame.align_to,
            codes_remove[0][4],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.36, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 整体 8 出现
        base_8.next_to(base_2[remove_recs][0][0], DOWN, buff=0.1)
        self.play(FadeInFrom(base_8, UP))
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(5),
            move_frame.move_to,
            codes_remove[0][5],
            move_frame.align_to,
            codes_remove[0][5],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.36, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(10),
            move_frame.move_to,
            codes_remove[1][2],
            move_frame.align_to,
            codes_remove[1][2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.36, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(11),
            move_frame.move_to,
            codes_remove[1][3],
            move_frame.align_to,
            codes_remove[1][3],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.36, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 括号弯曲
        arc_fac = ValueTracker(0.0)
        arc_tran = base_2[remove_recs - 1][0][2].copy()
        # 此处未考虑特殊情况
        arc_arrow = Arrow(
            base_2[remove_recs - 1][0][1].get_center(),
            base_2[remove_recs][0][1].get_center() + RIGHT * 1.3,
            color=BLACK,
            max_tip_length_to_length_ratio=0.08,
            max_stroke_width_to_length_ratio=1.5,
        )
        arc_fac.set_value(-2)
        arc_arrow.add_updater(
            lambda l: l.become(
                Arrow(
                    base_2[remove_recs - 1][0][1].get_center(),
                    base_2[remove_recs][0][1].get_center() + RIGHT * 1.3,
                    color=BLACK,
                    max_tip_length_to_length_ratio=0.08,
                    max_stroke_width_to_length_ratio=1.5,
                    path_arc=arc_fac.get_value(),
                )
            )
        )
        self.play(ReplacementTransform(base_2[remove_recs - 1][0][2], arc_arrow))
        self.add(arc_arrow)
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(12),
            move_frame.move_to,
            codes_remove[1][4],
            move_frame.align_to,
            codes_remove[1][4],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.36, "stretch": True},
            run_time=1,
        )
        self.wait()
        delete_out = VGroup(base_8, base_2[remove_recs])
        self.play(FadeOut(delete_out))
        self.wait()
        self.play(arc_fac.set_value, 0, rate_func=linear)
        self.wait()
        move_left = VGroup()
        move_left.add(base_4, base_5)
        for circles in range(remove_recs + 1, 4):
            move_left.add(base_2[circles])
        self.play(
            ReplacementTransform(arc_arrow, arc_tran),
            ApplyMethod(move_left.shift, LEFT * 1.625 * (narrow_multiple / 0.5)),
        )
        self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(14),
            move_frame.move_to,
            codes_remove[1][6],
            move_frame.align_to,
            codes_remove[1][6],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.36, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(base_6[1].set_value, 3)
        self.wait()


class search(Scene_White):
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
        background_left.set_height(3.5, stretch=True).set_width(7.8, stretch=True)
        background_right = background_left.copy()
        background_right.set_height(3.5, stretch=True).set_width(4.2, stretch=True)
        background_left.to_corner(UP * 1.5 + LEFT * 2.15)
        background_right.to_corner(UP * 1.5 + RIGHT * 2.15)
        background = VGroup(background_left, background_right)
        search_function = CodeLine_func(
            "search(2)", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.18)
        codes_search_1 = VGroup(*[CodeLine(code) for code in search_codes[:6]]).arrange(
            DOWN, aligned_edge=LEFT
        )
        codes_search_1.next_to(background_left.get_top(), DOWN, buff=0.2).shift(
            RIGHT * 0.15
        )
        codes_search_2 = VGroup(*[CodeLine(code) for code in search_codes[6:]]).arrange(
            DOWN, aligned_edge=LEFT
        )
        codes_search_2.next_to(background_right.get_top(), DOWN, buff=0.2).shift(
            RIGHT * 0
        )
        codes_search = VGroup(codes_search_1, codes_search_2)

        self.add(background, search_function, codes_search)
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
        rectangle_base = MySquare(color=BLACK, side_length=0.5, stroke_opacity=1)
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
        base = VGroup(rectangle_front.copy(), rectangle_later.copy(), vec_base.copy())
        # 箭头(head)
        vec_head = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # head
        head = (
            TextMobject("head", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_head, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(base.copy(), head.copy(), vec_head.copy())
        # 整体 2
        base_2 = VGroup()
        # 方块中的数字 n
        for i in range(clear_recs):
            n = (
                Integer(i, color=BLACK)
                .scale(0.7 * (narrow_multiple / 0.5))
                .move_to(base[0])
            )
            base_2_tmp = VGroup(base.copy(), n.copy())
            base_2.add(base_2_tmp.copy())
        base_2.arrange(RIGHT, buff=0.1 * (narrow_multiple / 0.5))
        # tail
        tail = TextMobject("tail", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # 箭头(tail_up)
        vec_tail_up = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 3
        base_3 = VGroup(tail.copy(), vec_tail_up.copy())
        # 箭头(tail_down)
        vec_tail_down = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, DOWN, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 4
        base_4 = VGroup(tail.copy(), vec_tail_down.copy())
        # 整题 5 (NULL)
        base_5 = TextMobject("NULL", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # curLength_value
        curLength_value = (
            Integer(clear_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(curLength, RIGHT)
        )
        # 整体 6
        base_6 = VGroup(curLength.copy(), curLength_value.copy())
        # tmp
        tmp = (
            TextMobject("tmp", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_tail_up.copy(), DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 7
        base_7 = VGroup(vec_tail_up.copy(), tmp.copy())
        # 箭头(p)
        vec_p = vec_tail_up.copy()
        # p
        p = (
            TextMobject("P", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_p, DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 8
        base_8 = VGroup(vec_p.copy(), p.copy())
        # count
        count_index = TextMobject("count = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # count_value
        count_value = (
            Integer(0, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(count_index, RIGHT)
        )
        # 整体 9
        base_9 = VGroup(count_index.copy(), count_value.copy())
        # value
        value_index = TextMobject("value = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # value_value
        value_value = (
            Integer(search_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(value_index, RIGHT)
        )
        # 整体 10
        base_10 = VGroup(value_index.copy(), value_value.copy())

        # 各整体的位置
        # 整体 6 靠左
        base_6.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.7 * (narrow_multiple / 0.5)
        )
        # 整体 1 在整体 6 右边
        base_1.next_to(base_6, RIGHT, buff=0.6 * (narrow_multiple / 0.5)).shift(
            UP * 0.4 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 1 右边顺序排序
        base_2.next_to(base_1, RIGHT, buff=0.1 * (narrow_multiple / 0.5)).shift(
            DOWN * 0.41 * (narrow_multiple / 0.5)
        )
        # 整体 5 在整体 2 右边
        base_5.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))
        # 整体 4 在整体 2 的最右边的方块的上面
        base_4.next_to(base_2[clear_recs - 1][0][0], UP, buff=0.1)
        # 整体 10 在整体 6 上面，整体 6 稍微下调
        base_6.shift(DOWN * 0.4)
        base_10.next_to(base_6, UP, buff=0.25).align_to(base_6, LEFT)
        # 整体 9 在整体 10 上面
        base_9.next_to(base_10, UP, buff=0.25).align_to(base_10, LEFT)

        self.add(frame_animation, base_6, base_1, base_2, base_5, base_4, base_10)
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
        ).move_to(codes_search[0][0]).align_to(codes_search[0][0], RIGHT).shift(
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
        base_8.next_to(base_2[0][0][0], DOWN, buff=0.1)
        self.play(FadeInFrom(base_8, UP))
        self.wait()
        # 第二行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(1),
            move_frame.move_to,
            codes_search[0][1],
            move_frame.align_to,
            codes_search[0][1],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(Write(base_9))
        # 用 for 循环代替 while
        for circles in range(search_recs):
            self.play(
                move_frame.set_width,
                ignore_space_len(2),
                move_frame.move_to,
                codes_search[0][2],
                move_frame.align_to,
                codes_search[0][2],
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
                codes_search[0][4],
                move_frame.align_to,
                codes_search[0][4],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            self.play(base_8.shift, RIGHT * 1.63 * (narrow_multiple / 0.5))
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(5),
                move_frame.move_to,
                codes_search[0][5],
                move_frame.align_to,
                codes_search[0][5],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            self.play(base_9[1].set_value, circles + 1)
            self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_search[0][2],
            move_frame.align_to,
            codes_search[0][2],
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
            codes_search[1][1],
            move_frame.align_to,
            codes_search[1][1],
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
            ignore_space_len(9),
            move_frame.move_to,
            codes_search[1][3],
            move_frame.align_to,
            codes_search[1][3],
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
            ignore_space_len(10),
            move_frame.move_to,
            codes_search[1][4],
            move_frame.align_to,
            codes_search[1][4],
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
        background_left.set_height(3, stretch=True).set_width(6.4, stretch=True)
        background_right = background_left.copy()
        background_left.to_corner(UP * 1.5 + LEFT * 1.36)
        background_right.to_corner(UP * 1.5 + RIGHT * 1.36)
        background = VGroup(background_left, background_right)
        visit_function = CodeLine_func(
            "visit(2)", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.18)
        codes_visit_1 = VGroup(*[CodeLine(code) for code in visit_codes[:5]]).arrange(
            DOWN, aligned_edge=LEFT
        )
        codes_visit_1.next_to(background_left.get_top(), DOWN, buff=0.2).shift(
            RIGHT * 0.1
        )
        codes_visit_2 = VGroup(*[CodeLine(code) for code in visit_codes[5:]]).arrange(
            DOWN, aligned_edge=LEFT
        )
        codes_visit_2.next_to(background_right.get_top(), DOWN, buff=0.2).shift(
            LEFT * 1.1
        )
        codes_visit = VGroup(codes_visit_1, codes_visit_2)

        self.add(background, visit_function, codes_visit)
        # 代码脚注线
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # --------------- 动画框架 ---------------
        # 动画下半区框架
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_opacity=0,
            height=4.2,
            width=14.2,
        ).to_corner(DOWN, buff=0)
        # 基准方块
        rectangle_base = MySquare(color=BLACK, side_length=0.5, stroke_opacity=1)
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
        base = VGroup(rectangle_front.copy(), rectangle_later.copy(), vec_base.copy())
        # 箭头(head)
        vec_head = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # head
        head = (
            TextMobject("head", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_head, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(base.copy(), head.copy(), vec_head.copy())
        # 整体 2
        base_2 = VGroup()
        # 方块中的数字 n
        for i in range(clear_recs):
            n = (
                Integer(i, color=BLACK)
                .scale(0.7 * (narrow_multiple / 0.5))
                .move_to(base[0])
            )
            base_2_tmp = VGroup(base.copy(), n.copy())
            base_2.add(base_2_tmp.copy())
        base_2.arrange(RIGHT, buff=0.1 * (narrow_multiple / 0.5))
        # tail
        tail = TextMobject("tail", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # 箭头(tail_up)
        vec_tail_up = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 3
        base_3 = VGroup(tail.copy(), vec_tail_up.copy())
        # 箭头(tail_down)
        vec_tail_down = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, DOWN, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 4
        base_4 = VGroup(tail.copy(), vec_tail_down.copy())
        # 整题 5 (NULL)
        base_5 = TextMobject("NULL", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # curLength_value
        curLength_value = (
            Integer(clear_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(curLength, RIGHT)
        )
        # 整体 6
        base_6 = VGroup(curLength.copy(), curLength_value.copy())
        # tmp
        tmp = (
            TextMobject("tmp", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_tail_up.copy(), DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 7
        base_7 = VGroup(vec_tail_up.copy(), tmp.copy())
        # 箭头(p)
        vec_p = vec_tail_up.copy()
        # p
        p = (
            TextMobject("P", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_p, DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 8
        base_8 = VGroup(vec_p.copy(), p.copy())
        # i
        i_index = TextMobject("i = ", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # i_value
        i_value = (
            Integer(visit_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(i_index, RIGHT)
        )
        # 整体 9
        base_9 = VGroup(i_index.copy(), i_value.copy())

        # 各整体的位置
        # 整体 6 靠左
        base_6.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.7 * (narrow_multiple / 0.5)
        )
        # 整体 1 在整体 6 右边
        base_1.next_to(base_6, RIGHT, buff=0.6 * (narrow_multiple / 0.5)).shift(
            UP * 0.4 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 1 右边顺序排序
        base_2.next_to(base_1, RIGHT, buff=0.1 * (narrow_multiple / 0.5)).shift(
            DOWN * 0.41 * (narrow_multiple / 0.5)
        )
        # 整体 5 在整体 2 右边
        base_5.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))
        # 整体 4 在整体 2 的最右边的方块的上面
        base_4.next_to(base_2[clear_recs - 1][0][0], UP, buff=0.1)
        # 整体 9 在整体 6 上面
        base_9.next_to(base_6, UP, buff=0.4).align_to(base_6, LEFT)

        self.add(frame_animation, base_6, base_1, base_2, base_5, base_4, base_9)
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
        ).move_to(codes_visit[0][0]).align_to(codes_visit[0][0], RIGHT).shift(
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
        base_8.next_to(base_2[0][0][0], DOWN, buff=0.1)
        self.play(FadeInFrom(base_8, UP))
        self.wait()
        # 第二行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(1),
            move_frame.move_to,
            codes_visit[0][1],
            move_frame.align_to,
            codes_visit[0][1],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
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
        # 整体 10 出现
        base_10 = (
            VGroup(count.copy(), count_value.copy())
            .next_to(base_6, DOWN, buff=0.05)
            .align_to(base_6, LEFT)
        )
        self.play(
            Write(base_10),
            ApplyMethod(base_6.shift, UP * 0.2),
            ApplyMethod(base_9.shift, UP * 0.1),
            run_time=1.5,
        )
        self.wait()
        # 第三行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_visit[0][2],
            move_frame.align_to,
            codes_visit[0][2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 用 for 循环代替 while
        for circles in range(visit_recs):
            self.play(
                move_frame.set_width,
                ignore_space_len(4),
                move_frame.move_to,
                codes_visit[0][4],
                move_frame.align_to,
                codes_visit[0][4],
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
                codes_visit[1][1],
                move_frame.align_to,
                codes_visit[1][1],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            # 箭头变蓝
            self.play(base_2[circles][0][2].set_color, BLUE)
            self.wait()
            # 整体 8 向右移动
            self.play(base_8.shift, RIGHT * 1.63 * (narrow_multiple / 0.5))
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(7),
                move_frame.move_to,
                codes_visit[1][2],
                move_frame.align_to,
                codes_visit[1][2],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            self.play(base_10[1].set_value, circles + 1)
            self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(4),
            move_frame.move_to,
            codes_visit[0][4],
            move_frame.align_to,
            codes_visit[0][4],
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
            ignore_space_len(9),
            move_frame.move_to,
            codes_visit[1][4],
            move_frame.align_to,
            codes_visit[1][4],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()


class inverse(Scene_White):
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
        background_left.set_height(3.5, stretch=True).set_width(6, stretch=True)
        background_right = background_left.copy()
        background_left.to_corner(UP * 1.5 + LEFT * 2.15)
        background_right.to_corner(UP * 1.5 + RIGHT * 2.15)
        background = VGroup(background_left, background_right)
        inverse_function = CodeLine_func(
            "inverse()", font="思源宋体 Heavy", size=0.8
        ).to_corner(UP, buff=0.18)
        codes_inverse_1 = VGroup(
            *[CodeLine(code) for code in inverse_codes[:6]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_inverse_1.next_to(background_left.get_top(), DOWN, buff=0.2).shift(
            LEFT * 0.8
        )
        codes_inverse_2 = VGroup(
            *[CodeLine(code) for code in inverse_codes[6:]]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_inverse_2.next_to(background_right.get_top(), DOWN, buff=0.2).shift(
            LEFT * 0.1
        )
        codes_inverse = VGroup(codes_inverse_1, codes_inverse_2)

        self.add(background, inverse_function, codes_inverse)
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
        rectangle_base = MySquare(color=BLACK, side_length=0.5, stroke_opacity=1)
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
        base = VGroup(rectangle_front.copy(), rectangle_later.copy(), vec_base.copy())
        # 箭头(head)
        vec_head = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(rectangle_front, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # head
        head = (
            TextMobject("head", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_head, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 1
        base_1 = VGroup(base.copy(), head.copy(), vec_head.copy())
        # 整体 2
        base_2 = VGroup()
        # 方块中的数字 n
        for i in range(inverse_recs):
            n = (
                Integer(i, color=BLACK)
                .scale(0.7 * (narrow_multiple / 0.5))
                .move_to(base[0])
            )
            base_2_tmp = VGroup(base.copy(), n.copy())
            base_2.add(base_2_tmp.copy())
        base_2.arrange(RIGHT, buff=0.1 * (narrow_multiple / 0.5))
        # tail
        tail = TextMobject("tail", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # 箭头(tail_up)
        vec_tail_up = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, UP, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 3
        base_3 = VGroup(tail.copy(), vec_tail_up.copy())
        # 箭头(tail_down)
        vec_tail_down = (
            Arrow(
                np.array([0, 1, 0]),
                np.array([0, -1, 0]),
                buff=0.6 * (narrow_multiple / 0.5),
                color=BLACK,
            )
            .scale(0.5 * (narrow_multiple / 0.5))
            .next_to(tail, DOWN, buff=0.1 * (narrow_multiple / 0.5))
        )
        # 整体 4
        base_4 = VGroup(tail.copy(), vec_tail_down.copy())
        # 整题 5 (NULL)
        base_5 = TextMobject("NULL", color=BLACK).scale(0.7 * (narrow_multiple / 0.5))
        # curLength
        curLength = TextMobject("curLength = ", color=BLACK).scale(
            0.7 * (narrow_multiple / 0.5)
        )
        # curLength_value
        curLength_value = (
            Integer(inverse_recs, color=BLUE)
            .scale(1 * (narrow_multiple / 0.5))
            .next_to(curLength, RIGHT)
        )
        # 整体 6
        base_6 = VGroup(curLength.copy(), curLength_value.copy())
        # tmp
        tmp = (
            TextMobject("tmp", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_tail_up.copy(), DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 7
        base_7 = VGroup(vec_tail_up.copy(), tmp.copy())
        # 箭头(p)
        vec_p = vec_tail_up.copy()
        # p
        p = (
            TextMobject("P", color=BLACK)
            .scale(0.7 * (narrow_multiple / 0.5))
            .next_to(vec_p, DOWN, buff=0.05 * (narrow_multiple / 0.5))
        )
        # 整体 8
        base_8 = VGroup(vec_p.copy(), p.copy())

        # 各整体的位置
        # 整体 6 靠左
        base_6.move_to(frame_animation).align_to(frame_animation, LEFT).shift(
            RIGHT * 0.7 * (narrow_multiple / 0.5)
        )
        # 整体 1 在整体 6 右边
        base_1.next_to(base_6, RIGHT, buff=0.6 * (narrow_multiple / 0.5)).shift(
            UP * 0.4 * (narrow_multiple / 0.5)
        )
        # 整体 2 在整体 1 右边顺序排序
        base_2.next_to(base_1, RIGHT, buff=0.1 * (narrow_multiple / 0.5)).shift(
            DOWN * 0.41 * (narrow_multiple / 0.5)
        )
        # 整体 5 在整体 2 右边
        base_5.next_to(base_2, RIGHT, buff=0.2 * (narrow_multiple / 0.5))
        # 整体 4 在整体 2 的最右边的方块的上面
        base_4.next_to(base_2[inverse_recs - 1][0][0], UP, buff=0.1)

        self.add(frame_animation, base_6, base_1, base_2, base_5, base_4)
        self.wait()

        # --------------- 动画演示 ---------------
        def ignore_space_len(num):
            origin_len = len(inverse_codes[num])
            begin = origin_len - 1
            record = 0
            for index in range(begin, 0, -1):
                if inverse_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.20
                elif inverse_codes[num][index] == " " and record == 0:
                    record = 1
                elif inverse_codes[num][index] != " ":
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
        ).move_to(codes_inverse[0][0]).align_to(codes_inverse[0][0], RIGHT).shift(
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
        skip()
        # 第二行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(1),
            move_frame.move_to,
            codes_inverse[0][1],
            move_frame.align_to,
            codes_inverse[0][1],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 整体 8 出现
        base_8.next_to(base_2[0][0][0], DOWN, buff=0.1)
        self.play(FadeInFrom(base_8, UP))
        self.wait()
        # 第三行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(2),
            move_frame.move_to,
            codes_inverse[0][2],
            move_frame.align_to,
            codes_inverse[0][2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 建立一个相同的整体 5
        base_5_same = (
            base_5.copy()
            .next_to(base_1, LEFT, buff=0.2 * (narrow_multiple / 0.5))
            .shift(DOWN * 0.4)
        )
        self.play(base_6.shift, DOWN * 0.7, base_1.flip, FadeInFrom(base_5_same, LEFT))
        self.play(base_1[1].flip)
        self.wait()
        # 第四行代码
        self.play(
            move_frame.set_width,
            ignore_space_len(3),
            move_frame.move_to,
            codes_inverse[0][3],
            move_frame.align_to,
            codes_inverse[0][3],
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
            codes_inverse[0][4],
            move_frame.align_to,
            codes_inverse[0][4],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        # 整体 3 出现，但之后会旋转，因此建立一个临时的整体 3，也建立一个临时的整体 8，用于转换
        base_3_tmp = base_3.copy().next_to(base_2[0][0][0], DOWN, buff=0.1)
        base_3_tmp[1].rotate(
            angle=(2 * PI - PI / 6), about_point=base_2[0][0][0].get_center()
        )
        base_3_tmp[0].shift(
            LEFT * 0.5 * (narrow_multiple / 0.5) + UP * 0.06 * (narrow_multiple / 0.5)
        )
        base_8_tmp = base_8.copy()
        self.play(FadeOut(base_4), ReplacementTransform(base_8_tmp, base_3_tmp))
        self.wait()
        # 用 for 循环代替 while
        for circles in range(inverse_recs):  # inverse_recs
            self.play(
                move_frame.set_width,
                ignore_space_len(5),
                move_frame.move_to,
                codes_inverse[0][5],
                move_frame.align_to,
                codes_inverse[0][5],
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
                codes_inverse[1][1],
                move_frame.align_to,
                codes_inverse[1][1],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            # 整体 7 出现
            if circles < inverse_recs - 1:
                base_7.next_to(base_2[circles + 1][0][0], DOWN, buff=0.1)
            elif circles == inverse_recs - 1:
                base_7.next_to(base_5, DOWN, buff=0.1)
            self.play(FadeInFrom(base_7, UP))
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(8),
                move_frame.move_to,
                codes_inverse[1][2],
                move_frame.align_to,
                codes_inverse[1][2],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            if circles == 0:
                self.play(
                    base_1.shift,
                    UP * 0.7 * (narrow_multiple / 0.5),
                    base_5_same.shift,
                    UP * 0.7 * (narrow_multiple / 0.5),
                )
                self.wait()
            self.play(base_2[circles].flip)
            if circles != 0:
                self.play(base_2[circles][1].flip)
            self.wait()
            if circles == 0:
                # 再建立一个相同的整体 5
                base_5_equal = base_5.copy().next_to(
                    base_2[0], LEFT, buff=0.2 * (narrow_multiple / 0.5)
                )
                self.play(
                    base_3_tmp.shift,
                    RIGHT * 1.025 * (narrow_multiple / 0.5),
                    base_8.shift,
                    RIGHT * 1.025 * (narrow_multiple / 0.5),
                    FadeInFrom(base_5_equal, LEFT),
                )
            else:
                self.play(base_8.shift, RIGHT * 1.025 * (narrow_multiple / 0.5))
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(9),
                move_frame.move_to,
                codes_inverse[1][3],
                move_frame.align_to,
                codes_inverse[1][3],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            if circles == 0:
                move_down = VGroup(
                    base_2, base_5, base_3_tmp, base_5_equal, base_8, base_7
                )
                self.play(move_down.shift, DOWN * 0.5 * (narrow_multiple / 0.5))
                self.wait()
                self.play(
                    base_1[0][2].rotate,
                    {"angle": 90 * DEGREES, "about_point": base_1[0][2].get_start()},
                    FadeOut(base_5_same),
                )
                self.play(base_1.shift, RIGHT * 2.3 * (narrow_multiple / 0.5))
            else:
                self.play(base_1.shift, RIGHT * 1.61 * (narrow_multiple / 0.5))
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(10),
                move_frame.move_to,
                codes_inverse[1][4],
                move_frame.align_to,
                codes_inverse[1][4],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.1,
                move_frame.set_height,
                {"height": 0.45, "stretch": True},
                run_time=1,
            )
            self.wait()
            if circles == 0:
                self.play(
                    base_8.move_to,
                    base_7,
                    FadeOut(base_7),
                    base_3_tmp[1].rotate,
                    {"angle": PI / 6, "about_point": base_2[0][0][0].get_center()},
                    base_3_tmp[0].shift,
                    RIGHT * 0.5 * (narrow_multiple / 0.5),
                )
            else:
                self.play(base_8.move_to, base_7, FadeOut(base_7))
            self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(5),
            move_frame.move_to,
            codes_inverse[0][5],
            move_frame.align_to,
            codes_inverse[0][5],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.1,
            move_frame.set_height,
            {"height": 0.45, "stretch": True},
            run_time=1,
        )
        self.wait()
        self.play(FadeOut(base_5), FadeOut(base_8))
        self.wait()
