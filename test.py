from manimlib import *
from manimlib.imports import *
from manim_sandbox.utils.imports import *
import math


class Scene_(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "use_plot_depth": True,
        }
    }


class groups2(Scene_):
    def construct(self):
        t2c = {"团子": BLUE, "七金": RED, "呗": "#801dae"}
        a = Text("爱吃团子的七金呗", font="江西拙楷", color=GOLD, t2c=t2c).scale(3)
        b = Text("ZhuKe Security Origin",
                 font="ZCOOL Addict Italic 01",
                 color="#3d3b4f").scale(1 * 1.5).move_to(a).shift(DOWN * 1.5)
        c = Text("ZSO", font="GenKaimincho",
                 color="#3d3b4f").scale(1.25 * 1.5).move_to(b)
        self.play(WriteRandom(a), run_time=1.5)
        self.play(a.shift, UP * 0.25)
        self.play(FadeIn(b), run_time=1)
        self.wait()
        self.play(ReplacementTransform(b, c))
        self.wait()


class tt1(Scene):
    def construct(self):
        a_vect = Arrow(1 * LEFT, 2 * UP, color=RED, stroke_width=0.3)
        b_vect = Arrow(1 * LEFT, 2 * RIGHT, color=RED, stroke_width=1.3)
        c_vect = Arrow(1 * LEFT, 2 * DOWN, color=RED, stroke_width=13)
        self.play(GrowArrow(a_vect))
        self.play(GrowArrow(b_vect))
        self.play(GrowArrow(c_vect))
        self.wait()


class tt2(Scene):
    def construct(self):
        # arrow = SVGMobject(r"D:\manim\ba.svg", color=BLACK).scale(0.2)
        mur = SVGMobject(
            r"D:\manim\manim_sandbox\videos\manimTutorial\part1_Mobjectmethod\emote_01.svg",
            color=BLACK).scale(0.2)

        self.add(mur)
        self.wait()


class tt3(Scene):
    CONFIG = {
        "camera_config": {
            "background_image": "2.png",
        },
    }

    def construct(self):
        a = Text("123")
        self.add(a)
        self.wait()


class tt4(Scene_):
    def construct(self):
        title1 = TextMobject("数据结构", color=BLACK).scale(2).shift(
            UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("算法模拟动画", color=BLACK).scale(1.3).shift(
            DOWN * 0.5).to_edge(RIGHT)
        title3 = TextMobject("Chapter 1", color=BLACK).scale(2).shift(
            UP * 0.5).to_edge(LEFT)
        title4 = TextMobject("顺序表算法演示", color=BLACK).scale(1.3).shift(
            DOWN * 0.5).to_edge(RIGHT)
        title2[0][:6].set_color("#ff2d51")
        title4[0][:3].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([-obj.get_center()[0] * dt * 2, 0, 0]))

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
        self.play(title1.shift, UP * 5, title1.scale, 0.5, title2.shift,
                  DOWN * 5, title2.scale, 0.5)
        self.wait()
        title = VGroup(title3, title4)
        self.play(FadeOutRandom(title))


class tt5(Scene_):
    def construct(self):
        title1 = TextMobject("Chapter 2", color=BLACK).scale(2).shift(
            UP * 0.5).to_edge(LEFT)
        title2 = TextMobject("单链表算法演示", color=BLACK).scale(1.3).shift(
            DOWN * 0.5).to_edge(RIGHT)
        title2[0][:3].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([-obj.get_center()[0] * dt * 2, 0, 0]))

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


class tt6(Scene_):
    def construct(self):
        t2c = {"KMP": ORANGE, "数据结构": "#44cef6"}
        text_color = DARK_GRAY

        font = "庞门正道标题体"
        text_1 = Text("算法模拟动画", font=font, color=text_color, size=1,
                      t2c=t2c).scale(2.25).to_edge(UP * 3, buff=1)
        text_2 = Text("KMP算法演示", font=font, color=text_color, size=1,
                      t2c=t2c).scale(2.25).to_edge(UP * 4.2, buff=1)
        text_all = VGroup(text_1, text_2)

        self.wait(0.5)
        self.play(Write(text_all), run_time=1)
        self.play(FadeOut(text_all))


class tt7(Scene_):
    def construct(self):
        # List
        rectangle_front = Rectangle(height=0.5,
                                    width=0.5,
                                    opacity=0,
                                    fill_color=BLACK,
                                    stroke_color=BLACK)
        rectangle_later = rectangle_front.copy()
        rectangle_later.next_to(rectangle_front, RIGHT, buff=0)
        rectangle_front_filling = rectangle_front.copy()
        rectangle_front_filling.set_opacity(0.5).set_color(BLUE).set_height(
            0.45).set_width(0.45)
        group_rectangle_0 = VGroup(rectangle_front, rectangle_later)
        group_rectangle_1 = group_rectangle_0.copy()
        group_rectangle_2 = group_rectangle_0.copy()
        group_rectangle_3 = group_rectangle_0.copy()
        group_rectangle_1.next_to(group_rectangle_0, RIGHT, buff=0.65)
        group_rectangle_2.next_to(group_rectangle_1, RIGHT, buff=0.65)
        group_rectangle_3.next_to(group_rectangle_2, RIGHT, buff=0.65)
        group_rectangle = VGroup(group_rectangle_0, group_rectangle_1,
                                 group_rectangle_2, group_rectangle_3)

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
        number_0.shift(RIGHT * 0.58)
        number_1.next_to(group_rectangle_1, LEFT)
        number_1.shift(RIGHT * 0.58)
        number_2.next_to(group_rectangle_2, LEFT)
        number_2.shift(RIGHT * 0.58)
        number_3.next_to(group_rectangle_3, LEFT)
        number_3.shift(RIGHT * 0.58)
        number = VGroup(number_0, number_1, number_2, number_3)

        # arrow_head
        vec_head = Arrow(np.array([0, 1, 0]),
                         np.array([0, -1, 0]),
                         buff=0.6,
                         color=BLACK)
        vec_head.scale(0.5)
        vec_head.next_to(group_rectangle_0, UP, buff=0.1)
        vec_head.shift(LEFT * 0.25)

        # arrow_tail
        vec_tail = vec_head.copy()
        vec_tail.next_to(group_rectangle_3, UP, buff=0.1)
        vec_tail.shift(LEFT * 0.25)

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
        vec_list_0.shift(LEFT * 0.3)
        vec_list_1.shift(LEFT * 0.3)
        vec_list_2.shift(LEFT * 0.3)
        vec_list_3.shift(LEFT * 0.3)
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
        All = VGroup(group_rectangle, vec_head, vec_tail,
                     rectangle_front_filling, arc_tran, vec_list, text, number,
                     params)
        All.shift(LEFT * 2.5 + DOWN * 2)

        # Code block
        tex_bg_1 = RoundedRectangle(stroke_width=1,
                                    stroke_color=GRAY,
                                    fill_color="#EBEBEB",
                                    fill_opacity=0.95,
                                    plot_depth=-1,
                                    corner_radius=0.05,
                                    sheen_factor=0.1,
                                    sheen_direction=UR)
        tex_bg_1.set_height(3.8, stretch=True).set_width(6, stretch=True)
        tex_bg_2 = tex_bg_1.copy()
        tex_bg_1.to_corner(UP * 1.5 + LEFT * 2.15)
        tex_bg_2.to_corner(UP * 1.5 + RIGHT * 2.15)
        method = CodeLine_func("remove(int i)", font='思源宋体 Heavy',
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
        codes_mob_1 = VGroup(*[CodeLine_remove(code)
                               for code in codes_1]).arrange(DOWN,
                                                             aligned_edge=LEFT)
        codes_mob_1.next_to(tex_bg_1.get_top(), DOWN,
                            buff=0.2).shift(LEFT * 0.6 + UP * 0.1)
        codes_mob_2 = VGroup(*[CodeLine_remove(code)
                               for code in codes_2]).arrange(DOWN,
                                                             aligned_edge=LEFT)
        codes_mob_2.next_to(tex_bg_2.get_top(), DOWN,
                            buff=0.2).shift(LEFT * 1.3 + UP * 0.1)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # Code text
        code_text = CodeLine("p", size=0.5).next_to(tex_bg_1.get_top(),
                                                    DOWN * 0.7 + LEFT * 4.8,
                                                    buff=0.2).shift(LEFT * 0.8)
        code_text_2 = CodeLine("q",
                               size=0.5).next_to(tex_bg_1.get_top(),
                                                 DOWN * 0.7 + LEFT * 1,
                                                 buff=0.2).shift(LEFT * 1.02)
        code_text_3 = CodeLine("getPosition(1)",
                               size=0.5).next_to(tex_bg_1.get_top(),
                                                 DOWN * 7.8,
                                                 buff=0.2).shift(LEFT * 1.22)

        # join
        self.add(tex_bg_1, tex_bg_2)
        # self.add(code_text, code_text_2)
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
        method_trans = CodeLine_func("remove(1)", font='思源宋体 Heavy',
                                     size=0.8).to_corner(UP, buff=0.18)
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
        codes_mob_trans = CodeLine("if (i < 0 || i > 4)",
                                   size=0.5).move_to(codes_mob_1[1],
                                                     aligned_edge=LEFT)
        codes_mob_tmp = codes_mob_1[1].copy()
        self.play(Transform(codes_mob_1[1], codes_mob_trans),
                  foot_line.set_length, 2.65, foot_line.shift, LEFT * 0.82)
        self.wait()

        # show 2
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.7)
        foot_line.next_to(codes_mob_1[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        codes_getPosition = CodeLine("p = getPosition(1);",
                                     size=0.5).move_to(codes_mob_1[3],
                                                       aligned_edge=LEFT)
        codes_getPosition_recover = codes_mob_1[3].copy()
        self.play(Transform(codes_mob_1[3], codes_getPosition))
        self.wait()
        self.play(Transform(code_text_3, rectangle_front_filling),
                  Transform(codes_mob_1[1], codes_mob_tmp),
                  run_time=1.5)
        self.wait()
        vec_tmp = Arrow(np.array([0, -1, 0]),
                        np.array([0, 1, 0]),
                        buff=0.6,
                        color=BLACK)
        vec_tmp.scale(0.5)
        vec_tmp.next_to(group_rectangle_0, DOWN, buff=0.1)
        vec_tmp.shift(LEFT * 0.25)
        self.play(Transform(code_text_3, vec_tmp),
                  ApplyMethod(code_text.next_to, {
                      "mobject_or_point": vec_tmp,
                      "direction": DOWN,
                      "buff": 0.1
                  }),
                  ApplyMethod(code_text_2.shift, LEFT * 0.5),
                  run_time=1.5)
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
        vec_tmp_2.shift(LEFT * 0.25)
        self.play(FadeIn(vec_tmp_2),
                  ApplyMethod(
                      code_text_2.next_to, {
                          "mobject_or_point": vec_tmp_2,
                          "direction": DOWN,
                          "buff": 0.1
                      }),
                  Transform(codes_mob_1[3], codes_getPosition_recover),
                  run_time=1.5)
        move_tmp_2 = VGroup(vec_tmp_2, code_text_2)
        self.wait()

        # show 4
        self.play(FadeOut(foot_line))
        foot_line.set_length(2)
        foot_line.next_to(codes_mob_1[5], DOWN, buff=0.1).shift(LEFT * 0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(0.6)
        foot_line.next_to(codes_mob_2[2], DOWN, buff=0.1).shift(LEFT * 0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.6)
        foot_line.next_to(codes_mob_2[3], DOWN, buff=0.1).shift(RIGHT * 0.25)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        vec_list_1_cp = vec_list_1.copy()
        vec_list_1_cp.set_color(BLUE)
        self.play(ShowCreation(vec_list_1_cp), run_time=1.5)
        self.wait()
        arc_fac = ValueTracker(0.)
        arc_arrow = Arrow(group_rectangle_0.get_center(),
                          group_rectangle_1.get_center() + RIGHT * 1.3,
                          color=BLACK,
                          max_tip_length_to_length_ratio=0.08,
                          max_stroke_width_to_length_ratio=1.5)
        arc_fac.set_value(-2)
        # self.play(ShowCreation(arc_arrow))
        arc_arrow.add_updater(lambda l: l.become(
            Arrow(group_rectangle_0.get_center(),
                  group_rectangle_1.get_center() + RIGHT * 1.3,
                  color=BLACK,
                  max_tip_length_to_length_ratio=0.08,
                  max_stroke_width_to_length_ratio=1.5,
                  path_arc=arc_fac.get_value())))
        self.play(Transform(vec_list_0_cp, arc_arrow),
                  Transform(vec_list_0, arc_arrow))
        self.add(arc_arrow)
        self.play(FadeOut(vec_list_0_cp), FadeOut(vec_list_0),
                  run_time=1)  # 相当于 self.wait()
        # self.play(arc_fac.set_value, 0, rate_func=linear)
        self.wait()

        # show 5
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.3)
        foot_line.next_to(codes_mob_2[4], DOWN, buff=0.1).shift(LEFT * 0.1)
        foot_line.shift(RIGHT * 0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        disappear = VGroup(move_tmp_2, group_rectangle_1, number_1, vec_list_1,
                           vec_list_1_cp)
        self.play(FadeOut(disappear))
        self.wait()
        self.play(arc_fac.set_value, 0, rate_func=linear)
        self.wait()
        move_other = VGroup(text_3, text_2, vec_list_2, vec_list_3, number_2,
                            number_3, group_rectangle_2, group_rectangle_3,
                            vec_tail, vec_list_3)
        self.play(ReplacementTransform(arc_arrow, arc_tran),
                  ApplyMethod(move_other.shift, LEFT * 1.65))
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


class tt8(Scene_):
    def construct(self):
        # List
        rectangle_0 = Rectangle(height=0.8,
                                width=0.8,
                                opacity=0,
                                fill_color=BLACK,
                                stroke_color=BLACK)
        rectangle_filling = rectangle_0.copy()
        rectangle_filling.set_opacity(0.5).set_color(BLUE).set_height(
            0.75).set_width(0.75)
        rectangle_1 = rectangle_0.copy()
        rectangle_2 = rectangle_0.copy()
        rectangle_3 = rectangle_0.copy()
        rectangle_1.next_to(rectangle_0, RIGHT, buff=0)
        rectangle_2.next_to(rectangle_1, RIGHT, buff=0)
        rectangle_3.next_to(rectangle_2, RIGHT, buff=0)
        group_rectangle = VGroup(rectangle_0, rectangle_1, rectangle_2,
                                 rectangle_3)

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
        All.shift(DOWN * 1.3 + RIGHT * 0.5)

        # Code block
        tex_bg = RoundedRectangle(stroke_width=1,
                                  stroke_color=GRAY,
                                  fill_color="#EBEBEB",
                                  fill_opacity=0.95,
                                  plot_depth=-1,
                                  corner_radius=0.05,
                                  sheen_factor=0.1,
                                  sheen_direction=UR)
        tex_bg.set_height(3.2, stretch=True).set_width(6.7, stretch=True)
        tex_bg.to_corner(UP * 2)
        method = CodeLine_func("resize()", size=0.8).to_corner(UP, buff=0.3)
        codes = [
            "elemType *p = data;",
            "maxSize *= 2;",
            "data = new elemType[maxSize];",
            "for (int i = 0; i < curLength; ++i)",
            "    data[i] = p[i];",
            "delete[] p;",
        ]
        codes_mob = VGroup(*[CodeLine_seq_traverse(code)
                             for code in codes]).arrange(DOWN,
                                                         aligned_edge=LEFT)
        codes_mob.next_to(tex_bg.get_top(), DOWN, buff=0.2)
        foot_line = Line(opacity=1, stroke_color=PURPLE_E)

        # join
        self.add(group_rectangle, number, params)
        self.add(tex_bg, method, codes_mob)
        self.wait()

        # show 1
        reveal = Rectangle(height=0.5,
                           width=0.5,
                           opacity=0,
                           fill_color=GOLD,
                           stroke_color=GOLD)
        reveal.move_to(maxSize_value)
        self.play(ShowCreation(reveal))
        self.wait(0.5)
        self.play(FadeOut(reveal))
        foot_line_front = Line(opacity=1, stroke_color=PURPLE_E)
        foot_line_front.put_start_and_end_on(
            codes_mob[0].get_center() + RIGHT * 1.45 + DOWN * 0.25,
            codes_mob[0].get_center() + RIGHT * 0.75 + DOWN * 0.25)
        self.play(ShowCreation(foot_line_front))
        self.wait(0.5)
        seqlist = VGroup(group_rectangle, number)
        self.play(params.shift, LEFT * 0.8, seqlist.shift, RIGHT * 0.8)
        vec_data = Arrow(np.array([-1, 0, 0]),
                         np.array([1, 0, 0]),
                         buff=0.6,
                         color=BLACK)
        vec_data.scale(0.6)
        vec_data.next_to(number_0, LEFT, buff=0.15)
        vec_data.shift(LEFT * 0.25)
        text_data = TextMobject("data", color=BLACK)
        text_data.scale(0.6).next_to(vec_data, LEFT, buff=0.1)
        data = VGroup(vec_data, text_data)
        self.play(FadeInFrom(data, direction=LEFT))
        foot_line_second = foot_line_front.copy()
        foot_line_second.put_start_and_end_on(
            codes_mob[0].get_center() + RIGHT * 0.75 + DOWN * 0.25,
            codes_mob[0].get_center() + LEFT * 1.55 + DOWN * 0.25)
        self.play(ShowCreation(foot_line_second), run_time=1)
        self.wait()
        vec_p = Arrow(np.array([-1, 0, 0]),
                      np.array([1, 0, 0]),
                      buff=0.6,
                      color=BLACK)
        vec_p.scale(0.6)
        vec_p.next_to(number_0, LEFT, buff=0.15)
        vec_p.shift(LEFT * 0.25 + UP * 0.25)
        text_p = TextMobject("p", color=BLACK)
        text_p.scale(0.6).next_to(vec_p, LEFT, buff=0.1)
        p = VGroup(vec_p, text_p)
        self.play(data.shift, DOWN * 0.25)
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
        codes_mob_maxsize = CodeLine("data = new elemType[6];",
                                     size=0.6).move_to(codes_mob[2],
                                                       aligned_edge=LEFT)
        codes_mob_maxsize_cp = codes_mob[2].copy()
        self.play(Transform(codes_mob[2], codes_mob_maxsize),
                  foot_line.set_length, 3.8, foot_line.shift, LEFT * 0.5)
        self.wait()
        self.play(seqlist.shift, UP * 0.5, p.shift, UP * 0.5, data.shift,
                  UP * 0.5)
        self.play(p.shift, DOWN * 0.25, data.shift, DOWN * 1)
        rectangle0 = Rectangle(height=0.8,
                               width=0.8,
                               opacity=0,
                               fill_color=BLACK,
                               stroke_color=BLACK)
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
        group_rectangle_new = VGroup(rectangle0, rectangle1, rectangle2,
                                     rectangle3, rectangle4, rectangle5)
        group_rectangle_new.next_to(vec_data, RIGHT, buff=0.15)
        self.play(ShowCreation(group_rectangle_new))

        # show 3
        self.play(FadeOut(foot_line))
        foot_line.set_length(5.8)
        foot_line.next_to(codes_mob[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line),
                  Transform(codes_mob[2], codes_mob_maxsize_cp))
        self.wait()
        circle_1 = CodeLine("for (int i = 0; 0 < 4; ++i)",
                            size=0.6).move_to(codes_mob[3], aligned_edge=LEFT)
        circle_old = codes_mob[3].copy()  # 为了之后的复原
        self.play(Transform(codes_mob[3], circle_1), foot_line.set_length, 4.5,
                  foot_line.shift, LEFT * 0.65)
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.6)
        foot_line.next_to(codes_mob[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT * 0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_1 = CodeLine("    data[0] = p[0];",
                         size=0.6).move_to(codes_mob[4], aligned_edge=LEFT)
        clc_old = codes_mob[4].copy()  # 为了之后的复原
        self.play(Transform(codes_mob[4], clc_1))
        self.wait()
        #
        rectangle_filling.move_to(number_0)
        number_0_cp = number_0.copy()
        self.play(FadeIn(rectangle_filling))
        self.wait()
        self.play(number_0_cp.shift, DOWN * 1.25 + RIGHT * 0.02)
        #
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_2 = CodeLine("for (int i = 0; 1 < 4; ++i)",
                            size=0.6).move_to(codes_mob[3], aligned_edge=LEFT)
        self.play(Transform(codes_mob[3], circle_2))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.6)
        foot_line.next_to(codes_mob[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT * 0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_2 = CodeLine("    data[1] = p[1];",
                         size=0.6).move_to(codes_mob[4], aligned_edge=LEFT)
        self.play(Transform(codes_mob[4], clc_2))
        self.wait()
        #
        number_1_cp = number_1.copy()
        self.play(rectangle_filling.shift, RIGHT * 0.8)
        self.wait()
        self.play(number_1_cp.shift, DOWN * 1.25 + RIGHT * 0.02)
        #
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_3 = CodeLine("for (int i = 0; 2 < 4; ++i)",
                            size=0.6).move_to(codes_mob[3], aligned_edge=LEFT)
        self.play(Transform(codes_mob[3], circle_3))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.6)
        foot_line.next_to(codes_mob[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT * 0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_3 = CodeLine("    data[2] = p[2];",
                         size=0.6).move_to(codes_mob[4], aligned_edge=LEFT)
        self.play(Transform(codes_mob[4], clc_3))
        self.wait()
        #
        number_2_cp = number_2.copy()
        self.play(rectangle_filling.shift, RIGHT * 0.8)
        self.wait()
        self.play(number_2_cp.shift, DOWN * 1.25 + RIGHT * 0.02)
        #
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_4 = CodeLine("for (int i = 0; 3 < 4; ++i)",
                            size=0.6).move_to(codes_mob[3], aligned_edge=LEFT)
        self.play(Transform(codes_mob[3], circle_4))
        self.wait()
        self.play(FadeOut(foot_line))
        foot_line.set_length(2.6)
        foot_line.next_to(codes_mob[4], DOWN, buff=0.1)
        foot_line.shift(RIGHT * 0.35)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        clc_4 = CodeLine("    data[3] = p[3];",
                         size=0.6).move_to(codes_mob[4], aligned_edge=LEFT)
        self.play(Transform(codes_mob[4], clc_4))
        self.wait()
        #
        number_3_cp = number_3.copy()
        self.play(rectangle_filling.shift, RIGHT * 0.8)
        self.wait()
        self.play(number_3_cp.shift, DOWN * 1.25 + RIGHT * 0.02)
        #
        self.play(FadeOut(foot_line))
        foot_line.set_length(4.5)
        foot_line.next_to(codes_mob[3], DOWN, buff=0.1)
        self.play(GrowFromCenter(foot_line))
        self.wait()
        circle_5 = CodeLine("for (int i = 0; 4 < 4; ++i)",
                            size=0.6).move_to(codes_mob[3], aligned_edge=LEFT)
        self.play(Transform(codes_mob[3], circle_5))
        self.wait()

        # show 4
        self.play(FadeOut(foot_line))
        foot_line.set_length(1.9)
        foot_line.next_to(codes_mob[5], DOWN, buff=0.05)
        self.play(GrowFromCenter(foot_line), Transform(codes_mob[3],
                                                       circle_old),
                  Transform(codes_mob[4], clc_old), FadeOut(rectangle_filling))
        self.wait()
        up_ = VGroup(data, group_rectangle_new, number_0_cp, number_1_cp,
                     number_2_cp, number_3_cp)
        self.play(FadeOut(seqlist), FadeOut(p), up_.shift, UP * 0.75)


class tt9(Scene):
    def construct(self):
        a = Text("123", font='Consolas')

        self.add(a)
        self.wait()


class tt10(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "use_plot_depth": True,
        }
    }

    def construct(self):
        value1 = Integer(1, color=BLACK)
        value2 = Integer(2, color=BLACK).next_to(value1, RIGHT, buff=0.2)
        value3 = Integer(3, color=BLACK).next_to(value2, RIGHT, buff=0.2)
        ally = VGroup(value1, value2, value3)
        self.add(ally)
        self.play(ally.shift, RIGHT * 0.2, run_time=0.5)
        self.wait()
        value_tmp = Integer(-1, color=BLACK).next_to(value2, RIGHT, buff=0.2)
        self.play(Transform(ally[2], value_tmp))
        self.play(ally.shift, RIGHT * 0.2, run_time=0.5)
        self.wait()
        value_tmp = Integer(0, color=BLACK).next_to(value2, RIGHT, buff=0.2)
        Transform(ally[2], value_tmp)
        self.play(ally.shift, RIGHT * 0.2, run_time=0.5)
        self.wait()
        value_tmp = Integer(1, color=BLACK).next_to(value2, RIGHT, buff=0.2)
        self.play(Transform(ally[2], value_tmp))
        self.play(ally.shift, RIGHT * 0.2, run_time=0.5)
        self.wait()
        value_tmp = Integer(0, color=BLACK).next_to(value2, RIGHT, buff=0.2)
        self.play(Transform(ally[2], value_tmp))
        self.play(ally.shift, RIGHT * 0.2, run_time=0.5)
        self.wait()
        value_tmp = Integer(-1, color=BLACK).next_to(value2, RIGHT, buff=0.2)
        self.play(Transform(ally[2], value_tmp))
        self.play(ally.shift, RIGHT * 0.2, run_time=0.5)
        self.wait()


class tt11(Scene):
    # CONFIG = {"camera_config": {
    #    "background_color": WHITE, "use_plot_depth": True, }}

    def construct(self):
        a = TexMobject("{", "\\sqrt", "0", "}")
        a[2].set_color(RED)
        self.add(a)
        self.wait()


class tt12(Scene_):
    def construct(self):
        preOrderCreate_codes = [
            "void BinaryLinkList<elemType>::preOrderCreate(elemType flag, Node *&t)",
            "{",
            "   elemType value;",
            "   cin >> value;",
            "   if (value!=flag)",
            "   {",
            "      t = new Node(value);",
            "      preOrderCreate(flag, t->left);",
            "      preOrderCreate(flag, t->right);",
            "   }",
            "}",
        ]

        class codeline_preOrderCreate(Text):
            CONFIG = {
                "t2c": {
                    ".": WHITE,
                    "t.": BLACK
                },  # t. 需要和 . 区分开
                "size": 0.37,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        codes_preOrderCreate = (
            VGroup(*[
                codeline_preOrderCreate(code) for code in preOrderCreate_codes
            ]).arrange(DOWN, aligned_edge=LEFT, buff=0.05).move_to(ORIGIN)
            # .next_to(background.get_top(), DOWN, buff=0.2)
            # .shift(LEFT * 0.05 + DOWN * 0.15)
        )
        self.add(codes_preOrderCreate)
        self.wait()


class tt13(Scene_):
    def construct(self):
        a = "0123456789"
        b = ""
        for i in range(2):
            b += a
        c = Text(b, color=BLACK).scale(0.3).move_to(ORIGIN)
        self.add(c)
        self.wait()


class tt14(Scene_):
    def construct(self):
        a = "0123456789"
        b = ""
        for i in range(2):
            b += a
        c = Text(b, color=BLACK).scale(0.3).move_to(DOWN)
        self.add(c)
        self.wait()


class tt15(Scene_):
    def construct(self):
        tt13.construct(self)
        tt14.construct(self)
        # 合并操作


class tt16(Scene_):
    def construct(self):
        for j in range(6, 0, -1):
            print(j)  # 6 5 4 3 2 1


class tt17(Scene_):
    def construct(self):
        n = (Integer(1, color=BLACK).set_opacity(1))
        m = (Integer(-1, color=BLACK).set_opacity(1).next_to(n, DOWN))
        self.add(n)
        self.play(n.set_value, -1, m.set_value, 1)
        self.wait()
        self.play(n.set_value, 1, m.set_value, -1)
        self.wait()
        self.play(n.set_value, -1, m.set_value, 1)
        self.wait()
        self.play(n.set_value, 1, m.set_value, -1)
        self.wait()


class tt18(Scene_):
    def construct(self):
        self.wait(0.5)


class opening(Scene_):
    def construct(self):
        object_text = "getHead 函数演示"
        count = 0
        for i in object_text:
            if i == " ":
                break
            else:
                count += 1
        title1 = TextMobject("链队列", color=BLACK).scale(2).shift(
            UP * 0.5).to_edge(LEFT)
        title2 = TextMobject(object_text, color=BLACK).scale(1.3).shift(
            DOWN * 0.5).to_edge(RIGHT)
        title2[0][:count].set_color(ORANGE)

        def anim(obj, dt):
            # print(dt)
            obj.shift(np.array([-obj.get_center()[0] * dt * 2, 0, 0]))

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
        # self.play(Write(title1), Write(title2))


class opening2(Scene_):
    def construct(self):
        t2c = {"线性表": GOLD, "顺序表示": average_color(PINK, RED)}
        object_text1 = "本节将演示线性表的"
        object_text2 = "顺序表示的函数"
        text1 = Text(object_text1, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).shift(UP * 2.5)
        text2 = Text(object_text2, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).next_to(text1, DOWN, buff=0.1)
        a1 = Text("① clear", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).shift(UP * 0.5 + LEFT * 3)
        a2 = Text("② traverse", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(a1, DOWN,
                                                  buff=0.5).align_to(a1, LEFT)
        a3 = Text("③ search", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(a2, DOWN,
                                                  buff=0.5).align_to(a1, LEFT)
        a4 = Text("④ insert", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(a3, DOWN,
                                                  buff=0.5).align_to(a1, LEFT)
        b1 = Text("⑤ remove", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).shift(UP * 0.5 + RIGHT * 2.5)
        b2 = Text("⑥ inverse", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(b1, DOWN,
                                                  buff=0.5).align_to(b1, LEFT)
        b3 = Text("⑦ resize", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(b2, DOWN,
                                                  buff=0.5).align_to(b1, LEFT)
        b4 = Text("⑧ visit", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(b3, DOWN,
                                                  buff=0.5).align_to(b1, LEFT)
        out = VGroup(text1, text2, a1, a2, a3, a4, b1, b2, b3, b4)
        self.wait()
        self.play(FadeIn(out))
        self.wait(2)
        self.play(FadeOut(out))


class opening3(Scene_):
    def construct(self):
        t2c = {"线性表": GOLD, "链式表示": average_color(PINK, RED)}
        object_text1 = "本节将演示线性表的"
        object_text2 = "链式表示的函数"
        text1 = Text(object_text1, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).shift(UP * 2.5)
        text2 = Text(object_text2, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).next_to(text1, DOWN, buff=0.1)
        a1 = Text("① clear", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).shift(UP * 0.5 + LEFT * 3)
        a2 = Text("② traverse", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(a1, DOWN,
                                                  buff=0.5).align_to(a1, LEFT)
        a3 = Text("③ getposition", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(a2, DOWN,
                                                  buff=0.5).align_to(a1, LEFT)
        a4 = Text("④ search", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(a3, DOWN,
                                                  buff=0.5).align_to(a1, LEFT)
        b1 = Text("⑤ insert", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).shift(UP * 0.5 + RIGHT * 2.5)
        b2 = Text("⑥ remove", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(b1, DOWN,
                                                  buff=0.5).align_to(b1, LEFT)
        b3 = Text("⑦ inverse", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(b2, DOWN,
                                                  buff=0.5).align_to(b1, LEFT)
        b4 = Text("⑧ visit", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(b3, DOWN,
                                                  buff=0.5).align_to(b1, LEFT)
        out = VGroup(text1, text2, a1, a2, a3, a4, b1, b2, b3, b4)
        self.wait()
        self.play(FadeIn(out))
        self.wait(2)
        self.play(FadeOut(out))


class opening4(Scene_):
    def construct(self):
        t2c = {"KMP算法": GOLD}
        object_text = "本节将演示KMP算法的函数"
        text = Text(object_text, font="庞门正道标题体", color=BLACK,
                    t2c=t2c).scale(2).shift(UP * 1.5)
        a1 = Text("①  getNext + kmpFind", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).shift(UP * 0)
        a2 = Text("②  getNextVal + kmpFind", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(a1, DOWN,
                                                  buff=0.5).align_to(a1, LEFT)
        out = VGroup(text, a1, a2)
        self.wait()
        self.play(FadeIn(out))
        self.wait(2)
        self.play(FadeOut(out))


class opening5(Scene_):
    def construct(self):
        t2c = {"二叉树": GOLD, "遍历": average_color(PINK, RED), "建立": BLUE}
        object_text1 = "本节将演示二叉树的"
        object_text2 = "遍历的函数和建立的函数"
        text1 = Text(object_text1, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).shift(UP * 2.5)
        text2 = Text(object_text2, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).next_to(text1, DOWN, buff=0.1)
        title1 = Text("遍历函数", font="庞门正道标题体", color=BLACK,
                      t2c=t2c).scale(1.3).next_to(text2, DOWN,
                                                  buff=0.5).shift(LEFT * 3.2)
        title2 = Text("建立函数", font="庞门正道标题体", color=BLACK,
                      t2c=t2c).scale(1.3).next_to(text2, DOWN,
                                                  buff=0.5).shift(RIGHT * 2.4)
        a1 = Text("①  preOrder", font="思源宋体 Heavy",
                  color=BLACK).scale(1).next_to(title1, DOWN, buff=0.5)
        a2 = Text("②  inOrder", font="思源宋体 Heavy",
                  color=BLACK).scale(1).next_to(a1, DOWN,
                                                buff=0.5).align_to(a1, LEFT)
        a3 = Text("③  postOrder", font="思源宋体 Heavy",
                  color=BLACK).scale(1).next_to(a2, DOWN,
                                                buff=0.5).align_to(a1, LEFT)
        b1 = Text("④  preOrderCreate", font="思源宋体 Heavy",
                  color=BLACK).scale(1).next_to(title2, DOWN, buff=0.5)
        b2 = Text("⑤  levelOrderTraverse", font="思源宋体 Heavy",
                  color=BLACK).scale(1).next_to(b1, DOWN,
                                                buff=0.5).align_to(b1, LEFT)
        out = VGroup(text1, text2, a1, a2, a3, title1, title2, b1, b2)
        self.wait()
        self.play(FadeIn(out))
        self.wait(2)
        self.play(FadeOut(out))


class opening6(Scene_):
    def construct(self):
        t2c = {
            "队列": GOLD,
            "循环队列表示": average_color(PINK, RED),
            "链队列表示": BLUE,
            "循环队列": average_color(PINK, RED),
            "链队列": BLUE
        }
        object_text1 = "本节将演示队列的"
        object_text2 = "循环队列表示和链队列表示的函数"
        text1 = Text(object_text1, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).shift(UP * 2.5)
        text2 = Text(object_text2, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).next_to(text1, DOWN, buff=0.1)
        title1 = Text("循环队列函数", font="庞门正道标题体", color=BLACK,
                      t2c=t2c).scale(1.3).next_to(text2, DOWN,
                                                  buff=0.5).shift(LEFT * 3.2)
        title2 = Text("链队列函数", font="庞门正道标题体", color=BLACK,
                      t2c=t2c).scale(1.3).next_to(text2, DOWN,
                                                  buff=0.5).shift(RIGHT * 2.4)
        a1 = Text("①  seqQueue", font="思源宋体 Heavy",
                  color=BLACK).scale(0.9).next_to(title1, DOWN, buff=0.4)
        a2 = Text("②  enQueue", font="思源宋体 Heavy",
                  color=BLACK).scale(0.9).next_to(a1, DOWN,
                                                  buff=0.3).align_to(a1, LEFT)
        a3 = Text("③  deQueue", font="思源宋体 Heavy",
                  color=BLACK).scale(0.9).next_to(a2, DOWN,
                                                  buff=0.3).align_to(a1, LEFT)
        a4 = Text("④  getHead", font="思源宋体 Heavy",
                  color=BLACK).scale(0.9).next_to(a3, DOWN,
                                                  buff=0.3).align_to(a1, LEFT)
        a5 = Text("⑤  resize", font="思源宋体 Heavy",
                  color=BLACK).scale(0.9).next_to(a4, DOWN,
                                                  buff=0.3).align_to(a1, LEFT)
        b1 = Text("⑥  clear", font="思源宋体 Heavy",
                  color=BLACK).scale(0.9).next_to(title2, DOWN, buff=0.4)
        b2 = Text("⑦  size", font="思源宋体 Heavy",
                  color=BLACK).scale(0.9).next_to(b1, DOWN,
                                                  buff=0.3).align_to(b1, LEFT)
        b3 = Text("⑧  enQueue", font="思源宋体 Heavy",
                  color=BLACK).scale(0.9).next_to(b2, DOWN,
                                                  buff=0.3).align_to(b1, LEFT)
        b4 = Text("⑨  deQueue", font="思源宋体 Heavy",
                  color=BLACK).scale(0.9).next_to(b3, DOWN,
                                                  buff=0.3).align_to(b1, LEFT)
        b5 = Text("⑩  getHead", font="思源宋体 Heavy",
                  color=BLACK).scale(0.9).next_to(b4, DOWN,
                                                  buff=0.3).align_to(b1, LEFT)
        out = VGroup(text1, text2, a1, a2, a3, a4, a5, title1, title2, b1, b2,
                     b3, b4, b5)
        self.wait()
        self.play(FadeIn(out))
        self.wait(2)
        self.play(FadeOut(out))


class opening7(Scene_):
    def construct(self):
        t2c = {"排序": GOLD}
        t3c = {"归并排序": average_color(PINK, RED)}
        object_text1 = "本节将演示排序之"
        object_text2 = "归并排序的函数"
        text1 = Text(object_text1, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).shift(UP * 2.5)
        text2 = Text(object_text2, font="庞门正道标题体", color=BLACK,
                     t2c=t3c).scale(2).next_to(text1, DOWN, buff=0.1)
        a1 = Text("① 直接插入排序", font="思源宋体 Heavy",
                  color=GREY).scale(1.1).shift(UP * 0.5 + LEFT * 3)
        a2 = Text("② 折半插入排序", font="思源宋体 Heavy",
                  color=GREY).scale(1.1).next_to(a1, DOWN,
                                                 buff=0.5).align_to(a1, LEFT)
        a3 = Text("③ 希尔排序", font="思源宋体 Heavy",
                  color=GREY).scale(1.1).next_to(a2, DOWN,
                                                 buff=0.5).align_to(a1, LEFT)
        a4 = Text("④ 冒泡排序", font="思源宋体 Heavy",
                  color=GREY).scale(1.1).next_to(a3, DOWN,
                                                 buff=0.5).align_to(a1, LEFT)
        b1 = Text("⑤ 快速排序", font="思源宋体 Heavy",
                  color=GREY).scale(1.1).shift(UP * 0.5 + RIGHT * 2.5)
        b2 = Text("⑥ 直接选择排序", font="思源宋体 Heavy",
                  color=GREY).scale(1.1).next_to(b1, DOWN,
                                                 buff=0.5).align_to(b1, LEFT)
        b3 = Text("⑦ 堆排序", font="思源宋体 Heavy",
                  color=GREY).scale(1.1).next_to(b2, DOWN,
                                                 buff=0.5).align_to(b1, LEFT)
        b4 = Text("⑧ 归并排序", font="思源宋体 Heavy",
                  color=BLUE_D).scale(1.1).next_to(b3, DOWN,
                                                   buff=0.5).align_to(
                                                       b1, LEFT)
        out = VGroup(text1, text2, a1, a2, a3, a4, b1, b2, b3, b4)
        self.wait()
        self.play(FadeIn(out))
        self.wait(2)
        self.play(FadeOut(out))


class tt19(Scene_):
    def construct(self):
        t2c = {
            "可视化": average_color(PINK, RED),
            "数据结构": "#44cef6",
            "筱团": BLUE,
            "自由": RED,
            "六大章节": "#fbb034",
            "visualization": average_color(PINK, RED),
            "six chapters": "#fbb034",
        }
        text_1 = Text("全系列可视化函数", font="庞门正道标题体", color=BLACK,
                      t2c=t2c).scale(2.25).to_edge(UP * 0.4, buff=1)
        text_2 = Text("包含六大章节", font="庞门正道标题体", color=BLACK,
                      t2c=t2c).scale(2.25).to_edge(UP * 2.1, buff=1)
        en_1 = Text("Full range of visualization functions", font="庞门正道标题体", color=BLACK,
                      t2c=t2c).scale(0.85).next_to(text_1, DOWN, buff=0.3)
        en_2 = Text("Contains six chapters", font="庞门正道标题体", color=BLACK,
                      t2c=t2c).scale(0.85).next_to(text_2, DOWN, buff=0.2)
        a1 = Text("① 线性表", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).shift(DOWN * 0.2 + LEFT * 3.5)
        a2 = Text("② 栈和队列", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(a1, DOWN,
                                                  buff=0.8).align_to(a1, LEFT)
        a3 = Text("③ 字符串(KMP)", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(a2, DOWN,
                                                  buff=0.8).align_to(a1, LEFT)
        b1 = Text("④ 二叉树", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).shift(DOWN * 0.2 + RIGHT * 3.2)
        b2 = Text("⑤ 排序算法", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(b1, DOWN,
                                                  buff=0.8).align_to(b1, LEFT)
        b3 = Text("⑥ 图", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(b2, DOWN,
                                                  buff=0.8).align_to(b1, LEFT)
        c1 = Text("Linear List", font="思源宋体 Heavy",
                  color=BLACK).scale(0.6).next_to(a1, DOWN, buff=0.12).align_to(a1, LEFT)
        c2 = Text("Stacks and Queues", font="思源宋体 Heavy",
                  color=BLACK).scale(0.6).next_to(a2, DOWN, buff=0.12).align_to(a2, LEFT)
        c3 = Text("String (KMP)", font="思源宋体 Heavy",
                  color=BLACK).scale(0.6).next_to(a3, DOWN, buff=0.12).align_to(a3, LEFT)
        c4 = Text("Binary Tree", font="思源宋体 Heavy",
                  color=BLACK).scale(0.6).next_to(b1, DOWN, buff=0.12).align_to(b1, LEFT)
        c5 = Text("Sorting Algorithm", font="思源宋体 Heavy",
                  color=BLACK).scale(0.6).next_to(b2, DOWN, buff=0.12).align_to(b2, LEFT)
        c6 = Text("Graph", font="思源宋体 Heavy",
                  color=BLACK).scale(0.6).next_to(b3, DOWN, buff=0.12).align_to(b3, LEFT)
        self.add(text_1, text_2, a1, a2, a3, b1, b2, b3, en_1, en_2, c1, c2, c3, c4, c5, c6)
        # self.play(Write(text_1), Write(text_2))
        # self.wait()
        # self.play(FadeInFrom(a1, RIGHT))
        # self.play(FadeInFrom(a2, RIGHT))
        # self.play(FadeInFrom(a3, RIGHT))
        # self.play(FadeInFrom(b1, RIGHT))
        # self.play(FadeInFrom(b2, RIGHT))
        # self.play(FadeInFrom(b3, RIGHT))
        # self.wait()


class tt20(Scene_):
    def construct(self):
        # 基准 ⚪
        base_circle = Circle(color=BLACK, radius=2.0, stroke_opacity=1)
        # 满同心圆
        full_circle = Circle(color=BLACK,
                             fill_color=WHITE,
                             fill_opacity=1,
                             radius=1.0,
                             stroke_opacity=1)
        # 直径
        lines = VGroup()
        degrees = 60
        for i in range(3):
            base_line = Line(np.array([0, -2, 0]),
                             np.array([0, 2, 0]),
                             color=BLACK,
                             stroke_opacity=1)
            base_line.rotate(angle=i * 60 * DEGREES)
            lines.add(base_line)
        # 数值
        # math.sqrt(3)
        a = Integer(0, color=BLACK)
        b = Integer(1, color=BLACK)
        c = Integer(2, color=BLACK)
        d = Integer(3, color=BLACK)
        a.shift(LEFT * 1.5)
        b.shift(UP * 1.25 + LEFT * 1.25 / math.sqrt(3))
        c.shift(UP * 1.25 + RIGHT * 1.25 / math.sqrt(3))
        d.shift(RIGHT * 1.5)
        nums = VGroup(a, b, c, d)
        # 坐标
        index_a = Integer(0, color=BLACK).scale(0.5)
        index_b = Integer(1, color=BLACK).scale(0.5)
        index_c = Integer(2, color=BLACK).scale(0.5)
        index_d = Integer(3, color=BLACK).scale(0.5)
        index_e = Integer(4, color=BLACK).scale(0.5)
        index_f = Integer(5, color=BLACK).scale(0.5)
        index_a.shift(LEFT * 2.2)
        index_b.shift(UP * 2 + LEFT * 2 / math.sqrt(3))
        index_c.shift(UP * 2 + RIGHT * 2 / math.sqrt(3))
        index_d.shift(RIGHT * 2.2)
        index_e.shift(DOWN * 2 + RIGHT * 2 / math.sqrt(3))
        index_f.shift(DOWN * 2 + LEFT * 2 / math.sqrt(3))
        indexs = VGroup(index_a, index_b, index_c, index_d, index_e, index_f)
        pass
        circles = VGroup(base_circle, lines, full_circle)
        self.add(circles)
        self.add(nums, indexs)
        # self.play(Write(circles))
        # self.wait()


class tt21(Scene_):
    def construct(self):
        """
        new_circles = VGroup()
        for i in range(12):
            fan = AnnularSector(outer_radius=2*0.75, inner_radius=1*0.75, stroke_width=2, stroke_color=BLACK,
                                start_angle=(PI/6)*i, angle=PI/6)
            new_circles.add(fan.copy())
        nums = VGroup()
        for i in range(12):
            num = Integer(i, color=BLACK).scale(0.5)
            num.move_to(new_circles[i])
            nums.add(num.copy())
        self.add(new_circles, nums)
        """
        # 基准 ⚪
        base_circle = Circle(color=BLACK, radius=2.0, stroke_opacity=1)
        # 满同心圆
        full_circle = Circle(color=BLACK,
                             fill_color=WHITE,
                             fill_opacity=1,
                             radius=1.0,
                             stroke_opacity=1)
        # 直径
        lines = VGroup()
        degrees = 30
        for i in range(6):
            base_line = Line(np.array([0, -2, 0]),
                             np.array([0, 2, 0]),
                             color=BLACK,
                             stroke_opacity=1)
            base_line.rotate(angle=i * 30 * DEGREES)
            lines.add(base_line)
        # 数值
        # 2-math.sqrt(3)
        tan = 2 - math.sqrt(3)
        a = Integer(0, color=BLACK)
        b = Integer(1, color=BLACK)
        c = Integer(2, color=BLACK)
        d = Integer(3, color=BLACK)
        a.shift(LEFT * 1.5 + UP * 1.5 * tan)
        b.shift(UP * 1.1 + LEFT * 1.1)
        c.shift(LEFT * 1.5 * tan + UP * 1.5)
        d.shift(RIGHT * 1.5 * tan + UP * 1.5)
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
        index_a.shift(LEFT * 2.1 + UP * 2.1 * tan)
        index_b.shift(UP * 1.6 + LEFT * 1.6)
        index_c.shift(LEFT * 2.1 * tan + UP * 2.1)
        index_d.shift(RIGHT * 2.1 * tan + UP * 2.1)
        index_e.shift(UP * 1.6 + RIGHT * 1.6)
        index_f.shift(RIGHT * 2.1 + UP * 2.1 * tan)

        index_g.shift(RIGHT * 2.1 + DOWN * 2.1 * tan)
        index_h.shift(DOWN * 1.6 + RIGHT * 1.6)
        index_i.shift(RIGHT * 2.1 * tan + DOWN * 2.1)
        index_j.shift(LEFT * 2.1 * tan + DOWN * 2.1)
        index_k.shift(LEFT * 1.6 + DOWN * 1.6)
        index_l.shift(LEFT * 2.1 + DOWN * 2.1 * tan)
        indexs = VGroup(index_a, index_b, index_c, index_d, index_e, index_f,
                        index_g, index_h, index_i, index_j, index_k, index_l)
        # 整体 1(基准 ⚪)
        base_new = VGroup(base_circle, lines, full_circle, nums,
                          indexs).scale(0.75)
        self.add(base_new)
        self.wait()


class tt22(Scene_):
    def construct(self):
        t2c = {
            "可视化": average_color(PINK, RED),
            "数据结构": "#44cef6",
            "筱团": BLUE,
            "自由": RED,
            "六大章节": "#fbb034"
        }
        text_1 = Text("同学们好!", font="庞门正道标题体", color=BLACK,
                      t2c=t2c).scale(2.25).to_edge(UP * 2, buff=1)
        text_2 = Text("欢迎来到数据结构视频教程", font="庞门正道标题体", color=BLACK,
                      t2c=t2c).scale(2.25).to_edge(UP * 3.2, buff=1)
        text_3 = Text("本系列教程将可视化", font="庞门正道标题体", color=BLACK,
                      t2c=t2c).scale(2.05).to_edge(UP * 2, buff=1)
        text_4 = Text("数据结构书中部分章节的代码", font="庞门正道标题体", color=BLACK,
                      t2c=t2c).scale(2.05).to_edge(UP * 3.2, buff=1)
        text_5 = Text("全系列可视化函数", font="庞门正道标题体", color=BLACK,
                      t2c=t2c).scale(2.25).to_edge(UP * 0.8, buff=1)
        text_6 = Text("包含六大章节", font="庞门正道标题体", color=BLACK,
                      t2c=t2c).scale(2.25).to_edge(UP * 2, buff=1)
        self.wait(0.5)
        self.play(Write(text_1))
        self.wait(0.5)
        self.play(WriteRandom(text_2), run_time=1.5)
        self.wait(1.8)
        self.play(Transform(text_1, text_3),
                  Transform(text_2, text_4),
                  run_time=1.2)
        self.wait(1.8)
        self.play(FadeOutRandom(text_1), FadeOutRandom(text_2), run_time=1.8)
        self.wait()
        t2c = {"筱团": BLUE, "自由": RED}
        codeboard = ImageMobject("book.png").scale(2.5).shift(LEFT * 4)
        manim = Text("动画引擎：Manim", font="方正字迹-青柠体 简", color=BLACK,
                     t2c=t2c).scale(1.6).shift(RIGHT * 1.75 + UP * 1)
        up = Text("制作up：自由的筱团", font="方正字迹-青柠体 简", color=BLACK,
                  t2c=t2c).scale(1.6).shift(DOWN * 1).align_to(manim, LEFT)
        self.play(FadeIn(codeboard), run_time=0.75)
        self.wait(0.5)
        self.play(Write(manim), Write(up))
        self.wait(2)
        self.play(FadeOutRandom(manim), FadeOutRandom(up),
                  FadeOutAndShift(codeboard))
        self.wait()
        a1 = Text("① 线性表", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).shift(UP * 0.25 + LEFT * 3)
        a2 = Text("② 栈和队列", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(a1, DOWN,
                                                  buff=0.8).align_to(a1, LEFT)
        a3 = Text("③ 字符串(KMP)", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(a2, DOWN,
                                                  buff=0.8).align_to(a1, LEFT)
        b1 = Text("④ 二叉树", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).shift(UP * 0.25 + RIGHT * 2.5)
        b2 = Text("⑤ 排序算法", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(b1, DOWN,
                                                  buff=0.8).align_to(b1, LEFT)
        b3 = Text("⑥ 图", font="思源宋体 Heavy",
                  color=BLACK).scale(1.1).next_to(b2, DOWN,
                                                  buff=0.8).align_to(b1, LEFT)
        self.play(Write(text_5), Write(text_6))
        self.wait()
        self.play(FadeInFrom(a1, RIGHT))
        self.play(FadeInFrom(a2, RIGHT))
        self.play(FadeInFrom(a3, RIGHT))
        self.play(FadeInFrom(b1, RIGHT))
        self.play(FadeInFrom(b2, RIGHT))
        self.play(FadeInFrom(b3, RIGHT))
        self.wait()


class tt23(Scene_):
    def construct(self):
        title = Text("配乐", font="庞门正道标题体", color=RED_D,
                     size=1.5).to_edge(UP * 0.5)
        line = Line(LEFT_SIDE, RIGHT_SIDE, color=RED_D).next_to(title, DOWN)
        title.add(line)
        self.add(title)
        a0 = Text("Begin", font="庞门正道标题体", color=BLACK).scale(1.2)
        a = Text("顺序表", font="庞门正道标题体", color=BLACK).scale(1.2)
        b = Text("单链表", font="庞门正道标题体", color=BLACK).scale(1.2)
        c = Text("栈", font="庞门正道标题体", color=BLACK).scale(1.2)
        d = Text("队列", font="庞门正道标题体", color=BLACK).scale(1.2)
        e = Text("KMP算法", font="庞门正道标题体", color=BLACK).scale(1.2)
        f = Text("二叉树", font="庞门正道标题体", color=BLACK).scale(1.2)
        g = Text("排序", font="庞门正道标题体", color=BLACK).scale(1.2)
        h = Text("图", font="庞门正道标题体", color=BLACK).scale(1.2)
        a0.shift(LEFT * 5.5 + UP * 2.5)
        t0 = Text("蜜雪冰城主题曲MV 中英双语版", font="思源宋体 CN Heavy",
                  color=BLACK).scale(0.7).next_to(a0, DOWN).align_to(a0, LEFT)
        tt0 = Text("(BV:1wv41157Rr)", font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.6).next_to(t0,
                                                   DOWN).align_to(t0, LEFT)
        self.add(a0, t0, tt0)
        a.next_to(a0, DOWN, buff=1.5).align_to(a, LEFT).shift(UP * 0.2)
        t1 = Text("【Animenz】火花 - 你的名字 钢琴", font="思源宋体 CN Heavy",
                  color=BLACK).scale(0.7).next_to(a, DOWN).align_to(a, LEFT)
        tt1 = Text("(BV:1S64y1179w)", font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.6).next_to(t1,
                                                   DOWN).align_to(t1, LEFT)
        self.add(a, t1, tt1)
        b.next_to(a, DOWN, buff=1.5).align_to(a, LEFT).shift(UP * 0.2)
        t2 = Text("『纯筝版』《赤伶》玉面小嫣然", font="思源宋体 CN Heavy",
                  color=BLACK).scale(0.7).next_to(b, DOWN).align_to(b, LEFT)
        tt2 = Text("(BV:1A4411S7rv)", font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.6).next_to(t2,
                                                   DOWN).align_to(t2, LEFT)
        t3 = Text("古筝《大鱼》古筝版大鱼海棠印象曲", font="思源宋体 CN Heavy",
                  color=BLACK).scale(0.7).next_to(tt2, DOWN).align_to(b, LEFT)
        tt3 = Text("(BV:1JJ411x7Hr)", font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.6).next_to(t3,
                                                   DOWN).align_to(t3, LEFT)
        self.add(b, t2, tt2, t3, tt3)
        c.shift(RIGHT * 0 + UP * 2.5).align_to(a0, UP)
        t4 = Text("【琵琶】南山雪——“飞满天似我挂念你无边”", font="思源宋体 CN Heavy",
                  color=BLACK).scale(0.7).next_to(c, DOWN).align_to(c, LEFT)
        tt4 = Text("(BV:17i4y1A7uH)", font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.6).next_to(t4,
                                                   DOWN).align_to(t4, LEFT)
        t5 = Text("【陆二胡】热爱105℃的你", font="思源宋体 CN Heavy",
                  color=BLACK).scale(0.7).next_to(tt4, DOWN).align_to(c, LEFT)
        tt5 = Text("(BV:1PB4y1M7Ry)", font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.6).next_to(t5,
                                                   DOWN).align_to(t5, LEFT)
        t6 = Text("【拇指琴】《溯Reverse》世界是冰 就让她冰",
                  font="思源宋体 CN Heavy",
                  color=BLACK).scale(0.7).next_to(tt5, DOWN).align_to(c, LEFT)
        tt6 = Text("(BV:1Yy4y1S7Qq)", font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.6).next_to(t6,
                                                   DOWN).align_to(t6, LEFT)
        self.add(c, t4, t5, t6, tt4, tt5, tt6)
        d.next_to(tt6, DOWN).align_to(tt6, LEFT)
        t7 = Text("【钢琴】风居住的街道【高清音质】风の住む街", font="思源宋体 CN Heavy",
                  color=BLACK).scale(0.7).next_to(d, DOWN).align_to(d, LEFT)
        tt7 = Text("(BV:1xJ411u76b)", font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.6).next_to(t7,
                                                   DOWN).align_to(t7, LEFT)
        self.add(d, t7, tt7)
        self.wait(2)


class tt24(Scene_):
    def construct(self):
        title = Text("配乐", font="庞门正道标题体", color=RED_D,
                     size=1.5).to_edge(UP * 0.5)
        line = Line(LEFT_SIDE, RIGHT_SIDE, color=RED_D).next_to(title, DOWN)
        title.add(line)
        self.add(title)
        e = Text("KMP算法", font="庞门正道标题体", color=BLACK).scale(1.2)
        f = Text("二叉树", font="庞门正道标题体", color=BLACK).scale(1.2)
        g = Text("排序", font="庞门正道标题体", color=BLACK).scale(1.2)
        h = Text("图", font="庞门正道标题体", color=BLACK).scale(1.2)
        t8 = Text("【钢琴】《人类之光•愛のテーマ》", font="思源宋体 CN Heavy",
                  color=BLACK).scale(0.7)
        t8.shift(LEFT * 3.8 + UP * 2.5)
        tt8 = Text("(BV:1pJ411e7U3)", font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.6).next_to(t8,
                                                   DOWN).align_to(t8, LEFT)
        self.add(t8, tt8)
        e.next_to(tt8, DOWN).align_to(tt8, LEFT)
        t9 = Text("LiSA×Uru 再会 钢琴版", font="思源宋体 CN Heavy",
                  color=BLACK).scale(0.7).next_to(e, DOWN).align_to(e, LEFT)
        tt9 = Text("(BV:15v411Y7mx)", font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.6).next_to(t9,
                                                   DOWN).align_to(t9, LEFT)
        t10 = Text("【钢琴郎朗】视奏《前前前世》", font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.7).next_to(tt9,
                                                   DOWN).align_to(tt9, LEFT)
        tt10 = Text("(BV:1qs411e7Ch)", font="思源宋体 CN Heavy",
                    color=BLACK).scale(0.6).next_to(t10,
                                                    DOWN).align_to(t10, LEFT)
        self.add(e, t9, tt9, t10, tt10)
        f.next_to(tt10, DOWN).align_to(tt10, LEFT)
        t11 = Text("Game of Thrones 【孟晓洁_笛箫】",
                   font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.7).next_to(f, DOWN).align_to(f, LEFT)
        tt11 = Text("(BV:1Jb411M7G9)", font="思源宋体 CN Heavy",
                    color=BLACK).scale(0.6).next_to(t11,
                                                    DOWN).align_to(t11, LEFT)
        t12 = Text("指弹吉他《Lemon》 Kenshi Yonezu ",
                   font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.7)
        t12.shift(RIGHT * 2.5 + UP * 2.5)
        tt12 = Text("(BV:1TJ411h7sz)", font="思源宋体 CN Heavy",
                    color=BLACK).scale(0.6).next_to(t12,
                                                    DOWN).align_to(t12, LEFT)
        t13 = Text("【空灵の箫】犬夜叉《穿越时空的思念》", font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.7).next_to(tt12,
                                                   DOWN).align_to(tt12, LEFT)
        tt13 = Text("(BV:1gE411i7QR)", font="思源宋体 CN Heavy",
                    color=BLACK).scale(0.6).next_to(t13,
                                                    DOWN).align_to(t13, LEFT)
        t14 = Text("【绝美指弹吉他】未闻花名ED", font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.7).next_to(tt13,
                                                   DOWN).align_to(tt13, LEFT)
        tt14 = Text("(BV:1gs411m7XZ)", font="思源宋体 CN Heavy",
                    color=BLACK).scale(0.6).next_to(t14,
                                                    DOWN).align_to(t14, LEFT)
        self.add(f, t11, tt11, t12, tt12, t13, tt13, t14, tt14)
        g.next_to(tt14, DOWN).align_to(tt14, LEFT)
        gg = Text("(直接插入排序)", font="庞门正道标题体",
                  color=BLACK).scale(0.8).next_to(g, RIGHT).align_to(g, DOWN)
        t15 = Text("小提琴演奏【天空之城】主题曲《We All Lie》",
                   font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.7).next_to(g, DOWN).align_to(g, LEFT)
        tt15 = Text("(BV:1b44y1m7sT)", font="思源宋体 CN Heavy",
                    color=BLACK).scale(0.6).next_to(t15,
                                                    DOWN).align_to(t15, LEFT)
        t16 = Text("人间冰激凌，小提琴翻奏《蜜雪冰城主题曲》", font="思源宋体 CN Heavy",
                   color=BLACK).scale(0.7).next_to(tt15,
                                                   DOWN).align_to(tt15, LEFT)
        tt16 = Text("(BV:1bX4y1P7w3)", font="思源宋体 CN Heavy",
                    color=BLACK).scale(0.6).next_to(t16,
                                                    DOWN).align_to(t16, LEFT)
        self.add(g, gg, t15, tt15, t16, tt16)
        self.wait(2)


class tt25(Scene_):
    def construct(self):
        circle1 = Circle(color=RED)
        circle2 = Circle(color=BLUE)
        circle2.next_to(circle1, DOWN).shift(RIGHT)
        self.add(circle1, circle2)
        self.wait()
        a = circle2.copy().move_to(circle1)
        self.play(circle2.align_to, circle2.copy().move_to(circle1), LEFT)


class tt26(Scene_):
    def construct(self):
        t2c = {
            "队列": GOLD,
            "循环队列表示": average_color(PINK, RED),
            "链队列表示": BLUE,
            "循环队列": average_color(PINK, RED),
            "链队列": BLUE
        }
        object_text1 = "本节将演示队列的"
        object_text2 = "循环队列表示的函数"
        text1 = Text(object_text1, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).shift(UP * 2.5)
        text2 = Text(object_text2, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).next_to(text1, DOWN, buff=0.1)
        a1 = Text("①  seqQueue", font="思源宋体 Heavy",
                  color=BLACK).scale(1.2).next_to(text2, DOWN, buff=0.5)
        a2 = Text("②  enQueue", font="思源宋体 Heavy",
                  color=BLACK).scale(1.2).next_to(a1, DOWN, buff=0.6).align_to(
                      a1, LEFT).shift(LEFT * 2.2)
        a3 = Text("③  deQueue", font="思源宋体 Heavy",
                  color=BLACK).scale(1.2).next_to(a1, DOWN, buff=0.6).align_to(
                      a1, LEFT).shift(RIGHT * 3)
        a4 = Text("④  getHead", font="思源宋体 Heavy",
                  color=BLACK).scale(1.2).next_to(a2, DOWN, buff=0.6).align_to(
                      a1, LEFT).shift(LEFT * 2.2)
        a5 = Text("⑤  resize", font="思源宋体 Heavy",
                  color=BLACK).scale(1.2).next_to(a2, DOWN, buff=0.6).align_to(
                      a1, LEFT).shift(RIGHT * 3)

        out = VGroup(text1, text2, a1, a2, a3, a4, a5)
        self.wait()
        self.play(FadeIn(out))
        self.wait(2)
        self.play(FadeOut(out))


class tt27(Scene_):
    def construct(self):
        a = Circle(color=BLUE)
        b = Circle().next_to(a, DOWN)
        self.add(a, b)
        self.play(Swap(a, b))


class tt28(Scene_):
    def construct(self):
        a = Text("李蓝骏回来啦！", font="思源宋体 Heavy", color=BLACK).scale(2)
        self.wait()
        self.play(FadeIn(a))
        self.wait()


class opening8(Scene_):
    def construct(self):
        t2c = {"堆排序": GOLD, "两个": average_color(PINK, RED)}
        object_text1 = "堆排序涉及两个函数： "
        object_text2 = "siftDown(...) "
        object_text3 = "heapSort(...) "
        text1 = Text(object_text1, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).shift(UP * 1.5)
        text2 = Text(object_text2, font="思源宋体 Heavy",
                     color=GREY).scale(1.5).next_to(text1, DOWN, buff=0.7)
        text3 = Text(object_text3, font="思源宋体 Heavy",
                     color=GREY).scale(1.5).next_to(text2, DOWN, buff=0.5)

        out = VGroup(text1, text2, text3)
        self.wait()
        self.play(FadeIn(out))
        self.wait()
        self.play(out[1].set_color, BLUE_D)
        self.wait(2)
        self.play(FadeOut(out))


class opening9(Scene_):
    def construct(self):
        t2c = {"堆排序": GOLD, "两个": average_color(PINK, RED)}
        object_text1 = "堆排序涉及两个函数： "
        object_text2 = "siftDown(...) "
        object_text3 = "heapSort(...) "
        text1 = Text(object_text1, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).shift(UP * 1.5)
        text2 = Text(object_text2, font="思源宋体 Heavy",
                     color=BLUE_D).scale(1.5).next_to(text1, DOWN, buff=0.7)
        text3 = Text(object_text3, font="思源宋体 Heavy",
                     color=GREY).scale(1.5).next_to(text2, DOWN, buff=0.5)

        out = VGroup(text1, text2, text3)
        self.wait()
        self.play(FadeIn(out))
        self.wait()
        self.play(out[1].set_color, GREY, out[2].set_color, BLUE_D)
        self.wait(2)
        self.play(FadeOut(out))

class opening10(Scene_):
    def construct(self):
        t2c = {"归并排序": GOLD, "两个": average_color(PINK, RED)}
        object_text1 = "归并排序涉及两个函数： "
        object_text2 = "merge(...) "
        object_text3 = "mergeSort(...) "
        text1 = Text(object_text1, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).shift(UP * 1.5)
        text2 = Text(object_text2, font="思源宋体 Heavy",
                     color=GREY).scale(1.5).next_to(text1, DOWN, buff=0.7)
        text3 = Text(object_text3, font="思源宋体 Heavy",
                     color=GREY).scale(1.5).next_to(text2, DOWN, buff=0.5)

        out = VGroup(text1, text2, text3)
        self.wait()
        self.play(FadeIn(out))
        self.wait()
        self.play(out[1].set_color, BLUE_D)
        self.wait(2)
        self.play(FadeOut(out))


class opening11(Scene_):
    def construct(self):
        t2c = {"归并排序": GOLD, "两个": average_color(PINK, RED)}
        object_text1 = "归并排序涉及两个函数： "
        object_text2 = "merge(...) "
        object_text3 = "mergeSort(...) "
        text1 = Text(object_text1, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).shift(UP * 1.5)
        text2 = Text(object_text2, font="思源宋体 Heavy",
                     color=BLUE_D).scale(1.5).next_to(text1, DOWN, buff=0.7)
        text3 = Text(object_text3, font="思源宋体 Heavy",
                     color=GREY).scale(1.5).next_to(text2, DOWN, buff=0.5)

        out = VGroup(text1, text2, text3)
        self.wait()
        self.play(FadeIn(out))
        self.wait()
        self.play(out[1].set_color, GREY, out[2].set_color, BLUE_D)
        self.wait(2)
        self.play(FadeOut(out))

class opening12(Scene_):
    def construct(self):
        t2c = {"快速排序": GOLD, "两个": average_color(PINK, RED)}
        object_text1 = "快速排序涉及两个函数： "
        object_text2 = "partition(...) "
        object_text3 = "quickSort(...) "
        text1 = Text(object_text1, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).shift(UP * 1.5)
        text2 = Text(object_text2, font="思源宋体 Heavy",
                     color=GREY).scale(1.5).next_to(text1, DOWN, buff=0.7)
        text3 = Text(object_text3, font="思源宋体 Heavy",
                     color=GREY).scale(1.5).next_to(text2, DOWN, buff=0.5)

        out = VGroup(text1, text2, text3)
        self.wait()
        self.play(FadeIn(out))
        self.wait()
        self.play(out[1].set_color, BLUE_D)
        self.wait(2)
        self.play(FadeOut(out))


class opening13(Scene_):
    def construct(self):
        t2c = {"快速排序": GOLD, "两个": average_color(PINK, RED)}
        object_text1 = "快速排序涉及两个函数： "
        object_text2 = "partition(...) "
        object_text3 = "quickSort(...) "
        text1 = Text(object_text1, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).shift(UP * 1.5)
        text2 = Text(object_text2, font="思源宋体 Heavy",
                     color=BLUE_D).scale(1.5).next_to(text1, DOWN, buff=0.7)
        text3 = Text(object_text3, font="思源宋体 Heavy",
                     color=GREY).scale(1.5).next_to(text2, DOWN, buff=0.5)

        out = VGroup(text1, text2, text3)
        self.wait()
        self.play(FadeIn(out))
        self.wait()
        self.play(out[1].set_color, GREY, out[2].set_color, BLUE_D)
        self.wait(2)
        self.play(FadeOut(out))

class tt29(Scene_):
    def construct(self):
        a = Circle(color=BLACK, radius=2.0, stroke_opacity=1).scale(0.5)
        group = VGroup(a)
        self.wait()
        self.play(FadeIn(group))
        self.play(group.shift, RIGHT * 2)
        self.play(a.set_color, BLUE)
        self.play(group.shift, LEFT * 2)
        self.wait()


class opening14(Scene_):
    def construct(self):
        t2c = {"图": GOLD,"Prim": "#e64dd4", "无向图": average_color(PINK, RED), "邻接矩阵": BLUE}
        object_text1 = "本节将演示图的Prim算法"
        object_text2 = "采用无向图和邻接矩阵"
        text1 = Text(object_text1, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).shift(UP * 1)
        text2 = Text(object_text2, font="庞门正道标题体", color=BLACK,
                     t2c=t2c).scale(2).next_to(text1, DOWN, buff=0.2)
        out = VGroup(text1, text2)
        self.wait()
        self.play(FadeIn(out))
        self.wait(2)
        self.play(FadeOut(out))
