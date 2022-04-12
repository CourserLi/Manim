from manimlib.imports import *
from manim_tuan import *

"""
TODO
1:
"""

# straightSort
# binaryInsertSort
# shellSort
# bubbleSort
# partition
# quickSort
# straightSelectSort
# siftDown
# heapSort
# merge
# mergeSort

straightSort_codes = [
    "int pos, j;",
    "Type tmp;",
    "for (pos = 1; pos < size; pos++)",
    "{",
    "   tmp = R[pos];",
    "   for (j = pos - 1; tmp < R[j] && j >= 0; j--)",
    "      R[j + 1] = R[j];",
    "   R[j + 1] = tmp;",
    "}",
]

binaryInsertSort_codes = [
    "int pos, j, low, high, mid;",
    "Type tmp;",
    "for (pos = 1; pos < size; pos++)",
    "{",
    "   tmp = R[pos];",
    "   low = 0;",
    "   high = pos - 1;",
    "   while (low <= high)",
    "   {",
    "      mid = (low + high) / 2;",
    "      if (tmp < R[mid])",
    "         high = mid - 1;",
    "      else",
    "         low = mid + 1;",
    "   }",
    "   for (j = pos - 1; j >= low; j--)",
    "      R[j + 1] = R[j];",
    "   R[low] = tmp;",
    "}",
]

shellSort_codes = [
    "int gap, pos, j;",
    "Type tmp;",
    "for (gap = size / 2; gap > 0; gap /= 2)",
    "{",
    "   for (pos = gap; pos < size; pos++)",
    "   {",
    "      tmp = R[pos];",
    "      for (j = pos - gap; j >= 0 && R[j] > tmp; j -= gap)",
    "         R[j + gap] = R[j];",
    "      R[j + gap] = tmp;",
    "   }",
    "}",
]

bubbleSort_codes = [
    "int i, j;",
    "bool flag = true;",
    "for (int i = 1; i < size && size && flag; ++i)",
    "{",
    "   flag = false;",
    "   for (j = 0; j < size - i; ++j)",
    "   {",
    "      if (R[j + 1] < R[j])",
    "      {",
    "         swap(R[j], R[j + 1]);",
    "         flag = true;",
    "      }",
    "   }",
    "}",
]

partition_codes = [
    "Type tmp = S[low];",
    "while (low != high)",
    "{",
    "   while (low < high && S[high] >= tmp)",
    "      high--;",
    "   if (low < high)",
    "   {",
    "      S[low] = S[high];",
    "      low++;",
    "   }",
    "   while (low < high && S[low] <= tmp)",
    "      low++;",
    "   if (low < high)",
    "   {",
    "      S[high] = S[low];",
    "      high--;",
    "   }",
    "}",
    "S[low] = tmp;",
    "return low;",
]

quickSort_main_codes = [
    "int pivot;",
    "if (low >= high)",
    "   return;",
    "pivot = partition(S, low, high);",
    "quickSort(S, low, pivot - 1);",
    "quickSort(S, pivot + 1, high);",
]

quickSort_vice_codes = [
    "quickSort(S, 0, size - 1);",
]

straightSelectSort_codes = [
    "int pos, min, j;",
    "for (pos = 0; pos < size - 1; pos++)",
    "{",
    "   min = pos;",
    "   for (j = pos + 1; j < size; ++j)",
    "      if (R[j] < R[min])",
    "         min = j;",
    "   if (pos != min)",
    "      swap(R[pos], R[min]);",
    "}",
]

siftDown_codes = [
    "int child;",
    "Type tmp = R[pos];",
    "for (; pos * 2 + 1 < size; pos = child)",
    "{",
    "   child = pos * 2 + 1;",
    "   if (child != size - 1 && R[child + 1] > R[child])",
    "      child++;",
    "   if (R[child] > tmp)",
    "      R[pos] = R[child];",
    "   else",
    "      break;",
    "}",
    "R[pos] = tmp;",
]

heapSort_codes = [
    "int i;",
    "for (i = size / 2 - 1; i >= 0; i--)",
    "   siftDown(R, i, size);",
    "for (i = size - 1; i > 0; i--)",
    "{",
    "   swap(R[0], R[i]);",
    "   siftDown(R, 0, i);",
    "}",
]

merge_codes = [
    "int i = low, j = mid, k = 0;",
    "while (i < mid && j <= high)",
    "   if (R[i] < R[j])",
    "      tmp[k++] = R[i++];",
    "   else",
    "      tmp[k++] = R[j++];",
    "while (i < mid)",
    "   tmp[k++] = R[i++];",
    "while (j <= high)",
    "   tmp[k++] = R[j++];",
    "for (i = 0, k = low; k <= high;)",
    "   R[k++] = tmp[i++];",
]

mergeSort_main_codes = [
    "if (low == high)",
    "   return;",
    "int mid = (low + high) / 2;",
    "mergeSort(R, tmp, low, mid);",
    "mergeSort(R, tmp, mid + 1, high);",
    "merge(R, tmp, low, mid + 1, high);",
]

mergeSort_vice_codes = [
    "Type *tmp = new Type[size];",
    "mergeSort(R, tmp, 0, size - 1);",
    "delete[] tmp;",
]


class Scene_White(Scene):
    CONFIG = {"camera_config": {
        "background_color": WHITE, "use_plot_depth": True, }}


class straightSort(Scene_White):
    def construct(self):
        # global
        # Frame 整体框架
        # height: 8  *  width: 14.2
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_color=WHITE,
            fill_opacity=1,
            height=4.5,
            width=11.2,
        ).to_corner(UL, buff=0)
        frame_tmp = Rectangle(
            color=GREEN, stroke_opacity=0, height=4.5, width=3,
        ).to_corner(UR, buff=0)
        frame_code = Rectangle(
            color=BLUE, stroke_opacity=0, height=3.5, width=7.1+1,
        ).to_corner(DL, buff=0)
        frame_variable = Rectangle(
            color=RED, stroke_opacity=0, height=3.5, width=7.1-1,
        ).to_corner(DR, buff=0)
        self.add(frame_animation, frame_code, frame_variable)

        # --------------- 动画框架 ---------------
        # 标题
        title = (
            Text("直接插入排序", font="思源宋体 Heavy", color=BLACK)
            .scale(0.8)
            .to_corner(UP)
            .shift(UP*0.25)
        )
        self.add(title)
        # 基准长方形
        rectangle_base = MyRectangle(
            fill_color=BLUE, color=BLUE, height=2.5, width=0.8, fill_opacity=1, opacity=1, stroke_opacity=1)
        # 存储待排序的长方块
        rec_base = VGroup()
        # 存储每个长方块的高度
        rec_height = []
        for i in range(8):
            highest = 2.5
            shortest = 0.5
            gap = (highest-shortest)/7
            rec_height_element = shortest+gap*i
            rec_height.append(rec_height_element)
        # 打乱长方块的顺序
        chaos = [5, 1, 2, 7, 0, 6, 3, 4]  # 自定义顺序
        rec_height_chaos = []
        for i in range(8):
            rec_height_chaos.append(rec_height[chaos[i]])
        for i in range(8):
            rectangle_order = rectangle_base.copy()
            rectangle_order.set_height(rec_height_chaos[i], stretch=True)
            rec_base.add(rectangle_order.copy())
        rec_base.arrange(RIGHT, aligned_edge=DOWN, buff=0.5)
        rec_base.move_to(frame_animation).shift(UP*0.2)
        # 各方块下标
        rec_subscript = VGroup()
        for i in range(8):
            subscript = (
                Text(str(i), font="思源宋体 Heavy", color=BLACK)
                .scale(0.4)
                .next_to(rec_base[i], DOWN, buff=0.1)
            )
            rec_subscript.add(subscript)
        # 额外的 -1 下标
        extra_subscript = (
            Text(str(-1), font="思源宋体 Heavy", color=BLACK)
            .scale(0.4)
            .move_to(rec_subscript[0])
            .shift(LEFT*0.6)
        )
        # 各方块坐标
        rec_coordinate = VGroup()
        for i in range(8):
            coordinate = (
                Text(str(chaos[i]), font="江西拙楷", color=BLACK)
                .scale(0.7)
                .move_to(rec_base[i])
            )
            # coordinate.add_updater(lambda a: a.move_to(rec_base[i]))
            rec_coordinate.add(coordinate)
        # 映射表
        rec_map = {0: rec_base[0], 1: rec_base[1], 2: rec_base[2], 3: rec_base[3],
                   4: rec_base[4], 5: rec_base[5], 6: rec_base[6], 7: rec_base[7]}
        num_map = {0: rec_coordinate[0], 1: rec_coordinate[1], 2: rec_coordinate[2], 3: rec_coordinate[3],
                   4: rec_coordinate[4], 5: rec_coordinate[5], 6: rec_coordinate[6], 7: rec_coordinate[7]}
        self.add(rec_base, rec_subscript, rec_coordinate)
        # self.add(extra_subscript)

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
        background.set_height(3, stretch=True).set_width(7.5, stretch=True)
        background.move_to(frame_code)

        # 代码 + 移动框
        class codeline_straightSort(Text):
            CONFIG = {
                "size": 0.5,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        def ignore_space_len(code, num):
            origin_len = len(code)
            begin = origin_len - 1
            record = 0
            temp_codes = straightSort_codes
            for index in range(begin, 0, -1):
                if temp_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.15
                elif temp_codes[num][index] == " " and record == 0:
                    record = 1
                elif temp_codes[num][index] != " ":
                    record = 0
            return origin_len * 0.15

        codes_straightSort = (
            VGroup(
                *[
                    codeline_straightSort(code)
                    for code in straightSort_codes
                ]
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.05)
            .next_to(background.get_top(), DOWN, buff=0)
            .shift(RIGHT * 0.1 + DOWN * 0.25)
        )

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=2.5, stroke_color=BLUE, corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1, fill_color=RED).rotate(
            90 * DEGREES, axis=IN
        )
        arrow.scale(0.1)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))

        # 一键添加代码背景 and 代码
        self.add(background, codes_straightSort)
        # self.add(arrow, move_frame)
        move_frame.set_width(
            ignore_space_len(codes_straightSort[0], 0), stretch=True
        ).set_height(0.28, stretch=True).move_to(
            codes_straightSort[0]
        ).align_to(
            codes_straightSort[0], RIGHT
        ).shift(
            RIGHT * 0.05
        )

        # 箭头
        vec_j = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                color=BLACK,
                buff=0.3,
                fill_color=BLACK
            )
            .scale(0.35)
        )
        vec_pos = vec_j.copy()
        vec_j.next_to(rec_base[0], DOWN, buff=0.35)
        vec_pos.next_to(rec_base[1], DOWN, buff=0.35)
        vec_j_variables = (
            Text("j", font="思源宋体 Heavy", color=BLACK)
            .scale(0.6)
        )
        vec_pos_variables = (
            Text("pos", font="思源宋体 Heavy", color=BLACK)
            .scale(0.6)
            .next_to(vec_pos, DOWN, buff=0.15)
        )
        vec_j_variables.add_updater(lambda a: a.next_to(vec_j, DOWN, buff=0.1))
        vec_pos_variables.add_updater(
            lambda a: a.next_to(vec_pos, DOWN, buff=0.1))
        vec_j_all = VGroup(vec_j, vec_j_variables)
        vec_pos_all = VGroup(vec_pos, vec_pos_variables)
        # self.add(vec_j_all, vec_pos_all)

        # 变量框
        t2c = {
            "j": "#01cd74",
            "Size": BLUE,
            "R[j]": GOLD,
            "pos": PURPLE,
        }
        variable_rectangle = Rectangle(
            color="#003472", height=3, width=5, stroke_opacity=1).move_to(frame_variable)
        variable_Size = (
            Text("Size:  8", font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(1)
            .next_to(variable_rectangle.get_top(), DOWN, buff=0.7)
            .align_to(variable_rectangle, LEFT)
            .shift(RIGHT * 0.4)
        )
        variable_Rj = (
            Text("R[j]:", font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(1)
            .next_to(variable_rectangle.get_top(), DOWN, buff=0.7)
            .align_to(variable_rectangle, RIGHT)
            .shift(LEFT * 1)
        )
        variable_pos = (
            Text("pos:", font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(1)
            .next_to(variable_rectangle.get_bottom(), UP, buff=0.7)
            .align_to(variable_Size, LEFT)
        )
        variable_j = (
            Text("j:", font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(1)
            .next_to(variable_rectangle.get_bottom(), UP, buff=0.7)
            .align_to(variable_Rj, LEFT)
        )
        RJ_num = (
            Text(str(5), font="思源宋体 Heavy", color=BLACK)
            .scale(1)
            .next_to(variable_Rj, RIGHT, buff=0.3)
        )
        pos_num = (
            Text(str(1), font="思源宋体 Heavy", color=BLACK)
            .scale(1)
            .next_to(variable_pos, RIGHT, buff=0.3)
        )
        j_num = (
            Text(str(0), font="思源宋体 Heavy", color=BLACK)
            .scale(1)
            .next_to(variable_j, RIGHT, buff=0.3)
        )
        all_num = VGroup(RJ_num, pos_num, j_num)
        self.add(variable_rectangle, variable_Size,
                 variable_Rj, variable_pos, variable_j)

        # tmp 框
        tmp_rectangle = RoundedRectangle(
            stroke_width=8,
            stroke_color=GREEN_B,
            fill_color="#EBEBEB",
            fill_opacity=0,
            plot_depth=-1,
            corner_radius=0.05,
            sheen_factor=0.1,
            sheen_direction=UR,
        )
        tmp_rectangle.set_height(4, stretch=True).set_width(2, stretch=True)
        tmp_rectangle.move_to(frame_tmp)
        tmp_variables = (
            Text("Tmp", font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(1)
            .next_to(tmp_rectangle.get_bottom(), UP, buff=0.2)
        )
        self.add(tmp_rectangle, tmp_variables)

        """        
        int pos, j;
        Type tmp;
        for (pos = 1; pos < size; pos++)
        {
           tmp = R[pos];
           for (j = pos - 1; tmp < R[j] && j >= 0; j--)
              R[j + 1] = R[j];
           R[j + 1] = tmp;
        }
        """
        # 直接插入排序
        # """
        rec_base_position = rec_base.copy()  # 记录每个长方块的位置
        j_pos = 0  # j_pos 相当于 j
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait(0.5)
        self.play(
            move_frame.set_width,
            ignore_space_len(codes_straightSort[1], 1),
            move_frame.move_to,
            codes_straightSort[1],
            move_frame.align_to,
            codes_straightSort[1],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.05,
            move_frame.set_height,
            {"height": 0.28, "stretch": True},
            run_time=1.5,
        )
        self.wait(0.5)
        for pos in range(1, 8):
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_straightSort[2], 2),
                move_frame.move_to,
                codes_straightSort[2],
                move_frame.align_to,
                codes_straightSort[2],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.15,
                move_frame.set_height,
                {"height": 0.28, "stretch": True},
                run_time=1.5,
            )
            self.wait()
            if pos == 1:
                vec_pos_all.next_to(rec_base[pos], DOWN, buff=0.4)
                self.play(FadeInFrom(vec_pos_all, DOWN), FadeIn(all_num[1]))
            else:
                pos_num_tmp = (
                    Text(str(pos), font="思源宋体 Heavy", color=BLACK)
                    .scale(1)
                    .next_to(variable_pos, RIGHT, buff=0.3)
                )
                self.play(vec_pos_all.shift, RIGHT*1.3,
                          Transform(all_num[1], pos_num_tmp))
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_straightSort[4], 4),
                move_frame.move_to,
                codes_straightSort[4],
                move_frame.align_to,
                codes_straightSort[4],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.28, "stretch": True},
                run_time=1.5,
            )
            self.wait()
            tmp = rec_height_chaos[pos]
            # del rec_map[pos] num_map[pos]
            self.play(FadeOut(rec_base[pos]), FadeOut(rec_coordinate[pos]))
            rec_base[pos].move_to(frame_tmp)
            rec_coordinate[pos].move_to(frame_tmp)
            self.play(FadeIn(rec_base[pos]), FadeIn(rec_coordinate[pos]))
            self.wait()
            for j in range(pos-1, -1, -1):
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_straightSort[5], 5),
                    move_frame.move_to,
                    codes_straightSort[5],
                    move_frame.align_to,
                    codes_straightSort[5],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.15,
                    move_frame.set_height,
                    {"height": 0.28, "stretch": True},
                    run_time=1.5,
                )
                self.wait()
                Rj_num_tmp = (
                    Text(num_map[j].text, font="思源宋体 Heavy", color=BLACK)
                    .scale(1)
                    .next_to(variable_Rj, RIGHT, buff=0.3)
                )
                j_num_tmp = (
                    Text(str(j), font="思源宋体 Heavy", color=BLACK)
                    .scale(1)
                    .next_to(variable_j, RIGHT, buff=0.3)
                )
                if j == pos-1:
                    vec_j_all.move_to(vec_pos_all).align_to(
                        vec_pos_all, UP).shift(LEFT*1.3)
                    if j == 0:
                        self.play(FadeInFrom(vec_j_all, RIGHT),
                                  FadeIn(all_num[0]), FadeIn(all_num[2]))
                    elif j_pos == 0:
                        self.play(FadeInFrom(vec_j_all, RIGHT),
                                  Transform(all_num[0], Rj_num_tmp), Transform(all_num[2], j_num_tmp))
                    else:
                        self.play(FadeInFrom(vec_j_all, RIGHT), Transform(
                            all_num[0], Rj_num_tmp), Transform(all_num[2], j_num_tmp))
                else:
                    self.play(vec_j_all.shift, LEFT*1.3, Transform(
                        all_num[0], Rj_num_tmp), Transform(all_num[2], j_num_tmp))
                self.wait()
                # rec_height_chaos 相当于 R
                j_pos = j
                if tmp < rec_height_chaos[j]:
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(codes_straightSort[6], 6),
                        move_frame.move_to,
                        codes_straightSort[6],
                        move_frame.align_to,
                        codes_straightSort[6],
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.28, "stretch": True},
                        run_time=1.5,
                    )
                    self.wait()
                    rec_height_chaos[j+1] = rec_height_chaos[j]
                    self.play(rec_map[j].move_to, rec_base_position[j+1],
                              rec_map[j].align_to, rec_base_position[j+1], DOWN,
                              num_map[j].shift, RIGHT*1.3)
                    # del rec_map[j] num_map[pos]
                    rec_map[j+1] = rec_map[j]
                    num_map[j+1] = num_map[j]
                    self.wait(0.5)
                else:
                    j_pos += 1
                    break
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_straightSort[5], 5),
                move_frame.move_to,
                codes_straightSort[5],
                move_frame.align_to,
                codes_straightSort[5],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.15,
                move_frame.set_height,
                {"height": 0.28, "stretch": True},
                run_time=1.5,
            )
            self.wait()
            if j_pos != 0:
                pass
            else:
                Rj_num_tmp = (
                    Text(num_map[j_pos].text, font="思源宋体 Heavy", color=WHITE)
                    .scale(1)
                    .next_to(variable_Rj, RIGHT, buff=0.3)
                )
                j_num_tmp = (
                    Text(str(-1), font="思源宋体 Heavy", color=BLACK)
                    .scale(1)
                    .next_to(variable_j, RIGHT, buff=0.3)
                )
                self.play(vec_j_all.shift, LEFT*0.6, FadeIn(extra_subscript),
                          Transform(all_num[0], Rj_num_tmp), Transform(all_num[2], j_num_tmp))
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_straightSort[7], 7),
                move_frame.move_to,
                codes_straightSort[7],
                move_frame.align_to,
                codes_straightSort[7],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.28, "stretch": True},
                run_time=1.5,
            )
            self.wait()
            rec_height_chaos[j_pos] = tmp
            rec_map[j_pos] = rec_base[pos]
            num_map[j_pos] = rec_coordinate[pos]
            self.play(FadeOut(rec_base[pos]), FadeOut(rec_coordinate[pos]))
            rec_base[pos].move_to(rec_base_position[j_pos])
            rec_base[pos].align_to(rec_base_position[j_pos], DOWN)
            rec_coordinate[pos].move_to(rec_map[j_pos])
            self.play(FadeIn(rec_base[pos]), FadeIn(rec_coordinate[pos]))
            self.wait()
            if j_pos != 0:
                self.play(FadeOut(vec_j_all))
            else:
                self.play(FadeOut(vec_j_all), FadeOut(extra_subscript))
            self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(codes_straightSort[2], 2),
            move_frame.move_to,
            codes_straightSort[2],
            move_frame.align_to,
            codes_straightSort[2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.15,
            move_frame.set_height,
            {"height": 0.28, "stretch": True},
            run_time=1.5,
        )
        self.wait()
        pos_num_tmp = (
            Text(str(8), font="思源宋体 Heavy", color=BLACK)
            .scale(1)
            .next_to(variable_pos, RIGHT, buff=0.3)
        )
        self.play(FadeOutAndShift(vec_pos_all, RIGHT),
                  Transform(all_num[1], pos_num_tmp))
        self.wait()
        # """


class binaryInsertSort(Scene_White):
    def construct(self):
        # global
        # Frame 整体框架
        # height: 8  *  width: 14.2
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=1,
            fill_color=WHITE,
            fill_opacity=1,
            height=4.5,
            width=11.2,
        ).to_corner(UL, buff=0)
        frame_tmp = Rectangle(
            color=GREEN, stroke_opacity=1, height=4.5, width=3,
        ).to_corner(UR, buff=0)
        frame_code = Rectangle(
            color=BLUE, stroke_opacity=1, height=3.5, width=7.1+2.5,
        ).to_corner(DL, buff=0)
        frame_variable = Rectangle(
            color=RED, stroke_opacity=1, height=3.5, width=7.1-2.5,
        ).to_corner(DR, buff=0)
        self.add(frame_animation, frame_code, frame_variable)

        # --------------- 动画框架 ---------------
        # 标题
        title = (
            Text("折半插入排序", font="思源宋体 Heavy", color=BLACK)
            .scale(0.8)
            .to_corner(UP)
            .shift(UP*0.25)
        )
        self.add(title)
        # 基准长方形
        rectangle_base = MyRectangle(
            fill_color=BLUE, color=BLUE, height=2.5, width=0.8, fill_opacity=1, opacity=1, stroke_opacity=1)
        # 存储待排序的长方块
        rec_base = VGroup()
        # 存储每个长方块的高度
        rec_height = []
        for i in range(8):
            highest = 2.5
            shortest = 0.5
            gap = (highest-shortest)/7
            rec_height_element = shortest+gap*i
            rec_height.append(rec_height_element)
        # 打乱长方块的顺序
        chaos = [5, 1, 2, 7, 0, 6, 3, 4]  # 自定义顺序
        rec_height_chaos = []
        for i in range(8):
            rec_height_chaos.append(rec_height[chaos[i]])
        for i in range(8):
            rectangle_order = rectangle_base.copy()
            rectangle_order.set_height(rec_height_chaos[i], stretch=True)
            rec_base.add(rectangle_order.copy())
        rec_base.arrange(RIGHT, aligned_edge=DOWN, buff=0.5)
        rec_base.move_to(frame_animation).shift(UP*0.2)
        # 各方块下标
        rec_subscript = VGroup()
        for i in range(8):
            subscript = (
                Text(str(i), font="思源宋体 Heavy", color=BLACK)
                .scale(0.4)
                .next_to(rec_base[i], DOWN, buff=0.1)
            )
            rec_subscript.add(subscript)
        # 额外的 -1 下标
        extra_subscript = (
            Text(str(-1), font="思源宋体 Heavy", color=BLACK)
            .scale(0.4)
            .move_to(rec_subscript[0])
            .shift(LEFT*0.6)
        )
        # 各方块坐标
        rec_coordinate = VGroup()
        for i in range(8):
            coordinate = (
                Text(str(chaos[i]), font="江西拙楷", color=BLACK)
                .scale(0.7)
                .move_to(rec_base[i])
            )
            # coordinate.add_updater(lambda a: a.move_to(rec_base[i]))
            rec_coordinate.add(coordinate)
        # 映射表
        rec_map = {0: rec_base[0], 1: rec_base[1], 2: rec_base[2], 3: rec_base[3],
                   4: rec_base[4], 5: rec_base[5], 6: rec_base[6], 7: rec_base[7]}
        num_map = {0: rec_coordinate[0], 1: rec_coordinate[1], 2: rec_coordinate[2], 3: rec_coordinate[3],
                   4: rec_coordinate[4], 5: rec_coordinate[5], 6: rec_coordinate[6], 7: rec_coordinate[7]}
        self.add(rec_base, rec_subscript, rec_coordinate)
        # self.add(extra_subscript)

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
        background.set_height(3, stretch=True).set_width(9.2, stretch=True)
        background.move_to(frame_code)

        # 代码中间线
        middle_line = DashedLine(np.array([0, 0, 0]),
                                 np.array([0, 3, 0]), color=BLACK, stroke_width=1.0).move_to(frame_code)

        # 代码 + 移动框
        class codeline_binaryInsertSort(Text):
            CONFIG = {
                "size": 0.45,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        def ignore_space_len(code, num):
            origin_len = len(code)
            begin = origin_len - 1
            record = 0
            temp_codes = binaryInsertSort_codes
            for index in range(begin, 0, -1):
                if temp_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.125
                elif temp_codes[num][index] == " " and record == 0:
                    record = 1
                elif temp_codes[num][index] != " ":
                    record = 0
            return origin_len * 0.125

        codes_binaryInsertSort_left = (
            VGroup(
                *[
                    codeline_binaryInsertSort(code)
                    for code in binaryInsertSort_codes[:11]
                ]
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.05)
            .next_to(background.get_top(), DOWN, buff=0)
            .shift(LEFT * 2.25 + DOWN * 0.15)
        )
        codes_binaryInsertSort_right = (
            VGroup(
                *[
                    codeline_binaryInsertSort(code)
                    for code in binaryInsertSort_codes[11:]
                ]
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.05)
            .next_to(background.get_top(), DOWN, buff=0)
            .shift(RIGHT * 2.25 + DOWN * 0.15)
        )
        codes_binaryInsertSort = VGroup(
            codes_binaryInsertSort_left, codes_binaryInsertSort_right)

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=2.5, stroke_color=BLUE, corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1, fill_color=RED).rotate(
            90 * DEGREES, axis=IN
        )
        arrow.scale(0.1)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))

        # 一键添加代码背景 and 代码
        self.add(background, middle_line, codes_binaryInsertSort)
        # self.add(arrow, move_frame)
        move_frame.set_width(
            ignore_space_len(codes_binaryInsertSort[0][0], 0), stretch=True
        ).set_height(0.28, stretch=True).move_to(
            codes_binaryInsertSort[0][0]
        ).align_to(
            codes_binaryInsertSort[0][0], RIGHT
        ).shift(
            RIGHT * 0.05
        )
        arrow.next_to(move_frame, LEFT, buff=0.1)

        # 箭头
        vec_j = (
            Arrow(
                np.array([0, -1, 0]),
                np.array([0, 1, 0]),
                color=BLACK,
                buff=0.3,
                fill_color=BLACK
            )
            .scale(0.35)
        )
        vec_pos = vec_j.copy()
        vec_high = vec_j.copy()
        vec_low = vec_j.copy()
        vec_mid = vec_j.copy()
        vec_j.next_to(rec_base[0], DOWN, buff=0.35)
        vec_pos.next_to(rec_base[1], DOWN, buff=0.35)
        vec_high.next_to(rec_base[2], DOWN, buff=0.35)
        vec_low.next_to(rec_base[3], DOWN, buff=0.35)
        vec_mid.next_to(rec_base[4], DOWN, buff=0.35)
        vec_j_variables = (
            Text("j", font="思源宋体 Heavy", color=BLACK)
            .scale(0.6)
        )
        vec_pos_variables = (
            Text("pos", font="思源宋体 Heavy", color=BLACK)
            .scale(0.6)
            .next_to(vec_pos, DOWN, buff=0.15)
        )
        vec_high_variables = (
            Text("high", font="思源宋体 Heavy", color=BLACK)
            .scale(0.6)
            .next_to(vec_high, DOWN, buff=0.15)
        )
        vec_low_variables = (
            Text("low", font="思源宋体 Heavy", color=BLACK)
            .scale(0.6)
            .next_to(vec_low, DOWN, buff=0.15)
        )
        vec_mid_variables = (
            Text("mid", font="思源宋体 Heavy", color=BLACK)
            .scale(0.6)
            .next_to(vec_mid, DOWN, buff=0.15)
        )
        vec_j_variables.add_updater(lambda a: a.next_to(vec_j, DOWN, buff=0.1))
        vec_pos_variables.add_updater(
            lambda a: a.next_to(vec_pos, DOWN, buff=0.1))
        vec_high_variables.add_updater(
            lambda a: a.next_to(vec_high, DOWN, buff=0.05))
        vec_low_variables.add_updater(
            lambda a: a.next_to(vec_low, DOWN, buff=0.05))
        vec_mid_variables.add_updater(
            lambda a: a.next_to(vec_mid, DOWN, buff=0.05))
        vec_j_all = VGroup(vec_j, vec_j_variables)
        vec_pos_all = VGroup(vec_pos, vec_pos_variables)
        vec_high_all = VGroup(vec_high, vec_high_variables)
        vec_low_all = VGroup(vec_low, vec_low_variables)
        vec_mid_all = VGroup(vec_mid, vec_mid_variables)
        # self.add(vec_j_all, vec_pos_all, vec_high_all, vec_low_all, vec_mid_all)

        # 变量框
        t2c = {
            "j": "#01cd74",
            "mid": GREEN,
            "Size": BLUE,
            "R[mid]": GOLD,
            "pos": PURPLE,
            "high": RED,
            "low": "#da1884",
        }
        variable_rectangle = Rectangle(
            color="#003472", height=3, width=4, stroke_opacity=1).move_to(frame_variable)
        variable_Size = (
            Text("Size:  8", font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(0.8)
            .next_to(variable_rectangle.get_top(), DOWN, buff=0.2)
            .align_to(variable_rectangle, LEFT)
            .shift(RIGHT * 0.25)
        )
        variable_high = (
            Text("high:", font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(0.8)
            .next_to(variable_Size, DOWN, buff=0.3)
            .align_to(variable_Size, LEFT)
        )
        variable_low = (
            Text("low:", font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(0.8)
            .next_to(variable_high, DOWN, buff=0.3)
            .align_to(variable_Size, LEFT)
        )
        variable_j = (
            Text("j:", font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(0.8)
            .next_to(variable_low, DOWN, buff=0.3)
            .align_to(variable_Size, LEFT)
        )
        variable_Rm = (
            Text("R[mid]:", font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(0.8)
            .next_to(variable_rectangle.get_top(), DOWN, buff=0.2)
            .align_to(variable_rectangle, RIGHT)
            .shift(LEFT * 0.6)
        )
        variable_mid = (
            Text("mid:", font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(0.8)
            .next_to(variable_Rm, DOWN, buff=0.3)
            .align_to(variable_Rm, LEFT)
            .shift(RIGHT * 0.2)
        )
        variable_pos = (
            Text("pos:", font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(0.8)
            .next_to(variable_mid, DOWN, buff=0.4)
            .align_to(variable_Rm, LEFT)
            .shift(RIGHT * 0.2)
        )
        Rm_num = (
            Text(str(5), font="思源宋体 Heavy", color=BLACK)
            .scale(0.8)
            .next_to(variable_Rm, RIGHT, buff=0.2)
        )
        high_num = (
            Text(str(0), font="思源宋体 Heavy", color=BLACK)
            .scale(0.8)
            .next_to(variable_high, RIGHT, buff=0.2)
        )
        mid_num = (
            Text(str(0), font="思源宋体 Heavy", color=BLACK)
            .scale(0.8)
            .next_to(variable_mid, RIGHT, buff=0.2)
        )
        low_num = (
            Text(str(0), font="思源宋体 Heavy", color=BLACK)
            .scale(0.8)
            .next_to(variable_low, RIGHT, buff=0.2)
        )
        pos_num = (
            Text(str(1), font="思源宋体 Heavy", color=BLACK)
            .scale(0.8)
            .next_to(variable_pos, RIGHT, buff=0.2)
        )
        j_num = (
            Text(str(0), font="思源宋体 Heavy", color=BLACK)
            .scale(0.8)
            .next_to(variable_j, RIGHT, buff=0.2)
        )
        all_num = VGroup(Rm_num, high_num, mid_num, low_num, pos_num, j_num)
        self.add(variable_rectangle, variable_Size, variable_high, variable_low,
                 variable_j, variable_Rm, variable_mid, variable_pos)
        # self.add(all_num)

        # tmp 框
        tmp_rectangle = RoundedRectangle(
            stroke_width=8,
            stroke_color=GREEN_B,
            fill_color="#EBEBEB",
            fill_opacity=0,
            plot_depth=-1,
            corner_radius=0.05,
            sheen_factor=0.1,
            sheen_direction=UR,
        )
        tmp_rectangle.set_height(4, stretch=True).set_width(2, stretch=True)
        tmp_rectangle.move_to(frame_tmp)
        tmp_variables = (
            Text("Tmp", font="思源宋体 Heavy", color=BLACK, t2c=t2c)
            .scale(1)
            .next_to(tmp_rectangle.get_bottom(), UP, buff=0.2)
        )
        self.add(tmp_rectangle, tmp_variables)

        """
        int pos, j, low, high, mid;
        Type tmp;
        for (pos = 1; pos < size; pos++)
        {
           tmp = R[pos];
           low = 0;
           high = pos - 1;
           while (low <= high)
           {
              mid = (low + high) / 2;
              if (tmp < R[mid])
                 high = mid - 1;
              else
                 low = mid + 1;
           }
           for (j = pos - 1; j >= low; j--)
              R[j + 1] = R[j];
           R[low] = tmp;
        }
        """
        # 折半插入排序
        # """
        rec_base_position = rec_base.copy()  # 记录每个长方块的位置
        j_pos = 0  # j_pos 相当于 j
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait(0.5)
        self.play(
            move_frame.set_width,
            ignore_space_len(codes_binaryInsertSort[0][1], 1),
            move_frame.move_to,
            codes_binaryInsertSort[0][1],
            move_frame.align_to,
            codes_binaryInsertSort[0][1],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.05,
            move_frame.set_height,
            {"height": 0.28, "stretch": True},
            run_time=1.5,
        )
        self.wait(0.5)
        for pos in range(1, 4):
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_binaryInsertSort[0][2], 2),
                move_frame.move_to,
                codes_binaryInsertSort[0][2],
                move_frame.align_to,
                codes_binaryInsertSort[0][2],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.28, "stretch": True},
                run_time=1.5,
            )
            self.wait()
            if pos == 1:
                vec_pos_all.next_to(rec_base[pos], DOWN, buff=0.4)
                self.play(FadeInFrom(vec_pos_all, DOWN), FadeIn(all_num[4]))
            else:
                pos_num_tmp = (
                    Text(str(pos), font="思源宋体 Heavy", color=BLACK)
                    .scale(0.8)
                    .next_to(variable_pos, RIGHT, buff=0.2)
                )
                self.play(vec_pos_all.shift, RIGHT*1.3,
                          Transform(all_num[4], pos_num_tmp))
            self.wait()
            tmp = rec_height_chaos[pos]
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_binaryInsertSort[0][4], 4),
                move_frame.move_to,
                codes_binaryInsertSort[0][4],
                move_frame.align_to,
                codes_binaryInsertSort[0][4],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.28, "stretch": True},
                run_time=1.5,
            )
            self.wait()
            self.play(FadeOut(rec_base[pos]), FadeOut(rec_coordinate[pos]))
            rec_base[pos].move_to(frame_tmp)
            rec_coordinate[pos].move_to(frame_tmp)
            self.play(FadeIn(rec_base[pos]), FadeIn(rec_coordinate[pos]))
            self.wait()
            low = 0
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_binaryInsertSort[0][5], 5),
                move_frame.move_to,
                codes_binaryInsertSort[0][5],
                move_frame.align_to,
                codes_binaryInsertSort[0][5],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.28, "stretch": True},
                run_time=1.5,
            )
            self.wait()
            if pos == 1:
                vec_low_all.next_to(rec_map[0], DOWN, buff=0.4)
                self.play(FadeInFrom(vec_low_all, DOWN), FadeIn(all_num[3]))
            else:
                vec_low_all.next_to(rec_map[0], DOWN, buff=0.4)
                low_num_tmp = (
                    Text(str(0), font="思源宋体 Heavy", color=BLACK)
                    .scale(0.8)
                    .next_to(variable_low, RIGHT, buff=0.2)
                )
                self.play(FadeInFrom(vec_low_all, DOWN),
                          Transform(all_num[3], low_num_tmp))
            self.wait()
            high = pos - 1
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_binaryInsertSort[0][6], 6),
                move_frame.move_to,
                codes_binaryInsertSort[0][6],
                move_frame.align_to,
                codes_binaryInsertSort[0][6],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.28, "stretch": True},
                run_time=1.5,
            )
            self.wait()
            if pos == 1:
                vec_high_all.next_to(rec_map[0], DOWN, buff=0.4)
                self.play(FadeInFrom(vec_high_all, DOWN), FadeIn(all_num[1]))
            else:
                vec_high_all.next_to(rec_map[high], DOWN, buff=0.4)
                high_num_tmp = (
                    Text(str(int(high)), font="思源宋体 Heavy", color=BLACK)
                    .scale(0.8)
                    .next_to(variable_high, RIGHT, buff=0.2)
                )
                self.play(FadeInFrom(vec_high_all, DOWN),
                          Transform(all_num[1], high_num_tmp))
            self.wait()
            old_mid = -1  # 记录旧的 mid 的值
            first_mid == True  # 记录 mid 是否第一次出现
            while low <= high:
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_binaryInsertSort[0][7], 7),
                    move_frame.move_to,
                    codes_binaryInsertSort[0][7],
                    move_frame.align_to,
                    codes_binaryInsertSort[0][7],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.28, "stretch": True},
                    run_time=1.5,
                )
                self.wait()
                mid = int((low + high) / 2)
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_binaryInsertSort[0][9], 9),
                    move_frame.move_to,
                    codes_binaryInsertSort[0][9],
                    move_frame.align_to,
                    codes_binaryInsertSort[0][9],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.28, "stretch": True},
                    run_time=1.5,
                )
                self.wait()
                if pos == 1:
                    vec_mid_all.next_to(rec_map[0], DOWN, buff=0.4)
                    self.play(FadeInFrom(vec_mid_all, DOWN),
                              FadeIn(all_num[0]), FadeIn(all_num[2]))
                else:
                    vec_mid_all.next_to(rec_map[int(mid)], DOWN, buff=0.4)
                    mid_num_tmp = (
                        Text(str(int(mid)), font="思源宋体 Heavy", color=BLACK)
                        .scale(0.8)
                        .next_to(variable_mid, RIGHT, buff=0.2)
                    )
                    mid_Rm_tmp = (
                        Text(
                            str(int(rec_height_chaos[int(mid)])), font="思源宋体 Heavy", color=BLACK)
                        .scale(0.8)
                        .next_to(variable_Rm, RIGHT, buff=0.2)
                    )
                    if first_mid == True:
                        first_mid = False
                        self.play(FadeInFrom(vec_mid_all, DOWN),
                                  Transform(all_num[0], mid_Rm_tmp), Transform(all_num[2], mid_num_tmp))
                    else:
                        self.play(vec_mid_all.shift, LEFT*1.3*(old_mid-mid),
                                  Transform(all_num[0], mid_Rm_tmp), Transform(all_num[2], mid_num_tmp))
                old_mid = mid
                self.wait()
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_binaryInsertSort[0][10], 10),
                    move_frame.move_to,
                    codes_binaryInsertSort[0][10],
                    move_frame.align_to,
                    codes_binaryInsertSort[0][10],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.28, "stretch": True},
                    run_time=1.5,
                )
                self.wait()
                if tmp < rec_height_chaos[int(mid)]:
                    high = mid-1
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(codes_binaryInsertSort[1][0], 11),
                        move_frame.move_to,
                        codes_binaryInsertSort[1][0],
                        move_frame.align_to,
                        codes_binaryInsertSort[1][0],
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.28, "stretch": True},
                        run_time=1.5,
                    )
                    self.wait()
                    high_num_tmp = (
                        Text(str(int(high)), font="思源宋体 Heavy", color=BLACK)
                        .scale(0.8)
                        .next_to(variable_high, RIGHT, buff=0.2)
                    )
                    if high == -1:
                        self.play(vec_high_all.shift, (LEFT*1.3*(mid-high-1)+LEFT*0.6),
                                  FadeIn(extra_subscript), Transform(all_num[1], high_num_tmp))
                    else:
                        self.play(vec_high_all.shift, LEFT*1.3*(mid-high),
                                  Transform(all_num[1], high_num_tmp))
                    self.wait()
                else:
                    low = mid+1
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(codes_binaryInsertSort[1][1], 12),
                        move_frame.move_to,
                        codes_binaryInsertSort[1][1],
                        move_frame.align_to,
                        codes_binaryInsertSort[1][1],
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.28, "stretch": True},
                        run_time=1.5,
                    )
                    self.wait(0.5)
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(codes_binaryInsertSort[1][2], 13),
                        move_frame.move_to,
                        codes_binaryInsertSort[1][2],
                        move_frame.align_to,
                        codes_binaryInsertSort[1][2],
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.28, "stretch": True},
                        run_time=1.5,
                    )
                    self.wait()
                    low_num_tmp = (
                        Text(str(low), font="思源宋体 Heavy", color=BLACK)
                        .scale(0.8)
                        .next_to(variable_low, RIGHT, buff=0.2)
                    )
                    self.play(vec_low_all.shift, RIGHT*1.3*(low-mid),
                              Transform(all_num[3], low_num_tmp))
                    self.wait()
            if high == -1:
                self.play(FadeOut(vec_high_all), FadeOut(
                    vec_mid_all), FadeOut(extra_subscript))
            else:
                self.play(FadeOut(vec_high_all), FadeOut(vec_mid_all))
            through_for = False
            for j in range(pos-1, int(low)-1, -1):
                through_for = True
                j_pos = j
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_binaryInsertSort[1][4], 15),
                    move_frame.move_to,
                    codes_binaryInsertSort[1][4],
                    move_frame.align_to,
                    codes_binaryInsertSort[1][4],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.28, "stretch": True},
                    run_time=1.5,
                )
                self.wait()
                if pos == 1:
                    if j == pos-1:
                        vec_j_all.next_to(rec_map[0], DOWN, buff=0.4)
                        self.play(FadeInFrom(vec_j_all, DOWN),
                                  FadeIn(all_num[5]))
                    else:
                        j_num_tmp = (
                            Text(str(j), font="思源宋体 Heavy", color=BLACK)
                            .scale(0.8)
                            .next_to(variable_j, RIGHT, buff=0.2)
                        )
                        self.play(vec_j_all.shift, LEFT*1.3,
                                  Transform(all_num[5], j_num_tmp))
                else:
                    j_num_tmp = (
                        Text(str(j), font="思源宋体 Heavy", color=BLACK)
                        .scale(0.8)
                        .next_to(variable_j, RIGHT, buff=0.2)
                    )
                    if j == pos-1:
                        vec_j_all.next_to(rec_map[j], DOWN, buff=0.4)
                        self.play(FadeInFrom(vec_j_all, DOWN),
                                  Transform(all_num[5], j_num_tmp))
                    else:
                        self.play(vec_j_all.shift, LEFT*1.3,
                                  Transform(all_num[5], j_num_tmp))
                self.wait()
                rec_height_chaos[j+1] = rec_height_chaos[j]
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_binaryInsertSort[1][5], 16),
                    move_frame.move_to,
                    codes_binaryInsertSort[1][5],
                    move_frame.align_to,
                    codes_binaryInsertSort[1][5],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.28, "stretch": True},
                    run_time=1.5,
                )
                self.wait()
                self.play(rec_map[j].move_to, rec_base_position[j+1],
                          rec_map[j].align_to, rec_base_position[j+1], DOWN,
                          num_map[j].shift, RIGHT*1.3)
                rec_map[j+1] = rec_map[j]
                num_map[j+1] = num_map[j]
                self.wait()
            # for 循环一开始相等就不会执行，因此要额外用 if 补充其他情况
            if through_for == False:
                j_num_tmp = (
                    Text(str(pos-1), font="思源宋体 Heavy", color=BLACK)
                    .scale(0.8)
                    .next_to(variable_j, RIGHT, buff=0.2)
                )
                vec_j_all.next_to(rec_map[pos-1], DOWN, buff=0.4)
                self.play(FadeInFrom(vec_j_all, DOWN),
                          Transform(all_num[5], j_num_tmp))
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_binaryInsertSort[1][4], 15),
                move_frame.move_to,
                codes_binaryInsertSort[1][4],
                move_frame.align_to,
                codes_binaryInsertSort[1][4],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.28, "stretch": True},
                run_time=1.5,
            )
            self.wait()
            j_num_tmp = (
                Text(str(j_pos-1), font="思源宋体 Heavy", color=BLACK)
                .scale(0.8)
                .next_to(variable_j, RIGHT, buff=0.2)
            )
            if through_for == True:
                if j_pos != 0:
                    self.play(vec_j_all.shift, LEFT*1.3,
                              Transform(all_num[5], j_num_tmp))
                else:
                    self.play(vec_j_all.shift, LEFT*0.6, FadeIn(extra_subscript),
                              Transform(all_num[5], j_num_tmp))
            self.wait()
            rec_height_chaos[int(low)] = tmp
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_binaryInsertSort[1][6], 17),
                move_frame.move_to,
                codes_binaryInsertSort[1][6],
                move_frame.align_to,
                codes_binaryInsertSort[1][6],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.28, "stretch": True},
                run_time=1.5,
            )
            self.wait()
            rec_height_chaos[int(low)] = tmp
            rec_map[int(low)] = rec_base[pos]
            num_map[int(low)] = rec_coordinate[pos]
            self.play(FadeOut(rec_base[pos]), FadeOut(rec_coordinate[pos]))
            rec_base[pos].move_to(rec_base_position[int(low)])
            rec_base[pos].align_to(rec_base_position[int(low)], DOWN)
            rec_coordinate[pos].move_to(rec_map[int(low)])
            self.play(FadeIn(rec_base[pos]), FadeIn(rec_coordinate[pos]))
            self.wait()
            if j_pos != 0 or (through_for == False):
                self.play(FadeOut(vec_j_all), FadeOut(vec_low_all))
            else:
                self.play(FadeOut(vec_j_all), FadeOut(
                    vec_low_all), FadeOut(extra_subscript))
            self.wait()
        self.play(
            move_frame.set_width,
            ignore_space_len(codes_binaryInsertSort[0][2], 2),
            move_frame.move_to,
            codes_binaryInsertSort[0][2],
            move_frame.align_to,
            codes_binaryInsertSort[0][2],
            RIGHT,
            move_frame.shift,
            RIGHT * 0.05,
            move_frame.set_height,
            {"height": 0.28, "stretch": True},
            run_time=1.5,
        )
        self.wait()
        pos_num_tmp = (
            Text(str(8), font="思源宋体 Heavy", color=BLACK)
            .scale(0.8)
            .next_to(variable_pos, RIGHT, buff=0.2)
        )
        self.play(FadeOutAndShift(vec_pos_all, RIGHT),
                  Transform(all_num[4], pos_num_tmp))
        self.wait()
        # """


