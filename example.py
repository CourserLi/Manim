#!/usr/bin/env python

from manimlib.imports import *
from manim_sandbox.utils.imports import *


class CodeLine(Text):

    CONFIG = {
        't2c': {
            # 'x': average_color(BLUE, PINK),
            # 'y': average_color(BLUE, PINK),
            # 'z': average_color(BLUE, PINK),
            'linkList': TEAL_D,
            'Node': TEAL_D,
            'head': BLUE_D,
            'while': PINK,
            'NULL': DARK_BLUE,
            'template': DARK_BLUE,
            'void': DARK_BLUE,
            'class': DARK_BLUE,
            'tmp': BLUE_D,
            'p': BLUE_D,
            'q': BLUE_D,
            'next': BLUE_D,
            'delete': PINK,
            'tail': BLUE_D,
            'curLength': BLUE_D,
            'elemType': TEAL_D,
            'clear': YELLOW_B,
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
        },
        'font': 'Consolas',
        'size': 0.7,
        'color': DARK_GRAY,
        'plot_depth': 2,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class CodeLine_remove(Text):

    CONFIG = {
        't2c': {
            # 'x': average_color(BLUE, PINK),
            # 'y': average_color(BLUE, PINK),
            # 'z': average_color(BLUE, PINK),
            'linkList': TEAL_D,
            'Node': TEAL_D,
            'head': BLUE_D,
            'while': PINK,
            'NULL': DARK_BLUE,
            'template': DARK_BLUE,
            'void': DARK_BLUE,
            'class': DARK_BLUE,
            'tmp': BLUE_D,
            'p': BLUE_D,
            'q': BLUE_D,
            'next': BLUE_D,
            'delete': PINK,
            'tail': BLUE_D,
            'curLength': BLUE_D,
            'elemType': TEAL_D,
            'clear': YELLOW_B,
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
        },
        'font': 'Consolas',
        'size': 0.5,  # 0.7
        'color': DARK_GRAY,
        'plot_depth': 2,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


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


class CodeLine_seq_traverse(Text):

    CONFIG = {
        't2c': {
            # 'x': average_color(BLUE, PINK),
            # 'y': average_color(BLUE, PINK),
            # 'z': average_color(BLUE, PINK),
            'linkList': TEAL_D,
            'Node': TEAL_D,
            'head': BLUE_D,
            'while': PINK,
            'NULL': DARK_BLUE,
            'template': DARK_BLUE,
            'void': DARK_BLUE,
            'class': DARK_BLUE,
            'tmp': BLUE_D,
            'p': BLUE_D,
            'q': BLUE_D,
            'next': BLUE_D,
            'delete': PINK,
            'tail': BLUE_D,
            'curLength': BLUE_D,
            'elemType': TEAL_D,
            'clear': YELLOW_B,
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
        },
        'font': 'Consolas',
        'size': 0.6,  # 0.7
        'color': DARK_GRAY,
        'plot_depth': 2,
    }

    def __init__(self, text, **kwargs):
        Text.__init__(self, text, **kwargs)


class Scene_(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "use_plot_depth": True,
        }
    }


class OpeningScene(Scene_):
    def construct(self):
        line_begin = Line(np.array([0, 2, 0]),
                          np.array([0, -2, 0]),
                          fill_color=BLACK,
                          stroke_color=BLACK,)
        line1 = Line(np.array([0, 2, 0]),
                     np.array([0, 0, 0]),
                     fill_color=BLACK,
                     stroke_color=BLACK,)
        line2 = Line(np.array([0, 0, 0]),
                     np.array([0, -2, 0]),
                     fill_color=BLACK,
                     stroke_color=BLACK,)
        school = TextMobject("\\large 网络工程", buff=2)
        profession = TextMobject("\\large 李蓝骏", buff=2)
        school.set_color(BLACK)
        profession.set_color(BLACK)
        school.next_to(line_begin, LEFT, buff=0.5)
        school.shift(UP*1)
        profession.next_to(line_begin, RIGHT, buff=0.5)
        profession.shift(DOWN*1)
        self.play(GrowFromCenter(line_begin))
        self.add(line1, line2)
        self.wait(0.5)
        self.play(ReplacementTransform(line1, school),
                  ReplacementTransform(line2, profession))
        # self.play(FadeInFrom(school, direction=LEFT),
        #           FadeInFrom(profession, direction=RIGHT))


class DepartmentDetails_link_clear(Scene_):

    def construct(self):
        # List
        rectangle_front = Rectangle(height=0.5, width=0.5,
                                    opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_later = rectangle_front.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        group_rectangle_0 = VGroup(rectangle_front, rectangle_later)
        group_rectangle_1 = group_rectangle_0.copy()
        group_rectangle_2 = group_rectangle_0.copy()
        group_rectangle_3 = group_rectangle_0.copy()
        group_rectangle_1.next_to(group_rectangle_0, RIGHT, buff=0.65)
        group_rectangle_2.next_to(group_rectangle_1, RIGHT, buff=0.65)
        group_rectangle_3.next_to(group_rectangle_2, RIGHT, buff=0.65)
        group_rectangle = VGroup(
            group_rectangle_0, group_rectangle_1, group_rectangle_2, group_rectangle_3)

        # number
        number_0 = TextMobject("0", color=BLACK)
        number_1 = TextMobject("1", color=BLACK)
        number_2 = TextMobject("2", color=BLACK)
        number_3 = TextMobject("3", color=BLACK)
        number_0.scale(0.7)
        number_1.scale(0.7)
        number_2.scale(0.7)
        number_3.scale(0.7)
        number_0.next_to(group_rectangle_0, LEFT)
        number_0.shift(RIGHT*0.58)
        number_1.next_to(group_rectangle_1, LEFT)
        number_1.shift(RIGHT*0.58)
        number_2.next_to(group_rectangle_2, LEFT)
        number_2.shift(RIGHT*0.58)
        number_3.next_to(group_rectangle_3, LEFT)
        number_3.shift(RIGHT*0.58)
        number = VGroup(number_0, number_1, number_2, number_3)

        # arrow_head
        vec_head = Arrow(np.array([0, 1, 0]), np.array(
            [0, -1, 0]), buff=0.6, color=BLACK)
        vec_head.scale(0.5)
        vec_head.next_to(group_rectangle_0, UP, buff=0.1)
        vec_head.shift(LEFT*0.25)

        # arrow_tail
        vec_tail = vec_head.copy()
        vec_tail.next_to(group_rectangle_3, UP, buff=0.1)
        vec_tail.shift(LEFT*0.25)

        # arrow_list
        vec_list_0 = Arrow(buff=0.5, color=BLACK)
        vec_list_0.scale(0.75)
        vec_list_1 = vec_list_0.copy()
        vec_list_2 = vec_list_0.copy()
        vec_list_3 = vec_list_0.copy()
        vec_list_0.next_to(group_rectangle_0, RIGHT, buff=0.1)
        vec_list_1.next_to(group_rectangle_1, RIGHT, buff=0.1)
        vec_list_2.next_to(group_rectangle_2, RIGHT, buff=0.1)
        vec_list_3.next_to(group_rectangle_3, RIGHT, buff=0.1)
        vec_list_0.shift(LEFT*0.3)
        vec_list_1.shift(LEFT*0.3)
        vec_list_2.shift(LEFT*0.3)
        vec_list_3.shift(LEFT*0.3)
        vec_list = VGroup(vec_list_0, vec_list_1, vec_list_2, vec_list_3)

        # arrow_rotate
        vec_rotate = vec_head.copy()
        vec_head_cp = vec_head.copy()
        vec_rotate.rotate(angle=PI/6, about_point=number_0.get_center())

        # arrow_tmp
        vec_tmp = vec_head.copy()
        vec_head_cp_2 = vec_head.copy()
        vec_head_cp_2.rotate(angle=PI, about_point=number_0.get_center())
        vec_tmp.rotate(angle=5*PI/6, about_point=number_0.get_center())

        # text
        text_1 = TextMobject("head", color=BLACK)
        text_1.next_to(vec_head, UP, buff=0.05)
        text_1.scale(0.7)
        text_2 = TextMobject("tail", color=BLACK)
        text_2.next_to(vec_tail, UP, buff=0.05)
        text_2.scale(0.7)
        text_3 = TextMobject("NULL", color=BLACK)
        text_3.next_to(vec_list_3, RIGHT, buff=0)
        text_3.scale(0.7)
        text = VGroup(text_1, text_2, text_3)
        text_1_cp = text_1.copy()
        text_4 = TextMobject("P", color=BLACK)
        text_4.next_to(text_1, LEFT, buff=0.1)
        text_4.scale(0.7)
        text_5 = TextMobject("tmp", color=BLACK)
        text_5.scale(0.7)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params = VGroup(curLength, curLength_value)
        params.next_to(group_rectangle_0, LEFT, buff=0.7)

        # All
        All = VGroup(group_rectangle, vec_head, vec_tail,
                     vec_list, text, number, params, text_1_cp, text_4, vec_rotate, vec_head_cp, vec_tmp, vec_head_cp_2)
        All.shift(LEFT*2.5+DOWN*2)

        # Code block
        tex_bg_1 = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                    fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg_1.set_height(3.5, stretch=True).set_width(6, stretch=True)
        tex_bg_2 = tex_bg_1.copy()
        tex_bg_1.to_corner(UP*1.5+LEFT*2.15)
        tex_bg_2.to_corner(UP*1.5+RIGHT*2.15)
        method = CodeLine("clear()",
                          size=0.8).to_corner(UP, buff=0.18)
        codes_1 = [
            "Node *p = head->next;",
            "while (p != NULL)",
            "{",
            "    Node *tmp = p;",
            "    p = p->next;",
            "    delete tmp;",
        ]
        codes_2 = [
            "}",
            "head->next = NULL;",
            "tail = head;",
            "curLength = 0;",
        ]
        codes_mob_1 = VGroup(
            *[
                CodeLine(code) for code in codes_1
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_1.next_to(tex_bg_1.get_top(), DOWN, buff=0.2).shift(LEFT*0.8)
        codes_mob_2 = VGroup(
            *[
                CodeLine(code) for code in codes_2
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_2.next_to(tex_bg_2.get_top(), DOWN, buff=0.2).shift(LEFT)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # join
        self.add(tex_bg_1, tex_bg_2)
        self.add(method, codes_mob_1, codes_mob_2)
        self.add(group_rectangle)
        self.add(vec_head)
        self.add(vec_tail)
        self.add(vec_list)
        self.add(text)
        self.add(number)
        self.add(params)
        self.add(text_1_cp)
        self.wait()

        # show 1
        foot_line.set_length(4.1)
        foot_line.next_to(codes_mob_1[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(Transform(text_1_cp, text_4),
                  Transform(vec_head_cp, vec_rotate))
        self.wait()
        self.play(Rotate(vec_head_cp, angle=PI-PI/6,
                         about_point=number_0.get_center()), FadeOut(text_1_cp))
        text_4.next_to(vec_head_cp, DOWN, buff=0.05)
        self.wait(0.1)
        self.play(FadeIn(text_4))
        text_4.cp = text_4.copy()   # show 2.1 要用
        self.wait()

        # show 2.1
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.3)
        foot_line.next_to(codes_mob_1[1], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.8)
        foot_line.next_to(codes_mob_1[3], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.4)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        text_5.next_to(text_4, LEFT, buff=0.1)
        text_4_cp = text_4.copy()
        self.play(Transform(text_4_cp, text_5),
                  Transform(vec_head_cp_2, vec_tmp))
        vec_list_0_cp = vec_list_0.copy()
        vec_list_0_cp.set_color(BLUE)  # 注意箭头变蓝
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait(0.5)
        self.play(ShowCreation(vec_list_0_cp), run_time=1.5)
        move_pointer = VGroup(text_4, vec_head_cp)
        self.play(ApplyMethod(move_pointer.next_to, number_1, DOWN, buff=0.05), ApplyMethod(
            text_4_cp.move_to, text_4.cp), ApplyMethod(vec_head_cp_2.rotate, {"angle": PI/6, "about_point": number_0.get_center()}))
        self.wait()

        # show 2.2
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.2)
        foot_line.next_to(codes_mob_1[5], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(group_rectangle_0), FadeOut(number_0), FadeOut(vec_list_0), FadeOut(
            vec_list_0_cp), FadeOut(text_4_cp), FadeOut(vec_head_cp_2), FadeOut(vec_head))
        self.wait()
        All_2 = VGroup(group_rectangle_1, group_rectangle_2, group_rectangle_3, vec_tail, text_2, text_3,
                       vec_list_1, vec_list_2, vec_list_3, number_1, number_2, number_3, move_pointer)
        self.play(All_2.shift, LEFT)
        self.wait()
        vec_tmp_2 = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_tmp_2.scale(0.5)
        vec_tmp_2.next_to(group_rectangle_1, DOWN, buff=0.1)
        vec_tmp_2.shift(LEFT*0.25)
        vec_tmp_2.rotate(angle=PI/6, axis=IN,
                         about_point=number_1.get_center())
        vec_head_cp_tmp = vec_head_cp.copy()
        text_5.next_to(text_4, LEFT, buff=0.1)
        text_4_cp_2 = text_4.copy()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.8)
        foot_line.next_to(codes_mob_1[3], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.4)
        self.play(GrowFromCenter(foot_line))
        self.play()
        self.play(Transform(text_4_cp_2, text_5),
                  Transform(vec_head_cp_tmp, vec_tmp_2))
        self.wait()
        vec_list_1_cp = vec_list_1.copy()
        vec_list_1_cp.set_color(BLUE)
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait(0.5)
        self.play(ShowCreation(vec_list_1_cp), run_time=1.5)
        self.play(ApplyMethod(move_pointer.next_to, number_2, DOWN, buff=0.05), ApplyMethod(
            text_4_cp_2.move_to, text_4), ApplyMethod(vec_head_cp_tmp.rotate, {"angle": PI/6, "about_point": number_1.get_center()}))
        self.wait()

        # show 2.3
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.2)
        foot_line.next_to(codes_mob_1[5], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(group_rectangle_1), FadeOut(number_1), FadeOut(vec_list_1), FadeOut(
            vec_list_1_cp), FadeOut(text_4_cp_2), FadeOut(vec_head_cp_tmp))
        self.wait()
        All_3 = VGroup(group_rectangle_2, group_rectangle_3, vec_tail, text_2, text_3,
                       vec_list_2, vec_list_3,  number_2, number_3, move_pointer)
        self.play(All_3.shift, LEFT)
        self.wait()
        vec_tmp_3 = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_tmp_3.scale(0.5)
        vec_tmp_3.next_to(group_rectangle_2, DOWN, buff=0.1)
        vec_tmp_3.shift(LEFT*0.25)
        vec_tmp_3.rotate(angle=PI/6, axis=IN,
                         about_point=number_2.get_center())
        vec_head_cp_tmp_2 = vec_head_cp.copy()
        text_5.next_to(text_4, LEFT, buff=0.1)
        text_4_cp_3 = text_4.copy()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.8)
        foot_line.next_to(codes_mob_1[3], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.4)
        self.play(GrowFromCenter(foot_line))
        self.play()
        self.play(Transform(text_4_cp_3, text_5),
                  Transform(vec_head_cp_tmp_2, vec_tmp_3))
        vec_list_2_cp = vec_list_2.copy()
        vec_list_2_cp.set_color(BLUE)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait(0.5)
        self.play(ShowCreation(vec_list_2_cp), run_time=1.5)
        self.play(ApplyMethod(move_pointer.next_to, number_3, DOWN, buff=0.05), ApplyMethod(
            text_4_cp_3.move_to, text_4), ApplyMethod(vec_head_cp_tmp_2.rotate, {"angle": PI/6, "about_point": number_2.get_center()}))
        self.wait()

        # show 2.3
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.2)
        foot_line.next_to(codes_mob_1[5], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(group_rectangle_2), FadeOut(number_2), FadeOut(vec_list_2), FadeOut(
            vec_list_2_cp), FadeOut(text_4_cp_3), FadeOut(vec_head_cp_tmp_2))
        self.wait()
        All_4 = VGroup(group_rectangle_3, vec_tail, text_2,
                       text_3, vec_list_3, number_3, move_pointer)
        self.play(All_4.shift, LEFT)
        self.wait()
        vec_tmp_4 = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_tmp_4.scale(0.5)
        vec_tmp_4.next_to(group_rectangle_3, DOWN, buff=0.1)
        vec_tmp_4.shift(LEFT*0.25)
        vec_tmp_4.rotate(angle=PI/6, axis=IN,
                         about_point=number_3.get_center())
        vec_head_cp_tmp_3 = vec_head_cp.copy()
        text_5.next_to(text_4, LEFT, buff=0.1)
        text_4_cp_4 = text_4.copy()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.8)
        foot_line.next_to(codes_mob_1[3], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.4)
        self.play(GrowFromCenter(foot_line))
        self.play()
        self.play(Transform(text_4_cp_4, text_5),
                  Transform(vec_head_cp_tmp_3, vec_tmp_4))
        vec_list_3_cp = vec_list_3.copy()
        vec_list_3_cp.set_color(BLUE)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait(0.5)
        self.play(ShowCreation(vec_list_3_cp), run_time=1.5)
        self.play(ApplyMethod(move_pointer.next_to, text_3, DOWN, buff=0.05), ApplyMethod(
            text_4_cp_4.move_to, text_4), ApplyMethod(vec_head_cp_tmp_3.rotate, {"angle": PI/6, "about_point": number_3.get_center()}))
        self.wait()

        # show 2.3
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.2)
        foot_line.next_to(codes_mob_1[5], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        number_3_position = number_3
        self.play(FadeOut(group_rectangle_3), FadeOut(number_3), FadeOut(vec_tail),
                  FadeOut(text_4_cp_4), FadeOut(vec_head_cp_tmp_3))
        self.wait()
        vec_last = vec_list_3.copy()
        vec_last.set_color(RED)
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.5)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(text_1.move_to, number_3_position, FadeOut(text_4), FadeOut(vec_head_cp),
                  ShowCreation(vec_last), run_time=1.5)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.3)
        foot_line.next_to(codes_mob_2[2], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_tail_head = Arrow(np.array([0, 1, 0]), np.array(
            [0, -1, 0]), buff=0.6, color=RED)
        vec_tail_head.scale(0.7)
        vec_tail_head.next_to(text_2, DOWN, buff=0.1)
        self.play(ShowCreation(vec_tail_head))
        self.wait()
        self.wait()
        curLength_value_cp = TextMobject("0", color=RED)
        curLength_value_cp.next_to(curLength, RIGHT)
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.7)
        foot_line.next_to(codes_mob_2[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(Transform(curLength_value, curLength_value_cp))
        self.wait()


class DepartmentDetails_link_traverse(Scene_):

    def construct(self):
        # List
        rectangle_front = Rectangle(height=0.5, width=0.5,
                                    opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_later = rectangle_front.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        rectangle_front_filling = rectangle_front.copy()
        rectangle_front_filling.set_opacity(0.5).set_color(
            BLUE).set_height(0.45).set_width(0.45)
        group_rectangle_0 = VGroup(rectangle_front, rectangle_later)
        group_rectangle_1 = group_rectangle_0.copy()
        group_rectangle_2 = group_rectangle_0.copy()
        group_rectangle_3 = group_rectangle_0.copy()
        group_rectangle_1.next_to(group_rectangle_0, RIGHT, buff=0.65)
        group_rectangle_2.next_to(group_rectangle_1, RIGHT, buff=0.65)
        group_rectangle_3.next_to(group_rectangle_2, RIGHT, buff=0.65)
        group_rectangle = VGroup(
            group_rectangle_0, group_rectangle_1, group_rectangle_2, group_rectangle_3)

        # number
        number_0 = TextMobject("0", color=BLACK)
        number_1 = TextMobject("1", color=BLACK)
        number_2 = TextMobject("2", color=BLACK)
        number_3 = TextMobject("3", color=BLACK)
        number_0.scale(0.7)
        number_1.scale(0.7)
        number_2.scale(0.7)
        number_3.scale(0.7)
        number_0.next_to(group_rectangle_0, LEFT)
        number_0.shift(RIGHT*0.58)
        number_1.next_to(group_rectangle_1, LEFT)
        number_1.shift(RIGHT*0.58)
        number_2.next_to(group_rectangle_2, LEFT)
        number_2.shift(RIGHT*0.58)
        number_3.next_to(group_rectangle_3, LEFT)
        number_3.shift(RIGHT*0.58)
        number = VGroup(number_0, number_1, number_2, number_3)

        # arrow_head
        vec_head = Arrow(np.array([0, 1, 0]), np.array(
            [0, -1, 0]), buff=0.6, color=BLACK)
        vec_head.scale(0.5)
        vec_head.next_to(group_rectangle_0, UP, buff=0.1)
        vec_head.shift(LEFT*0.25)

        # arrow_tmp
        vec_tmp = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_tmp.scale(0.5)
        vec_tmp.next_to(group_rectangle_0, DOWN, buff=0.1)
        vec_tmp.shift(LEFT*0.25)

        # arrow_tail
        vec_tail = vec_head.copy()
        vec_tail.next_to(group_rectangle_3, UP, buff=0.1)
        vec_tail.shift(LEFT*0.25)

        # arrow_list
        vec_list_0 = Arrow(buff=0.5, color=BLACK)
        vec_list_0.scale(0.75)
        vec_list_1 = vec_list_0.copy()
        vec_list_2 = vec_list_0.copy()
        vec_list_3 = vec_list_0.copy()
        vec_list_0.next_to(group_rectangle_0, RIGHT, buff=0.1)
        vec_list_1.next_to(group_rectangle_1, RIGHT, buff=0.1)
        vec_list_2.next_to(group_rectangle_2, RIGHT, buff=0.1)
        vec_list_3.next_to(group_rectangle_3, RIGHT, buff=0.1)
        vec_list_0.shift(LEFT*0.3)
        vec_list_1.shift(LEFT*0.3)
        vec_list_2.shift(LEFT*0.3)
        vec_list_3.shift(LEFT*0.3)
        vec_list = VGroup(vec_list_0, vec_list_1, vec_list_2, vec_list_3)

        # text
        text_1 = TextMobject("head", color=BLACK)
        text_1.next_to(vec_head, UP, buff=0.05)
        text_1.scale(0.7)
        text_2 = TextMobject("tail", color=BLACK)
        text_2.next_to(vec_tail, UP, buff=0.05)
        text_2.scale(0.7)
        text_3 = TextMobject("NULL", color=BLACK)
        text_3.next_to(vec_list_3, RIGHT, buff=0)
        text_3.scale(0.7)
        text = VGroup(text_1, text_2, text_3)
        text_4 = TextMobject("P", color=BLACK)
        text_4.next_to(vec_tmp, DOWN, buff=0.05)
        text_4.scale(0.7)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params = VGroup(curLength, curLength_value)
        params.next_to(group_rectangle_0, LEFT, buff=0.7)

        # All
        All = VGroup(group_rectangle, vec_head, vec_tail, rectangle_front_filling, vec_tmp, text_4,
                     vec_list, text, number, params)
        All.shift(LEFT*2.5+DOWN*2)

        # Code block
        tex_bg_1 = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                    fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg_1.set_height(3.5, stretch=True).set_width(6.5, stretch=True)
        tex_bg_2 = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                    fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg_2.set_height(3.5, stretch=True).set_width(5.5, stretch=True)
        tex_bg_1.to_corner(UP*1.5+LEFT*2.15)
        tex_bg_2.to_corner(UP*1.5+RIGHT*2.15)
        method = CodeLine("traverse()",
                          size=0.8).to_corner(UP, buff=0.18)
        codes_1 = [
            "Node *p = head->next;",
            "if (p == NULL)",
            "    cout << \"link list is empty\";",
            "else cout << \"result:\";",
            "while (p != NULL)",
            "{",
        ]
        codes_2 = [
            "    cout << p->data << ' ';",
            "    p = p->next;",
            "}",
            "cout << endl;",
        ]
        codes_mob_1 = VGroup(
            *[
                CodeLine(code) for code in codes_1
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_1.next_to(tex_bg_1.get_top(), DOWN, buff=0.2)  # .shift(LEFT)
        codes_mob_2 = VGroup(
            *[
                CodeLine(code) for code in codes_2
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_2.next_to(tex_bg_2.get_top(), DOWN, buff=0.2)  # .shift(LEFT)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # Code text
        code_text = CodeLine(
            "head->next", size=0.7).next_to(tex_bg_1.get_top(), DOWN, buff=0.2).shift(LEFT*0.26)
        code_text2 = CodeLine(
            "result:", size=0.7).next_to(tex_bg_1.get_top(), DOWN*9.5, buff=0.2).shift(LEFT*0.77)

        # join
        self.add(tex_bg_1, tex_bg_2)
        self.add(method, codes_mob_1, codes_mob_2)
        self.add(group_rectangle)
        self.add(vec_head)
        self.add(vec_tail)
        self.add(vec_list)
        self.add(text)
        self.add(number)
        self.add(params)
        self.wait()

        # show 1
        foot_line_front = Line(opacity=1, stroke_color=PURPLE_E)
        foot_line_front.put_start_and_end_on(codes_mob_1[0].get_center(
        )+RIGHT*1.9+DOWN*0.25, codes_mob_1[0].get_center()+LEFT*0.1+DOWN*0.25)
        self.play(ShowCreation(foot_line_front))
        self.wait(0.5)
        # foot_line.set_length(3)
        # foot_line.next_to(codes_mob_1[0], DOWN, buff=0.1)
        # self.play(GrowFromCenter(foot_line))
        vec_head_cp = vec_head.copy()
        vec_head_cp.set_color(BLUE)
        self.play(ShowCreation(vec_head_cp), run_time=1.5)
        self.wait()
        self.play(Transform(code_text, rectangle_front_filling), run_time=1.5)
        self.wait()
        foot_line_second = foot_line_front.copy()
        foot_line_second.put_start_and_end_on(codes_mob_1[0].get_center(
        )+LEFT*0.1+DOWN*0.25, codes_mob_1[0].get_center()+LEFT*2+DOWN*0.25)
        self.play(ShowCreation(foot_line_second), run_time=1)
        self.wait()
        # self.play(FadeOut(foot_line))
        # foot_line.set_length(3)
        # foot_line.next_to(codes_mob_1[0], DOWN, buff=0.1)
        # foot_line.shift(RIGHT*0.35)
        # self.play(GrowFromCenter(foot_line))
        move_tmp = VGroup(vec_tmp, text_4)
        self.play(Transform(code_text, move_tmp), run_time=1.5)

        # show 2
        self.play(FadeOut(foot_line_front), FadeOut(foot_line_second))
        foot_line.set_length(2.8)
        foot_line.next_to(codes_mob_1[1], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.5)
        foot_line.next_to(codes_mob_1[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        result = TextMobject("result: ", color=BLACK)
        result.next_to(curLength, DOWN, buff=0.05).shift(UP*0.35)
        result.shift(LEFT)
        result.scale(0.7)
        self.play(Transform(code_text2, result),
                  ApplyMethod(params.shift, UP*0.5), run_time=1.5)
        self.wait()

        # show 3
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.3)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_tmp_cp = vec_tmp.copy()
        vec_tmp_cp.set_color(BLUE)
        self.play(ShowCreation(vec_tmp_cp), run_time=1.5)
        self.wait()
        result_0 = number_0.copy()
        result_0.next_to(result, RIGHT, buff=0.25)
        number_0_cp = number_0.copy()
        self.play(Transform(number_0_cp, result_0), run_time=1.5)
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.4)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_list_0_cp = vec_list_0.copy()
        vec_list_0_cp.set_color(BLUE)
        self.play(FadeOut(vec_tmp_cp), ShowCreation(
            vec_list_0_cp), run_time=1.5)
        self.wait()
        self.play(ApplyMethod(code_text.shift, RIGHT*1.65), run_time=1.5)

        # show 4
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.3)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_tmp_cp_2 = vec_tmp.copy()
        vec_tmp_cp_2.set_color(BLUE)
        vec_tmp_cp_2.shift(RIGHT*1.65)
        self.play(ShowCreation(vec_tmp_cp_2), run_time=1.5)
        self.wait()
        result_1 = number_1.copy()
        result_1.next_to(result_0, RIGHT, buff=0.3)
        number_1_cp = number_1.copy()
        self.play(Transform(number_1_cp, result_1), run_time=1.5)
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.4)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_list_1_cp = vec_list_1.copy()
        vec_list_1_cp.set_color(BLUE)
        self.play(FadeOut(vec_tmp_cp_2), ShowCreation(
            vec_list_1_cp), run_time=1.5)
        self.wait()
        self.play(ApplyMethod(code_text.shift, RIGHT*1.65), run_time=1.5)

        # show 5
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.3)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_tmp_cp_3 = vec_tmp.copy()
        vec_tmp_cp_3.set_color(BLUE)
        vec_tmp_cp_3.shift(RIGHT*3.3)
        self.play(ShowCreation(vec_tmp_cp_3), run_time=1.5)
        self.wait()
        result_2 = number_2.copy()
        result_2.next_to(result_1, RIGHT, buff=0.3)
        number_2_cp = number_2.copy()
        self.play(Transform(number_2_cp, result_2), run_time=1.5)
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.4)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_list_2_cp = vec_list_2.copy()
        vec_list_2_cp.set_color(BLUE)
        self.play(FadeOut(vec_tmp_cp_3), ShowCreation(
            vec_list_2_cp), run_time=1.5)
        self.wait()
        self.play(ApplyMethod(code_text.shift, RIGHT*1.65), run_time=1.5)

        # show 6
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.3)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_tmp_cp_4 = vec_tmp.copy()
        vec_tmp_cp_4.set_color(BLUE)
        vec_tmp_cp_4.shift(RIGHT*4.95)
        self.play(ShowCreation(vec_tmp_cp_4), run_time=1.5)
        self.wait()
        result_3 = number_3.copy()
        result_3.next_to(result_2, RIGHT, buff=0.3)
        number_3_cp = number_3.copy()
        self.play(Transform(number_3_cp, result_3), run_time=1.5)
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.4)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_list_3_cp = vec_list_3.copy()
        vec_list_3_cp.set_color(BLUE)
        self.play(FadeOut(vec_tmp_cp_4), ShowCreation(
            vec_list_3_cp), run_time=1.5)
        self.wait()
        self.play(ApplyMethod(code_text.shift, RIGHT*2), run_time=1.5)

        # show 7
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.3)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.5)
        foot_line.next_to(codes_mob_2[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()


class DepartmentDetails_link_getposition(Scene_):

    def construct(self):
        # List
        rectangle_front = Rectangle(height=0.5, width=0.5,
                                    opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_later = rectangle_front.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        group_rectangle_0 = VGroup(rectangle_front, rectangle_later)
        group_rectangle_1 = group_rectangle_0.copy()
        group_rectangle_2 = group_rectangle_0.copy()
        group_rectangle_3 = group_rectangle_0.copy()
        group_rectangle_1.next_to(group_rectangle_0, RIGHT, buff=0.65)
        group_rectangle_2.next_to(group_rectangle_1, RIGHT, buff=0.65)
        group_rectangle_3.next_to(group_rectangle_2, RIGHT, buff=0.65)
        group_rectangle = VGroup(
            group_rectangle_0, group_rectangle_1, group_rectangle_2, group_rectangle_3)

        # number
        number_0 = TextMobject("1", color=BLACK)
        number_1 = TextMobject("2", color=BLACK)
        number_2 = TextMobject("3", color=BLACK)
        number_3 = TextMobject("4", color=BLACK)
        number_0.scale(0.7)
        number_1.scale(0.7)
        number_2.scale(0.7)
        number_3.scale(0.7)
        number_0.next_to(group_rectangle_0, LEFT)
        number_0.shift(RIGHT*0.58)
        number_1.next_to(group_rectangle_1, LEFT)
        number_1.shift(RIGHT*0.58)
        number_2.next_to(group_rectangle_2, LEFT)
        number_2.shift(RIGHT*0.58)
        number_3.next_to(group_rectangle_3, LEFT)
        number_3.shift(RIGHT*0.58)
        number = VGroup(number_0, number_1, number_2, number_3)

        # arrow_head
        vec_head = Arrow(np.array([0, 1, 0]), np.array(
            [0, -1, 0]), buff=0.6, color=BLACK)
        vec_head.scale(0.5)
        vec_head.next_to(group_rectangle_0, UP, buff=0.1)
        vec_head.shift(LEFT*0.25)

        # arrow_tail
        vec_tail = vec_head.copy()
        vec_tail.next_to(group_rectangle_3, UP, buff=0.1)
        vec_tail.shift(LEFT*0.25)

        # arrow_list
        vec_list_0 = Arrow(buff=0.5, color=BLACK)
        vec_list_0.scale(0.75)
        vec_list_1 = vec_list_0.copy()
        vec_list_2 = vec_list_0.copy()
        vec_list_3 = vec_list_0.copy()
        vec_list_0.next_to(group_rectangle_0, RIGHT, buff=0.1)
        vec_list_1.next_to(group_rectangle_1, RIGHT, buff=0.1)
        vec_list_2.next_to(group_rectangle_2, RIGHT, buff=0.1)
        vec_list_3.next_to(group_rectangle_3, RIGHT, buff=0.1)
        vec_list_0.shift(LEFT*0.3)
        vec_list_1.shift(LEFT*0.3)
        vec_list_2.shift(LEFT*0.3)
        vec_list_3.shift(LEFT*0.3)
        vec_list = VGroup(vec_list_0, vec_list_1, vec_list_2, vec_list_3)

        # text
        text_1 = TextMobject("head", color=BLACK)
        text_1.next_to(vec_head, UP, buff=0.05)
        text_1.scale(0.7)
        text_2 = TextMobject("tail", color=BLACK)
        text_2.next_to(vec_tail, UP, buff=0.05)
        text_2.scale(0.7)
        text_3 = TextMobject("NULL", color=BLACK)
        text_3.next_to(vec_list_3, RIGHT, buff=0)
        text_3.scale(0.7)
        text = VGroup(text_1, text_2, text_3)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params = VGroup(curLength, curLength_value)
        params.next_to(group_rectangle_0, LEFT, buff=0.7)

        # All
        All = VGroup(group_rectangle, vec_head, vec_tail,
                     vec_list, text, number, params)
        All.shift(LEFT*2.5+DOWN*2)

        # Code block
        tex_bg_1 = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                    fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg_1.set_height(3.5, stretch=True).set_width(6, stretch=True)
        tex_bg_2 = tex_bg_1.copy()
        tex_bg_1.to_corner(UP*1.5+LEFT*2.15)
        tex_bg_2.to_corner(UP*1.5+RIGHT*2.15)
        method = CodeLine("getPosition(int i)",
                          size=0.8).to_corner(UP, buff=0.18)
        codes_1 = [
            "Node *p = head;",
            "if (i < 0 || i > curLength)",
            "    return NULL;",
            "int count = 0;",
            "while (count < i)",
            "{",
        ]
        codes_2 = [
            "    p = p->next;",
            "    ++count;",
            "}",
            "return p;",
        ]
        codes_mob_1 = VGroup(
            *[
                CodeLine(code) for code in codes_1
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_1.next_to(tex_bg_1.get_top(), DOWN, buff=0.2).shift(LEFT*0.2)
        codes_mob_2 = VGroup(
            *[
                CodeLine(code) for code in codes_2
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_2.next_to(tex_bg_2.get_top(), DOWN, buff=0.2).shift(LEFT*1.2)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # Code text
        code_text = CodeLine(
            "head", size=0.7).next_to(tex_bg_1.get_top(), DOWN, buff=0.2).shift(LEFT*0.48)

        # join
        self.add(tex_bg_1, tex_bg_2)
        self.add(method, codes_mob_1, codes_mob_2)
        self.add(group_rectangle)
        self.add(vec_head)
        self.add(vec_tail)
        self.add(vec_list)
        self.add(text)
        self.add(number)
        self.add(params)
        self.wait()

        # show 1
        self.wait()
        method_trans = CodeLine("getPosition(2)",
                                size=0.8).to_corner(UP, buff=0.18)
        self.play(Transform(method, method_trans))
        foot_line_front = Line(opacity=1, stroke_color=PURPLE_E)
        foot_line_front.put_start_and_end_on(codes_mob_1[0].get_center(
        )+RIGHT*1.3+DOWN*0.25, codes_mob_1[0].get_center()+RIGHT*0.5+DOWN*0.25)
        self.play(ShowCreation(foot_line_front))
        self.wait(0.5)
        # foot_line.set_length(3)
        # foot_line.next_to(codes_mob_1[0], DOWN, buff=0.1)
        # self.play(GrowFromCenter(foot_line))
        text_1_cp = text_1.copy()
        text_1_cp.set_color(BLUE)
        self.play(Transform(code_text, text_1_cp), run_time=1.5)
        self.wait()
        foot_line_second = foot_line_front.copy()
        foot_line_second.put_start_and_end_on(codes_mob_1[0].get_center(
        )+RIGHT*0.5+DOWN*0.25, codes_mob_1[0].get_center()+LEFT*1.5+DOWN*0.25)
        self.play(ShowCreation(foot_line_second), run_time=1)
        self.wait(1)
        # self.play(FadeOut(foot_line))
        # foot_line.set_length(3)
        # foot_line.next_to(codes_mob_1[0], DOWN, buff=0.1)
        # foot_line.shift(RIGHT*0.35)
        # self.play(GrowFromCenter(foot_line))
        vec_tmp = Arrow(np.array([-1, 0, 0]), np.array(
            [1, 0, 0]), buff=0.6, color=BLACK)
        vec_tmp.scale(0.5)
        vec_tmp.next_to(text_1, LEFT, buff=0.1)
        # vec_tmp.shift(LEFT*0.25)
        text_4 = TextMobject("P", color=BLACK)
        text_4.next_to(vec_tmp, LEFT, buff=0.05)
        text_4.scale(0.7)
        move_tmp = VGroup(vec_tmp, text_4)
        self.play(Transform(code_text, move_tmp), run_time=1.5)

        # show 2
        self.play(FadeOut(foot_line_front), FadeOut(foot_line_second))
        foot_line.set_length(5.3)
        foot_line.next_to(codes_mob_1[1], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans_len = CodeLine("if (i < 0 || i > 4)",
                                       size=0.7).move_to(codes_mob_1[1], aligned_edge=LEFT)
        codes_mob_tmp = codes_mob_1[1].copy()
        self.play(Transform(codes_mob_1[1], codes_mob_trans_len),
                  foot_line.set_length, 3.8, foot_line.shift, LEFT*0.75)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.8)
        foot_line.next_to(codes_mob_1[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()

        # show 3
        count = TextMobject("count = ", color=BLACK)
        count.scale(0.7)
        count.next_to(curLength, DOWN, aligned_edge=LEFT, buff=0)
        count.shift(LEFT*0.3)
        count_value = TextMobject("0", color=RED_D)
        count_value.next_to(count, RIGHT)
        count_params = VGroup(count, count_value)
        self.play(FadeInFromDown(count_params), ApplyMethod(
            params.shift, UP*0.45+LEFT*0.35), Transform(codes_mob_1[1], codes_mob_tmp))
        self.wait()

        # show 4
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans_count = CodeLine(
            "while (   0  < 2)", size=0.7).move_to(codes_mob_1[4])
        self.play(Transform(codes_mob_1[4], codes_mob_trans_count))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.5)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        codes_mob_trans_count_2 = CodeLine(
            "while (count < 2)", size=0.7).move_to(codes_mob_1[4])
        self.play(GrowFromCenter(foot_line), Transform(
            codes_mob_1[4], codes_mob_trans_count_2))
        self.wait()
        vec_head_cp = vec_head.copy()
        vec_head_cp.set_color(BLUE)
        self.play(ShowCreation(vec_head_cp), run_time=1.5)
        self.wait()
        vec_tmp_2 = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_tmp_2.scale(0.5)
        vec_tmp_2.next_to(group_rectangle_0, DOWN, buff=0.1)
        vec_tmp_2.shift(LEFT*0.25)
        text_5 = TextMobject("P", color=BLACK)
        text_5.next_to(vec_tmp_2, DOWN, buff=0.05)
        text_5.scale(0.7)
        move_tmp_2 = VGroup(vec_tmp_2, text_5)
        self.play(FadeOut(code_text), FadeIn(move_tmp_2))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.5)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        count_value_1 = TextMobject("1", color=average_color(BLUE, PINK))
        count_value_1.next_to(count, RIGHT)
        self.play(Transform(count_value, count_value_1))
        self.wait()

        # show 5
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans_count_3 = CodeLine(
            "while (   1  < 2)", size=0.7).move_to(codes_mob_1[4])
        self.play(Transform(codes_mob_1[4], codes_mob_trans_count_3))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.5)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line), Transform(
            codes_mob_1[4], codes_mob_trans_count_2))
        self.wait()
        vec_list_0_cp = vec_list_0.copy()
        vec_list_0_cp.set_color(BLUE)
        self.play(ShowCreation(vec_list_0_cp), run_time=1.5)
        self.wait()
        self.play(ApplyMethod(move_tmp_2.shift, RIGHT*1.65))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.5)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        count_value_2 = TextMobject("2", color=average_color(BLUE, PINK))
        count_value_2.next_to(count, RIGHT)
        self.play(Transform(count_value, count_value_2))
        self.wait()

        # show 6
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans_count_3 = CodeLine(
            "while (   2  < 2)", size=0.7).move_to(codes_mob_1[4])
        self.play(Transform(codes_mob_1[4], codes_mob_trans_count_3))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.9)
        foot_line.next_to(codes_mob_2[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line), Transform(
            codes_mob_1[4], codes_mob_trans_count_2))
        self.wait()


class DepartmentDetails_link_insert(Scene_):

    def construct(self):
        # List
        rectangle_front = Rectangle(height=0.5, width=0.5,
                                    opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_later = rectangle_front.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        rectangle_front_filling = rectangle_front.copy()
        rectangle_front_filling.set_opacity(0.5).set_color(
            BLUE).set_height(0.45).set_width(0.45)
        group_rectangle_0 = VGroup(rectangle_front, rectangle_later)
        group_rectangle_1 = group_rectangle_0.copy()
        group_rectangle_2 = group_rectangle_0.copy()
        group_rectangle_3 = group_rectangle_0.copy()
        group_rectangle_1.next_to(group_rectangle_0, RIGHT, buff=0.65)
        group_rectangle_2.next_to(group_rectangle_1, RIGHT, buff=0.65)
        group_rectangle_3.next_to(group_rectangle_2, RIGHT, buff=0.65)
        group_rectangle = VGroup(
            group_rectangle_0, group_rectangle_1, group_rectangle_2, group_rectangle_3)

        # number
        number_0 = TextMobject("0", color=BLACK)
        number_1 = TextMobject("1", color=BLACK)
        number_2 = TextMobject("2", color=BLACK)
        number_3 = TextMobject("3", color=BLACK)
        number_0.scale(0.7)
        number_1.scale(0.7)
        number_2.scale(0.7)
        number_3.scale(0.7)
        number_0.next_to(group_rectangle_0, LEFT)
        number_0.shift(RIGHT*0.58)
        number_1.next_to(group_rectangle_1, LEFT)
        number_1.shift(RIGHT*0.58)
        number_2.next_to(group_rectangle_2, LEFT)
        number_2.shift(RIGHT*0.58)
        number_3.next_to(group_rectangle_3, LEFT)
        number_3.shift(RIGHT*0.58)
        number = VGroup(number_0, number_1, number_2, number_3)

        # arrow_head
        vec_head = Arrow(np.array([0, 1, 0]), np.array(
            [0, -1, 0]), buff=0.6, color=BLACK)
        vec_head.scale(0.5)
        vec_head.next_to(group_rectangle_0, UP, buff=0.1)
        vec_head.shift(LEFT*0.25)

        # arrow_tail
        vec_tail = vec_head.copy()
        vec_tail.next_to(group_rectangle_3, UP, buff=0.1)
        vec_tail.shift(LEFT*0.25)

        # arrow_list
        vec_list_0 = Arrow(buff=0.5, color=BLACK)
        vec_list_0.scale(0.75)
        vec_list_1 = vec_list_0.copy()
        vec_list_2 = vec_list_0.copy()
        vec_list_3 = vec_list_0.copy()
        vec_list_0.next_to(group_rectangle_0, RIGHT, buff=0.1)
        vec_list_1.next_to(group_rectangle_1, RIGHT, buff=0.1)
        vec_list_2.next_to(group_rectangle_2, RIGHT, buff=0.1)
        vec_list_3.next_to(group_rectangle_3, RIGHT, buff=0.1)
        vec_list_0.shift(LEFT*0.3)
        vec_list_1.shift(LEFT*0.3)
        vec_list_2.shift(LEFT*0.3)
        vec_list_3.shift(LEFT*0.3)
        vec_list = VGroup(vec_list_0, vec_list_1, vec_list_2, vec_list_3)

        # text
        text_1 = TextMobject("head", color=BLACK)
        text_1.next_to(vec_head, UP, buff=0.05)
        text_1.scale(0.7)
        text_2 = TextMobject("tail", color=BLACK)
        text_2.next_to(vec_tail, UP, buff=0.05)
        text_2.scale(0.7)
        text_3 = TextMobject("NULL", color=BLACK)
        text_3.next_to(vec_list_3, RIGHT, buff=0)
        text_3.scale(0.7)
        text = VGroup(text_1, text_2, text_3)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params = VGroup(curLength, curLength_value)
        params.next_to(group_rectangle_0, LEFT, buff=0.7)

        # All
        All = VGroup(group_rectangle, vec_head, vec_tail, rectangle_front_filling,
                     vec_list, text, number, params)
        All.shift(LEFT*2.5+DOWN*2)

        # Code block
        tex_bg_1 = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                    fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg_1.set_height(3.5, stretch=True).set_width(6, stretch=True)
        tex_bg_2 = tex_bg_1.copy()
        tex_bg_1.to_corner(UP*1.5+LEFT*2.15)
        tex_bg_2.to_corner(UP*1.5+RIGHT*2.15)
        method = CodeLine("insert(int i, const elemType &value)",
                          size=0.8).to_corner(UP, buff=0.18)
        codes_1 = [
            "Node *p, *q;",
            "if (i < 0 || i > curLength)",
            "    throw outOfRange();",
            "p = getPosition(i);",
            "q = new Node(value, p->next);",
            "p->next = q;",
        ]
        codes_2 = [
            "if (p == tail)",
            "    tail = q;",
            "++curLength;",
        ]
        codes_mob_1 = VGroup(
            *[
                CodeLine(code) for code in codes_1
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_1.next_to(tex_bg_1.get_top(), DOWN,
                            buff=0.2)  # .shift(LEFT*0.2)
        codes_mob_2 = VGroup(
            *[
                CodeLine(code) for code in codes_2
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_2.next_to(tex_bg_2.get_top(), DOWN, buff=0.2).shift(LEFT*1.4)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # Code text
        code_text = CodeLine("p", size=0.7).next_to(
            tex_bg_1.get_top(), DOWN*1.3+LEFT*4.8, buff=0.2).shift(LEFT*0.48)
        code_text_2 = CodeLine("q", size=0.7).next_to(
            tex_bg_1.get_top(), DOWN*1.3+LEFT*1, buff=0.2).shift(LEFT*0.48)
        code_text_3 = CodeLine("getPosition(1)", size=0.7).next_to(
            tex_bg_1.get_top(), DOWN*9.7, buff=0.2).shift(LEFT*0.67)

        # join
        self.add(tex_bg_1, tex_bg_2)
        self.add(method, codes_mob_1, codes_mob_2)
        self.add(group_rectangle)
        self.add(vec_head)
        self.add(vec_tail)
        self.add(vec_list)
        self.add(text)
        self.add(number)
        self.add(params)
        self.wait()

        # show 1
        self.wait()
        method_trans = CodeLine(
            "insert(1,10)", size=0.8).to_corner(UP, buff=0.18)
        self.play(Transform(method, method_trans))
        self.wait()
        foot_line.set_length(2.5)
        foot_line.next_to(codes_mob_1[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        code_text_cp = code_text.copy()
        code_text_cp_tmp = code_text.copy()
        code_text_cp_tmp.next_to(curLength, UP, aligned_edge=LEFT, buff=0.6)
        code_text_cp2 = code_text_2.copy()
        code_text_cp_tmp2 = code_text_2.copy()
        code_text_cp_tmp2.next_to(code_text_cp_tmp, RIGHT, buff=0.3)
        self.play(Transform(code_text_cp, code_text_cp_tmp),
                  Transform(code_text_cp2, code_text_cp_tmp2))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(5.3)
        foot_line.next_to(codes_mob_1[1], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans = CodeLine("if (i < 0 || i > 4)", size=0.7).move_to(
            codes_mob_1[1], aligned_edge=LEFT)
        codes_mob_tmp = codes_mob_1[1].copy()
        self.play(Transform(codes_mob_1[1], codes_mob_trans),
                  foot_line.set_length, 3.8, foot_line.shift, LEFT*0.75)
        self.wait()

        # show 2
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.8)
        foot_line.next_to(codes_mob_1[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans_2 = CodeLine("p = getPosition(1);", size=0.7).move_to(
            codes_mob_1[3], aligned_edge=LEFT)
        codes_mob_tmp_2 = codes_mob_1[3].copy()
        self.play(Transform(codes_mob_1[3], codes_mob_trans_2))
        self.wait()
        self.play(Transform(code_text_3, rectangle_front_filling),
                  Transform(codes_mob_1[1], codes_mob_tmp), run_time=1.5)
        self.wait()
        vec_tmp = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_tmp.scale(0.5)
        vec_tmp.next_to(group_rectangle_0, DOWN, buff=0.1)
        vec_tmp.shift(LEFT*0.25)
        self.play(Transform(code_text_3, vec_tmp), ApplyMethod(
            code_text_cp.next_to, {"mobject_or_point": vec_tmp, "direction": DOWN, "buff": 0.1}), ApplyMethod(code_text_cp2.shift, LEFT*0.5), run_time=1.5)
        move_tmp = VGroup(code_text_3, code_text_cp)
        self.wait()

        # show 3
        self.play(FadeOut(foot_line))
        foot_line.set_length(5.7)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans_node = CodeLine("q = new Node(10, p->next);", size=0.7).move_to(
            codes_mob_1[4], aligned_edge=LEFT)
        codes_mob_tmp_3 = codes_mob_1[4].copy()
        self.play(Transform(codes_mob_1[4], codes_mob_trans_node),
                  foot_line.set_length, 5.1, foot_line.shift, LEFT*0.3)
        self.wait()
        vec_list_0_cp = vec_list_0.copy()
        vec_list_0_cp.set_color(BLUE)
        self.play(ShowCreation(vec_list_0_cp), run_time=1.5)
        self.wait()
        group_rectangle_tmp = group_rectangle_0.copy().shift(
            RIGHT*0.9+DOWN*1)
        number_node = TextMobject("10", color=BLACK)
        number_node.scale(0.7)
        number_node.next_to(group_rectangle_tmp, LEFT)
        number_node.shift(RIGHT*0.67)
        vec_list_node = Arrow(buff=0.5, color=BLACK)
        vec_list_node.scale(0.75)
        vec_list_node.next_to(group_rectangle_tmp, RIGHT,
                              buff=0.1).shift(LEFT*0.35)
        vec_list_node.rotate(
            angle=PI/2.5, about_point=group_rectangle_tmp.get_center()+RIGHT*0.3)
        insert_node = VGroup(group_rectangle_tmp, number_node, vec_list_node)
        codes_node = CodeLine("Node(10, p->next)", size=0.7).next_to(
            tex_bg_1.get_top(), DOWN*12.6, buff=0.2).shift(RIGHT*0.4)
        self.play(Transform(codes_node, insert_node),
                  Transform(codes_mob_1[3], codes_mob_tmp_2), run_time=1.5)
        self.wait()

        # show 4
        vec_insert = Arrow(np.array([-1, 0, 0]), np.array(
            [1, 0, 0]), buff=0.6, color=BLACK)
        vec_insert.scale(0.5)
        vec_insert.next_to(group_rectangle_tmp, LEFT, buff=0.1)
        self.play(FadeOut(move_tmp), FadeIn(vec_insert), ApplyMethod(code_text_cp2.next_to, {
                  "mobject_or_point": vec_insert, "direction": LEFT, "buff": 0.1}), run_time=1.5)
        insert_tmp = VGroup(vec_insert, code_text_cp2)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.4)
        foot_line.next_to(codes_mob_1[5], DOWN, buff=0.07)
        self.play(GrowFromCenter(foot_line), FadeOut(vec_list_0_cp))
        self.wait()
        self.play(Transform(codes_mob_1[4],
                            codes_mob_tmp_3), FadeOut(insert_tmp))
        self.play(FadeIn(move_tmp))
        self.wait()
        self.play(vec_list_0.rotate, {
                  "angle": 2*PI-PI/2.5, "about_point": group_rectangle_0.get_center()+RIGHT*0.3})
        self.wait()

        # show 5
        self.add(insert_node)
        self.play(FadeOut(codes_node), run_time=0.1)
        list_after = VGroup(text_3, text_2, vec_list_1, vec_list_2, vec_list_3, number_1, number_2, number_3,
                            group_rectangle_1, group_rectangle_2, group_rectangle_3, vec_tail, vec_list_3)
        self.play(ApplyMethod(list_after.shift, RIGHT*1.6), ApplyMethod(insert_node.next_to, {
                  "mobject_or_point": group_rectangle_0, "direction": RIGHT, "buff": 0.65, "aligned_edge": DOWN}), run_time=1.5)
        vec_tmp2 = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_tmp2.scale(0.5)
        vec_tmp2.next_to(group_rectangle_tmp, DOWN, buff=0.1)
        vec_tmp2.shift(LEFT*0.25)
        code_q = CodeLine("q", size=0.7).next_to(vec_tmp2, DOWN, buff=0.05)
        move_tmp2 = VGroup(code_q, vec_tmp2)
        self.play(ApplyMethod(vec_list_0.rotate, {
                  "angle": PI/2.5, "about_point": group_rectangle_0.get_center()+RIGHT*0.3}), ApplyMethod(vec_list_node.rotate, {
                      "angle": 2*PI-PI/2.5, "about_point": group_rectangle_tmp.get_center()+RIGHT*0.3}), FadeIn(move_tmp2), run_time=1.5)
        self.wait()

        # show 6
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.8)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.4)
        foot_line.next_to(codes_mob_2[2], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        curLength_value2 = TextMobject("5", color=BLUE)
        curLength_value2.next_to(curLength, RIGHT)
        self.play(Transform(curLength_value, curLength_value2))
        self.wait()

        # show 7 讲解
        method_trans_last = CodeLine(
            "insert(0,10)", size=0.8).to_corner(UP, buff=0.18)
        self.play(Transform(method, method_trans_last))
        self.wait()
        self.play(FadeOut(move_tmp), FadeOut(move_tmp2))
        self.wait(0.5)
        vec_p_head = Arrow(np.array([-1, 0, 0]), np.array(
            [1, 0, 0]), buff=0.6, color=BLACK)
        vec_p_head.scale(0.5)
        vec_p_head.next_to(text_1, LEFT, buff=0.1)
        code_p_head = CodeLine("p", size=0.7).next_to(
            vec_p_head, LEFT, buff=0.05)
        p_head = VGroup(code_p_head, vec_p_head)
        vec_q_0 = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_q_0.scale(0.5)
        vec_q_0.next_to(number_0, DOWN, buff=0.25)
        code_q_0 = CodeLine("q", size=0.7).next_to(vec_q_0, DOWN, buff=0.05)
        q_0 = VGroup(code_q_0, vec_q_0)
        number_p_head = TextMobject("10", color=BLACK)
        number_p_head.scale(0.7)
        number_p_head.next_to(group_rectangle_0, LEFT).shift(RIGHT*0.66)
        number_q_0 = TextMobject("0", color=BLACK)
        number_q_0.scale(0.7)
        number_q_0.next_to(group_rectangle_tmp, LEFT).shift(RIGHT*0.57)
        self.play(FadeIn(p_head), FadeIn(q_0), Transform(
            number_0, number_p_head), Transform(number_node, number_q_0))
        self.wait()


class DepartmentDetails_link_remove(Scene_):

    def construct(self):
        # List
        rectangle_front = Rectangle(height=0.5, width=0.5,
                                    opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_later = rectangle_front.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        rectangle_front_filling = rectangle_front.copy()
        rectangle_front_filling.set_opacity(0.5).set_color(
            BLUE).set_height(0.45).set_width(0.45)
        group_rectangle_0 = VGroup(rectangle_front, rectangle_later)
        group_rectangle_1 = group_rectangle_0.copy()
        group_rectangle_2 = group_rectangle_0.copy()
        group_rectangle_3 = group_rectangle_0.copy()
        group_rectangle_1.next_to(group_rectangle_0, RIGHT, buff=0.65)
        group_rectangle_2.next_to(group_rectangle_1, RIGHT, buff=0.65)
        group_rectangle_3.next_to(group_rectangle_2, RIGHT, buff=0.65)
        group_rectangle = VGroup(
            group_rectangle_0, group_rectangle_1, group_rectangle_2, group_rectangle_3)

        # number
        number_0 = TextMobject("0", color=BLACK)
        number_1 = TextMobject("1", color=BLACK)
        number_2 = TextMobject("2", color=BLACK)
        number_3 = TextMobject("3", color=BLACK)
        number_0.scale(0.7)
        number_1.scale(0.7)
        number_2.scale(0.7)
        number_3.scale(0.7)
        number_0.next_to(group_rectangle_0, LEFT)
        number_0.shift(RIGHT*0.58)
        number_1.next_to(group_rectangle_1, LEFT)
        number_1.shift(RIGHT*0.58)
        number_2.next_to(group_rectangle_2, LEFT)
        number_2.shift(RIGHT*0.58)
        number_3.next_to(group_rectangle_3, LEFT)
        number_3.shift(RIGHT*0.58)
        number = VGroup(number_0, number_1, number_2, number_3)

        # arrow_head
        vec_head = Arrow(np.array([0, 1, 0]), np.array(
            [0, -1, 0]), buff=0.6, color=BLACK)
        vec_head.scale(0.5)
        vec_head.next_to(group_rectangle_0, UP, buff=0.1)
        vec_head.shift(LEFT*0.25)

        # arrow_tail
        vec_tail = vec_head.copy()
        vec_tail.next_to(group_rectangle_3, UP, buff=0.1)
        vec_tail.shift(LEFT*0.25)

        # arrow_list
        vec_list_0 = Arrow(buff=0.5, color=BLACK)
        vec_list_0.scale(0.75)
        vec_list_1 = vec_list_0.copy()
        vec_list_2 = vec_list_0.copy()
        vec_list_3 = vec_list_0.copy()
        vec_list_0.next_to(group_rectangle_0, RIGHT, buff=0.1)
        vec_list_1.next_to(group_rectangle_1, RIGHT, buff=0.1)
        vec_list_2.next_to(group_rectangle_2, RIGHT, buff=0.1)
        vec_list_3.next_to(group_rectangle_3, RIGHT, buff=0.1)
        vec_list_0.shift(LEFT*0.3)
        vec_list_1.shift(LEFT*0.3)
        vec_list_2.shift(LEFT*0.3)
        vec_list_3.shift(LEFT*0.3)
        vec_list = VGroup(vec_list_0, vec_list_1, vec_list_2, vec_list_3)
        arc_tran = vec_list_0.copy()  # show 5 有用到

        # text
        text_1 = TextMobject("head", color=BLACK)
        text_1.next_to(vec_head, UP, buff=0.05)
        text_1.scale(0.7)
        text_2 = TextMobject("tail", color=BLACK)
        text_2.next_to(vec_tail, UP, buff=0.05)
        text_2.scale(0.7)
        text_3 = TextMobject("NULL", color=BLACK)
        text_3.next_to(vec_list_3, RIGHT, buff=0)
        text_3.scale(0.7)
        text = VGroup(text_1, text_2, text_3)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params = VGroup(curLength, curLength_value)
        params.next_to(group_rectangle_0, LEFT, buff=0.7)

        # All
        All = VGroup(group_rectangle, vec_head, vec_tail, rectangle_front_filling, arc_tran,
                     vec_list, text, number, params)
        All.shift(LEFT*2.5+DOWN*2)

        # Code block
        tex_bg_1 = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                    fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg_1.set_height(3.8, stretch=True).set_width(6, stretch=True)
        tex_bg_2 = tex_bg_1.copy()
        tex_bg_1.to_corner(UP*1.5+LEFT*2.15)
        tex_bg_2.to_corner(UP*1.5+RIGHT*2.15)
        method = CodeLine("remove(int i)",
                          size=0.8).to_corner(UP, buff=0.18)
        codes_1 = [
            "Node *p, *q;",
            "if (i < 0 || i > curLength - 1)",
            "    throw outOfRange();",
            "p = getPosition(i);",
            "q = p->next;",
            "if (q == tail) {",
            "    tail = p;",
            "    p->next = NULL;",
        ]
        codes_2 = [
            "    delete q;",
            "}",
            "else {",
            "    p->next = q->next;",
            "    delete q;",
            "}",
            "--curLength;",
        ]
        codes_mob_1 = VGroup(
            *[
                CodeLine_remove(code) for code in codes_1
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_1.next_to(tex_bg_1.get_top(), DOWN,
                            buff=0.2).shift(LEFT*0.6+UP*0.1)
        codes_mob_2 = VGroup(
            *[
                CodeLine_remove(code) for code in codes_2
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_2.next_to(tex_bg_2.get_top(), DOWN,
                            buff=0.2).shift(LEFT*1.3+UP*0.1)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # Code text
        code_text = CodeLine("p", size=0.5).next_to(
            tex_bg_1.get_top(), DOWN*0.7+LEFT*4.8, buff=0.2).shift(LEFT*0.8)
        code_text_2 = CodeLine("q", size=0.5).next_to(
            tex_bg_1.get_top(), DOWN*0.7+LEFT*1, buff=0.2).shift(LEFT*1.02)
        code_text_3 = CodeLine("getPosition(1)", size=0.5).next_to(
            tex_bg_1.get_top(), DOWN*7.8, buff=0.2).shift(LEFT*1.22)

        # join
        self.add(tex_bg_1, tex_bg_2)
        #self.add(code_text, code_text_2)
        self.add(method, codes_mob_1, codes_mob_2)
        self.add(group_rectangle)
        self.add(vec_head)
        self.add(vec_tail)
        self.add(vec_list)
        self.add(text)
        self.add(number)
        self.add(params)
        self.wait()

        # show 1
        self.wait()
        method_trans = CodeLine(
            "remove(1)", size=0.8).to_corner(UP, buff=0.18)
        self.play(Transform(method, method_trans))
        self.wait()
        foot_line.set_length(1.8)
        foot_line.next_to(codes_mob_1[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        code_text_cp = CodeLine("p", size=0.7)
        code_text_cp.next_to(curLength, UP, aligned_edge=LEFT, buff=0.6)
        code_text_cp2 = CodeLine("q", size=0.7)
        code_text_cp2.next_to(code_text_cp, RIGHT, buff=0.3)
        self.play(Transform(code_text, code_text_cp),
                  Transform(code_text_2, code_text_cp2))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.3)
        foot_line.next_to(codes_mob_1[1], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans = CodeLine("if (i < 0 || i > 4)", size=0.5).move_to(
            codes_mob_1[1], aligned_edge=LEFT)
        codes_mob_tmp = codes_mob_1[1].copy()
        self.play(Transform(codes_mob_1[1], codes_mob_trans),
                  foot_line.set_length, 2.65, foot_line.shift, LEFT*0.82)
        self.wait()

        # show 2
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.7)
        foot_line.next_to(codes_mob_1[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_getPosition = CodeLine("p = getPosition(1);", size=0.5).move_to(
            codes_mob_1[3], aligned_edge=LEFT)
        codes_getPosition_recover = codes_mob_1[3].copy()
        self.play(Transform(codes_mob_1[3], codes_getPosition))
        self.wait()
        self.play(Transform(code_text_3, rectangle_front_filling),
                  Transform(codes_mob_1[1], codes_mob_tmp), run_time=1.5)
        self.wait()
        vec_tmp = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_tmp.scale(0.5)
        vec_tmp.next_to(group_rectangle_0, DOWN, buff=0.1)
        vec_tmp.shift(LEFT*0.25)
        self.play(Transform(code_text_3, vec_tmp), ApplyMethod(
            code_text.next_to, {"mobject_or_point": vec_tmp, "direction": DOWN, "buff": 0.1}), ApplyMethod(code_text_2.shift, LEFT*0.5), run_time=1.5)
        move_tmp = VGroup(code_text, code_text_cp)
        self.wait()

        # show 3
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.8)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_list_0_cp = vec_list_0.copy()
        vec_list_0_cp.set_color(BLUE)
        self.play(ShowCreation(vec_list_0_cp), run_time=1.5)
        self.wait()
        vec_tmp_2 = vec_tmp.copy()
        vec_tmp_2.next_to(group_rectangle_1, DOWN, buff=0.1)
        vec_tmp_2.shift(LEFT*0.25)
        self.play(FadeIn(vec_tmp_2), ApplyMethod(code_text_2.next_to, {"mobject_or_point": vec_tmp_2, "direction": DOWN, "buff": 0.1}),
                  Transform(codes_mob_1[3], codes_getPosition_recover), run_time=1.5)
        move_tmp_2 = VGroup(vec_tmp_2, code_text_2)
        self.wait()

        # show 4
        self.play(FadeOut(foot_line))
        foot_line.set_length(2)
        foot_line.next_to(codes_mob_1[5], DOWN, buff=0.1).shift(LEFT*0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(0.6)
        foot_line.next_to(codes_mob_2[2], DOWN, buff=0.1).shift(LEFT*0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.6)
        foot_line.next_to(codes_mob_2[3], DOWN, buff=0.1).shift(RIGHT*0.25)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_list_1_cp = vec_list_1.copy()
        vec_list_1_cp.set_color(BLUE)
        self.play(ShowCreation(vec_list_1_cp), run_time=1.5)
        self.wait()
        arc_fac = ValueTracker(0.)
        arc_arrow = Arrow(group_rectangle_0.get_center(), group_rectangle_1.get_center()+RIGHT*1.3,
                          color=BLACK, max_tip_length_to_length_ratio=0.08, max_stroke_width_to_length_ratio=1.5)
        arc_fac.set_value(-2)
        # self.play(ShowCreation(arc_arrow))
        arc_arrow.add_updater(lambda l: l.become(
            Arrow(group_rectangle_0.get_center(), group_rectangle_1.get_center()+RIGHT*1.3,
                  color=BLACK, max_tip_length_to_length_ratio=0.08, max_stroke_width_to_length_ratio=1.5, path_arc=arc_fac.get_value())
        ))
        self.play(Transform(vec_list_0_cp, arc_arrow),
                  Transform(vec_list_0, arc_arrow))
        self.add(arc_arrow)
        self.play(FadeOut(vec_list_0_cp), FadeOut(
            vec_list_0), run_time=1)  # 相当于 self.wait()
        # self.play(arc_fac.set_value, 0, rate_func=linear)
        self.wait()

        # show 5
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.3)
        foot_line.next_to(codes_mob_2[4], DOWN, buff=0.1).shift(LEFT*0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        disappear = VGroup(move_tmp_2, group_rectangle_1,
                           number_1, vec_list_1, vec_list_1_cp)
        self.play(FadeOut(disappear))
        self.wait()
        self.play(arc_fac.set_value, 0, rate_func=linear)
        self.wait()
        move_other = VGroup(text_3, text_2, vec_list_2, vec_list_3, number_2, number_3,
                            group_rectangle_2, group_rectangle_3, vec_tail, vec_list_3)
        self.play(ReplacementTransform(arc_arrow, arc_tran),
                  ApplyMethod(move_other.shift, LEFT*1.65))
        self.wait()

        # show 6
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.8)
        foot_line.next_to(codes_mob_2[6], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        curLength_value2 = TextMobject("3", color=BLUE)
        curLength_value2.next_to(curLength, RIGHT)
        self.play(Transform(curLength_value, curLength_value2))
        self.wait()


class DepartmentDetails_link_search(Scene_):

    def construct(self):
        # List
        rectangle_front = Rectangle(height=0.5, width=0.5,
                                    opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_later = rectangle_front.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        rectangle_front_filling = rectangle_front.copy()
        rectangle_front_filling.set_opacity(0.5).set_color(
            BLUE).set_height(0.45).set_width(0.45)
        group_rectangle_0 = VGroup(rectangle_front, rectangle_later)
        group_rectangle_1 = group_rectangle_0.copy()
        group_rectangle_2 = group_rectangle_0.copy()
        group_rectangle_3 = group_rectangle_0.copy()
        group_rectangle_1.next_to(group_rectangle_0, RIGHT, buff=0.65)
        group_rectangle_2.next_to(group_rectangle_1, RIGHT, buff=0.65)
        group_rectangle_3.next_to(group_rectangle_2, RIGHT, buff=0.65)
        group_rectangle = VGroup(
            group_rectangle_0, group_rectangle_1, group_rectangle_2, group_rectangle_3)

        # number
        number_0 = TextMobject("0", color=BLACK)
        number_1 = TextMobject("1", color=BLACK)
        number_2 = TextMobject("2", color=BLACK)
        number_3 = TextMobject("3", color=BLACK)
        number_0.scale(0.7)
        number_1.scale(0.7)
        number_2.scale(0.7)
        number_3.scale(0.7)
        number_0.next_to(group_rectangle_0, LEFT)
        number_0.shift(RIGHT*0.58)
        number_1.next_to(group_rectangle_1, LEFT)
        number_1.shift(RIGHT*0.58)
        number_2.next_to(group_rectangle_2, LEFT)
        number_2.shift(RIGHT*0.58)
        number_3.next_to(group_rectangle_3, LEFT)
        number_3.shift(RIGHT*0.58)
        number = VGroup(number_0, number_1, number_2, number_3)

        # arrow_head
        vec_head = Arrow(np.array([0, 1, 0]), np.array(
            [0, -1, 0]), buff=0.6, color=BLACK)
        vec_head.scale(0.5)
        vec_head.next_to(group_rectangle_0, UP, buff=0.1)
        vec_head.shift(LEFT*0.25)

        # arrow_tail
        vec_tail = vec_head.copy()
        vec_tail.next_to(group_rectangle_3, UP, buff=0.1)
        vec_tail.shift(LEFT*0.25)

        # arrow_list
        vec_list_0 = Arrow(buff=0.5, color=BLACK)
        vec_list_0.scale(0.75)
        vec_list_1 = vec_list_0.copy()
        vec_list_2 = vec_list_0.copy()
        vec_list_3 = vec_list_0.copy()
        vec_list_0.next_to(group_rectangle_0, RIGHT, buff=0.1)
        vec_list_1.next_to(group_rectangle_1, RIGHT, buff=0.1)
        vec_list_2.next_to(group_rectangle_2, RIGHT, buff=0.1)
        vec_list_3.next_to(group_rectangle_3, RIGHT, buff=0.1)
        vec_list_0.shift(LEFT*0.3)
        vec_list_1.shift(LEFT*0.3)
        vec_list_2.shift(LEFT*0.3)
        vec_list_3.shift(LEFT*0.3)
        vec_list = VGroup(vec_list_0, vec_list_1, vec_list_2, vec_list_3)

        # text
        text_1 = TextMobject("head", color=BLACK)
        text_1.next_to(vec_head, UP, buff=0.05)
        text_1.scale(0.7)
        text_2 = TextMobject("tail", color=BLACK)
        text_2.next_to(vec_tail, UP, buff=0.05)
        text_2.scale(0.7)
        text_3 = TextMobject("NULL", color=BLACK)
        text_3.next_to(vec_list_3, RIGHT, buff=0)
        text_3.scale(0.7)
        text = VGroup(text_1, text_2, text_3)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params = VGroup(curLength, curLength_value)
        params.next_to(group_rectangle_0, LEFT, buff=0.7)

        # All
        All = VGroup(group_rectangle, vec_head, vec_tail, rectangle_front_filling,
                     vec_list, text, number, params)
        All.shift(LEFT*2.5+DOWN*2)

        # Code block
        tex_bg_1 = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                    fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg_1.set_height(3.5, stretch=True).set_width(7.5, stretch=True)
        tex_bg_2 = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                    fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg_2.set_height(3.5, stretch=True).set_width(4.5, stretch=True)
        tex_bg_1.to_corner(UP*1.5+LEFT*2.15)
        tex_bg_2.to_corner(UP*1.5+RIGHT*2.15)
        method = CodeLine("search(const elemType &value)",
                          size=0.8).to_corner(UP, buff=0.18)
        codes_1 = [
            "Node *p = head->next; ",
            "int count = 0;",
            "while (p != NULL && p->data != value)",
            "{",
            "    p = p->next;",
            "    count++;",
        ]
        codes_2 = [
            "}",
            "if (p == NULL)",
            "    return -1;",
            "else",
            "    return count;",
        ]
        codes_mob_1 = VGroup(
            *[
                CodeLine(code) for code in codes_1
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_1.next_to(tex_bg_1.get_top(), DOWN, buff=0.2)
        codes_mob_2 = VGroup(
            *[
                CodeLine(code) for code in codes_2
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_2.next_to(tex_bg_2.get_top(), DOWN, buff=0.2).shift(LEFT*0.4)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # Code text
        code_text_head = CodeLine(
            "head->next", size=0.7).next_to(tex_bg_1.get_top(), DOWN, buff=0.2).shift(LEFT*0.67)

        # join
        self.add(tex_bg_1, tex_bg_2)
        self.add(method, codes_mob_1, codes_mob_2)
        self.add(group_rectangle)
        self.add(vec_head)
        self.add(vec_tail)
        self.add(vec_list)
        self.add(text)
        self.add(number)
        self.add(params)
        self.wait()

        # show 1
        self.wait()
        method_trans = CodeLine(
            "search(2)", size=0.8).to_corner(UP, buff=0.18)
        self.play(Transform(method, method_trans))
        self.wait()
        foot_line.set_length(4.2)
        foot_line.next_to(codes_mob_1[0], DOWN, buff=0.1).shift(LEFT*0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_head_cp = vec_head.copy()
        vec_head_cp.set_color(BLUE)
        self.play(ShowCreation(vec_head_cp), run_time=1.5)
        self.wait()
        self.play(ReplacementTransform(code_text_head,
                                       rectangle_front_filling), run_time=1.5)
        self.wait()
        vec_tmp = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_tmp.scale(0.5)
        vec_tmp.next_to(group_rectangle_0, DOWN, buff=0.1)
        vec_tmp.shift(LEFT*0.25)
        text_p = TextMobject("P", color=BLACK)
        text_p.next_to(vec_tmp, DOWN, buff=0.05)
        text_p.scale(0.7)
        move_tmp = VGroup(vec_tmp, text_p)
        self.play(ReplacementTransform(
            rectangle_front_filling, move_tmp), run_time=1.5)
        self.wait()

        # show 2
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.8)
        foot_line.next_to(codes_mob_1[1], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        count = TextMobject("count = ", color=BLACK)
        count.scale(0.7)
        count.next_to(curLength, DOWN, aligned_edge=LEFT, buff=0)
        count.shift(LEFT*0.3)
        count_value = TextMobject("0", color=RED_D)
        count_value.next_to(count, RIGHT)
        count_params = VGroup(count, count_value)
        self.play(FadeInFromDown(count_params), ApplyMethod(
            params.shift, UP*0.45+LEFT*0.35))
        self.wait()

        # show 3
        self.play(FadeOut(foot_line))
        foot_line.set_length(7.2)
        foot_line.next_to(codes_mob_1[2], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans = CodeLine("while (p != NULL && 0 != 2)", size=0.7).move_to(
            codes_mob_1[2], aligned_edge=LEFT)
        codes_mob_tmp = codes_mob_1[2].copy()
        self.play(Transform(codes_mob_1[2], codes_mob_trans),
                  foot_line.set_length, 5.3, foot_line.shift, LEFT)
        self.wait()

        # show 4
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_list_0_cp = vec_list_0.copy()
        vec_list_0_cp.set_color(BLUE)
        self.play(ShowCreation(vec_list_0_cp), Transform(
            codes_mob_1[2], codes_mob_tmp), run_time=1.5)
        self.wait()
        self.play(move_tmp.shift, RIGHT*1.65)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.6)
        foot_line.next_to(codes_mob_1[5], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        count_value1 = TextMobject("1", color=RED_D)
        count_value1.next_to(count, RIGHT)
        self.play(ReplacementTransform(count_value, count_value1))
        self.wait()

        # show 5
        self.play(FadeOut(foot_line))
        foot_line.set_length(7.2)
        foot_line.next_to(codes_mob_1[2], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans2 = CodeLine("while (p != NULL && 1 != 2)", size=0.7).move_to(
            codes_mob_1[2], aligned_edge=LEFT)
        codes_mob_tmp2 = codes_mob_1[2].copy()
        self.play(Transform(codes_mob_1[2], codes_mob_trans2),
                  foot_line.set_length, 5.3, foot_line.shift, LEFT)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_list_1_cp = vec_list_1.copy()
        vec_list_1_cp.set_color(BLUE)
        self.play(ShowCreation(vec_list_1_cp), Transform(
            codes_mob_1[2], codes_mob_tmp2), run_time=1.5)
        self.wait()
        self.play(move_tmp.shift, RIGHT*1.65)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.6)
        foot_line.next_to(codes_mob_1[5], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        count_value2 = TextMobject("2", color=RED_D)
        count_value2.next_to(count, RIGHT)
        self.play(ReplacementTransform(count_value1, count_value2))
        self.wait()

        # show 6
        self.play(FadeOut(foot_line))
        foot_line.set_length(7.2)
        foot_line.next_to(codes_mob_1[2], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans3 = CodeLine("while (p != NULL && 2 != 2)", size=0.7).move_to(
            codes_mob_1[2], aligned_edge=LEFT)
        codes_mob_tmp3 = codes_mob_1[2].copy()
        self.play(Transform(codes_mob_1[2], codes_mob_trans3),
                  foot_line.set_length, 5.3, foot_line.shift, LEFT)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.8)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(0.8)
        foot_line.next_to(codes_mob_2[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line), Transform(
            codes_mob_1[2], codes_mob_tmp3))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.6)
        foot_line.next_to(codes_mob_2[4], DOWN, buff=0.1).shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()


class DepartmentDetails_link_visit(Scene_):

    def construct(self):
        # List
        rectangle_front = Rectangle(height=0.5, width=0.5,
                                    opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_later = rectangle_front.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        rectangle_front_filling = rectangle_front.copy()
        rectangle_front_filling.set_opacity(0.5).set_color(
            BLUE).set_height(0.45).set_width(0.45)
        group_rectangle_0 = VGroup(rectangle_front, rectangle_later)
        group_rectangle_1 = group_rectangle_0.copy()
        group_rectangle_2 = group_rectangle_0.copy()
        group_rectangle_3 = group_rectangle_0.copy()
        group_rectangle_1.next_to(group_rectangle_0, RIGHT, buff=0.65)
        group_rectangle_2.next_to(group_rectangle_1, RIGHT, buff=0.65)
        group_rectangle_3.next_to(group_rectangle_2, RIGHT, buff=0.65)
        group_rectangle = VGroup(
            group_rectangle_0, group_rectangle_1, group_rectangle_2, group_rectangle_3)

        # number
        number_0 = TextMobject("0", color=BLACK)
        number_1 = TextMobject("1", color=BLACK)
        number_2 = TextMobject("2", color=BLACK)
        number_3 = TextMobject("3", color=BLACK)
        number_0.scale(0.7)
        number_1.scale(0.7)
        number_2.scale(0.7)
        number_3.scale(0.7)
        number_0.next_to(group_rectangle_0, LEFT)
        number_0.shift(RIGHT*0.58)
        number_1.next_to(group_rectangle_1, LEFT)
        number_1.shift(RIGHT*0.58)
        number_2.next_to(group_rectangle_2, LEFT)
        number_2.shift(RIGHT*0.58)
        number_3.next_to(group_rectangle_3, LEFT)
        number_3.shift(RIGHT*0.58)
        number = VGroup(number_0, number_1, number_2, number_3)

        # arrow_head
        vec_head = Arrow(np.array([0, 1, 0]), np.array(
            [0, -1, 0]), buff=0.6, color=BLACK)
        vec_head.scale(0.5)
        vec_head.next_to(group_rectangle_0, UP, buff=0.1)
        vec_head.shift(LEFT*0.25)

        # arrow_tail
        vec_tail = vec_head.copy()
        vec_tail.next_to(group_rectangle_3, UP, buff=0.1)
        vec_tail.shift(LEFT*0.25)

        # arrow_list
        vec_list_0 = Arrow(buff=0.5, color=BLACK)
        vec_list_0.scale(0.75)
        vec_list_1 = vec_list_0.copy()
        vec_list_2 = vec_list_0.copy()
        vec_list_3 = vec_list_0.copy()
        vec_list_0.next_to(group_rectangle_0, RIGHT, buff=0.1)
        vec_list_1.next_to(group_rectangle_1, RIGHT, buff=0.1)
        vec_list_2.next_to(group_rectangle_2, RIGHT, buff=0.1)
        vec_list_3.next_to(group_rectangle_3, RIGHT, buff=0.1)
        vec_list_0.shift(LEFT*0.3)
        vec_list_1.shift(LEFT*0.3)
        vec_list_2.shift(LEFT*0.3)
        vec_list_3.shift(LEFT*0.3)
        vec_list = VGroup(vec_list_0, vec_list_1, vec_list_2, vec_list_3)

        # text
        text_1 = TextMobject("head", color=BLACK)
        text_1.next_to(vec_head, UP, buff=0.05)
        text_1.scale(0.7)
        text_2 = TextMobject("tail", color=BLACK)
        text_2.next_to(vec_tail, UP, buff=0.05)
        text_2.scale(0.7)
        text_3 = TextMobject("NULL", color=BLACK)
        text_3.next_to(vec_list_3, RIGHT, buff=0)
        text_3.scale(0.7)
        text = VGroup(text_1, text_2, text_3)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params = VGroup(curLength, curLength_value)
        params.next_to(group_rectangle_0, LEFT, buff=0.7)

        # All
        All = VGroup(group_rectangle, vec_head, vec_tail, rectangle_front_filling,
                     vec_list, text, number, params)
        All.shift(LEFT*2.5+DOWN*2)

        # Code block
        tex_bg_1 = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                    fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg_1.set_height(3.5, stretch=True).set_width(6.5, stretch=True)
        tex_bg_2 = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                    fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg_2.set_height(3.5, stretch=True).set_width(5.5, stretch=True)
        tex_bg_1.to_corner(UP*1.5+LEFT*2.15)
        tex_bg_2.to_corner(UP*1.5+RIGHT*2.15)
        method = CodeLine("visit(int i)",
                          size=0.8).to_corner(UP, buff=0.18)
        codes_1 = [
            "Node *p = head->next;",
            "int count = 0;",
            "if (i < 0 || i > curLength - 1)",
            "    throw outOfRange();",
            "while (count < i)",
            "{",
        ]
        codes_2 = [
            "    p = p->next;",
            "    ++count;",
            "}",
            "return p->data;",
        ]
        codes_mob_1 = VGroup(
            *[
                CodeLine(code) for code in codes_1
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_1.next_to(tex_bg_1.get_top(), DOWN, buff=0.2).shift(LEFT*0.1)
        codes_mob_2 = VGroup(
            *[
                CodeLine(code) for code in codes_2
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_2.next_to(tex_bg_2.get_top(), DOWN, buff=0.2).shift(LEFT*1.1)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # Code text
        code_text_head = CodeLine(
            "head->next", size=0.7).next_to(tex_bg_1.get_top(), DOWN, buff=0.2).shift(LEFT*0.18)

        # join
        self.add(tex_bg_1, tex_bg_2)
        self.add(method, codes_mob_1, codes_mob_2)
        self.add(group_rectangle)
        self.add(vec_head)
        self.add(vec_tail)
        self.add(vec_list)
        self.add(text)
        self.add(number)
        self.add(params)
        self.add(code_text_head)
        self.wait()

        # show 1
        self.wait()
        method_trans = CodeLine(
            "visit(1)", size=0.8).to_corner(UP, buff=0.18)
        self.play(Transform(method, method_trans))
        self.wait()
        foot_line.set_length(4.2)
        foot_line.next_to(codes_mob_1[0], DOWN, buff=0.1).shift(LEFT*0.05)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_head_cp = vec_head.copy()
        vec_head_cp.set_color(BLUE)
        self.play(ShowCreation(vec_head_cp), run_time=1.5)
        self.wait()
        self.play(ReplacementTransform(code_text_head,
                                       rectangle_front_filling), run_time=1.5)
        self.wait()
        vec_tmp = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_tmp.scale(0.5)
        vec_tmp.next_to(group_rectangle_0, DOWN, buff=0.1)
        vec_tmp.shift(LEFT*0.25)
        text_p = TextMobject("P", color=BLACK)
        text_p.next_to(vec_tmp, DOWN, buff=0.05)
        text_p.scale(0.7)
        move_tmp = VGroup(vec_tmp, text_p)
        self.play(ReplacementTransform(
            rectangle_front_filling, move_tmp), run_time=1.5)
        self.wait()

        # show 2
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.8)
        foot_line.next_to(codes_mob_1[1], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        count = TextMobject("count = ", color=BLACK)
        count.scale(0.7)
        count.next_to(curLength, DOWN, aligned_edge=LEFT, buff=0)
        count.shift(LEFT*0.3)
        count_value = TextMobject("0", color=RED_D)
        count_value.next_to(count, RIGHT)
        count_params = VGroup(count, count_value)
        self.play(FadeInFromDown(count_params), ApplyMethod(
            params.shift, UP*0.45+LEFT*0.35))
        self.wait()

        # show 3
        self.play(FadeOut(foot_line))
        foot_line.set_length(6)
        foot_line.next_to(codes_mob_1[2], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans = CodeLine("if (i < 0 || i > 3)", size=0.7).move_to(
            codes_mob_1[2], aligned_edge=LEFT)
        codes_mob_tmp = codes_mob_1[2].copy()   # 为了之后的复原
        self.play(Transform(codes_mob_1[2], codes_mob_trans),
                  foot_line.set_length, 3.7, foot_line.shift, LEFT*1.15)
        self.wait()

        # show 4
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans2 = CodeLine("while (0 < 1)", size=0.7).move_to(
            codes_mob_1[4], aligned_edge=LEFT)
        codes_mob_tmp2 = codes_mob_1[4].copy()   # 为了之后的复原
        self.play(Transform(codes_mob_1[4], codes_mob_trans2),
                  foot_line.set_length, 2.6, foot_line.shift, LEFT*0.35)
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.5)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1).shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line), Transform(
            codes_mob_1[2], codes_mob_tmp))
        self.wait()
        vec_list_0_cp = vec_list_0.copy()
        vec_list_0_cp.set_color(BLUE)
        self.play(ShowCreation(vec_list_0_cp), Transform(
            codes_mob_1[4], codes_mob_tmp2), run_time=1.5)
        self.wait()
        self.play(move_tmp.shift, RIGHT*1.65)
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.6)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1).shift(RIGHT*0.4)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        count_value1 = TextMobject("1", color=RED_D)
        count_value1.next_to(count, RIGHT)
        self.play(ReplacementTransform(count_value, count_value1))

        # show 5
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans3 = CodeLine("while (1 < 1)", size=0.7).move_to(
            codes_mob_1[4], aligned_edge=LEFT)
        codes_mob_tmp3 = codes_mob_1[4].copy()   # 为了之后的复原
        self.play(Transform(codes_mob_1[4], codes_mob_trans3),
                  foot_line.set_length, 2.6, foot_line.shift, LEFT*0.35)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3)
        foot_line.next_to(codes_mob_2[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line), Transform(
            codes_mob_1[4], codes_mob_tmp3))
        self.wait()


class DepartmentDetails_link_inverse(Scene_):

    def construct(self):
        # List
        rectangle_front = Rectangle(height=0.5, width=0.5,
                                    opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_later = rectangle_front.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        rectangle_front_filling = rectangle_front.copy()
        rectangle_front_filling.set_opacity(0.5).set_color(
            BLUE).set_height(0.45).set_width(0.45)
        group_rectangle_0 = VGroup(rectangle_front, rectangle_later)
        group_rectangle_1 = group_rectangle_0.copy()
        group_rectangle_2 = group_rectangle_0.copy()
        group_rectangle_3 = group_rectangle_0.copy()
        group_rectangle_1.next_to(group_rectangle_0, RIGHT, buff=0.65)
        group_rectangle_2.next_to(group_rectangle_1, RIGHT, buff=0.65)
        group_rectangle_3.next_to(group_rectangle_2, RIGHT, buff=0.65)
        group_rectangle = VGroup(
            group_rectangle_0, group_rectangle_1, group_rectangle_2, group_rectangle_3)

        # number
        number_0 = TextMobject("0", color=BLACK)
        number_1 = TextMobject("1", color=BLACK)
        number_2 = TextMobject("2", color=BLACK)
        number_3 = TextMobject("3", color=BLACK)
        number_0.scale(0.7)
        number_1.scale(0.7)
        number_2.scale(0.7)
        number_3.scale(0.7)
        number_0.next_to(group_rectangle_0, LEFT)
        number_0.shift(RIGHT*0.58)
        number_1.next_to(group_rectangle_1, LEFT)
        number_1.shift(RIGHT*0.58)
        number_2.next_to(group_rectangle_2, LEFT)
        number_2.shift(RIGHT*0.58)
        number_3.next_to(group_rectangle_3, LEFT)
        number_3.shift(RIGHT*0.58)
        number = VGroup(number_0, number_1, number_2, number_3)

        # arrow_head
        vec_head = Arrow(np.array([0, 1, 0]), np.array(
            [0, -1, 0]), buff=0.6, color=BLACK)
        vec_head.scale(0.5)
        vec_head.next_to(group_rectangle_0, UP, buff=0.1)
        vec_head.shift(LEFT*0.25)

        # arrow_tail
        vec_tail = vec_head.copy()
        vec_tail.next_to(group_rectangle_3, UP, buff=0.1)
        vec_tail.shift(LEFT*0.25)

        # arrow_list
        vec_list_0 = Arrow(buff=0.5, color=BLACK)
        vec_list_0.scale(0.75)
        vec_list_1 = vec_list_0.copy()
        vec_list_2 = vec_list_0.copy()
        vec_list_3 = vec_list_0.copy()
        vec_list_0.next_to(group_rectangle_0, RIGHT, buff=0.1)
        vec_list_1.next_to(group_rectangle_1, RIGHT, buff=0.1)
        vec_list_2.next_to(group_rectangle_2, RIGHT, buff=0.1)
        vec_list_3.next_to(group_rectangle_3, RIGHT, buff=0.1)
        vec_list_0.shift(LEFT*0.3)
        vec_list_1.shift(LEFT*0.3)
        vec_list_2.shift(LEFT*0.3)
        vec_list_3.shift(LEFT*0.3)
        vec_list = VGroup(vec_list_0, vec_list_1, vec_list_2, vec_list_3)

        # text
        text_1 = TextMobject("head", color=BLACK)
        text_1.next_to(vec_head, UP, buff=0.05)
        text_1.scale(0.7)
        text_2 = TextMobject("tail", color=BLACK)
        text_2.next_to(vec_tail, UP, buff=0.05)
        text_2.scale(0.7)
        text_3 = TextMobject("NULL", color=BLACK)
        text_3.next_to(vec_list_3, RIGHT, buff=0)
        text_3.scale(0.7)
        text = VGroup(text_1, text_2, text_3)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params = VGroup(curLength, curLength_value)
        params.next_to(group_rectangle_0, LEFT, buff=0.7)

        # All
        All = VGroup(group_rectangle, vec_head, vec_tail, rectangle_front_filling,
                     vec_list, text, number, params)
        All.shift(LEFT*2.5+DOWN*2)

        # Code block
        tex_bg_1 = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                    fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg_1.set_height(3.5, stretch=True).set_width(6, stretch=True)
        tex_bg_2 = tex_bg_1.copy()
        tex_bg_1.to_corner(UP*1.5+LEFT*2.15)
        tex_bg_2.to_corner(UP*1.5+RIGHT*2.15)
        method = CodeLine("inverse()",
                          size=0.8).to_corner(UP, buff=0.18)
        codes_1 = [
            "Node *p = head->next;",
            "head->next = NULL;",
            "if (p != NULL)",
            "    tail = p;",
            "while (p != NULL)",
            "{",
        ]
        codes_2 = [
            "    Node *tmp = p->next;",
            "    p->next = head->next;",
            "    head->next = p;",
            "    p = tmp;",
            "}",
        ]
        codes_mob_1 = VGroup(
            *[
                CodeLine(code) for code in codes_1
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_1.next_to(tex_bg_1.get_top(), DOWN, buff=0.2).shift(LEFT*0.8)
        codes_mob_2 = VGroup(
            *[
                CodeLine(code) for code in codes_2
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_2.next_to(tex_bg_2.get_top(), DOWN, buff=0.2).shift(LEFT*0.4)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # Code text
        code_text = CodeLine(
            "head->next", size=0.7).next_to(tex_bg_1.get_top(), DOWN, buff=0.2).shift(RIGHT*0.1)

        # join
        self.add(tex_bg_1, tex_bg_2)
        self.add(method, codes_mob_1, codes_mob_2)
        self.add(group_rectangle)
        self.add(vec_head)
        self.add(vec_tail)
        self.add(vec_list)
        self.add(text)
        self.add(number)
        self.add(params)
        self.add(code_text)
        self.wait()

        # show 1
        foot_line.set_length(4.2)
        foot_line.next_to(codes_mob_1[0], DOWN, buff=0.1).shift(LEFT*0.05)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_head_cp = vec_head.copy()
        vec_head_cp.set_color(BLUE)
        self.play(ShowCreation(vec_head_cp), run_time=1.5)
        self.wait()
        self.play(ReplacementTransform(code_text,
                                       rectangle_front_filling), run_time=1.5)
        self.wait()
        vec_tmp = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_tmp.scale(0.5)
        vec_tmp.next_to(group_rectangle_0, DOWN, buff=0.1)
        vec_tmp.shift(LEFT*0.25)
        text_p = TextMobject("P", color=BLACK)
        text_p.next_to(vec_tmp, DOWN, buff=0.05)
        text_p.scale(0.7)
        move_tmp = VGroup(vec_tmp, text_p)
        self.play(ReplacementTransform(
            rectangle_front_filling, move_tmp), run_time=1.5)
        self.wait()

        # show 2
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.6)
        foot_line.next_to(codes_mob_1[1], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_head_null = Arrow(np.array([1, 0, 0]), np.array(
            [-1, 0, 0]), buff=0.6, color=BLACK)
        vec_head_null.scale(0.75)
        vec_head_null.next_to(text_1, LEFT, buff=0.1)
        text_head_null = text_3.copy()
        text_head_null.next_to(vec_head_null, LEFT, buff=0.15)
        head_null = VGroup(vec_head_null, text_head_null)
        self.play(FadeOut(vec_head_cp), FadeOut(
            vec_head), FadeIn(vec_head_null), FadeInFrom(text_head_null, direction=LEFT), run_time=1.5)
        self.wait()

        # show 3
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.7)
        foot_line.next_to(codes_mob_1[2], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.8)
        foot_line.next_to(codes_mob_1[3], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.38)
        self.play(GrowFromCenter(foot_line))
        vec_tail_real = vec_head.copy()
        vec_tail_real.rotate(angle=5*PI/6, about_point=number_0.get_center())
        self.wait()
        text_tail = TextMobject("tail", color=BLACK)
        text_tail.scale(0.7)
        text_tail.next_to(text_p, LEFT, buff=0.1)
        text_tail_cp = text_p.copy()
        vec_tail_real_cp = vec_tmp.copy()
        self.play(ReplacementTransform(text_tail_cp, text_tail),
                  ReplacementTransform(vec_tail_real_cp, vec_tail_real), FadeOut(text_2), FadeOut(vec_tail))
        tail_real = VGroup(text_tail, vec_tail_real)
        self.wait()

        # show 3
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.9)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1).shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        # 第一个箭头变蓝
        vec_list_0_cp = vec_list_0.copy()
        vec_list_0_cp.set_color(BLUE)
        self.play(ShowCreation(vec_list_0_cp), run_time=1.5)
        self.wait()
        # 出现 tmp指针(改位置即可)
        vec_tmp_real = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_tmp_real.scale(0.5)
        vec_tmp_real.next_to(group_rectangle_1, DOWN, buff=0.1)
        vec_tmp_real.shift(LEFT*0.25)
        text_tmp = TextMobject("tmp", color=BLACK)
        text_tmp.next_to(vec_tmp_real, DOWN, buff=0.05)
        text_tmp.scale(0.7)
        move_tmp_real = VGroup(vec_tmp_real, text_tmp)
        self.play(FadeIn(move_tmp_real))
        self.wait()
        #
        self.play(FadeOut(foot_line))
        foot_line_front = Line(opacity=1, stroke_color=PURPLE_E)
        foot_line_front.put_start_and_end_on(codes_mob_2[1].get_center(
        )+RIGHT*1.75+DOWN*0.25, codes_mob_2[1].get_center()+LEFT*0.2+DOWN*0.25).shift(RIGHT*0.5)
        self.play(ShowCreation(foot_line_front),
                  FadeOut(vec_list_0_cp))  # 蓝箭头消失
        self.wait(0.5)
        # head -> NULL 的箭头变蓝
        vec_head_null_cp = vec_head_null.copy()
        vec_head_null_cp.set_color(BLUE)
        self.play(ShowCreation(vec_head_null_cp), run_time=1.5)
        self.wait()
        #
        foot_line_second = foot_line_front.copy()
        foot_line_second.put_start_and_end_on(codes_mob_2[1].get_center(
        )+LEFT*0.2+DOWN*0.25, codes_mob_2[1].get_center()+LEFT*2.1+DOWN*0.25).shift(RIGHT*0.5)
        self.play(ShowCreation(foot_line_second), run_time=1)
        self.wait()
        # 第一个链块(方块 数字 箭头)翻转180度、tail和p与其箭头一起向右移动一点、第一个链块的蓝色箭头消失、curlength向左下移动一点、NULL从上面出现
        rotate_rectangle = VGroup(
            group_rectangle_0, number_0, vec_list_0, vec_list_0_cp)
        one_shot_move = VGroup(tail_real, move_tmp)
        text_0_null = text_3.copy()
        text_0_null.next_to(vec_list_0, LEFT, buff=0.15).shift(LEFT*1.35)
        self.play(FadeIn(vec_list_0_cp), ApplyMethod(
            params.shift, LEFT*0.5+DOWN*0.8))
        self.wait(0.75)
        self.play(ApplyMethod(rotate_rectangle.rotate, {
                  "angle": PI, "axis": OUT, "about_point": group_rectangle_0.get_center()}),
                  ApplyMethod(one_shot_move.shift, RIGHT*0.5), FadeInFrom(text_0_null, direction=UP))
        self.wait()
        #
        self.play(FadeOut(foot_line_front), FadeOut(foot_line_second))
        foot_line.set_length(2.9)
        foot_line.next_to(codes_mob_2[2], DOWN, buff=0.1).shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line), FadeOut(vec_list_0_cp))
        self.wait()
        # head指移动
        vec_head_0 = Arrow(np.array([0, 1, 0]), np.array(
            [0, -1, 0]), buff=0.6, color=BLACK)
        vec_head_0.scale(0.5)
        vec_head_0.next_to(number_0, UP, buff=0.25)
        self.play(FadeOut(text_head_null), FadeOut(vec_head_null),
                  FadeOut(vec_head_null_cp), text_1.shift, RIGHT*0.5)
        self.wait(0.5)
        self.play(FadeIn(vec_head_0))
        head_final = VGroup(vec_head_0, text_1)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.5)
        foot_line.next_to(codes_mob_2[3], DOWN, buff=0.1).shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        # p指针、tail指针、tmp指针的移动
        self.play(ApplyMethod(vec_tail_real.rotate, {"angle": PI/6, "about_point": number_0.get_center()}),
                  ApplyMethod(vec_tmp_real.rotate, {
                              "angle": PI/6, "about_point": number_1.get_center()}),
                  ApplyMethod(move_tmp.shift, RIGHT*1.15), ApplyMethod(text_tail.shift, RIGHT*0.5), ApplyMethod(text_tmp.shift, RIGHT*0.5), run_time=1.5)
        self.wait()

        # show 4
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.9)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1).shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        # 第二个箭头变蓝
        vec_list_1_cp = vec_list_1.copy()
        vec_list_1_cp.set_color(BLUE)
        self.play(ShowCreation(vec_list_1_cp), run_time=1.5)
        self.wait()
        # 出现 tmp指针(改位置即可)
        self.play(FadeOut(move_tmp_real))
        self.wait(0.5)
        vec_tmp_real2 = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_tmp_real2.scale(0.5)
        vec_tmp_real2.next_to(group_rectangle_2, DOWN, buff=0.1)
        vec_tmp_real2.shift(LEFT*0.25)
        text_tmp2 = TextMobject("tmp", color=BLACK)
        text_tmp2.next_to(vec_tmp_real2, DOWN, buff=0.05)
        text_tmp2.scale(0.7)
        move_tmp_real2 = VGroup(vec_tmp_real2, text_tmp2)
        self.play(FadeIn(move_tmp_real2))
        self.wait()
        #
        self.play(FadeOut(foot_line))
        foot_line_front = Line(opacity=1, stroke_color=PURPLE_E)
        foot_line_front.put_start_and_end_on(codes_mob_2[1].get_center(
        )+RIGHT*1.75+DOWN*0.25, codes_mob_2[1].get_center()+LEFT*0.2+DOWN*0.25).shift(RIGHT*0.5)
        self.play(ShowCreation(foot_line_front),
                  FadeOut(vec_list_1_cp))  # 蓝箭头消失
        self.wait(0.5)
        vec_head_0_cp = vec_head_0.copy()
        vec_head_0_cp.set_color(BLUE)
        self.play(ShowCreation(vec_head_0_cp), run_time=1.5)
        self.wait()
        #
        foot_line_second = foot_line_front.copy()
        foot_line_second.put_start_and_end_on(codes_mob_2[1].get_center(
        )+LEFT*0.2+DOWN*0.25, codes_mob_2[1].get_center()+LEFT*2.1+DOWN*0.25).shift(RIGHT*0.5)
        self.play(ShowCreation(foot_line_second), run_time=1)
        self.wait()
        # 第二个链块(方块 数字 箭头)翻转180度、tail和p与其箭头一起向右移动一点、第一个链块的蓝色箭头消失、curlength向左下移动一点、NULL从上面出现
        rotate_rectangle2 = VGroup(
            group_rectangle_1, number_1, vec_list_1, vec_list_1_cp)
        self.play(FadeIn(vec_list_1_cp))
        self.wait(0.75)
        self.play(ApplyMethod(rotate_rectangle2.rotate, {
                  "angle": PI, "axis": OUT, "about_point": group_rectangle_1.get_center()}),
                  ApplyMethod(move_tmp.shift, RIGHT*0.5))
        self.play(ApplyMethod(number_1.rotate, PI))
        self.wait()
        #
        self.play(FadeOut(foot_line_front), FadeOut(foot_line_second))
        foot_line.set_length(2.9)
        foot_line.next_to(codes_mob_2[2], DOWN, buff=0.1).shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line), FadeOut(vec_list_1_cp))
        self.wait()
        # head指移动
        self.play(head_final.shift, RIGHT*1.65,
                  vec_head_0_cp.shift, RIGHT*1.65)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.5)
        foot_line.next_to(codes_mob_2[3], DOWN, buff=0.1).shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line), FadeOut(vec_head_0_cp))
        self.wait()
        # p指针、tail指针、tmp指针的移动
        self.play(ApplyMethod(vec_tmp_real2.rotate, {"angle": PI/6, "about_point": number_2.get_center()}),
                  ApplyMethod(move_tmp.shift, RIGHT*1.15), ApplyMethod(text_tmp2.shift, RIGHT*0.5), run_time=1.5)
        self.wait()

        # show 5
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.9)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1).shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        # 第三个箭头变蓝
        vec_list_2_cp = vec_list_2.copy()
        vec_list_2_cp.set_color(BLUE)
        self.play(ShowCreation(vec_list_2_cp), run_time=1.5)
        self.wait()
        # 出现 tmp指针(改位置即可)
        self.play(FadeOut(move_tmp_real2))
        self.wait(0.5)
        vec_tmp_real3 = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_tmp_real3.scale(0.5)
        vec_tmp_real3.next_to(group_rectangle_3, DOWN, buff=0.1)
        vec_tmp_real3.shift(LEFT*0.25)
        text_tmp3 = TextMobject("tmp", color=BLACK)
        text_tmp3.next_to(vec_tmp_real3, DOWN, buff=0.05)
        text_tmp3.scale(0.7)
        move_tmp_real3 = VGroup(vec_tmp_real3, text_tmp3)
        self.play(FadeIn(move_tmp_real3))
        self.wait()
        #
        self.play(FadeOut(foot_line))
        foot_line_front = Line(opacity=1, stroke_color=PURPLE_E)
        foot_line_front.put_start_and_end_on(codes_mob_2[1].get_center(
        )+RIGHT*1.75+DOWN*0.25, codes_mob_2[1].get_center()+LEFT*0.2+DOWN*0.25).shift(RIGHT*0.5)
        self.play(ShowCreation(foot_line_front),
                  FadeOut(vec_list_2_cp))  # 蓝箭头消失
        self.wait(0.5)
        self.play(ShowCreation(vec_head_0_cp), run_time=1.5)
        self.wait()
        #
        foot_line_second = foot_line_front.copy()
        foot_line_second.put_start_and_end_on(codes_mob_2[1].get_center(
        )+LEFT*0.2+DOWN*0.25, codes_mob_2[1].get_center()+LEFT*2.1+DOWN*0.25).shift(RIGHT*0.5)
        self.play(ShowCreation(foot_line_second), run_time=1)
        self.wait()
        # 第二个链块(方块 数字 箭头)翻转180度、tail和p与其箭头一起向右移动一点、第一个链块的蓝色箭头消失、curlength向左下移动一点、NULL从上面出现
        rotate_rectangle3 = VGroup(
            group_rectangle_2, number_2, vec_list_2, vec_list_2_cp)
        self.play(FadeIn(vec_list_2_cp))
        self.wait(0.75)
        self.play(ApplyMethod(rotate_rectangle3.rotate, {
                  "angle": PI, "axis": OUT, "about_point": group_rectangle_2.get_center()}),
                  ApplyMethod(move_tmp.shift, RIGHT*0.5))
        self.play(ApplyMethod(number_2.rotate, PI))
        self.wait()
        #
        self.play(FadeOut(foot_line_front), FadeOut(foot_line_second))
        foot_line.set_length(2.9)
        foot_line.next_to(codes_mob_2[2], DOWN, buff=0.1).shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line), FadeOut(vec_list_2_cp))
        self.wait()
        # head指移动
        self.play(head_final.shift, RIGHT*1.65,
                  vec_head_0_cp.shift, RIGHT*1.65)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.5)
        foot_line.next_to(codes_mob_2[3], DOWN, buff=0.1).shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line), FadeOut(vec_head_0_cp))
        self.wait()
        # p指针、tail指针、tmp指针的移动
        self.play(ApplyMethod(vec_tmp_real3.rotate, {"angle": PI/6, "about_point": number_3.get_center()}),
                  ApplyMethod(move_tmp.shift, RIGHT*1.15), ApplyMethod(text_tmp3.shift, RIGHT*0.5), run_time=1.5)
        self.wait()

        # show 6
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.9)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1).shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        # 第三个箭头变蓝
        vec_list_3_cp = vec_list_3.copy()
        vec_list_3_cp.set_color(BLUE)
        self.play(ShowCreation(vec_list_3_cp), run_time=1.5)
        self.wait()
        # 出现 tmp指针(改位置即可)
        self.play(FadeOut(move_tmp_real3))
        self.wait(0.5)
        vec_tmp_real4 = Arrow(np.array([0, -1, 0]), np.array(
            [0, 1, 0]), buff=0.6, color=BLACK)
        vec_tmp_real4.scale(0.5)
        vec_tmp_real4.next_to(text_3, DOWN, buff=0.2).shift(RIGHT*0.5)
        vec_tmp_real4.shift(LEFT*0.25)
        text_tmp4 = TextMobject("tmp", color=BLACK)
        text_tmp4.next_to(vec_tmp_real4, DOWN, buff=0.05)
        text_tmp4.scale(0.7)
        move_tmp_real4 = VGroup(vec_tmp_real4, text_tmp4)
        self.play(FadeIn(move_tmp_real4))
        self.wait()
        #
        self.play(FadeOut(foot_line))
        foot_line_front = Line(opacity=1, stroke_color=PURPLE_E)
        foot_line_front.put_start_and_end_on(codes_mob_2[1].get_center(
        )+RIGHT*1.75+DOWN*0.25, codes_mob_2[1].get_center()+LEFT*0.2+DOWN*0.25).shift(RIGHT*0.5)
        self.play(ShowCreation(foot_line_front),
                  FadeOut(vec_list_3_cp))  # 蓝箭头消失
        self.wait(0.5)
        self.play(ShowCreation(vec_head_0_cp), run_time=1.5)
        self.wait()
        #
        foot_line_second = foot_line_front.copy()
        foot_line_second.put_start_and_end_on(codes_mob_2[1].get_center(
        )+LEFT*0.2+DOWN*0.25, codes_mob_2[1].get_center()+LEFT*2.1+DOWN*0.25).shift(RIGHT*0.5)
        self.play(ShowCreation(foot_line_second), run_time=1)
        self.wait()
        # 第二个链块(方块 数字 箭头)翻转180度、tail和p与其箭头一起向右移动一点、第一个链块的蓝色箭头消失、curlength向左下移动一点、NULL从上面出现
        rotate_rectangle4 = VGroup(
            group_rectangle_3, number_3, vec_list_3, vec_list_3_cp)
        self.play(FadeIn(vec_list_3_cp))
        self.wait(0.75)
        self.play(ApplyMethod(rotate_rectangle4.rotate, {
                  "angle": PI, "axis": OUT, "about_point": group_rectangle_3.get_center()}),
                  ApplyMethod(move_tmp.shift, RIGHT*0.5))
        self.play(ApplyMethod(number_3.rotate, PI))
        self.wait()
        #
        self.play(FadeOut(foot_line_front), FadeOut(foot_line_second))
        foot_line.set_length(2.9)
        foot_line.next_to(codes_mob_2[2], DOWN, buff=0.1).shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line), FadeOut(vec_list_3_cp))
        self.wait()
        #
        self.play(head_final.shift, RIGHT*1.65,
                  vec_head_0_cp.shift, RIGHT*1.65)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.5)
        foot_line.next_to(codes_mob_2[3], DOWN, buff=0.1).shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line), FadeOut(vec_head_0_cp))
        self.wait()
        # p指针、tail指针、tmp指针的移动
        self.play(ApplyMethod(move_tmp.shift, RIGHT*1.15), run_time=1.5)
        self.wait()

        # show 7
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.4)
        foot_line.next_to(codes_mob_1[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_head_tail = Arrow(np.array([0, 1, 0]), np.array(
            [0, -1, 0]), buff=0.6, color=BLACK)
        vec_head_tail.scale(0.5)
        vec_head_tail.next_to(group_rectangle_0, UP, buff=0.1)
        vec_head_tail.shift(RIGHT*0.25)
        text_head_tail = TextMobject("tail", color=BLACK)
        text_head_tail.next_to(vec_head_tail, UP, buff=0.05)
        text_head_tail.scale(0.7)
        tail_up_up = VGroup(vec_head_tail, text_head_tail)
        self.play(Transform(tail_real, tail_up_up), FadeOut(
            text_3), FadeOut(move_tmp), FadeOut(move_tmp_real4))
        self.wait()
        big_big = VGroup(tail_real, head_final, text_0_null,
                         group_rectangle, vec_list, number)
        self.play(big_big.shift, RIGHT*2, params.shift, UP*0.8+RIGHT*0.9)
        self.wait()


class DepartmentDetails_seq_clear(Scene_):

    def construct(self):
        # List
        rectangle_0 = Rectangle(height=0.8, width=0.8,
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
        number_0.scale(1)
        number_1.scale(1)
        number_2.scale(1)
        number_3.scale(1)
        number_0.move_to(rectangle_0)
        number_1.move_to(rectangle_1)
        number_2.move_to(rectangle_2)
        number_3.move_to(rectangle_3)
        number = VGroup(number_0, number_1, number_2, number_3)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params_1 = VGroup(curLength, curLength_value)
        maxSize = TextMobject("maxSize = ", color=BLACK)
        maxSize.scale(0.7)
        maxSize_value = TextMobject("10", color=BLUE)
        maxSize_value.next_to(maxSize, RIGHT)
        params_2 = VGroup(maxSize, maxSize_value)
        params_2.next_to(params_1, DOWN, buff=0.5)
        params = VGroup(params_1, params_2)
        params.next_to(rectangle_0, LEFT, buff=1.5)

        # All
        All = VGroup(group_rectangle, number, params)
        All.shift(DOWN*0.5+RIGHT*0.5)

        # Code block
        tex_bg = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                  fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg.set_height(0.7, stretch=True).set_width(4, stretch=True)
        tex_bg.to_corner(UP*3.5)
        method = CodeLine_code("clear()",font='思源宋体 Heavy',
                                       size=0.8).to_corner(UP, buff=0.7)
        codes = [
            "curLength = 0;",
        ]
        codes_mob = VGroup(
            *[
                CodeLine(code) for code in codes
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob.next_to(tex_bg.get_top(), DOWN, buff=0.2)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # join
        self.add(group_rectangle, number, params)
        self.add(tex_bg, method, codes_mob)
        self.wait()

        # only show
        foot_line.set_length(3.1)
        foot_line.next_to(codes_mob[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        curLength_value_cp = TextMobject("0", color=BLUE)
        curLength_value_cp.next_to(curLength, RIGHT)
        self.play(Transform(curLength_value, curLength_value_cp))


class DepartmentDetails_seq_traverse(Scene_):

    def construct(self):
        # List
        rectangle_0 = Rectangle(height=0.8, width=0.8,
                                opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_filling = rectangle_0.copy()
        rectangle_filling.set_opacity(0.5).set_color(
            BLUE).set_height(0.75).set_width(0.75)
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
        number_0.scale(1)
        number_1.scale(1)
        number_2.scale(1)
        number_3.scale(1)
        number_0.move_to(rectangle_0)
        number_1.move_to(rectangle_1)
        number_2.move_to(rectangle_2)
        number_3.move_to(rectangle_3)
        number = VGroup(number_0, number_1, number_2, number_3)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params_1 = VGroup(curLength, curLength_value)
        maxSize = TextMobject("maxSize = ", color=BLACK)
        maxSize.scale(0.7)
        maxSize_value = TextMobject("10", color=BLUE)
        maxSize_value.next_to(maxSize, RIGHT)
        params_2 = VGroup(maxSize, maxSize_value)
        params_2.next_to(params_1, DOWN, buff=0.5)
        params = VGroup(params_1, params_2)
        params.next_to(rectangle_0, LEFT, buff=1.5)

        # All
        All = VGroup(group_rectangle, rectangle_filling, number, params)
        All.shift(DOWN*1.3+RIGHT*0.5)

        # Code block
        tex_bg_1 = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                    fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg_1.set_height(2.2, stretch=True).set_width(6.3, stretch=True)
        tex_bg_2 = tex_bg_1.copy()
        tex_bg_1.to_corner(UP*2+LEFT*1.55)
        tex_bg_2.to_corner(UP*2+RIGHT*1.55)
        method = CodeLine_seq_traverse("traverse()",
                                       size=0.8).to_corner(UP, buff=0.3)
        codes_1 = [
            "if (empty())",
            "  cout << \"Sequence list is empty\";",
            "else {",
            "  cout << \"result:\";",
        ]
        codes_2 = [
            "  for (int i = 0; i < curLength; ++i)",
            "     cout << data[i] << ' ';",
            "  cout << endl;",
            "}",
        ]
        codes_mob_1 = VGroup(
            *[
                CodeLine_seq_traverse(code) for code in codes_1
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_1.next_to(tex_bg_1.get_top(), DOWN, buff=0.2).shift(LEFT*0.1)
        codes_mob_2 = VGroup(
            *[
                CodeLine_seq_traverse(code) for code in codes_2
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_2.next_to(tex_bg_2.get_top(), DOWN, buff=0.2)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # Code text
        code_text = CodeLine_seq_traverse("empty()", size=0.6).next_to(
            tex_bg_1.get_top(), DOWN, buff=0.2).shift(LEFT*1.75)
        code_text_2 = CodeLine_seq_traverse("result:", size=0.6).next_to(
            tex_bg_1.get_top(), DOWN*8.85+RIGHT*3.1, buff=0.2).shift(LEFT*1.75)

        # join
        self.add(group_rectangle, number, params)
        self.add(tex_bg_1, tex_bg_2, method, codes_mob_1, codes_mob_2)
        self.wait()

        # show 1
        foot_line.set_length(2.1)
        foot_line.next_to(codes_mob_1[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        code_text_cp = code_text.copy()
        tex_bg_3 = RoundedRectangle(stroke_width=1, stroke_color=BLACK,
                                    fill_color="#EEA9A9", fill_opacity=0.45, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UL)
        tex_bg_3.set_height(2, stretch=True).set_width(4.5, stretch=True)
        tex_bg_3.move_to(DOWN*0.5)
        codes_empty = [
            "bool empty() const",
            "{",
            "    return curLength == 0;",
            "}",
        ]
        codes_mob_empty = VGroup(
            *[
                CodeLine_seq_traverse(code) for code in codes_empty
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_empty.next_to(
            tex_bg_3.get_top(), DOWN, buff=0.2).shift(UP*0.1)
        center = VGroup(tex_bg_3, codes_mob_empty)
        self.play(params.shift, LEFT*1.5+DOWN, group_rectangle.shift, RIGHT*2+DOWN,
                  number.shift, RIGHT*2+DOWN, ReplacementTransform(code_text, center))
        self.wait()
        self.play(params.shift, RIGHT*1.5+UP, group_rectangle.shift, LEFT*2+UP,
                  number.shift, LEFT*2+UP, ReplacementTransform(center, code_text_cp))
        self.wait()

        # show 2
        self.play(FadeOut(foot_line), FadeOut(code_text_cp))
        foot_line.set_length(0.7)
        foot_line.next_to(codes_mob_1[2], DOWN, buff=0.1)
        foot_line.shift(LEFT*0.15)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3)
        foot_line.next_to(codes_mob_1[3], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.15)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        result = TextMobject("result:", color=BLACK)
        result.scale(0.7)
        result.next_to(maxSize, DOWN, buff=0.5).shift(LEFT*0.5)
        self.play(ReplacementTransform(
            code_text_2, result), params.shift, UP*0.2)

        # show 3
        self.play(FadeOut(foot_line))
        foot_line.set_length(5.8)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.15)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        one_shot_trans = CodeLine("  for (int i = 0; i < 4; ++i)", size=0.6).move_to(
            codes_mob_2[0], aligned_edge=LEFT)
        one_shot_after = codes_mob_2[0].copy()   # 为了之后的复原
        self.play(Transform(codes_mob_2[0], one_shot_trans),
                  foot_line.set_length, 4.5, foot_line.shift, LEFT*0.7)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.8)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.4)
        self.play(GrowFromCenter(foot_line), FadeIn(rectangle_filling))
        self.wait()
        result_0 = number_0.copy()
        result_0.next_to(result, RIGHT, buff=0.25).scale(0.8)
        number_0_cp = number_0.copy()
        self.play(ReplacementTransform(number_0_cp, result_0), run_time=1.5)
        one_shot_1 = CodeLine("  for (int i = 1; i < 4; ++i)", size=0.6).move_to(
            codes_mob_2[0], aligned_edge=LEFT)
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.15)
        self.play(GrowFromCenter(foot_line))
        self.play(Transform(codes_mob_2[0], one_shot_1))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.8)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.4)
        self.play(GrowFromCenter(foot_line),
                  rectangle_filling.move_to, rectangle_1.get_center())
        self.wait()
        result_1 = number_1.copy()
        result_1.next_to(result_0, RIGHT, buff=0.3).scale(0.8)
        number_1_cp = number_1.copy()
        self.play(ReplacementTransform(number_1_cp, result_1), run_time=1.5)
        one_shot_2 = CodeLine("  for (int i = 2; i < 4; ++i)", size=0.6).move_to(
            codes_mob_2[0], aligned_edge=LEFT)
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.15)
        self.play(GrowFromCenter(foot_line))
        self.play(Transform(codes_mob_2[0], one_shot_2))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.8)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.4)
        self.play(GrowFromCenter(foot_line),
                  rectangle_filling.move_to, rectangle_2.get_center())
        self.wait()
        result_2 = number_2.copy()
        result_2.next_to(result_1, RIGHT, buff=0.3).scale(0.8)
        number_2_cp = number_2.copy()
        self.play(ReplacementTransform(number_2_cp, result_2), run_time=1.5)
        one_shot_3 = CodeLine("  for (int i = 3; i < 4; ++i)", size=0.6).move_to(
            codes_mob_2[0], aligned_edge=LEFT)
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.15)
        self.play(GrowFromCenter(foot_line))
        self.play(Transform(codes_mob_2[0], one_shot_3))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.8)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.4)
        self.play(GrowFromCenter(foot_line),
                  rectangle_filling.move_to, rectangle_3.get_center())
        self.wait()
        result_3 = number_3.copy()
        result_3.next_to(result_2, RIGHT, buff=0.3).scale(0.8)
        number_3_cp = number_3.copy()
        self.play(ReplacementTransform(number_3_cp, result_3), run_time=1.5)
        one_shot_4 = CodeLine("  for (int i = 4; i < 4; ++i)", size=0.6).move_to(
            codes_mob_2[0], aligned_edge=LEFT)

        # show 4
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.15)
        self.play(GrowFromCenter(foot_line))
        self.play(Transform(codes_mob_2[0], one_shot_4))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.3)
        foot_line.next_to(codes_mob_2[2], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.15)
        self.play(Transform(codes_mob_2[0], one_shot_after), GrowFromCenter(
            foot_line), FadeOut(rectangle_filling))
        self.wait()


class DepartmentDetails_seq_resize(Scene_):

    def construct(self):
        # List
        rectangle_0 = Rectangle(height=0.8, width=0.8,
                                opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_filling = rectangle_0.copy()
        rectangle_filling.set_opacity(0.5).set_color(
            BLUE).set_height(0.75).set_width(0.75)
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
        number_0.scale(1)
        number_1.scale(1)
        number_2.scale(1)
        number_3.scale(1)
        number_0.move_to(rectangle_0)
        number_1.move_to(rectangle_1)
        number_2.move_to(rectangle_2)
        number_3.move_to(rectangle_3)
        number = VGroup(number_0, number_1, number_2, number_3)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params_1 = VGroup(curLength, curLength_value)
        maxSize = TextMobject("maxSize = ", color=BLACK)
        maxSize.scale(0.7)
        maxSize_value = TextMobject("3", color=BLUE)
        maxSize_value.next_to(maxSize, RIGHT)
        params_2 = VGroup(maxSize, maxSize_value)
        params_2.next_to(params_1, DOWN, buff=0.5)
        params = VGroup(params_1, params_2)
        params.next_to(rectangle_0, LEFT, buff=1.5)

        # All
        All = VGroup(group_rectangle, number, params)
        All.shift(DOWN*1.3+RIGHT*0.5)

        # Code block
        tex_bg = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                  fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg.set_height(3.2, stretch=True).set_width(6.7, stretch=True)
        tex_bg.to_corner(UP*2)
        method = CodeLine_seq_traverse("resize()",
                                       size=0.8).to_corner(UP, buff=0.3)
        codes = [
            "elemType *p = data;",
            "maxSize *= 2;",
            "data = new elemType[maxSize];",
            "for (int i = 0; i < curLength; ++i)",
            "    data[i] = p[i];",
            "delete[] p;",
        ]
        codes_mob = VGroup(
            *[
                CodeLine_seq_traverse(code) for code in codes
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob.next_to(tex_bg.get_top(), DOWN, buff=0.2)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # join
        self.add(group_rectangle, number, params)
        self.add(tex_bg, method, codes_mob)
        self.wait()

        # show 1
        reveal = Rectangle(height=0.5, width=0.5,
                           opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal.move_to(maxSize_value)
        self.play(ShowCreation(reveal))
        self.wait(0.5)
        self.play(FadeOut(reveal))
        foot_line_front = Line(opacity=1, stroke_color=PURPLE_E)
        foot_line_front.put_start_and_end_on(codes_mob[0].get_center(
        )+RIGHT*1.45+DOWN*0.25, codes_mob[0].get_center()+RIGHT*0.75+DOWN*0.25)
        self.play(ShowCreation(foot_line_front))
        self.wait(0.5)
        seqlist = VGroup(group_rectangle, number)
        self.play(params.shift, LEFT*0.8, seqlist.shift, RIGHT*0.8)
        vec_data = Arrow(np.array([-1, 0, 0]), np.array(
            [1, 0, 0]), buff=0.6, color=BLACK)
        vec_data.scale(0.6)
        vec_data.next_to(number_0, LEFT, buff=0.15)
        vec_data.shift(LEFT*0.25)
        text_data = TextMobject("data", color=BLACK)
        text_data.scale(0.6).next_to(vec_data, LEFT, buff=0.1)
        data = VGroup(vec_data, text_data)
        self.play(FadeInFrom(data, direction=LEFT))
        foot_line_second = foot_line_front.copy()
        foot_line_second.put_start_and_end_on(codes_mob[0].get_center(
        )+RIGHT*0.75+DOWN*0.25, codes_mob[0].get_center()+LEFT*1.55+DOWN*0.25)
        self.play(ShowCreation(foot_line_second), run_time=1)
        self.wait()
        vec_p = Arrow(np.array([-1, 0, 0]), np.array(
            [1, 0, 0]), buff=0.6, color=BLACK)
        vec_p.scale(0.6)
        vec_p.next_to(number_0, LEFT, buff=0.15)
        vec_p.shift(LEFT*0.25+UP*0.25)
        text_p = TextMobject("p", color=BLACK)
        text_p.scale(0.6).next_to(vec_p, LEFT, buff=0.1)
        p = VGroup(vec_p, text_p)
        self.play(data.shift, DOWN*0.25)
        data_cp = data.copy()
        self.play(ReplacementTransform(data_cp, p))
        self.play(FadeOut(foot_line_front), FadeOut(foot_line_second))
        foot_line.set_length(2.2)
        foot_line.next_to(codes_mob[1], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        maxSize_value_trans = TextMobject("6", color=BLUE)
        maxSize_value_trans.next_to(maxSize, RIGHT)
        self.play(Transform(maxSize_value, maxSize_value_trans))
        self.wait()

        # show 2
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.8)
        foot_line.next_to(codes_mob[2], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_maxsize = CodeLine("data = new elemType[6];", size=0.6).move_to(
            codes_mob[2], aligned_edge=LEFT)
        codes_mob_maxsize_cp = codes_mob[2].copy()
        self.play(Transform(codes_mob[2], codes_mob_maxsize),
                  foot_line.set_length, 3.8, foot_line.shift, LEFT*0.5)
        self.wait()
        self.play(seqlist.shift, UP*0.5, p.shift, UP*0.5, data.shift, UP*0.5)
        self.play(p.shift, DOWN*0.25, data.shift, DOWN*1)
        rectangle0 = Rectangle(height=0.8, width=0.8,
                               opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle1 = rectangle0.copy()
        rectangle2 = rectangle0.copy()
        rectangle3 = rectangle0.copy()
        rectangle4 = rectangle0.copy()
        rectangle5 = rectangle0.copy()
        rectangle1.next_to(rectangle0, RIGHT, buff=0)
        rectangle2.next_to(rectangle1, RIGHT, buff=0)
        rectangle3.next_to(rectangle2, RIGHT, buff=0)
        rectangle4.next_to(rectangle3, RIGHT, buff=0)
        rectangle5.next_to(rectangle4, RIGHT, buff=0)
        group_rectangle_new = VGroup(
            rectangle0, rectangle1, rectangle2, rectangle3, rectangle4, rectangle5)
        group_rectangle_new.next_to(vec_data, RIGHT, buff=0.15)
        self.play(ShowCreation(group_rectangle_new))

        # show 3
        self.play(FadeOut(foot_line))
        foot_line.set_length(5.8)
        foot_line.next_to(codes_mob[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line), Transform(
            codes_mob[2], codes_mob_maxsize_cp))
        self.wait()
        circle_1 = CodeLine("for (int i = 0; 0 < 4; ++i)", size=0.6).move_to(
            codes_mob[3], aligned_edge=LEFT)
        circle_old = codes_mob[3].copy()   # 为了之后的复原
        self.play(Transform(codes_mob[3], circle_1),
                  foot_line.set_length, 4.5, foot_line.shift, LEFT*0.65)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.6)
        foot_line.next_to(codes_mob[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_1 = CodeLine("    data[0] = p[0];", size=0.6).move_to(
            codes_mob[4], aligned_edge=LEFT)
        clc_old = codes_mob[4].copy()   # 为了之后的复原
        self.play(Transform(codes_mob[4], clc_1))
        self.wait()
        #
        rectangle_filling.move_to(number_0)
        number_0_cp = number_0.copy()
        self.play(FadeIn(rectangle_filling))
        self.wait()
        self.play(number_0_cp.shift, DOWN*1.25+RIGHT*0.02)
        #
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_2 = CodeLine("for (int i = 0; 1 < 4; ++i)", size=0.6).move_to(
            codes_mob[3], aligned_edge=LEFT)
        self.play(Transform(codes_mob[3], circle_2))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.6)
        foot_line.next_to(codes_mob[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_2 = CodeLine("    data[1] = p[1];", size=0.6).move_to(
            codes_mob[4], aligned_edge=LEFT)
        self.play(Transform(codes_mob[4], clc_2))
        self.wait()
        #
        number_1_cp = number_1.copy()
        self.play(rectangle_filling.shift, RIGHT*0.8)
        self.wait()
        self.play(number_1_cp.shift, DOWN*1.25+RIGHT*0.02)
        #
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_3 = CodeLine("for (int i = 0; 2 < 4; ++i)", size=0.6).move_to(
            codes_mob[3], aligned_edge=LEFT)
        self.play(Transform(codes_mob[3], circle_3))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.6)
        foot_line.next_to(codes_mob[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_3 = CodeLine("    data[2] = p[2];", size=0.6).move_to(
            codes_mob[4], aligned_edge=LEFT)
        self.play(Transform(codes_mob[4], clc_3))
        self.wait()
        #
        number_2_cp = number_2.copy()
        self.play(rectangle_filling.shift, RIGHT*0.8)
        self.wait()
        self.play(number_2_cp.shift, DOWN*1.25+RIGHT*0.02)
        #
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_4 = CodeLine("for (int i = 0; 3 < 4; ++i)", size=0.6).move_to(
            codes_mob[3], aligned_edge=LEFT)
        self.play(Transform(codes_mob[3], circle_4))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.6)
        foot_line.next_to(codes_mob[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_4 = CodeLine("    data[3] = p[3];", size=0.6).move_to(
            codes_mob[4], aligned_edge=LEFT)
        self.play(Transform(codes_mob[4], clc_4))
        self.wait()
        #
        number_3_cp = number_3.copy()
        self.play(rectangle_filling.shift, RIGHT*0.8)
        self.wait()
        self.play(number_3_cp.shift, DOWN*1.25+RIGHT*0.02)
        #
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_5 = CodeLine("for (int i = 0; 4 < 4; ++i)", size=0.6).move_to(
            codes_mob[3], aligned_edge=LEFT)
        self.play(Transform(codes_mob[3], circle_5))
        self.wait()

        # show 4
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.9)
        foot_line.next_to(codes_mob[5], DOWN, buff=0.05)
        self.play(GrowFromCenter(foot_line), Transform(
            codes_mob[3], circle_old), Transform(
            codes_mob[4], clc_old), FadeOut(rectangle_filling))
        self.wait()
        up_ = VGroup(data, group_rectangle_new, number_0_cp,
                     number_1_cp, number_2_cp, number_3_cp)
        self.play(FadeOut(seqlist), FadeOut(p), up_.shift, UP*0.75)


class DepartmentDetails_seq_insert(Scene_):

    def construct(self):
        # List
        rectangle_0 = Rectangle(height=0.8, width=0.8,
                                opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_filling = rectangle_0.copy()
        rectangle_filling.set_opacity(0.5).set_color(
            BLUE).set_height(0.75).set_width(0.75)
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
        number_0.scale(1)
        number_1.scale(1)
        number_2.scale(1)
        number_3.scale(1)
        number_0.move_to(rectangle_0)
        number_1.move_to(rectangle_1)
        number_2.move_to(rectangle_2)
        number_3.move_to(rectangle_3)
        number = VGroup(number_0, number_1, number_2, number_3)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params_1 = VGroup(curLength, curLength_value)
        maxSize = TextMobject("maxSize = ", color=BLACK)
        maxSize.scale(0.7)
        maxSize_value = TextMobject("4", color=BLUE)
        maxSize_value.next_to(maxSize, RIGHT)
        params_2 = VGroup(maxSize, maxSize_value)
        params_2.next_to(params_1, DOWN, buff=0.5)
        params = VGroup(params_1, params_2)
        params.next_to(rectangle_0, LEFT, buff=1.5)

        # All
        All = VGroup(group_rectangle, number, params)
        All.shift(DOWN*1.3+RIGHT*0.5)

        # Code block
        tex_bg_1 = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                    fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg_1.set_height(2.3, stretch=True).set_width(6.3, stretch=True)
        tex_bg_2 = tex_bg_1.copy()
        tex_bg_1.to_corner(UP*2+LEFT*1.55)
        tex_bg_2.to_corner(UP*2+RIGHT*1.55)
        method = CodeLine_seq_traverse("insert(int i, const elemType &value)",
                                       size=0.8).to_corner(UP, buff=0.3)
        codes_1 = [
            "if (i < 0 || i > curLength)",
            "    throw outOfRange();",
            "if (curLength == maxSize)",
            "    resize();",
        ]
        codes_2 = [
            "for (int j = curLength; j > i; --j)",
            "    data[j] = data[j - 1];",
            "data[i] = value;",
            "++curLength;",
        ]
        codes_mob_1 = VGroup(
            *[
                CodeLine_seq_traverse(code) for code in codes_1
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_1.next_to(tex_bg_1.get_top(), DOWN, buff=0.2).shift(LEFT*0.7)
        codes_mob_2 = VGroup(
            *[
                CodeLine_seq_traverse(code) for code in codes_2
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob_2.next_to(tex_bg_2.get_top(), DOWN, buff=0.2)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # join
        self.add(group_rectangle, number, params)
        self.add(tex_bg_1, tex_bg_2, method, codes_mob_1, codes_mob_2)
        self.wait()

        # show 1
        reveal = Rectangle(height=0.5, width=0.5,
                           opacity=0, fill_color=GOLD, stroke_color=GOLD)
        reveal.move_to(maxSize_value)
        self.play(ShowCreation(reveal))
        self.wait(0.5)
        self.play(FadeOut(reveal))
        self.wait()
        method_trans = CodeLine_seq_traverse(
            "insert(1,10)", size=0.8).to_corner(UP, buff=0.3)
        self.play(Transform(method, method_trans))
        self.wait()
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob_1[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans = CodeLine("if (i < 0 || i > 4)", size=0.6).move_to(
            codes_mob_1[0], aligned_edge=LEFT)
        codes_mob_tmp = codes_mob_1[0].copy()
        self.play(Transform(codes_mob_1[0], codes_mob_trans),
                  foot_line.set_length, 3.2, foot_line.shift, LEFT*0.65)
        self.wait()

        # show 2
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.2)
        foot_line.next_to(codes_mob_1[2], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line), Transform(
            codes_mob_1[0], codes_mob_tmp))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.5)
        foot_line.next_to(codes_mob_1[3], DOWN, buff=0.1).shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        all_left = VGroup(params, group_rectangle, number)
        self.play(all_left.shift, LEFT*1.3)
        self.wait()
        group_rectangle_cp = group_rectangle.copy()
        group_rectangle_cp.next_to(group_rectangle, RIGHT, buff=0)
        maxSize_value_change = TextMobject("8", color=BLUE)
        maxSize_value_change.next_to(maxSize, RIGHT)
        self.play(ShowCreation(group_rectangle_cp), Transform(
            maxSize_value, maxSize_value_change))
        self.wait()

        # show 3
        self.play(FadeOut(foot_line))
        foot_line.set_length(5.8)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_1 = CodeLine("for (int j = 4; 4 > 1; --j)", size=0.6).move_to(
            codes_mob_2[0], aligned_edge=LEFT)
        circle_old = codes_mob_2[0].copy()
        self.play(Transform(codes_mob_2[0], circle_1),
                  foot_line.set_length, 4.5, foot_line.shift, LEFT*0.65)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.7)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_1 = CodeLine("    data[4] = data[3];", size=0.6).move_to(
            codes_mob_2[1], aligned_edge=LEFT)
        clc_old = codes_mob_2[1].copy()
        self.play(Transform(codes_mob_2[1], clc_1),
                  foot_line.set_length, 3, foot_line.shift, LEFT*0.35)
        self.wait()
        rectangle_filling.move_to(number_3).shift(RIGHT*0.8)
        number_3_cp = number_3.copy()
        self.play(FadeIn(rectangle_filling))
        self.wait()
        self.play(number_3_cp.shift, RIGHT*0.8)
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_2 = CodeLine("for (int j = 4; 3 > 1; --j)", size=0.6).move_to(
            codes_mob_2[0], aligned_edge=LEFT)
        self.play(Transform(codes_mob_2[0], circle_2))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_2 = CodeLine("    data[3] = data[2];", size=0.6).move_to(
            codes_mob_2[1], aligned_edge=LEFT)
        self.play(Transform(codes_mob_2[1], clc_2))
        self.wait()
        self.play(rectangle_filling.shift, LEFT*0.8)
        self.wait()
        number_2_cp = number_2.copy()
        self.play(number_2_cp.shift, RIGHT*0.8, FadeOut(number_3))
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_3 = CodeLine("for (int j = 4; 2 > 1; --j)", size=0.6).move_to(
            codes_mob_2[0], aligned_edge=LEFT)
        self.play(Transform(codes_mob_2[0], circle_3))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3)
        foot_line.next_to(codes_mob_2[1], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_3 = CodeLine("    data[2] = data[1];", size=0.6).move_to(
            codes_mob_2[1], aligned_edge=LEFT)
        self.play(Transform(codes_mob_2[1], clc_3))
        self.wait()
        self.play(rectangle_filling.shift, LEFT*0.8)
        self.wait()
        number_1_cp = number_1.copy()
        self.play(number_1_cp.shift, RIGHT*0.8, FadeOut(number_2))
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob_2[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_4 = CodeLine("for (int j = 4; 1 > 1; --j)", size=0.6).move_to(
            codes_mob_2[0], aligned_edge=LEFT)
        self.play(Transform(codes_mob_2[0], circle_4))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.8)
        foot_line.next_to(codes_mob_2[2], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line), Transform(
            codes_mob_2[0], circle_old), Transform(codes_mob_2[1], clc_old))
        self.wait()
        circle_last = CodeLine("data[1] = 10;", size=0.6).move_to(
            codes_mob_2[2], aligned_edge=LEFT)
        circle_last_old = codes_mob_2[2].copy()
        self.play(Transform(codes_mob_2[2], circle_last),
                  foot_line.set_length, 2.2, foot_line.shift, LEFT*0.25)
        self.wait()
        self.play(rectangle_filling.shift, LEFT*0.8)
        self.wait()
        number_10 = TextMobject("10", color=BLACK)
        number_10.scale(1)
        number_10.move_to(rectangle_1)
        self.play(Transform(number_1, number_10))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.1)
        foot_line.next_to(codes_mob_2[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line), Transform(
            codes_mob_2[2], circle_last_old))
        self.wait()
        curLength_value5 = TextMobject("5", color=BLUE)
        curLength_value5.next_to(curLength, RIGHT)
        self.play(Transform(curLength_value, curLength_value5))
        self.play(FadeOut(rectangle_filling))


class DepartmentDetails_seq_remove(Scene_):

    def construct(self):
        # List
        rectangle_0 = Rectangle(height=0.8, width=0.8,
                                opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_filling = rectangle_0.copy()
        rectangle_filling.set_opacity(0.5).set_color(
            BLUE).set_height(0.75).set_width(0.75)
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
        number_0.scale(1)
        number_1.scale(1)
        number_2.scale(1)
        number_3.scale(1)
        number_0.move_to(rectangle_0)
        number_1.move_to(rectangle_1)
        number_2.move_to(rectangle_2)
        number_3.move_to(rectangle_3)
        number = VGroup(number_0, number_1, number_2, number_3)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params_1 = VGroup(curLength, curLength_value)
        maxSize = TextMobject("maxSize = ", color=BLACK)
        maxSize.scale(0.7)
        maxSize_value = TextMobject("10", color=BLUE)
        maxSize_value.next_to(maxSize, RIGHT)
        params_2 = VGroup(maxSize, maxSize_value)
        params_2.next_to(params_1, DOWN, buff=0.5)
        params = VGroup(params_1, params_2)
        params.next_to(rectangle_0, LEFT, buff=1.5)

        # All
        All = VGroup(group_rectangle, number, params)
        All.shift(DOWN*1.3+RIGHT*0.5)

        # Code block
        tex_bg = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                  fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg.set_height(3.1, stretch=True).set_width(8, stretch=True)
        tex_bg.to_corner(UP*2)
        method = CodeLine("remove(int i)",
                          size=0.8).to_corner(UP, buff=0.3)
        codes = [
            "if (i < 0 || i > curLength)",
            "    throw outOfRange();",
            "for (int j = i; j < curLength - 1; ++j)",
            "    data[j] = data[j + 1];",
            "--curLength;",
        ]
        codes_mob = VGroup(
            *[
                CodeLine(code) for code in codes
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob.next_to(tex_bg.get_top(), DOWN, buff=0.2)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # join
        self.add(group_rectangle, number, params)
        self.add(tex_bg, method, codes_mob)
        self.wait()

        # show 1
        method_trans = CodeLine(
            "remove(1)", size=0.8).to_corner(UP, buff=0.3)
        self.play(Transform(method, method_trans))
        self.wait()
        foot_line.set_length(5.2)
        foot_line.next_to(codes_mob[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans = CodeLine("if (i < 0 || i > 4)", size=0.7).move_to(
            codes_mob[0], aligned_edge=LEFT)
        codes_mob_tmp = codes_mob[0].copy()
        self.play(Transform(codes_mob[0], codes_mob_trans),
                  foot_line.set_length, 3.8, foot_line.shift, LEFT*0.8)
        self.wait()

        # show 2
        self.play(FadeOut(foot_line))
        foot_line.set_length(7.5)
        foot_line.next_to(codes_mob[2], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line),
                  Transform(codes_mob[0], codes_mob_tmp))
        self.wait()
        circle_1 = CodeLine("for (int j = 1; 1 < 3; ++j)", size=0.7).move_to(
            codes_mob[2], aligned_edge=LEFT)
        circle_old = codes_mob[2].copy()
        self.play(Transform(codes_mob[2], circle_1),
                  foot_line.set_length, 5.3, foot_line.shift, LEFT*1.15)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.2)
        foot_line.next_to(codes_mob[3], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_1 = CodeLine("    data[1] = data[2];", size=0.7).move_to(
            codes_mob[3], aligned_edge=LEFT)
        clc_old = codes_mob[3].copy()
        self.play(Transform(codes_mob[3], clc_1),
                  foot_line.set_length, 3.5, foot_line.shift, LEFT*0.33)
        self.wait()
        rectangle_filling.move_to(number_1)
        number_2_cp = number_2.copy()
        self.play(FadeIn(rectangle_filling))
        self.wait()
        self.play(number_2_cp.shift, LEFT*0.8, FadeOut(number_1))
        self.play(FadeOut(foot_line))
        foot_line.set_length(5.3)
        foot_line.next_to(codes_mob[2], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_2 = CodeLine("for (int j = 1; 2 < 3; ++j)", size=0.7).move_to(
            codes_mob[2], aligned_edge=LEFT)
        self.play(Transform(codes_mob[2], circle_2))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(3.5)
        foot_line.next_to(codes_mob[3], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_2 = CodeLine("    data[2] = data[3];", size=0.7).move_to(
            codes_mob[3], aligned_edge=LEFT)
        self.play(Transform(codes_mob[3], clc_2))
        self.wait()
        number_3_cp = number_3.copy()
        self.play(rectangle_filling.shift, RIGHT*0.8)
        self.wait()
        self.play(number_3_cp.shift, LEFT*0.8, FadeOut(number_2))
        self.play(FadeOut(foot_line))
        foot_line.set_length(5.3)
        foot_line.next_to(codes_mob[2], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_3 = CodeLine("for (int j = 1; 3 < 3; ++j)", size=0.7).move_to(
            codes_mob[2], aligned_edge=LEFT)
        self.play(Transform(codes_mob[2], circle_3))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.5)
        foot_line.next_to(codes_mob[4], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line), Transform(codes_mob[2], circle_old), Transform(
            codes_mob[3], clc_old), FadeOut(rectangle_filling))
        self.wait()
        curLength_value5 = TextMobject("3", color=BLUE)
        curLength_value5.next_to(curLength, RIGHT)
        self.play(Transform(curLength_value, curLength_value5))


class DepartmentDetails_seq_search(Scene_):

    def construct(self):
        # List
        rectangle_0 = Rectangle(height=0.8, width=0.8,
                                opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_filling = rectangle_0.copy()
        rectangle_filling.set_opacity(0.5).set_color(
            BLUE).set_height(0.75).set_width(0.75)
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
        number_0.scale(1)
        number_1.scale(1)
        number_2.scale(1)
        number_3.scale(1)
        number_0.move_to(rectangle_0)
        number_1.move_to(rectangle_1)
        number_2.move_to(rectangle_2)
        number_3.move_to(rectangle_3)
        number = VGroup(number_0, number_1, number_2, number_3)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params_1 = VGroup(curLength, curLength_value)
        maxSize = TextMobject("maxSize = ", color=BLACK)
        maxSize.scale(0.7)
        maxSize_value = TextMobject("10", color=BLUE)
        maxSize_value.next_to(maxSize, RIGHT)
        params_2 = VGroup(maxSize, maxSize_value)
        params_2.next_to(params_1, DOWN, buff=0.5)
        params = VGroup(params_1, params_2)
        params.next_to(rectangle_0, LEFT, buff=1.5)

        # All
        All = VGroup(group_rectangle, number, params)
        All.shift(DOWN*1.3+RIGHT*0.5)

        # Code block
        tex_bg = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                  fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg.set_height(2.4, stretch=True).set_width(7, stretch=True)
        tex_bg.to_corner(UP*2)
        method = CodeLine("search(const elemType &value)",
                          size=0.8).to_corner(UP, buff=0.3)
        codes = [
            "for (int i = 0; i < curLength; ++i)",
            "    if (value == data[i])",
            "        return i;",
            "return -1;",
        ]
        codes_mob = VGroup(
            *[
                CodeLine(code) for code in codes
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob.next_to(tex_bg.get_top(), DOWN, buff=0.2)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # join
        self.add(group_rectangle, number, params)
        self.add(tex_bg, method, codes_mob)
        self.wait()

        # show 1
        method_trans = CodeLine(
            "search(1)", size=0.8).to_corner(UP, buff=0.3)
        self.play(Transform(method, method_trans))
        self.wait()
        foot_line.set_length(6.8)
        foot_line.next_to(codes_mob[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()

        # show 2
        circle_1 = CodeLine("for (int i = 0; 0 < 4; ++i)", size=0.7).move_to(
            codes_mob[0], aligned_edge=LEFT)
        circle_old = codes_mob[0].copy()
        self.play(Transform(codes_mob[0], circle_1),
                  foot_line.set_length, 5.2, foot_line.shift, LEFT*0.8)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.2)
        foot_line.next_to(codes_mob[1], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.36)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_1 = CodeLine("    if (1 == 0)", size=0.7).move_to(
            codes_mob[1], aligned_edge=LEFT)
        clc_old = codes_mob[1].copy()
        self.play(Transform(codes_mob[1], clc_1),
                  foot_line.set_length, 2.2, foot_line.shift, LEFT*0.95)
        self.wait()
        rectangle_filling.move_to(number_0)
        self.play(FadeIn(rectangle_filling))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(5.2)
        foot_line.next_to(codes_mob[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_2 = CodeLine("for (int i = 0; 1 < 4; ++i)", size=0.7).move_to(
            codes_mob[0], aligned_edge=LEFT)
        self.play(Transform(codes_mob[0], circle_2))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.2)
        foot_line.next_to(codes_mob[1], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.36)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_2 = CodeLine("    if (1 == 1)", size=0.7).move_to(
            codes_mob[1], aligned_edge=LEFT)
        self.play(Transform(codes_mob[1], clc_2))
        self.wait()
        self.play(rectangle_filling.shift, RIGHT*0.8)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.8)
        foot_line.next_to(codes_mob[2], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.7)
        self.play(GrowFromCenter(foot_line), Transform(codes_mob[0], circle_old), Transform(
            codes_mob[1], clc_old))
        self.wait()
        c3 = CodeLine("        return 1;", size=0.7).move_to(
            codes_mob[2], aligned_edge=LEFT)
        self.play(Transform(codes_mob[2], c3))
        self.wait()


class DepartmentDetails_seq_visit(Scene_):

    def construct(self):
        # List
        rectangle_0 = Rectangle(height=0.8, width=0.8,
                                opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_filling = rectangle_0.copy()
        rectangle_filling.set_opacity(0.5).set_color(
            BLUE).set_height(0.75).set_width(0.75)
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
        number_0.scale(1)
        number_1.scale(1)
        number_2.scale(1)
        number_3.scale(1)
        number_0.move_to(rectangle_0)
        number_1.move_to(rectangle_1)
        number_2.move_to(rectangle_2)
        number_3.move_to(rectangle_3)
        number = VGroup(number_0, number_1, number_2, number_3)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params_1 = VGroup(curLength, curLength_value)
        maxSize = TextMobject("maxSize = ", color=BLACK)
        maxSize.scale(0.7)
        maxSize_value = TextMobject("10", color=BLUE)
        maxSize_value.next_to(maxSize, RIGHT)
        params_2 = VGroup(maxSize, maxSize_value)
        params_2.next_to(params_1, DOWN, buff=0.5)
        params = VGroup(params_1, params_2)
        params.next_to(rectangle_0, LEFT, buff=1.5)

        # All
        All = VGroup(group_rectangle, number, params)
        All.shift(DOWN*1.3+RIGHT*0.5)

        # Code block
        tex_bg = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                  fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg.set_height(2, stretch=True).set_width(6.3, stretch=True)
        tex_bg.to_corner(UP*2)
        method = CodeLine("visit(int i)",
                          size=0.8).to_corner(UP, buff=0.3)
        codes = [
            "if (i < 0 || i > curLength)",
            "    throw outOfRange();",
            "return data[i];",
        ]
        codes_mob = VGroup(
            *[
                CodeLine(code) for code in codes
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob.next_to(tex_bg.get_top(), DOWN, buff=0.2)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # join
        self.add(group_rectangle, number, params)
        self.add(tex_bg, method, codes_mob)
        self.wait()

        # show 1
        method_trans = CodeLine(
            "visit(1)", size=0.8).to_corner(UP, buff=0.3)
        self.play(Transform(method, method_trans))
        self.wait()
        foot_line.set_length(5.3)
        foot_line.next_to(codes_mob[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_mob_trans = CodeLine("if (i < 0 || i > 4)", size=0.7).move_to(
            codes_mob[0], aligned_edge=LEFT)
        codes_mob_tmp = codes_mob[0].copy()
        self.play(Transform(codes_mob[0], codes_mob_trans),
                  foot_line.set_length, 3.7, foot_line.shift, LEFT*0.75)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.9)
        foot_line.next_to(codes_mob[2], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line),
                  Transform(codes_mob[0], codes_mob_tmp))
        self.wait()
        codes_mob_last = CodeLine("return 1;", size=0.7).move_to(
            codes_mob[2], aligned_edge=LEFT)
        rectangle_filling.move_to(number_1)
        self.play(Transform(codes_mob[2], codes_mob_last),
                  foot_line.set_length, 1.7, foot_line.shift, LEFT*0.6, FadeIn(rectangle_filling))


class DepartmentDetails_seq_inverse(Scene_):

    def construct(self):
        # List
        rectangle_0 = Rectangle(height=0.8, width=0.8,
                                opacity=0, fill_color=BLACK, stroke_color=BLACK)
        rectangle_filling = rectangle_0.copy()
        rectangle_filling.set_opacity(0.5).set_color(
            BLUE).set_height(0.75).set_width(0.75)
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
        number_0.scale(1)
        number_1.scale(1)
        number_2.scale(1)
        number_3.scale(1)
        number_0.move_to(rectangle_0)
        number_1.move_to(rectangle_1)
        number_2.move_to(rectangle_2)
        number_3.move_to(rectangle_3)
        number = VGroup(number_0, number_1, number_2, number_3)

        # params
        curLength = TextMobject("curLength = ", color=BLACK)
        curLength.scale(0.7)
        curLength_value = TextMobject("4", color=BLUE)
        curLength_value.next_to(curLength, RIGHT)
        params_1 = VGroup(curLength, curLength_value)
        maxSize = TextMobject("maxSize = ", color=BLACK)
        maxSize.scale(0.7)
        maxSize_value = TextMobject("10", color=BLUE)
        maxSize_value.next_to(maxSize, RIGHT)
        params_2 = VGroup(maxSize, maxSize_value)
        params_2.next_to(params_1, DOWN, buff=0.5)
        params = VGroup(params_1, params_2)
        params.next_to(rectangle_0, LEFT, buff=1.5)

        # All
        All = VGroup(group_rectangle, number, params)
        All.shift(DOWN*1.3+RIGHT*0.5)

        # Code block
        tex_bg = RoundedRectangle(stroke_width=1, stroke_color=GRAY,
                                  fill_color="#EBEBEB", fill_opacity=0.95, plot_depth=-1, corner_radius=0.05, sheen_factor=0.1, sheen_direction=UR)
        tex_bg.set_height(3.2, stretch=True).set_width(7, stretch=True)
        tex_bg.to_corner(UP*2)
        method = CodeLine_seq_traverse("inverse()",
                                       size=0.8).to_corner(UP, buff=0.3)
        codes = [
            "elemType tmp;",
            "for (int i = 0; i < curLength / 2; ++i) {",
            "    tmp = data[i];",
            "    data[i] = data[curLength - 1 - i];",
            "    data[curLength - 1 - i] = tmp;",
            "}",
        ]
        codes_mob = VGroup(
            *[
                CodeLine_seq_traverse(code) for code in codes
            ]
        ).arrange(DOWN, aligned_edge=LEFT)
        codes_mob.next_to(tex_bg.get_top(), DOWN, buff=0.2)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # join
        self.add(group_rectangle, number, params)
        self.add(tex_bg, method, codes_mob)
        self.wait()

        # show 1
        foot_line.set_length(2.2)
        foot_line.next_to(codes_mob[0], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        up_up = VGroup(group_rectangle, number)
        tmp = TextMobject("tmp", color=BLACK)
        tmp.scale(0.7)
        tmp.next_to(group_rectangle, DOWN*0.35)
        self.play(up_up.shift, UP*0.4, FadeInFrom(tmp, direction=DOWN))

        # show 2
        self.play(FadeOut(foot_line))
        foot_line.set_length(6.4)
        foot_line.next_to(codes_mob[1], DOWN, buff=0.1).shift(LEFT*0.15)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_1 = CodeLine("for (int i = 0; 0 < 2; ++i) {", size=0.6).move_to(
            codes_mob[1], aligned_edge=LEFT)
        circle_old = codes_mob[1].copy()
        self.play(Transform(codes_mob[1], circle_1),
                  foot_line.set_length, 4.5, foot_line.shift, LEFT)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.4)
        foot_line.next_to(codes_mob[2], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_1 = CodeLine("    tmp = data[0];", size=0.6).move_to(
            codes_mob[2], aligned_edge=LEFT)
        clc_old = codes_mob[2].copy()
        self.play(Transform(codes_mob[2], clc_1))
        self.wait()
        rectangle_filling.move_to(number_0)
        self.play(FadeIn(rectangle_filling))
        self.wait()
        tmp_s = TextMobject("tmp = ", color=BLACK)
        tmp_s.scale(0.7).next_to(tmp, aligned_edge=LEFT).shift(LEFT)
        number_0_cp = number_0.copy()
        tmp_v = number_0.copy()
        tmp_v.next_to(tmp_s, RIGHT)
        self.play(ReplacementTransform(tmp, tmp_s),
                  Transform(number_0_cp, tmp_v))
        self.play(FadeOut(foot_line))
        foot_line.set_length(5.6)
        foot_line.next_to(codes_mob[3], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        cl_1 = CodeLine("    data[0] = data[3];", size=0.6).move_to(
            codes_mob[3], aligned_edge=LEFT)
        cl_old = codes_mob[3].copy()
        self.play(Transform(codes_mob[3], cl_1),
                  foot_line.set_length, 3, foot_line.shift, LEFT*1.35)
        self.wait()
        number_3_cp = number_3.copy()
        self.play(number_3_cp.shift, LEFT*2.4, FadeOut(number_0))
        self.play(FadeOut(foot_line))
        foot_line.set_length(5)
        foot_line.next_to(codes_mob[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        c_1 = CodeLine("    data[3] = tmp;", size=0.6).move_to(
            codes_mob[4], aligned_edge=LEFT)
        c_old = codes_mob[4].copy()
        self.play(Transform(codes_mob[4], c_1),
                  foot_line.set_length, 2.3, foot_line.shift, LEFT*1.35)
        self.wait()
        number_0_fly = number_0_cp.copy()
        self.play(rectangle_filling.shift, RIGHT*2.4)
        self.wait()
        self.play(FadeOut(number_3), number_0_fly.move_to, number_3)
        self.wait()

        # show 3
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob[1], DOWN, buff=0.1).shift(LEFT*0.15)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_2 = CodeLine("for (int i = 0; 1 < 2; ++i) {", size=0.6).move_to(
            codes_mob[1], aligned_edge=LEFT)
        self.play(Transform(codes_mob[1], circle_2))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.4)
        foot_line.next_to(codes_mob[2], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_2 = CodeLine("    tmp = data[1];", size=0.6).move_to(
            codes_mob[2], aligned_edge=LEFT)
        self.play(Transform(codes_mob[2], clc_2))
        self.wait()
        self.play(rectangle_filling.shift, LEFT*1.6)
        self.wait()
        number_1_cp = number_1.copy()
        self.play(number_1_cp.move_to, number_0_cp, FadeOut(number_0_cp))
        self.play(FadeOut(foot_line))
        foot_line.set_length(3)
        foot_line.next_to(codes_mob[3], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        cl_2 = CodeLine("    data[1] = data[2];", size=0.6).move_to(
            codes_mob[3], aligned_edge=LEFT)
        self.play(Transform(codes_mob[3], cl_2))
        self.wait()
        number_2_cp = number_2.copy()
        self.play(number_2_cp.shift, LEFT*0.8, FadeOut(number_1))
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.3)
        foot_line.next_to(codes_mob[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT*0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        c_3 = CodeLine("    data[2] = tmp;", size=0.6).move_to(
            codes_mob[4], aligned_edge=LEFT)
        self.play(Transform(codes_mob[4], c_3))
        self.wait()
        number_1_fly = number_1_cp.copy()
        self.play(rectangle_filling.shift, RIGHT*0.8)
        self.wait()
        self.play(FadeOut(number_2), number_1_fly.move_to, number_2)

        # show 4
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob[1], DOWN, buff=0.1).shift(LEFT*0.15)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_3 = CodeLine("for (int i = 0; 2 < 2; ++i) {", size=0.6).move_to(
            codes_mob[1], aligned_edge=LEFT)
        self.play(Transform(codes_mob[1], circle_3))
        self.wait()
        fly = VGroup(number_0_fly, number_1_fly, number_2_cp,
                     number_3_cp, group_rectangle)
        self.play(FadeOut(foot_line), Transform(codes_mob[1], circle_old), Transform(codes_mob[2], clc_old), Transform(codes_mob[3], cl_old),
                  Transform(codes_mob[4], c_old), FadeOut(rectangle_filling), FadeOut(tmp_s), FadeOut(number_1_cp), fly.shift, DOWN*0.5)


class Imitate(Scene):
    def construct(self):
        demo = TextMobject("李蓝骏")
        demo2 = TextMobject("最帅啦！")
        text = Text("中文测试", font="思源宋体 Heavy").shift(DOWN)
        text2 = Text("中文测试", font="思源黑体 CN Bold").shift(DOWN*1.5)
        vg = VGroup(demo, demo2)
        vg.scale(2.5)

        self.add(demo)
        self.wait()
        self.play(Transform(demo, demo2))
        self.play(Write(text), Write(text2))


class CourserLi(Scene):
    def construct(self):

        # LOVE
        circle01 = Circle(color=RED, fill_color=RED, fill_opacity=0.5)
        circle02 = Circle(color=RED, fill_color=RED, fill_opacity=0.5)
        square01 = Square(color=RED, fill_color=RED, fill_opacity=0.5)
        love = VGroup(circle01, circle02, square01)

        # Death
        rec01 = Rectangle(height=0.8, width=4,
                          fill_color=RED, color=RED, fill_opacity=0.5)
        rec02 = Rectangle(height=0.8, width=4,
                          fill_color=RED, color=RED, fill_opacity=0.5)
        death = VGroup(rec01, rec02)

        # Robots
        square02 = Square(color=RED, fill_color=RED, fill_opacity=0.5)
        square02.scale(1.6)
        c01 = Circle(color=RED, fill_color=BLACK, fill_opacity=0.5)
        c02 = Circle(color=RED, fill_color=BLACK, fill_opacity=0.5)
        c01.scale(0.45)
        c02.scale(0.45)
        robots = VGroup(square02, c01, c02)

        # Line
        line = Line(np.array([-6, -2.4, 0]), np.array([6, -2.4, 0]), color=RED)
        line.set_height(0.2)

        # Text
        text = TextMobject("LOVE\nDEATH\n\&\nROBOTS", color=RED)
        text.scale(1.8)

        group_three = VGroup(love, death, robots)
        group_all = VGroup(love, death, robots, line, text)

        # ME
        me = TextMobject("筱团", color=RED, buff=0.1)
        me.scale(1.2)

        # Position
        circle01.shift((UP+LEFT)*np.sqrt(2)/2)
        circle02.shift((UP+RIGHT)*np.sqrt(2)/2)
        square01.rotate(np.pi/4)

        rec01.rotate(np.pi/4)
        rec02.rotate(-np.pi/4)

        c01.shift(np.array([-0.72, 0.6, 0]))
        c02.shift(np.array([0.72, 0.6, 0]))
        robots.shift(RIGHT*4)

        text.shift(DOWN*2.5)

        me.next_to(group_all, DOWN)

        # Show
        self.play(ShowCreation(circle01), ShowCreation(
            circle02), ShowCreation(square01))
        self.wait()
        self.play(ApplyMethod(love.shift, LEFT*4))
        self.wait()
        self.play(ShowCreation(rec01), ShowCreation(rec02))
        self.wait()
        self.play(ShowCreation(square02))
        self.play(ShowCreation(c01), ShowCreation(c02))
        self.wait()
        self.play(ApplyMethod(group_three.set_opacity, 1))
        self.wait()
        self.play(ShowCreation(line))
        self.wait()
        self.play(Transform(line, text))
        self.wait()
        self.play(ApplyMethod(group_all.shift, UP*0.5), Write(me))


class ExampleTikz(Scene):

    def construct(self):
        #测试用例
        pass
