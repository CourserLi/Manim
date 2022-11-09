
from manimlib import *
from manimlib.imports import *
from manim_sandbox.utils.imports import *


class Scene_(Scene):
    CONFIG = {
        "camera_config": {
            # "background_image": "1.png",
            "background_color": WHITE,
            "use_plot_depth": True,
        }
    }


class CodeLine_code(Text):

    CONFIG = {
        't2c': {
            'public': '#ffa400',
            'private': '#ffa400',
            'int': '#4b5cc4',
            'template': DARK_BLUE,
            'void': DARK_BLUE,
            'class': DARK_BLUE,
            'bool': '#D0104C',
            'elemType': TEAL_D,
            "Node": PURPLE,  # E439A1
            '0': RED_D,
            '1': average_color(BLUE, PINK),
            '2': average_color(BLUE, PINK),
            '3': average_color(BLUE, PINK),
            '4': average_color(BLUE, PINK),
            '5': average_color(BLUE, PINK),
            '6': average_color(BLUE, PINK),
            '7': average_color(BLUE, PINK),
            '8': average_color(BLUE, PINK),
            '9': average_color(BLUE, PINK),
            '10': average_color(BLUE, PINK),
            # 'clear': '#44cef6',
            # 'traverse': '#ff461f',
            # 'insert': '#00bc12',
            # 'remove': '#ff7500',
            # 'search': '#eacd76',
            # 'visit': '#725e82',
            # 'inverse': '#801dae',
            # 'empty': '#9b4400',
            # 'size': '#75878a',
        },
        'font': 'Consolas',
        'size': 0.5,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class CodeLine_func(Text):

    CONFIG = {
        't2c': {
            'clear': '#44cef6',
            'traverse': '#ff461f',
            'insert': '#00bc12',
            'remove': '#ff7500',
            'search': '#eacd76',
            'visit': '#725e82',
            'inverse': '#801dae',
            'empty': '#9b4400',
            'size': '#75878a',
            'ally': '#003371',
            'Union': '#cb3a56',
            'resize': '#1bd1a5',
            'getposition': '#725e82',
        },
        'font': 'Consolas',
        'size': 0.8,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class OpeningScene(Scene_):
    def construct(self):
        t2c = {"可视化": average_color(PINK, RED),
               "线性表": GOLD,
               "数据结构": "#44cef6"}
        text_color = DARK_GRAY

        font = "庞门正道标题体"
        text_1 = Text("同学们好!", font=font, color=text_color,
                      size=1, t2c=t2c).scale(2.25).to_edge(UP * 2, buff=1)
        text_2 = Text("欢迎来到数据结构视频教程", font=font,
                      color=text_color, size=1, t2c=t2c).scale(2.25).to_edge(UP * 3.2, buff=1)
        text_3 = Text("本期视频我们将学习", font=font, color=text_color,
                      size=1, t2c=t2c).scale(2.25).to_edge(UP * 2, buff=1)
        text_4 = Text("线性表", font=font, color=text_color,
                      size=1, t2c=t2c).scale(2.25).to_edge(UP * 3.2, buff=1)
        text_5 = Text("视频将会以最清晰的动画", font=font, color=text_color,
                      size=1, t2c=t2c).scale(2.25).to_edge(UP * 2, buff=1)
        text_6 = Text("可视化线性表的代码", font=font, color=text_color,
                      size=1, t2c=t2c).scale(2.25).to_edge(UP * 3.2, buff=1)
        text_56, text_34, text_12 = VGroup(text_5, text_6), VGroup(
            text_3, text_4), VGroup(text_1, text_2)

        methods = [['clear', 'traverse', 'insert', 'remove'],
                   ['search', 'visit', 'inverse', 'empty'],
                   ['size, ', 'ally, ', 'Union, ', 'resize, ', 'getposition']]
        m_group_1 = VGroup(*[CodeLine_func(tex + ', ', size=0.42, font='Consolas',
                                           stroke_width=2, color=BLUE_D) for tex in methods[0]]).arrange(RIGHT)
        m_group_2 = VGroup(*[CodeLine_func(tex + ', ', size=0.42, font='Consolas',
                                           stroke_width=2, color=BLUE_D) for tex in methods[1]]).arrange(RIGHT)
        m_group_3 = VGroup(*[CodeLine_func(tex, size=0.42, font='Consolas', stroke_width=2,
                                           color=BLUE_D) for tex in methods[2]]).arrange(RIGHT)
        m_group = VGroup(m_group_1, m_group_2, m_group_3).arrange(
            DOWN, aligned_edge=LEFT, buff=0.42)
        methodes_group = VGroup(
            *m_group_1, *m_group_2, *m_group_3).scale(2).next_to(text_56, DOWN, buff=0.5)

        self.wait(0.5)
        self.play(Write(text_1))
        self.wait(0.5)
        self.play(WriteRandom(text_2), run_time=1.5)
        self.wait(1.8)
        self.play(ReplacementTransform(text_12, text_34), run_time=1.2)
        self.wait(1.8)
        self.play(ReplacementTransform(text_34, text_56), run_time=1.2)
        self.wait(1.2)
        self.play(FadeInRandom(methodes_group), run_time=2.4)
        self.wait(2.6)
        self.play(FadeOutRandom(methodes_group), FadeOutRandom(text_5),
                  FadeOutRandom(text_6), run_time=1.8)
        self.wait()


class List(Scene_):
    def construct(self):
        t2c = {"空表": BLUE,
               "线性表": GOLD,
               "元素": average_color(PINK, RED)}
        tex_bg = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                  fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg.set_height(7.5, stretch=True).set_width(8.5, stretch=True)
        tex_bg.to_corner(UP*0.5+LEFT*0.5)
        codes = [
            "template <class elemType>",
            "class List",
            "{",
            "public:",
            "    virtual void clear() = 0;",
            "    virtual void traverse() const = 0;",
            "    virtual void insert(int i, const elemType &value) = 0;",
            "    virtual void remove(int i) = 0;",
            "    virtual int search(const elemType &value) const = 0;",
            "    virtual elemType visit(int i) const = 0;",
            "    virtual void inverse() = 0;",
            "    virtual bool empty() const = 0;",
            "    virtual int size() const = 0;",
            "    virtual ~List(){};",
            "};",
        ]
        codes_mob = VGroup(
            *[
                CodeLine_code(code) for code in codes
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob.next_to(tex_bg.get_top(), DOWN, buff=0.2)

        func_1 = CodeLine_func("clear()").to_corner(UP*0.5+RIGHT*4)
        func_2 = CodeLine_func("traverse()").next_to(
            func_1, DOWN, aligned_edge=ORIGIN, buff=0.5)
        func_3 = CodeLine_func("insert()").next_to(
            func_2, DOWN, aligned_edge=ORIGIN, buff=0.5)
        func_4 = CodeLine_func("remove()").next_to(
            func_3, DOWN, aligned_edge=ORIGIN, buff=0.5)
        func_5 = CodeLine_func("search()").next_to(
            func_4, DOWN, aligned_edge=ORIGIN, buff=0.5)
        func_6 = CodeLine_func("visit()").next_to(
            func_5, DOWN, aligned_edge=ORIGIN, buff=0.5)
        func_7 = CodeLine_func("inverse()").next_to(
            func_6, DOWN, aligned_edge=ORIGIN, buff=0.5)
        func_8 = CodeLine_func("empty()").next_to(
            func_7, DOWN, aligned_edge=ORIGIN, buff=0.5)
        func_9 = CodeLine_func("size()").next_to(
            func_8, DOWN, aligned_edge=ORIGIN, buff=0.5)
        functions = VGroup(func_1, func_2, func_3, func_4,
                           func_5, func_6, func_7, func_8, func_9)

        tras_func_1 = CodeLine_code("clear()").next_to(
            codes_mob[4], aligned_edge=RIGHT).shift(LEFT*1.38)
        tras_func_2 = CodeLine_code("traverse()").next_to(
            codes_mob[5], aligned_edge=RIGHT).shift(LEFT*2.41)
        tras_func_3 = CodeLine_code("insert(int i, const elemType &value)").next_to(
            codes_mob[6], aligned_edge=RIGHT).shift(LEFT*3.37)
        tras_func_4 = CodeLine_code("remove(int i)").next_to(
            codes_mob[7], aligned_edge=RIGHT).shift(LEFT*1.8)
        tras_func_5 = CodeLine_code("search(const elemType &value)").next_to(
            codes_mob[8], aligned_edge=RIGHT).shift(LEFT*3.7)
        tras_func_6 = CodeLine_code("visit(int i)").next_to(
            codes_mob[9], aligned_edge=RIGHT).shift(LEFT*2.55)
        tras_func_7 = CodeLine_code("inverse()").next_to(
            codes_mob[10], aligned_edge=RIGHT).shift(LEFT*1.5)
        tras_func_8 = CodeLine_code("empty()").next_to(
            codes_mob[11], aligned_edge=RIGHT).shift(LEFT*2.2)
        tras_func_9 = CodeLine_code("size()").next_to(
            codes_mob[12], aligned_edge=RIGHT).shift(LEFT*2.15)
        tras_functions = VGroup(tras_func_1, tras_func_2, tras_func_3, tras_func_4,
                                tras_func_5, tras_func_6, tras_func_7, tras_func_8, tras_func_9)

        # join
        self.add(tex_bg, codes_mob)

        # show 1
        reveal = Rectangle(height=0.5, width=3.6,
                           opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal.move_to(codes_mob[0])
        self.play(ShowCreation(reveal))
        self.wait()
        reveal_2 = Rectangle(height=0.5, width=1.6,
                             opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal_2.move_to(codes_mob[1])
        self.play(Transform(reveal, reveal_2))
        self.wait()
        reveal_3 = Rectangle(height=0.5, width=1,
                             opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal_3.move_to(codes_mob[3])
        self.play(Transform(reveal, reveal_3))
        self.wait()
        self.play(FadeOut(reveal))
        self.wait()

        # show 2
        self.play(ReplacementTransform(tras_func_1, func_1),
                  ReplacementTransform(tras_func_2, func_2),
                  ReplacementTransform(tras_func_3, func_3),
                  ReplacementTransform(tras_func_4, func_4),
                  ReplacementTransform(tras_func_5, func_5),
                  ReplacementTransform(tras_func_6, func_6),
                  ReplacementTransform(tras_func_7, func_7),
                  ReplacementTransform(tras_func_8, func_8),
                  ReplacementTransform(tras_func_9, func_9))
        self.wait()
        self.play(func_2.shift, DOWN*0.85,
                  func_3.shift, DOWN*0.85*2,
                  func_4.shift, DOWN*0.85*3,
                  FadeOutAndShift(func_5),
                  FadeOutAndShift(func_6),
                  FadeOutAndShift(func_7),
                  FadeOutAndShift(func_8),
                  FadeOutAndShift(func_9))

        # show 3
        text1 = Text("将线性表清空", font="庞门正道标题体", color=BLACK, t2c=t2c).next_to(
            func_1, DOWN*0.85)
        text1_2 = Text("使之成为空表", font="庞门正道标题体", color=BLACK, t2c=t2c).next_to(
            text1, DOWN, buff=0.1)
        text2 = Text("遍历整个线性表", font="庞门正道标题体", color=BLACK,
                     t2c=t2c).next_to(func_2, DOWN*1.6)
        text3 = Text("将一个新元素插入", font="庞门正道标题体", color=BLACK, t2c=t2c).next_to(
            func_3, DOWN*0.85)
        text3_2 = Text("线性表的任意位置", font="庞门正道标题体", color=BLACK, t2c=t2c).next_to(
            text3, DOWN, buff=0.1)
        text4 = Text("将任意一个元素", font="庞门正道标题体", color=BLACK, t2c=t2c).next_to(
            func_4, DOWN*0.85)
        text4_2 = Text("从线性表中删除", font="庞门正道标题体", color=BLACK, t2c=t2c).next_to(
            text4, DOWN, buff=0.1)
        self.play(Write(text1), Write(text1_2))
        self.wait()
        self.play(Write(text2))
        self.wait()
        self.play(Write(text3), Write(text3_2))
        self.wait()
        self.play(Write(text4), Write(text4_2))
        self.wait()
        methoded_out = VGroup(func_1, func_2, func_3, func_4)
        self.play(FadeOutRandom(text1), FadeOutRandom(text1_2), FadeOutRandom(text3), FadeOutRandom(text3_2),
                  FadeOutRandom(text4), FadeOutRandom(text4_2), FadeOutRandom(text2), FadeOutRandom(methoded_out))
        func_5.shift(UP*0.85*4)
        func_6.shift(UP*0.85*3.4)
        func_7.shift(UP*0.85*2.8)
        func_8.shift(UP*0.85*2.2)
        func_9.shift(UP*0.85*1.6)
        text5 = Text("查找一个特定的元素", font="庞门正道标题体", color=BLACK, t2c=t2c).next_to(
            func_5, DOWN*1.2)
        text6 = Text("查找目标位置的元素", font="庞门正道标题体", color=BLACK, t2c=t2c).next_to(
            func_6, DOWN*1.2)
        text7 = Text("逆置线性表", font="庞门正道标题体", color=BLACK,
                     t2c=t2c).next_to(func_7, DOWN*1.2)
        text8 = Text("判断线性表是否为空", font="庞门正道标题体", color=BLACK, t2c=t2c).next_to(
            func_8, DOWN*1.2)
        text9 = Text("返回线性表长度", font="庞门正道标题体", color=BLACK,
                     t2c=t2c).next_to(func_9, DOWN*1.2)
        self.play(FadeInFromDown(func_5),
                  FadeInFromDown(func_6),
                  FadeInFromDown(func_7),
                  FadeInFromDown(func_8),
                  FadeInFromDown(func_9))
        self.play(Write(text5))
        self.wait()
        self.play(Write(text6))
        self.wait()
        self.play(Write(text7))
        self.wait()
        self.play(Write(text8))
        self.wait()
        self.play(Write(text9))
        self.wait()
        reveal_4 = Rectangle(height=0.5, width=1.3,
                             opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal_4.move_to(codes_mob[13]).shift(RIGHT*0.75)
        self.play(ShowCreation(reveal_4))
        self.wait()
        self.play(FadeOut(reveal_4))
        self.wait()


class SeqList(Scene_):
    def construct(self):
        t2c = {"空表": BLUE,
               "线性表": GOLD,
               "元素": average_color(PINK, RED),
               "->": GOLD,
               ".": GOLD,
               "指针": BLUE,
               "类对象": BLUE,
               "运算符": average_color(PINK, RED),
               "new": average_color(PINK, RED),
               "delete": average_color(PINK, RED),
               "data": average_color(PINK, RED),
               "进程退出": GOLD,
               "代码规范": GOLD}
        tex_bg = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                  fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg.set_height(13.5, stretch=True).set_width(7, stretch=True)
        tex_bg.to_corner(UP*0.5+LEFT*0.5)
        codes = [
            "template <class elemType>",
            "class seqList : public List<elemType>",
            "{",
            "public:",
            "    void clear();",
            "    void traverse() const;",
            "    void insert(int i, const elemType &value);",
            "    void remove(int i);",
            "    int search(const elemType &value) const;",
            "    elemType visit(int i) const;",
            "    void inverse();",
            "    void ally(seqList<elemType> &B);",
            "    bool empty() const {",
            "        return curLength == 0;",
            "    }",
            "    int size() const {",
            "        return curLength;",
            "    }",
            "    seqList(int initSize = 10);",
            "    seqList(seqList &tmpList);",
            "    ~seqList();",
            "",
            "private:",
            "    elemType *data;",
            "    int curLength;",
            "    int maxSize;",
            "    void resize();",
            "};",
        ]
        codes_mob = VGroup(
            *[
                CodeLine_code(code) for code in codes
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob.next_to(tex_bg.get_top(), DOWN, buff=0.2)

        # VGroup
        link_codes = VGroup(tex_bg, codes_mob)

        # show 1
        link_codes.scale(0.58)
        link_codes.shift(UP*3+RIGHT*3.4)
        self.add(link_codes)
        self.play(link_codes.scale, 2, link_codes.shift, DOWN*4)
        self.wait()
        reveal = Rectangle(height=0.5, width=4.2,
                           opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal.move_to(codes_mob[0])
        self.play(ShowCreation(reveal))
        self.wait()
        reveal_2 = Rectangle(height=0.5, width=6,
                             opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal_2.move_to(codes_mob[1])
        self.play(Transform(reveal, reveal_2))
        self.wait()
        self.play(FadeOut(reveal))
        self.wait()
        self.play(link_codes.shift, UP*2.35, run_time=1)
        self.wait()
        reveal_3 = Rectangle(height=7.7, width=7,
                             fill_opacity=0.2, fill_color=BLUE, stroke_color=GOLD)
        reveal_3.move_to(codes_mob[10]).shift(DOWN*0.25+RIGHT*2.4)
        self.play(ShowCreation(reveal_3))
        reveal_4 = Rectangle(height=0.5, width=5.2,
                             fill_opacity=0.2, fill_color=BLUE, stroke_color=GOLD)
        reveal_4.move_to(codes_mob[11]).shift(RIGHT*0.35)
        self.wait()
        self.play(Transform(reveal_3, reveal_4))  # 一会我们会细讲
        self.wait()
        self.play(FadeOut(reveal_3))
        self.wait()
        self.play(link_codes.shift, UP*(8-2.35), run_time=1)
        self.wait()
        reveal_5 = Rectangle(height=1.8, width=4.6,
                             fill_color=BLUE, stroke_color=GOLD)
        reveal_5.move_to(codes_mob[19]).shift(RIGHT*0.5)
        self.play(ShowCreation(reveal_5))
        self.wait()
        reveal_6 = Rectangle(height=1.2, width=4.6,
                             fill_opacity=0.2, fill_color=BLUE, stroke_color=BLUE, stroke_opacity=0)
        reveal_6.move_to(codes_mob[19]).shift(RIGHT*0.5+UP*0.3)
        reveal_7 = Rectangle(height=0.6, width=4.6,
                             fill_opacity=0.2, fill_color=RED, stroke_color=RED, stroke_opacity=0)
        reveal_7.move_to(codes_mob[19]).shift(RIGHT*0.5+DOWN*0.6)
        self.play(ShowCreation(reveal_6))
        self.wait()
        self.play(ShowCreation(reveal_7))
        self.wait()
        changing = VGroup(reveal_5, reveal_6, reveal_7)
        private = Rectangle(height=2.1, width=3,
                            fill_color=GOLD, stroke_color=GOLD)
        private.move_to(codes_mob[24]).shift(DOWN*0.25+RIGHT*0.5)
        self.play(ReplacementTransform(changing, private))
        self.wait()
        self.play(FadeOut(private))

        # show 2
        self.play(link_codes.scale, 0.5, link_codes.shift, DOWN*4)
        self.wait()
        self.play(link_codes.scale, 2, link_codes.shift, DOWN*4+LEFT*2.5)
        self.wait()

        func_1 = CodeLine_func("clear()").to_corner(UP*0.8+RIGHT*4)
        func_2 = CodeLine_func("traverse()").next_to(
            func_1, DOWN, aligned_edge=ORIGIN, buff=0.2)
        func_3 = CodeLine_func("insert()").next_to(
            func_2, DOWN, aligned_edge=ORIGIN, buff=0.2)
        func_4 = CodeLine_func("remove()").next_to(
            func_3, DOWN, aligned_edge=ORIGIN, buff=0.2)
        func_5 = CodeLine_func("search()").next_to(
            func_4, DOWN, aligned_edge=ORIGIN, buff=0.2)
        func_6 = CodeLine_func("visit()").next_to(
            func_5, DOWN, aligned_edge=ORIGIN, buff=0.2)
        func_7 = CodeLine_func("inverse()").next_to(
            func_6, DOWN, aligned_edge=ORIGIN, buff=0.2)
        func_8 = CodeLine_func("ally()").next_to(
            func_7, DOWN, aligned_edge=ORIGIN, buff=0.2)
        func_9 = CodeLine_func("empty()").next_to(
            func_8, DOWN, aligned_edge=ORIGIN, buff=0.2)
        func_10 = CodeLine_func("size()").next_to(
            func_9, DOWN, aligned_edge=ORIGIN, buff=0.2)
        functions = VGroup(func_1, func_2, func_3, func_4, func_5,
                           func_6, func_7, func_8, func_9, func_10)

        # List
        rectangle_0 = Rectangle(height=0.6, width=0.6,
                                opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_1 = rectangle_0.copy()
        rectangle_2 = rectangle_0.copy()
        rectangle_3 = rectangle_0.copy()
        rectangle_1.next_to(rectangle_0, RIGHT, buff=0)
        rectangle_2.next_to(rectangle_1, RIGHT, buff=0)
        rectangle_3.next_to(rectangle_2, RIGHT, buff=0)
        group_rectangle = VGroup(
            rectangle_0, rectangle_1, rectangle_2, rectangle_3)

        # number
        number_0 = TextMobject("0", color=BLACK)
        number_1 = TextMobject("1", color=BLACK)
        number_2 = TextMobject("2", color=BLACK)
        number_3 = TextMobject("3", color=BLACK)
        number_0.scale(0.7)
        number_1.scale(0.7)
        number_2.scale(0.7)
        number_3.scale(0.7)
        number_0.move_to(rectangle_0)
        number_1.move_to(rectangle_1)
        number_2.move_to(rectangle_2)
        number_3.move_to(rectangle_3)
        number = VGroup(number_0, number_1, number_2, number_3)

        group = VGroup(group_rectangle, number)
        group_1 = group.copy().next_to(func_1, DOWN, buff=0.2)
        group_2 = group.copy().next_to(func_2, DOWN, buff=0.2)
        group_3 = group.copy().next_to(func_3, DOWN, buff=0.2)
        group_4 = group.copy().next_to(func_4, DOWN, buff=0.2)
        group_5 = group.copy().next_to(func_5, DOWN, buff=0.2)
        group_6 = group.copy().next_to(func_6, DOWN, buff=0.2)
        group_7 = group.copy().next_to(func_7, DOWN, buff=0.2)
        group_8 = group.copy().next_to(func_8, DOWN, buff=0.2)
        group_9 = group.copy().next_to(func_9, DOWN, buff=0.2)
        group_10 = group.copy().next_to(func_10, DOWN, buff=0.2)

        self.play(FadeInFrom(func_1, direction=LEFT))
        self.wait()
        self.play(ShowCreation(group_1))
        self.wait()
        trans_to_0 = CodeLine_code("0").scale(2).move_to(group_1)
        self.play(ReplacementTransform(group_1, trans_to_0))
        self.wait()
        self.play(FadeOut(trans_to_0))
        self.wait()
        self.play(FadeInFrom(func_2, direction=LEFT))
        self.wait()
        self.play(ShowCreation(group_2))
        self.wait()
        write_num = CodeLine_code("0 1 2 3").scale(
            2).next_to(group_2, DOWN, buff=0.2)
        self.play(Write(write_num))
        self.wait()
        self.play(FadeOut(group_2), FadeOut(write_num))
        self.wait()
        self.play(FadeInFrom(func_3, direction=LEFT))
        self.wait()
        self.play(ShowCreation(group_3))
        self.wait()
        self.play(group_3[0][0].shift, LEFT*0.3, group_3[1][0].shift, LEFT*0.3,
                  group_3[0][1].shift, RIGHT *
                  0.3, group_3[1][1].shift, RIGHT*0.3,
                  group_3[0][2].shift, RIGHT *
                  0.3, group_3[1][2].shift, RIGHT*0.3,
                  group_3[0][3].shift, RIGHT*0.3, group_3[1][3].shift, RIGHT*0.3)
        rectangle_tmp = Rectangle(height=0.6, width=0.6,
                                  opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_tmp.next_to(group_3[0][0], RIGHT, buff=0).shift(DOWN*0.8)
        number_tmp = TextMobject("10", color=BLACK).scale(
            0.7).move_to(rectangle_tmp)
        tmp = VGroup(rectangle_tmp, number_tmp)
        self.play(ShowCreation(tmp))
        self.wait(0.5)
        self.play(tmp.shift, UP*0.8)
        self.wait()
        self.play(FadeOut(group_3), FadeOut(tmp))
        self.wait()
        self.play(FadeInFrom(func_4, direction=LEFT))
        self.wait()
        self.play(ShowCreation(group_4))
        self.wait()
        self.play(FadeOut(group_4[0][1]), FadeOut(group_4[1][1]))
        self.wait()
        self.play(group_4[0][0].shift, RIGHT*0.3, group_4[1][0].shift, RIGHT*0.3,
                  group_4[0][2].shift, LEFT*0.3, group_4[1][2].shift, LEFT*0.3,
                  group_4[0][3].shift, LEFT*0.3, group_4[1][3].shift, LEFT*0.3)
        self.wait()
        fade_group_4 = VGroup(
            group_4[0][0], group_4[0][2], group_4[0][3], group_4[1][0], group_4[1][2], group_4[1][3])
        self.play(FadeOut(fade_group_4))
        self.wait()
        self.play(FadeInFrom(func_5, direction=LEFT))
        self.wait()
        self.play(ShowCreation(group_5))
        self.wait()
        subscript_0 = TextMobject("0", color=BLACK).scale(
            0.4).next_to(group_5[0][0], DOWN*0.5)
        subscript_1 = TextMobject("1", color=BLACK).scale(
            0.4).next_to(group_5[0][1], DOWN*0.5)
        subscript_2 = TextMobject("2", color=BLACK).scale(
            0.4).next_to(group_5[0][2], DOWN*0.5)
        subscript_3 = TextMobject("3", color=BLACK).scale(
            0.4).next_to(group_5[0][3], DOWN*0.5)
        subscript = VGroup(subscript_0, subscript_1, subscript_2, subscript_3)
        self.play(Write(subscript))
        self.wait()
        target = Text("target:2", font="思源宋体 Heavy", color=BLACK).scale(
            0.65).next_to(group_5, DOWN*1.7)
        self.play(Write(target))
        fill_rectangle = Rectangle(height=0.58, width=0.58,
                                   fill_opacity=0.5, fill_color=BLUE, stroke_opacity=0).move_to(group_5[0][0])
        self.play(FadeIn(fill_rectangle))
        self.wait()
        self.play(fill_rectangle.shift, RIGHT*0.6)
        self.wait()
        self.play(fill_rectangle.shift, RIGHT*0.6)
        self.wait()
        self.play(subscript_2.scale, 2.4, subscript_2.move_to, group_5,
                  FadeOut(fill_rectangle), FadeOut(target),
                  FadeOut(group_5), FadeOut(subscript_0),
                  FadeOut(subscript_1), FadeOut(subscript_3))
        self.wait()
        self.play(FadeOut(subscript_2))
        self.wait()
        self.play(FadeInFrom(func_6, direction=LEFT))
        self.wait()
        self.play(ShowCreation(group_6))
        self.wait()
        target.next_to(group_6, DOWN*1.7)
        self.play(Write(target))
        self.wait()
        fill_rectangle.move_to(group_6[0][0])
        self.play(FadeIn(fill_rectangle))
        self.wait()
        self.play(fill_rectangle.shift, RIGHT*0.6)
        self.wait()
        self.play(fill_rectangle.shift, RIGHT*0.6)
        self.wait()
        self.play(group_6[1][2].scale, 1.4, group_6[1][2].move_to, group_6,
                  FadeOut(fill_rectangle), FadeOut(
                      target), FadeOut(group_6[0]),
                  FadeOut(group_6[1][0]), FadeOut(group_6[1][1]), FadeOut(group_6[1][3]))
        self.wait()
        self.play(FadeOut(group_6[1][2]))
        self.wait()
        self.play(FadeInFrom(func_7, direction=LEFT))
        self.wait()
        self.play(ShowCreation(group_7))
        self.wait()
        self.play(Swap(group_7[1][0], group_7[1][3]),
                  Swap(group_7[1][1], group_7[1][2]))
        self.wait()
        self.play(FadeOut(group_7))
        self.wait()
        self.play(FadeInFrom(func_8, direction=LEFT))
        self.wait()
        ally_0 = rectangle_0.copy()
        ally_1 = rectangle_1.copy()
        ally_2 = rectangle_2.copy()
        ally_1.next_to(ally_0, RIGHT, buff=0)
        ally_2.next_to(ally_1, RIGHT, buff=0)
        ally_rectangle_1 = VGroup(ally_0, ally_1, ally_2)
        ally_rectangle_2 = ally_rectangle_1.copy()
        ally_rectangle_1.move_to(group_8)
        ally_rectangle_2.next_to(ally_rectangle_1, DOWN, buff=0.35)
        ally_number_0 = TextMobject("0", color=BLACK).scale(
            0.7).move_to(ally_rectangle_1[0])
        ally_number_1 = TextMobject("2", color=BLACK).scale(
            0.7).move_to(ally_rectangle_1[1])
        ally_number_2 = TextMobject("4", color=BLACK).scale(
            0.7).move_to(ally_rectangle_1[2])
        ally_number_3 = TextMobject("1", color=BLACK).scale(
            0.7).move_to(ally_rectangle_2[0])
        ally_number_4 = TextMobject("3", color=BLACK).scale(
            0.7).move_to(ally_rectangle_2[1])
        ally_number_5 = TextMobject("5", color=BLACK).scale(
            0.7).move_to(ally_rectangle_2[2])
        ally_all_1 = VGroup(ally_rectangle_1, ally_number_0,
                            ally_number_1, ally_number_2)
        ally_all_2 = VGroup(ally_rectangle_2, ally_number_3,
                            ally_number_4, ally_number_5)
        self.play(ShowCreation(ally_all_1),
                  ShowCreation(ally_all_2))
        self.wait()
        union_1 = ally_rectangle_1.copy()
        union_2 = union_1.copy().next_to(union_1, RIGHT, buff=0)
        union = VGroup(union_1, union_2).move_to(group_8)
        self.play(ally_rectangle_1[0].move_to, union_1[0], ally_number_0.move_to, union_1[0],
                  ally_rectangle_2[0].move_to, union_1[1], ally_number_3.move_to, union_1[1],
                  ally_rectangle_1[1].move_to, union_1[2], ally_number_1.move_to, union_1[2],
                  ally_rectangle_2[1].move_to, union_2[0], ally_number_4.move_to, union_2[0],
                  ally_rectangle_1[2].move_to, union_2[1], ally_number_2.move_to, union_2[1],
                  ally_rectangle_2[2].move_to, union_2[2], ally_number_5.move_to, union_2[2],)
        self.wait()
        self.play(FadeOut(ally_all_1), FadeOut(ally_all_2))
        self.wait()

        # turn page
        self.play(link_codes.shift, UP*4, run_time=1)
        self.wait()
        self.play(FadeInFrom(func_9, direction=LEFT))
        self.wait()
        group_99 = group_rectangle.copy().next_to(group_9, DOWN*0.5)
        self.play(ShowCreation(group_9), ShowCreation(group_99))
        self.wait()
        self.play(group_9.shift, LEFT*1, group_99.shift, LEFT*1)
        self.wait()
        return_1 = Text("return:", font="思源宋体 Heavy", color=BLACK).scale(
            0.65).next_to(group_9, RIGHT*1.3)
        return_2 = return_1.copy().next_to(group_99, RIGHT*1.3)
        result_1 = CodeLine_code("0").scale(1.8).next_to(return_1)
        result_2 = CodeLine_code("1").scale(1.8).next_to(return_2)
        self.play(Write(return_1))
        self.play(Write(result_1))
        self.wait()
        self.play(Write(return_2))
        self.play(Write(result_2))
        self.wait()
        fade_group = VGroup(return_1, return_2, result_1,
                            result_2, group_9, group_99)
        self.play(FadeOut(fade_group))
        self.wait()
        self.play(FadeInFrom(func_10, direction=LEFT))
        self.wait()
        self.play(ShowCreation(group_10))
        self.wait()
        self.play(group_10.shift, LEFT*1)
        self.wait()
        return_3 = return_1.copy().next_to(group_10, RIGHT*1.3)
        result_3 = CodeLine_code("4").scale(1.8).next_to(return_3)
        self.play(Write(return_3))
        self.play(Write(result_3))
        self.wait()
        self.play(FadeOut(group_10), FadeOut(return_3), FadeOut(result_3))
        self.wait()

        # turn page
        func_11 = CodeLine_code("seqList(int initSize = 10);", font='思源宋体 Heavy').scale(1.3).next_to(
            func_10, DOWN, aligned_edge=ORIGIN, buff=0.2)
        func_12 = CodeLine_code("seqList(seqList &tmpList);", font='思源宋体 Heavy').scale(1.3).next_to(
            func_11, DOWN, aligned_edge=ORIGIN, buff=0.2)
        func_13 = CodeLine_code("~seqList();", font='思源宋体 Heavy').scale(1.3).next_to(
            func_12, DOWN, aligned_edge=ORIGIN, buff=0.2)
        self.play(FadeInFrom(func_11, direction=LEFT))
        self.play(FadeInFrom(func_12, direction=LEFT))
        self.play(FadeInFrom(func_13, direction=LEFT))
        self.wait()
        self.play(link_codes.shift, UP*4, func_11.move_to, func_2, func_12.move_to,
                  func_6, func_13.move_to, func_10, FadeOut(functions))
        self.wait()

        # private中的全部成员变量共同组成了顺序表，之所以这些成员变量和函数放在private中，是为了隐藏数据，避免被类对象直接引用而遭遇修改（开始转动画）
        # 但要注意的是，只有public中的函数能调用此函数，类变量不能直接调用此函数，resize()函数在后面会详细讲到
        boom_Rectangle = Rectangle(height=3.6, width=4,
                                   fill_color=GOLD, stroke_color=PURPLE).next_to(func_11, RIGHT).shift(RIGHT*4.5+DOWN*1)
        private_code_0 = CodeLine_code("private", font='思源宋体 Heavy').next_to(
            boom_Rectangle.get_top(), DOWN, aligned_edge=ORIGIN, buff=0.25).scale(1.7)
        private_code_1 = CodeLine_code("elemType *data").next_to(
            private_code_0, DOWN, aligned_edge=ORIGIN, buff=0.45).scale(1.5)
        private_code_2 = CodeLine_code("int curLength").next_to(
            private_code_1, DOWN, aligned_edge=ORIGIN, buff=0.3).scale(1.5)
        private_code_3 = CodeLine_code("int maxSize").next_to(
            private_code_2, DOWN, aligned_edge=ORIGIN, buff=0.3).scale(1.5)
        private_code_4 = CodeLine_code("void resize()").next_to(
            private_code_3, DOWN, aligned_edge=ORIGIN, buff=0.3).scale(1.5)
        private_code = VGroup(private_code_0, private_code_1,
                              private_code_2, private_code_3, private_code_4)
        foot_line = Line(opacity=1, stroke_color=BLUE)
        foot_line.set_length(3.8)
        foot_line.next_to(private_code_0, DOWN, buff=0.15)
        self.add(boom_Rectangle, private_code_0, private_code_1, foot_line,
                 private_code_2, private_code_3, private_code_4)
        last_3_funcs = VGroup(func_11, func_12, func_13)
        self.play(link_codes.shift, LEFT*9, func_11.shift, LEFT*9+UP*0.5, boom_Rectangle.shift, LEFT*9, private_code.shift, LEFT*9, foot_line.shift, LEFT*9,
                  func_12.shift, LEFT*9+UP*2, func_13.shift, LEFT*9+UP*3.5, run_time=2)
        self.wait()

        # List + number
        rec_0 = Rectangle(height=0.8, width=0.8,
                          opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rec_1 = rec_0.copy().next_to(rec_0, RIGHT, buff=0)
        rec_2 = rec_0.copy().next_to(rec_1, RIGHT, buff=0)
        rec_3 = rec_0.copy().next_to(rec_2, RIGHT, buff=0)
        group_rec = VGroup(rec_0, rec_1, rec_2, rec_3)
        num_0 = TextMobject("0", color=BLACK).scale(1).move_to(rec_0)
        num_1 = TextMobject("1", color=BLACK).scale(1).move_to(rec_1)
        num_2 = TextMobject("2", color=BLACK).scale(1).move_to(rec_2)
        num_3 = TextMobject("3", color=BLACK).scale(1).move_to(rec_3)
        nums = VGroup(num_0, num_1, num_2, num_3)
        group_rec_nums = VGroup(group_rec, nums)
        group_rec_nums.next_to(func_13, DOWN*8).shift(RIGHT*3.5)
        self.play(ReplacementTransform(private_code_1, group_rec))
        self.wait()
        curLength = TextMobject("curLength", color=BLACK).scale(
            0.7).next_to(group_rec, LEFT*1)
        self.play(ReplacementTransform(private_code_2, curLength))
        self.wait()
        curLength_num_0 = CodeLine_code("= 0").scale(
            2).move_to(curLength)
        curLength_num_0_cp = curLength_num_0.copy()
        curLength_num_1 = CodeLine_code(
            "= 1").scale(2).move_to(curLength_num_0)
        curLength_num_2 = CodeLine_code(
            "= 2").scale(2).move_to(curLength_num_0)
        curLength_num_3 = CodeLine_code(
            "= 3").scale(2).move_to(curLength_num_0)
        curLength_num_4 = CodeLine_code(
            "= 4").scale(2).move_to(curLength_num_0)
        self.play(curLength.shift, LEFT*1.5, FadeIn(curLength_num_0))
        self.wait()
        self.play(Write(num_0), Transform(curLength_num_0, curLength_num_1))
        self.play(Write(num_1), Transform(curLength_num_0, curLength_num_2))
        self.play(Write(num_2), Transform(curLength_num_0, curLength_num_3))
        self.play(Write(num_3), Transform(curLength_num_0, curLength_num_4))
        self.wait()
        maxSize = TextMobject("maxSize", color=BLACK).scale(
            0.7).next_to(group_rec, LEFT*1).shift(DOWN*0.25)
        self.play(curLength.shift, UP*0.25, curLength_num_0.shift,
                  UP*0.25, ReplacementTransform(private_code_3, maxSize))
        self.wait()
        maxSize_num_4 = curLength_num_4.copy().move_to(maxSize).shift(LEFT*0.15)
        self.play(maxSize.shift, LEFT*1.5, FadeIn(maxSize_num_4))
        curLength_num_5 = CodeLine_code(
            "= 5").scale(2).move_to(curLength_num_0)
        curLength_num_6 = CodeLine_code(
            "= 6").scale(2).move_to(curLength_num_0)
        curLength_num_7 = CodeLine_code(
            "= 7").scale(2).move_to(curLength_num_0)
        curLength_num_8 = CodeLine_code(
            "= 8").scale(2).move_to(curLength_num_0)
        num_4 = TextMobject("4", color=BLACK).scale(
            1).move_to(num_3).shift(RIGHT*0.8)
        num_5 = TextMobject("5", color=BLACK).scale(
            1).move_to(num_4).shift(RIGHT*0.8)
        num_6 = TextMobject("6", color=BLACK).scale(
            1).move_to(num_5).shift(RIGHT*0.8)
        num_7 = TextMobject("7", color=BLACK).scale(
            1).move_to(num_6).shift(RIGHT*0.8)
        the_nums = VGroup(num_0, num_1, num_2, num_3,
                          num_4, num_5, num_6, num_7)
        self.wait()
        self.play(Write(num_4), Transform(curLength_num_0, curLength_num_5))
        group_rec_plus = group_rec.copy().next_to(group_rec, RIGHT, buff=0)
        maxSize_num_8 = CodeLine_code("= 8").scale(2).move_to(maxSize_num_4)
        self.play(ReplacementTransform(private_code_4, group_rec_plus),
                  Transform(maxSize_num_4, maxSize_num_8))
        self.wait()
        self.play(Write(num_5), Transform(curLength_num_0, curLength_num_6))
        self.play(Write(num_6), Transform(curLength_num_0, curLength_num_7))
        self.play(Write(num_7), Transform(curLength_num_0, curLength_num_8))
        self.wait()
        # 这样一个就顺序表就构造好了
        # 你可以简单的认为maxSize就是格子的个数，curLength就是数字的个数
        self.play(FadeOut(maxSize_num_4), FadeOut(curLength_num_0), FadeOut(curLength), FadeOut(maxSize), FadeOut(group_rec_plus),
                  FadeOut(group_rec), FadeOut(the_nums), FadeOut(private_code_0), FadeOut(foot_line), FadeOut(boom_Rectangle))
        self.wait()

        # last_page(淦，太累了我)
        old_position_func_11 = func_11.copy()
        old_position_func_12 = func_12.copy()
        self.play(func_11.shift, RIGHT*7, func_12.move_to,
                  old_position_func_11, func_13.move_to, old_position_func_12)
        self.wait()

        # Code block
        background = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                      fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        background.set_height(3.2, stretch=True).set_width(6.7, stretch=True)
        background.next_to(func_11, DOWN*0.5)
        last_codes = [
            "if (initSize <= 0)",
            "    throw badSize();",
            "maxSize = initSize;",
            "data = new elemType[maxSize];",
            "curLength = 0;",
        ]
        last_codes_mob = VGroup(
            *[
                CodeLine_code(code) for code in last_codes
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        last_codes_mob.scale(1.25)
        last_codes_mob.next_to(background.get_top(), DOWN, buff=0.2)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)
        initSize_change_0 = CodeLine_code(
            "seqList(int initSize = 10)", font='思源宋体 Heavy').scale(1.3).move_to(func_11)
        self.play(ShowCreation(background), Write(last_codes_mob),
                  Transform(func_11, initSize_change_0))
        self.wait()

        # int initSize = 10 默认情况下是10，（）也就是什么都不写，int initSize 但是我们在构造函数时可以选择其他整型数字，（4）比如我们选一个4写进去
        initSize_change_1 = CodeLine_code(
            "seqList()", font='思源宋体 Heavy').scale(1.3).move_to(func_11)
        initSize_change_2 = CodeLine_code(
            "seqList(4)", font='思源宋体 Heavy').scale(1.3).move_to(func_11)
        reveal_initSize = Rectangle(height=0.5, width=4.2,
                                    opacity=0, fill_color=GOLD, stroke_color=GOLD).move_to(func_11)
        self.play(ShowCreation(reveal_initSize))
        self.wait(0.5)
        self.play(FadeOut(reveal_initSize))
        self.wait()
        self.play(Transform(func_11, initSize_change_1))
        self.wait()
        self.play(Transform(func_11, initSize_change_2))
        self.wait()
        foot_line.set_length(3.3)
        foot_line.next_to(last_codes_mob[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        i_am_so_tired = CodeLine_code("if (4 <= 0)").scale(1.25).move_to(
            last_codes_mob[0], aligned_edge=LEFT)
        i_am_so_tired_tmp = last_codes_mob[0].copy()
        self.play(Transform(last_codes_mob[0], i_am_so_tired),
                  foot_line.set_length, 1.9, foot_line.shift, LEFT*0.6)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.3)
        foot_line.next_to(last_codes_mob[2], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line), Transform(
            last_codes_mob[0], i_am_so_tired_tmp))
        self.wait()
        i_so_tired = CodeLine_code("maxSize = 4;").scale(1.25).move_to(
            last_codes_mob[2], aligned_edge=LEFT)
        i_so_tired_tmp = last_codes_mob[2].copy()
        self.play(Transform(last_codes_mob[2], i_so_tired),
                  foot_line.set_length, 2, foot_line.shift, LEFT*0.6)
        self.wait()
        group_rec.shift(RIGHT*2+DOWN*1)
        maxSize.next_to(group_rec, LEFT*7)
        maxSize_num_4_change = curLength_num_4.copy()
        maxSize_num_4_change.next_to(maxSize, RIGHT*1)
        self.play(FadeIn(maxSize), FadeIn(maxSize_num_4_change))
        self.wait()
        self.play(FadeOut(foot_line))
        self.wait()
        foot_line.set_length(5)
        foot_line.next_to(last_codes_mob[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        i_tired = CodeLine_code("data = new elemType[4];").scale(1.25).move_to(
            last_codes_mob[3], aligned_edge=LEFT)
        i_tired_tmp = last_codes_mob[3].copy()
        self.play(Transform(last_codes_mob[3], i_tired),
                  foot_line.set_length, 4, foot_line.shift, LEFT*0.5)
        self.wait()
        self.play(FadeIn(group_rec))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.5)
        foot_line.next_to(last_codes_mob[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line), Transform(
            last_codes_mob[2], i_so_tired_tmp), Transform(last_codes_mob[3], i_tired_tmp))
        self.wait()
        curLength.next_to(group_rec, LEFT*7).shift(UP*0.25)
        # curLength_num_4.next_to(curLength, RIGHT*1)
        curLength_num_0_cp.next_to(curLength, RIGHT*1)
        self.play(maxSize.shift, DOWN*0.25,
                  maxSize_num_4_change.shift, DOWN*0.25)
        self.wait()
        self.play(FadeIn(curLength), FadeIn(curLength_num_0_cp))
        self.play(FadeOut(foot_line))

        # 开始下一个 ExampleTikz
        self.wait()
        self.play(FadeOut(last_codes_mob), FadeOut(background), FadeOut(func_11), FadeOut(group_rec),
                  FadeOut(curLength), FadeOut(curLength_num_0_cp), FadeOut(maxSize), FadeOut(maxSize_num_4_change))
        self.wait()
        euqal_change_0 = CodeLine_code(
            "seqList(seqList &tmpList)", font='思源宋体 Heavy').scale(1.3).move_to(func_11)
        euqal_change_1 = CodeLine_code(
            "seqList(tmpList)", font='思源宋体 Heavy').scale(1.3).move_to(func_11)

        # Code block
        background.set_height(3.2, stretch=True).set_width(8, stretch=True)
        background.next_to(func_11, DOWN*0.5)
        last_codes = [
            "this->maxSize = tmpList.maxSize;",
            "this->curLength = tmpList.curLength;",
            "this->data = new elemType[tmpList.maxSize];",
            "for (int i = 0; i < tmpList.curLength; ++i)",
            "    this->data[i] = tmpList.data[i];",
        ]
        last_codes_mob = VGroup(
            *[
                CodeLine_code(code) for code in last_codes
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        last_codes_mob.scale(1.25)
        last_codes_mob.next_to(background.get_top(), DOWN, buff=0.2)
        self.play(func_12.shift, RIGHT*7,
                  func_13.move_to, old_position_func_11)
        self.wait()
        self.play(ShowCreation(background), Write(last_codes_mob),
                  Transform(func_12, euqal_change_0))
        self.wait()
        # ->是指针指向其成员的运算符 .是类对象指向其成员的运算符
        # 最大的区别是->前面回放的是指针，而.前面跟的是类对象
        zz = TextMobject("-->", color=BLACK).next_to(
            func_13, DOWN*1.5)
        text_miao = Text("是指针指向其", font="庞门正道标题体", color=BLACK, t2c=t2c).next_to(
            zz, DOWN*0.7)
        text_miao2 = Text("成员的运算符", font="庞门正道标题体", color=BLACK, t2c=t2c).next_to(
            text_miao, DOWN*0.5)
        self.play(Write(zz), Write(text_miao), Write(text_miao2))
        self.wait()
        d = TextMobject(".", color=BLACK).next_to(
            text_miao2, DOWN*1.5)
        text_miao3 = Text("是类对象指向其", font="庞门正道标题体", color=BLACK, t2c=t2c).next_to(
            d, DOWN*0.7)
        text_miao4 = Text("成员的运算符", font="庞门正道标题体", color=BLACK, t2c=t2c).next_to(
            text_miao3, DOWN*0.5)
        self.play(Write(d), Write(text_miao3), Write(text_miao4))
        self.wait()
        re_0 = Rectangle(height=0.8, width=0.8,
                         opacity=0, fill_color=BLACK, stroke_color=BLACK)
        re_1 = re_0.copy().next_to(re_0, RIGHT, buff=0)
        re_2 = re_0.copy().next_to(re_1, RIGHT, buff=0)
        re_3 = re_0.copy().next_to(re_2, RIGHT, buff=0)
        group_re = VGroup(re_0, re_1, re_2, re_3)
        nu_0 = TextMobject("0", color=BLACK).scale(1).move_to(re_0)
        nu_1 = TextMobject("1", color=BLACK).scale(1).move_to(re_1)
        nu_2 = TextMobject("2", color=BLACK).scale(1).move_to(re_2)
        nu_3 = TextMobject("3", color=BLACK).scale(1).move_to(re_3)
        nus = VGroup(nu_0, nu_1, nu_2, nu_3)
        group_re_nus = VGroup(group_re, nus)
        group_re_nus.to_corner(DOWN*4+LEFT*7.5)
        curLength_last = TextMobject("curLength", color=BLACK).scale(
            0.7).next_to(group_re, LEFT*7).shift(UP*0.25)
        maxSize_last = TextMobject("maxSize", color=BLACK).scale(
            0.7).next_to(group_re, LEFT*7).shift(DOWN*0.25)
        subala_4 = CodeLine_code("= 4").scale(
            2).move_to(curLength_last).shift(RIGHT*1.5)
        subala_4_a = subala_4.copy().shift(DOWN*0.5)
        i_am_the_king = VGroup(group_re_nus, curLength_last,
                               maxSize_last, subala_4, subala_4_a)
        reveal_little_king = Rectangle(height=0.5, width=5,
                                       opacity=0, fill_color=GOLD, stroke_color=GOLD).move_to(func_12)
        # 我们再重新看代码就一目了然了
        self.play(ShowCreation(reveal_little_king))
        self.wait()
        reveal_medium_king = Rectangle(height=0.5, width=3.5,
                                       opacity=0, fill_color=GOLD, stroke_color=GOLD).move_to(func_12)
        # 传入一个类对象
        self.play(Transform(func_12, euqal_change_1), ReplacementTransform(
            reveal_little_king, reveal_medium_king))
        self.wait()
        reveal_king = Rectangle(height=2, width=7,
                                opacity=0, fill_color=GOLD, stroke_color=GOLD).shift(DOWN*1.3+LEFT*3.4)
        tmpList_li = CodeLine_code("tmpList", font='思源宋体 Medium').scale(
            1.6).next_to(reveal_king.get_top(), DOWN, buff=0.2)
        self.play(FadeIn(i_am_the_king), ReplacementTransform(
            reveal_medium_king, reveal_king), Write(tmpList_li))
        self.wait()
        i_am_the_king_li = i_am_the_king.copy().shift(RIGHT*6.9)
        this_li = CodeLine_code("this", font='思源宋体 Medium').scale(
            1.6).next_to(reveal_king.get_top(), DOWN, buff=0.2).shift(RIGHT*6.9)
        self.play(reveal_king.shift, RIGHT*6.9, FadeIn(i_am_the_king_li),
                  FadeOut(tmpList_li), Write(this_li))
        self.wait()

        # 最后的最后了
        i_love_music = VGroup(zz, d, text_miao, text_miao2, text_miao3, text_miao4, func_12,
                              background, last_codes_mob, i_am_the_king_li, i_am_the_king, reveal_king, this_li)
        self.play(FadeOut(i_love_music))
        self.wait()
        emm_change = CodeLine_code(
            "~seqList()", font='思源宋体 Heavy').scale(1.3).shift(UP*3)
        self.play(Transform(func_13, emm_change))
        self.wait()
        background = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                      fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        background.set_height(1.5, stretch=True).set_width(4, stretch=True)
        background.next_to(func_13, DOWN*0.5)
        last_codes = [
            "clear();",
            "delete[] data;",
        ]
        last_codes_mob = VGroup(
            *[
                CodeLine_code(code) for code in last_codes
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        last_codes_mob.scale(1.25)
        last_codes_mob.next_to(background.get_top(), DOWN, buff=0.2)
        re_0 = Rectangle(height=0.8, width=0.8,
                         opacity=0, fill_color=BLACK, stroke_color=BLACK)
        re_1 = re_0.copy().next_to(re_0, RIGHT, buff=0)
        re_2 = re_0.copy().next_to(re_1, RIGHT, buff=0)
        re_3 = re_0.copy().next_to(re_2, RIGHT, buff=0)
        group_re = VGroup(re_0, re_1, re_2, re_3)
        nu_0 = TextMobject("0", color=BLACK).scale(1).move_to(re_0)
        nu_1 = TextMobject("1", color=BLACK).scale(1).move_to(re_1)
        nu_2 = TextMobject("2", color=BLACK).scale(1).move_to(re_2)
        nu_3 = TextMobject("3", color=BLACK).scale(1).move_to(re_3)
        nus = VGroup(nu_0, nu_1, nu_2, nu_3)
        group_re_nus = VGroup(group_re, nus)
        group_re_nus.to_corner(DOWN*4+LEFT*7.5)
        curLength_last = TextMobject("curLength", color=BLACK).scale(
            0.7).next_to(group_re, LEFT*7).shift(UP*0.25)
        maxSize_last = TextMobject("maxSize", color=BLACK).scale(
            0.7).next_to(group_re, LEFT*7).shift(DOWN*0.25)
        subala_4 = CodeLine_code("= 4").scale(
            2).move_to(curLength_last).shift(RIGHT*1.5)
        subala_4_a = subala_4.copy().shift(DOWN*0.5)
        i_am_the_king = VGroup(group_re_nus, curLength_last,
                               maxSize_last, subala_4, subala_4_a).next_to(background, DOWN).shift(DOWN)
        self.play(ShowCreation(background), Write(last_codes_mob))
        self.wait()
        self.play(FadeIn(i_am_the_king))
        self.wait()
        xjb_trans = CodeLine_code("curLength = 0;").scale(
            1.25).move_to(last_codes_mob[0], aligned_edge=LEFT)
        self.play(Transform(last_codes_mob[0], xjb_trans))
        self.wait()
        kimoji_0 = CodeLine_code("= 0").scale(
            2).move_to(subala_4)
        self.play(ReplacementTransform(
            subala_4, kimoji_0), FadeOut(group_re_nus))
        self.wait()
        self.play(curLength_last.shift, RIGHT*2+UP*0.5, maxSize_last.shift,
                  RIGHT*2+UP*0.5, kimoji_0.shift, RIGHT*2+UP*0.5, subala_4_a.shift, RIGHT*2+UP*0.5)
        self.wait()
        # 进程退出时，操作系统会将其所有new过的内存的对象全部自动delete的
        # 但为了代码规范，对于用指针申请数组的data，我们是默认写delete的
        xixo = Text("进程退出时",
                    font="庞门正道标题体", color=BLACK, t2c=t2c).shift(DOWN)
        xixo2 = Text("操作系统会将其所有new过的内存的对象全部自动delete的",
                     font="庞门正道标题体", color=BLACK, t2c=t2c).shift(DOWN*1.5)
        xixo3 = Text("但为了代码规范",
                     font="庞门正道标题体", color=BLACK, t2c=t2c).shift(DOWN*2.5)
        xixo4 = Text("对于用指针申请数组的data，我们是默认写delete的",
                     font="庞门正道标题体", color=BLACK, t2c=t2c).shift(DOWN*3)
        self.play(Write(xixo))
        self.play(Write(xixo2))
        self.wait()
        self.play(Write(xixo3))
        self.play(Write(xixo4))
        self.wait()

        # 后面的代码也是这样的演示方式，动画配合源代码一起食用效果更佳哦~


class LinkList(Scene_):
    def construct(self):
        t2c = {"空表": BLUE,
               "线性表": GOLD,
               "元素": average_color(PINK, RED),
               "head": '#FF6C00',
               "head->next": '#3016B0',
               "tail": '#A64600',
               "空结点": '#FFD330',
               "第一个": '#C9007A',
               "最后一个": '#028E9B'}
        tex_bg = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                  fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg.set_height(19.5, stretch=True).set_width(8, stretch=True)
        tex_bg.to_corner(UP*0.5+LEFT*0.5)
        codes = [
            "template <class elemType>",
            "class linkList : public List<elemType>",
            "{",
            "public:",
            "    void clear();",
            "    void traverse() const;",
            "    void insert(int i, const elemType &value);",
            "    void remove(int i);",
            "    int search(const elemType &value) const;",
            "    elemType visit(int i) const;",
            "    void inverse();",
            "    void Union(linkList<elemType> &B);",
            "    bool empty() const {",
            "        return head->next == NULL;",
            "    }",
            "    int size() const {",
            "        return curLength;",
            "    }",
            "    linkList();",
            "    linkList(linkList &tmpList);",
            "    ~linkList();",
            "",
            "private:",
            "    struct Node",
            "    {",
            "        elemType data;",
            "        Node *next;",
            "        Node(Node *p = NULL) {",
            "            next = p;",
            "        }",
            "        Node(const elemType value, Node *p = NULL)",
            "        {",
            "            data = value;",
            "            next = p;",
            "        }",
            "    };",
            "    Node *head;",
            "    Node *tail;",
            "    int curLength;",
            "    Node *getPosition(int i) const;",
            "};",
        ]
        codes_mob = VGroup(
            *[
                CodeLine_code(code) for code in codes
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob.next_to(tex_bg.get_top(), DOWN, buff=0.2)

        # VGroup
        link_codes = VGroup(tex_bg, codes_mob)

        # join entirety
        link_codes.scale(0.4)
        link_codes.shift(UP*6+RIGHT*3.2)

        # show two parts
        tex_bg_left = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                       fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg_right = tex_bg_left.copy()
        tex_bg_left.set_height(9, stretch=True).set_width(8, stretch=True)
        tex_bg_right.set_height(10, stretch=True).set_width(8, stretch=True)
        tex_bg_left.to_corner(UP*0.5+LEFT*0.5)
        tex_bg_right.to_corner(UP*0.5+RIGHT*0.5)
        codes_left = [
            "template <class elemType>",
            "class linkList : public List<elemType>",
            "{",
            "public:",
            "    void clear();",
            "    void traverse() const;",
            "    void insert(int i, const elemType &value);",
            "    void remove(int i);",
            "    int search(const elemType &value) const;",
            "    elemType visit(int i) const;",
            "    void inverse();",
            "    void Union(linkList<elemType> &B);",
            "    bool empty() const {",
            "        return head->next == NULL;",
            "    }",
            "    int size() const {",
            "        return curLength;",
            "    }",
        ]
        codes_mob_left = VGroup(
            *[
                CodeLine_code(code) for code in codes_left
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_left.next_to(tex_bg_left.get_top(), DOWN, buff=0.2)
        codes_right = [
            "    linkList();",
            "    linkList(linkList &tmpList);",
            "    ~linkList();",
            "private:",
            "    struct Node",
            "    {",
            "        elemType data;",
            "        Node *next;",
            "        Node(Node *p = NULL) {",
            "            next = p;",
            "        }",
            "        Node(const elemType value, Node *p = NULL) {",
            "            data = value;",
            "            next = p;",
            "        }",
            "    };",
            "    Node *head;",
            "    Node *tail;",
            "    int curLength;",
            "    Node *getPosition(int i) const;",
            "};",
        ]
        codes_mob_right = VGroup(
            *[
                CodeLine_code(code) for code in codes_right
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_right.next_to(tex_bg_right.get_top(), DOWN, buff=0.2)

        # VGroup
        link_codes_cp = link_codes.copy()
        link_codes_left = VGroup(tex_bg_left, codes_mob_left).scale(
            0.85).shift(UP*0.75+LEFT*0.4)
        link_codes_right = VGroup(tex_bg_right, codes_mob_right).scale(
            0.75).shift(UP*1.3+RIGHT*0.75)

        # transform two parts
        self.add(link_codes, link_codes_cp)
        self.wait()
        self.play(ReplacementTransform(link_codes, link_codes_left),
                  ReplacementTransform(link_codes_cp, link_codes_right))
        # self.add(link_codes_left, link_codes_right)
        self.wait()
        # show whole
        reveal = Rectangle(height=0.4, width=3,
                           opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal.move_to(codes_mob_left[0])
        self.play(ShowCreation(reveal))
        self.wait()
        reveal2 = Rectangle(height=0.4, width=5,
                            opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal2.move_to(codes_mob_left[1])
        self.play(Transform(reveal, reveal2))
        self.wait()
        reveal3 = Rectangle(height=6, width=6,
                            opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal3.move_to(codes_mob_left[10]).shift(RIGHT*1.5)
        self.play(Transform(reveal, reveal3))
        self.wait()
        reveal4 = Rectangle(height=0.4, width=4.6,
                            opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal4.move_to(codes_mob_left[11]).shift(RIGHT*0.3)
        self.play(Transform(reveal, reveal4))
        self.wait()
        reveal5 = Rectangle(height=1.1, width=3.8,
                            opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal5.move_to(codes_mob_right[1]).shift(RIGHT*0.3)
        self.play(Transform(reveal, reveal5))
        self.wait()
        reveal_6 = Rectangle(height=0.7, width=3.8,
                             fill_opacity=0.2, fill_color=BLUE, stroke_color=BLUE, stroke_opacity=0)
        reveal_6.move_to(codes_mob_right[1]).shift(RIGHT*0.3+UP*0.2)
        reveal_7 = Rectangle(height=0.4, width=3.8,
                             fill_opacity=0.2, fill_color=RED, stroke_color=RED, stroke_opacity=0)
        reveal_7.move_to(codes_mob_right[1]).shift(RIGHT*0.3+DOWN*0.35)
        self.play(ShowCreation(reveal_6))
        self.wait()
        self.play(ShowCreation(reveal_7))
        self.wait()
        # 上面是结构体的定义，用于生成一个链块
        reveal8 = Rectangle(height=4.2, width=5.3,
                            opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal8.move_to(codes_mob_right[10]).shift(RIGHT*2.4+UP*0.15)
        self.play(FadeOut(reveal_6), FadeOut(
            reveal_7), Transform(reveal, reveal8))
        self.wait()
        # 下面含有指针head、指针tail和成员变量，这些是单链表的信息
        reveal9 = Rectangle(height=1.5, width=3.5,
                            opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal9.move_to(codes_mob_right[18]).shift(RIGHT*1+UP*0.15)
        self.play(Transform(reveal, reveal9))
        self.wait()
        # 它们合起来共同组成了单链表
        self.play(FadeOut(reveal))
        self.wait()

        # show left part
        self.play(FadeOut(link_codes_right))
        self.wait()

        func_1 = CodeLine_func("clear()").to_corner(UP*0.8+RIGHT*5)
        func_2 = CodeLine_func("traverse()").next_to(
            func_1, DOWN, aligned_edge=ORIGIN, buff=0.3)
        func_3 = CodeLine_func("insert()").next_to(
            func_2, DOWN, aligned_edge=ORIGIN, buff=0.3)
        func_4 = CodeLine_func("remove()").next_to(
            func_3, DOWN, aligned_edge=ORIGIN, buff=0.3)
        func_5 = CodeLine_func("search()").next_to(
            func_4, DOWN, aligned_edge=ORIGIN, buff=0.3)
        func_6 = CodeLine_func("visit()").next_to(
            func_5, DOWN, aligned_edge=ORIGIN, buff=0.3)
        func_7 = CodeLine_func("inverse()").next_to(
            func_6, DOWN, aligned_edge=ORIGIN, buff=0.3)
        func_8 = CodeLine_func("Union()").next_to(
            func_7, DOWN, aligned_edge=ORIGIN, buff=0.3)
        func_9 = CodeLine_func("empty()").next_to(
            func_8, DOWN, aligned_edge=ORIGIN, buff=0.3)
        func_10 = CodeLine_func("size()").next_to(
            func_9, DOWN, aligned_edge=ORIGIN, buff=0.3)
        functions = VGroup(func_1, func_2, func_3, func_4, func_5,
                           func_6, func_7, func_8, func_9, func_10)

        # List
        rectangle_front = Rectangle(height=0.4, width=0.4,
                                    opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_later = rectangle_front.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        group_rectangle_0 = VGroup(rectangle_front, rectangle_later)
        group_rectangle_1 = group_rectangle_0.copy().next_to(
            group_rectangle_0, RIGHT, buff=0.35)
        group_rectangle_2 = group_rectangle_0.copy().next_to(
            group_rectangle_1, RIGHT, buff=0.35)
        group_rectangle = VGroup(
            group_rectangle_0, group_rectangle_1, group_rectangle_2)

        # number
        number_0 = TextMobject("0", color=BLACK).scale(
            0.5).move_to(group_rectangle_0[0])
        number_1 = TextMobject("1", color=BLACK).scale(
            0.5).move_to(group_rectangle_1[0])
        number_2 = TextMobject("2", color=BLACK).scale(
            0.5).move_to(group_rectangle_2[0])
        # number_3 = TextMobject("3", color=BLACK).scale(0.5).move_to(group_rectangle_3[0], LEFT)
        # number_4 = TextMobject("4", color=BLACK).scale(0.5).move_to(group_rectangle_4[0], LEFT)
        number = VGroup(number_0, number_1, number_2)

        # arrow_head + arrow_list
        vec_head = Arrow(buff=0.5, color=BLACK).scale(
            0.5).move_to(group_rectangle_0[0]).shift(LEFT*0.5)
        vec_list_0 = Arrow(buff=0.5, color=BLACK).scale(0.5)
        vec_list_1 = vec_list_0.copy()
        vec_list_0.move_to(group_rectangle_0[1]).shift(RIGHT*0.25)
        vec_list_1.move_to(group_rectangle_1[1]).shift(RIGHT*0.25)
        vec_list = VGroup(vec_head, vec_list_0, vec_list_1)

        # text
        text_head = Text("head", font="思源宋体 Heavy", color=BLACK).scale(0.55).move_to(
            vec_head).shift(LEFT*0.7)
        text_null = Text("NULL", font="思源宋体 Heavy", color=BLACK).scale(0.55)

        # ex_link
        ex_link = VGroup(text_head, vec_list, group_rectangle,
                         number).next_to(func_1, DOWN*1)
        # [0] head [1] 箭头 [2] 方块 [3] 数字
        ex_link2 = ex_link.copy().next_to(func_2, DOWN*1)
        ex_link3 = ex_link.copy().next_to(func_3, DOWN*1)
        ex_link4 = ex_link.copy().next_to(func_4, DOWN*1)
        ex_link5 = ex_link.copy().next_to(func_5, DOWN*1)
        ex_link6 = ex_link.copy().next_to(func_6, DOWN*1)
        ex_link7 = ex_link.copy().next_to(func_7, DOWN*1)
        ex_link8 = ex_link.copy().next_to(func_8, DOWN*1)
        ex_link9 = ex_link.copy().next_to(func_9, DOWN*1)
        ex_link10 = ex_link.copy().next_to(func_10, DOWN*1)

        # show clear
        self.play(FadeInFrom(func_1, direction=LEFT))
        self.wait()
        self.play(Write(ex_link))
        self.wait()
        clear_vec_head = Arrow(buff=0.5, color=BLACK).scale(0.5)
        clear_head = Text("head", font="思源宋体 Heavy", color=BLACK).scale(
            0.55).move_to(clear_vec_head).shift(LEFT*0.7)
        clear_null = Text("NULL", font="思源宋体 Heavy", color=BLACK).scale(
            0.55).move_to(clear_vec_head).shift(RIGHT*0.7)
        clear_after = VGroup(clear_vec_head, clear_head,
                             clear_null).next_to(func_1, DOWN*1)
        self.play(Transform(ex_link, clear_after))
        self.wait()
        self.play(FadeOut(ex_link))
        self.wait()
        # show traverse
        self.play(FadeInFrom(func_2, direction=LEFT))
        self.wait()
        self.play(Write(ex_link2))
        self.wait()
        write_num = CodeLine_code("0   1   2").scale(
            1.5).next_to(ex_link2, DOWN, buff=0.2)
        self.play(Write(write_num))
        self.wait()
        self.play(FadeOut(ex_link2), FadeOut(write_num))
        self.wait()
        # show insert
        self.play(FadeInFrom(func_3, direction=LEFT))
        self.wait()
        self.play(Write(ex_link3))
        self.wait()
        insert_front = Rectangle(height=0.4, width=0.4,
                                 opacity=0, fill_color=BLACK, stroke_color=BLACK)
        insert_later = insert_front.copy()
        insert_later.next_to(insert_front, RIGHT, buff=0)
        insert_rectangle = VGroup(insert_front, insert_later)
        insert_rectangle.next_to(ex_link3[2][0], DOWN)
        insert_10 = TextMobject("10", color=BLACK).scale(
            0.5).move_to(insert_rectangle[0])
        insert_list = Arrow(buff=0.5, color=BLACK).scale(
            0.5).move_to(insert_rectangle[1]).shift(RIGHT*0.25)
        insert_list = VGroup(insert_rectangle, insert_10, insert_list)
        self.play(FadeIn(insert_list))
        self.wait()
        ex_link3_left = VGroup(
            ex_link3[0], ex_link3[1][0], ex_link3[1][1], ex_link3[2][0], ex_link3[3][0])
        ex_link3_right = VGroup(
            ex_link3[1][2], ex_link3[2][1], ex_link3[2][2], ex_link3[3][1], ex_link3[3][2])
        self.play(ex_link3_left.shift, LEFT*0.65, ex_link3_right.shift,
                  RIGHT*0.5, insert_list.shift, UP*0.65+RIGHT*0.5)
        self.wait()
        self.play(FadeOut(ex_link3), FadeOut(insert_list))
        self.wait()
        # show remove
        self.play(FadeInFrom(func_4, direction=LEFT))
        self.wait()
        self.play(Write(ex_link4))
        self.wait()
        ex_link4_fadeout = VGroup(
            ex_link4[1][2], ex_link4[2][1], ex_link4[3][1])
        ex_link4_left = VGroup(
            ex_link4[0], ex_link4[1][0], ex_link4[1][1], ex_link4[2][0], ex_link4[3][0])
        ex_link4_right = VGroup(ex_link4[2][2], ex_link4[3][2])
        self.play(FadeOut(ex_link4_fadeout), ex_link4_left.shift,
                  RIGHT*0.65, ex_link4_right.shift, LEFT*0.5)
        self.wait()
        self.play(FadeOut(ex_link4_left), FadeOut(ex_link4_right))
        self.wait()
        # show search
        self.play(FadeInFrom(func_5, direction=LEFT))
        self.wait()
        self.play(Write(ex_link5))
        self.wait()
        subscript_0 = TextMobject("0", color=BLACK).scale(
            0.4).next_to(ex_link5[3][0], DOWN*0.9)
        subscript_1 = TextMobject("1", color=BLACK).scale(
            0.4).next_to(ex_link5[3][1], DOWN*0.9)
        subscript_2 = TextMobject("2", color=BLACK).scale(
            0.4).next_to(ex_link5[3][2], DOWN*0.9)
        subscript = VGroup(subscript_0, subscript_1, subscript_2)
        self.play(Write(subscript))
        target = Text("target:2", font="思源宋体 Heavy", color=BLACK).scale(
            0.65).next_to(ex_link5, DOWN*1.7)
        self.play(Write(target))
        fill_rectangle = Rectangle(height=0.38, width=0.38,
                                   fill_opacity=0.5, fill_color=BLUE, stroke_opacity=0).move_to(ex_link5[2][0][0])
        self.play(FadeIn(fill_rectangle))
        self.wait()
        self.play(fill_rectangle.shift, RIGHT*1.15)
        self.wait()
        self.play(fill_rectangle.shift, RIGHT*1.15)
        self.wait()
        self.play(subscript_2.scale, 2.4, subscript_2.move_to, ex_link5,
                  FadeOut(fill_rectangle), FadeOut(target),
                  FadeOut(ex_link5), FadeOut(subscript_0),
                  FadeOut(subscript_1))
        self.wait()
        self.play(FadeOut(subscript_2))
        self.wait()
        # show visit
        self.play(FadeInFrom(func_6, direction=LEFT))
        self.wait()
        self.play(Write(ex_link6))
        self.wait()
        target.next_to(ex_link6, DOWN*1.7)
        self.play(Write(target))
        self.wait()
        # [0] head [1] 箭头 [2] 方块 [3] 数字
        fill_rectangle.move_to(ex_link6[2][0][0])
        self.play(FadeIn(fill_rectangle))
        self.wait()
        self.play(fill_rectangle.shift, RIGHT*1.15)
        self.wait()
        self.play(fill_rectangle.shift, RIGHT*1.15)
        self.wait()
        self.play(ex_link6[3][2].scale, 1.4, ex_link6[3][2].move_to, ex_link6,
                  FadeOut(fill_rectangle), FadeOut(target), FadeOut(
                      ex_link6[0]), FadeOut(ex_link6[1]),
                  FadeOut(ex_link6[2]), FadeOut(ex_link6[3][0]), FadeOut(ex_link6[3][1]))
        self.wait()
        self.play(FadeOut(ex_link6[3][2]))
        self.wait()
        # show inverse
        self.play(FadeInFrom(func_7, direction=LEFT))
        self.wait()
        self.play(Write(ex_link7))
        self.wait()
        self.play(Swap(ex_link7[3][0], ex_link7[3][2]))
        self.wait()
        self.play(FadeOut(ex_link7))
        self.wait()
        # show Union
        self.play(FadeInFrom(func_8, direction=LEFT))
        self.wait()
        union_front = Rectangle(height=0.4, width=0.4,
                                opacity=0, fill_color=BLACK, stroke_color=BLACK)
        union_later = union_front.copy()
        union_later.next_to(union_front, RIGHT, buff=0)
        union_rectangle1 = VGroup(union_front, union_later)
        union_rectangle2 = union_rectangle1.copy()
        union_rectangle3 = union_rectangle1.copy().next_to(union_rectangle1, RIGHT*1.5)
        union_rectangle4 = union_rectangle1.copy().next_to(union_rectangle2, RIGHT*1.5)
        union_rectangle5 = union_rectangle1.copy().next_to(union_rectangle3, RIGHT*1.5)
        union_1 = TextMobject("0", color=BLACK).scale(
            0.5).move_to(union_rectangle1[0])
        union_2 = TextMobject("1", color=BLACK).scale(
            0.5).move_to(union_rectangle2[0])
        union_3 = TextMobject("2", color=BLACK).scale(
            0.5).move_to(union_rectangle3[0])
        union_4 = TextMobject("3", color=BLACK).scale(
            0.5).move_to(union_rectangle4[0])
        union_5 = TextMobject("4", color=BLACK).scale(
            0.5).move_to(union_rectangle5[0])
        union_list1 = Arrow(buff=0.5, color=BLACK).scale(
            0.5).move_to(union_rectangle1[0]).shift(LEFT*0.5)
        union_list2 = union_list1.copy().move_to(
            union_rectangle2[0]).shift(LEFT*0.5)
        union_list3 = union_list1.copy().move_to(
            union_rectangle3[0]).shift(LEFT*0.5)
        union_list4 = union_list1.copy().move_to(
            union_rectangle4[0]).shift(LEFT*0.5)
        union_list5 = union_list1.copy().move_to(
            union_rectangle5[0]).shift(LEFT*0.5)
        union_head1 = Text("head", font="思源宋体 Heavy", color=BLACK).scale(0.55).move_to(
            union_list1).shift(LEFT*0.7)
        union_head2 = union_head1.copy().move_to(union_list2).shift(LEFT*0.7)
        merge_up = VGroup(union_head1, union_rectangle1, union_rectangle3, union_rectangle5,
                          union_1, union_3, union_5, union_list1, union_list3, union_list5).move_to(ex_link8)
        merge_down = VGroup(union_head2, union_rectangle2,
                            union_rectangle4, union_2, union_4, union_list2, union_list4).move_to(ex_link8).shift(DOWN*0.75)
        merges = VGroup(merge_up, merge_down)
        self.play(Write(merge_up), Write(merge_down))
        self.wait()

        # union_rectangle2.next_to(union_rectangle1, RIGHT*1.5)
        # union_rectangle3.next_to(union_rectangle2, RIGHT*1.5)
        # union_rectangle4.next_to(union_rectangle3, RIGHT*1.5)
        # union_rectangle5.next_to(union_rectangle4, RIGHT*1.5)
        # union_1.move_to(union_rectangle1[0])
        # union_2.move_to(union_rectangle2[0])
        # union_3.move_to(union_rectangle3[0])
        # union_4.move_to(union_rectangle4[0])
        # union_5.move_to(union_rectangle5[0])
        # union_list1.move_to(union_rectangle1[0]).shift(LEFT*0.5)
        # union_list2.move_to(union_rectangle2[0]).shift(LEFT*0.5)
        # union_list3.move_to(union_rectangle3[0]).shift(LEFT*0.5)
        # union_list4.move_to(union_rectangle4[0]).shift(LEFT*0.5)
        # union_list5.move_to(union_rectangle5[0]).shift(LEFT*0.5)

        union_entire1 = VGroup(union_rectangle1, union_1, union_list1)
        union_entire2 = VGroup(union_rectangle2, union_2, union_list2)
        union_entire3 = VGroup(union_rectangle3, union_3, union_list3)
        union_entire4 = VGroup(union_rectangle4, union_4, union_list4)
        union_entire5 = VGroup(union_rectangle5, union_5, union_list5)
        self.play(union_head1.shift, LEFT*1.4, union_entire1.shift, LEFT*1.4, union_entire2.shift, UP*0.75+LEFT*0.85, union_entire3.shift, LEFT*0.27,
                  union_entire4.shift, UP*0.75+RIGHT*0.3, union_entire5.shift, RIGHT*0.85, FadeOut(union_head2))
        self.wait()
        merge_down_cp = VGroup(union_rectangle2,
                               union_rectangle4, union_2, union_4, union_list2, union_list4)
        self.play(FadeOut(merge_up), FadeOut(merge_down_cp))
        self.wait()
        # show empty
        self.play(FadeInFrom(func_9, direction=LEFT))
        self.wait()
        ex_link.move_to(ex_link9).shift(DOWN*0.75)
        self.play(Write(ex_link9), Write(ex_link))
        self.wait()
        self.play(ex_link9.shift, LEFT*1.4, ex_link.shift, LEFT*1.4)
        self.wait()
        return_1 = Text("return:", font="思源宋体 Heavy", color=BLACK).scale(
            0.65).next_to(ex_link9, RIGHT*1.3)
        return_2 = return_1.copy().next_to(ex_link, RIGHT*6)
        result_1 = CodeLine_code("0").scale(1.8).next_to(return_1)
        result_2 = CodeLine_code("1").scale(1.8).next_to(return_2)
        self.play(Write(return_1))
        self.play(Write(result_1))
        self.wait()
        self.play(Write(return_2))
        self.play(Write(result_2))
        self.wait()
        fade_group = VGroup(return_1, return_2, result_1,
                            result_2, ex_link9, ex_link)
        self.play(FadeOut(fade_group))
        self.wait()
        # show size
        self.play(FadeInFrom(func_10, direction=LEFT))
        self.wait()
        self.play(Write(ex_link10))
        self.wait()
        self.play(ex_link10.shift, LEFT*1.4)
        self.wait()
        return_3 = return_1.copy().next_to(ex_link10, RIGHT*1.3)
        result_3 = CodeLine_code("3").scale(1.8).next_to(return_3)
        self.play(Write(return_3))
        self.play(Write(result_3))
        self.wait()
        fade_group2 = VGroup(return_3, result_3, ex_link10)
        self.play(FadeOut(fade_group2))
        self.wait()

        # show right part
        self.play(FadeOut(functions))
        self.wait()
        self.play(FadeOut(link_codes_left), FadeIn(link_codes_right))
        self.wait()
        # self.play(FadeOut(link_codes_left))  # 待删
        self.wait()
        node_front = Rectangle(height=0.4, width=0.4,
                               opacity=0, fill_color=BLACK, stroke_color=BLACK)
        node_later = node_front.copy()
        node_later.next_to(node_front, RIGHT, buff=0)
        node_rectangle = VGroup(
            node_front, node_later).to_corner(UP*1.5+LEFT*1.5)
        node_list = Arrow(buff=0.5, color=BLACK).scale(
            0.5).move_to(node_rectangle[1]).shift(RIGHT*0.25)
        fill_rectangle = Rectangle(height=0.38, width=0.38,
                                   fill_opacity=0.5, fill_color=BLUE, stroke_opacity=0).move_to(node_rectangle[0])
        node = VGroup(node_rectangle, node_list, fill_rectangle)
        reveal_little_king = Rectangle(height=0.3, width=1.7,
                                       opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal_little_king.move_to(codes_mob_right[4]).shift(RIGHT*0.28)
        self.play(ShowCreation(reveal_little_king))
        self.wait()
        self.play(ShowCreation(node_rectangle))
        self.wait()
        reveal_medium_king = Rectangle(height=0.3, width=1.7,
                                       opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal_medium_king.move_to(codes_mob_right[6]).shift(RIGHT*0.48)
        self.play(ReplacementTransform(reveal_little_king, reveal_medium_king))
        self.wait()
        self.play(ShowCreation(fill_rectangle))
        self.wait()
        reveal_big_king = Rectangle(height=0.3, width=1.5,
                                    opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal_big_king.move_to(codes_mob_right[7]).shift(RIGHT*0.45)
        self.play(ReplacementTransform(reveal_medium_king, reveal_big_king))
        self.wait()
        self.play(ShowCreation(node_list))
        # 这就是一个链块
        self.wait()
        harmony = Text("{", font="思源黑体 CN ExtraLight",
                       color=BLACK).scale(3).next_to(node)
        self.play(Write(harmony))
        self.wait()
        node_up = VGroup(node[0].copy(), node[1].copy()).next_to(
            harmony).shift(UP*0.5+RIGHT*0.5)
        node_null = Text("NULL", font="思源宋体 Heavy", color=BLACK).scale(
            0.55).move_to(node_up[1]).shift(RIGHT*0.7)
        reveal_boom_king = Rectangle(height=1.1, width=2.5,
                                     opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal_boom_king.move_to(codes_mob_right[9]).shift(RIGHT*0.9)
        self.play(ReplacementTransform(reveal_big_king, reveal_boom_king))
        self.wait()
        # 一般用于LinkList()构造函数
        self.play(Write(node_up), Write(node_null))
        self.wait()
        node_down = VGroup(node[0].copy(), node[1].copy()).next_to(
            harmony).shift(DOWN*0.5+RIGHT*0.5)
        node_2 = TextMobject("2", color=BLACK).scale(
            0.5).move_to(node_down[0][0])
        node_p = Text("P", font="思源宋体 Heavy", color=BLACK).scale(
            0.55).move_to(node_down[1]).shift(RIGHT*0.4)
        reveal_bing_king = Rectangle(height=1.5, width=5,
                                     opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal_bing_king.move_to(codes_mob_right[12]).shift(RIGHT*1.8+DOWN*0.2)
        self.play(ReplacementTransform(reveal_boom_king, reveal_bing_king))
        self.wait()
        # 一般用于insert()函数
        # 比如我们value取2，p就取指针P代入构造函数中
        self.play(Write(node_down), Write(
            node_2), Write(node_p))
        self.wait()
        reveal_bong_king = Rectangle(height=1.5, width=3.5,
                                     opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal_bong_king.move_to(codes_mob_right[17]).shift(RIGHT*1.2+DOWN*0.2)
        self.play(ReplacementTransform(reveal_bing_king, reveal_bong_king))
        self.wait()
        # 前两个虽然都是指针，但是它们有着显著的差异
        # 指针head指向空结点(链块)，head->next（才）指向链表中的第一个链块的地址
        text_one = Text("指针head指向空结点(链块)的地址", font="庞门正道标题体", color=BLACK, t2c=t2c).scale(0.8).next_to(
            node_down, DOWN*1.5)
        text_two = Text("head->next指向链表中的第一个链块的地址", font="庞门正道标题体", color=BLACK, t2c=t2c).scale(0.8).next_to(
            text_one, DOWN*0.25)
        self.play(Write(text_one))
        self.play(Write(text_two))
        # 举个例子，比方说这个链块是head指向的地址，而这个是head->next指向的地址
        # List
        rectangle_front = Rectangle(height=0.4, width=0.4,
                                    opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_later = rectangle_front.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        group_rectangle_0 = VGroup(rectangle_front, rectangle_later)
        group_rectangle_1 = group_rectangle_0.copy().next_to(
            group_rectangle_0, RIGHT, buff=0.35)
        group_rectangle_2 = group_rectangle_0.copy().next_to(
            group_rectangle_1, RIGHT, buff=0.35)
        group_rectangle = VGroup(
            group_rectangle_0, group_rectangle_1, group_rectangle_2)

        # number
        number_0 = TextMobject("0", color=BLACK).scale(
            0.5).move_to(group_rectangle_1[0])
        number_1 = TextMobject("1", color=BLACK).scale(
            0.5).move_to(group_rectangle_2[0])
        number = VGroup(number_0, number_1)

        # arrow_head + arrow_list
        vec_head = Arrow(buff=0.5, color=BLACK).scale(
            0.5).move_to(group_rectangle_0[0]).shift(LEFT*0.5)
        vec_list_0 = Arrow(buff=0.5, color=BLACK).scale(0.5)
        vec_list_1 = vec_list_0.copy()
        vec_list_2 = vec_list_0.copy()
        vec_list_0.move_to(group_rectangle_0[1]).shift(RIGHT*0.25)
        vec_list_1.move_to(group_rectangle_1[1]).shift(RIGHT*0.25)
        vec_list_2.move_to(group_rectangle_2[1]).shift(RIGHT*0.25)
        vec_list = VGroup(vec_head, vec_list_0, vec_list_1, vec_list_2)

        # text
        text_head = Text("head", font="思源宋体 Heavy", color=BLACK).scale(0.55).move_to(
            vec_head).shift(LEFT*0.7)
        text_null = Text("NULL", font="思源宋体 Heavy", color=BLACK).scale(0.55).move_to(
            vec_list_2).shift(RIGHT*0.7)

        # last_link
        last_link = VGroup(text_head, text_null, vec_list,
                           group_rectangle, number).next_to(text_two, DOWN*2)
        last_link2 = VGroup(
            text_head, text_null, vec_list[1], vec_list[2], vec_list[3], group_rectangle[1], group_rectangle[2], number)
        self.play(ShowCreation(last_link))
        self.wait()
        ex_circle = Circle(
            arc_center=group_rectangle[0].get_center(), radius=0.55, stroke_color=GOLD)
        self.play(ShowCreation(ex_circle))
        self.wait()
        self.play(ex_circle.shift, RIGHT*1.15)
        self.wait()
        self.play(FadeOut(ex_circle))
        self.wait()
        # 但是为了便于演示，之后的动画中我将会省略空结点(链块)，把head和空结点(链块)视为一个整体，但是同学们千万要记得指针head并不直接指向第一个链块的地址，切忌弄混
        to_head = VGroup(last_link[2][0], last_link[3][0])
        self.play(FadeOut(to_head), last_link[0].shift, RIGHT*1.2)
        self.wait()
        self.play(FadeOut(last_link2))
        self.wait()
        # 指针tail指向链表中最后一个链块的地址
        text_three = Text("指针tail指向链表中最后一个链块的地址", font="庞门正道标题体", color=BLACK, t2c=t2c).scale(0.8).next_to(
            text_two, DOWN*1.5)
        self.play(Write(text_three))
        self.wait()
        last_link2.next_to(text_three, DOWN*2)
        last_arrow = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.5, color=BLACK).scale(0.5).move_to(last_link2[6][0]).shift(DOWN*0.5)
        text_tail = Text("tail", font="思源宋体 Heavy",
                         color=BLACK).scale(0.55).move_to(last_arrow).shift(DOWN*0.4)
        self.play(ShowCreation(last_link2), ShowCreation(
            last_arrow), ShowCreation(text_tail))
        self.wait()
        ex_circle.move_to(last_link2[6][0]).shift(RIGHT*0.2)
        self.play(ShowCreation(ex_circle))
        self.wait()
        self.play(FadeOut(ex_circle))
        self.wait()
        text_cur = Text("curLength = 2", font="思源宋体 Heavy", color=BLACK).scale(
            0.55).move_to(text_tail).shift(LEFT*2.5)
        self.play(FadeIn(text_cur))
        self.wait()
        # 最后一个getposition函数的作用是返回目标链块的指针，后面会详细讲到
        reveal_king = Rectangle(height=0.3, width=1.2,
                                opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal_king.move_to(codes_mob_right[0]).shift(RIGHT*0.22)
        self.play(ReplacementTransform(reveal_bong_king, reveal_king))
        self.wait()
        # 接下里我们回到第一个构造函数
        finish = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                  fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        finish.set_height(0.9, stretch=True).set_width(4, stretch=True)
        finish.to_corner(DOWN*3.5+LEFT*3)
        codes_mur = [
            "head = tail = new Node();",
            "curLength = 0;",
        ]
        codes_mob_mur = VGroup(
            *[
                CodeLine_code(code) for code in codes_mur
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_mur.next_to(finish.get_top(), DOWN, buff=0.1)
        self.play(Write(finish), Write(codes_mob_mur))
        self.wait()
        self.play(finish.shift, RIGHT*1.5, codes_mob_mur.shift, RIGHT*1.5)
        the = group_rectangle_0.copy().next_to(finish, DOWN, buff=0.35).shift(LEFT*3)
        world = Arrow(buff=0.5, color=BLACK).scale(
            0.5).move_to(the[1]).shift(RIGHT*0.5)
        world2 = Arrow(np.array([0, 1, 0]), np.array(
            [0, -1, 0]), buff=0.5, color=BLACK).scale(0.5).move_to(the[0]).shift(UP*0.5)
        world3 = Arrow(np.array([0, -1, 0]), np.array([0, 1, 0]), buff=0.5,
                       color=BLACK).scale(0.5).move_to(the[0]).shift(DOWN*0.5)
        hello = Text("head", font="思源宋体 Heavy", color=BLACK).scale(
            0.55).move_to(world2).shift(UP*0.4)
        hello2 = Text("tail", font="思源宋体 Heavy", color=BLACK).scale(
            0.55).move_to(world3).shift(DOWN*0.4)
        hello3 = Text("NULL", font="思源宋体 Heavy", color=BLACK).scale(
            0.55).move_to(world).shift(RIGHT*0.65)
        wofola = Text("curLength = 0", font="思源宋体 Heavy", color=BLACK).scale(
            0.55).move_to(hello2).shift(RIGHT*2.5)
        hello_the_world = VGroup(
            the, world, world2, world3, hello, hello2, hello3, wofola)
        self.play(ShowCreation(hello_the_world))
        self.wait()
        self.play(FadeOut(the), FadeOut(world2), hello.shift, RIGHT*0.28 +
                  DOWN*0.9, world3.shift, RIGHT*0.28, hello2.shift, RIGHT*0.28)
        self.wait()
        # 剩下一个构造函数和析构函数与第一个视频中所讲顺序表的类似，因此同学们可以自行理解


class Introduction(Scene_):
    def construct(self):
        t2c = {"链式表示": BLUE,
               "线性表": GOLD,
               "顺序表示": RED,
               "动态": '#ff0097',
               "静态": "#2edfa3"}
        font = "庞门正道标题体"
        text_1 = Text("线性表", font=font,
                      size=1, t2c=t2c).scale(1.5).to_edge(UP * 1, buff=1)
        text_2 = Text("顺序表示", font=font,
                      size=1, t2c=t2c).scale(1.5).to_edge(UP * 3+LEFT*2, buff=1)
        text_3 = Text("链式表示", font=font,
                      size=1, t2c=t2c).scale(1.5).to_edge(UP * 3+RIGHT*2, buff=1)
        # List
        rectangle_front = Rectangle(height=0.4, width=0.4,
                                    opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_later = rectangle_front.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        group_rectangle_0 = VGroup(rectangle_front, rectangle_later)
        group_rectangle_1 = group_rectangle_0.copy().next_to(
            group_rectangle_0, RIGHT, buff=0.35)
        group_rectangle_2 = group_rectangle_0.copy().next_to(
            group_rectangle_1, RIGHT, buff=0.35)
        group_rectangle = VGroup(
            group_rectangle_0, group_rectangle_1, group_rectangle_2)
        # number
        number_0 = TextMobject("0", color=BLACK).scale(
            0.5).move_to(group_rectangle_0[0])
        number_1 = TextMobject("1", color=BLACK).scale(
            0.5).move_to(group_rectangle_1[0])
        number_2 = TextMobject("2", color=BLACK).scale(
            0.5).move_to(group_rectangle_2[0])
        number = VGroup(number_0, number_1, number_2)
        # arrow_list
        vec_list_0 = Arrow(buff=0.5, color=BLACK).scale(0.5)
        vec_list_1 = vec_list_0.copy()
        vec_list_2 = vec_list_0.copy()
        vec_list_0.move_to(group_rectangle_0[1]).shift(RIGHT*0.25)
        vec_list_1.move_to(group_rectangle_1[1]).shift(RIGHT*0.25)
        vec_list_2.move_to(group_rectangle_2[1]).shift(RIGHT*0.25)
        vec_list = VGroup(vec_list_0, vec_list_1, vec_list_2)

        # ex_link
        text_null = Text("NULL", font="思源宋体 Heavy", color=BLACK).scale(
            0.55).next_to(vec_list_2, RIGHT*0.5)
        ex_link = VGroup(vec_list, group_rectangle, number, text_null)

        # ex_link2
        two_rectangle_front = Rectangle(height=0.4, width=0.4,
                                        opacity=0, fill_color=BLACK, stroke_color=BLACK)
        two_rectangle_later = two_rectangle_front.copy().next_to(
            two_rectangle_front, RIGHT, buff=0)
        two_rectangle_third = two_rectangle_front.copy().next_to(
            two_rectangle_later, RIGHT, buff=0)
        two_group_rectangle_0 = VGroup(
            two_rectangle_front, two_rectangle_later, two_rectangle_third)
        two_group_rectangle_1 = two_group_rectangle_0.copy().next_to(
            two_group_rectangle_0, RIGHT*1.5)
        two_group_rectangle_2 = two_group_rectangle_0.copy().next_to(
            two_group_rectangle_1, RIGHT*1.5)
        two_group_rectangle = VGroup(
            two_group_rectangle_0, two_group_rectangle_1, two_group_rectangle_2)
        medeium_number_0 = TextMobject("0", color=BLACK).scale(
            0.5).move_to(two_group_rectangle_0[1])
        medeium_number_1 = TextMobject("1", color=BLACK).scale(
            0.5).move_to(two_group_rectangle_1[1])
        medeium_number_2 = TextMobject("2", color=BLACK).scale(
            0.5).move_to(two_group_rectangle_2[1])
        medeium_number = VGroup(
            medeium_number_0, medeium_number_1, medeium_number_2)
        two_vec_left = Arrow(np.array([1, 0, 0]), np.array(
            [-1, 0, 0]), buff=0.5, color=BLACK).scale(0.5).move_to(two_group_rectangle_0[0]).shift(LEFT*0.25)
        two_vec_right = Arrow(
            np.array([-1, 0, 0]), np.array([1, 0, 0]), buff=0.5, color=BLACK).scale(0.5).move_to(two_group_rectangle_2[2]).shift(RIGHT*0.25)
        two_vec_1 = two_vec_left.copy().move_to(
            two_group_rectangle_0[2]).shift(RIGHT*0.25)
        two_vec_2 = two_vec_left.copy().move_to(
            two_group_rectangle_1[2]).shift(RIGHT*0.25)
        two_vec_3 = two_vec_right.copy().move_to(
            two_group_rectangle_1[0]).shift(LEFT*0.25)
        two_vec_4 = two_vec_right.copy().move_to(
            two_group_rectangle_2[0]).shift(LEFT*0.25)
        two_vec = VGroup(two_vec_left, two_vec_right,
                         two_vec_1, two_vec_2, two_vec_3, two_vec_4)
        text_null2 = text_null.copy().next_to(
            two_group_rectangle_0[0], LEFT*1.5)
        text_null3 = text_null.copy().next_to(
            two_group_rectangle_2[2], RIGHT*1.5)
        ex_link2 = VGroup(two_group_rectangle, two_vec,
                          medeium_number, text_null3, text_null2)

        # ex_link3
        ex_link3_little = VGroup(
            vec_list[0].copy(), vec_list[1].copy(), group_rectangle.copy(), number.copy())
        arc_fac = ValueTracker(0.)
        arc_arrow = Arrow(ex_link3_little[2][2][1].get_center()+RIGHT*0.2, ex_link3_little[2][0][0].get_center()+LEFT*0.2,
                          color=BLACK, max_tip_length_to_length_ratio=0.08, max_stroke_width_to_length_ratio=1.2)
        arc_fac.set_value(-2)
        arc_arrow.add_updater(lambda l: l.become(
            Arrow(ex_link3_little[2][2][1].get_center()+RIGHT*0.2, ex_link3_little[2][0][0].get_center()+LEFT*0.2,
                  color=BLACK, max_tip_length_to_length_ratio=0.08, max_stroke_width_to_length_ratio=1.2, path_arc=arc_fac.get_value())
        ))
        ex_link3 = VGroup(ex_link3_little, arc_arrow)

        # seq
        rectangle_seq0 = Rectangle(height=0.5, width=0.5,
                                   opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_seq1 = rectangle_seq0.copy().next_to(rectangle_seq0, RIGHT, buff=0)
        rectangle_seq2 = rectangle_seq0.copy().next_to(rectangle_seq1, RIGHT, buff=0)
        rectangle_seq3 = rectangle_seq0.copy().next_to(rectangle_seq2, RIGHT, buff=0)
        rectangle_seq = VGroup(
            rectangle_seq0, rectangle_seq1, rectangle_seq2, rectangle_seq3)
        seq_0 = TextMobject("0", color=BLACK).scale(
            0.6).move_to(rectangle_seq[0])
        seq_1 = TextMobject("1", color=BLACK).scale(
            0.6).move_to(rectangle_seq[1])
        seq_2 = TextMobject("2", color=BLACK).scale(
            0.6).move_to(rectangle_seq[2])
        seq_3 = TextMobject("3", color=BLACK).scale(
            0.6).move_to(rectangle_seq[3])
        number = VGroup(seq_0, seq_1, seq_2, seq_3)
        seq_link = VGroup(rectangle_seq, number)
        seq_link2 = seq_link.copy()

        # normal
        rectangle_normal0 = Rectangle(height=0.5, width=0.5,
                                      opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_normal1 = rectangle_normal0.copy().next_to(
            rectangle_normal0, RIGHT, buff=0.3)
        rectangle_normal2 = rectangle_normal0.copy().next_to(
            rectangle_normal1, RIGHT, buff=0.3)
        rectangle_normal3 = rectangle_normal0.copy().next_to(
            rectangle_normal2, RIGHT, buff=0.3)
        rectangle_normal = VGroup(
            rectangle_normal0, rectangle_normal1, rectangle_normal2, rectangle_normal3)
        no_0 = TextMobject("0", color=BLACK).scale(
            0.6).move_to(rectangle_normal0)
        no_1 = TextMobject("1", color=BLACK).scale(
            0.6).move_to(rectangle_normal1)
        no_2 = TextMobject("2", color=BLACK).scale(
            0.6).move_to(rectangle_normal2)
        no_3 = TextMobject("3", color=BLACK).scale(
            0.6).move_to(rectangle_normal3)
        number_n = VGroup(no_0, no_1, no_2, no_3)
        no_list = VGroup(rectangle_normal, number_n)

        # position
        ex_link.move_to(text_3).shift(DOWN*1)
        ex_link2.move_to(ex_link).shift(DOWN*1)
        ex_link3.move_to(ex_link2).shift(DOWN*1.5)
        seq_link.move_to(text_2).shift(DOWN*1.5).shift(RIGHT*1)
        seq_link2.move_to(seq_link).shift(DOWN*1.5)
        no_list.move_to(text_1).shift(DOWN*1)
        text_o = Text("动态顺序表", font="思源宋体 Heavy", t2c=t2c,
                      color=BLACK).move_to(seq_link).shift(LEFT*2.5)
        text_t = Text("静态顺序表", font="思源宋体 Heavy", t2c=t2c,
                      color=BLACK).move_to(seq_link2).shift(LEFT*2.5)
        text_th = Text("单链表", font="思源宋体 Heavy", t2c=t2c,
                       color=BLACK).move_to(ex_link).shift(LEFT*3.1)
        text_f = Text("双链表", font="思源宋体 Heavy", t2c=t2c, color=BLACK).move_to(
            ex_link2).shift(LEFT*3.1+DOWN*0.5)
        text_fi = Text("循环链表", font="思源宋体 Heavy", t2c=t2c,
                       color=BLACK).move_to(ex_link3).shift(LEFT*3)
        #self.add(text_1, text_2, text_3, ex_link, ex_link2, ex_link3,seq_link,seq_link2)
        #self.add(text_o, text_t, text_th, text_f, text_fi,no_list)
        self.wait()

        # show
        text_1_cp = text_1.copy()
        text_1_cpp = text_1.copy()
        self.play(Write(text_1))
        self.play(Write(no_list))
        self.wait()
        self.play(ReplacementTransform(text_1_cp, text_2))
        self.wait()
        self.play(Write(text_o), Write(seq_link))
        self.play(Write(text_t), Write(seq_link2))
        self.wait()
        self.play(ReplacementTransform(text_1_cpp, text_3))
        self.wait()
        self.play(Write(text_th), Write(ex_link))
        self.play(Write(ex_link2), Write(text_f))
        self.play(Write(text_fi), Write(ex_link3))
        self.wait()
        self.play(FadeOut(text_t), FadeOut(seq_link2),
                  text_o.shift, DOWN*0.5, seq_link.shift, DOWN*0.5)
        self.wait()
        self.play(FadeOut(ex_link2), FadeOut(text_f), text_th.shift, DOWN*1, ex_link.shift, DOWN*1,
                  FadeOut(text_fi), FadeOut(ex_link3))
        self.wait()


class Staff(Scene_):
    CONFIG = {
        "font": "Orbitron",
    }

    def construct(self):
        title = Text("鸣谢", font="庞门正道标题体",
                     color=RED_D, size=1.5).to_edge(UP)
        line = Line(LEFT_SIDE, RIGHT_SIDE, color=RED_D).next_to(title, DOWN)
        title.add(line)
        staff = [
            ["制作", "@李蓝骏"],
            ["配音", "@李蓝骏"],
            ["参考书籍", "@冯广惠《算法与数据结构》"],
            ["参考风格", "@Manim-Kindergarten"]
        ]
        staff_mob = VGroup(*[VGroup() for _ in range(4)])
        for i in range(4):
            staff_mob[0].add(
                Text(staff[i][0], font="庞门正道标题体", size=1.5, color=BLACK))
            staff_mob[1].add(
                Text(staff[i][1], font="思源宋体 CN Heavy", size=1.25, color=BLUE_E))
        for i in range(4):
            staff_mob[i].arrange(DOWN, aligned_edge=LEFT, buff=0.5)
        VGroup(staff_mob[0]).shift(LEFT*4)
        VGroup(staff_mob[1]).shift(RIGHT*3)

        self.wait()
        self.play(Write(title))
        self.wait()
        for i in range(4):
            self.play(
                Write(VGroup(staff_mob[0][i], staff_mob[1][i])),
                run_time=0.5
            )
        self.wait(3)
        self.play(FadeOutAndShift(VGroup(*self.mobjects)))
        self.wait()


class Chapter_list(Scene_):
    def construct(self):
        title1 = TextMobject("数据结构教程", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("Manim 引擎制作", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title3 = TextMobject("Chapter 1", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title4 = TextMobject("List 全局代码演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:5].set_color("#ff2d51")
        title4[0][:4].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        title1.add_updater(anim)
        title2.add_updater(anim)
        anim1 = Write(title1)
        anim2 = Write(title2)
        anim3 = Write(title3)
        anim4 = Write(title4)
        self.wait()
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait(0.4)
        self.wait(2)
        title1.clear_updaters()
        title2.clear_updaters()
        title3.add_updater(anim)
        title4.add_updater(anim)
        self.add(title3, title4)
        turn_animation_into_updater(anim3)
        turn_animation_into_updater(anim4)
        self.play(title1.shift, UP * 5,
                  title1.scale, 0.5,
                  title2.shift, DOWN * 5,
                  title2.scale, 0.5)
        self.wait()
        title = VGroup(title3, title4)
        self.play(FadeOutRandom(title))


class Chapter_seqlist(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 2", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("SeqList 全局代码演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:7].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_seqlist_clear(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 3", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("clear 函数演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:5].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_seqlist_traverse(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 4", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("traverse 函数演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:8].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_seqlist_resize(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 5", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("resize 函数演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:6].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_seqlist_insert(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 6", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("insert 函数演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:6].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_seqlist_remove(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 7", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("remove 函数演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:6].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_seqlist_search(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 8", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("search 函数演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:6].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_seqlist_visit(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 9", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("visit 函数演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:5].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_seqlist_inverse(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 10", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("inverse 函数演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:7].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_linklist(Scene_):
    def construct(self):
        title1 = TextMobject("数据结构教程", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("Manim 引擎制作", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title3 = TextMobject("Chapter 1", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title4 = TextMobject("LinkList 全局代码演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:5].set_color("#ff2d51")
        title4[0][:8].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        title1.add_updater(anim)
        title2.add_updater(anim)
        anim1 = Write(title1)
        anim2 = Write(title2)
        anim3 = Write(title3)
        anim4 = Write(title4)
        self.wait()
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait(0.4)
        self.wait(2)
        title1.clear_updaters()
        title2.clear_updaters()
        title3.add_updater(anim)
        title4.add_updater(anim)
        self.add(title3, title4)
        turn_animation_into_updater(anim3)
        turn_animation_into_updater(anim4)
        self.play(title1.shift, UP * 5,
                  title1.scale, 0.5,
                  title2.shift, DOWN * 5,
                  title2.scale, 0.5)
        self.wait()
        title = VGroup(title3, title4)
        self.play(FadeOutRandom(title))


class Chapter_linklist_clear(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 2", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("clear 函数演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:5].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_linklist_traverse(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 3", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("traverse 函数演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:8].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_linklist_getposition(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 4", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("getposition 函数", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:11].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_linklist_insert(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 5", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("insert 函数演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:6].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_linklist_remove(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 6", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("remove 函数演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:6].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_linklist_search(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 7", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("search 函数演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:6].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_linklist_visit(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 8", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("visit 函数演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:5].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))


class Chapter_linklist_inverse(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 9", color=BLACK).scale(
            2).shift(UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("inverse 函数演示", color=BLACK).scale(
            1.3).shift(DOWN * 0.5).to_edge(RIGHT)
        title2[0][:7].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([
                -obj.get_center()[0] * dt * 2, 0, 0
            ]))

        anim1 = Write(title1)
        anim2 = Write(title2)
        title1.add_updater(anim)
        title2.add_updater(anim)
        self.add(title1, title2)
        turn_animation_into_updater(anim1)
        turn_animation_into_updater(anim2)
        self.wait()
        title = VGroup(title1, title2)
        self.play(FadeOutRandom(title))
