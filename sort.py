from manimlib.imports import *
from manim_tuan import *
"""
TODO
0: 从二分查找(binaryInsertSort)开始, 整体采用了伪面向对象(OOP)模式, 望早日(重写时)建立真正的面向对象模型
1: shellSort 先指针变换,再变换数字
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
    "   for (j = 0; j < size - i; ++j) {",
    "      if (R[j + 1] < R[j]) {",
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

quickSort_codes = [
    "void quickSort(Type S[], int low, int high) {",
    "   int pivot;",
    "   if (low >= high)",
    "      return;",
    "   pivot = partition(S, low, high);",
    "   quickSort(S, low, pivot - 1);",
    "   quickSort(S, pivot + 1, high);",
    "}",
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
    "void siftDown (Type R[], int pos, int size) {", "    int child;",
    "    Type tmp = R[pos];", "    for (; pos * 2 + 1 < size; pos = child)",
    "    {", "       child = pos * 2 + 1;",
    "       if (child != size - 1 && R[child + 1] > R[child])",
    "          child++;", "       if (R[child] > tmp)",
    "          R[pos] = R[child];", "       else", "          break;", "    }",
    "    R[pos] = tmp;", "}"
]

heapSort_codes = [
    "void heapSort(Type R[],int size) {",
    "    int i;",
    "    for (i = size / 2 - 1; i >= 0; i--)",
    "       siftDown(R, i, size);",
    "    for (i = size - 1; i > 0; i--)",
    "    {",
    "       swap(R[0], R[i]);",
    "       siftDown(R, 0, i);",
    "    }",
    "}",
]

merge_codes = [
    "void merge(Type R[], Type tmp[], int low, int mid, int high) {",
    "    int i = low, j = mid, k = 0;",
    "    while (i < mid && j <= high)",
    "       if (R[i] < R[j])",
    "          tmp[k++] = R[i++];",
    "       else",
    "          tmp[k++] = R[j++];",
    "    while (i < mid)",
    "       tmp[k++] = R[i++];",
    "    while (j <= high)",
    "       tmp[k++] = R[j++];",
    "    for (k = 0, i = low; i <= high;)",
    "       R[i++] = tmp[k++];",
    "}",
]

mergeSort_codes = [
    "void mergeSort(Type R[], Type tmp[], int low, int high) {",
    "    if (low == high)",
    "       return;",
    "    int mid = (low + high) / 2;",
    "    mergeSort(R, tmp, low, mid);",
    "    mergeSort(R, tmp, mid + 1, high);",
    "    merge(R, tmp, low, mid + 1, high);",
    "}",
]

mergeSort_vice_codes = [
    "Type *tmp = new Type[size];",
    "mergeSort(R, tmp, 0, size - 1);",
    "delete[] tmp;",
]


class Scene_White(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "use_plot_depth": True,
        }
    }


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
            color=GREEN,
            stroke_opacity=0,
            height=4.5,
            width=3,
        ).to_corner(UR, buff=0)
        frame_code = Rectangle(
            color=BLUE,
            stroke_opacity=0,
            height=3.5,
            width=7.1 + 1,
        ).to_corner(DL, buff=0)
        frame_variable = Rectangle(
            color=RED,
            stroke_opacity=0,
            height=3.5,
            width=7.1 - 1,
        ).to_corner(DR, buff=0)
        self.add(frame_animation, frame_code, frame_variable)

        # --------------- 动画框架 ---------------
        # 标题
        title = (Text("直接插入排序", font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).to_corner(UP).shift(UP * 0.25))
        self.add(title)
        # 基准长方形
        rectangle_base = MyRectangle(fill_color=BLUE,
                                     color=BLUE,
                                     height=2.5,
                                     width=0.8,
                                     fill_opacity=1,
                                     opacity=1,
                                     stroke_opacity=1)
        # 存储待排序的长方块
        rec_base = VGroup()
        # 存储每个长方块的高度
        rec_height = []
        for i in range(8):
            highest = 2.5
            shortest = 0.5
            gap = (highest - shortest) / 7
            rec_height_element = shortest + gap * i
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
        rec_base.move_to(frame_animation).shift(UP * 0.2)
        # 各方块下标
        rec_subscript = VGroup()
        for i in range(8):
            subscript = (Text(str(i), font="思源宋体 Heavy",
                              color=BLACK).scale(0.4).next_to(rec_base[i],
                                                              DOWN,
                                                              buff=0.1))
            rec_subscript.add(subscript)
        # 额外的 -1 下标
        extra_subscript = (Text(str(-1), font="思源宋体 Heavy",
                                color=BLACK).scale(0.4).move_to(
                                    rec_subscript[0]).shift(LEFT * 0.6))
        # 各方块坐标
        rec_coordinate = VGroup()
        for i in range(8):
            coordinate = (Text(str(chaos[i]), font="江西拙楷",
                               color=BLACK).scale(0.7).move_to(rec_base[i]))
            # coordinate.add_updater(lambda a: a.move_to(rec_base[i]))
            rec_coordinate.add(coordinate)
        # 映射表
        rec_map = {
            0: rec_base[0],
            1: rec_base[1],
            2: rec_base[2],
            3: rec_base[3],
            4: rec_base[4],
            5: rec_base[5],
            6: rec_base[6],
            7: rec_base[7]
        }
        num_map = {
            0: rec_coordinate[0],
            1: rec_coordinate[1],
            2: rec_coordinate[2],
            3: rec_coordinate[3],
            4: rec_coordinate[4],
            5: rec_coordinate[5],
            6: rec_coordinate[6],
            7: rec_coordinate[7]
        }
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

        codes_straightSort = (VGroup(
            *[codeline_straightSort(code)
              for code in straightSort_codes]).arrange(
                  DOWN, aligned_edge=LEFT,
                  buff=0.05).next_to(background.get_top(), DOWN,
                                     buff=0).shift(RIGHT * 0.1 + DOWN * 0.25))

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=2.5,
            stroke_color=BLUE,
            corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1,
                         fill_color=RED).rotate(90 * DEGREES, axis=IN)
        arrow.scale(0.1)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))

        # 一键添加代码背景 and 代码
        self.add(background, codes_straightSort)
        # self.add(arrow, move_frame)
        move_frame.set_width(
            ignore_space_len(codes_straightSort[0], 0),
            stretch=True).set_height(0.28, stretch=True).move_to(
                codes_straightSort[0]).align_to(codes_straightSort[0],
                                                RIGHT).shift(RIGHT * 0.05)

        # 箭头
        vec_j = (Arrow(np.array([0, -1, 0]),
                       np.array([0, 1, 0]),
                       color=BLACK,
                       buff=0.3,
                       fill_color=BLACK).scale(0.35))
        vec_pos = vec_j.copy()
        vec_j.next_to(rec_base[0], DOWN, buff=0.35)
        vec_pos.next_to(rec_base[1], DOWN, buff=0.35)
        vec_j_variables = (Text("j", font="思源宋体 Heavy",
                                color=BLACK).scale(0.6))
        vec_pos_variables = (Text("pos", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.6).next_to(vec_pos,
                                                                  DOWN,
                                                                  buff=0.15))
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
            color="#003472", height=3, width=5,
            stroke_opacity=1).move_to(frame_variable)
        variable_Size = (Text("Size:  8",
                              font="思源宋体 Heavy",
                              color=BLACK,
                              t2c=t2c).scale(1).next_to(
                                  variable_rectangle.get_top(), DOWN,
                                  buff=0.7).align_to(variable_rectangle,
                                                     LEFT).shift(RIGHT * 0.4))
        variable_Rj = (Text("R[j]:", font="思源宋体 Heavy", color=BLACK,
                            t2c=t2c).scale(1).next_to(
                                variable_rectangle.get_top(), DOWN,
                                buff=0.7).align_to(variable_rectangle,
                                                   RIGHT).shift(LEFT * 1))
        variable_pos = (Text(
            "pos:", font="思源宋体 Heavy", color=BLACK,
            t2c=t2c).scale(1).next_to(variable_rectangle.get_bottom(),
                                      UP,
                                      buff=0.7).align_to(variable_Size, LEFT))
        variable_j = (Text(
            "j:", font="思源宋体 Heavy", color=BLACK,
            t2c=t2c).scale(1).next_to(variable_rectangle.get_bottom(),
                                      UP,
                                      buff=0.7).align_to(variable_Rj, LEFT))
        RJ_num = (Text(str(5), font="思源宋体 Heavy",
                       color=BLACK).scale(1).next_to(variable_Rj,
                                                     RIGHT,
                                                     buff=0.3))
        pos_num = (Text(str(1), font="思源宋体 Heavy",
                        color=BLACK).scale(1).next_to(variable_pos,
                                                      RIGHT,
                                                      buff=0.3))
        j_num = (Text(str(0), font="思源宋体 Heavy",
                      color=BLACK).scale(1).next_to(variable_j,
                                                    RIGHT,
                                                    buff=0.3))
        all_num = VGroup(RJ_num, pos_num, j_num)
        self.add(variable_rectangle, variable_Size, variable_Rj, variable_pos,
                 variable_j)

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
        tmp_variables = (Text("Tmp", font="思源宋体 Heavy", color=BLACK,
                              t2c=t2c).scale(1).next_to(
                                  tmp_rectangle.get_bottom(), UP, buff=0.2))
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
            {
                "height": 0.28,
                "stretch": True
            },
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
                {
                    "height": 0.28,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()
            if pos == 1:
                vec_pos_all.next_to(rec_base[pos], DOWN, buff=0.4)
                self.play(FadeInFrom(vec_pos_all, DOWN), FadeIn(all_num[1]))
            else:
                pos_num_tmp = (Text(str(pos), font="思源宋体 Heavy",
                                    color=BLACK).scale(1).next_to(variable_pos,
                                                                  RIGHT,
                                                                  buff=0.3))
                self.play(vec_pos_all.shift, RIGHT * 1.3,
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
                {
                    "height": 0.28,
                    "stretch": True
                },
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
            for j in range(pos - 1, -1, -1):
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
                    {
                        "height": 0.28,
                        "stretch": True
                    },
                    run_time=1.5,
                )
                self.wait()
                Rj_num_tmp = (Text(num_map[j].text,
                                   font="思源宋体 Heavy",
                                   color=BLACK).scale(1).next_to(variable_Rj,
                                                                 RIGHT,
                                                                 buff=0.3))
                j_num_tmp = (Text(str(j), font="思源宋体 Heavy",
                                  color=BLACK).scale(1).next_to(variable_j,
                                                                RIGHT,
                                                                buff=0.3))
                if j == pos - 1:
                    vec_j_all.move_to(vec_pos_all).align_to(
                        vec_pos_all, UP).shift(LEFT * 1.3)
                    if j == 0:
                        self.play(FadeInFrom(vec_j_all, RIGHT),
                                  FadeIn(all_num[0]), FadeIn(all_num[2]))
                    elif j_pos == 0:
                        self.play(FadeInFrom(vec_j_all, RIGHT),
                                  Transform(all_num[0], Rj_num_tmp),
                                  Transform(all_num[2], j_num_tmp))
                    else:
                        self.play(FadeInFrom(vec_j_all, RIGHT),
                                  Transform(all_num[0], Rj_num_tmp),
                                  Transform(all_num[2], j_num_tmp))
                else:
                    self.play(vec_j_all.shift, LEFT * 1.3,
                              Transform(all_num[0], Rj_num_tmp),
                              Transform(all_num[2], j_num_tmp))
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
                        {
                            "height": 0.28,
                            "stretch": True
                        },
                        run_time=1.5,
                    )
                    self.wait()
                    rec_height_chaos[j + 1] = rec_height_chaos[j]
                    self.play(rec_map[j].move_to, rec_base_position[j + 1],
                              rec_map[j].align_to, rec_base_position[j + 1],
                              DOWN, num_map[j].shift, RIGHT * 1.3)
                    # del rec_map[j] num_map[pos]
                    rec_map[j + 1] = rec_map[j]
                    num_map[j + 1] = num_map[j]
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
                {
                    "height": 0.28,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()
            if j_pos != 0:
                pass
            else:
                Rj_num_tmp = (Text(num_map[j_pos].text,
                                   font="思源宋体 Heavy",
                                   color=WHITE).scale(1).next_to(variable_Rj,
                                                                 RIGHT,
                                                                 buff=0.3))
                j_num_tmp = (Text(str(-1), font="思源宋体 Heavy",
                                  color=BLACK).scale(1).next_to(variable_j,
                                                                RIGHT,
                                                                buff=0.3))
                self.play(vec_j_all.shift, LEFT * 0.6, FadeIn(extra_subscript),
                          Transform(all_num[0], Rj_num_tmp),
                          Transform(all_num[2], j_num_tmp))
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
                {
                    "height": 0.28,
                    "stretch": True
                },
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
            {
                "height": 0.28,
                "stretch": True
            },
            run_time=1.5,
        )
        self.wait()
        pos_num_tmp = (Text(str(8), font="思源宋体 Heavy",
                            color=BLACK).scale(1).next_to(variable_pos,
                                                          RIGHT,
                                                          buff=0.3))
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
            color=GREEN,
            stroke_opacity=1,
            height=4.5,
            width=3,
        ).to_corner(UR, buff=0)
        frame_code = Rectangle(
            color=BLUE,
            stroke_opacity=1,
            height=3.5,
            width=7.1 + 2.5,
        ).to_corner(DL, buff=0)
        frame_variable = Rectangle(
            color=RED,
            stroke_opacity=1,
            height=3.5,
            width=7.1 - 2.5,
        ).to_corner(DR, buff=0)
        self.add(frame_animation, frame_code, frame_variable)

        # --------------- 动画框架 ---------------
        # 标题
        title = (Text("折半插入排序", font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).to_corner(UP).shift(UP * 0.25))
        self.add(title)
        # 基准长方形
        rectangle_base = MyRectangle(fill_color=BLUE,
                                     color=BLUE,
                                     height=2.5,
                                     width=0.8,
                                     fill_opacity=1,
                                     opacity=1,
                                     stroke_opacity=1)
        # 存储待排序的长方块
        rec_base = VGroup()
        # 存储每个长方块的高度
        rec_height = []
        for i in range(8):
            highest = 2.5
            shortest = 0.5
            gap = (highest - shortest) / 7
            rec_height_element = shortest + gap * i
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
        rec_base.move_to(frame_animation).shift(UP * 0.2)
        # 各方块下标
        rec_subscript = VGroup()
        for i in range(8):
            subscript = (Text(str(i), font="思源宋体 Heavy",
                              color=BLACK).scale(0.4).next_to(rec_base[i],
                                                              DOWN,
                                                              buff=0.1))
            rec_subscript.add(subscript)
        # 额外的 -1 下标
        extra_subscript = (Text(str(-1), font="思源宋体 Heavy",
                                color=BLACK).scale(0.4).move_to(
                                    rec_subscript[0]).shift(LEFT * 0.6))
        # 各方块坐标
        rec_coordinate = VGroup()
        for i in range(8):
            coordinate = (Text(str(chaos[i]), font="江西拙楷",
                               color=BLACK).scale(0.7).move_to(rec_base[i]))
            # coordinate.add_updater(lambda a: a.move_to(rec_base[i]))
            rec_coordinate.add(coordinate)
        # 映射表
        rec_map = {
            0: rec_base[0],
            1: rec_base[1],
            2: rec_base[2],
            3: rec_base[3],
            4: rec_base[4],
            5: rec_base[5],
            6: rec_base[6],
            7: rec_base[7]
        }
        num_map = {
            0: rec_coordinate[0],
            1: rec_coordinate[1],
            2: rec_coordinate[2],
            3: rec_coordinate[3],
            4: rec_coordinate[4],
            5: rec_coordinate[5],
            6: rec_coordinate[6],
            7: rec_coordinate[7]
        }
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
                                 np.array([0, 3, 0]),
                                 color=BLACK,
                                 stroke_width=1.0).move_to(frame_code)

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

        codes_binaryInsertSort_left = (VGroup(*[
            codeline_binaryInsertSort(code)
            for code in binaryInsertSort_codes[:11]
        ]).arrange(DOWN, aligned_edge=LEFT,
                   buff=0.05).next_to(background.get_top(), DOWN,
                                      buff=0).shift(LEFT * 2.25 + DOWN * 0.15))
        codes_binaryInsertSort_right = (VGroup(*[
            codeline_binaryInsertSort(code)
            for code in binaryInsertSort_codes[11:]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.05).next_to(
            background.get_top(), DOWN,
            buff=0).shift(RIGHT * 2.25 + DOWN * 0.15))
        codes_binaryInsertSort = VGroup(codes_binaryInsertSort_left,
                                        codes_binaryInsertSort_right)

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=2.5,
            stroke_color=BLUE,
            corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1,
                         fill_color=RED).rotate(90 * DEGREES, axis=IN)
        arrow.scale(0.1)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))

        # 一键添加代码背景 and 代码
        self.add(background, middle_line, codes_binaryInsertSort)
        # self.add(arrow, move_frame)
        move_frame.set_width(ignore_space_len(codes_binaryInsertSort[0][0], 0),
                             stretch=True).set_height(
                                 0.28, stretch=True).move_to(
                                     codes_binaryInsertSort[0][0]).align_to(
                                         codes_binaryInsertSort[0][0],
                                         RIGHT).shift(RIGHT * 0.05)
        arrow.next_to(move_frame, LEFT, buff=0.1)

        # 箭头
        vec_j = (Arrow(np.array([0, -1, 0]),
                       np.array([0, 1, 0]),
                       color=BLACK,
                       buff=0.3,
                       fill_color=BLACK).scale(0.35))
        vec_pos = vec_j.copy()
        vec_high = vec_j.copy()
        vec_low = vec_j.copy()
        vec_mid = vec_j.copy()
        vec_j.next_to(rec_base[0], DOWN, buff=0.35)
        vec_pos.next_to(rec_base[1], DOWN, buff=0.35)
        vec_high.next_to(rec_base[2], DOWN, buff=0.35)
        vec_low.next_to(rec_base[3], DOWN, buff=0.35)
        vec_mid.next_to(rec_base[4], DOWN, buff=0.35)
        vec_j_variables = (Text("j", font="思源宋体 Heavy",
                                color=BLACK).scale(0.6))
        vec_pos_variables = (Text("pos", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.6).next_to(vec_pos,
                                                                  DOWN,
                                                                  buff=0.15))
        vec_high_variables = (Text("high", font="思源宋体 Heavy",
                                   color=BLACK).scale(0.6).next_to(vec_high,
                                                                   DOWN,
                                                                   buff=0.15))
        vec_low_variables = (Text("low", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.6).next_to(vec_low,
                                                                  DOWN,
                                                                  buff=0.15))
        vec_mid_variables = (Text("mid", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.6).next_to(vec_mid,
                                                                  DOWN,
                                                                  buff=0.15))
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
            color="#003472", height=3, width=4,
            stroke_opacity=1).move_to(frame_variable)
        variable_Size = (Text("Size:  8",
                              font="思源宋体 Heavy",
                              color=BLACK,
                              t2c=t2c).scale(0.8).next_to(
                                  variable_rectangle.get_top(), DOWN,
                                  buff=0.2).align_to(variable_rectangle,
                                                     LEFT).shift(RIGHT * 0.25))
        variable_high = (Text("high:", font="思源宋体 Heavy", color=BLACK,
                              t2c=t2c).scale(0.8).next_to(variable_Size,
                                                          DOWN,
                                                          buff=0.3).align_to(
                                                              variable_Size,
                                                              LEFT))
        variable_low = (Text("low:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(0.8).next_to(variable_high,
                                                         DOWN,
                                                         buff=0.3).align_to(
                                                             variable_Size,
                                                             LEFT))
        variable_j = (Text("j:", font="思源宋体 Heavy", color=BLACK,
                           t2c=t2c).scale(0.8).next_to(variable_low,
                                                       DOWN,
                                                       buff=0.3).align_to(
                                                           variable_Size,
                                                           LEFT))
        variable_Rm = (Text("R[mid]:", font="思源宋体 Heavy", color=BLACK,
                            t2c=t2c).scale(0.8).next_to(
                                variable_rectangle.get_top(), DOWN,
                                buff=0.2).align_to(variable_rectangle,
                                                   RIGHT).shift(LEFT * 0.6))
        variable_mid = (Text("mid:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(0.8).next_to(
                                 variable_Rm, DOWN,
                                 buff=0.3).align_to(variable_Rm,
                                                    LEFT).shift(RIGHT * 0.2))
        variable_pos = (Text("pos:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(0.8).next_to(
                                 variable_mid, DOWN,
                                 buff=0.4).align_to(variable_Rm,
                                                    LEFT).shift(RIGHT * 0.2))
        Rm_num = (Text(str(5), font="思源宋体 Heavy",
                       color=BLACK).scale(0.8).next_to(variable_Rm,
                                                       RIGHT,
                                                       buff=0.2))
        high_num = (Text(str(0), font="思源宋体 Heavy",
                         color=BLACK).scale(0.8).next_to(variable_high,
                                                         RIGHT,
                                                         buff=0.2))
        mid_num = (Text(str(0), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.2))
        low_num = (Text(str(0), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_low,
                                                        RIGHT,
                                                        buff=0.2))
        pos_num = (Text(str(1), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_pos,
                                                        RIGHT,
                                                        buff=0.2))
        j_num = (Text(str(0), font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).next_to(variable_j,
                                                      RIGHT,
                                                      buff=0.2))
        all_num = VGroup(Rm_num, high_num, mid_num, low_num, pos_num, j_num)
        self.add(variable_rectangle, variable_Size, variable_high,
                 variable_low, variable_j, variable_Rm, variable_mid,
                 variable_pos)
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
        tmp_variables = (Text("Tmp", font="思源宋体 Heavy", color=BLACK,
                              t2c=t2c).scale(1).next_to(
                                  tmp_rectangle.get_bottom(), UP, buff=0.2))
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
            {
                "height": 0.28,
                "stretch": True
            },
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
                {
                    "height": 0.28,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()
            if pos == 1:
                vec_pos_all.next_to(rec_base[pos], DOWN, buff=0.4)
                self.play(FadeInFrom(vec_pos_all, DOWN), FadeIn(all_num[4]))
            else:
                pos_num_tmp = (Text(str(pos), font="思源宋体 Heavy",
                                    color=BLACK).scale(0.8).next_to(
                                        variable_pos, RIGHT, buff=0.2))
                self.play(vec_pos_all.shift, RIGHT * 1.3,
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
                {
                    "height": 0.28,
                    "stretch": True
                },
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
                {
                    "height": 0.28,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()
            if pos == 1:
                vec_low_all.next_to(rec_map[0], DOWN, buff=0.4)
                self.play(FadeInFrom(vec_low_all, DOWN), FadeIn(all_num[3]))
            else:
                vec_low_all.next_to(rec_map[0], DOWN, buff=0.4)
                low_num_tmp = (Text(str(0), font="思源宋体 Heavy",
                                    color=BLACK).scale(0.8).next_to(
                                        variable_low, RIGHT, buff=0.2))
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
                {
                    "height": 0.28,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()
            if pos == 1:
                vec_high_all.next_to(rec_map[0], DOWN, buff=0.4)
                self.play(FadeInFrom(vec_high_all, DOWN), FadeIn(all_num[1]))
            else:
                vec_high_all.next_to(rec_map[high], DOWN, buff=0.4)
                high_num_tmp = (Text(str(int(high)),
                                     font="思源宋体 Heavy",
                                     color=BLACK).scale(0.8).next_to(
                                         variable_high, RIGHT, buff=0.2))
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
                    {
                        "height": 0.28,
                        "stretch": True
                    },
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
                    {
                        "height": 0.28,
                        "stretch": True
                    },
                    run_time=1.5,
                )
                self.wait()
                if pos == 1:
                    vec_mid_all.next_to(rec_map[0], DOWN, buff=0.4)
                    self.play(FadeInFrom(vec_mid_all, DOWN),
                              FadeIn(all_num[0]), FadeIn(all_num[2]))
                else:
                    vec_mid_all.next_to(rec_map[int(mid)], DOWN, buff=0.4)
                    mid_num_tmp = (Text(str(int(mid)),
                                        font="思源宋体 Heavy",
                                        color=BLACK).scale(0.8).next_to(
                                            variable_mid, RIGHT, buff=0.2))
                    mid_Rm_tmp = (Text(str(int(rec_height_chaos[int(mid)])),
                                       font="思源宋体 Heavy",
                                       color=BLACK).scale(0.8).next_to(
                                           variable_Rm, RIGHT, buff=0.2))
                    if first_mid == True:
                        first_mid = False
                        self.play(FadeInFrom(vec_mid_all, DOWN),
                                  Transform(all_num[0], mid_Rm_tmp),
                                  Transform(all_num[2], mid_num_tmp))
                    else:
                        self.play(vec_mid_all.shift,
                                  LEFT * 1.3 * (old_mid - mid),
                                  Transform(all_num[0], mid_Rm_tmp),
                                  Transform(all_num[2], mid_num_tmp))
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
                    {
                        "height": 0.28,
                        "stretch": True
                    },
                    run_time=1.5,
                )
                self.wait()
                if tmp < rec_height_chaos[int(mid)]:
                    high = mid - 1
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
                        {
                            "height": 0.28,
                            "stretch": True
                        },
                        run_time=1.5,
                    )
                    self.wait()
                    high_num_tmp = (Text(str(int(high)),
                                         font="思源宋体 Heavy",
                                         color=BLACK).scale(0.8).next_to(
                                             variable_high, RIGHT, buff=0.2))
                    if high == -1:
                        self.play(vec_high_all.shift,
                                  (LEFT * 1.3 * (mid - high - 1) + LEFT * 0.6),
                                  FadeIn(extra_subscript),
                                  Transform(all_num[1], high_num_tmp))
                    else:
                        self.play(vec_high_all.shift,
                                  LEFT * 1.3 * (mid - high),
                                  Transform(all_num[1], high_num_tmp))
                    self.wait()
                else:
                    low = mid + 1
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
                        {
                            "height": 0.28,
                            "stretch": True
                        },
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
                        {
                            "height": 0.28,
                            "stretch": True
                        },
                        run_time=1.5,
                    )
                    self.wait()
                    low_num_tmp = (Text(str(low),
                                        font="思源宋体 Heavy",
                                        color=BLACK).scale(0.8).next_to(
                                            variable_low, RIGHT, buff=0.2))
                    self.play(vec_low_all.shift, RIGHT * 1.3 * (low - mid),
                              Transform(all_num[3], low_num_tmp))
                    self.wait()
            if high == -1:
                self.play(FadeOut(vec_high_all), FadeOut(vec_mid_all),
                          FadeOut(extra_subscript))
            else:
                self.play(FadeOut(vec_high_all), FadeOut(vec_mid_all))
            through_for = False
            for j in range(pos - 1, int(low) - 1, -1):
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
                    {
                        "height": 0.28,
                        "stretch": True
                    },
                    run_time=1.5,
                )
                self.wait()
                if pos == 1:
                    if j == pos - 1:
                        vec_j_all.next_to(rec_map[0], DOWN, buff=0.4)
                        self.play(FadeInFrom(vec_j_all, DOWN),
                                  FadeIn(all_num[5]))
                    else:
                        j_num_tmp = (Text(str(j),
                                          font="思源宋体 Heavy",
                                          color=BLACK).scale(0.8).next_to(
                                              variable_j, RIGHT, buff=0.2))
                        self.play(vec_j_all.shift, LEFT * 1.3,
                                  Transform(all_num[5], j_num_tmp))
                else:
                    j_num_tmp = (Text(str(j), font="思源宋体 Heavy",
                                      color=BLACK).scale(0.8).next_to(
                                          variable_j, RIGHT, buff=0.2))
                    if j == pos - 1:
                        vec_j_all.next_to(rec_map[j], DOWN, buff=0.4)
                        self.play(FadeInFrom(vec_j_all, DOWN),
                                  Transform(all_num[5], j_num_tmp))
                    else:
                        self.play(vec_j_all.shift, LEFT * 1.3,
                                  Transform(all_num[5], j_num_tmp))
                self.wait()
                rec_height_chaos[j + 1] = rec_height_chaos[j]
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
                    {
                        "height": 0.28,
                        "stretch": True
                    },
                    run_time=1.5,
                )
                self.wait()
                self.play(rec_map[j].move_to, rec_base_position[j + 1],
                          rec_map[j].align_to, rec_base_position[j + 1], DOWN,
                          num_map[j].shift, RIGHT * 1.3)
                rec_map[j + 1] = rec_map[j]
                num_map[j + 1] = num_map[j]
                self.wait()
            # for 循环一开始相等就不会执行，因此要额外用 if 补充其他情况
            if through_for == False:
                j_num_tmp = (Text(str(pos - 1), font="思源宋体 Heavy",
                                  color=BLACK).scale(0.8).next_to(variable_j,
                                                                  RIGHT,
                                                                  buff=0.2))
                vec_j_all.next_to(rec_map[pos - 1], DOWN, buff=0.4)
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
                {
                    "height": 0.28,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()
            j_num_tmp = (Text(str(j_pos - 1), font="思源宋体 Heavy",
                              color=BLACK).scale(0.8).next_to(variable_j,
                                                              RIGHT,
                                                              buff=0.2))
            if through_for == True:
                if j_pos != 0:
                    self.play(vec_j_all.shift, LEFT * 1.3,
                              Transform(all_num[5], j_num_tmp))
                else:
                    self.play(vec_j_all.shift, LEFT * 0.6,
                              FadeIn(extra_subscript),
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
                {
                    "height": 0.28,
                    "stretch": True
                },
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
                self.play(FadeOut(vec_j_all), FadeOut(vec_low_all),
                          FadeOut(extra_subscript))
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
            {
                "height": 0.28,
                "stretch": True
            },
            run_time=1.5,
        )
        self.wait()
        pos_num_tmp = (Text(str(8), font="思源宋体 Heavy",
                            color=BLACK).scale(0.8).next_to(variable_pos,
                                                            RIGHT,
                                                            buff=0.2))
        self.play(FadeOutAndShift(vec_pos_all, RIGHT),
                  Transform(all_num[4], pos_num_tmp))
        self.wait()
        # """


class binaryInsertSort_OOP(Scene_White):
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
            color=GREEN,
            stroke_opacity=0,
            height=4.5,
            width=3,
        ).to_corner(UR, buff=0)
        frame_code = Rectangle(
            color=BLUE,
            stroke_opacity=0,
            height=3.5,
            width=7.1 + 2.5,
        ).to_corner(DL, buff=0)
        frame_variable = Rectangle(
            color=RED,
            stroke_opacity=0,
            height=3.5,
            width=7.1 - 2.5,
        ).to_corner(DR, buff=0)
        self.add(frame_animation, frame_code, frame_variable)

        # --------------- 动画框架 ---------------
        # 标题
        title = (Text("折半插入排序", font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).to_corner(UP).shift(UP * 0.25))
        self.add(title)
        # 基准长方形
        rectangle_base = MyRectangle(fill_color=BLUE,
                                     color=BLUE,
                                     height=2.5,
                                     width=0.8,
                                     fill_opacity=1,
                                     opacity=1,
                                     stroke_opacity=1)
        # 存储待排序的长方块
        rec_base = VGroup()
        # 存储每个长方块的高度
        rec_height = []
        for i in range(8):
            highest = 2.5
            shortest = 0.5
            gap = (highest - shortest) / 7
            rec_height_element = shortest + gap * i
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
        rec_base.move_to(frame_animation).shift(UP * 0.2)
        # 各方块下标
        rec_subscript = VGroup()
        for i in range(8):
            subscript = (Text(str(i), font="思源宋体 Heavy",
                              color=BLACK).scale(0.4).next_to(rec_base[i],
                                                              DOWN,
                                                              buff=0.1))
            rec_subscript.add(subscript)
        # 额外的 -1 下标
        extra_subscript = (Text(str(-1), font="思源宋体 Heavy",
                                color=BLACK).scale(0.4).move_to(
                                    rec_subscript[0]).shift(LEFT * 0.6))
        # 各方块坐标
        rec_coordinate = VGroup()
        for i in range(8):
            coordinate = (Text(str(chaos[i]), font="江西拙楷",
                               color=BLACK).scale(0.7).move_to(rec_base[i]))
            # coordinate.add_updater(lambda a: a.move_to(rec_base[i]))
            rec_coordinate.add(coordinate)
        # 映射表
        rec_map = {
            0: rec_base[0],
            1: rec_base[1],
            2: rec_base[2],
            3: rec_base[3],
            4: rec_base[4],
            5: rec_base[5],
            6: rec_base[6],
            7: rec_base[7]
        }
        num_map = {
            0: rec_coordinate[0],
            1: rec_coordinate[1],
            2: rec_coordinate[2],
            3: rec_coordinate[3],
            4: rec_coordinate[4],
            5: rec_coordinate[5],
            6: rec_coordinate[6],
            7: rec_coordinate[7]
        }
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
                                 np.array([0, 3, 0]),
                                 color=BLACK,
                                 stroke_width=1.0).move_to(frame_code)

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

        codes_binaryInsertSort_left = (VGroup(*[
            codeline_binaryInsertSort(code)
            for code in binaryInsertSort_codes[:11]
        ]).arrange(DOWN, aligned_edge=LEFT,
                   buff=0.05).next_to(background.get_top(), DOWN,
                                      buff=0).shift(LEFT * 2.25 + DOWN * 0.15))
        codes_binaryInsertSort_right = (VGroup(*[
            codeline_binaryInsertSort(code)
            for code in binaryInsertSort_codes[11:]
        ]).arrange(DOWN, aligned_edge=LEFT, buff=0.05).next_to(
            background.get_top(), DOWN,
            buff=0).shift(RIGHT * 2.25 + DOWN * 0.15))
        codes_binaryInsertSort = VGroup(codes_binaryInsertSort_left,
                                        codes_binaryInsertSort_right)

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=2.5,
            stroke_color=BLUE,
            corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1,
                         fill_color=RED).rotate(90 * DEGREES, axis=IN)
        arrow.scale(0.1)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))

        # 一键添加代码背景 and 代码
        self.add(background, middle_line, codes_binaryInsertSort)
        # self.add(arrow, move_frame)
        move_frame.set_width(ignore_space_len(codes_binaryInsertSort[0][0], 0),
                             stretch=True).set_height(
                                 0.28, stretch=True).move_to(
                                     codes_binaryInsertSort[0][0]).align_to(
                                         codes_binaryInsertSort[0][0],
                                         RIGHT).shift(RIGHT * 0.05)
        arrow.next_to(move_frame, LEFT, buff=0.1)

        # 箭头
        vec_j = (Arrow(np.array([0, -1, 0]),
                       np.array([0, 1, 0]),
                       color=BLACK,
                       buff=0.3,
                       fill_color=BLACK).scale(0.35))
        vec_pos = vec_j.copy()
        vec_low_big = vec_j.copy()
        vec_high = (Arrow(np.array([0, -1, 0]),
                          np.array([0, 1, 0]),
                          color=BLACK,
                          buff=0.2,
                          fill_color=BLACK).scale(0.20))
        vec_low = vec_high.copy()
        vec_mid = vec_high.copy()
        vec_j.next_to(rec_base[0], DOWN, buff=0.35)
        vec_pos.next_to(rec_base[1], DOWN, buff=0.35)
        vec_high.next_to(rec_base[2], DOWN, buff=0.35)
        vec_low.next_to(rec_base[2], DOWN, buff=0.35)
        vec_mid.next_to(rec_base[2], DOWN, buff=0.35)
        vec_low_big.next_to(rec_base[3], DOWN, buff=0.35)
        vec_j_variables = (Text("j", font="思源宋体 Heavy",
                                color=BLACK).scale(0.6))
        vec_pos_variables = (Text("pos", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.6))
        vec_low_variables_big = (Text("low", font="思源宋体 Heavy",
                                      color=BLACK).scale(0.6))
        vec_high_variables = (Text("high", font="思源宋体 Heavy",
                                   color=BLACK).scale(0.4))
        vec_low_variables = (Text("low", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.4))
        vec_mid_variables = (Text("mid", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.4))
        vec_j_variables.add_updater(lambda a: a.next_to(vec_j, DOWN, buff=0.1))
        vec_pos_variables.add_updater(
            lambda a: a.next_to(vec_pos, DOWN, buff=0.1))
        vec_high_variables.add_updater(
            lambda a: a.next_to(vec_high, DOWN, buff=0.5))
        vec_low_variables.add_updater(
            lambda a: a.next_to(vec_low, DOWN, buff=0))
        vec_mid_variables.add_updater(
            lambda a: a.next_to(vec_mid, DOWN, buff=0.25))
        vec_low_variables_big.add_updater(
            lambda a: a.next_to(vec_low_big, DOWN, buff=0.05))
        vec_j_all = VGroup(vec_j, vec_j_variables)
        vec_pos_all = VGroup(vec_pos, vec_pos_variables)
        vec_high_all = VGroup(vec_high, vec_high_variables)
        vec_low_all = VGroup(vec_low, vec_low_variables)
        vec_mid_all = VGroup(vec_mid, vec_mid_variables)
        vec_low_big_all = VGroup(vec_low_big, vec_low_variables_big)
        # self.add(vec_j_all, vec_pos_all, vec_high_all, vec_low_all, vec_mid_all, vec_low_big_all)

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
            color="#003472", height=3, width=4,
            stroke_opacity=1).move_to(frame_variable)
        variable_Size = (Text("Size:  8",
                              font="思源宋体 Heavy",
                              color=BLACK,
                              t2c=t2c).scale(0.8).next_to(
                                  variable_rectangle.get_top(), DOWN,
                                  buff=0.2).align_to(variable_rectangle,
                                                     LEFT).shift(RIGHT * 0.25))
        variable_high = (Text("high:", font="思源宋体 Heavy", color=BLACK,
                              t2c=t2c).scale(0.8).next_to(variable_Size,
                                                          DOWN,
                                                          buff=0.3).align_to(
                                                              variable_Size,
                                                              LEFT))
        variable_low = (Text("low:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(0.8).next_to(variable_high,
                                                         DOWN,
                                                         buff=0.3).align_to(
                                                             variable_Size,
                                                             LEFT))
        variable_j = (Text("j:", font="思源宋体 Heavy", color=BLACK,
                           t2c=t2c).scale(0.8).next_to(variable_low,
                                                       DOWN,
                                                       buff=0.3).align_to(
                                                           variable_Size,
                                                           LEFT))
        variable_Rm = (Text("R[mid]:", font="思源宋体 Heavy", color=BLACK,
                            t2c=t2c).scale(0.8).next_to(
                                variable_rectangle.get_top(), DOWN,
                                buff=0.2).align_to(variable_rectangle,
                                                   RIGHT).shift(LEFT * 0.6))
        variable_mid = (Text("mid:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(0.8).next_to(
                                 variable_Rm, DOWN,
                                 buff=0.3).align_to(variable_Rm,
                                                    LEFT).shift(RIGHT * 0.2))
        variable_pos = (Text("pos:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(0.8).next_to(
                                 variable_mid, DOWN,
                                 buff=0.4).align_to(variable_Rm,
                                                    LEFT).shift(RIGHT * 0.2))
        Rm_num = (Text(str(5), font="思源宋体 Heavy",
                       color=BLACK).scale(0.8).next_to(variable_Rm,
                                                       RIGHT,
                                                       buff=0.2))
        high_num = (Text(str(0), font="思源宋体 Heavy",
                         color=BLACK).scale(0.8).next_to(variable_high,
                                                         RIGHT,
                                                         buff=0.2))
        mid_num = (Text(str(0), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.2))
        low_num = (Text(str(0), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_low,
                                                        RIGHT,
                                                        buff=0.2))
        pos_num = (Text(str(1), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_pos,
                                                        RIGHT,
                                                        buff=0.2))
        j_num = (Text(str(0), font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).next_to(variable_j,
                                                      RIGHT,
                                                      buff=0.2))
        all_num = VGroup(Rm_num, high_num, mid_num, low_num, pos_num, j_num)
        self.add(variable_rectangle, variable_Size, variable_high,
                 variable_low, variable_j, variable_Rm, variable_mid,
                 variable_pos)
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
        tmp_variables = (Text("Tmp", font="思源宋体 Heavy", color=BLACK,
                              t2c=t2c).scale(1).next_to(
                                  tmp_rectangle.get_bottom(), UP, buff=0.2))
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
        """
        下面我想引入面向对象方法(实际上我也不确定这样的方法是否属于), 因为一次用一个大的 for 循环太过于复杂,
        而且循环前几次每次出现的情况不太有规律可循, 甚至有指针交叉重叠的情况出现, 因此我想拆解成几个小的部分,
        大的 for 循环中间的 while 循环为第一个小部分, 下面的 for 循环为第二个小部分, 这两个小部分我称之为
        面向对象函数, 它们的特点是: 过程独立(单独的一个函数)、可选择性(参数可供选择)、随时调用(字面意思)、
        且便于阅读, 另一个部分即整体 for 循环中其他零零散散的部分, 这些部分与大的 for 循环依然为面向过程设计

        分析情况:
        面向对象零 (包装代码框移动)
        这次特地包装了代码框, 以前没想到将 self.play() 整个写入函数中也可以运行, 终于整出来了, 同时也可以运行
        其他(多个)方法

        面向对象一 (变量框元素值更新)
        设计一个函数, 仅仅调用时可更新变量框内某个元素的值, 调用方法包含在 self.play() 内部

        面向对象二 (low | high | mid 的变化)
        只用考虑到的变量为指针 low、high、mid, 不包括指针 pos
        传入参数为: low 和 high
        动画: (在指针 low 和 high 已经出现的基础上) 首先出现指针 mid, 接着指针 high 向左移动或者 low 向右移动
        特性: 为了保持函数独立性, 指针出现的地方对应的是固定的长条位置(不随长条的移动变换)

        面向对象三 (元素长条的移动)
        考虑到的对象为 pos 前的全部长条, 还有指针 j 和 low
        传入参数为
        动画: 首先出现指针 low(大版)、j, 接着长条依次向右移动, 最后长条 tmp 复原
        """

        # 初始信息
        R = [5, 1, 2, 7, 0, 6, 3, 4]
        rec_fix = rec_base.copy()  # 固定的长条位置
        NULL = Dot(color=WHITE).next_to(title, LEFT)  # 用于代替 self.play() 中的 空

        # 面向对象零 (包装代码框移动)
        def code_move(i, j, *method):
            # 调用方法举例: code_move(1, 0, FadeIn(vec_pos_all))
            lines = 11 * i + j
            self.play(
                *method,
                move_frame.set_width,
                ignore_space_len(codes_binaryInsertSort[i][j], lines),
                move_frame.move_to,
                codes_binaryInsertSort[i][j],
                move_frame.align_to,
                codes_binaryInsertSort[i][j],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {
                    "height": 0.28,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()

        # 面向对象一 (变量框元素值更新)
        def renew_variable(string, num):
            # 调用方法举例: self.play(renew_variable('rm', 1))
            if string == 'rm':
                Rm_num = (Text(str(num), font="思源宋体 Heavy",
                               color=BLACK).scale(0.8).next_to(variable_Rm,
                                                               RIGHT,
                                                               buff=0.2))
                return Transform(all_num[0], Rm_num)
            elif string == 'high':
                high_num = (Text(str(num), font="思源宋体 Heavy",
                                 color=BLACK).scale(0.8).next_to(variable_high,
                                                                 RIGHT,
                                                                 buff=0.2))
                return Transform(all_num[1], high_num)
            elif string == 'mid':
                mid_num = (Text(str(num), font="思源宋体 Heavy",
                                color=BLACK).scale(0.8).next_to(variable_mid,
                                                                RIGHT,
                                                                buff=0.2))
                return Transform(all_num[2], mid_num)
            elif string == 'low':
                low_num = (Text(str(num), font="思源宋体 Heavy",
                                color=BLACK).scale(0.8).next_to(variable_low,
                                                                RIGHT,
                                                                buff=0.2))
                return Transform(all_num[3], low_num)
            elif string == 'pos':
                pos_num = (Text(str(num), font="思源宋体 Heavy",
                                color=BLACK).scale(0.8).next_to(variable_pos,
                                                                RIGHT,
                                                                buff=0.2))
                return Transform(all_num[4], pos_num)
            elif string == 'j':
                j_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(0.8).next_to(variable_j,
                                                              RIGHT,
                                                              buff=0.2))
                return Transform(all_num[5], j_num)

        # 面向对象二 (low | high | mid 的变化)
        def while_OOP(low, high, tmp):
            cmd = 0
            while (low <= high):
                if (cmd):
                    code_move(0, 7)
                else:
                    # 指针 pos 消失
                    code_move(0, 7, FadeOut(vec_pos_all))
                mid = int((low + high) / 2)
                code_move(0, 9)
                if (cmd):
                    # 指针 mid 更新位置
                    self.play(FadeOut(vec_mid_all))
                    vec_mid_all.next_to(rec_fix[mid], DOWN, buff=0.35)
                    self.play(FadeIn(vec_mid_all),
                              renew_variable('rm', R[mid]),
                              renew_variable('mid', mid))
                    self.wait()
                else:
                    # 指针 mid 出现
                    vec_mid_all.next_to(rec_fix[mid], DOWN, buff=0.35)
                    self.play(FadeIn(vec_mid_all),
                              renew_variable('rm', R[mid]),
                              renew_variable('mid', mid))
                    self.wait()
                    cmd = 1
                code_move(0, 10)
                if (tmp < R[mid]):
                    # 指针 high 左移
                    code_move(1, 0)
                    if mid == 0:
                        self.play(vec_high_all.shift, LEFT * 0.6,
                                  renew_variable('high', mid - 1),
                                  FadeIn(extra_subscript))
                    else:
                        self.play(vec_high_all.shift,
                                  LEFT * 1.3 * (high - mid + 1),
                                  renew_variable('high', mid - 1))
                    high = mid - 1
                    self.wait()
                else:
                    # 指针 low 右移
                    code_move(1, 1)
                    code_move(1, 2)
                    self.play(vec_low_all.shift, RIGHT * 1.3 * (mid + 1 - low),
                              renew_variable('low', mid + 1))
                    low = mid + 1
                    self.wait()
            code_move(0, 7)
            return low, high

        # 面向对象三 (元素长条的移动)
        def for_OOP(pos, low, high, tmp):
            cmd = 0
            for j in range(pos - 1, low - 1, -1):
                if (cmd):
                    code_move(1, 4)
                else:
                    # 指针 low、high、mid 消失
                    code_move(
                        1, 4, FadeOut(vec_low_all), FadeOut(vec_high_all),
                        FadeOut(vec_mid_all),
                        FadeOut(extra_subscript)
                        if high == -1 else FadeIn(NULL))
                if (cmd):
                    # 指针 j 左移
                    vec_low_big_position = vec_low_big_all.copy().next_to(
                        rec_fix[low], DOWN, buff=0.35)
                    vec_j_position = vec_j_all.copy().next_to(rec_fix[j],
                                                              DOWN,
                                                              buff=0.35)
                    if low == j:
                        vec_low_big_position.shift(LEFT * 0.2)
                        vec_j_position.shift(RIGHT * 0.2)
                    self.play(vec_j_all.move_to, vec_j_position,
                              vec_low_big_all.move_to, vec_low_big_position,
                              renew_variable('j', j))
                    self.wait()
                else:
                    # 指针 low_big、j 出现
                    vec_low_big_all.next_to(rec_fix[low], DOWN, buff=0.35)
                    vec_j_all.next_to(rec_fix[j], DOWN, buff=0.35)
                    if low == j:
                        vec_low_big_all.shift(LEFT * 0.2)
                        vec_j_all.shift(RIGHT * 0.2)
                    self.play(FadeIn(vec_low_big_all), FadeIn(vec_j_all),
                              renew_variable('low', low),
                              renew_variable('j', j))
                    self.wait()
                    cmd = 1
                code_move(1, 5)
                R[j + 1] = R[j]
                # 长条右移
                self.play(rec_map[j].move_to, rec_fix[j + 1],
                          rec_map[j].align_to, rec_fix[j + 1], DOWN,
                          num_map[j].shift, RIGHT * 1.3)
                self.wait()
                # 哈希表更新
                rec_map[j + 1], num_map[j + 1] = rec_map[j], num_map[j]
            # 存在根本没执行 for 循环的情况
            if cmd == 0:
                # 指针 low、high、mid 消失 且 指针 low_big、j 出现
                j = pos - 1
                vec_low_big_all.next_to(rec_fix[low], DOWN, buff=0.35)
                vec_j_all.next_to(rec_fix[j], DOWN, buff=0.35)
                code_move(
                    1, 4, FadeOut(vec_low_all), FadeOut(vec_high_all),
                    FadeOut(vec_mid_all),
                    FadeOut(extra_subscript) if high == -1 else FadeIn(NULL),
                    FadeIn(vec_low_big_all), FadeIn(vec_j_all),
                    renew_variable('j', j))
                cmd = 2
            else:
                code_move(1, 4)
            # 指针 j 左移
            j = low - 1
            vec_low_big_position = vec_low_big_all.copy().next_to(rec_fix[low],
                                                                  DOWN,
                                                                  buff=0.35)
            if j == -1:
                vec_j_position = vec_j_all.copy().next_to(rec_fix[0],
                                                          DOWN,
                                                          buff=0.35)
                vec_j_position.align_to(
                    vec_j_position.copy().move_to(extra_subscript), LEFT)
                self.play(vec_j_all.move_to, vec_j_position,
                          vec_low_big_all.move_to, vec_low_big_position,
                          FadeIn(extra_subscript), renew_variable('j', j))
                # 指针 j 消失
                self.wait()
                code_move(1, 6, FadeOut(vec_j_all), FadeOut(extra_subscript))
            elif cmd == 2:
                # 指针 j 消失
                self.wait()
                code_move(1, 6, FadeOut(vec_j_all))
            else:
                vec_j_position = vec_j_all.copy().next_to(rec_fix[j],
                                                          DOWN,
                                                          buff=0.35)
                self.play(vec_j_all.move_to, vec_j_position,
                          vec_low_big_all.move_to, vec_low_big_position,
                          renew_variable('j', j))
                # 指针 j 消失
                self.wait()
                code_move(1, 6, FadeOut(vec_j_all))
            R[low] = tmp
            # 哈希表更新
            rec_map[low], num_map[low] = rec_base[pos], rec_coordinate[pos]
            # Tmp 长条(与数字)归位
            self.play(FadeOut(rec_base[pos]),
                      FadeOut(rec_coordinate[pos]))  # Tmp 的长条和数字消失
            rec_base[pos].move_to(rec_fix[low]).align_to(rec_fix[low],
                                                         DOWN)  # Tmp 的长条移动到空位
            rec_coordinate[pos].move_to(rec_map[low])  # Tmp 的数字随着移动
            self.play(FadeIn(rec_base[pos]),
                      FadeIn(rec_coordinate[pos]))  # Tmp 的长条和数字出现

        # 折半插入排序 (面向过程 + 面向对象)
        code_move(0, 0)
        code_move(0, 1)
        # -------------- 面向过程 第一次 for 循环 --------------
        pos = 1
        code_move(0, 2)
        # 指针 pos 出现
        vec_pos_all.next_to(rec_fix[pos], DOWN, buff=0.35)
        self.play(FadeIn(vec_pos_all), FadeIn(all_num[4]))
        self.wait()
        code_move(0, 4)
        # Tmp 长条(与数字)瞬移到 Tmp 框
        tmp = R[pos]
        rec_tmp = VGroup(rec_base[pos], rec_coordinate[pos])
        self.play(FadeOut(rec_tmp))
        rec_tmp.move_to(frame_tmp)
        self.play(FadeIn(rec_tmp))
        self.wait()
        code_move(0, 5)
        # 指针 low 出现
        low = 0
        vec_low_all.next_to(rec_fix[low], DOWN, buff=0.35)
        self.play(FadeIn(vec_low_all), FadeIn(all_num[3]))
        self.wait()
        code_move(0, 6)
        # 指针 high 出现
        high = pos - 1
        vec_high_all.next_to(rec_fix[high], DOWN, buff=0.35)
        self.play(FadeIn(vec_high_all), FadeIn(all_num[1]))
        self.wait()
        # 面向对象二 (low | high | mid 的变化)
        # low, high = while_OOP(low, high, tmp)
        code_move(0, 7, FadeOut(vec_pos_all))
        mid = int((low + high) / 2)
        code_move(0, 9)
        vec_mid_all.next_to(rec_fix[mid], DOWN, buff=0.35)
        self.play(FadeIn(vec_mid_all), FadeIn(all_num[0]), FadeIn(all_num[2]))
        self.wait()
        code_move(0, 10)
        code_move(1, 0)
        high = mid - 1
        self.play(vec_high_all.shift, LEFT * 0.6, renew_variable('high', high),
                  FadeIn(extra_subscript))
        self.wait()
        code_move(0, 7)
        # 面向对象三 (元素长条的移动)
        # for_OOP(pos, low, high, tmp)
        j = pos - 1
        code_move(1, 4, FadeOut(vec_low_all), FadeOut(vec_high_all),
                  FadeOut(vec_mid_all), FadeOut(extra_subscript))
        vec_low_big_all.next_to(rec_fix[low], DOWN,
                                buff=0.35).shift(LEFT * 0.2)
        vec_j_all.next_to(rec_fix[j], DOWN, buff=0.35).shift(RIGHT * 0.2)
        self.play(FadeIn(vec_low_big_all), FadeIn(vec_j_all),
                  renew_variable('low', low), FadeIn(all_num[5]))
        self.wait()
        code_move(1, 5)
        R[j + 1] = R[j]
        # 长条右移
        self.play(rec_map[j].move_to, rec_fix[j + 1], rec_map[j].align_to,
                  rec_fix[j + 1], DOWN, num_map[j].shift, RIGHT * 1.3)
        self.wait()
        # 哈希表更新
        rec_map[j + 1], num_map[j + 1] = rec_map[j], num_map[j]
        # 指针 j 左移
        j = low - 1
        code_move(1, 4)
        self.play(vec_j_all.shift, LEFT * 0.8, vec_low_big_all.shift,
                  RIGHT * 0.2, FadeIn(extra_subscript))
        # 指针 j 消失
        self.wait()
        code_move(1, 6, FadeOut(vec_j_all), FadeOut(extra_subscript))
        R[low] = tmp
        # 哈希表更新
        rec_map[low], num_map[low] = rec_base[pos], rec_coordinate[pos]
        # Tmp 长条(与数字)归位
        self.play(FadeOut(rec_base[pos]),
                  FadeOut(rec_coordinate[pos]))  # Tmp 的长条和数字消失
        rec_base[pos].move_to(rec_fix[low]).align_to(rec_fix[low],
                                                     DOWN)  # Tmp 的长条移动到空位
        rec_coordinate[pos].move_to(rec_map[low])  # Tmp 的数字随着移动
        self.play(FadeIn(rec_base[pos]),
                  FadeIn(rec_coordinate[pos]))  # Tmp 的长条和数字出现
        self.wait()
        # -------------- 面向对象 第 n 次 for 循环 --------------
        for pos in range(2, 8):
            code_move(0, 2, FadeOut(vec_low_big_all))
            # 指针 pos 出现
            vec_pos_all.next_to(rec_fix[pos], DOWN, buff=0.35)
            self.play(FadeIn(vec_pos_all), renew_variable('pos', pos))
            self.wait()
            code_move(0, 4)
            # Tmp 长条(与数字)瞬移到 Tmp 框
            tmp = R[pos]
            rec_tmp = VGroup(rec_base[pos], rec_coordinate[pos])
            self.play(FadeOut(rec_tmp))
            rec_tmp.move_to(frame_tmp)
            self.play(FadeIn(rec_tmp))
            self.wait()
            code_move(0, 5)
            # 指针 low 出现
            low = 0
            vec_low_all.next_to(rec_fix[low], DOWN, buff=0.35)
            self.play(FadeIn(vec_low_all), renew_variable('low', low))
            self.wait()
            code_move(0, 6)
            # 指针 high 出现
            high = pos - 1
            vec_high_all.next_to(rec_fix[high], DOWN, buff=0.35)
            self.play(FadeIn(vec_high_all), renew_variable('high', high))
            self.wait()
            # 面向对象二 (low | high | mid 的变化)
            low, high = while_OOP(low, high, tmp)
            # 面向对象三 (元素长条的移动)
            for_OOP(pos, low, high, tmp)
            self.wait()
        code_move(0, 2, FadeOut(vec_low_big_all))
        self.wait()


class shellSort(Scene_White):
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
            color=GREEN,
            stroke_opacity=0,
            height=4.5,
            width=3,
        ).to_corner(UR, buff=0)
        frame_code = Rectangle(
            color=BLUE,
            stroke_opacity=0,
            height=3.5,
            width=7.1 + 1.5,
        ).to_corner(DL, buff=0)
        frame_variable = Rectangle(
            color=RED,
            stroke_opacity=0,
            height=3.5,
            width=7.1 - 1.5,
        ).to_corner(DR, buff=0)
        self.add(frame_animation, frame_code, frame_variable)

        # --------------- 动画框架 ---------------
        # 标题
        title = (Text("希尔排序", font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).to_corner(UP).shift(UP * 0.25))
        self.add(title)
        # 基准长方形
        rectangle_base = MyRectangle(fill_color=BLUE,
                                     color=BLUE,
                                     height=2.5,
                                     width=0.8,
                                     fill_opacity=1,
                                     opacity=1,
                                     stroke_opacity=1)
        # 存储待排序的长方块
        rec_base = VGroup()
        # 存储每个长方块的高度
        rec_height = []
        for i in range(8):
            highest = 2.5
            shortest = 0.5
            gap = (highest - shortest) / 7
            rec_height_element = shortest + gap * i
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
        rec_base.move_to(frame_animation).shift(UP * 0.2)
        # 各方块下标
        rec_subscript = VGroup()
        for i in range(8):
            subscript = (Text(str(i), font="思源宋体 Heavy",
                              color=BLACK).scale(0.4).next_to(rec_base[i],
                                                              DOWN,
                                                              buff=0.1))
            rec_subscript.add(subscript)
        # 额外的 -1 下标
        extra_subscript = (Text(str(-1), font="思源宋体 Heavy",
                                color=BLACK).scale(0.4).move_to(
                                    rec_subscript[0]).shift(LEFT * 0.6))
        # 各方块坐标
        rec_coordinate = VGroup()
        for i in range(8):
            coordinate = (Text(str(chaos[i]), font="江西拙楷",
                               color=BLACK).scale(0.7).move_to(rec_base[i]))
            rec_coordinate.add(coordinate)
        # 映射表
        rec_map = {
            0: rec_base[0],
            1: rec_base[1],
            2: rec_base[2],
            3: rec_base[3],
            4: rec_base[4],
            5: rec_base[5],
            6: rec_base[6],
            7: rec_base[7]
        }
        num_map = {
            0: rec_coordinate[0],
            1: rec_coordinate[1],
            2: rec_coordinate[2],
            3: rec_coordinate[3],
            4: rec_coordinate[4],
            5: rec_coordinate[5],
            6: rec_coordinate[6],
            7: rec_coordinate[7]
        }
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
        background.set_height(3, stretch=True).set_width(8.2, stretch=True)
        background.move_to(frame_code)

        # 代码 + 移动框
        class codeline_shellSort(Text):
            CONFIG = {
                "size": 0.42,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        def ignore_space_len(code, num):
            origin_len = len(code)
            begin = origin_len - 1
            record = 0
            temp_codes = shellSort_codes
            for index in range(begin, 0, -1):
                if temp_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.125
                elif temp_codes[num][index] == " " and record == 0:
                    record = 1
                elif temp_codes[num][index] != " ":
                    record = 0
            return origin_len * 0.125

        codes_shellSort = (VGroup(
            *[codeline_shellSort(code)
              for code in shellSort_codes[:]]).arrange(
                  DOWN, aligned_edge=LEFT,
                  buff=0.05).next_to(background.get_top(), DOWN,
                                     buff=0).shift(LEFT * 0 + DOWN * 0.1))

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=2.5,
            stroke_color=BLUE,
            corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1,
                         fill_color=RED).rotate(90 * DEGREES, axis=IN)
        arrow.scale(0.1)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))

        # 一键添加代码背景 and 代码
        self.add(background, codes_shellSort)
        # self.add(arrow, move_frame)
        move_frame.set_width(
            ignore_space_len(codes_shellSort[0], 0),
            stretch=True).set_height(0.24, stretch=True).move_to(
                codes_shellSort[0]).align_to(codes_shellSort[0],
                                             RIGHT).shift(RIGHT * 0.05)
        arrow.next_to(move_frame, LEFT, buff=0.1)

        # 箭头
        vec_j = (Arrow(np.array([0, -1, 0]),
                       np.array([0, 1, 0]),
                       color=BLACK,
                       buff=0.3,
                       fill_color=BLACK).scale(0.35))
        vec_pos = vec_j.copy()
        vec_gap = vec_j.copy()
        vec_j.next_to(rec_base[0], DOWN, buff=0.35)
        vec_pos.next_to(rec_base[1], DOWN, buff=0.35)
        vec_gap.next_to(rec_base[2], DOWN, buff=0.35)
        vec_j_variables = (Text("j", font="思源宋体 Heavy",
                                color=BLACK).scale(0.6))
        vec_pos_variables = (Text("pos", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.6))
        vec_gap_variables = (Text("gap", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.6))
        vec_j_variables.add_updater(lambda a: a.next_to(vec_j, DOWN, buff=0.1))
        vec_pos_variables.add_updater(
            lambda a: a.next_to(vec_pos, DOWN, buff=0.1))
        vec_gap_variables.add_updater(
            lambda a: a.next_to(vec_gap, DOWN, buff=0.1))
        vec_j_all = VGroup(vec_j, vec_j_variables)
        vec_pos_all = VGroup(vec_pos, vec_pos_variables)
        vec_gap_all = VGroup(vec_gap, vec_gap_variables)
        # self.add(vec_j_all, vec_pos_all, vec_gap_all)

        # 变量框
        t2c = {
            "j": "#01cd74",
            "Size": BLUE,
            "R[j]": GOLD,
            "pos": PURPLE,
            "gap": RED,
        }
        variable_rectangle = Rectangle(
            color="#003472", height=3, width=5,
            stroke_opacity=1).move_to(frame_variable)
        variable_Size = (Text("Size:  8",
                              font="思源宋体 Heavy",
                              color=BLACK,
                              t2c=t2c).scale(1).next_to(
                                  variable_rectangle.get_top(), DOWN,
                                  buff=0.3).align_to(variable_rectangle,
                                                     LEFT).shift(RIGHT * 0.3))
        variable_gap = (Text("gap:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(1).next_to(variable_Size,
                                                       DOWN,
                                                       buff=0.5).align_to(
                                                           variable_Size,
                                                           LEFT))
        variable_pos = (Text("pos:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(1).next_to(variable_gap,
                                                       DOWN,
                                                       buff=0.5).align_to(
                                                           variable_Size,
                                                           LEFT))
        variable_Rj = (Text("R[j]:", font="思源宋体 Heavy", color=BLACK,
                            t2c=t2c).scale(1).next_to(
                                variable_rectangle.get_top(), DOWN,
                                buff=0.3).align_to(variable_rectangle,
                                                   RIGHT).shift(LEFT * 1))
        variable_j = (Text("j:", font="思源宋体 Heavy", color=BLACK,
                           t2c=t2c).scale(1).next_to(variable_Rj,
                                                     DOWN,
                                                     buff=0.3).align_to(
                                                         variable_Rj, LEFT))
        Rj_num = (Text(str(5), font="思源宋体 Heavy",
                       color=BLACK).scale(1).next_to(variable_Rj,
                                                     RIGHT,
                                                     buff=0.3))
        pos_num = (Text(str(4), font="思源宋体 Heavy",
                        color=BLACK).scale(1).next_to(variable_pos,
                                                      RIGHT,
                                                      buff=0.3))
        j_num = (Text(str(0), font="思源宋体 Heavy",
                      color=BLACK).scale(1).next_to(variable_j,
                                                    RIGHT,
                                                    buff=0.3))
        gap_num = (Text(str(4), font="思源宋体 Heavy",
                        color=BLACK).scale(1).next_to(variable_gap,
                                                      RIGHT,
                                                      buff=0.3))
        all_num = VGroup(Rj_num, pos_num, j_num, gap_num)
        self.add(variable_rectangle, variable_Size, variable_j, variable_Rj,
                 variable_pos, variable_gap)
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
        tmp_variables = (Text("Tmp", font="思源宋体 Heavy", color=BLACK,
                              t2c=t2c).scale(1).next_to(
                                  tmp_rectangle.get_bottom(), UP, buff=0.2))
        self.add(tmp_rectangle, tmp_variables)
        """
        int gap, pos, j;
        Type tmp;
        for (gap = size / 2; gap > 0; gap /= 2)
        {
            for (pos = gap; pos < size; pos++)
            {
                tmp = R[pos];
                for (j = pos - gap; j >= 0 && R[j] > tmp; j -= gap)
                    R[j + gap] = R[j];
                R[j + gap] = tmp;
            }
        }
        """

        # 借用 OOP 的方法
        # 面向对象零 (包装代码框移动)
        def code_move(i, *method):
            # 调用方法举例: code_move(1, 0, FadeIn(vec_pos_all))
            self.play(
                *method,
                move_frame.set_width,
                ignore_space_len(codes_shellSort[i], i),
                move_frame.move_to,
                codes_shellSort[i],
                move_frame.align_to,
                codes_shellSort[i],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {
                    "height": 0.24,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()

        # 面向对象一 (变量框元素值更新)

        def renew_variable(string, num):
            # 调用方法举例: self.play(renew_variable('rm', 1))
            if string == 'Rj':
                Rj_num = (Text(str(num), font="思源宋体 Heavy",
                               color=BLACK).scale(1).next_to(variable_Rj,
                                                             RIGHT,
                                                             buff=0.3))
                return Transform(all_num[0], Rj_num)
            elif string == 'pos':
                pos_num = (Text(str(num), font="思源宋体 Heavy",
                                color=BLACK).scale(1).next_to(variable_pos,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[1], pos_num)
            elif string == 'j':
                j_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(1).next_to(variable_j,
                                                            RIGHT,
                                                            buff=0.3))
                return Transform(all_num[2], j_num)
            elif string == 'gap':
                gap_num = (Text(str(num), font="思源宋体 Heavy",
                                color=BLACK).scale(1).next_to(variable_gap,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[3], gap_num)

        # 希尔排序
        R = [5, 1, 2, 7, 0, 6, 3, 4]
        rec_fix = rec_base.copy()  # 固定的长条位置
        NULL = Dot(color=WHITE).next_to(title, LEFT)  # 用于代替 self.play() 中的 空
        size = len(R)
        gap = size // 2
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()
        code_move(1)
        while gap > 0:
            code_move(2)
            self.play(FadeIn(gap_num)) if gap == size // 2 else self.play(
                renew_variable('gap', gap))
            self.wait()
            for pos in range(gap, size):
                code_move(4)
                self.play(FadeIn(pos_num)) if (gap == size // 2
                                               and pos == gap) else self.play(
                                                   renew_variable('pos', pos))
                vec_pos_all.next_to(rec_base[pos], DOWN,
                                    buff=0.35) if pos == gap else NULL
                self.play(FadeIn(vec_pos_all)) if pos == gap else self.play(
                    vec_pos_all.shift, RIGHT * 1.3)
                self.wait()
                tmp = R[pos]
                code_move(6)
                # Tmp 长条(与数字)瞬移到 Tmp 框
                rec_tmp = VGroup(rec_map[pos], num_map[pos])
                self.play(FadeOut(rec_tmp))
                rec_tmp.move_to(frame_tmp)
                self.play(FadeIn(rec_tmp))
                self.wait()
                j = pos - gap
                code_move(7)
                self.play(FadeIn(j_num), FadeIn(Rj_num)) if (
                    gap == size // 2 and pos == gap
                    and j == pos - gap) else self.play(
                        renew_variable('j', j), renew_variable('Rj', R[j]))
                vec_j_all.next_to(rec_fix[j], DOWN, buff=0.35)
                self.play(FadeIn(vec_j_all))
                self.wait()
                while j >= 0 and R[j] > tmp:
                    NULL if j == pos - gap else code_move(7)
                    NULL if j == pos - \
                        gap else self.play(renew_variable('j', j), renew_variable('Rj', R[j]))
                    NULL if j == pos - gap else self.wait()
                    NULL if j == pos - \
                        gap else self.play(vec_j_all.shift, LEFT*1.3*gap)
                    NULL if j == pos - gap else self.wait()
                    R[j + gap] = R[j]
                    code_move(8)
                    self.wait()
                    # 长条右移
                    self.play(rec_map[j].move_to, rec_fix[j + gap],
                              rec_map[j].align_to, rec_fix[j + gap], DOWN,
                              num_map[j].shift, RIGHT * 1.3 * gap)
                    self.wait()
                    # 哈希表更新
                    rec_map[j + gap], num_map[j + gap] = rec_map[j], num_map[j]
                    j -= gap
                NULL if j == pos - gap else code_move(7)
                NULL if j == pos - \
                    gap else self.play(renew_variable('j', j), renew_variable('Rj', R[j]))
                NULL if j == pos - gap else self.wait()
                NULL if j == pos - \
                    gap else self.play(vec_j_all.shift, LEFT*1.3*gap)
                NULL if j == pos - gap else self.wait()
                R[j + gap] = tmp
                code_move(9)
                # 哈希表更新
                rec_map[j + gap], num_map[j + gap] = rec_tmp[0], rec_tmp[1]
                # Tmp 长条(与数字)归位
                self.play(FadeOut(rec_tmp[0]),
                          FadeOut(rec_tmp[1]))  # Tmp 的长条和数字消失
                rec_tmp[0].move_to(rec_fix[j + gap]).align_to(
                    rec_fix[j + gap], DOWN)  # Tmp 的长条移动到空位
                rec_tmp[1].move_to(rec_map[j + gap])  # Tmp 的数字随着移动
                self.play(FadeIn(rec_tmp[0]),
                          FadeIn(rec_tmp[1]))  # Tmp 的长条和数字出现
                self.wait()
                self.play(FadeOut(vec_j_all))
                self.wait()
            code_move(4)
            self.play(FadeOut(vec_pos_all))
            self.wait()
            gap //= 2
        code_move(2)


class bubbleSort(Scene_White):
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
            width=14.2,
        ).to_corner(UL, buff=0)
        frame_code = Rectangle(
            color=BLUE,
            stroke_opacity=0,
            height=3.5,
            width=7.1 + 1,
        ).to_corner(DL, buff=0)
        frame_variable = Rectangle(
            color=RED,
            stroke_opacity=0,
            height=3.5,
            width=7.1 - 1,
        ).to_corner(DR, buff=0)
        self.add(frame_animation, frame_code, frame_variable)

        # --------------- 动画框架 ---------------
        # 标题
        title = (Text("冒泡排序", font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).to_corner(UP).shift(UP * 0.25))
        self.add(title)
        # 基准长方形
        rectangle_base = MyRectangle(fill_color=BLUE,
                                     color=BLUE,
                                     height=2.5,
                                     width=0.8,
                                     fill_opacity=1,
                                     opacity=1,
                                     stroke_opacity=1)
        # 存储待排序的长方块
        rec_base = VGroup()
        # 存储每个长方块的高度
        rec_height = []
        for i in range(8):
            highest = 2.5
            shortest = 0.5
            gap = (highest - shortest) / 7
            rec_height_element = shortest + gap * i
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
        rec_base.move_to(frame_animation).shift(UP * 0.2)
        # 各方块下标
        rec_subscript = VGroup()
        for i in range(8):
            subscript = (Text(str(i), font="思源宋体 Heavy",
                              color=BLACK).scale(0.4).next_to(rec_base[i],
                                                              DOWN,
                                                              buff=0.1))
            rec_subscript.add(subscript)
        # 额外的 -1 下标
        extra_subscript = (Text(str(-1), font="思源宋体 Heavy",
                                color=BLACK).scale(0.4).move_to(
                                    rec_subscript[0]).shift(LEFT * 0.6))
        # 各方块坐标
        rec_coordinate = VGroup()
        for i in range(8):
            coordinate = (Text(str(chaos[i]), font="江西拙楷",
                               color=BLACK).scale(0.7).move_to(rec_base[i]))
            rec_coordinate.add(coordinate)
        # 映射表
        rec_map = {
            0: rec_base[0],
            1: rec_base[1],
            2: rec_base[2],
            3: rec_base[3],
            4: rec_base[4],
            5: rec_base[5],
            6: rec_base[6],
            7: rec_base[7]
        }
        num_map = {
            0: rec_coordinate[0],
            1: rec_coordinate[1],
            2: rec_coordinate[2],
            3: rec_coordinate[3],
            4: rec_coordinate[4],
            5: rec_coordinate[5],
            6: rec_coordinate[6],
            7: rec_coordinate[7]
        }
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
        background.set_height(3, stretch=True).set_width(7, stretch=True)
        background.move_to(frame_code)

        # 代码 + 移动框
        class codeline_bubbleSort(Text):
            CONFIG = {
                "size": 0.42,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        def ignore_space_len(code, num):
            origin_len = len(code)
            begin = origin_len - 1
            record = 0
            temp_codes = bubbleSort_codes
            for index in range(begin, 0, -1):
                if temp_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.125
                elif temp_codes[num][index] == " " and record == 0:
                    record = 1
                elif temp_codes[num][index] != " ":
                    record = 0
            return origin_len * 0.125

        codes_bubbleSort = (VGroup(
            *[codeline_bubbleSort(code)
              for code in bubbleSort_codes[:]]).arrange(
                  DOWN, aligned_edge=LEFT,
                  buff=0.05).next_to(background.get_top(), DOWN,
                                     buff=0).shift(LEFT * 0 + DOWN * 0.1))

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=2.5,
            stroke_color=BLUE,
            corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1,
                         fill_color=RED).rotate(90 * DEGREES, axis=IN)
        arrow.scale(0.1)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))

        # 一键添加代码背景 and 代码
        self.add(background, codes_bubbleSort)
        # self.add(arrow, move_frame)
        move_frame.set_width(
            ignore_space_len(codes_bubbleSort[0], 0),
            stretch=True).set_height(0.24, stretch=True).move_to(
                codes_bubbleSort[0]).align_to(codes_bubbleSort[0],
                                              RIGHT).shift(RIGHT * 0.05)
        arrow.next_to(move_frame, LEFT, buff=0.1)

        # 箭头
        vec_j = (Arrow(np.array([0, -1, 0]),
                       np.array([0, 1, 0]),
                       color=BLACK,
                       buff=0.3,
                       fill_color=BLACK).scale(0.35))
        vec_i = vec_j.copy()
        vec_j.next_to(rec_base[0], DOWN, buff=0.35)
        vec_i.next_to(rec_base[1], DOWN, buff=0.35)
        vec_j_variables = (Text("j", font="思源宋体 Heavy",
                                color=BLACK).scale(0.6))
        vec_i_variables = (Text("i", font="思源宋体 Heavy",
                                color=BLACK).scale(0.6))
        vec_j_variables.add_updater(lambda a: a.next_to(vec_j, DOWN, buff=0.1))
        vec_i_variables.add_updater(lambda a: a.next_to(vec_i, DOWN, buff=0.1))
        vec_j_all = VGroup(vec_j, vec_j_variables)
        vec_i_all = VGroup(vec_i, vec_i_variables)
        # self.add(vec_j_all, vec_i_all)

        # 变量框
        t2c = {
            "i": RED,
            "j": "#01cd74",
            "Size": BLUE,
            "flag": GOLD,
            "R[j]": PURPLE,
            "R[j+1]": "#da1884",
        }
        variable_rectangle = Rectangle(
            color="#003472", height=3, width=5.5,
            stroke_opacity=1).move_to(frame_variable)
        variable_Size = (Text("Size:  8",
                              font="思源宋体 Heavy",
                              color=BLACK,
                              t2c=t2c).scale(1).next_to(
                                  variable_rectangle.get_top(), DOWN,
                                  buff=0.3).align_to(variable_rectangle,
                                                     LEFT).shift(RIGHT * 0.4))
        variable_i = (Text("i:", font="思源宋体 Heavy", color=BLACK,
                           t2c=t2c).scale(1).next_to(variable_Size,
                                                     DOWN,
                                                     buff=0.5).align_to(
                                                         variable_Size, LEFT))
        variable_j = (Text("j:", font="思源宋体 Heavy", color=BLACK,
                           t2c=t2c).scale(1).next_to(variable_i,
                                                     DOWN,
                                                     buff=0.5).align_to(
                                                         variable_i, LEFT))
        variable_flag = (Text("flag:", font="思源宋体 Heavy", color=BLACK,
                              t2c=t2c).scale(1).next_to(
                                  variable_rectangle.get_top(), DOWN,
                                  buff=0.3).align_to(variable_rectangle,
                                                     RIGHT).shift(LEFT * 1.8))
        variable_Rj = (Text("R[j]:", font="思源宋体 Heavy", color=BLACK,
                            t2c=t2c).scale(1).next_to(
                                variable_flag, DOWN,
                                buff=0.3).align_to(variable_flag,
                                                   LEFT).shift(LEFT * 0))
        variable_Rj2 = (Text("R[j+1]:",
                             font="思源宋体 Heavy",
                             color=BLACK,
                             t2c=t2c).scale(1).next_to(variable_Rj,
                                                       DOWN,
                                                       buff=0.5).align_to(
                                                           variable_Rj, LEFT))
        flag_num = (Text("true", font="思源宋体 Heavy",
                         color=BLACK).scale(1).next_to(variable_flag,
                                                       RIGHT,
                                                       buff=0.3))
        Rj_num = (Text(str(5), font="思源宋体 Heavy",
                       color=BLACK).scale(1).next_to(variable_Rj,
                                                     RIGHT,
                                                     buff=0.3))
        j_num = (Text(str(0), font="思源宋体 Heavy",
                      color=BLACK).scale(1).next_to(variable_j,
                                                    RIGHT,
                                                    buff=0.3))
        i_num = (Text(str(1), font="思源宋体 Heavy",
                      color=BLACK).scale(1).next_to(variable_i,
                                                    RIGHT,
                                                    buff=0.3))
        Rj2_num = (Text(str(1), font="思源宋体 Heavy",
                        color=BLACK).scale(1).next_to(variable_Rj2,
                                                      RIGHT,
                                                      buff=0.3))
        all_num = VGroup(flag_num, Rj_num, j_num, i_num, Rj2_num)
        self.add(variable_rectangle, variable_Size, variable_j, variable_flag,
                 variable_Rj, variable_i, variable_Rj2)
        # self.add(all_num)
        """
        int i, j;
        bool flag = true;
        for (int i = 1; i < size && size && flag; ++i)
        {
            flag = false;
            for (j = 0; j < size - i; ++j)
            {
                if (R[j + 1] < R[j])
                {
                    swap(R[j], R[j + 1]);
                    flag = true;
                }
            }
        }
        """

        # 借用 OOP 的方法
        # 面向对象零 (包装代码框移动)
        def code_move(i, *method):
            # 调用方法举例: code_move(1, 0, FadeIn(vec_pos_all))
            self.play(
                *method,
                move_frame.set_width,
                ignore_space_len(codes_bubbleSort[i], i),
                move_frame.move_to,
                codes_bubbleSort[i],
                move_frame.align_to,
                codes_bubbleSort[i],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {
                    "height": 0.24,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()

        # 面向对象一 (变量框元素值更新)

        def renew_variable(string, num):
            # 调用方法举例: self.play(renew_variable('rm', 1))
            if string == 'flag':
                flag_num = (Text(num, font="思源宋体 Heavy",
                                 color=BLACK).scale(1).next_to(variable_flag,
                                                               RIGHT,
                                                               buff=0.3))
                return Transform(all_num[0], flag_num)
            elif string == 'Rj':
                Rj_num = (Text(str(num), font="思源宋体 Heavy",
                               color=BLACK).scale(1).next_to(variable_Rj,
                                                             RIGHT,
                                                             buff=0.3))
                return Transform(all_num[1], Rj_num)
            elif string == 'j':
                j_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(1).next_to(variable_j,
                                                            RIGHT,
                                                            buff=0.3))
                return Transform(all_num[2], j_num)
            elif string == 'i':
                i_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(1).next_to(variable_i,
                                                            RIGHT,
                                                            buff=0.3))
                return Transform(all_num[3], i_num)
            elif string == 'Rj2':
                Rj2_num = (Text(str(num), font="思源宋体 Heavy",
                                color=BLACK).scale(1).next_to(variable_Rj2,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[4], Rj2_num)

        # 冒泡排序
        R = [5, 1, 2, 7, 0, 6, 3, 4]
        rec_fix = rec_base.copy()  # 固定的长条位置
        NULL = Dot(color=WHITE).next_to(title, LEFT)  # 用于代替 self.play() 中的 空
        bubble_all = VGroup()
        for i in range(8):
            bubble = Text("O", font="思源宋体",
                          color=BLUE).scale(0.5).next_to(rec_subscript[i],
                                                         DOWN,
                                                         buff=0.2)
            bubble_all.add(bubble.copy())
        size = len(R)
        flag = False
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()
        code_move(1)
        self.play(FadeIn(flag_num))
        self.wait()
        for i in range(1, 5):
            code_move(2) if i == 1 else code_move(
                2, FadeInFromDown(bubble_all[8 - i + 1]))
            self.play(FadeIn(i_num)) if i == 1 else self.play(
                renew_variable('i', i))
            self.wait()
            code_move(4)
            flag = False
            self.play(renew_variable('flag', "false"))
            self.wait()
            vec_j_all.next_to(rec_fix[0], DOWN, buff=0.35)
            for j in range(0, size - i):
                code_move(5)
                self.play(FadeIn(vec_j_all)) if j == 0 else self.play(
                    vec_j_all.shift, RIGHT * 1.3)
                self.play(FadeIn(j_num), FadeIn(Rj_num), FadeIn(Rj2_num)) if (
                    i == 1 and j == 0) else self.play(
                        renew_variable('j', j), renew_variable('Rj', R[j]),
                        renew_variable('Rj2', R[j + 1]))
                self.wait()
                code_move(6)
                if R[j + 1] < R[j]:
                    code_move(7)
                    R[j], R[j + 1] = R[j + 1], R[j]
                    self.play(rec_map[j].shift, RIGHT * 1.3,
                              rec_map[j + 1].shift, LEFT * 1.3,
                              num_map[j].shift, RIGHT * 1.3,
                              num_map[j + 1].shift, LEFT * 1.3,
                              renew_variable('Rj', R[j]),
                              renew_variable('Rj2', R[j + 1]))
                    self.wait()
                    # 哈希表更新
                    rec_map[j], num_map[j], rec_map[j + 1], num_map[
                        j + 1] = rec_map[j +
                                         1], num_map[j +
                                                     1], rec_map[j], num_map[j]
                    code_move(8)
                    flag = True
                    self.play(renew_variable('flag', "true"))
                    self.wait()
            code_move(5)
            self.play(FadeOut(vec_j_all))
            self.wait()
        code_move(2, FadeInFromDown(bubble_all[0]),
                  FadeInFromDown(bubble_all[1]), FadeInFromDown(bubble_all[2]),
                  FadeInFromDown(bubble_all[3]), FadeInFromDown(bubble_all[4]))


class straightSelectSort(Scene_White):
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
        frame_min = Rectangle(
            color=GREEN,
            stroke_opacity=0,
            height=4.5,
            width=3,
        ).to_corner(UR, buff=0)
        frame_code = Rectangle(
            color=BLUE,
            stroke_opacity=0,
            height=3.5,
            width=7.1 + 1,
        ).to_corner(DL, buff=0)
        frame_variable = Rectangle(
            color=RED,
            stroke_opacity=0,
            height=3.5,
            width=7.1 - 1,
        ).to_corner(DR, buff=0)
        self.add(frame_animation, frame_code, frame_variable)

        # --------------- 动画框架 ---------------
        # 标题
        title = (Text("直接选择排序", font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).to_corner(UP).shift(UP * 0.25))
        self.add(title)
        # 基准长方形
        rectangle_base = MyRectangle(fill_color=BLUE,
                                     color=BLUE,
                                     height=2.5,
                                     width=0.8,
                                     fill_opacity=1,
                                     opacity=1,
                                     stroke_opacity=1)
        # 存储待排序的长方块
        rec_base = VGroup()
        # 存储每个长方块的高度
        rec_height = []
        for i in range(8):
            highest = 2.5
            shortest = 0.5
            gap = (highest - shortest) / 7
            rec_height_element = shortest + gap * i
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
        rec_base.move_to(frame_animation).shift(UP * 0.2)
        # 各方块下标
        rec_subscript = VGroup()
        for i in range(8):
            subscript = (Text(str(i), font="思源宋体 Heavy",
                              color=BLACK).scale(0.4).next_to(rec_base[i],
                                                              DOWN,
                                                              buff=0.1))
            rec_subscript.add(subscript)
        # 额外的 -1 下标
        extra_subscript = (Text(str(-1), font="思源宋体 Heavy",
                                color=BLACK).scale(0.4).move_to(
                                    rec_subscript[0]).shift(LEFT * 0.6))
        # 各方块坐标
        rec_coordinate = VGroup()
        for i in range(8):
            coordinate = (Text(str(chaos[i]), font="江西拙楷",
                               color=BLACK).scale(0.7).move_to(rec_base[i]))
            rec_coordinate.add(coordinate)
        # 映射表
        rec_map = {
            0: rec_base[0],
            1: rec_base[1],
            2: rec_base[2],
            3: rec_base[3],
            4: rec_base[4],
            5: rec_base[5],
            6: rec_base[6],
            7: rec_base[7]
        }
        num_map = {
            0: rec_coordinate[0],
            1: rec_coordinate[1],
            2: rec_coordinate[2],
            3: rec_coordinate[3],
            4: rec_coordinate[4],
            5: rec_coordinate[5],
            6: rec_coordinate[6],
            7: rec_coordinate[7]
        }
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
        background.set_height(3, stretch=True).set_width(7, stretch=True)
        background.move_to(frame_code)

        # 代码 + 移动框
        class codeline_straightSelectSort(Text):
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
            temp_codes = straightSelectSort_codes
            for index in range(begin, 0, -1):
                if temp_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.14
                elif temp_codes[num][index] == " " and record == 0:
                    record = 1
                elif temp_codes[num][index] != " ":
                    record = 0
            return origin_len * 0.14

        codes_straightSelectSort = (VGroup(*[
            codeline_straightSelectSort(code)
            for code in straightSelectSort_codes[:]
        ]).arrange(DOWN, aligned_edge=LEFT,
                   buff=0.05).next_to(background.get_top(), DOWN,
                                      buff=0).shift(LEFT * 0 + DOWN * 0.1))

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=2.5,
            stroke_color=BLUE,
            corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1,
                         fill_color=RED).rotate(90 * DEGREES, axis=IN)
        arrow.scale(0.1)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))

        # 一键添加代码背景 and 代码
        self.add(background, codes_straightSelectSort)
        # self.add(arrow, move_frame)
        move_frame.set_width(ignore_space_len(codes_straightSelectSort[0], 0),
                             stretch=True).set_height(
                                 0.255, stretch=True).move_to(
                                     codes_straightSelectSort[0]).align_to(
                                         codes_straightSelectSort[0],
                                         RIGHT).shift(RIGHT * 0.05)
        arrow.next_to(move_frame, LEFT, buff=0.1)

        # 箭头
        vec_j = (Arrow(np.array([0, -1, 0]),
                       np.array([0, 1, 0]),
                       color=BLACK,
                       buff=0.3,
                       fill_color=BLACK).scale(0.35))
        vec_pos = vec_j.copy()
        vec_j.next_to(rec_base[0], DOWN, buff=0.35)
        vec_pos.next_to(rec_base[1], DOWN, buff=0.35)
        vec_j_variables = (Text("j", font="思源宋体 Heavy",
                                color=BLACK).scale(0.6))
        vec_pos_variables = (Text("pos", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.6))
        vec_j_variables.add_updater(lambda a: a.next_to(vec_j, DOWN, buff=0.1))
        vec_pos_variables.add_updater(
            lambda a: a.next_to(vec_pos, DOWN, buff=0.1))
        vec_j_all = VGroup(vec_j, vec_j_variables)
        vec_pos_all = VGroup(vec_pos, vec_pos_variables)
        # self.add(vec_j_all, vec_pos_all)

        # 变量框
        t2c = {
            "Size": BLUE,
            "j": RED,
            "pos": PURPLE,
            "R[min]": GOLD,
            "R[j]": "#01cd74",
            "R[pos]": "#da1884",
        }
        variable_rectangle = Rectangle(
            color="#003472", height=3, width=5.5,
            stroke_opacity=1).move_to(frame_variable)
        variable_Size = (Text("Size:  8",
                              font="思源宋体 Heavy",
                              color=BLACK,
                              t2c=t2c).scale(1).next_to(
                                  variable_rectangle.get_top(), DOWN,
                                  buff=0.3).align_to(variable_rectangle,
                                                     LEFT).shift(RIGHT * 0.3))
        variable_j = (Text("j:", font="思源宋体 Heavy", color=BLACK,
                           t2c=t2c).scale(1).next_to(variable_Size,
                                                     DOWN,
                                                     buff=0.5).align_to(
                                                         variable_Size, LEFT))
        variable_pos = (Text("pos:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(1).next_to(variable_j,
                                                       DOWN,
                                                       buff=0.5).align_to(
                                                           variable_Size,
                                                           LEFT))
        variable_Rm = (Text("R[min]:", font="思源宋体 Heavy", color=BLACK,
                            t2c=t2c).scale(1).next_to(
                                variable_rectangle.get_top(), DOWN,
                                buff=0.3).align_to(variable_rectangle,
                                                   RIGHT).shift(LEFT * 1))
        variable_Rj = (Text("R[j]:", font="思源宋体 Heavy", color=BLACK,
                            t2c=t2c).scale(1).next_to(variable_Rm,
                                                      DOWN,
                                                      buff=0.4).align_to(
                                                          variable_Rm, LEFT))
        variable_Rp = (Text("R[pos]:", font="思源宋体 Heavy", color=BLACK,
                            t2c=t2c).scale(1).next_to(variable_Rj,
                                                      DOWN,
                                                      buff=0.4).align_to(
                                                          variable_Rj, LEFT))
        Rm_num = (Text(str(5), font="思源宋体 Heavy",
                       color=BLACK).scale(1).next_to(variable_Rm,
                                                     RIGHT,
                                                     buff=0.3))
        pos_num = (Text(str(0), font="思源宋体 Heavy",
                        color=BLACK).scale(1).next_to(variable_pos,
                                                      RIGHT,
                                                      buff=0.3))
        Rj_num = (Text(str(1), font="思源宋体 Heavy",
                       color=BLACK).scale(1).next_to(variable_Rj,
                                                     RIGHT,
                                                     buff=0.3))
        j_num = (Text(str(1), font="思源宋体 Heavy",
                      color=BLACK).scale(1).next_to(variable_j,
                                                    RIGHT,
                                                    buff=0.3))
        Rp_num = (Text(str(5), font="思源宋体 Heavy",
                       color=BLACK).scale(1).next_to(variable_Rp,
                                                     RIGHT,
                                                     buff=0.3))
        all_num = VGroup(Rm_num, pos_num, Rj_num, j_num, Rp_num)
        self.add(variable_rectangle, variable_Size, variable_j, variable_Rm,
                 variable_pos, variable_Rj, variable_Rp)
        # self.add(all_num)

        # min 框
        min_rectangle = RoundedRectangle(
            stroke_width=8,
            stroke_color=GREEN_B,
            fill_color="#EBEBEB",
            fill_opacity=0,
            plot_depth=-1,
            corner_radius=0.05,
            sheen_factor=0.1,
            sheen_direction=UR,
        )
        min_rectangle.set_height(4, stretch=True).set_width(2, stretch=True)
        min_rectangle.move_to(frame_min)
        min_variables = (Text("MIN", font="思源宋体 Heavy", color=BLACK,
                              t2c=t2c).scale(1).next_to(
                                  min_rectangle.get_bottom(), UP, buff=0.2))
        self.add(min_rectangle, min_variables)
        """
        int pos, min, j;
        for (pos = 0; pos < size - 1; pos++)
        {
            min = pos;
            for (j = pos + 1; j < size; ++j)
                if (R[j] < R[min])
                    min = j;
            if (pos != min)      
                swap(R[pos], R[min]);
        }
        """

        # 借用 OOP 的方法
        # 面向对象零 (包装代码框移动)
        def code_move(i, *method):
            # 调用方法举例: code_move(1, 0, FadeIn(vec_pos_all))
            self.play(
                *method,
                move_frame.set_width,
                ignore_space_len(codes_straightSelectSort[i], i),
                move_frame.move_to,
                codes_straightSelectSort[i],
                move_frame.align_to,
                codes_straightSelectSort[i],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {
                    "height": 0.255,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()

        # 面向对象一 (变量框元素值更新)

        def renew_variable(string, num):
            # 调用方法举例: self.play(renew_variable('rm', 1))
            if string == 'Rm':
                Rm_num = (Text(str(num), font="思源宋体 Heavy",
                               color=BLACK).scale(1).next_to(variable_Rm,
                                                             RIGHT,
                                                             buff=0.3))
                return Transform(all_num[0], Rm_num)
            elif string == 'pos':
                pos_num = (Text(str(num), font="思源宋体 Heavy",
                                color=BLACK).scale(1).next_to(variable_pos,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[1], pos_num)
            elif string == 'Rj':
                Rj_num = (Text(str(num), font="思源宋体 Heavy",
                               color=BLACK).scale(1).next_to(variable_Rj,
                                                             RIGHT,
                                                             buff=0.3))
                return Transform(all_num[2], Rj_num)
            elif string == 'j':
                j_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(1).next_to(variable_j,
                                                            RIGHT,
                                                            buff=0.3))
                return Transform(all_num[3], j_num)
            elif string == 'Rp':
                Rp_num = (Text(str(num), font="思源宋体 Heavy",
                               color=BLACK).scale(1).next_to(variable_Rp,
                                                             RIGHT,
                                                             buff=0.3))
                return Transform(all_num[4], Rp_num)

        # 直接选择排序
        R = [5, 1, 2, 7, 0, 6, 3, 4]
        size = len(R)
        rec_fix = rec_base.copy()  # 固定的长条位置
        NULL = Dot(color=WHITE).next_to(title, LEFT)  # 用于代替 self.play() 中的 空
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()
        for pos in range(size - 1):
            code_move(1) if pos == 0 else code_move(1, FadeOut(MIN))
            vec_pos_all.next_to(rec_fix[pos], DOWN,
                                buff=0.35) if pos == 0 else NULL
            self.play(FadeIn(vec_pos_all)) if pos == 0 else self.play(
                vec_pos_all.shift, RIGHT * 1.3)
            self.play(FadeIn(pos_num)) if pos == 0 else self.play(
                renew_variable('pos', pos))
            self.wait()
            code_move(3)
            min = pos
            MIN = VGroup(rec_map[pos].copy(),
                         num_map[pos].copy()).move_to(frame_min)
            self.play(FadeIn(MIN))
            self.play(
                FadeIn(Rm_num), FadeIn(Rp_num)) if pos == 0 else self.play(
                    renew_variable('Rm', R[min]), renew_variable('Rp', R[pos]))
            self.wait()
            for j in range(pos + 1, size):
                code_move(4)
                vec_j_all.next_to(rec_fix[pos + 1], DOWN,
                                  buff=0.35) if j == pos + 1 else NULL
                self.play(FadeIn(vec_j_all)) if j == pos + 1 else self.play(
                    vec_j_all.shift, RIGHT * 1.3)
                self.play(FadeIn(j_num), FadeIn(Rj_num)) if (
                    pos == 0 and j == pos + 1) else self.play(
                        renew_variable('j', j), renew_variable('Rj', R[j]))
                self.wait()
                code_move(5)
                if R[j] < R[min]:
                    code_move(6)
                    min = j
                    self.play(
                        Transform(
                            MIN,
                            VGroup(rec_map[j].copy(),
                                   num_map[j].copy()).move_to(frame_min)),
                        renew_variable('Rm', R[min]))
                    self.wait()
            code_move(4)
            code_move(7, FadeOut(vec_j_all))
            if pos != min:
                code_move(8)
                R[pos], R[min] = R[min], R[pos]
                self.play(rec_map[pos].shift, RIGHT * 1.3 * (min - pos),
                          rec_map[min].shift, LEFT * 1.3 * (min - pos),
                          num_map[pos].shift, RIGHT * 1.3 * (min - pos),
                          num_map[min].shift, LEFT * 1.3 * (min - pos),
                          renew_variable('Rp', R[pos]),
                          renew_variable('Rm', R[min]))
                self.wait()
                # 哈希表更新
                rec_map[pos], num_map[pos], rec_map[min], num_map[
                    min] = rec_map[min], num_map[min], rec_map[pos], num_map[
                        pos]
        code_move(1)
        self.play(FadeOutAndShift(vec_pos_all, RIGHT))


class heapSort_siftDown(Scene_White):
    def construct(self):
        # global
        # Frame 整体框架
        # height: 8  *  width: 14.2
        frame_code = Rectangle(
            color=BLUE,
            stroke_opacity=0,
            height=4.5,
            width=7.1,
        ).to_corner(UR, buff=0)
        frame_variable = Rectangle(
            color=RED,
            stroke_opacity=0,
            height=3.5,
            width=7.1,
        ).to_corner(DR, buff=0)
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_color=WHITE,
            fill_opacity=1,
            height=8,
            width=7.1,
        ).to_corner(LEFT, buff=0)
        self.add(frame_code, frame_variable, frame_animation)

        # --------------- 动画框架 ---------------
        # 标题
        title = (Text("堆排序       siftDown(R, 0, 11)",
                      font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).to_corner(UP).shift(UP * 0.25))
        self.add(title)
        # 基准圆形
        circle_base = Circle(radius=0.4,
                             stroke_width=5,
                             stroke_color=BLACK,
                             stroke_opacity=1)
        # 结点集合
        base_all = VGroup()
        for i in range(11):
            base_tmp = circle_base.copy()
            base_all.add(base_tmp)
        # 结点 0 的位置
        base_all[0].move_to(frame_animation).align_to(
            frame_animation, UP).shift(DOWN * 0.8 + RIGHT * 0.25)
        # 结点 1 结点 2 的位置
        base_all[1].move_to(base_all[0]).shift(DOWN * 1.3).shift(LEFT * 1.2)
        base_all[2].move_to(base_all[0]).shift(DOWN * 1.3).shift(RIGHT * 1.2)
        # 结点 3 结点 4 的位置
        base_all[3].move_to(base_all[1]).shift(DOWN * 1.3).shift(LEFT * 1.1)
        base_all[4].move_to(base_all[1]).shift(DOWN * 1.3).shift(RIGHT * 0.6)
        # 结点 5 结点 6 的位置
        base_all[5].move_to(base_all[2]).shift(DOWN * 1.3).shift(LEFT * 0.6)
        base_all[6].move_to(base_all[2]).shift(DOWN * 1.3).shift(RIGHT * 1.1)
        # 结点 7 结点 8 的位置
        base_all[7].move_to(base_all[3]).shift(DOWN * 1.3).shift(LEFT * 0.6)
        base_all[8].move_to(base_all[3]).shift(DOWN * 1.3).shift(RIGHT * 0.6)
        # 结点 9 结点 10 的位置
        base_all[9].move_to(base_all[4]).shift(DOWN * 1.3).shift(LEFT * 0.1)
        base_all[10].move_to(base_all[4]).shift(DOWN * 1.3).shift(RIGHT * 1.1)
        # 结点连线集合
        line_all = VGroup()
        # 结点 0 1 连线
        base_0 = base_all[0].point_at_angle(250 * DEGREES)
        base_1 = base_all[1].point_at_angle(90 * DEGREES)
        line_0_1 = Line(np.array(base_0),
                        np.array(base_1),
                        color=BLACK,
                        stroke_width=5)
        # 结点 0 2 连线
        base_0 = base_all[0].point_at_angle(290 * DEGREES)
        base_2 = base_all[2].point_at_angle(90 * DEGREES)
        line_0_2 = Line(np.array(base_0),
                        np.array(base_2),
                        color=BLACK,
                        stroke_width=5)
        # 结点 1 3 连线
        base_1 = base_all[1].point_at_angle(240 * DEGREES)
        base_3 = base_all[3].point_at_angle(90 * DEGREES)
        line_1_3 = Line(np.array(base_1),
                        np.array(base_3),
                        color=BLACK,
                        stroke_width=5)
        # 结点 1 4 连线
        base_1 = base_all[1].point_at_angle(290 * DEGREES)
        base_4 = base_all[4].point_at_angle(90 * DEGREES)
        line_1_4 = Line(np.array(base_1),
                        np.array(base_4),
                        color=BLACK,
                        stroke_width=5)
        # 结点 2 5 连线
        base_2 = base_all[2].point_at_angle(250 * DEGREES)
        base_5 = base_all[5].point_at_angle(90 * DEGREES)
        line_2_5 = Line(np.array(base_2),
                        np.array(base_5),
                        color=BLACK,
                        stroke_width=5)
        # 结点 2 6 连线
        base_2 = base_all[2].point_at_angle(300 * DEGREES)
        base_6 = base_all[6].point_at_angle(90 * DEGREES)
        line_2_6 = Line(np.array(base_2),
                        np.array(base_6),
                        color=BLACK,
                        stroke_width=5)
        # 结点 3 7 连线
        base_3 = base_all[3].point_at_angle(260 * DEGREES)
        base_7 = base_all[7].point_at_angle(90 * DEGREES)
        line_3_7 = Line(np.array(base_3),
                        np.array(base_7),
                        color=BLACK,
                        stroke_width=5)
        # 结点 3 8 连线
        base_3 = base_all[3].point_at_angle(280 * DEGREES)
        base_8 = base_all[8].point_at_angle(90 * DEGREES)
        line_3_8 = Line(np.array(base_3),
                        np.array(base_8),
                        color=BLACK,
                        stroke_width=5)
        # 结点 4 9 连线
        base_4 = base_all[4].point_at_angle(270 * DEGREES)
        base_9 = base_all[9].point_at_angle(90 * DEGREES)
        line_4_9 = Line(np.array(base_4),
                        np.array(base_9),
                        color=BLACK,
                        stroke_width=5)
        # 结点 4 10 连线
        base_4 = base_all[4].point_at_angle(310 * DEGREES)
        base_10 = base_all[10].point_at_angle(120 * DEGREES)
        line_4_10 = Line(np.array(base_4),
                         np.array(base_10),
                         color=BLACK,
                         stroke_width=5)
        # 集合
        line_all = VGroup(line_0_1, line_0_2, line_1_3, line_1_4, line_2_5,
                          line_2_6, line_3_7, line_3_8, line_4_9, line_4_10)
        self.add(base_all, line_all)

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
        background.set_height(3.6, stretch=True).set_width(6.5, stretch=True)
        background.move_to(frame_code).shift(DOWN * 0.4)

        # 代码 + 移动框
        class codeline_siftDown(Text):
            CONFIG = {
                "size": 0.4,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        def ignore_space_len(code, num):
            origin_len = len(code)
            begin = origin_len - 1
            record = 0
            temp_codes = siftDown_codes
            for index in range(begin, 0, -1):
                if temp_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.115
                elif temp_codes[num][index] == " " and record == 0:
                    record = 1
                elif temp_codes[num][index] != " ":
                    record = 0
            return origin_len * 0.115

        codes_siftDown = (VGroup(
            *[codeline_siftDown(code) for code in siftDown_codes]).arrange(
                DOWN, aligned_edge=LEFT,
                buff=0.05).next_to(background.get_top(), DOWN,
                                   buff=0).shift(RIGHT * 0.1 + DOWN * 0.15))

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=2.5,
            stroke_color=BLUE,
            corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1,
                         fill_color=RED).rotate(90 * DEGREES, axis=IN)
        arrow.scale(0.08)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.08))

        # 一键添加代码背景 and 代码
        self.add(background, codes_siftDown)
        # self.add(arrow, move_frame)
        move_frame.set_width(
            ignore_space_len(codes_siftDown[1], 1),
            stretch=True).set_height(0.22, stretch=True).move_to(
                codes_siftDown[1]).align_to(codes_siftDown[1],
                                            RIGHT).shift(RIGHT * 0.05)

        # 变量框
        t2c = {
            "Size": BLUE,
            "tmp": RED,
            "pos": PURPLE,
            "child": "#01cd74",
            "R[child]": GOLD,
            "R[pos]": "#da1884",
        }
        variable_rectangle = Rectangle(
            color="#003472", height=3, width=6.5,
            stroke_opacity=1).move_to(frame_variable)
        variable_Size = (Text("Size:  11",
                              font="思源宋体 Heavy",
                              color=BLACK,
                              t2c=t2c).scale(1).next_to(
                                  variable_rectangle.get_top(), DOWN,
                                  buff=0.3).align_to(variable_rectangle,
                                                     LEFT).shift(RIGHT * 0.3))
        variable_Rp = (Text("R[pos]:", font="思源宋体 Heavy", color=BLACK,
                            t2c=t2c).scale(1).next_to(variable_Size,
                                                      DOWN,
                                                      buff=0.5).align_to(
                                                          variable_Size, LEFT))
        variable_Rc = (Text("R[child]:",
                            font="思源宋体 Heavy",
                            color=BLACK,
                            t2c=t2c).scale(1).next_to(variable_Rp,
                                                      DOWN,
                                                      buff=0.5).align_to(
                                                          variable_Size, LEFT))
        variable_tmp = (Text("tmp:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(1).next_to(
                                 variable_rectangle.get_top(), DOWN,
                                 buff=0.3).align_to(variable_rectangle,
                                                    RIGHT).shift(LEFT * 1.5))
        variable_pos = (Text("pos:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(1).next_to(variable_tmp,
                                                       DOWN,
                                                       buff=0.4).align_to(
                                                           variable_tmp, LEFT))
        variable_child = (Text("child:",
                               font="思源宋体 Heavy",
                               color=BLACK,
                               t2c=t2c).scale(1).next_to(variable_pos,
                                                         DOWN,
                                                         buff=0.4).align_to(
                                                             variable_pos,
                                                             LEFT))
        Rp_num = (Text(str(8), font="思源宋体 Heavy",
                       color=BLACK).scale(1).next_to(variable_Rp,
                                                     RIGHT,
                                                     buff=0.3))
        Rc_num = (Text(str(7), font="思源宋体 Heavy",
                       color=BLACK).scale(1).next_to(variable_Rc,
                                                     RIGHT,
                                                     buff=0.3))
        tmp_num = (Text(str(8), font="思源宋体 Heavy",
                        color=BLACK).scale(1).next_to(variable_tmp,
                                                      RIGHT,
                                                      buff=0.3))
        pos_num = (Text(str(0), font="思源宋体 Heavy",
                        color=BLACK).scale(1).next_to(variable_pos,
                                                      RIGHT,
                                                      buff=0.3))
        child_num = (Text(str(1), font="思源宋体 Heavy",
                          color=BLACK).scale(1).next_to(variable_child,
                                                        RIGHT,
                                                        buff=0.3))
        all_num = VGroup(Rp_num, Rc_num, tmp_num, pos_num, child_num)
        self.add(variable_rectangle, variable_Size, variable_Rp, variable_Rc,
                 variable_tmp, variable_pos, variable_child)
        self.add(all_num[0], all_num[3])  # self.add(all_num)

        # 正方块序列
        rectangle_all = VGroup()
        for i in range(11):
            rectangle_base = MySquare(color=BLACK,
                                      side_length=0.55,
                                      stroke_opacity=1)
            rectangle_all.add(rectangle_base)
        for i in range(1, 11):
            rectangle_all[i].next_to(rectangle_all[i - 1], RIGHT, buff=0)
        rectangle_all.move_to(frame_animation).align_to(frame_animation,
                                                        DOWN).shift(UP * 0.8)
        self.add(rectangle_all)

        # 序列的序号
        rectangle_num_all = VGroup()
        for i in range(11):
            rectangle_num_base = Text(str(i), font="思源宋体 Heavy",
                                      color=BLACK).scale(0.5).next_to(
                                          rectangle_all[i], UP, buff=0.1)
            rectangle_num_all.add(rectangle_num_base)
        self.add(rectangle_num_all)

        # 序列的元素
        rectangle_list = [8, 7, 10, 6, 5, 0, 9, 2, 1, 4, 3]
        rectangle_element_all = VGroup()
        for i in range(11):
            rectangle_element_tmp = Text(str(rectangle_list[i]),
                                         font="江西拙楷",
                                         color=BLACK).scale(0.6).move_to(
                                             rectangle_all[i])
            rectangle_element_all.add(rectangle_element_tmp)
        self.add(rectangle_element_all)

        # 结点元素集合
        element_list = [8, 7, 10, 6, 5, 0, 9, 2, 1, 4, 3]
        element_all = VGroup()
        for i in range(11):
            element_tmp = Text(str(element_list[i]), font="江西拙楷",
                               color=BLACK).scale(0.8).move_to(base_all[i])
            element_all.add(element_tmp)
        self.add(element_all)

        # 移动圆环
        move_circle = Circle(radius=0.3,
                             stroke_width=15,
                             stroke_color=BLUE,
                             stroke_opacity=1).shift(LEFT * 10)  # 让它换地方消失

        # 借用 OOP 的方法
        # 面向对象零 (包装代码框移动)
        def code_move(i, *method):
            # 调用方法举例: code_move(1, 0, FadeIn(vec_pos_all))
            self.play(
                *method,
                move_frame.set_width,
                ignore_space_len(codes_siftDown[i], i),
                move_frame.move_to,
                codes_siftDown[i],
                move_frame.align_to,
                codes_siftDown[i],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {
                    "height": 0.22,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()

        # 面向对象一 (变量框元素值更新)
        def renew_variable(string, num):
            # 调用方法举例: self.play(renew_variable('rm', 1))
            if string == 'Rp':
                Rp_num = (Text(str(num), font="思源宋体 Heavy",
                               color=BLACK).scale(1).next_to(variable_Rp,
                                                             RIGHT,
                                                             buff=0.3))
                return Transform(all_num[0], Rp_num)
            elif string == 'Rc':
                Rc_num = (Text(str(num), font="思源宋体 Heavy",
                               color=BLACK).scale(1).next_to(variable_Rc,
                                                             RIGHT,
                                                             buff=0.3))
                return Transform(all_num[1], Rc_num)
            elif string == 'tmp':
                tmp_num = (Text(str(num), font="思源宋体 Heavy",
                                color=BLACK).scale(1).next_to(variable_tmp,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[2], tmp_num)
            elif string == 'pos':
                pos_num = (Text(str(num), font="思源宋体 Heavy",
                                color=BLACK).scale(1).next_to(variable_pos,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[3], pos_num)
            elif string == 'child':
                child_num = (Text(str(num), font="思源宋体 Heavy",
                                  color=BLACK).scale(1).next_to(variable_child,
                                                                RIGHT,
                                                                buff=0.3))
                return Transform(all_num[4], child_num)

        # siftDown
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()
        code_move(2)
        self.play(FadeIn(all_num[2]))
        self.wait()
        code_move(3)
        code_move(5)
        move_circle_new_position = move_circle.copy()
        move_circle_new_position.move_to(base_all[1])
        self.play(FadeIn(all_num[1]), FadeIn(all_num[4]),
                  FadeIn(move_circle_new_position), FadeOut(move_circle))
        move_circle = move_circle_new_position
        self.wait()
        code_move(6)
        code_move(7)
        move_circle_new_position = move_circle.copy()
        move_circle_new_position.move_to(base_all[2])
        self.play(renew_variable('child', 2), renew_variable('Rc', 10),
                  FadeIn(move_circle_new_position), FadeOut(move_circle))
        move_circle = move_circle_new_position
        self.wait()
        code_move(8)
        code_move(9)
        element_tmp = element_all[2].copy().move_to(element_all[0])
        rectangle_element_tmp = rectangle_element_all[2].copy().move_to(
            rectangle_element_all[0])
        self.play(
            renew_variable('Rp', 10),
            Transform(element_all[0], element_tmp.copy()),
            Transform(rectangle_element_all[0], rectangle_element_tmp.copy()))
        self.wait()
        code_move(3)
        self.play(renew_variable('pos', 2))
        self.wait()
        code_move(5)
        move_circle_new_position = move_circle.copy()
        move_circle_new_position.move_to(base_all[5])
        self.play(renew_variable('child', 5), renew_variable('Rc', 0),
                  FadeIn(move_circle_new_position), FadeOut(move_circle))
        move_circle = move_circle_new_position
        self.wait()
        code_move(6)
        code_move(7)
        move_circle_new_position = move_circle.copy()
        move_circle_new_position.move_to(base_all[6])
        self.play(renew_variable('child', 6), renew_variable('Rc', 9),
                  FadeIn(move_circle_new_position), FadeOut(move_circle))
        move_circle = move_circle_new_position
        self.wait()
        code_move(8)
        code_move(9)
        element_tmp = element_all[6].copy().move_to(element_all[2])
        rectangle_element_tmp = rectangle_element_all[6].copy().move_to(
            rectangle_element_all[2])
        self.play(
            renew_variable('Rp', 9),
            Transform(element_all[2], element_tmp.copy()),
            Transform(rectangle_element_all[2], rectangle_element_tmp.copy()))
        self.wait()
        code_move(3)
        self.play(renew_variable('pos', 6))
        self.wait()
        code_move(13)
        element_tmp = Text(str(8), font="江西拙楷",
                           color=BLACK).scale(0.8).move_to(base_all[6])
        rectangle_element_tmp = Text(str(8), font="江西拙楷",
                                     color=BLACK).scale(0.6).move_to(
                                         rectangle_all[6])
        self.play(
            renew_variable('Rp', 8),
            Transform(element_all[6], element_tmp.copy()),
            Transform(rectangle_element_all[6], rectangle_element_tmp.copy()))
        self.wait()
        self.play(FadeOut(move_frame), FadeOut(arrow), FadeOut(move_circle))
        self.wait()


class heapSort_heapSort(Scene_White):
    def construct(self):
        # global
        # Frame 整体框架
        # height: 8  *  width: 14.2
        frame_code = Rectangle(
            color=BLUE,
            stroke_opacity=0,
            height=4.5,
            width=7.1,
        ).to_corner(UR, buff=0)
        frame_variable = Rectangle(
            color=RED,
            stroke_opacity=0,
            height=3.5,
            width=7.1,
        ).to_corner(DR, buff=0)
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_color=WHITE,
            fill_opacity=1,
            height=8,
            width=7.1,
        ).to_corner(LEFT, buff=0)
        self.add(frame_code, frame_variable, frame_animation)

        # --------------- 动画框架 ---------------
        # 标题
        title = (Text("堆排序       heapSort(R, 11)",
                      font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).to_corner(UP).shift(UP * 0.25))
        self.add(title)
        # 基准圆形
        circle_base = Circle(radius=0.4,
                             stroke_width=5,
                             stroke_color=BLACK,
                             stroke_opacity=1)
        # 结点集合
        base_all = VGroup()
        for i in range(11):
            base_tmp = circle_base.copy()
            base_all.add(base_tmp)
        # 结点 0 的位置
        base_all[0].move_to(frame_animation).align_to(
            frame_animation, UP).shift(DOWN * 0.8 + RIGHT * 0.25)
        # 结点 1 结点 2 的位置
        base_all[1].move_to(base_all[0]).shift(DOWN * 1.3).shift(LEFT * 1.2)
        base_all[2].move_to(base_all[0]).shift(DOWN * 1.3).shift(RIGHT * 1.2)
        # 结点 3 结点 4 的位置
        base_all[3].move_to(base_all[1]).shift(DOWN * 1.3).shift(LEFT * 1.1)
        base_all[4].move_to(base_all[1]).shift(DOWN * 1.3).shift(RIGHT * 0.6)
        # 结点 5 结点 6 的位置
        base_all[5].move_to(base_all[2]).shift(DOWN * 1.3).shift(LEFT * 0.6)
        base_all[6].move_to(base_all[2]).shift(DOWN * 1.3).shift(RIGHT * 1.1)
        # 结点 7 结点 8 的位置
        base_all[7].move_to(base_all[3]).shift(DOWN * 1.3).shift(LEFT * 0.6)
        base_all[8].move_to(base_all[3]).shift(DOWN * 1.3).shift(RIGHT * 0.6)
        # 结点 9 结点 10 的位置
        base_all[9].move_to(base_all[4]).shift(DOWN * 1.3).shift(LEFT * 0.1)
        base_all[10].move_to(base_all[4]).shift(DOWN * 1.3).shift(RIGHT * 1.1)
        # 结点连线集合
        line_all = VGroup()
        # 结点 0 1 连线
        base_0 = base_all[0].point_at_angle(250 * DEGREES)
        base_1 = base_all[1].point_at_angle(90 * DEGREES)
        line_0_1 = Line(np.array(base_0),
                        np.array(base_1),
                        color=BLACK,
                        stroke_width=5)
        # 结点 0 2 连线
        base_0 = base_all[0].point_at_angle(290 * DEGREES)
        base_2 = base_all[2].point_at_angle(90 * DEGREES)
        line_0_2 = Line(np.array(base_0),
                        np.array(base_2),
                        color=BLACK,
                        stroke_width=5)
        # 结点 1 3 连线
        base_1 = base_all[1].point_at_angle(240 * DEGREES)
        base_3 = base_all[3].point_at_angle(90 * DEGREES)
        line_1_3 = Line(np.array(base_1),
                        np.array(base_3),
                        color=BLACK,
                        stroke_width=5)
        # 结点 1 4 连线
        base_1 = base_all[1].point_at_angle(290 * DEGREES)
        base_4 = base_all[4].point_at_angle(90 * DEGREES)
        line_1_4 = Line(np.array(base_1),
                        np.array(base_4),
                        color=BLACK,
                        stroke_width=5)
        # 结点 2 5 连线
        base_2 = base_all[2].point_at_angle(250 * DEGREES)
        base_5 = base_all[5].point_at_angle(90 * DEGREES)
        line_2_5 = Line(np.array(base_2),
                        np.array(base_5),
                        color=BLACK,
                        stroke_width=5)
        # 结点 2 6 连线
        base_2 = base_all[2].point_at_angle(300 * DEGREES)
        base_6 = base_all[6].point_at_angle(90 * DEGREES)
        line_2_6 = Line(np.array(base_2),
                        np.array(base_6),
                        color=BLACK,
                        stroke_width=5)
        # 结点 3 7 连线
        base_3 = base_all[3].point_at_angle(260 * DEGREES)
        base_7 = base_all[7].point_at_angle(90 * DEGREES)
        line_3_7 = Line(np.array(base_3),
                        np.array(base_7),
                        color=BLACK,
                        stroke_width=5)
        # 结点 3 8 连线
        base_3 = base_all[3].point_at_angle(280 * DEGREES)
        base_8 = base_all[8].point_at_angle(90 * DEGREES)
        line_3_8 = Line(np.array(base_3),
                        np.array(base_8),
                        color=BLACK,
                        stroke_width=5)
        # 结点 4 9 连线
        base_4 = base_all[4].point_at_angle(270 * DEGREES)
        base_9 = base_all[9].point_at_angle(90 * DEGREES)
        line_4_9 = Line(np.array(base_4),
                        np.array(base_9),
                        color=BLACK,
                        stroke_width=5)
        # 结点 4 10 连线
        base_4 = base_all[4].point_at_angle(310 * DEGREES)
        base_10 = base_all[10].point_at_angle(120 * DEGREES)
        line_4_10 = Line(np.array(base_4),
                         np.array(base_10),
                         color=BLACK,
                         stroke_width=5)
        # 集合
        line_all = VGroup(line_0_1, line_0_2, line_1_3, line_1_4, line_2_5,
                          line_2_6, line_3_7, line_3_8, line_4_9, line_4_10)
        self.add(base_all, line_all)

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
        background.set_height(3.3, stretch=True).set_width(6.5, stretch=True)
        background.move_to(frame_code).shift(DOWN * 0.6)

        # 代码 + 移动框
        class codeline_heapSort(Text):
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
            temp_codes = heapSort_codes
            for index in range(begin, 0, -1):
                if temp_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.145
                elif temp_codes[num][index] == " " and record == 0:
                    record = 1
                elif temp_codes[num][index] != " ":
                    record = 0
            return origin_len * 0.145

        codes_heapSort = (VGroup(
            *[codeline_heapSort(code) for code in heapSort_codes]).arrange(
                DOWN, aligned_edge=LEFT,
                buff=0.05).next_to(background.get_top(), DOWN,
                                   buff=0).shift(RIGHT * 0.1 + DOWN * 0.3))

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=2.5,
            stroke_color=BLUE,
            corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1,
                         fill_color=RED).rotate(90 * DEGREES, axis=IN)
        arrow.scale(0.1)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.08))

        # 一键添加代码背景 and 代码
        self.add(background, codes_heapSort)
        # self.add(arrow, move_frame)
        move_frame.set_width(
            ignore_space_len(codes_heapSort[1], 1),
            stretch=True).set_height(0.28, stretch=True).move_to(
                codes_heapSort[1]).align_to(codes_heapSort[1],
                                            RIGHT).shift(RIGHT * 0.05)

        # 变量框
        t2c = {
            "i": "#01cd74",
            "Size": BLUE,
            "R[i]": GOLD,
            "R[0]": PURPLE,
        }
        variable_rectangle = Rectangle(
            color="#003472", height=2, width=6.5,
            stroke_opacity=1).move_to(frame_variable)
        variable_Size = (Text("Size:  11",
                              font="思源宋体 Heavy",
                              color=BLACK,
                              t2c=t2c).scale(1).next_to(
                                  variable_rectangle.get_top(), DOWN,
                                  buff=0.3).align_to(variable_rectangle,
                                                     LEFT).shift(RIGHT * 0.6))
        variable_i = (Text("i:", font="思源宋体 Heavy", color=BLACK,
                           t2c=t2c).scale(1).next_to(
                               variable_rectangle.get_top(), DOWN,
                               buff=0.3).align_to(variable_rectangle,
                                                  RIGHT).shift(LEFT * 2.2))
        variable_R0 = (Text(
            "R[0]:", font="思源宋体 Heavy", color=BLACK,
            t2c=t2c).scale(1).next_to(variable_rectangle.get_bottom(),
                                      UP,
                                      buff=0.3).align_to(variable_Size, LEFT))
        variable_Ri = (Text(
            "R[i]:", font="思源宋体 Heavy", color=BLACK,
            t2c=t2c).scale(1).next_to(variable_rectangle.get_bottom(),
                                      UP,
                                      buff=0.3).align_to(variable_i, LEFT))
        i_num = (Text(str(4), font="思源宋体 Heavy",
                      color=BLACK).scale(1).next_to(variable_i,
                                                    RIGHT,
                                                    buff=0.3))
        R0_num = (Text(str(10), font="思源宋体 Heavy",
                       color=BLACK).scale(1).next_to(variable_R0,
                                                     RIGHT,
                                                     buff=0.3))
        Ri_num = (Text(str(3), font="思源宋体 Heavy",
                       color=BLACK).scale(1).next_to(variable_Ri,
                                                     RIGHT,
                                                     buff=0.3))
        all_num = VGroup(i_num, R0_num, Ri_num)
        self.add(variable_rectangle, variable_Size, variable_i, variable_R0,
                 variable_Ri)
        # self.add(all_num)

        # 正方块序列
        rectangle_all = VGroup()
        for i in range(11):
            rectangle_base = MySquare(color=BLACK,
                                      side_length=0.55,
                                      stroke_opacity=1)
            rectangle_all.add(rectangle_base)
        for i in range(1, 11):
            rectangle_all[i].next_to(rectangle_all[i - 1], RIGHT, buff=0)
        rectangle_all.move_to(frame_animation).align_to(frame_animation,
                                                        DOWN).shift(UP * 0.8)
        self.add(rectangle_all)

        # 序列的序号
        rectangle_num_all = VGroup()
        for i in range(11):
            rectangle_num_base = Text(str(i), font="思源宋体 Heavy",
                                      color=BLACK).scale(0.5).next_to(
                                          rectangle_all[i], UP, buff=0.1)
            rectangle_num_all.add(rectangle_num_base)
        self.add(rectangle_num_all)

        # 序列的元素
        rectangle_list = [8, 1, 9, 6, 3, 0, 10, 2, 7, 4, 5]
        global rectangle_element_all
        rectangle_element_all = VGroup()
        for i in range(11):
            rectangle_element_tmp = Text(str(rectangle_list[i]),
                                         font="江西拙楷",
                                         color=BLACK).scale(0.6).move_to(
                                             rectangle_all[i])
            rectangle_element_all.add(rectangle_element_tmp)
        self.add(rectangle_element_all)

        # 结点元素集合
        element_list = [8, 1, 9, 6, 3, 0, 10, 2, 7, 4, 5]
        global element_all
        element_all = VGroup()
        for i in range(11):
            element_tmp = Text(str(element_list[i]), font="江西拙楷",
                               color=BLACK).scale(0.8).move_to(base_all[i])
            element_all.add(element_tmp)
        self.add(element_all)

        # 移动圆环1
        move_circle = Circle(radius=0.3,
                             stroke_width=15,
                             stroke_color=RED,
                             stroke_opacity=1).shift(LEFT * 10)  # 让它换地方消失
        # 移动圆环2
        move_circle2 = Circle(radius=0.3,
                              stroke_width=15,
                              stroke_color=GREEN,
                              stroke_opacity=1).shift(LEFT * 10)  # 让它换地方消失

        # 借用 OOP 的方法
        # 面向对象零 (包装代码框移动)
        def code_move(i, *method):
            # 调用方法举例: code_move(1, 0, FadeIn(vec_pos_all))
            self.play(
                *method,
                move_frame.set_width,
                ignore_space_len(codes_heapSort[i], i),
                move_frame.move_to,
                codes_heapSort[i],
                move_frame.align_to,
                codes_heapSort[i],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {
                    "height": 0.28,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()

        # 面向对象一 (变量框元素值更新)
        def renew_variable(string, num):
            # 调用方法举例: self.play(renew_variable('rm', 1))
            if string == 'i':
                i_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(1).next_to(variable_i,
                                                            RIGHT,
                                                            buff=0.3))
                return Transform(all_num[0], i_num)
            elif string == 'R0':
                R0_num = (Text(str(num), font="思源宋体 Heavy",
                               color=BLACK).scale(1).next_to(variable_R0,
                                                             RIGHT,
                                                             buff=0.3))
                return Transform(all_num[1], R0_num)
            elif string == 'Ri':
                Ri_num = (Text(str(num), font="思源宋体 Heavy",
                               color=BLACK).scale(1).next_to(variable_Ri,
                                                             RIGHT,
                                                             buff=0.3))
                return Transform(all_num[2], Ri_num)

        # 面向对象二 (交换 element_all 中的元素)
        def change_cir_group(num1, num2):
            # 调用方法举例: change_group(1, 2)
            global element_all
            element_tmp_all = VGroup()
            for i in range(11):
                if i == num1:
                    element_tmp_all.add(element_all[num2])
                elif i == num2:
                    element_tmp_all.add(element_all[num1])
                else:
                    element_tmp_all.add(element_all[i])
            element_all = element_tmp_all

        # 面向对象三 (交换 rectangle_element_all 中的元素)
        def change_rec_group(num1, num2):
            # 调用方法举例: change_group(1, 2)
            global rectangle_element_all
            rectangle_element_tmp_all = VGroup()
            for i in range(11):
                if i == num1:
                    rectangle_element_tmp_all.add(rectangle_element_all[num2])
                elif i == num2:
                    rectangle_element_tmp_all.add(rectangle_element_all[num1])
                else:
                    rectangle_element_tmp_all.add(rectangle_element_all[i])
            rectangle_element_all = rectangle_element_tmp_all

        # 面向对象四 (一键完成)
        def swap_group(num1, num2, R0, Ri):
            # 调用方法举例: swap_group(0, 10, 3, 10)
            global element_all
            global rectangle_element_all
            self.play(
                Swap(element_all[num1], element_all[num2]),
                Swap(rectangle_element_all[num1], rectangle_element_all[num2]),
                renew_variable("R0", R0), renew_variable("Ri", Ri))
            change_cir_group(num1, num2)
            change_rec_group(num1, num2)
            self.wait()

        # heapSort
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()
        code_move(2)
        move_circle_new_position = move_circle.copy()
        move_circle_new_position.move_to(base_all[4])
        self.play(FadeIn(all_num[0]), FadeIn(move_circle_new_position),
                  FadeOut(move_circle))
        move_circle = move_circle_new_position
        self.wait()
        code_move(3)
        element_tmp1 = element_all[10].copy().move_to(element_all[4])
        element_tmp2 = element_all[4].copy().move_to(element_all[10])
        rectangle_element_tmp1 = rectangle_element_all[10].copy().move_to(
            rectangle_element_all[4])
        rectangle_element_tmp2 = rectangle_element_all[4].copy().move_to(
            rectangle_element_all[10])
        self.play(Transform(element_all[4], element_tmp1),
                  Transform(element_all[10], element_tmp2),
                  Transform(rectangle_element_all[4], rectangle_element_tmp1),
                  Transform(rectangle_element_all[10], rectangle_element_tmp2))
        self.wait()
        code_move(2)
        move_circle_new_position = move_circle.copy()
        move_circle_new_position.move_to(base_all[3])
        self.play(renew_variable("i", 3), FadeIn(move_circle_new_position),
                  FadeOut(move_circle))
        move_circle = move_circle_new_position
        self.wait()
        code_move(3)
        element_tmp1 = element_all[8].copy().move_to(element_all[3])
        element_tmp2 = element_all[3].copy().move_to(element_all[8])
        rectangle_element_tmp1 = rectangle_element_all[8].copy().move_to(
            rectangle_element_all[3])
        rectangle_element_tmp2 = rectangle_element_all[3].copy().move_to(
            rectangle_element_all[8])
        self.play(Transform(element_all[3], element_tmp1),
                  Transform(element_all[8], element_tmp2),
                  Transform(rectangle_element_all[3], rectangle_element_tmp1),
                  Transform(rectangle_element_all[8], rectangle_element_tmp2))
        self.wait()
        code_move(2)
        move_circle_new_position = move_circle.copy()
        move_circle_new_position.move_to(base_all[2])
        self.play(renew_variable("i", 2), FadeIn(move_circle_new_position),
                  FadeOut(move_circle))
        move_circle = move_circle_new_position
        self.wait()
        code_move(3)
        element_tmp1 = element_all[6].copy().move_to(element_all[2])
        element_tmp2 = element_all[2].copy().move_to(element_all[6])
        rectangle_element_tmp1 = rectangle_element_all[6].copy().move_to(
            rectangle_element_all[2])
        rectangle_element_tmp2 = rectangle_element_all[2].copy().move_to(
            rectangle_element_all[6])
        self.play(Transform(element_all[2], element_tmp1),
                  Transform(element_all[6], element_tmp2),
                  Transform(rectangle_element_all[2], rectangle_element_tmp1),
                  Transform(rectangle_element_all[6], rectangle_element_tmp2))
        self.wait()
        code_move(2)
        move_circle_new_position = move_circle.copy()
        move_circle_new_position.move_to(base_all[1])
        self.play(renew_variable("i", 1), FadeIn(move_circle_new_position),
                  FadeOut(move_circle))
        move_circle = move_circle_new_position
        self.wait()
        code_move(3)
        element_tmp1 = element_all[3].copy().move_to(element_all[1])
        element_tmp2 = element_all[8].copy().move_to(element_all[3])
        element_tmp3 = element_all[1].copy().move_to(element_all[8])
        rectangle_element_tmp1 = rectangle_element_all[3].copy().move_to(
            rectangle_element_all[1])
        rectangle_element_tmp2 = rectangle_element_all[8].copy().move_to(
            rectangle_element_all[3])
        rectangle_element_tmp3 = rectangle_element_all[1].copy().move_to(
            rectangle_element_all[8])
        self.play(Transform(element_all[1], element_tmp1),
                  Transform(element_all[3], element_tmp2),
                  Transform(element_all[8], element_tmp3),
                  Transform(rectangle_element_all[1], rectangle_element_tmp1),
                  Transform(rectangle_element_all[3], rectangle_element_tmp2),
                  Transform(rectangle_element_all[8], rectangle_element_tmp3))
        self.wait()
        code_move(2)
        move_circle_new_position = move_circle.copy()
        move_circle_new_position.move_to(base_all[0])
        self.play(renew_variable("i", 0), FadeIn(move_circle_new_position),
                  FadeOut(move_circle))
        move_circle = move_circle_new_position
        self.wait()
        code_move(3)
        element_tmp1 = element_all[0].copy().move_to(element_all[6])
        element_tmp2 = element_all[6].copy().move_to(element_all[2])
        element_tmp3 = element_all[2].copy().move_to(element_all[0])
        rectangle_element_tmp1 = rectangle_element_all[0].copy().move_to(
            rectangle_element_all[6])
        rectangle_element_tmp2 = rectangle_element_all[6].copy().move_to(
            rectangle_element_all[2])
        rectangle_element_tmp3 = rectangle_element_all[2].copy().move_to(
            rectangle_element_all[0])
        self.play(Transform(element_all[6], element_tmp1),
                  Transform(element_all[2], element_tmp2),
                  Transform(element_all[0], element_tmp3),
                  Transform(rectangle_element_all[6], rectangle_element_tmp1),
                  Transform(rectangle_element_all[2], rectangle_element_tmp2),
                  Transform(rectangle_element_all[0], rectangle_element_tmp3))
        self.wait()
        code_move(2)
        self.play(renew_variable("i", -1), FadeOut(move_circle))
        self.wait()
        code_move(4)
        move_circle_new_position = move_circle2.copy()
        move_circle_new_position.move_to(base_all[10])
        self.play(renew_variable("i", 10), FadeIn(move_circle_new_position),
                  FadeOut(move_circle2), FadeIn(all_num[1]),
                  FadeIn(all_num[2]))
        self.wait()
        move_circle2 = move_circle_new_position
        code_move(6)
        swap_group(0, 10, 3, 10)
        code_move(7)
        element_tmp1 = element_all[0].copy().move_to(element_all[6])
        element_tmp2 = element_all[2].copy().move_to(element_all[0])
        element_tmp3 = element_all[6].copy().move_to(element_all[2])
        rectangle_element_tmp1 = rectangle_element_all[0].copy().move_to(
            rectangle_element_all[6])
        rectangle_element_tmp2 = rectangle_element_all[2].copy().move_to(
            rectangle_element_all[0])
        rectangle_element_tmp3 = rectangle_element_all[6].copy().move_to(
            rectangle_element_all[2])
        self.play(Transform(element_all[6], element_tmp1),
                  Transform(element_all[0], element_tmp2),
                  Transform(element_all[2], element_tmp3),
                  Transform(rectangle_element_all[6], rectangle_element_tmp1),
                  Transform(rectangle_element_all[0], rectangle_element_tmp2),
                  Transform(rectangle_element_all[2], rectangle_element_tmp3),
                  renew_variable("R0", 9))
        self.wait()
        rectangle_blue = rectangle_all[0].copy()
        rectangle_blue.set_opacity(0.5).set_color(BLUE).set_height(
            0.5).set_width(0.5).move_to(rectangle_all[10])
        self.play(FadeIn(rectangle_blue))
        self.wait()
        # 9
        code_move(4)
        move_circle_new_position = move_circle2.copy()
        move_circle_new_position.move_to(base_all[9])
        self.play(renew_variable("i", 9), FadeIn(move_circle_new_position),
                  FadeOut(move_circle2), renew_variable("Ri", 4))
        self.wait()
        move_circle2 = move_circle_new_position
        code_move(6)
        swap_group(0, 9, 4, 9)
        code_move(7)
        element_tmp1 = element_all[0].copy().move_to(element_all[2])
        element_tmp2 = element_all[2].copy().move_to(element_all[0])
        rectangle_element_tmp1 = rectangle_element_all[0].copy().move_to(
            rectangle_element_all[2])
        rectangle_element_tmp2 = rectangle_element_all[2].copy().move_to(
            rectangle_element_all[0])
        self.play(Transform(element_all[2], element_tmp1),
                  Transform(element_all[0], element_tmp2),
                  Transform(rectangle_element_all[2], rectangle_element_tmp1),
                  Transform(rectangle_element_all[0], rectangle_element_tmp2),
                  renew_variable("R0", 8))
        self.wait()
        rectangle_blue = rectangle_all[0].copy()
        rectangle_blue.set_opacity(0.5).set_color(BLUE).set_height(
            0.5).set_width(0.5).move_to(rectangle_all[9])
        self.play(FadeIn(rectangle_blue))
        self.wait()
        # 8
        code_move(4)
        move_circle_new_position = move_circle2.copy()
        move_circle_new_position.move_to(base_all[8])
        self.play(renew_variable("i", 8), FadeIn(move_circle_new_position),
                  FadeOut(move_circle2), renew_variable("Ri", 1))
        self.wait()
        move_circle2 = move_circle_new_position
        code_move(6)
        swap_group(0, 8, 1, 8)
        code_move(7)
        element_tmp1 = element_all[1].copy().move_to(element_all[0])
        element_tmp2 = element_all[3].copy().move_to(element_all[1])
        element_tmp3 = element_all[7].copy().move_to(element_all[3])
        element_tmp4 = element_all[0].copy().move_to(element_all[7])
        rectangle_element_tmp1 = rectangle_element_all[1].copy().move_to(
            rectangle_element_all[0])
        rectangle_element_tmp2 = rectangle_element_all[3].copy().move_to(
            rectangle_element_all[1])
        rectangle_element_tmp3 = rectangle_element_all[7].copy().move_to(
            rectangle_element_all[3])
        rectangle_element_tmp4 = rectangle_element_all[0].copy().move_to(
            rectangle_element_all[7])
        self.play(Transform(element_all[0], element_tmp1),
                  Transform(element_all[1], element_tmp2),
                  Transform(element_all[3], element_tmp3),
                  Transform(element_all[7], element_tmp4),
                  Transform(rectangle_element_all[0], rectangle_element_tmp1),
                  Transform(rectangle_element_all[1], rectangle_element_tmp2),
                  Transform(rectangle_element_all[3], rectangle_element_tmp3),
                  Transform(rectangle_element_all[7], rectangle_element_tmp4),
                  renew_variable("R0", 7))
        self.wait()
        rectangle_blue = rectangle_all[0].copy()
        rectangle_blue.set_opacity(0.5).set_color(BLUE).set_height(
            0.5).set_width(0.5).move_to(rectangle_all[8])
        self.play(FadeIn(rectangle_blue))
        self.wait()
        # 7
        code_move(4)
        move_circle_new_position = move_circle2.copy()
        move_circle_new_position.move_to(base_all[7])
        self.play(renew_variable("i", 7), FadeIn(move_circle_new_position),
                  FadeOut(move_circle2), renew_variable("Ri", 1))
        self.wait()
        move_circle2 = move_circle_new_position
        code_move(6)
        swap_group(0, 7, 1, 7)
        code_move(7)
        element_tmp1 = element_all[1].copy().move_to(element_all[0])
        element_tmp2 = element_all[4].copy().move_to(element_all[1])
        element_tmp3 = element_all[0].copy().move_to(element_all[4])
        rectangle_element_tmp1 = rectangle_element_all[1].copy().move_to(
            rectangle_element_all[0])
        rectangle_element_tmp2 = rectangle_element_all[4].copy().move_to(
            rectangle_element_all[1])
        rectangle_element_tmp3 = rectangle_element_all[0].copy().move_to(
            rectangle_element_all[4])
        self.play(Transform(element_all[0], element_tmp1),
                  Transform(element_all[1], element_tmp2),
                  Transform(element_all[4], element_tmp3),
                  Transform(rectangle_element_all[0], rectangle_element_tmp1),
                  Transform(rectangle_element_all[1], rectangle_element_tmp2),
                  Transform(rectangle_element_all[4], rectangle_element_tmp3),
                  renew_variable("R0", 6))
        self.wait()
        rectangle_blue = rectangle_all[0].copy()
        rectangle_blue.set_opacity(0.5).set_color(BLUE).set_height(
            0.5).set_width(0.5).move_to(rectangle_all[7])
        self.play(FadeIn(rectangle_blue))
        self.wait()
        # 6
        code_move(4)
        move_circle_new_position = move_circle2.copy()
        move_circle_new_position.move_to(base_all[6])
        self.play(renew_variable("i", 6), FadeIn(move_circle_new_position),
                  FadeOut(move_circle2), renew_variable("Ri", 3))
        self.wait()
        move_circle2 = move_circle_new_position
        code_move(6)
        swap_group(0, 6, 3, 6)
        code_move(7)
        element_tmp1 = element_all[1].copy().move_to(element_all[0])
        element_tmp2 = element_all[0].copy().move_to(element_all[1])
        rectangle_element_tmp1 = rectangle_element_all[1].copy().move_to(
            rectangle_element_all[0])
        rectangle_element_tmp2 = rectangle_element_all[0].copy().move_to(
            rectangle_element_all[1])
        self.play(Transform(element_all[0], element_tmp1),
                  Transform(element_all[1], element_tmp2),
                  Transform(rectangle_element_all[0], rectangle_element_tmp1),
                  Transform(rectangle_element_all[1], rectangle_element_tmp2),
                  renew_variable("R0", 5))
        self.wait()
        rectangle_blue = rectangle_all[0].copy()
        rectangle_blue.set_opacity(0.5).set_color(BLUE).set_height(
            0.5).set_width(0.5).move_to(rectangle_all[6])
        self.play(FadeIn(rectangle_blue))
        self.wait()
        # 5
        code_move(4)
        move_circle_new_position = move_circle2.copy()
        move_circle_new_position.move_to(base_all[5])
        self.play(renew_variable("i", 5), FadeIn(move_circle_new_position),
                  FadeOut(move_circle2), renew_variable("Ri", 0))
        self.wait()
        move_circle2 = move_circle_new_position
        code_move(6)
        swap_group(0, 5, 0, 5)
        code_move(7)
        element_tmp1 = element_all[2].copy().move_to(element_all[0])
        element_tmp2 = element_all[0].copy().move_to(element_all[2])
        rectangle_element_tmp1 = rectangle_element_all[2].copy().move_to(
            rectangle_element_all[0])
        rectangle_element_tmp2 = rectangle_element_all[0].copy().move_to(
            rectangle_element_all[2])
        self.play(Transform(element_all[0], element_tmp1),
                  Transform(element_all[2], element_tmp2),
                  Transform(rectangle_element_all[0], rectangle_element_tmp1),
                  Transform(rectangle_element_all[2], rectangle_element_tmp2),
                  renew_variable("R0", 4))
        self.wait()
        rectangle_blue = rectangle_all[0].copy()
        rectangle_blue.set_opacity(0.5).set_color(BLUE).set_height(
            0.5).set_width(0.5).move_to(rectangle_all[5])
        self.play(FadeIn(rectangle_blue))
        self.wait()
        # 4
        code_move(4)
        move_circle_new_position = move_circle2.copy()
        move_circle_new_position.move_to(base_all[4])
        self.play(renew_variable("i", 4), FadeIn(move_circle_new_position),
                  FadeOut(move_circle2), renew_variable("Ri", 1))
        self.wait()
        move_circle2 = move_circle_new_position
        code_move(6)
        swap_group(0, 4, 1, 4)
        code_move(7)
        element_tmp1 = element_all[1].copy().move_to(element_all[0])
        element_tmp2 = element_all[3].copy().move_to(element_all[1])
        element_tmp3 = element_all[0].copy().move_to(element_all[3])
        rectangle_element_tmp1 = rectangle_element_all[1].copy().move_to(
            rectangle_element_all[0])
        rectangle_element_tmp2 = rectangle_element_all[3].copy().move_to(
            rectangle_element_all[1])
        rectangle_element_tmp3 = rectangle_element_all[0].copy().move_to(
            rectangle_element_all[3])
        self.play(Transform(element_all[0], element_tmp1),
                  Transform(element_all[1], element_tmp2),
                  Transform(element_all[3], element_tmp3),
                  Transform(rectangle_element_all[0], rectangle_element_tmp1),
                  Transform(rectangle_element_all[1], rectangle_element_tmp2),
                  Transform(rectangle_element_all[3], rectangle_element_tmp3),
                  renew_variable("R0", 3))
        self.wait()
        rectangle_blue = rectangle_all[0].copy()
        rectangle_blue.set_opacity(0.5).set_color(BLUE).set_height(
            0.5).set_width(0.5).move_to(rectangle_all[4])
        self.play(FadeIn(rectangle_blue))
        self.wait()
        # 3
        code_move(4)
        move_circle_new_position = move_circle2.copy()
        move_circle_new_position.move_to(base_all[3])
        self.play(renew_variable("i", 3), FadeIn(move_circle_new_position),
                  FadeOut(move_circle2), renew_variable("Ri", 1))
        self.wait()
        move_circle2 = move_circle_new_position
        code_move(6)
        swap_group(0, 3, 1, 3)
        code_move(7)
        element_tmp1 = element_all[1].copy().move_to(element_all[0])
        element_tmp2 = element_all[0].copy().move_to(element_all[1])
        rectangle_element_tmp1 = rectangle_element_all[1].copy().move_to(
            rectangle_element_all[0])
        rectangle_element_tmp2 = rectangle_element_all[0].copy().move_to(
            rectangle_element_all[1])
        self.play(Transform(element_all[0], element_tmp1),
                  Transform(element_all[1], element_tmp2),
                  Transform(rectangle_element_all[0], rectangle_element_tmp1),
                  Transform(rectangle_element_all[1], rectangle_element_tmp2),
                  renew_variable("R0", 2))
        self.wait()
        rectangle_blue = rectangle_all[0].copy()
        rectangle_blue.set_opacity(0.5).set_color(BLUE).set_height(
            0.5).set_width(0.5).move_to(rectangle_all[3])
        self.play(FadeIn(rectangle_blue))
        self.wait()
        # 2
        code_move(4)
        move_circle_new_position = move_circle2.copy()
        move_circle_new_position.move_to(base_all[2])
        self.play(renew_variable("i", 2), FadeIn(move_circle_new_position),
                  FadeOut(move_circle2), renew_variable("Ri", 0))
        self.wait()
        move_circle2 = move_circle_new_position
        code_move(6)
        swap_group(0, 2, 0, 2)
        code_move(7)
        element_tmp1 = element_all[1].copy().move_to(element_all[0])
        element_tmp2 = element_all[0].copy().move_to(element_all[1])
        rectangle_element_tmp1 = rectangle_element_all[1].copy().move_to(
            rectangle_element_all[0])
        rectangle_element_tmp2 = rectangle_element_all[0].copy().move_to(
            rectangle_element_all[1])
        self.play(Transform(element_all[0], element_tmp1),
                  Transform(element_all[1], element_tmp2),
                  Transform(rectangle_element_all[0], rectangle_element_tmp1),
                  Transform(rectangle_element_all[1], rectangle_element_tmp2),
                  renew_variable("R0", 1))
        self.wait()
        rectangle_blue = rectangle_all[0].copy()
        rectangle_blue.set_opacity(0.5).set_color(BLUE).set_height(
            0.5).set_width(0.5).move_to(rectangle_all[2])
        self.play(FadeIn(rectangle_blue))
        self.wait()
        # 1
        code_move(4)
        move_circle_new_position = move_circle2.copy()
        move_circle_new_position.move_to(base_all[1])
        self.play(renew_variable("i", 1), FadeIn(move_circle_new_position),
                  FadeOut(move_circle2), renew_variable("Ri", 0))
        self.wait()
        move_circle2 = move_circle_new_position
        code_move(6)
        swap_group(0, 1, 0, 1)
        code_move(7)
        rectangle_blue = rectangle_all[0].copy()
        rectangle_blue.set_opacity(0.5).set_color(BLUE).set_height(
            0.5).set_width(0.5).move_to(rectangle_all[1])
        self.play(FadeIn(rectangle_blue))
        self.wait()
        # 0
        code_move(4)
        move_circle_new_position = move_circle2.copy()
        move_circle_new_position.move_to(base_all[0])
        self.play(renew_variable("i", 0), FadeIn(move_circle_new_position),
                  FadeOut(move_circle2), renew_variable("Ri", 0))
        self.wait()
        move_circle2 = move_circle_new_position
        rectangle_blue = rectangle_all[0].copy()
        rectangle_blue.set_opacity(0.5).set_color(BLUE).set_height(
            0.5).set_width(0.5).move_to(rectangle_all[0])
        self.play(FadeIn(rectangle_blue), FadeOut(move_circle2),
                  FadeOut(arrow), FadeOut(move_frame))
        self.wait(1.5)


class mergeSort_merge(Scene_White):
    def construct(self):
        # global
        # Frame 整体框架
        # height: 8  *  width: 14.2
        frame_code = Rectangle(
            color=BLUE,
            stroke_opacity=0,
            height=3.7,
            width=7.1 + 1,
        ).to_corner(DL, buff=0)
        frame_variable = Rectangle(
            color=RED,
            stroke_opacity=0,
            height=3.7,
            width=7.1 - 1,
        ).to_corner(DR, buff=0)
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_color=WHITE,
            fill_opacity=1,
            height=4.3,
            width=14.2,
        ).to_corner(UP, buff=0)
        self.add(frame_code, frame_variable, frame_animation)

        # --------------- 动画框架 ---------------
        # 标题
        title = (Text("归并排序       merge(R, tmp, 0, 4, 7)",
                      font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).to_corner(UP).shift(UP * 0.25))
        self.add(title)

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
        background.set_height(3.3, stretch=True).set_width(7.3, stretch=True)
        background.move_to(frame_code).shift(DOWN * 0)

        # 代码 + 移动框
        class codeline_merge(Text):
            CONFIG = {
                "size": 0.4,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        def ignore_space_len(code, num):
            origin_len = len(code)
            begin = origin_len - 1
            record = 0
            temp_codes = merge_codes
            for index in range(begin, 0, -1):
                if temp_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.115
                elif temp_codes[num][index] == " " and record == 0:
                    record = 1
                elif temp_codes[num][index] != " ":
                    record = 0
            return origin_len * 0.115

        codes_merge = (VGroup(
            *[codeline_merge(code) for code in merge_codes]).arrange(
                DOWN, aligned_edge=LEFT,
                buff=0.05).next_to(background.get_top(), DOWN,
                                   buff=0).shift(RIGHT * 0.1 + DOWN * 0.05))

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=2.5,
            stroke_color=BLUE,
            corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1,
                         fill_color=RED).rotate(90 * DEGREES, axis=IN)
        arrow.scale(0.09)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.08))

        # 一键添加代码背景 and 代码
        self.add(background, codes_merge)
        # self.add(arrow, move_frame)
        move_frame.set_width(
            ignore_space_len(codes_merge[1], 1),
            stretch=True).set_height(0.24, stretch=True).move_to(
                codes_merge[1]).align_to(codes_merge[1],
                                         RIGHT).shift(RIGHT * 0.05)

        # 正方块序列
        rectangle_all = VGroup()
        for i in range(8):
            rectangle_base = MySquare(color=BLACK,
                                      side_length=0.55,
                                      stroke_opacity=1)
            rectangle_all.add(rectangle_base)
        for i in range(1, 8):
            rectangle_all[i].next_to(rectangle_all[i - 1], RIGHT, buff=0)
        rectangle_all_R = rectangle_all.copy()
        rectangle_all_tmp = rectangle_all.copy()
        rectangle_all_R.move_to(frame_animation).align_to(
            frame_animation, DOWN).shift(UP * 1.75 + LEFT * 3)
        rectangle_all_tmp.move_to(frame_animation).align_to(
            frame_animation, DOWN).shift(UP * 1.75 + RIGHT * 4)
        self.add(rectangle_all_R, rectangle_all_tmp)

        # 序列的序号
        rectangle_num_all_R = VGroup()
        rectangle_num_all_tmp = VGroup()
        for i in range(8):
            rectangle_num_base = Text(str(i), font="思源宋体 Heavy",
                                      color=BLACK).scale(0.35)
            rectangle_num_base_R = rectangle_num_base.copy().next_to(
                rectangle_all_R[i], DOWN, buff=0.1)
            rectangle_num_all_R.add(rectangle_num_base_R)
            rectangle_num_base_tmp = rectangle_num_base.copy().next_to(
                rectangle_all_tmp[i], DOWN, buff=0.1)
            rectangle_num_all_tmp.add(rectangle_num_base_tmp)
        self.add(rectangle_num_all_R, rectangle_num_all_tmp)

        # 序列的元素
        rectangle_list_R = [2, 4, 5, 6, 0, 1, 3, 7]
        rectangle_list_tmp = [0, 1, 2, 3, 4, 5, 6, 7]
        rectangle_element_all_R = VGroup()
        rectangle_element_all_tmp = VGroup()
        for i in range(8):
            rectangle_element_tmp_R = Text(str(rectangle_list_R[i]),
                                           font="江西拙楷",
                                           color=BLACK).scale(0.6).move_to(
                                               rectangle_all_R[i])
            rectangle_element_all_R.add(rectangle_element_tmp_R)
            rectangle_element_tmp_tmp = Text(str(rectangle_list_tmp[i]),
                                             font="江西拙楷",
                                             color=BLACK).scale(0.6).move_to(
                                                 rectangle_all_tmp[i])
            rectangle_element_all_tmp.add(rectangle_element_tmp_tmp)
        self.add(rectangle_element_all_R)

        # R 指针
        vec_R = (Arrow(np.array([-1, 0, 0]),
                       np.array([1, 0, 0]),
                       color=BLACK,
                       buff=0.1,
                       fill_color=BLACK).scale(0.35))
        vec_R.next_to(rectangle_all_R, LEFT, buff=0.1)
        vec_R_variables = (Text("R", font="思源宋体 Heavy",
                                color=BLACK).scale(0.7))
        vec_R_variables.next_to(vec_R, LEFT, buff=0.15)
        self.add(vec_R, vec_R_variables)

        # tmp 指针
        vec_tmp = vec_R.copy()
        vec_tmp.next_to(rectangle_all_tmp, LEFT, buff=0.1)
        vec_tmp_variables = (Text("tmp", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.7))
        vec_tmp_variables.next_to(vec_tmp, LEFT, buff=0.15)
        self.add(vec_tmp, vec_tmp_variables)

        # i and j 箭头
        vec_j = (Arrow(np.array([0, -1, 0]),
                       np.array([0, 1, 0]),
                       color=BLACK,
                       buff=0.3,
                       fill_color=BLACK).scale(0.25))
        vec_i = vec_j.copy()
        vec_j.next_to(rectangle_all_R[4], DOWN, buff=0.35)
        vec_i.next_to(rectangle_all_R[0], DOWN, buff=0.35)
        vec_j_variables = (Text("j", font="思源宋体 Heavy",
                                color=BLACK).scale(0.55))
        vec_i_variables = (Text("i", font="思源宋体 Heavy",
                                color=BLACK).scale(0.55))
        vec_j_variables.add_updater(lambda a: a.next_to(vec_j, DOWN, buff=0.1))
        vec_i_variables.add_updater(lambda a: a.next_to(vec_i, DOWN, buff=0.1))
        vec_j_all = VGroup(vec_j, vec_j_variables)
        vec_i_all = VGroup(vec_i, vec_i_variables)
        # self.add(vec_j_all, vec_i_all)

        # k 箭头
        vec_k = vec_j.copy()
        vec_k.next_to(rectangle_all_tmp[0], DOWN, buff=0.35)
        vec_k_variables = (Text("k", font="思源宋体 Heavy",
                                color=BLACK).scale(0.55))
        vec_k_variables.add_updater(lambda a: a.next_to(vec_k, DOWN, buff=0.1))
        vec_k_all = VGroup(vec_k, vec_k_variables)
        # self.add(vec_k_all)

        # 变量框
        t2c = {
            "i": "#2932e1",
            "j": "#801dae",
            "k": "#801dae",
            "low": BLUE,
            "mid": RED,
            "high": PURPLE,
            "R[i]": GOLD,
            "R[j]": "#01cd74",
            "tmp[k-1]": "#da1884",
            "tmp[k]": "#da1884",
        }
        variable_rectangle = Rectangle(
            color="#003472", height=3.3, width=5.5,
            stroke_opacity=1).move_to(frame_variable)
        variable_low = (Text("low:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(0.8).next_to(
                                 variable_rectangle.get_top(), DOWN,
                                 buff=0.3).align_to(variable_rectangle,
                                                    LEFT).shift(RIGHT * 0.26))
        variable_mid = (Text("mid:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(0.8).next_to(variable_low,
                                                         DOWN,
                                                         buff=0.8).align_to(
                                                             variable_low,
                                                             LEFT))
        variable_high = (Text("high:", font="思源宋体 Heavy", color=BLACK,
                              t2c=t2c).scale(0.8).next_to(variable_mid,
                                                          DOWN,
                                                          buff=0.8).align_to(
                                                              variable_mid,
                                                              LEFT))
        variable_i = (Text("i:", font="思源宋体 Heavy", color=BLACK,
                           t2c=t2c).scale(0.8).next_to(
                               variable_rectangle.get_top(), DOWN,
                               buff=0.3).align_to(variable_rectangle,
                                                  LEFT).shift(RIGHT * 2.15))
        variable_j = (Text("j:", font="思源宋体 Heavy", color=BLACK,
                           t2c=t2c).scale(0.8).next_to(variable_i,
                                                       DOWN,
                                                       buff=0.75).align_to(
                                                           variable_i, LEFT))
        variable_k = (Text("k:", font="思源宋体 Heavy", color=BLACK,
                           t2c=t2c).scale(0.8).next_to(variable_i,
                                                       DOWN,
                                                       buff=0.8).align_to(
                                                           variable_i, LEFT))
        variable_Ri = (Text("R[i]:", font="思源宋体 Heavy", color=BLACK,
                            t2c=t2c).scale(0.8).next_to(
                                variable_rectangle.get_top(), DOWN,
                                buff=0.3).align_to(variable_rectangle,
                                                   LEFT).shift(RIGHT * 3.3))
        variable_Rj = (Text("R[j]:", font="思源宋体 Heavy", color=BLACK,
                            t2c=t2c).scale(0.8).next_to(variable_Ri,
                                                        DOWN,
                                                        buff=0.7).align_to(
                                                            variable_Ri, LEFT))
        variable_tk = (Text("tmp[k-1]:",
                            font="思源宋体 Heavy",
                            color=BLACK,
                            t2c=t2c).scale(0.8).next_to(variable_Rj,
                                                        DOWN,
                                                        buff=0.7).shift(LEFT *
                                                                        0.5))
        variable_tk_new = (Text(
            "tmp[k]:", font="思源宋体 Heavy", color=BLACK,
            t2c=t2c).scale(0.8).move_to(variable_tk).align_to(
                variable_tk, LEFT))
        low_num = (Text(str(0), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_low,
                                                        RIGHT,
                                                        buff=0.3))
        mid_num = (Text(str(4), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        high_num = (Text(str(7), font="思源宋体 Heavy",
                         color=BLACK).scale(0.8).next_to(variable_high,
                                                         RIGHT,
                                                         buff=0.3))
        i_num = (Text(str(0), font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).next_to(variable_i,
                                                      RIGHT,
                                                      buff=0.3))
        j_num = (Text(str(4), font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).next_to(variable_j,
                                                      RIGHT,
                                                      buff=0.3))
        k_num = (Text(str(0), font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).next_to(variable_k,
                                                      RIGHT,
                                                      buff=0.3))
        Ri_num = (Text(str(2), font="思源宋体 Heavy",
                       color=BLACK).scale(0.8).next_to(variable_Ri,
                                                       RIGHT,
                                                       buff=0.3))
        Rj_num = (Text(str(0), font="思源宋体 Heavy",
                       color=BLACK).scale(0.8).next_to(variable_Rj,
                                                       RIGHT,
                                                       buff=0.3))
        tk_num = (Text(str(0), font="思源宋体 Heavy",
                       color=BLACK).scale(0.8).next_to(variable_tk,
                                                       RIGHT,
                                                       buff=0.3))
        tk_new_num = (Text(str(0), font="思源宋体 Heavy",
                           color=BLACK).scale(0.8).next_to(variable_tk_new,
                                                           RIGHT,
                                                           buff=0.3))
        all_num = VGroup(low_num, mid_num, high_num, i_num, j_num, Ri_num,
                         Rj_num, tk_num)
        self.add(variable_rectangle, variable_low, variable_mid, variable_high,
                 variable_i, variable_j, variable_Ri, variable_Rj, variable_tk)
        self.add(all_num[0], all_num[1], all_num[2])

        # 借用 OOP 的方法
        # 面向对象零 (包装代码框移动)
        def code_move(i, *method):
            # 调用方法举例: code_move(1, 0, FadeIn(vec_pos_all))
            self.play(
                *method,
                move_frame.set_width,
                ignore_space_len(codes_merge[i], i),
                move_frame.move_to,
                codes_merge[i],
                move_frame.align_to,
                codes_merge[i],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {
                    "height": 0.24,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()

        # 面向对象一 (变量框元素值更新)
        def renew_variable(string, num):
            # 调用方法举例: self.play(renew_variable('rm', 1))
            if string == 'i':
                i_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(0.8).next_to(variable_i,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[3], i_num)
            elif string == 'j':
                j_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(0.8).next_to(variable_j,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[4], j_num)
            elif string == 'k':
                k_num_tmp = (Text(str(num), font="思源宋体 Heavy",
                                  color=BLACK).scale(0.8).next_to(variable_k,
                                                                  RIGHT,
                                                                  buff=0.3))
                return Transform(k_num, k_num_tmp)
            elif string == 'Ri':
                Ri_num = (Text(str(num), font="思源宋体 Heavy",
                               color=BLACK).scale(0.8).next_to(variable_Ri,
                                                               RIGHT,
                                                               buff=0.3))
                return Transform(all_num[5], Ri_num)
            elif string == 'Rj':
                Rj_num = (Text(str(num), font="思源宋体 Heavy",
                               color=BLACK).scale(0.8).next_to(variable_Rj,
                                                               RIGHT,
                                                               buff=0.3))
                return Transform(all_num[6], Rj_num)
            elif string == 'tk':
                tk_num = (Text(str(num), font="思源宋体 Heavy",
                               color=BLACK).scale(0.8).next_to(variable_tk,
                                                               RIGHT,
                                                               buff=0.3))
                return Transform(all_num[7], tk_num)
            elif string == 'tkn':
                tk_new_num_tmp = (Text(str(num),
                                       font="思源宋体 Heavy",
                                       color=BLACK).scale(0.8).next_to(
                                           variable_tk_new, RIGHT, buff=0.3))
                return Transform(tk_new_num, tk_new_num_tmp)

        # merge
        self.wait()
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()
        self.play(FadeIn(all_num[3]), FadeIn(all_num[4]), FadeIn(all_num[5]),
                  FadeIn(all_num[6]), FadeIn(vec_j_all), FadeIn(vec_i_all),
                  FadeIn(vec_k_all))
        self.wait()
        # 0
        code_move(2)
        code_move(3)
        code_move(5)
        code_move(6)
        self.play(vec_j_all.shift, RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55,
                  FadeIn(rectangle_element_all_tmp[0]), renew_variable('j', 5),
                  renew_variable('Rj', 1), FadeIn(all_num[7]))
        self.wait()
        # 1
        code_move(2)
        code_move(3)
        code_move(5)
        code_move(6)
        self.play(vec_j_all.shift, RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55,
                  FadeIn(rectangle_element_all_tmp[1]), renew_variable('j', 6),
                  renew_variable('Rj', 3), renew_variable('tk', 1))
        self.wait()
        # 2
        code_move(2)
        code_move(3)
        code_move(4)
        self.play(vec_i_all.shift, RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55,
                  FadeIn(rectangle_element_all_tmp[2]), renew_variable('i', 1),
                  renew_variable('Ri', 4), renew_variable('tk', 2))
        self.wait()
        # 3
        code_move(2)
        code_move(3)
        code_move(5)
        code_move(6)
        self.play(vec_j_all.shift, RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55,
                  FadeIn(rectangle_element_all_tmp[3]), renew_variable('j', 7),
                  renew_variable('Rj', 7), renew_variable('tk', 3))
        self.wait()
        # 4
        code_move(2)
        code_move(3)
        code_move(4)
        self.play(vec_i_all.shift, RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55,
                  FadeIn(rectangle_element_all_tmp[4]), renew_variable('i', 2),
                  renew_variable('Ri', 5), renew_variable('tk', 4))
        self.wait()
        # 5
        code_move(2)
        code_move(3)
        code_move(4)
        self.play(vec_i_all.shift, RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55,
                  FadeIn(rectangle_element_all_tmp[5]), renew_variable('i', 3),
                  renew_variable('Ri', 6), renew_variable('tk', 5))
        self.wait()
        # 6
        code_move(2)
        code_move(3)
        code_move(4)
        self.play(vec_i_all.shift, RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55,
                  FadeIn(rectangle_element_all_tmp[6]), renew_variable('i', 4),
                  renew_variable('Ri', 0), renew_variable('tk', 6))
        self.wait()
        # 7
        code_move(2)
        code_move(7)
        code_move(9)
        code_move(10)
        rectangle_num_all_R_tmp = Text(
            str(8), font="思源宋体 Heavy", color=BLACK).scale(0.35).move_to(
                rectangle_num_all_R[7]).shift(RIGHT * 0.55)
        rectangle_num_all_tmp_tmp = Text(str(8),
                                         font="思源宋体 Heavy",
                                         color=BLACK).scale(0.35).move_to(
                                             rectangle_num_all_tmp[7]).shift(
                                                 RIGHT * 0.55)
        self.play(vec_j_all.shift, RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55,
                  FadeIn(rectangle_element_all_tmp[7]), renew_variable('j', 8),
                  FadeOut(all_num[6]), renew_variable('tk', 7),
                  FadeIn(rectangle_num_all_R_tmp),
                  FadeIn(rectangle_num_all_tmp_tmp))
        self.wait()
        code_move(9)
        variable_j_Rj = VGroup(variable_j, variable_Rj, all_num[4])
        variable_tk_all = VGroup(variable_tk, all_num[7])
        code_move(11, FadeOut(rectangle_num_all_R_tmp),
                  FadeOut(rectangle_num_all_tmp_tmp), FadeOut(vec_i_all),
                  FadeOut(vec_j_all), FadeOut(vec_k_all),
                  Transform(variable_j_Rj, variable_k),
                  Transform(variable_tk_all, variable_tk_new))
        vec_i_all.next_to(rectangle_all_R[0], DOWN, buff=0.35)
        vec_k_all.next_to(rectangle_all_tmp[0], DOWN, buff=0.35)
        self.play(FadeIn(vec_i_all), FadeIn(vec_k_all), FadeIn(k_num),
                  FadeIn(tk_new_num), renew_variable('i', 0),
                  renew_variable('Ri', 2))
        self.wait()
        # 移动
        code_move(12)
        change_tmp2R = rectangle_element_all_tmp[0].copy()
        self.play(change_tmp2R.move_to, rectangle_element_all_R[0],
                  FadeOut(rectangle_element_all_R[0]), renew_variable('Ri', 0))
        self.wait()
        # 变换变量
        self.play(renew_variable('i', 1), renew_variable('Ri', 4),
                  renew_variable('k', 1), renew_variable('tkn', 1),
                  vec_i_all.shift, RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55)
        self.wait()
        # 1
        code_move(11)
        # 移动
        code_move(12)
        change_tmp2R = rectangle_element_all_tmp[1].copy()
        self.play(change_tmp2R.move_to, rectangle_element_all_R[1],
                  FadeOut(rectangle_element_all_R[1]), renew_variable('Ri', 1))
        self.wait()
        # 变换变量
        self.play(renew_variable('i', 2), renew_variable('Ri', 5),
                  renew_variable('k', 2), renew_variable('tkn', 2),
                  vec_i_all.shift, RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55)
        self.wait()
        # 2
        code_move(11)
        # 移动
        code_move(12)
        change_tmp2R = rectangle_element_all_tmp[2].copy()
        self.play(change_tmp2R.move_to, rectangle_element_all_R[2],
                  FadeOut(rectangle_element_all_R[2]), renew_variable('Ri', 2))
        self.wait()
        # 变换变量
        self.play(renew_variable('i', 3), renew_variable('Ri', 6),
                  renew_variable('k', 3), renew_variable('tkn', 3),
                  vec_i_all.shift, RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55)
        self.wait()
        # 3
        code_move(11)
        # 移动
        code_move(12)
        change_tmp2R = rectangle_element_all_tmp[3].copy()
        self.play(change_tmp2R.move_to, rectangle_element_all_R[3],
                  FadeOut(rectangle_element_all_R[3]), renew_variable('Ri', 3))
        self.wait()
        # 变换变量
        self.play(renew_variable('i', 4), renew_variable('Ri', 0),
                  renew_variable('k', 4), renew_variable('tkn', 4),
                  vec_i_all.shift, RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55)
        self.wait()
        # 4
        code_move(11)
        # 移动
        code_move(12)
        change_tmp2R = rectangle_element_all_tmp[4].copy()
        self.play(change_tmp2R.move_to, rectangle_element_all_R[4],
                  FadeOut(rectangle_element_all_R[4]), renew_variable('Ri', 4))
        self.wait()
        # 变换变量
        self.play(renew_variable('i', 5), renew_variable('Ri', 1),
                  renew_variable('k', 5), renew_variable('tkn', 5),
                  vec_i_all.shift, RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55)
        self.wait()
        # 5
        code_move(11)
        # 移动
        code_move(12)
        change_tmp2R = rectangle_element_all_tmp[5].copy()
        self.play(change_tmp2R.move_to, rectangle_element_all_R[5],
                  FadeOut(rectangle_element_all_R[5]), renew_variable('Ri', 5))
        self.wait()
        # 变换变量
        self.play(renew_variable('i', 6), renew_variable('Ri', 3),
                  renew_variable('k', 6), renew_variable('tkn', 6),
                  vec_i_all.shift, RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55)
        self.wait()
        # 6
        code_move(11)
        # 移动
        code_move(12)
        change_tmp2R = rectangle_element_all_tmp[6].copy()
        self.play(change_tmp2R.move_to, rectangle_element_all_R[6],
                  FadeOut(rectangle_element_all_R[6]), renew_variable('Ri', 6))
        self.wait()
        # 变换变量
        self.play(renew_variable('i', 7), renew_variable('Ri', 7),
                  renew_variable('k', 7), renew_variable('tkn', 7),
                  vec_i_all.shift, RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55)
        self.wait()
        # 7
        code_move(11)
        # 移动
        code_move(12)
        change_tmp2R = rectangle_element_all_tmp[7].copy()
        self.play(change_tmp2R.move_to, rectangle_element_all_R[7],
                  FadeOut(rectangle_element_all_R[7]), renew_variable('Ri', 7))
        self.wait()
        # 变换变量
        self.play(renew_variable('i', 8), FadeOut(all_num[5]),
                  renew_variable('k', 8), FadeOut(tk_new_num),
                  FadeIn(rectangle_num_all_R_tmp),
                  FadeIn(rectangle_num_all_tmp_tmp), vec_i_all.shift,
                  RIGHT * 0.55, vec_k_all.shift, RIGHT * 0.55)
        self.wait()
        # 8
        code_move(11)
        self.play(FadeOut(rectangle_num_all_R_tmp),
                  FadeOut(rectangle_num_all_tmp_tmp), FadeOut(vec_i_all),
                  FadeOut(vec_k_all), FadeOut(move_frame), FadeOut(arrow))
        self.wait()


class mergeSort_mergeSort(Scene_White):
    def construct(self):
        # global
        # Frame 整体框架
        # height: 8  *  width: 14.2
        frame_code = Rectangle(
            color=BLUE,
            stroke_opacity=0,
            height=4,
            width=7.1,
        ).to_corner(UR, buff=0)
        frame_variable = Rectangle(
            color=RED,
            stroke_opacity=0,
            height=4,
            width=7.1,
        ).to_corner(DR, buff=0)
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_color=WHITE,
            fill_opacity=1,
            height=8,
            width=7.1,
        ).to_corner(LEFT, buff=0)
        self.add(frame_code, frame_variable, frame_animation)

        # --------------- 动画框架 ---------------
        # 标题
        title = (Text("归并排序       mergeSort(R, tmp, 0, 7)",
                      font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).to_corner(UP).shift(UP * 0.25))
        self.add(title)

        # 正方块序列
        rectangle_base = MySquare(color=BLACK,
                                  side_length=0.55,
                                  stroke_opacity=1)
        rectangle_8 = VGroup()
        rectangle_4 = VGroup()
        rectangle_2 = VGroup()
        for i in range(8):
            rectangle_8.add(rectangle_base.copy())
        for i in range(4):
            rectangle_4.add(rectangle_base.copy())
        for i in range(2):
            rectangle_2.add(rectangle_base.copy())
        for i in range(1, 8):
            rectangle_8[i].next_to(rectangle_8[i - 1], RIGHT, buff=0)
        for i in range(1, 4):
            rectangle_4[i].next_to(rectangle_4[i - 1], RIGHT, buff=0)
        rectangle_2[1].next_to(rectangle_2[0], RIGHT, buff=0)
        # 全部归并块
        rectangle_8_1 = rectangle_8.copy()
        rectangle_8_2 = rectangle_8.copy()
        rectangle_4_1 = rectangle_4.copy()
        rectangle_4_2 = rectangle_4.copy()
        rectangle_4_3 = rectangle_4.copy()
        rectangle_4_4 = rectangle_4.copy()
        rectangle_2_1 = rectangle_2.copy()
        rectangle_2_2 = rectangle_2.copy()
        rectangle_2_3 = rectangle_2.copy()
        rectangle_2_4 = rectangle_2.copy()
        rectangle_2_5 = rectangle_2.copy()
        rectangle_2_6 = rectangle_2.copy()
        rectangle_2_7 = rectangle_2.copy()
        rectangle_2_8 = rectangle_2.copy()
        rectangle_1_1 = rectangle_base.copy()
        rectangle_1_2 = rectangle_base.copy()
        rectangle_1_3 = rectangle_base.copy()
        rectangle_1_4 = rectangle_base.copy()
        rectangle_1_5 = rectangle_base.copy()
        rectangle_1_6 = rectangle_base.copy()
        rectangle_1_7 = rectangle_base.copy()
        rectangle_1_8 = rectangle_base.copy()
        rectangle_8_1.move_to(frame_animation).align_to(frame_animation,
                                                        UP).shift(DOWN * 1)
        self.add(rectangle_8_1)
        rectangle_4_1.move_to(rectangle_8_1).shift(DOWN * 1 + LEFT * 1.5)
        rectangle_4_2.move_to(rectangle_8_1).shift(DOWN * 1 + RIGHT * 1.5)
        # self.add(rectangle_4_1,rectangle_4_2)
        rectangle_2_1.move_to(rectangle_4_1).shift(DOWN * 1 + LEFT * 0.75)
        rectangle_2_2.move_to(rectangle_4_1).shift(DOWN * 1 + RIGHT * 0.75)
        rectangle_2_3.move_to(rectangle_4_2).shift(DOWN * 1 + LEFT * 0.75)
        rectangle_2_4.move_to(rectangle_4_2).shift(DOWN * 1 + RIGHT * 0.75)
        # self.add(rectangle_2_1,rectangle_2_2,rectangle_2_3,rectangle_2_4)
        rectangle_1_1.move_to(rectangle_2_1).shift(DOWN * 1 + LEFT * 0.37)
        rectangle_1_2.move_to(rectangle_2_1).shift(DOWN * 1 + RIGHT * 0.37)
        rectangle_1_3.move_to(rectangle_2_2).shift(DOWN * 1 + LEFT * 0.37)
        rectangle_1_4.move_to(rectangle_2_2).shift(DOWN * 1 + RIGHT * 0.37)
        rectangle_1_5.move_to(rectangle_2_3).shift(DOWN * 1 + LEFT * 0.37)
        rectangle_1_6.move_to(rectangle_2_3).shift(DOWN * 1 + RIGHT * 0.37)
        rectangle_1_7.move_to(rectangle_2_4).shift(DOWN * 1 + LEFT * 0.37)
        rectangle_1_8.move_to(rectangle_2_4).shift(DOWN * 1 + RIGHT * 0.37)
        # self.add(rectangle_1_1,rectangle_1_2,rectangle_1_3,rectangle_1_4,rectangle_1_5,rectangle_1_6,rectangle_1_7,rectangle_1_8)
        rectangle_2_5.move_to(rectangle_2_1).shift(DOWN * 1 * 2)
        rectangle_2_6.move_to(rectangle_2_2).shift(DOWN * 1 * 2)
        rectangle_2_7.move_to(rectangle_2_3).shift(DOWN * 1 * 2)
        rectangle_2_8.move_to(rectangle_2_4).shift(DOWN * 1 * 2)
        # self.add(rectangle_2_5,rectangle_2_6,rectangle_2_7,rectangle_2_8)
        rectangle_4_3.move_to(rectangle_4_1).shift(DOWN * 1 * 4)
        rectangle_4_4.move_to(rectangle_4_2).shift(DOWN * 1 * 4)
        # self.add(rectangle_4_3,rectangle_4_4)
        rectangle_8_2.move_to(rectangle_8_1).shift(DOWN * 1 * 6)
        # self.add(rectangle_8_2)

        # 序列下标
        rectangle_num_all = VGroup()
        for i in range(8):
            rectangle_num_base = Text(str(i), font="思源宋体 Heavy",
                                      color=BLACK).scale(0.35)
            rectangle_num_all.add(rectangle_num_base.copy())
        rectangle_num_1 = rectangle_num_all.copy()
        rectangle_num_2 = rectangle_num_all.copy()
        rectangle_num_3 = rectangle_num_all.copy()
        rectangle_num_4 = rectangle_num_all.copy()
        rectangle_num_5 = rectangle_num_all.copy()
        rectangle_num_6 = rectangle_num_all.copy()
        rectangle_num_7 = rectangle_num_all.copy()
        for i in range(8):
            rectangle_num_1[i].next_to(rectangle_8_1[i], UP, buff=0.1)
        self.add(rectangle_num_1)
        for i in range(4):
            rectangle_num_2[i].next_to(rectangle_4_1[i], UP, buff=0.1)
        for i in range(4):
            rectangle_num_2[i + 4].next_to(rectangle_4_2[i], UP, buff=0.1)
        # self.add(rectangle_num_2)
        for i in range(2):
            rectangle_num_3[i].next_to(rectangle_2_1[i], UP, buff=0.1)
        for i in range(2):
            rectangle_num_3[i + 2].next_to(rectangle_2_2[i], UP, buff=0.1)
        for i in range(2):
            rectangle_num_3[i + 4].next_to(rectangle_2_3[i], UP, buff=0.1)
        for i in range(2):
            rectangle_num_3[i + 6].next_to(rectangle_2_4[i], UP, buff=0.1)
        # self.add(rectangle_num_3)
        rectangle_num_4[0].next_to(rectangle_1_1, UP, buff=0.1)
        rectangle_num_4[1].next_to(rectangle_1_2, UP, buff=0.1)
        rectangle_num_4[2].next_to(rectangle_1_3, UP, buff=0.1)
        rectangle_num_4[3].next_to(rectangle_1_4, UP, buff=0.1)
        rectangle_num_4[4].next_to(rectangle_1_5, UP, buff=0.1)
        rectangle_num_4[5].next_to(rectangle_1_6, UP, buff=0.1)
        rectangle_num_4[6].next_to(rectangle_1_7, UP, buff=0.1)
        rectangle_num_4[7].next_to(rectangle_1_8, UP, buff=0.1)
        # self.add(rectangle_num_4)
        for i in range(2):
            rectangle_num_5[i].next_to(rectangle_2_5[i], UP, buff=0.1)
        for i in range(2):
            rectangle_num_5[i + 2].next_to(rectangle_2_6[i], UP, buff=0.1)
        for i in range(2):
            rectangle_num_5[i + 4].next_to(rectangle_2_7[i], UP, buff=0.1)
        for i in range(2):
            rectangle_num_5[i + 6].next_to(rectangle_2_8[i], UP, buff=0.1)
        # self.add(rectangle_num_5)
        for i in range(4):
            rectangle_num_6[i].next_to(rectangle_4_3[i], UP, buff=0.1)
        for i in range(4):
            rectangle_num_6[i + 4].next_to(rectangle_4_4[i], UP, buff=0.1)
        # self.add(rectangle_num_6)
        for i in range(8):
            rectangle_num_7[i].next_to(rectangle_8_2[i], UP, buff=0.1)
        # self.add(rectangle_num_7)

        # 序列的元素
        rectangle_list_1 = [4, 2, 6, 5, 1, 7, 0, 3]
        rectangle_list_2 = [4, 2, 6, 5, 1, 7, 0, 3]
        rectangle_list_3 = [4, 2, 6, 5, 1, 7, 0, 3]
        rectangle_list_4 = [4, 2, 6, 5, 1, 7, 0, 3]
        rectangle_list_5 = [2, 4, 5, 6, 1, 7, 0, 3]
        rectangle_list_6 = [2, 4, 5, 6, 0, 1, 3, 7]
        rectangle_list_7 = [0, 1, 2, 3, 4, 5, 6, 7]
        rectangle_element_1 = VGroup()
        rectangle_element_2 = VGroup()
        rectangle_element_3 = VGroup()
        rectangle_element_4 = VGroup()
        rectangle_element_5 = VGroup()
        rectangle_element_6 = VGroup()
        rectangle_element_7 = VGroup()
        for i in range(8):
            rectangle_element_tmp = Text(str(rectangle_list_1[i]),
                                         font="江西拙楷",
                                         color=BLACK).scale(0.6)
            rectangle_element_1.add(rectangle_element_tmp)
            rectangle_element_tmp = Text(str(rectangle_list_2[i]),
                                         font="江西拙楷",
                                         color=BLACK).scale(0.6)
            rectangle_element_2.add(rectangle_element_tmp)
            rectangle_element_tmp = Text(str(rectangle_list_3[i]),
                                         font="江西拙楷",
                                         color=BLACK).scale(0.6)
            rectangle_element_3.add(rectangle_element_tmp)
            rectangle_element_tmp = Text(str(rectangle_list_4[i]),
                                         font="江西拙楷",
                                         color=BLACK).scale(0.6)
            rectangle_element_4.add(rectangle_element_tmp)
            rectangle_element_tmp = Text(str(rectangle_list_5[i]),
                                         font="江西拙楷",
                                         color=BLACK).scale(0.6)
            rectangle_element_5.add(rectangle_element_tmp)
            rectangle_element_tmp = Text(str(rectangle_list_6[i]),
                                         font="江西拙楷",
                                         color=BLACK).scale(0.6)
            rectangle_element_6.add(rectangle_element_tmp)
            rectangle_element_tmp = Text(str(rectangle_list_7[i]),
                                         font="江西拙楷",
                                         color=BLACK).scale(0.6)
            rectangle_element_7.add(rectangle_element_tmp)
        for i in range(8):
            rectangle_element_1[i].move_to(rectangle_8_1[i])
        self.add(rectangle_element_1)
        for i in range(4):
            rectangle_element_2[i].move_to(rectangle_4_1[i])
        for i in range(4):
            rectangle_element_2[i + 4].move_to(rectangle_4_2[i])
        # self.add(rectangle_element_2)
        for i in range(2):
            rectangle_element_3[i].move_to(rectangle_2_1[i])
        for i in range(2):
            rectangle_element_3[i + 2].move_to(rectangle_2_2[i])
        for i in range(2):
            rectangle_element_3[i + 4].move_to(rectangle_2_3[i])
        for i in range(2):
            rectangle_element_3[i + 6].move_to(rectangle_2_4[i])
        # self.add(rectangle_element_3)
        rectangle_element_4[0].move_to(rectangle_1_1)
        rectangle_element_4[1].move_to(rectangle_1_2)
        rectangle_element_4[2].move_to(rectangle_1_3)
        rectangle_element_4[3].move_to(rectangle_1_4)
        rectangle_element_4[4].move_to(rectangle_1_5)
        rectangle_element_4[5].move_to(rectangle_1_6)
        rectangle_element_4[6].move_to(rectangle_1_7)
        rectangle_element_4[7].move_to(rectangle_1_8)
        # self.add(rectangle_element_4)
        for i in range(2):
            rectangle_element_5[i].move_to(rectangle_2_5[i])
        for i in range(2):
            rectangle_element_5[i + 2].move_to(rectangle_2_6[i])
        for i in range(2):
            rectangle_element_5[i + 4].move_to(rectangle_2_7[i])
        for i in range(2):
            rectangle_element_5[i + 6].move_to(rectangle_2_8[i])
        # self.add(rectangle_element_5)
        for i in range(4):
            rectangle_element_6[i].move_to(rectangle_4_3[i])
        for i in range(4):
            rectangle_element_6[i + 4].move_to(rectangle_4_4[i])
        # self.add(rectangle_element_6)
        for i in range(8):
            rectangle_element_7[i].move_to(rectangle_8_2[i])
        # self.add(rectangle_element_7)

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
        background.set_height(2.1, stretch=True).set_width(6.7, stretch=True)
        background.move_to(frame_code).shift(DOWN * 0.5)

        # 代码 + 移动框
        class codeline_mergeSort(Text):
            CONFIG = {
                "size": 0.4,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        def ignore_space_len(code, num):
            origin_len = len(code)
            begin = origin_len - 1
            record = 0
            temp_codes = mergeSort_codes
            for index in range(begin, 0, -1):
                if temp_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.115
                elif temp_codes[num][index] == " " and record == 0:
                    record = 1
                elif temp_codes[num][index] != " ":
                    record = 0
            return origin_len * 0.115

        codes_mergeSort = (VGroup(
            *[codeline_mergeSort(code) for code in mergeSort_codes]).arrange(
                DOWN, aligned_edge=LEFT,
                buff=0.05).next_to(background.get_top(), DOWN,
                                   buff=0).shift(RIGHT * 0.1 + DOWN * 0.1))

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=2.5,
            stroke_color=BLUE,
            corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1,
                         fill_color=RED).rotate(90 * DEGREES, axis=IN)
        arrow.scale(0.09)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.08))

        # 一键添加代码背景 and 代码
        self.add(background, codes_mergeSort)
        # self.add(arrow, move_frame)
        move_frame.set_width(
            ignore_space_len(codes_mergeSort[1], 1),
            stretch=True).set_height(0.24, stretch=True).move_to(
                codes_mergeSort[1]).align_to(codes_mergeSort[1],
                                             RIGHT).shift(RIGHT * 0.05)

        # 变量框
        t2c = {
            "low": BLUE,
            "mid": RED,
            "high": PURPLE,
        }
        variable_rectangle = Rectangle(
            color="#003472", height=1, width=6.7,
            stroke_opacity=1).move_to(frame_variable).shift(UP * 1)
        variable_low = (Text("low:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(0.8).next_to(
                                 variable_rectangle.get_top(), DOWN,
                                 buff=0.3).align_to(variable_rectangle,
                                                    LEFT).shift(RIGHT * 0.26))
        variable_mid = (Text("mid:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(0.8).next_to(variable_low,
                                                         RIGHT,
                                                         buff=1.4).align_to(
                                                             variable_low, UP))
        variable_high = (Text("high:", font="思源宋体 Heavy", color=BLACK,
                              t2c=t2c).scale(0.8).next_to(variable_mid,
                                                          RIGHT,
                                                          buff=1.4).align_to(
                                                              variable_mid,
                                                              UP))
        low_num = (Text(str(0), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_low,
                                                        RIGHT,
                                                        buff=0.3))
        mid_num = (Text(str(3), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        high_num = (Text(str(7), font="思源宋体 Heavy",
                         color=BLACK).scale(0.8).next_to(variable_high,
                                                         RIGHT,
                                                         buff=0.3))
        all_num = VGroup(low_num, high_num, mid_num)
        self.add(variable_rectangle, variable_low, variable_mid, variable_high)
        self.add(all_num[0], all_num[1])

        # 借用 OOP 的方法
        # 面向对象零 (包装代码框移动)
        def code_move(i, *method):
            # 调用方法举例: code_move(1, 0, FadeIn(vec_pos_all))
            self.play(
                *method,
                move_frame.set_width,
                ignore_space_len(codes_mergeSort[i], i),
                move_frame.move_to,
                codes_mergeSort[i],
                move_frame.align_to,
                codes_mergeSort[i],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {
                    "height": 0.24,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()

        # 面向对象一 (变量框元素值更新)
        def renew_variable(string, num):
            # 调用方法举例: self.play(renew_variable('rm', 1))
            if string == 'low':
                i_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(0.8).next_to(variable_low,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[0], i_num)
            if string == 'high':
                i_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(0.8).next_to(variable_high,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[1], i_num)
            if string == 'mid':
                i_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(0.8).next_to(variable_mid,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[2], i_num)

        # mergeSort
        self.wait()
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()
        code_move(3)
        self.play(FadeIn(all_num[2]))
        self.wait()
        code_move(4)
        rectangle_all_1 = VGroup(rectangle_4_1)
        for i in range(4):
            rectangle_all_1.add(rectangle_num_2[i])
            rectangle_all_1.add(rectangle_element_2[i])
        code_move(1, renew_variable('high', 3), FadeOut(all_num[2]),
                  FadeInFrom(rectangle_all_1, UP))
        code_move(3)
        num_mid = (Text(str(1), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        self.play(FadeIn(num_mid))
        self.wait()
        code_move(4)
        rectangle_all_2 = VGroup(rectangle_2_1)
        for i in range(2):
            rectangle_all_2.add(rectangle_num_3[i])
            rectangle_all_2.add(rectangle_element_3[i])
        code_move(1, renew_variable('high', 1), FadeOut(num_mid),
                  FadeInFrom(rectangle_all_2, UP))
        code_move(3)
        num_mid = (Text(str(0), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        self.play(FadeIn(num_mid))
        self.wait()
        code_move(4)
        rectangle_all_3 = VGroup(rectangle_1_1)
        for i in range(1):
            rectangle_all_3.add(rectangle_num_4[i])
            rectangle_all_3.add(rectangle_element_4[i])
        code_move(1, renew_variable('high', 0), FadeOut(num_mid),
                  FadeInFrom(rectangle_all_3, UP))
        code_move(2)
        num_mid = (Text(str(0), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        code_move(5, renew_variable('low', 0), renew_variable('high', 1),
                  FadeIn(num_mid))  # 变量全变
        rectangle_all_4 = VGroup(rectangle_1_2)
        for i in range(1, 2):
            rectangle_all_4.add(rectangle_num_4[i])
            rectangle_all_4.add(rectangle_element_4[i])
        code_move(1, renew_variable('low', 1), FadeOut(num_mid),
                  FadeInFrom(rectangle_all_4, UP))
        code_move(2)
        num_mid = (Text(str(0), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        code_move(6, renew_variable('low', 0), renew_variable('high', 1),
                  FadeIn(num_mid))
        rectangle_all_5 = VGroup(rectangle_2_5)
        for i in range(2):
            rectangle_all_5.add(rectangle_num_5[i])
            rectangle_all_5.add(rectangle_element_5[i])
        self.play(FadeInFrom(rectangle_all_5, UP))
        self.wait()
        num_mid2 = (Text(str(1), font="思源宋体 Heavy",
                         color=BLACK).scale(0.8).next_to(variable_mid,
                                                         RIGHT,
                                                         buff=0.3))
        code_move(5, renew_variable('low', 0), renew_variable('high', 3),
                  Transform(num_mid, num_mid2))
        rectangle_all_6 = VGroup(rectangle_2_2)
        for i in range(2, 4):
            rectangle_all_6.add(rectangle_num_3[i])
            rectangle_all_6.add(rectangle_element_3[i])
        code_move(1, renew_variable('low', 2), FadeInFrom(rectangle_all_6, UP),
                  FadeOut(num_mid))
        code_move(3)
        num_mid = (Text(str(2), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        self.play(FadeIn(num_mid))
        self.wait()
        code_move(4)
        rectangle_all_7 = VGroup(rectangle_1_3)
        for i in range(2, 3):
            rectangle_all_7.add(rectangle_num_4[i])
            rectangle_all_7.add(rectangle_element_4[i])
        code_move(1, renew_variable('high', 2),
                  FadeInFrom(rectangle_all_7, UP), FadeOut(num_mid))
        code_move(2)
        num_mid = (Text(str(2), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        code_move(5, renew_variable('high', 3), FadeIn(num_mid))
        rectangle_all_8 = VGroup(rectangle_1_4)
        for i in range(3, 4):
            rectangle_all_8.add(rectangle_num_4[i])
            rectangle_all_8.add(rectangle_element_4[i])
        code_move(1, renew_variable('low', 3), FadeOut(num_mid),
                  FadeInFrom(rectangle_all_8, UP))
        code_move(2)
        num_mid = (Text(str(2), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        code_move(6, renew_variable('low', 2), renew_variable('high', 3),
                  FadeIn(num_mid))
        rectangle_all_9 = VGroup(rectangle_2_6)
        for i in range(2, 4):
            rectangle_all_9.add(rectangle_num_5[i])
            rectangle_all_9.add(rectangle_element_5[i])
        self.play(FadeInFrom(rectangle_all_9, UP))
        self.wait()
        num_mid2 = (Text(str(1), font="思源宋体 Heavy",
                         color=BLACK).scale(0.8).next_to(variable_mid,
                                                         RIGHT,
                                                         buff=0.3))
        self.play(renew_variable('low', 0), renew_variable('high', 3),
                  Transform(num_mid, num_mid2))
        self.wait()
        rectangle_all_10 = VGroup(rectangle_4_3)
        for i in range(4):
            rectangle_all_10.add(rectangle_num_6[i])
            rectangle_all_10.add(rectangle_element_6[i])
        self.play(FadeInFrom(rectangle_all_10, UP))
        self.wait()
        num_mid2 = (Text(str(3), font="思源宋体 Heavy",
                         color=BLACK).scale(0.8).next_to(variable_mid,
                                                         RIGHT,
                                                         buff=0.3))
        code_move(5, Transform(num_mid, num_mid2), renew_variable('high', 7))
        rectangle_all_11 = VGroup(rectangle_4_2)
        for i in range(4, 8):
            rectangle_all_11.add(rectangle_num_2[i])
            rectangle_all_11.add(rectangle_element_2[i])
        code_move(1, FadeInFrom(rectangle_all_11, UP), FadeOut(num_mid),
                  renew_variable('low', 4))
        code_move(3)
        num_mid = (Text(str(5), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        self.play(FadeIn(num_mid))
        self.wait()
        code_move(4)
        rectangle_all_12 = VGroup(rectangle_2_3)
        for i in range(4, 6):
            rectangle_all_12.add(rectangle_num_3[i])
            rectangle_all_12.add(rectangle_element_3[i])
        code_move(1, FadeInFrom(rectangle_all_12, UP), FadeOut(num_mid),
                  renew_variable('high', 5))
        code_move(3)
        num_mid = (Text(str(4), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        self.play(FadeIn(num_mid))
        self.wait()
        code_move(4)
        rectangle_all_13 = VGroup(rectangle_1_5)
        for i in range(4, 5):
            rectangle_all_13.add(rectangle_num_4[i])
            rectangle_all_13.add(rectangle_element_4[i])
        code_move(1, FadeInFrom(rectangle_all_13, UP), FadeOut(num_mid),
                  renew_variable('high', 4))
        code_move(2)
        num_mid = (Text(str(4), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        code_move(5, FadeIn(num_mid), renew_variable('high', 5))
        rectangle_all_14 = VGroup(rectangle_1_6)
        for i in range(5, 6):
            rectangle_all_14.add(rectangle_num_4[i])
            rectangle_all_14.add(rectangle_element_4[i])
        code_move(1, FadeInFrom(rectangle_all_14, UP), FadeOut(num_mid),
                  renew_variable('low', 5))
        code_move(2)
        num_mid = (Text(str(4), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        code_move(6, FadeIn(num_mid), renew_variable('low', 4))
        rectangle_all_15 = VGroup(rectangle_2_7)
        for i in range(4, 6):
            rectangle_all_15.add(rectangle_num_5[i])
            rectangle_all_15.add(rectangle_element_5[i])
        self.play(FadeInFrom(rectangle_all_15, UP))
        self.wait()
        num_mid2 = (Text(str(5), font="思源宋体 Heavy",
                         color=BLACK).scale(0.8).next_to(variable_mid,
                                                         RIGHT,
                                                         buff=0.3))
        code_move(5, Transform(num_mid, num_mid2), renew_variable('high', 7))
        rectangle_all_16 = VGroup(rectangle_2_4)
        for i in range(6, 8):
            rectangle_all_16.add(rectangle_num_3[i])
            rectangle_all_16.add(rectangle_element_3[i])
        code_move(1, FadeInFrom(rectangle_all_16, UP), FadeOut(num_mid),
                  renew_variable('low', 6))
        code_move(3)
        num_mid = (Text(str(6), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        self.play(FadeIn(num_mid))
        self.wait()
        code_move(4)
        rectangle_all_17 = VGroup(rectangle_1_7)
        for i in range(6, 7):
            rectangle_all_17.add(rectangle_num_4[i])
            rectangle_all_17.add(rectangle_element_4[i])
        code_move(1, FadeInFrom(rectangle_all_17, UP), FadeOut(num_mid),
                  renew_variable('high', 6))
        code_move(2)
        num_mid = (Text(str(6), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        code_move(5, FadeIn(num_mid), renew_variable('high', 7))
        rectangle_all_18 = VGroup(rectangle_1_8)
        for i in range(7, 8):
            rectangle_all_18.add(rectangle_num_4[i])
            rectangle_all_18.add(rectangle_element_4[i])
        code_move(1, FadeInFrom(rectangle_all_18, UP), FadeOut(num_mid),
                  renew_variable('low', 7))
        code_move(2)
        num_mid = (Text(str(6), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_mid,
                                                        RIGHT,
                                                        buff=0.3))
        code_move(6, FadeIn(num_mid), renew_variable('low', 6))
        rectangle_all_19 = VGroup(rectangle_2_8)
        for i in range(6, 8):
            rectangle_all_19.add(rectangle_num_5[i])
            rectangle_all_19.add(rectangle_element_5[i])
        self.play(FadeInFrom(rectangle_all_19, UP))
        self.wait()
        num_mid2 = (Text(str(5), font="思源宋体 Heavy",
                         color=BLACK).scale(0.8).next_to(variable_mid,
                                                         RIGHT,
                                                         buff=0.3))
        self.play(Transform(num_mid, num_mid2), renew_variable('low', 4))
        self.wait()
        rectangle_all_20 = VGroup(rectangle_4_4)
        for i in range(4, 8):
            rectangle_all_20.add(rectangle_num_6[i])
            rectangle_all_20.add(rectangle_element_6[i])
        self.play(FadeInFrom(rectangle_all_20, UP))
        self.wait()
        num_mid2 = (Text(str(3), font="思源宋体 Heavy",
                         color=BLACK).scale(0.8).next_to(variable_mid,
                                                         RIGHT,
                                                         buff=0.3))
        self.play(Transform(num_mid, num_mid2), renew_variable('low', 0))
        self.wait()
        rectangle_all_21 = VGroup(rectangle_8_2)
        for i in range(8):
            rectangle_all_21.add(rectangle_num_7[i])
            rectangle_all_21.add(rectangle_element_7[i])
        self.play(FadeInFrom(rectangle_all_21, UP))
        self.wait()
        self.play(FadeOut(move_frame), FadeOut(arrow))
        self.wait()


class quickSort_partition(Scene_White):
    def construct(self):
        # global
        # Frame 整体框架
        # height: 8  *  width: 14.2
        frame_code = Rectangle(
            color=BLUE,
            stroke_opacity=0,
            height=3.5,
            width=7.1 + 4,
        ).to_corner(DL, buff=0)
        frame_variable = Rectangle(
            color=RED,
            stroke_opacity=0,
            height=3.5,
            width=7.1 - 4,
        ).to_corner(DR, buff=0)
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_color=WHITE,
            fill_opacity=1,
            height=4.5,
            width=14.2,
        ).to_corner(UP, buff=0)
        self.add(frame_code, frame_variable, frame_animation)

        # --------------- 动画框架 ---------------
        # 标题
        title = (Text("快速排序       partition(S, 0, 7)",
                      font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).to_corner(UP).shift(UP * 0.25))
        self.add(title)

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
        background.set_height(2.8, stretch=True).set_width(10.5, stretch=True)
        background.move_to(frame_code)

        # 代码中间线
        middle_line = DashedLine(np.array([0, 0, 0]),
                                 np.array([0, 2.8, 0]),
                                 color=BLACK,
                                 stroke_width=1.0).move_to(frame_code)

        # 代码 + 移动框
        class codeline_partition(Text):
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
            temp_codes = partition_codes
            for index in range(begin, 0, -1):
                if temp_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.127
                elif temp_codes[num][index] == " " and record == 0:
                    record = 1
                elif temp_codes[num][index] != " ":
                    record = 0
            return origin_len * 0.127

        codes_partition_left = (VGroup(
            *[codeline_partition(code)
              for code in partition_codes[:10]]).arrange(
                  DOWN, aligned_edge=LEFT,
                  buff=0.05).next_to(background.get_top(), DOWN,
                                     buff=0).shift(LEFT * 2.5 + DOWN * 0.15))
        codes_partition_right = (VGroup(
            *[codeline_partition(code)
              for code in partition_codes[10:]]).arrange(
                  DOWN, aligned_edge=LEFT,
                  buff=0.05).next_to(background.get_top(), DOWN,
                                     buff=0).shift(RIGHT * 2.8 + DOWN * 0.15))
        codes_partition = VGroup(codes_partition_left, codes_partition_right)

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=2.5,
            stroke_color=BLUE,
            corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1,
                         fill_color=RED).rotate(90 * DEGREES, axis=IN)
        arrow.scale(0.1)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))

        # 一键添加代码背景 and 代码
        self.add(background, middle_line, codes_partition)
        # self.add(arrow, move_frame)
        move_frame.set_width(
            ignore_space_len(codes_partition[0][0], 0),
            stretch=True).set_height(0.28, stretch=True).move_to(
                codes_partition[0][0]).align_to(codes_partition[0][0],
                                                RIGHT).shift(RIGHT * 0.05)
        arrow.next_to(move_frame, LEFT, buff=0.1)

        # 变量框
        t2c = {
            "tmp": "#2932e1",
            "low": "#801dae",
            "high": "#da1884",
            "S[low]": BLUE,
            "S[high]": RED,
        }
        variable_rectangle = Rectangle(
            color="#003472", height=3.2, width=2.5,
            stroke_opacity=1).move_to(frame_variable)
        variable_tmp = (Text("tmp:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(0.8).next_to(
                                 variable_rectangle.get_top(), DOWN,
                                 buff=0.2).align_to(variable_rectangle,
                                                    LEFT).shift(RIGHT * 0.26))
        variable_low = (Text("low:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(0.8).next_to(variable_tmp,
                                                         DOWN,
                                                         buff=0.2).align_to(
                                                             variable_tmp,
                                                             LEFT))
        variable_high = (Text("high:", font="思源宋体 Heavy", color=BLACK,
                              t2c=t2c).scale(0.8).next_to(variable_low,
                                                          DOWN,
                                                          buff=0.2).align_to(
                                                              variable_low,
                                                              LEFT))
        variable_Slow = (Text("S[low]:",
                              font="思源宋体 Heavy",
                              color=BLACK,
                              t2c=t2c).scale(0.8).next_to(variable_high,
                                                          DOWN,
                                                          buff=0.2).align_to(
                                                              variable_high,
                                                              LEFT))
        variable_Shigh = (Text("S[high]:",
                               font="思源宋体 Heavy",
                               color=BLACK,
                               t2c=t2c).scale(0.8).next_to(variable_Slow,
                                                           DOWN,
                                                           buff=0.2).align_to(
                                                               variable_Slow,
                                                               LEFT))
        tmp_num = (Text(str(4), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_tmp,
                                                        RIGHT,
                                                        buff=0.3))
        low_num = (Text(str(0), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_low,
                                                        RIGHT,
                                                        buff=0.3))
        high_num = (Text(str(7), font="思源宋体 Heavy",
                         color=BLACK).scale(0.8).next_to(variable_high,
                                                         RIGHT,
                                                         buff=0.3))
        Slow_num = (Text(str(4), font="思源宋体 Heavy",
                         color=BLACK).scale(0.8).next_to(variable_Slow,
                                                         RIGHT,
                                                         buff=0.3))
        Shigh_num = (Text(str(3), font="思源宋体 Heavy",
                          color=BLACK).scale(0.8).next_to(variable_Shigh,
                                                          RIGHT,
                                                          buff=0.3))
        all_num = VGroup(tmp_num, low_num, high_num, Slow_num, Shigh_num)
        self.add(variable_rectangle, variable_tmp, variable_low, variable_high,
                 variable_Slow, variable_Shigh)
        self.add(all_num[1], all_num[2], all_num[3], all_num[4])

        # 正方块序列
        rectangle_all = VGroup()
        for i in range(8):
            rectangle_base = MySquare(color=BLACK,
                                      side_length=0.8,
                                      stroke_opacity=1)
            rectangle_all.add(rectangle_base)
        for i in range(1, 8):
            rectangle_all[i].next_to(rectangle_all[i - 1], RIGHT, buff=0)
        rectangle_all.move_to(frame_animation)
        self.add(rectangle_all)

        # 序列的序号
        rectangle_num_all = VGroup()
        for i in range(8):
            rectangle_num_base = Text(str(i), font="思源宋体 Heavy",
                                      color=BLACK).scale(0.4)
            rectangle_num_base = rectangle_num_base.copy().next_to(
                rectangle_all[i], UP, buff=0.1)
            rectangle_num_all.add(rectangle_num_base)
        self.add(rectangle_num_all)

        # 序列的元素
        rectangle_list = [4, 2, 6, 5, 1, 7, 0, 3]
        rectangle_element_all = VGroup()
        for i in range(8):
            rectangle_element_tmp = Text(str(rectangle_list[i]),
                                         font="江西拙楷",
                                         color=BLACK).scale(0.8).move_to(
                                             rectangle_all[i])
            rectangle_element_all.add(rectangle_element_tmp)
        self.add(rectangle_element_all)

        # 箭头
        vec_low = (Arrow(np.array([0, -1, 0]),
                         np.array([0, 1, 0]),
                         color=BLACK,
                         buff=0.3,
                         fill_color=BLACK).scale(0.35))
        vec_high = vec_low.copy()
        vec_low.next_to(rectangle_all[0], DOWN, buff=0.15)
        vec_high.next_to(rectangle_all[7], DOWN, buff=0.15)
        vec_low_variables = (Text("low", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.6).next_to(vec_low,
                                                                  DOWN,
                                                                  buff=0.15))
        vec_high_variables = (Text("high", font="思源宋体 Heavy",
                                   color=BLACK).scale(0.6).next_to(vec_high,
                                                                   DOWN,
                                                                   buff=0.15))
        vec_high_variables.add_updater(
            lambda a: a.next_to(vec_high, DOWN, buff=0.5))
        vec_low_variables.add_updater(
            lambda a: a.next_to(vec_low, DOWN, buff=0.05))
        vec_high_all = VGroup(vec_high, vec_high_variables)
        vec_low_all = VGroup(vec_low, vec_low_variables)
        self.add(vec_high_all, vec_low_all)

        # 面向对象零 (包装代码框移动)
        def code_move(i, j, *method):
            # 调用方法举例: code_move(1, 0, FadeIn(vec_pos_all))
            lines = 10 * i + j
            self.play(
                *method,
                move_frame.set_width,
                ignore_space_len(codes_partition[i][j], lines),
                move_frame.move_to,
                codes_partition[i][j],
                move_frame.align_to,
                codes_partition[i][j],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {
                    "height": 0.28,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()

        # 面向对象一 (变量框元素值更新)
        def renew_variable(string, num):
            # 调用方法举例: self.play(renew_variable('rm', 1))
            if string == 'low':
                i_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(0.8).next_to(variable_low,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[1], i_num)
            if string == 'high':
                i_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(0.8).next_to(variable_high,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[2], i_num)
            if string == 'Slow':
                i_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(0.8).next_to(variable_Slow,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[3], i_num)
            if string == 'Shigh':
                i_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(0.8).next_to(variable_Shigh,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[4], i_num)

        # partition
        self.wait()
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()
        self.play(FadeIn(all_num[0]))
        self.wait()
        code_move(0, 1)
        code_move(0, 3)
        code_move(0, 5)
        code_move(0, 7)
        numbers_1 = rectangle_element_all[7].copy()
        self.play(FadeOut(rectangle_element_all[0]), numbers_1.move_to,
                  rectangle_element_all[0], renew_variable('Slow', 3))
        self.wait()
        code_move(0, 8)
        self.play(vec_low_all.shift, RIGHT * 0.8, renew_variable('low', 1),
                  renew_variable('Slow', 2))
        self.wait()
        code_move(1, 0)
        code_move(1, 1)
        self.play(vec_low_all.shift, RIGHT * 0.8, renew_variable('low', 2),
                  renew_variable('Slow', 6))
        self.wait()
        code_move(1, 0)
        code_move(1, 2)
        code_move(1, 4)
        numbers_2 = rectangle_element_all[2].copy()
        self.play(FadeOut(rectangle_element_all[7]), numbers_2.move_to,
                  rectangle_element_all[7], renew_variable('Shigh', 6))
        self.wait()
        code_move(1, 5)
        self.play(vec_high_all.shift, LEFT * 0.8, renew_variable('high', 6),
                  renew_variable('Shigh', 0))
        self.wait()
        code_move(0, 1)
        code_move(0, 3)
        code_move(0, 5)
        code_move(0, 7)
        numbers_3 = rectangle_element_all[6].copy()
        self.play(FadeOut(rectangle_element_all[2]), numbers_3.move_to,
                  rectangle_element_all[2], renew_variable('Slow', 0))
        self.wait()
        code_move(0, 8)
        self.play(vec_low_all.shift, RIGHT * 0.8, renew_variable('low', 3),
                  renew_variable('Slow', 5))
        code_move(1, 0)
        code_move(1, 2)
        code_move(1, 4)
        numbers_4 = rectangle_element_all[3].copy()
        self.play(FadeOut(rectangle_element_all[6]), numbers_4.move_to,
                  rectangle_element_all[6], renew_variable('Shigh', 5))
        self.wait()
        code_move(1, 5)
        self.play(vec_high_all.shift, LEFT * 0.8, renew_variable('high', 5),
                  renew_variable('Shigh', 7))
        self.wait()
        code_move(0, 1)
        code_move(0, 3)
        code_move(0, 4)
        self.play(vec_high_all.shift, LEFT * 0.8, renew_variable('high', 4),
                  renew_variable('Shigh', 1))
        self.wait()
        code_move(0, 3)
        code_move(0, 5)
        code_move(0, 7)
        numbers_5 = rectangle_element_all[4].copy()
        self.play(FadeOut(rectangle_element_all[3]), numbers_5.move_to,
                  rectangle_element_all[3], renew_variable('Slow', 1))
        self.wait()
        code_move(0, 8)
        self.play(vec_low_all.shift, RIGHT * 0.8, renew_variable('low', 4),
                  renew_variable('Slow', 1))
        self.wait()
        code_move(1, 0)
        code_move(1, 2)
        code_move(1, 8)
        rectangle_element_tmp = Text(str(4), font="江西拙楷",
                                     color=BLACK).scale(0.8).move_to(
                                         rectangle_all[4])
        self.play(Transform(rectangle_element_all[4], rectangle_element_tmp),
                  renew_variable('Slow', 4), renew_variable('Shigh', 4))
        self.wait()
        code_move(1, 9)
        self.play(FadeOut(move_frame), FadeOut(arrow))
        self.wait()


class quickSort_quickSort(Scene_White):
    def construct(self):
        # global
        # Frame 整体框架
        # height: 8  *  width: 14.2
        frame_code = Rectangle(
            color=BLUE,
            stroke_opacity=0,
            height=3.5,
            width=7.1 + 2,
        ).to_corner(DL, buff=0)
        frame_variable = Rectangle(
            color=RED,
            stroke_opacity=0,
            height=3.5,
            width=7.1 - 2,
        ).to_corner(DR, buff=0)
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_color=WHITE,
            fill_opacity=1,
            height=4.5,
            width=14.2,
        ).to_corner(UP, buff=0)
        self.add(frame_code, frame_variable, frame_animation)

        # --------------- 动画框架 ---------------
        # 标题
        title = (Text("快速排序       quickSort(S, 0, 7)",
                      font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).to_corner(UP).shift(UP * 0.25))
        self.add(title)

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
        background.set_height(2.8, stretch=True).set_width(8, stretch=True)
        background.move_to(frame_code)  #.shift(DOWN * 0.5)

        # 代码 + 移动框
        class codeline_quickSort(Text):
            CONFIG = {
                "size": 0.6,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        def ignore_space_len(code, num):
            origin_len = len(code)
            begin = origin_len - 1
            record = 0
            temp_codes = quickSort_codes
            for index in range(begin, 0, -1):
                if temp_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.167
                elif temp_codes[num][index] == " " and record == 0:
                    record = 1
                elif temp_codes[num][index] != " ":
                    record = 0
            return origin_len * 0.167

        codes_quickSort = (VGroup(
            *[codeline_quickSort(code) for code in quickSort_codes]).arrange(
                DOWN, aligned_edge=LEFT,
                buff=0.05).next_to(background.get_top(), DOWN,
                                   buff=0).shift(RIGHT * 0.1 + DOWN * 0.1))

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=2.5,
            stroke_color=BLUE,
            corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1,
                         fill_color=RED).rotate(90 * DEGREES, axis=IN)
        arrow.scale(0.09)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.08))

        # 一键添加代码背景 and 代码
        self.add(background, codes_quickSort)
        # self.add(arrow, move_frame)
        move_frame.set_width(
            ignore_space_len(codes_quickSort[1], 1),
            stretch=True).set_height(0.31, stretch=True).move_to(
                codes_quickSort[1]).align_to(codes_quickSort[1],
                                             RIGHT).shift(RIGHT * 0.05)

        # 变量框
        t2c = {
            "low": BLUE,
            "pivot": RED,
            "high": PURPLE,
        }
        variable_rectangle = Rectangle(
            color="#003472", height=3, width=4,
            stroke_opacity=1).move_to(frame_variable)
        variable_low = (Text("low:", font="思源宋体 Heavy", color=BLACK,
                             t2c=t2c).scale(0.8).next_to(
                                 variable_rectangle.get_top(), DOWN,
                                 buff=0.3).align_to(variable_rectangle,
                                                    LEFT).shift(RIGHT * 1.2))
        variable_pivot = (Text("pivot:",
                               font="思源宋体 Heavy",
                               color=BLACK,
                               t2c=t2c).scale(0.8).next_to(variable_low,
                                                           DOWN,
                                                           buff=0.6).align_to(
                                                               variable_low,
                                                               LEFT))
        variable_high = (Text("high:", font="思源宋体 Heavy", color=BLACK,
                              t2c=t2c).scale(0.8).next_to(variable_pivot,
                                                          DOWN,
                                                          buff=0.6).align_to(
                                                              variable_pivot,
                                                              LEFT))
        low_num = (Text(str(0), font="思源宋体 Heavy",
                        color=BLACK).scale(0.8).next_to(variable_low,
                                                        RIGHT,
                                                        buff=0.3))
        pivot_num = (Text(str(4), font="思源宋体 Heavy",
                          color=BLACK).scale(0.8).next_to(variable_pivot,
                                                          RIGHT,
                                                          buff=0.3))
        high_num = (Text(str(7), font="思源宋体 Heavy",
                         color=BLACK).scale(0.8).next_to(variable_high,
                                                         RIGHT,
                                                         buff=0.3))
        all_num = VGroup(low_num, pivot_num, high_num)
        self.add(variable_rectangle, variable_low, variable_pivot,
                 variable_high)
        self.add(all_num[0], all_num[2])

        # 正方块序列
        rectangle_all = VGroup()
        for i in range(8):
            rectangle_base = MySquare(color=BLACK,
                                      side_length=0.8,
                                      stroke_opacity=1)
            rectangle_all.add(rectangle_base)
        for i in range(1, 8):
            rectangle_all[i].next_to(rectangle_all[i - 1], RIGHT, buff=0)
        rectangle_all.move_to(frame_animation)
        self.add(rectangle_all)

        # 序列的序号
        rectangle_num_all = VGroup()
        for i in range(8):
            rectangle_num_base = Text(str(i), font="思源宋体 Heavy",
                                      color=BLACK).scale(0.4)
            rectangle_num_base = rectangle_num_base.copy().next_to(
                rectangle_all[i], UP, buff=0.1)
            rectangle_num_all.add(rectangle_num_base)
        self.add(rectangle_num_all)

        # 序列的元素
        rectangle_list = [4, 2, 6, 5, 1, 7, 0, 3]
        rectangle_element_all = VGroup()
        for i in range(8):
            rectangle_element_tmp = Text(str(rectangle_list[i]),
                                         font="江西拙楷",
                                         color=BLACK).scale(0.8).move_to(
                                             rectangle_all[i])
            rectangle_element_all.add(rectangle_element_tmp)
        self.add(rectangle_element_all)

        # 箭头
        vec_low = (Arrow(np.array([0, -1, 0]),
                         np.array([0, 1, 0]),
                         color=BLACK,
                         buff=0.3,
                         fill_color=BLACK).scale(0.35))
        vec_high = vec_low.copy()
        vec_low.next_to(rectangle_all[0], DOWN, buff=0.15)
        vec_high.next_to(rectangle_all[7], DOWN, buff=0.15)
        vec_low_variables = (Text("low", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.6).next_to(vec_low,
                                                                  DOWN,
                                                                  buff=0.15))
        vec_high_variables = (Text("high", font="思源宋体 Heavy",
                                   color=BLACK).scale(0.6).next_to(vec_high,
                                                                   DOWN,
                                                                   buff=0.15))
        vec_high_variables.add_updater(
            lambda a: a.next_to(vec_high, DOWN, buff=0.5))
        vec_low_variables.add_updater(
            lambda a: a.next_to(vec_low, DOWN, buff=0.05))
        vec_high_all = VGroup(vec_high, vec_high_variables)
        vec_low_all = VGroup(vec_low, vec_low_variables)
        self.add(vec_high_all, vec_low_all)

        # 蓝色正方块
        rectangle_blue = rectangle_all.copy()
        for i in range(8):
            rectangle_blue[i].set_opacity(0.5).set_color(BLUE).set_height(
                0.75).set_width(0.75).move_to(rectangle_all[i])
        # self.add(rectangle_blue)

        # 借用 OOP 的方法
        # 面向对象零 (包装代码框移动)
        def code_move(i, *method):
            # 调用方法举例: code_move(1, 0, FadeIn(vec_pos_all))
            self.play(
                *method,
                move_frame.set_width,
                ignore_space_len(codes_quickSort[i], i),
                move_frame.move_to,
                codes_quickSort[i],
                move_frame.align_to,
                codes_quickSort[i],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {
                    "height": 0.31,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()

        # 面向对象一 (变量框元素值更新)
        def renew_variable(string, num):
            # 调用方法举例: self.play(renew_variable('rm', 1))
            if string == 'low':
                i_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(0.8).next_to(variable_low,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[0], i_num)
            if string == 'high':
                i_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(0.8).next_to(variable_high,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(all_num[2], i_num)
            if string == 'pivot':
                i_num = (Text(str(num), font="思源宋体 Heavy",
                              color=BLACK).scale(0.8).next_to(variable_pivot,
                                                              RIGHT,
                                                              buff=0.3))
                return Transform(pivot_num, i_num)

        # quickSort
        self.wait()
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()
        code_move(2)
        rectangle_element_tmp_0 = Text(str(3), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[0])
        rectangle_element_tmp_1 = Text(str(2), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[1])
        rectangle_element_tmp_2 = Text(str(0), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[2])
        rectangle_element_tmp_3 = Text(str(1), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[3])
        rectangle_element_tmp_4 = Text(str(4), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[4])
        rectangle_element_tmp_5 = Text(str(7), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[5])
        rectangle_element_tmp_6 = Text(str(5), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[6])
        rectangle_element_tmp_7 = Text(str(6), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[7])
        code_move(4)
        self.play(FadeIn(pivot_num), FadeIn(rectangle_blue[4]),
                  Transform(rectangle_element_all[0], rectangle_element_tmp_0),
                  Transform(rectangle_element_all[2], rectangle_element_tmp_2),
                  Transform(rectangle_element_all[3], rectangle_element_tmp_3),
                  Transform(rectangle_element_all[4], rectangle_element_tmp_4),
                  Transform(rectangle_element_all[6], rectangle_element_tmp_6),
                  Transform(rectangle_element_all[7], rectangle_element_tmp_7))
        self.wait()
        code_move(5)
        code_move(1, FadeOut(pivot_num), vec_high_all.shift, LEFT * 0.8 * 4,
                  renew_variable('high', 3))
        code_move(2)
        tmp_pivot = (Text(str(3), font="思源宋体 Heavy",
                          color=BLACK).scale(0.8).next_to(variable_pivot,
                                                          RIGHT,
                                                          buff=0.3))
        pivot_num = tmp_pivot.copy()
        rectangle_element_tmp_0 = Text(str(1), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[0])
        rectangle_element_tmp_1 = Text(str(2), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[1])
        rectangle_element_tmp_2 = Text(str(0), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[2])
        rectangle_element_tmp_3 = Text(str(3), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[3])
        rectangle_element_tmp_4 = Text(str(4), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[4])
        rectangle_element_tmp_5 = Text(str(7), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[5])
        rectangle_element_tmp_6 = Text(str(5), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[6])
        rectangle_element_tmp_7 = Text(str(6), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[7])
        code_move(4)
        self.play(FadeIn(pivot_num), FadeIn(rectangle_blue[3]),
                  Transform(rectangle_element_all[0], rectangle_element_tmp_0),
                  Transform(rectangle_element_all[3], rectangle_element_tmp_3))
        self.wait()
        code_move(5)
        code_move(1, FadeOut(pivot_num), vec_high_all.shift, LEFT * 0.8,
                  renew_variable('high', 2))
        code_move(2)
        tmp_pivot = (Text(str(1), font="思源宋体 Heavy",
                          color=BLACK).scale(0.8).next_to(variable_pivot,
                                                          RIGHT,
                                                          buff=0.3))
        pivot_num = tmp_pivot.copy()
        rectangle_element_tmp_0 = Text(str(0), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[0])
        rectangle_element_tmp_1 = Text(str(1), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[1])
        rectangle_element_tmp_2 = Text(str(2), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[2])
        rectangle_element_tmp_3 = Text(str(3), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[3])
        rectangle_element_tmp_4 = Text(str(4), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[4])
        rectangle_element_tmp_5 = Text(str(7), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[5])
        rectangle_element_tmp_6 = Text(str(5), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[6])
        rectangle_element_tmp_7 = Text(str(6), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[7])
        code_move(4)
        self.play(FadeIn(pivot_num), FadeIn(rectangle_blue[1]),
                  Transform(rectangle_element_all[0], rectangle_element_tmp_0),
                  Transform(rectangle_element_all[1], rectangle_element_tmp_1),
                  Transform(rectangle_element_all[2], rectangle_element_tmp_2))
        self.wait()
        code_move(5)
        code_move(1, FadeOut(pivot_num), vec_high_all.shift, LEFT * 0.8 * 2,
                  renew_variable('high', 0))
        code_move(2)
        code_move(3)
        # 箭头移动，变量变化
        tmp_pivot = (Text(str(1), font="思源宋体 Heavy",
                          color=BLACK).scale(0.8).next_to(variable_pivot,
                                                          RIGHT,
                                                          buff=0.3))
        pivot_num = tmp_pivot.copy()
        code_move(6, FadeIn(pivot_num), FadeIn(rectangle_blue[0]),
                  vec_high_all.shift, RIGHT * 0.8 * 2,
                  renew_variable('high', 2))
        code_move(1, FadeOut(pivot_num), vec_low_all.shift, RIGHT * 0.8 * 2,
                  renew_variable('low', 2))
        code_move(2)
        code_move(3)
        # 箭头移动，变量变化
        tmp_pivot = (Text(str(1), font="思源宋体 Heavy",
                          color=BLACK).scale(0.8).next_to(variable_pivot,
                                                          RIGHT,
                                                          buff=0.3))
        pivot_num = tmp_pivot.copy()
        code_move(6, FadeIn(pivot_num), FadeIn(rectangle_blue[2]),
                  vec_low_all.shift, LEFT * 0.8 * 2, renew_variable('low', 0))
        self.play(renew_variable('pivot', 3), vec_high_all.shift, RIGHT * 0.8,
                  renew_variable('high', 3))
        self.wait()
        self.play(renew_variable('pivot', 4), vec_high_all.shift,
                  RIGHT * 0.8 * 4, renew_variable('high', 7))
        self.wait()
        code_move(1, FadeOut(pivot_num), vec_low_all.shift, RIGHT * 0.8 * 5,
                  renew_variable('low', 5))
        code_move(2)
        tmp_pivot = (Text(str(7), font="思源宋体 Heavy",
                          color=BLACK).scale(0.8).next_to(variable_pivot,
                                                          RIGHT,
                                                          buff=0.3))
        pivot_num = tmp_pivot.copy()
        rectangle_element_tmp_0 = Text(str(0), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[0])
        rectangle_element_tmp_1 = Text(str(1), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[1])
        rectangle_element_tmp_2 = Text(str(2), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[2])
        rectangle_element_tmp_3 = Text(str(3), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[3])
        rectangle_element_tmp_4 = Text(str(4), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[4])
        rectangle_element_tmp_5 = Text(str(6), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[5])
        rectangle_element_tmp_6 = Text(str(5), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[6])
        rectangle_element_tmp_7 = Text(str(7), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[7])
        code_move(4)
        self.play(FadeIn(pivot_num), FadeIn(rectangle_blue[7]),
                  Transform(rectangle_element_all[5], rectangle_element_tmp_5),
                  Transform(rectangle_element_all[6], rectangle_element_tmp_6),
                  Transform(rectangle_element_all[7], rectangle_element_tmp_7))
        self.wait()
        code_move(5)
        code_move(1, FadeOut(pivot_num), vec_high_all.shift, LEFT * 0.8,
                  renew_variable('high', 6))
        code_move(2)
        tmp_pivot = (Text(str(6), font="思源宋体 Heavy",
                          color=BLACK).scale(0.8).next_to(variable_pivot,
                                                          RIGHT,
                                                          buff=0.3))
        pivot_num = tmp_pivot.copy()
        rectangle_element_tmp_0 = Text(str(0), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[0])
        rectangle_element_tmp_1 = Text(str(1), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[1])
        rectangle_element_tmp_2 = Text(str(2), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[2])
        rectangle_element_tmp_3 = Text(str(3), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[3])
        rectangle_element_tmp_4 = Text(str(4), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[4])
        rectangle_element_tmp_5 = Text(str(5), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[5])
        rectangle_element_tmp_6 = Text(str(6), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[6])
        rectangle_element_tmp_7 = Text(str(7), font="江西拙楷",
                                       color=BLACK).scale(0.8).move_to(
                                           rectangle_all[7])
        code_move(4)
        self.play(FadeIn(pivot_num), FadeIn(rectangle_blue[6]),
                  Transform(rectangle_element_all[5], rectangle_element_tmp_5),
                  Transform(rectangle_element_all[6], rectangle_element_tmp_6))
        self.wait()
        code_move(5)
        code_move(1, FadeOut(pivot_num), vec_high_all.shift, LEFT * 0.8,
                  renew_variable('high', 5))
        code_move(2)
        code_move(3)
        # 箭头移动，变量变化
        tmp_pivot = (Text(str(6), font="思源宋体 Heavy",
                          color=BLACK).scale(0.8).next_to(variable_pivot,
                                                          RIGHT,
                                                          buff=0.3))
        pivot_num = tmp_pivot.copy()
        code_move(6, FadeIn(rectangle_blue[5]), FadeIn(pivot_num),
                  vec_high_all.shift, RIGHT * 0.8, renew_variable('high', 6))
        self.play(renew_variable('pivot', 7), vec_high_all.shift, RIGHT * 0.8,
                  renew_variable('high', 7))
        self.wait()
        self.play(renew_variable('pivot', 4), vec_low_all.shift,
                  LEFT * 0.8 * 5, renew_variable('low', 0))
        self.wait()
        self.play(FadeOut(move_frame), FadeOut(arrow))
        self.wait()
