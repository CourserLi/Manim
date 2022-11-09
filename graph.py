from manimlib.imports import *
from manim_tuan import *

# dfsTraverse
# dfsList
# dfsMatrix
# bfsTraverse_List
# bfsTraverse_Matrix
# primList
# primMatrix
# kruskalList
# kruskalMatrix

dfsTraverse_codes = [
    "",
]

dfsList_codes = [
    "",
]

dfsMatrix_codes = [
    "",
]

bfsTraverse_List_codes = [
    "",
]

bfsTraverse_Matrix_codes = [
    "",
]

primList_codes = [
    "",
]

primMatrix_codes = [
    "void prim(EdgeType noEdge)",
    "{",
    "  struct Dist",
    "  {",
    "    int adjVex;",
    "    EdgeType lowCost;",
    "  } *D = new Dist[this->verNum];",
    "  EdgeType minCost;",
    "  int u, i, j, count = 0;",
    "  for (i = 0; i < this->verNum; ++i)",
    "  {",
    "    this->visited[i] = false;",
    "    D[i].lowCost = noEdge;",
    "  }",
    "  u = 0;",
    "  this->visited[u] = true;",
    "  for (i = 1; i < this->verNum; ++i)",
    "  {",
    "    for (j = 0; j < this->verNum; ++j)",
    "      if (!this->visited[j]&&edges[u][j] != noEdge)",
    "      {",
    "        if (edges[u][j] < D[j].lowCost)",
    "        {",
    "          D[j].lowCost = edges[u][j];",
    "          D[j].adjVex = u;",
    "        }",
    "      }",
    "    minCost = noEdge;",
    "    for (j = 0; j < this->verNum; ++j)",
    "      if (D[j].lowCost < minCost)",
    "      {",
    "        minCost = D[j].lowCost;",
    "        u = j;",
    "      }",
    "    this->TE[count].vex1 = D[u].adjVex;",
    "    this->TE[count].vex2 = u;",
    "    this->TE[count++].weight = D[u].lowCost;",
    "    D[u].lowCost = noEdge;",
    "    this->visited[u] = true;",
    "  }",
    "  delete[] D;",
    "}",
]

kruskalList_codes = [
    "",
]

kruskalMatrix_codes = [
    "",
]


class Scene_White(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
            "use_plot_depth": True,
        }
    }


class dfsMatrix(Scene_White):
    def construct(self):
        self.add(Text("dfsMatrix", font="思源宋体 Heavy", color=BLACK))
        self.wait(1)


class primMatrix(Scene_White):
    def construct(self):
        '''
        # printGraph + 显示矩阵
        # prim + 动画演示
        # printMst + 显示最小生成树
        # 矩阵定量：visited[i] TE[i].vex1.vex2.weight 
        # 定量：noEdge-INF, verNum-6
        # 变量：minCost, u, i, j, count
        self.add(Text("primMatrix", font="思源宋体 Heavy", color=BLACK))
        self.wait(1)
        '''
        # global
        # Frame 整体框架
        # height: 8  *  width: 14.2
        frame_edge = Rectangle(
            color=GREEN,
            stroke_opacity=0,
            height=4,
            width=4,
        ).to_corner(UL, buff=0)
        frame_variable = Rectangle(
            color=RED,
            stroke_opacity=0,
            height=4,
            width=4,
        ).to_corner(DL, buff=0)
        frame_animation = Rectangle(
            color="#ffa400",
            stroke_width=5,
            stroke_opacity=0,
            fill_color=WHITE,
            fill_opacity=1,
            height=8,
            width=14.2 - 4 - 4.5,
        ).to_corner(ORIGIN, buff=0).shift(LEFT * 0.25)
        frame_code = Rectangle(
            color=BLUE,
            stroke_opacity=0,
            height=8,
            width=4.5,
        ).to_corner(RIGHT, buff=0)
        frame_right = Rectangle(
            color=BLUE,
            stroke_opacity=0,
            height=8,
            width=4,
        ).next_to(frame_code, buff=0)
        # self.add(frame_edge, frame_variable, frame_animation, frame_code, frame_right)

        # --------------- 动画框架 ---------------
        # 标题
        title = (Text("Prim", font="思源宋体 Heavy",
                      color=BLACK).scale(0.8).to_corner(UP).shift(UP * 0.25))
        # self.add(title)

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
        background.set_height(7.9, stretch=True).set_width(4.4, stretch=True)
        background.move_to(frame_code)

        # 代码 + 移动框
        class codeline_primMatrix(Text):
            CONFIG = {
                "size": 0.3,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        def ignore_space_len(code, num):
            origin_len = len(code)
            begin = origin_len - 1
            record = 0
            temp_codes = primMatrix_codes
            for index in range(begin, 0, -1):
                if temp_codes[num][index] == " " and record == 1:
                    return (origin_len - index - 2) * 0.076
                elif temp_codes[num][index] == " " and record == 0:
                    record = 1
                elif temp_codes[num][index] != " ":
                    record = 0
            return origin_len * 0.076

        def new_ignore_space_len(num):
            return len(primMatrix_codes[num].strip()) * 0.087

        codes_primMatrix = (VGroup(
            *[codeline_primMatrix(code) for code in primMatrix_codes]).arrange(
                DOWN, aligned_edge=LEFT,
                buff=0.05).next_to(background.get_top(), DOWN,
                                   buff=0).shift(RIGHT * 0 + DOWN * 0.06))

        # 代码框
        move_frame = RoundedRectangle(
            stroke_width=2,
            stroke_color=BLUE,
            corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1,
                         fill_color=RED).rotate(90 * DEGREES, axis=IN)
        arrow.scale(0.065)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.05))

        # 一键添加代码背景 and 代码
        # self.add(background, codes_primMatrix)
        move_frame.set_width(new_ignore_space_len(7), stretch=True).set_height(
            0.165, stretch=True).move_to(codes_primMatrix[7]).align_to(
                codes_primMatrix[7], RIGHT).shift(RIGHT * 0.05)
        """
        整体代码框移动测试
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()
        for i in range(3, len(primMatrix_codes)):
            code_move(i)
            self.wait()
        """

        # edge 框
        block = Rectangle(
            color=BLACK,
            stroke_width=2,
            stroke_opacity=1,
            fill_color=WHITE,
            fill_opacity=1,
            height=4 / 7,
            width=4 / 7,
        )
        block.align_to(frame_edge, LEFT).align_to(frame_edge, UP)
        edge_blocks = VGroup()
        for i in range(7):
            for j in range(7):
                item = block.copy()
                item.shift((4 / 7) * i * DOWN)
                item.shift((4 / 7) * j * RIGHT)
                edge_blocks.add(item)
        # self.add(edge_blocks)

        # 填入字符和颜色
        edge_text, edge_color = VGroup(), VGroup()
        edge_text.add(
            Text(" ", font="思源宋体 Heavy", color=WHITE).move_to(edge_blocks[0]))
        edge_color.add(
            Rectangle(stroke_opacity=0,
                      fill_color=WHITE,
                      fill_opacity=1,
                      height=3.9 / 7,
                      width=3.9 / 7).move_to(edge_blocks[0]))
        for i in range(7):
            for j in range(7):
                text, color = edge_text[0].copy(), edge_color[0].copy()
                # 横排 Vx
                if (i == 0 and j != 0):
                    text = Text("V" + str(j - 1),
                                font="思源宋体 Heavy",
                                color=BLACK).scale(0.5)
                    color.set_fill("#759464")  # 绿色
                # 竖排 Vx
                if (j == 0 and i != 0):
                    text = Text("V" + str(i - 1),
                                font="思源宋体 Heavy",
                                color=BLACK).scale(0.5)
                    color.set_fill("#759464")  # 绿色
                # 斜中心 INF
                if (i == j and i != 0 and j != 0):
                    text = Text("INF", font="思源宋体 Heavy",
                                color=BLACK).scale(0.5)
                    color.set_fill("#AD5D67")  # 红色
                # 其他 INF
                if ((i == 1 and j == 5) or (i == 1 and j == 6)
                        or (i == 2 and j == 4) or (i == 2 and j == 6)
                        or (i == 5 and j == 1) or (i == 6 and j == 1)
                        or (i == 4 and j == 2) or (i == 6 and j == 2)
                        or (i == 4 and j == 5) or (i == 5 and j == 4)):
                    text = Text("INF", font="思源宋体 Heavy",
                                color=BLACK).scale(0.5)
                    color.set_fill("#AD5D67")  # 红色
                # 数字 1
                if ((i == 1 and j == 3) or (i == 3 and j == 1)):
                    text = Text("1", font="思源宋体 Heavy", color=BLACK).scale(0.5)
                    color.set_fill("#589DD6")  # 蓝色
                # 数字 2
                if ((i == 4 and j == 6) or (i == 6 and j == 4)):
                    text = Text("2", font="思源宋体 Heavy", color=BLACK).scale(0.5)
                    color.set_fill("#589DD6")  # 蓝色
                # 数字 3
                if ((i == 2 and j == 5) or (i == 5 and j == 2)):
                    text = Text("3", font="思源宋体 Heavy", color=BLACK).scale(0.5)
                    color.set_fill("#589DD6")  # 蓝色
                # 数字 4
                if ((i == 3 and j == 6) or (i == 6 and j == 3)):
                    text = Text("4", font="思源宋体 Heavy", color=BLACK).scale(0.5)
                    color.set_fill("#589DD6")  # 蓝色
                # 数字 5
                if ((i == 3 and j == 4) or (i == 1 and j == 4)
                        or (i == 2 and j == 3) or (i == 4 and j == 3)
                        or (i == 4 and j == 1) or (i == 3 and j == 2)):
                    text = Text("5", font="思源宋体 Heavy", color=BLACK).scale(0.5)
                    color.set_fill("#589DD6")  # 蓝色
                # 数字 6
                if ((i == 1 and j == 2) or (i == 3 and j == 5)
                        or (i == 5 and j == 6) or (i == 2 and j == 1)
                        or (i == 5 and j == 3) or (i == 6 and j == 5)):
                    text = Text("6", font="思源宋体 Heavy", color=BLACK).scale(0.5)
                    color.set_fill("#589DD6")  # 蓝色
                text.move_to(edge_blocks[7 * i + j])
                edge_text.add(text)
                color.move_to(edge_blocks[7 * i + j])
                edge_color.add(color)
        # 左斜框内的 edge 文本
        edge_core = Text("edge", font="思源宋体 Heavy", color=BLACK).scale(0.5)
        edge_core.move_to(edge_blocks[0])
        edge_core.rotate(angle=45 * DEGREES)
        # self.add(edge_color, edge_text, edge_core)

        # 变量框
        t2c = {
            "adjVex": RED,
            "lowCost": "#801dae",
        }
        variable_rectangle = Rectangle(
            color="#003472",
            height=3.8,
            width=3.9,
            stroke_width=1,
            stroke_opacity=1).move_to(frame_variable)
        # self.add(variable_rectangle)
        variable_adjvex, variable_lowcost = VGroup(), VGroup()
        variable_adjvex_num, variable_lowcost_num = VGroup(), VGroup()
        for i in range(6):
            if (i == 0):
                variable_adjvex_tmp = Text("D[0].adjVex:",
                                           font="思源宋体 Heavy",
                                           color=BLACK,
                                           t2c=t2c).scale(0.4)
                variable_adjvex_tmp.align_to(variable_rectangle,
                                             LEFT).align_to(
                                                 variable_rectangle, UP)
                variable_adjvex_tmp.shift(RIGHT * 0.15 + DOWN * 0.1)
            else:
                variable_adjvex_tmp = Text("D[" + str(i) + "].adjVex:",
                                           font="思源宋体 Heavy",
                                           color=BLACK,
                                           t2c=t2c).scale(0.4)
                variable_adjvex_tmp.move_to(variable_adjvex[i - 1])
                variable_adjvex_tmp.shift(DOWN * 0.5)
            variable_adjvex.add(variable_adjvex_tmp)
        for i in range(6):
            if (i == 0):
                variable_lowcost_tmp = Text("D[0].lowCost:",
                                            font="思源宋体 Heavy",
                                            color=BLACK,
                                            t2c=t2c).scale(0.4)
                variable_lowcost_tmp.align_to(variable_rectangle,
                                              RIGHT).align_to(
                                                  variable_rectangle, UP)
                variable_lowcost_tmp.shift(LEFT * 0.6 + DOWN * 0.1)
            else:
                variable_lowcost_tmp = Text("D[" + str(i) + "].lowCost:",
                                            font="思源宋体 Heavy",
                                            color=BLACK,
                                            t2c=t2c).scale(0.4)
                variable_lowcost_tmp.move_to(variable_lowcost[i - 1])
                variable_lowcost_tmp.shift(DOWN * 0.5)
            variable_lowcost.add(variable_lowcost_tmp)
        # self.add(variable_adjvex, variable_lowcost)
        variable_mincost = Text("minCost:",
                                font="思源宋体 Heavy",
                                color=BLACK,
                                t2c=t2c).scale(0.4)
        variable_mincost.next_to(
            variable_adjvex, DOWN,
            buff=0.25)  # .align_to(variable_adjvex, RIGHT)
        variable_u = Text("u:", font="思源宋体 Heavy", color=BLACK,
                          t2c=t2c).scale(0.4)
        variable_u.next_to(variable_mincost, DOWN,
                           buff=0.25)  # .align_to(variable_mincost, RIGHT)
        variable_i = Text("i:", font="思源宋体 Heavy", color=BLACK,
                          t2c=t2c).scale(0.4)
        variable_i.next_to(variable_lowcost, DOWN,
                           buff=0.25)  # .align_to(variable_lowcost, RIGHT)
        variable_j = Text("j:", font="思源宋体 Heavy", color=BLACK,
                          t2c=t2c).scale(0.4)
        variable_j.next_to(variable_i, DOWN,
                           buff=0.25)  # .align_to(variable_j, RIGHT)
        # self.add(variable_mincost, variable_u, variable_i, variable_j)
        adjvex_list = [0, 0, 0, 0, 2, 2]
        for i in range(6):
            num = Text(str(adjvex_list[i]), font="思源宋体 Heavy",
                       color=BLACK).scale(0.45)
            num.next_to(variable_adjvex[i], RIGHT, buff=0.1)
            variable_adjvex_num.add(num)
            inf = Text("INF", font="思源宋体 Heavy", color=BLACK).scale(0.45)
            inf.next_to(variable_lowcost[i], RIGHT, buff=0.1)
            variable_lowcost_num.add(inf)
        # self.add(variable_adjvex_num, variable_lowcost_num)
        variable_mincost_num = Text("INF", font="思源宋体 Heavy",
                                    color=BLACK).scale(0.45)
        variable_mincost_num.next_to(variable_mincost, RIGHT, buff=0.1)
        variable_u_num = Text("0", font="思源宋体 Heavy", color=BLACK).scale(0.45)
        variable_u_num.next_to(variable_u, RIGHT, buff=0.1)
        variable_i_num = Text("0", font="思源宋体 Heavy", color=BLACK).scale(0.45)
        variable_i_num.next_to(variable_i, RIGHT, buff=0.1)
        variable_j_num = Text("0", font="思源宋体 Heavy", color=BLACK).scale(0.45)
        variable_j_num.next_to(variable_j, RIGHT, buff=0.1)
        # self.add(variable_mincost_num, variable_u_num, variable_i_num, variable_j_num)
        division = Rectangle(color="#003472",
                             height=0.01,
                             width=3.9,
                             stroke_width=1,
                             stroke_opacity=1)
        division.move_to(frame_variable).shift(DOWN * 1.05)
        # self.add(division)

        # 动画中心区域
        circles, lines = VGroup(), VGroup()
        circle = Circle(radius=0.4,
                        stroke_width=3,
                        stroke_color=BLACK,
                        stroke_opacity=1)
        circle0, circle1, circle2, circle3, circle4, circle5 = circle.copy(
        ), circle.copy(), circle.copy(), circle.copy(), circle.copy(
        ), circle.copy()
        circle0.move_to(frame_animation).shift(UP * 2.5 + RIGHT * 0.25)
        circle2.move_to(circle0).shift(DOWN * 1.25)
        circle1.move_to(circle2).shift(LEFT * 1.25)
        circle3.move_to(circle2).shift(RIGHT * 1.25)
        circle4.move_to(circle2).shift(DOWN * 1.25 + LEFT * 0.65)
        circle5.move_to(circle2).shift(DOWN * 1.25 + RIGHT * 0.65)
        circles.add(circle0, circle1, circle2, circle3, circle4, circle5)
        # self.add(circles)
        base_0 = circles[0].point_at_angle((90 * 3 - 45) * DEGREES)
        base_1 = circles[1].point_at_angle((90 - 45) * DEGREES)
        line01 = Line(np.array(base_0),
                      np.array(base_1),
                      color=BLACK,
                      stroke_width=3)
        base_0 = circles[0].point_at_angle((90 * 3) * DEGREES)
        base_2 = circles[2].point_at_angle((90) * DEGREES)
        line02 = Line(np.array(base_0),
                      np.array(base_2),
                      color=BLACK,
                      stroke_width=3)
        base_0 = circles[0].point_at_angle((90 * 3 + 45) * DEGREES)
        base_3 = circles[3].point_at_angle((90 + 45) * DEGREES)
        line03 = Line(np.array(base_0),
                      np.array(base_3),
                      color=BLACK,
                      stroke_width=3)
        base_1 = circles[1].point_at_angle((0) * DEGREES)
        base_2 = circles[2].point_at_angle((90 * 2) * DEGREES)
        line12 = Line(np.array(base_1),
                      np.array(base_2),
                      color=BLACK,
                      stroke_width=3)
        base_2 = circles[2].point_at_angle((0) * DEGREES)
        base_3 = circles[3].point_at_angle((90 * 2) * DEGREES)
        line23 = Line(np.array(base_2),
                      np.array(base_3),
                      color=BLACK,
                      stroke_width=3)
        base_2 = circles[2].point_at_angle((90 * 3) * DEGREES)
        base_4 = circles[4].point_at_angle((90 - 45) * DEGREES)
        line24 = Line(np.array(base_2),
                      np.array(base_4),
                      color=BLACK,
                      stroke_width=3)
        base_2 = circles[2].point_at_angle((90 * 3) * DEGREES)
        base_5 = circles[5].point_at_angle((90 + 45) * DEGREES)
        line25 = Line(np.array(base_2),
                      np.array(base_5),
                      color=BLACK,
                      stroke_width=3)
        base_1 = circles[1].point_at_angle((90 * 3) * DEGREES)
        base_4 = circles[4].point_at_angle((90 + 45) * DEGREES)
        line14 = Line(np.array(base_1),
                      np.array(base_4),
                      color=BLACK,
                      stroke_width=3)
        base_3 = circles[3].point_at_angle((90 * 3) * DEGREES)
        base_5 = circles[5].point_at_angle((90 - 45) * DEGREES)
        line35 = Line(np.array(base_3),
                      np.array(base_5),
                      color=BLACK,
                      stroke_width=3)
        base_4 = circles[4].point_at_angle((0) * DEGREES)
        base_5 = circles[5].point_at_angle((90 * 2) * DEGREES)
        line45 = Line(np.array(base_4),
                      np.array(base_5),
                      color=BLACK,
                      stroke_width=3)
        lines.add(line01, line02, line03, line12, line23, line24, line25,
                  line14, line35, line45)
        # self.add(lines)
        nodes, fires = VGroup(), VGroup()
        node0 = Text("0", font="江西拙楷", color=BLACK).scale(0.85)
        node0.move_to(circles[0])
        node1 = Text("1", font="江西拙楷", color=BLACK).scale(0.85)
        node1.move_to(circles[1])
        node2 = Text("2", font="江西拙楷", color=BLACK).scale(0.85)
        node2.move_to(circles[2])
        node3 = Text("3", font="江西拙楷", color=BLACK).scale(0.85)
        node3.move_to(circles[3])
        node4 = Text("4", font="江西拙楷", color=BLACK).scale(0.85)
        node4.move_to(circles[4])
        node5 = Text("5", font="江西拙楷", color=BLACK).scale(0.85)
        node5.move_to(circles[5])
        nodes.add(node0, node1, node2, node3, node4, node5)
        # self.add(nodes)
        fire01 = Text("6", font="思源宋体 Heavy", color="#589dd6").scale(0.5)
        fire01.move_to(lines[0])
        fire02 = Text("1", font="思源宋体 Heavy", color="#589dd6").scale(0.5)
        fire02.move_to(lines[1])
        fire03 = Text("5", font="思源宋体 Heavy", color="#589dd6").scale(0.5)
        fire03.move_to(lines[2])
        fire12 = Text("5", font="思源宋体 Heavy", color="#589dd6").scale(0.5)
        fire12.move_to(lines[3])
        fire23 = Text("5", font="思源宋体 Heavy", color="#589dd6").scale(0.5)
        fire23.move_to(lines[4])
        fire24 = Text("6", font="思源宋体 Heavy", color="#589dd6").scale(0.5)
        fire24.move_to(lines[5])
        fire25 = Text("4", font="思源宋体 Heavy", color="#589dd6").scale(0.5)
        fire25.move_to(lines[6])
        fire14 = Text("3", font="思源宋体 Heavy", color="#589dd6").scale(0.5)
        fire14.move_to(lines[7])
        fire35 = Text("2", font="思源宋体 Heavy", color="#589dd6").scale(0.5)
        fire35.move_to(lines[8])
        fire45 = Text("6", font="思源宋体 Heavy", color="#589dd6").scale(0.5)
        fire45.move_to(lines[9])
        fires.add(fire01, fire02, fire03, fire12, fire23, fire24, fire25,
                  fire14, fire35, fire45)
        # self.add(fires)

        # 动画下方区域
        variable_visited = VGroup()
        for i in range(6):
            if (i == 0):
                variable_visited_tmp = Text("this->visited[0]:",
                                            font="思源宋体 Heavy",
                                            color=BLACK).scale(0.5)
                variable_visited_tmp.move_to(frame_animation).align_to(
                    frame_animation, UP)
                variable_visited_tmp.shift(DOWN * 4.8 + LEFT * 1)
            elif (i == 1):
                variable_visited_tmp = Text("this->visited[1]:",
                                            font="思源宋体 Heavy",
                                            color=BLACK).scale(0.5)
                variable_visited_tmp.move_to(frame_animation).align_to(
                    frame_animation, UP)
                variable_visited_tmp.shift(DOWN * 5.3 + RIGHT * 0.5)
            else:
                variable_visited_tmp = Text("this->visited[" + str(i) + "]:",
                                            font="思源宋体 Heavy",
                                            color=BLACK).scale(0.5)
                variable_visited_tmp.move_to(variable_visited[i - 2])
                variable_visited_tmp.shift(DOWN * 1)
            variable_visited.add(variable_visited_tmp)
        # self.add(variable_visited)
        variable_visited_bool = VGroup()
        for i in range(6):
            bool = Text("false", font="思源宋体 Heavy", color=BLACK).scale(0.45)
            bool.next_to(variable_visited[i], RIGHT, buff=0.1)
            variable_visited_bool.add(bool)
        # self.add(variable_visited_bool)

        # 第二视角整体对象
        variable_right = Rectangle(color="#003472",
                                   height=7.9,
                                   width=3.9,
                                   stroke_width=1,
                                   stroke_opacity=1).move_to(frame_right)
        # self.add(variable_right)
        t3c = {
            "count": "#2932e1",
            "noEdge": RED,
            "EdgeType": "#da1884",
            "VerNum": "#bd874a",
            "vex1": "#589dd6",
            "vex2": "#801dae",
        }
        variable_count = Text("count:",
                              font="思源宋体 Heavy",
                              color=BLACK,
                              t2c=t3c).scale(0.4)
        variable_count.align_to(variable_right,
                                LEFT).align_to(variable_right, UP)
        variable_count.shift(RIGHT * 0.25 + DOWN * 0.12)
        variable_noedge = Text("noEdge = 0x3f3f3f3f(INF)",
                               font="思源宋体 Heavy",
                               color=BLACK,
                               t2c=t3c).scale(0.4)
        variable_noedge.align_to(variable_right,
                                 RIGHT).align_to(variable_right, UP)
        variable_noedge.shift(LEFT * 0.15 + DOWN * 0.1)
        variable_edgetype = Text("EdgeType = int",
                                 font="思源宋体 Heavy",
                                 color=BLACK,
                                 t2c=t3c).scale(0.4)
        variable_edgetype.next_to(variable_count, DOWN,
                                  buff=0.3).shift(RIGHT * 0.4)
        variable_vernum = Text("this->VerNum = 6",
                               font="思源宋体 Heavy",
                               color=BLACK,
                               t2c=t3c).scale(0.4)
        variable_vernum.next_to(variable_noedge, DOWN,
                                buff=0.25).shift(RIGHT * 0.35)
        # self.add(variable_count, variable_noedge, variable_edgetype, variable_vernum)
        variable_count_num = Text("0", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.4)
        variable_count_num.next_to(variable_count, RIGHT, buff=0.1)
        # self.add(variable_count_num)
        variable_vex1, variable_vex2 = VGroup(), VGroup()
        variable_vex1_num, variable_vex2_num = VGroup(), VGroup()
        for i in range(5):
            if (i == 0):
                variable_vex1_tmp = Text("this->TE[0].vex1:",
                                         font="思源宋体 Heavy",
                                         color=BLACK,
                                         t2c=t3c).scale(0.4)
                variable_vex1_tmp.move_to(variable_right).align_to(
                    variable_right, UP)
                variable_vex1_tmp.shift(DOWN * 1.5)
                variable_vex2_tmp = Text("this->TE[0].vex2:",
                                         font="思源宋体 Heavy",
                                         color=BLACK,
                                         t2c=t3c).scale(0.4)
                variable_vex2_tmp.move_to(variable_vex1_tmp)
                variable_vex2_tmp.shift(DOWN * 0.3)
            else:
                variable_vex1_tmp = Text("this->TE[" + str(i) + "].vex1:",
                                         font="思源宋体 Heavy",
                                         color=BLACK,
                                         t2c=t3c).scale(0.4)
                variable_vex1_tmp.move_to(variable_vex2[i - 1])
                variable_vex1_tmp.shift(DOWN * 0.35)
                variable_vex2_tmp = Text("this->TE[" + str(i) + "].vex2:",
                                         font="思源宋体 Heavy",
                                         color=BLACK,
                                         t2c=t3c).scale(0.4)
                variable_vex2_tmp.move_to(variable_vex1_tmp)
                variable_vex2_tmp.shift(DOWN * 0.3)
            variable_vex1.add(variable_vex1_tmp)
            variable_vex2.add(variable_vex2_tmp)
        # self.add(variable_vex1, variable_vex2)
        vex1_list = [0, 2, 5, 3, 1]
        vex2_list = [2, 5, 3, 1, 4]
        for i in range(5):
            num = Text(str(vex1_list[i]),
                       font="思源宋体 Heavy",
                       color=BLACK,
                       t2c=t3c).scale(0.45)
            num.next_to(variable_vex1[i], RIGHT, buff=0.1)
            variable_vex1_num.add(num.copy())
            num = Text(str(vex2_list[i]),
                       font="思源宋体 Heavy",
                       color=BLACK,
                       t2c=t3c).scale(0.45)
            num.next_to(variable_vex2[i], RIGHT, buff=0.1)
            variable_vex2_num.add(num.copy())
        # self.add(variable_vex1_num, variable_vex2_num)
        division_right_one = Rectangle(color="#003472",
                                       height=0.01,
                                       width=3.9,
                                       stroke_width=1,
                                       stroke_opacity=1)
        division_right_two = division_right_one.copy()
        division_right_one.move_to(variable_right).shift(UP * 3)
        division_right_two.move_to(variable_right).shift(DOWN * 1.25)
        # self.add(division_right_one, division_right_two)
        circles_second, nodes_second = circles.copy(), nodes.copy()
        circles_second[0].move_to(variable_right).align_to(
            variable_right, DOWN).align_to(variable_right, LEFT)
        circles_second[0].shift(UP * 1.5 + RIGHT * 0.3)
        circles_second[2].move_to(variable_right).align_to(
            variable_right, DOWN)
        circles_second[2].shift(UP * 1.5)
        circles_second[5].move_to(variable_right).align_to(
            variable_right, DOWN).align_to(variable_right, RIGHT)
        circles_second[5].shift(UP * 1.5 + LEFT * 0.3)
        circles_second[4].move_to(variable_right).align_to(
            variable_right, DOWN).align_to(variable_right, LEFT)
        circles_second[4].shift(UP * 0.3 + RIGHT * 0.3)
        circles_second[1].move_to(variable_right).align_to(
            variable_right, DOWN)
        circles_second[1].shift(UP * 0.3)
        circles_second[3].move_to(variable_right).align_to(
            variable_right, DOWN).align_to(variable_right, RIGHT)
        circles_second[3].shift(UP * 0.3 + LEFT * 0.3)
        circles_second.set_color(WHITE)
        circles_second.set_stroke(BLACK)
        # self.add(circles_second)
        for i in range(6):
            nodes_second[i].move_to(circles_second[i])
        # self.add(nodes_second)
        lines_second, fires_second = VGroup(), VGroup()
        base_left = circles_second[0].point_at_angle((0) * DEGREES)
        base_right = circles_second[2].point_at_angle((90 * 2) * DEGREES)
        lineone = Line(np.array(base_left),
                       np.array(base_right),
                       color=BLACK,
                       stroke_width=3)
        lines_second.add(lineone)
        base_up = circles_second[5].point_at_angle((90 * 3) * DEGREES)
        base_down = circles_second[3].point_at_angle((90) * DEGREES)
        linetwo = Line(np.array(base_up),
                       np.array(base_down),
                       color=BLACK,
                       stroke_width=3)
        line_tmp = lineone.copy()
        line_tmp.next_to(circles_second[2], RIGHT, buff=0)
        lines_second.add(line_tmp.copy())
        lines_second.add(linetwo)
        line_tmp.next_to(circles_second[1], RIGHT, buff=0)
        lines_second.add(line_tmp.copy())
        line_tmp.next_to(circles_second[4], RIGHT, buff=0)
        lines_second.add(line_tmp.copy())
        # self.add(lines_second)
        num = Text("1", font="思源宋体 Heavy", color="#589dd6").scale(0.5)
        num.move_to(lines_second[0]).shift(UP * 0.2)
        fires_second.add(num.copy())
        num = Text("4", font="思源宋体 Heavy", color="#589dd6").scale(0.5)
        num.move_to(lines_second[1]).shift(UP * 0.2)
        fires_second.add(num.copy())
        num = Text("2", font="思源宋体 Heavy", color="#589dd6").scale(0.5)
        num.move_to(lines_second[2]).shift(RIGHT * 0.2)
        fires_second.add(num.copy())
        num = Text("5", font="思源宋体 Heavy", color="#589dd6").scale(0.5)
        num.move_to(lines_second[3]).shift(UP * 0.2)
        fires_second.add(num.copy())
        num = Text("3", font="思源宋体 Heavy", color="#589dd6").scale(0.5)
        num.move_to(lines_second[4]).shift(UP * 0.2)
        fires_second.add(num.copy())
        # self.add(fires_second)

        # 全部视角整体对象
        Camera_left = VGroup()
        Camera_left.add(frame_edge, frame_variable, frame_animation,
                        frame_code, frame_right)
        Camera_left.add(title)
        Camera_left.add(background, codes_primMatrix)
        # Camera_left.add(move_frame)
        Camera_left.add(edge_blocks)
        Camera_left.add(edge_color, edge_text, edge_core)
        Camera_left.add(variable_rectangle)
        Camera_left.add(variable_adjvex, variable_lowcost)
        Camera_left.add(variable_mincost, variable_u, variable_i, variable_j)
        # Camera_left.add(variable_adjvex_num, variable_lowcost_num)
        # Camera_left.add(variable_mincost_num, variable_u_num, variable_i_num, variable_j_num)
        Camera_left.add(division)
        Camera_left.add(circles)
        Camera_left.add(lines)
        Camera_left.add(nodes)
        Camera_left.add(fires)
        Camera_left.add(variable_visited)
        # Camera_left.add(variable_visited_bool)
        Camera_left.add(variable_right)
        Camera_left.add(variable_count, variable_noedge, variable_edgetype,
                        variable_vernum)
        Camera_left.add(variable_count_num)
        Camera_left.add(variable_vex1, variable_vex2)
        Camera_left.add(variable_vex1_num, variable_vex2_num)
        Camera_left.add(division_right_one, division_right_two)
        Camera_left.add(circles_second)
        Camera_left.add(nodes_second)
        Camera_left.add(lines_second)
        Camera_left.add(fires_second)
        self.add(Camera_left)

        # 调成透明
        variable_vex1_num.set_opacity(0)
        variable_vex2_num.set_opacity(0)
        circles_second.set_opacity(0)
        nodes_second.set_opacity(0)
        lines_second.set_opacity(0)
        fires_second.set_opacity(0)

        # 借用 OOP 的方法
        # 面向对象零 (包装代码框移动)
        def code_move(i, *method):
            # 调用方法举例: code_move(1, 0, FadeIn(vec_pos_all))
            self.play(
                *method,
                move_frame.set_width,
                new_ignore_space_len(i),
                move_frame.move_to,
                codes_primMatrix[i],
                move_frame.align_to,
                codes_primMatrix[i],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {
                    "height": 0.165,
                    "stretch": True
                },
                run_time=1.5,
            )
            self.wait()

        '''
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()
        code_move(7)
        self.wait()
        '''

        # 关于颜色的简要概括
        edge_BLUE = "#589DD6"
        edge_ORANGE = "#d7954a"
        edge_RED = "#AD5D67"

        # primMatrix
        self.wait()
        # 代码框开始运作
        self.play(ShowCreation(move_frame), Write(arrow))
        self.wait()
        Camera_left.add(move_frame)
        code_move(8)
        # 出现 u i j 的值
        self.play(FadeIn(variable_u_num), FadeIn(variable_i_num),
                  FadeIn(variable_j_num))
        self.wait()
        Camera_left.add(variable_u_num, variable_i_num, variable_j_num)
        # 左右移动视角
        self.play(Camera_left.shift, LEFT * 4)
        self.wait(3)
        self.play(Camera_left.shift, RIGHT * 4)
        self.wait()
        code_move(9)
        # 开始循环
        for i in range(6):
            if (i != 0):
                variable_i_num_tmp = Text(str(i),
                                          font="思源宋体 Heavy",
                                          color=BLACK).scale(0.45)
                variable_i_num_tmp.next_to(variable_i, RIGHT, buff=0.1)
                self.play(Transform(variable_i_num, variable_i_num_tmp))
            code_move(11)
            self.play(FadeIn(variable_visited_bool[i]))
            self.wait()
            code_move(12)
            self.play(FadeIn(variable_lowcost_num[i]))
            self.wait()
            code_move(9)
        Camera_left.add(variable_visited_bool)
        Camera_left.add(variable_lowcost_num)
        code_move(14)
        code_move(15)
        # 第一个 visit 改成 true，圈圈变红
        bool = Text("true", font="思源宋体 Heavy", color=BLACK).scale(0.45)
        bool.next_to(variable_visited[0], RIGHT, buff=0.1)
        self.play(Transform(variable_visited_bool[0], bool),
                  circles[0].set_color, RED)
        self.wait()
        # -------------------- 针对结点 u=0 --------------------
        variable_i_num_tmp = Text("1", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_i_num_tmp.next_to(variable_i, RIGHT, buff=0.1)
        code_move(16)
        self.play(Transform(variable_i_num, variable_i_num_tmp))  # i 变成 1
        self.wait()
        # 内部第一个循环（结点 0）
        # j=0 [0][0] 不产生内循环
        code_move(18)
        self.play(variable_visited[0].set_color, edge_ORANGE,
                  edge_color[1 * 7 + 2].set_color,
                  edge_ORANGE)  # 第一个 visit 变橙色，对应 edge 变橙色
        self.wait()
        code_move(19)
        # j=1 [0][1] 不产生内循环
        variable_j_num_tmp = Text("1", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[1 * 7 + 2].set_color,
            edge_RED,
            edge_color[1 * 7 + 3].set_color,
            edge_ORANGE,
            edge_color[2 * 7 + 2].set_color,
            edge_ORANGE,
            variable_visited[1].set_color,
            edge_ORANGE,
            variable_visited[0].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # 满足 if 条件
        code_move(21)
        # 不是最小
        code_move(23)
        variable_lowcost_num_tmp = Text("6", font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_lowcost_num_tmp.next_to(variable_lowcost[1], RIGHT, buff=0.1)
        self.play(
            Transform(variable_lowcost_num[1],
                      variable_lowcost_num_tmp.copy()))
        self.wait()
        code_move(24)
        variable_adjvex_num_tmp = Text("0", font="思源宋体 Heavy",
                                       color=BLACK).scale(0.45)
        variable_adjvex_num_tmp.next_to(variable_adjvex[1], RIGHT, buff=0.1)
        # self.play(Transform(variable_adjvex_num[1], variable_adjvex_num_tmp.copy()))
        self.play(ShowCreation(variable_adjvex_num[1]))
        self.wait()
        Camera_left.add(variable_adjvex_num[1])
        # j=2 [0][2] 不产生内循环
        variable_j_num_tmp = Text("2", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[1 * 7 + 3].set_color,
            edge_BLUE,
            edge_color[2 * 7 + 2].set_color,
            edge_BLUE,
            edge_color[1 * 7 + 4].set_color,
            edge_ORANGE,
            edge_color[3 * 7 + 2].set_color,
            edge_ORANGE,
            variable_visited[2].set_color,
            edge_ORANGE,
            variable_visited[1].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # 满足 if 条件
        code_move(21)
        # 不是最小
        code_move(23)
        variable_lowcost_num_tmp = Text("1", font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_lowcost_num_tmp.next_to(variable_lowcost[2], RIGHT, buff=0.1)
        self.play(
            Transform(variable_lowcost_num[2],
                      variable_lowcost_num_tmp.copy()))
        self.wait()
        code_move(24)
        variable_adjvex_num_tmp = Text("0", font="思源宋体 Heavy",
                                       color=BLACK).scale(0.45)
        variable_adjvex_num_tmp.next_to(variable_adjvex[2], RIGHT, buff=0.1)
        # self.play(Transform(variable_adjvex_num[2], variable_adjvex_num_tmp.copy()))
        self.play(ShowCreation(variable_adjvex_num[2]))
        self.wait()
        Camera_left.add(variable_adjvex_num[2])
        # j=3 [0][3] 不产生内循环
        variable_j_num_tmp = Text("3", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[1 * 7 + 4].set_color,
            edge_BLUE,
            edge_color[3 * 7 + 2].set_color,
            edge_BLUE,
            edge_color[1 * 7 + 5].set_color,
            edge_ORANGE,
            edge_color[4 * 7 + 2].set_color,
            edge_ORANGE,
            variable_visited[3].set_color,
            edge_ORANGE,
            variable_visited[2].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # 满足 if 条件
        code_move(21)
        # 不是最小
        code_move(23)
        variable_lowcost_num_tmp = Text("5", font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_lowcost_num_tmp.next_to(variable_lowcost[3], RIGHT, buff=0.1)
        self.play(
            Transform(variable_lowcost_num[3],
                      variable_lowcost_num_tmp.copy()))
        self.wait()
        code_move(24)
        variable_adjvex_num_tmp = Text("0", font="思源宋体 Heavy",
                                       color=BLACK).scale(0.45)
        variable_adjvex_num_tmp.next_to(variable_adjvex[3], RIGHT, buff=0.1)
        # self.play(Transform(variable_adjvex_num[3], variable_adjvex_num_tmp.copy()))
        self.play(ShowCreation(variable_adjvex_num[3]))
        self.wait()
        Camera_left.add(variable_adjvex_num[3])
        # j=4 [0][4] 不产生内循环
        variable_j_num_tmp = Text("4", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[1 * 7 + 5].set_color,
            edge_BLUE,
            edge_color[4 * 7 + 2].set_color,
            edge_BLUE,
            edge_color[1 * 7 + 6].set_color,
            edge_ORANGE,
            edge_color[5 * 7 + 2].set_color,
            edge_ORANGE,
            variable_visited[4].set_color,
            edge_ORANGE,
            variable_visited[3].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # j=5 [0][5] 不产生内循环
        variable_j_num_tmp = Text("5", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[1 * 7 + 6].set_color,
            edge_RED,
            edge_color[5 * 7 + 2].set_color,
            edge_RED,
            edge_color[1 * 7 + 7].set_color,
            edge_ORANGE,
            edge_color[6 * 7 + 2].set_color,
            edge_ORANGE,
            variable_visited[5].set_color,
            edge_ORANGE,
            variable_visited[4].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # j=6 略过，全部颜色复原
        variable_j_num_tmp = Text("6", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[1 * 7 + 7].set_color,
            edge_RED,
            edge_color[6 * 7 + 2].set_color,
            edge_RED,
            variable_visited[5].set_color,
            BLACK,
        )  # 上一个 visit 颜色褪回本色，上一个颜色褪回本色
        self.wait()
        code_move(27)
        self.play(ShowCreation(variable_mincost_num))
        self.wait()
        Camera_left.add(variable_mincost_num)
        # 内部第二个循环（结点 0）
        # j=0
        variable_j_num_tmp = Text("0", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=1
        variable_j_num_tmp = Text("1", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # 满足 if 条件
        code_move(31)
        variable_mincost_num_tmp = Text("6", font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_mincost_num_tmp.next_to(variable_mincost, RIGHT, buff=0.1)
        self.play(
            Transform(variable_mincost_num, variable_mincost_num_tmp.copy()))
        self.wait()
        code_move(32)
        variable_u_num_tmp = Text("1", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_u_num_tmp.next_to(variable_u, RIGHT, buff=0.1)
        self.play(Transform(variable_u_num, variable_u_num_tmp.copy()))
        self.wait()
        # j=2
        variable_j_num_tmp = Text("2", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # 满足 if 条件
        code_move(31)
        variable_mincost_num_tmp = Text("1", font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_mincost_num_tmp.next_to(variable_mincost, RIGHT, buff=0.1)
        self.play(
            Transform(variable_mincost_num, variable_mincost_num_tmp.copy()))
        self.wait()
        code_move(32)
        variable_u_num_tmp = Text("2", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_u_num_tmp.next_to(variable_u, RIGHT, buff=0.1)
        self.play(Transform(variable_u_num, variable_u_num_tmp.copy()))
        self.wait()
        # j=3
        variable_j_num_tmp = Text("3", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=4
        variable_j_num_tmp = Text("4", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=5
        variable_j_num_tmp = Text("5", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=6
        variable_j_num_tmp = Text("6", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        # 内部结尾（转向右侧）
        self.play(Camera_left.shift, LEFT * 4)
        self.wait(2)
        code_move(34)
        self.play(variable_vex1_num[0].set_opacity, 1)
        self.wait()
        code_move(35)
        self.play(variable_vex2_num[0].set_opacity, 1)
        self.wait()
        code_move(36)
        variable_count_num_tmp = Text("1", font="思源宋体 Heavy",
                                      color=BLACK).scale(0.4)
        variable_count_num_tmp.next_to(variable_count, RIGHT, buff=0.1)
        self.play(Transform(variable_count_num, variable_count_num_tmp),
                  circles_second[0].set_opacity, 1,
                  circles_second[2].set_opacity, 1,
                  nodes_second[0].set_opacity, 1, nodes_second[2].set_opacity,
                  1, lines_second[0].set_opacity, 1,
                  fires_second[0].set_opacity, 1)
        self.wait()
        # 转向左侧
        self.play(Camera_left.shift, RIGHT * 4)
        self.wait(2)
        code_move(37)
        variable_lowcost_num_tmp = Text("INF", font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_lowcost_num_tmp.next_to(variable_lowcost[2], RIGHT, buff=0.1)
        self.play(Transform(variable_lowcost_num[2], variable_lowcost_num_tmp))
        self.wait()
        code_move(38)
        bool = Text("true", font="思源宋体 Heavy", color=BLACK).scale(0.45)
        bool.next_to(variable_visited[2], RIGHT, buff=0.1)
        # 圈圈变红，线条变橙色
        self.play(Transform(variable_visited_bool[2], bool),
                  circles[2].set_color, RED, line02.set_color, ORANGE)
        self.wait()
        # -------------------- 针对结点 u=2 --------------------
        variable_i_num_tmp = Text("2", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_i_num_tmp.next_to(variable_i, RIGHT, buff=0.1)
        code_move(16)
        self.play(Transform(variable_i_num, variable_i_num_tmp))  # i 变成 2
        self.wait()
        # 内部第一个循环（结点 2）
        # j=0 [2][0] 不产生内循环
        variable_j_num_tmp = Text("0", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(Transform(variable_j_num,
                            variable_j_num_tmp), variable_visited[0].set_color,
                  edge_ORANGE, edge_color[1 * 7 + 4].set_color, edge_ORANGE,
                  edge_color[3 * 7 + 2].set_color,
                  edge_ORANGE)  # 第一个 visit 变橙色，对应 edge 变橙色
        self.wait()
        code_move(19)
        # j=1 [2][1] 不产生内循环
        variable_j_num_tmp = Text("1", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[1 * 7 + 4].set_color,
            edge_BLUE,
            edge_color[3 * 7 + 2].set_color,
            edge_BLUE,
            edge_color[2 * 7 + 4].set_color,
            edge_ORANGE,
            edge_color[3 * 7 + 3].set_color,
            edge_ORANGE,
            variable_visited[1].set_color,
            edge_ORANGE,
            variable_visited[0].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # ~~~~~ 开始内部 if 语句 ~~~~~
        what_is_j = 1
        adjvex_to = "2"
        lowcost_to = "5"
        # 一轮
        code_move(21)
        # 二轮（过了才可以添加下面的代码）
        code_move(23)
        variable_lowcost_num_tmp = Text(lowcost_to,
                                        font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_lowcost_num_tmp.next_to(variable_lowcost[what_is_j],
                                         RIGHT,
                                         buff=0.1)
        self.play(
            Transform(variable_lowcost_num[what_is_j],
                      variable_lowcost_num_tmp.copy()))
        self.wait()
        code_move(24)
        variable_adjvex_num_tmp = Text(adjvex_to,
                                       font="思源宋体 Heavy",
                                       color=BLACK).scale(0.45)
        variable_adjvex_num_tmp.next_to(variable_adjvex[what_is_j],
                                        RIGHT,
                                        buff=0.1)
        self.play(
            Transform(variable_adjvex_num[what_is_j],
                      variable_adjvex_num_tmp.copy()))  # 出现过
        # self.play(ShowCreation(variable_adjvex_num[what_is_j])) # 没出现过
        self.wait()
        # Camera_left.add(variable_adjvex_num[what_is_j]) # 没出现过
        # ~~~~~ 结束内部 if 语句 ~~~~~
        # j=2 [2][2] 不产生内循环
        variable_j_num_tmp = Text("2", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[2 * 7 + 4].set_color,
            edge_BLUE,
            edge_color[3 * 7 + 3].set_color,
            edge_BLUE,
            edge_color[3 * 7 + 4].set_color,
            edge_ORANGE,
            edge_color[3 * 7 + 4].set_color,
            edge_ORANGE,
            variable_visited[2].set_color,
            edge_ORANGE,
            variable_visited[1].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # j=3 [2][3] 不产生内循环
        variable_j_num_tmp = Text("3", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[3 * 7 + 4].set_color,
            edge_RED,
            edge_color[3 * 7 + 4].set_color,
            edge_RED,
            edge_color[4 * 7 + 4].set_color,
            edge_ORANGE,
            edge_color[3 * 7 + 5].set_color,
            edge_ORANGE,
            variable_visited[3].set_color,
            edge_ORANGE,
            variable_visited[2].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # ~~~~~ 开始内部 if 语句 ~~~~~
        # 一轮
        code_move(21)
        # ~~~~~ 结束内部 if 语句 ~~~~~
        # j=4 [2][4] 不产生内循环
        variable_j_num_tmp = Text("4", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[4 * 7 + 4].set_color,
            edge_BLUE,
            edge_color[3 * 7 + 5].set_color,
            edge_BLUE,
            edge_color[5 * 7 + 4].set_color,
            edge_ORANGE,
            edge_color[3 * 7 + 6].set_color,
            edge_ORANGE,
            variable_visited[4].set_color,
            edge_ORANGE,
            variable_visited[3].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # ~~~~~ 开始内部 if 语句 ~~~~~
        what_is_j = 4
        adjvex_to = "2"
        lowcost_to = "6"
        # 一轮
        code_move(21)
        # 二轮（过了才可以添加下面的代码）
        code_move(23)
        variable_lowcost_num_tmp = Text(lowcost_to,
                                        font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_lowcost_num_tmp.next_to(variable_lowcost[what_is_j],
                                         RIGHT,
                                         buff=0.1)
        self.play(
            Transform(variable_lowcost_num[what_is_j],
                      variable_lowcost_num_tmp.copy()))
        self.wait()
        code_move(24)
        variable_adjvex_num_tmp = Text(adjvex_to,
                                       font="思源宋体 Heavy",
                                       color=BLACK).scale(0.45)
        variable_adjvex_num_tmp.next_to(variable_adjvex[what_is_j],
                                        RIGHT,
                                        buff=0.1)
        # self.play(Transform(variable_adjvex_num[what_is_j], variable_adjvex_num_tmp.copy())) # 出现过
        self.play(ShowCreation(variable_adjvex_num[what_is_j]))  # 没出现过
        self.wait()
        Camera_left.add(variable_adjvex_num[what_is_j])  # 没出现过
        # ~~~~~ 结束内部 if 语句 ~~~~~
        # j=5 [2][5] 不产生内循环
        variable_j_num_tmp = Text("5", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[5 * 7 + 4].set_color,
            edge_BLUE,
            edge_color[3 * 7 + 6].set_color,
            edge_BLUE,
            edge_color[6 * 7 + 4].set_color,
            edge_ORANGE,
            edge_color[3 * 7 + 7].set_color,
            edge_ORANGE,
            variable_visited[5].set_color,
            edge_ORANGE,
            variable_visited[4].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # ~~~~~ 开始内部 if 语句 ~~~~~
        what_is_j = 5
        adjvex_to = "2"
        lowcost_to = "4"
        # 一轮
        code_move(21)
        # 二轮（过了才可以添加下面的代码）
        code_move(23)
        variable_lowcost_num_tmp = Text(lowcost_to,
                                        font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_lowcost_num_tmp.next_to(variable_lowcost[what_is_j],
                                         RIGHT,
                                         buff=0.1)
        self.play(
            Transform(variable_lowcost_num[what_is_j],
                      variable_lowcost_num_tmp.copy()))
        self.wait()
        code_move(24)
        variable_adjvex_num_tmp = Text(adjvex_to,
                                       font="思源宋体 Heavy",
                                       color=BLACK).scale(0.45)
        variable_adjvex_num_tmp.next_to(variable_adjvex[what_is_j],
                                        RIGHT,
                                        buff=0.1)
        # self.play(Transform(variable_adjvex_num[what_is_j], variable_adjvex_num_tmp.copy())) # 出现过
        self.play(ShowCreation(variable_adjvex_num[what_is_j]))  # 没出现过
        self.wait()
        Camera_left.add(variable_adjvex_num[what_is_j])  # 没出现过
        # ~~~~~ 结束内部 if 语句 ~~~~~
        # j=6 略过，全部颜色复原
        variable_j_num_tmp = Text("6", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[6 * 7 + 4].set_color,
            edge_BLUE,
            edge_color[3 * 7 + 7].set_color,
            edge_BLUE,
            variable_visited[5].set_color,
            BLACK,
        )  # 上一个 visit 颜色褪回本色，上一个颜色褪回本色
        self.wait()
        code_move(27)
        variable_mincost_num_tmp = Text("INF", font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_mincost_num_tmp.next_to(variable_mincost, RIGHT, buff=0.1)
        self.play(
            Transform(variable_mincost_num, variable_mincost_num_tmp.copy()))
        self.wait()
        # 内部第二个循环（结点 2）
        # j=0
        variable_j_num_tmp = Text("0", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=1
        variable_j_num_tmp = Text("1", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # ~~~~~ 满足内部 if 语句 ~~~~~
        what_is_u = "1"
        mincost_to = "5"
        code_move(31)
        variable_mincost_num_tmp = Text(mincost_to,
                                        font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_mincost_num_tmp.next_to(variable_mincost, RIGHT, buff=0.1)
        self.play(
            Transform(variable_mincost_num, variable_mincost_num_tmp.copy()))
        self.wait()
        code_move(32)
        variable_u_num_tmp = Text(what_is_u, font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_u_num_tmp.next_to(variable_u, RIGHT, buff=0.1)
        self.play(Transform(variable_u_num, variable_u_num_tmp.copy()))
        self.wait()
        # ~~~~~ 结束内部 if 语句 ~~~~~
        # j=2
        variable_j_num_tmp = Text("2", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=3
        variable_j_num_tmp = Text("3", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=4
        variable_j_num_tmp = Text("4", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=5
        variable_j_num_tmp = Text("5", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # ~~~~~ 满足内部 if 语句 ~~~~~
        what_is_u = "5"
        mincost_to = "4"
        code_move(31)
        variable_mincost_num_tmp = Text(mincost_to,
                                        font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_mincost_num_tmp.next_to(variable_mincost, RIGHT, buff=0.1)
        self.play(
            Transform(variable_mincost_num, variable_mincost_num_tmp.copy()))
        self.wait()
        code_move(32)
        variable_u_num_tmp = Text(what_is_u, font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_u_num_tmp.next_to(variable_u, RIGHT, buff=0.1)
        self.play(Transform(variable_u_num, variable_u_num_tmp.copy()))
        self.wait()
        # ~~~~~ 结束内部 if 语句 ~~~~~
        # j=6
        variable_j_num_tmp = Text("6", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        # 内部结尾（转向右侧）
        self.play(Camera_left.shift, LEFT * 4)
        self.wait(2)
        code_move(34)
        self.play(variable_vex1_num[1].set_opacity, 1)
        self.wait()
        code_move(35)
        self.play(variable_vex2_num[1].set_opacity, 1)
        self.wait()
        code_move(36)
        variable_count_num_tmp = Text("2", font="思源宋体 Heavy",
                                      color=BLACK).scale(0.4)
        variable_count_num_tmp.next_to(variable_count, RIGHT, buff=0.1)
        self.play(Transform(variable_count_num, variable_count_num_tmp),
                  circles_second[5].set_opacity, 1,
                  nodes_second[5].set_opacity, 1, lines_second[1].set_opacity,
                  1, fires_second[1].set_opacity, 1)
        self.wait()
        # 转向左侧
        self.play(Camera_left.shift, RIGHT * 4)
        self.wait(2)
        code_move(37)
        variable_lowcost_num_tmp = Text("INF", font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_lowcost_num_tmp.next_to(variable_lowcost[5], RIGHT, buff=0.1)
        self.play(Transform(variable_lowcost_num[5], variable_lowcost_num_tmp))
        self.wait()
        code_move(38)
        bool = Text("true", font="思源宋体 Heavy", color=BLACK).scale(0.45)
        bool.next_to(variable_visited[5], RIGHT, buff=0.1)
        # 圈圈变红，线条变橙色
        self.play(Transform(variable_visited_bool[5], bool),
                  circles[5].set_color, RED, line25.set_color, ORANGE)
        self.wait()
        # -------------------- 针对结点 u=5 --------------------
        variable_i_num_tmp = Text("3", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_i_num_tmp.next_to(variable_i, RIGHT, buff=0.1)
        code_move(16)
        self.play(Transform(variable_i_num, variable_i_num_tmp))  # i 变成 3
        self.wait()
        # 内部第一个循环（结点 5）
        # j=0 [5][0] 不产生内循环
        variable_j_num_tmp = Text("0", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(Transform(variable_j_num,
                            variable_j_num_tmp), variable_visited[0].set_color,
                  edge_ORANGE, edge_color[1 * 7 + 7].set_color, edge_ORANGE,
                  edge_color[6 * 7 + 2].set_color,
                  edge_ORANGE)  # 第一个 visit 变橙色，对应 edge 变橙色
        self.wait()
        code_move(19)
        # j=1 [5][1] 不产生内循环
        variable_j_num_tmp = Text("1", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[1 * 7 + 7].set_color,
            edge_RED,
            edge_color[6 * 7 + 2].set_color,
            edge_RED,
            edge_color[2 * 7 + 7].set_color,
            edge_ORANGE,
            edge_color[6 * 7 + 3].set_color,
            edge_ORANGE,
            variable_visited[1].set_color,
            edge_ORANGE,
            variable_visited[0].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # j=2 [2][2] 不产生内循环
        variable_j_num_tmp = Text("2", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[2 * 7 + 7].set_color,
            edge_RED,
            edge_color[6 * 7 + 3].set_color,
            edge_RED,
            edge_color[3 * 7 + 7].set_color,
            edge_ORANGE,
            edge_color[6 * 7 + 4].set_color,
            edge_ORANGE,
            variable_visited[2].set_color,
            edge_ORANGE,
            variable_visited[1].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # j=3 [5][3] 不产生内循环
        variable_j_num_tmp = Text("3", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[3 * 7 + 7].set_color,
            edge_BLUE,
            edge_color[6 * 7 + 4].set_color,
            edge_BLUE,
            edge_color[4 * 7 + 7].set_color,
            edge_ORANGE,
            edge_color[6 * 7 + 5].set_color,
            edge_ORANGE,
            variable_visited[3].set_color,
            edge_ORANGE,
            variable_visited[2].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # ~~~~~ 开始内部 if 语句 ~~~~~
        what_is_j = 3
        adjvex_to = "5"
        lowcost_to = "2"
        # 一轮
        code_move(21)
        # 二轮（过了才可以添加下面的代码）
        code_move(23)
        variable_lowcost_num_tmp = Text(lowcost_to,
                                        font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_lowcost_num_tmp.next_to(variable_lowcost[what_is_j],
                                         RIGHT,
                                         buff=0.1)
        self.play(
            Transform(variable_lowcost_num[what_is_j],
                      variable_lowcost_num_tmp.copy()))
        self.wait()
        code_move(24)
        variable_adjvex_num_tmp = Text(adjvex_to,
                                       font="思源宋体 Heavy",
                                       color=BLACK).scale(0.45)
        variable_adjvex_num_tmp.next_to(variable_adjvex[what_is_j],
                                        RIGHT,
                                        buff=0.1)
        self.play(
            Transform(variable_adjvex_num[what_is_j],
                      variable_adjvex_num_tmp.copy()))  # 出现过
        self.wait()
        # ~~~~~ 结束内部 if 语句 ~~~~~
        # j=4 [5][4] 不产生内循环
        variable_j_num_tmp = Text("4", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[4 * 7 + 7].set_color,
            edge_BLUE,
            edge_color[6 * 7 + 5].set_color,
            edge_BLUE,
            edge_color[5 * 7 + 7].set_color,
            edge_ORANGE,
            edge_color[6 * 7 + 6].set_color,
            edge_ORANGE,
            variable_visited[4].set_color,
            edge_ORANGE,
            variable_visited[3].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # ~~~~~ 开始内部 if 语句 ~~~~~
        # 一轮
        code_move(21)
        # ~~~~~ 结束内部 if 语句 ~~~~~
        # j=5 [5][5] 不产生内循环
        variable_j_num_tmp = Text("5", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[5 * 7 + 7].set_color,
            edge_BLUE,
            edge_color[6 * 7 + 6].set_color,
            edge_BLUE,
            edge_color[6 * 7 + 7].set_color,
            edge_ORANGE,
            edge_color[6 * 7 + 7].set_color,
            edge_ORANGE,
            variable_visited[5].set_color,
            edge_ORANGE,
            variable_visited[4].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # j=6 略过，全部颜色复原
        variable_j_num_tmp = Text("6", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[6 * 7 + 7].set_color,
            edge_RED,
            edge_color[6 * 7 + 7].set_color,
            edge_RED,
            variable_visited[5].set_color,
            BLACK,
        )  # 上一个 visit 颜色褪回本色，上一个颜色褪回本色
        self.wait()
        code_move(27)
        variable_mincost_num_tmp = Text("INF", font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_mincost_num_tmp.next_to(variable_mincost, RIGHT, buff=0.1)
        self.play(
            Transform(variable_mincost_num, variable_mincost_num_tmp.copy()))
        self.wait()
        # 内部第二个循环（结点 5）
        # j=0
        variable_j_num_tmp = Text("0", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=1
        variable_j_num_tmp = Text("1", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # ~~~~~ 满足内部 if 语句 ~~~~~
        what_is_u = "1"
        mincost_to = "5"
        code_move(31)
        variable_mincost_num_tmp = Text(mincost_to,
                                        font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_mincost_num_tmp.next_to(variable_mincost, RIGHT, buff=0.1)
        self.play(
            Transform(variable_mincost_num, variable_mincost_num_tmp.copy()))
        self.wait()
        code_move(32)
        variable_u_num_tmp = Text(what_is_u, font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_u_num_tmp.next_to(variable_u, RIGHT, buff=0.1)
        self.play(Transform(variable_u_num, variable_u_num_tmp.copy()))
        self.wait()
        # ~~~~~ 结束内部 if 语句 ~~~~~
        # j=2
        variable_j_num_tmp = Text("2", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=3
        variable_j_num_tmp = Text("3", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # ~~~~~ 满足内部 if 语句 ~~~~~
        what_is_u = "3"
        mincost_to = "2"
        code_move(31)
        variable_mincost_num_tmp = Text(mincost_to,
                                        font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_mincost_num_tmp.next_to(variable_mincost, RIGHT, buff=0.1)
        self.play(
            Transform(variable_mincost_num, variable_mincost_num_tmp.copy()))
        self.wait()
        code_move(32)
        variable_u_num_tmp = Text(what_is_u, font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_u_num_tmp.next_to(variable_u, RIGHT, buff=0.1)
        self.play(Transform(variable_u_num, variable_u_num_tmp.copy()))
        self.wait()
        # ~~~~~ 结束内部 if 语句 ~~~~~
        # j=4
        variable_j_num_tmp = Text("4", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=5
        variable_j_num_tmp = Text("5", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=6
        variable_j_num_tmp = Text("6", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        # 内部结尾（转向右侧）
        self.play(Camera_left.shift, LEFT * 4)
        self.wait(2)
        code_move(34)
        self.play(variable_vex1_num[2].set_opacity, 1)
        self.wait()
        code_move(35)
        self.play(variable_vex2_num[2].set_opacity, 1)
        self.wait()
        code_move(36)
        variable_count_num_tmp = Text("3", font="思源宋体 Heavy",
                                      color=BLACK).scale(0.4)
        variable_count_num_tmp.next_to(variable_count, RIGHT, buff=0.1)
        self.play(Transform(variable_count_num, variable_count_num_tmp),
                  circles_second[3].set_opacity, 1,
                  nodes_second[3].set_opacity, 1, lines_second[2].set_opacity,
                  1, fires_second[2].set_opacity, 1)
        self.wait()
        # 转向左侧
        self.play(Camera_left.shift, RIGHT * 4)
        self.wait(2)
        code_move(37)
        variable_lowcost_num_tmp = Text("INF", font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_lowcost_num_tmp.next_to(variable_lowcost[3], RIGHT, buff=0.1)
        self.play(Transform(variable_lowcost_num[3], variable_lowcost_num_tmp))
        self.wait()
        code_move(38)
        bool = Text("true", font="思源宋体 Heavy", color=BLACK).scale(0.45)
        bool.next_to(variable_visited[3], RIGHT, buff=0.1)
        # 圈圈变红，线条变橙色
        self.play(Transform(variable_visited_bool[3], bool),
                  circles[3].set_color, RED, line35.set_color, ORANGE)
        self.wait()
        # -------------------- 针对结点 u=3 --------------------
        variable_i_num_tmp = Text("4", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_i_num_tmp.next_to(variable_i, RIGHT, buff=0.1)
        code_move(16)
        self.play(Transform(variable_i_num, variable_i_num_tmp))  # i 变成 4
        self.wait()
        # 内部第一个循环（结点 3）
        # j=0 [3][0] 不产生内循环
        variable_j_num_tmp = Text("0", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(Transform(variable_j_num,
                            variable_j_num_tmp), variable_visited[0].set_color,
                  edge_ORANGE, edge_color[1 * 7 + 5].set_color, edge_ORANGE,
                  edge_color[4 * 7 + 2].set_color,
                  edge_ORANGE)  # 第一个 visit 变橙色，对应 edge 变橙色
        self.wait()
        code_move(19)
        # j=1 [3][1] 不产生内循环
        variable_j_num_tmp = Text("1", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[1 * 7 + 5].set_color,
            edge_BLUE,
            edge_color[4 * 7 + 2].set_color,
            edge_BLUE,
            edge_color[2 * 7 + 5].set_color,
            edge_ORANGE,
            edge_color[4 * 7 + 3].set_color,
            edge_ORANGE,
            variable_visited[1].set_color,
            edge_ORANGE,
            variable_visited[0].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # j=2 [3][2] 不产生内循环
        variable_j_num_tmp = Text("2", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[2 * 7 + 5].set_color,
            edge_RED,
            edge_color[4 * 7 + 3].set_color,
            edge_RED,
            edge_color[3 * 7 + 5].set_color,
            edge_ORANGE,
            edge_color[4 * 7 + 4].set_color,
            edge_ORANGE,
            variable_visited[2].set_color,
            edge_ORANGE,
            variable_visited[1].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # j=3 [3][3] 不产生内循环
        variable_j_num_tmp = Text("3", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[3 * 7 + 5].set_color,
            edge_BLUE,
            edge_color[4 * 7 + 4].set_color,
            edge_BLUE,
            edge_color[4 * 7 + 5].set_color,
            edge_ORANGE,
            edge_color[4 * 7 + 5].set_color,
            edge_ORANGE,
            variable_visited[3].set_color,
            edge_ORANGE,
            variable_visited[2].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # j=4 [3][4] 不产生内循环
        variable_j_num_tmp = Text("4", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[4 * 7 + 5].set_color,
            edge_RED,
            edge_color[4 * 7 + 5].set_color,
            edge_RED,
            edge_color[5 * 7 + 5].set_color,
            edge_ORANGE,
            edge_color[4 * 7 + 6].set_color,
            edge_ORANGE,
            variable_visited[4].set_color,
            edge_ORANGE,
            variable_visited[3].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # j=5 [3][5] 不产生内循环
        variable_j_num_tmp = Text("5", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[5 * 7 + 5].set_color,
            edge_RED,
            edge_color[4 * 7 + 6].set_color,
            edge_RED,
            edge_color[6 * 7 + 5].set_color,
            edge_ORANGE,
            edge_color[4 * 7 + 7].set_color,
            edge_ORANGE,
            variable_visited[5].set_color,
            edge_ORANGE,
            variable_visited[4].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # j=6 略过，全部颜色复原
        variable_j_num_tmp = Text("6", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[6 * 7 + 5].set_color,
            edge_BLUE,
            edge_color[4 * 7 + 7].set_color,
            edge_BLUE,
            variable_visited[5].set_color,
            BLACK,
        )  # 上一个 visit 颜色褪回本色，上一个颜色褪回本色
        self.wait()
        code_move(27)
        variable_mincost_num_tmp = Text("INF", font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_mincost_num_tmp.next_to(variable_mincost, RIGHT, buff=0.1)
        self.play(
            Transform(variable_mincost_num, variable_mincost_num_tmp.copy()))
        self.wait()
        # 内部第二个循环（结点 3）
        # j=0
        variable_j_num_tmp = Text("0", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=1
        variable_j_num_tmp = Text("1", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # ~~~~~ 满足内部 if 语句 ~~~~~
        what_is_u = "1"
        mincost_to = "5"
        code_move(31)
        variable_mincost_num_tmp = Text(mincost_to,
                                        font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_mincost_num_tmp.next_to(variable_mincost, RIGHT, buff=0.1)
        self.play(
            Transform(variable_mincost_num, variable_mincost_num_tmp.copy()))
        self.wait()
        code_move(32)
        variable_u_num_tmp = Text(what_is_u, font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_u_num_tmp.next_to(variable_u, RIGHT, buff=0.1)
        self.play(Transform(variable_u_num, variable_u_num_tmp.copy()))
        self.wait()
        # ~~~~~ 结束内部 if 语句 ~~~~~
        # j=2
        variable_j_num_tmp = Text("2", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=3
        variable_j_num_tmp = Text("3", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=4
        variable_j_num_tmp = Text("4", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=5
        variable_j_num_tmp = Text("5", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=6
        variable_j_num_tmp = Text("6", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        # 内部结尾（转向右侧）
        self.play(Camera_left.shift, LEFT * 4)
        self.wait(2)
        code_move(34)
        self.play(variable_vex1_num[3].set_opacity, 1)
        self.wait()
        code_move(35)
        self.play(variable_vex2_num[3].set_opacity, 1)
        self.wait()
        code_move(36)
        variable_count_num_tmp = Text("4", font="思源宋体 Heavy",
                                      color=BLACK).scale(0.4)
        variable_count_num_tmp.next_to(variable_count, RIGHT, buff=0.1)
        self.play(Transform(variable_count_num, variable_count_num_tmp),
                  circles_second[1].set_opacity, 1,
                  nodes_second[1].set_opacity, 1, lines_second[3].set_opacity,
                  1, fires_second[3].set_opacity, 1)
        self.wait()
        # 转向左侧
        self.play(Camera_left.shift, RIGHT * 4)
        self.wait(2)
        code_move(37)
        variable_lowcost_num_tmp = Text("INF", font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_lowcost_num_tmp.next_to(variable_lowcost[1], RIGHT, buff=0.1)
        self.play(Transform(variable_lowcost_num[1], variable_lowcost_num_tmp))
        self.wait()
        code_move(38)
        bool = Text("true", font="思源宋体 Heavy", color=BLACK).scale(0.45)
        bool.next_to(variable_visited[1], RIGHT, buff=0.1)
        # 圈圈变红，线条变橙色
        self.play(Transform(variable_visited_bool[1], bool),
                  circles[1].set_color, RED, line12.set_color, ORANGE)
        self.wait()
        # -------------------- 针对结点 u=1 --------------------
        variable_i_num_tmp = Text("5", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_i_num_tmp.next_to(variable_i, RIGHT, buff=0.1)
        code_move(16)
        self.play(Transform(variable_i_num, variable_i_num_tmp))  # i 变成 5
        self.wait()
        # 内部第一个循环（结点 1）
        # j=0 [1][0] 不产生内循环
        variable_j_num_tmp = Text("0", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(Transform(variable_j_num,
                            variable_j_num_tmp), variable_visited[0].set_color,
                  edge_ORANGE, edge_color[1 * 7 + 3].set_color, edge_ORANGE,
                  edge_color[2 * 7 + 2].set_color,
                  edge_ORANGE)  # 第一个 visit 变橙色，对应 edge 变橙色
        self.wait()
        code_move(19)
        # j=1 [1][1] 不产生内循环
        variable_j_num_tmp = Text("1", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[1 * 7 + 3].set_color,
            edge_BLUE,
            edge_color[2 * 7 + 2].set_color,
            edge_BLUE,
            edge_color[2 * 7 + 3].set_color,
            edge_ORANGE,
            edge_color[2 * 7 + 3].set_color,
            edge_ORANGE,
            variable_visited[1].set_color,
            edge_ORANGE,
            variable_visited[0].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # j=2 [1][2] 不产生内循环
        variable_j_num_tmp = Text("2", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[2 * 7 + 3].set_color,
            edge_RED,
            edge_color[2 * 7 + 3].set_color,
            edge_RED,
            edge_color[3 * 7 + 3].set_color,
            edge_ORANGE,
            edge_color[2 * 7 + 4].set_color,
            edge_ORANGE,
            variable_visited[2].set_color,
            edge_ORANGE,
            variable_visited[1].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # j=3 [1][3] 不产生内循环
        variable_j_num_tmp = Text("3", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[3 * 7 + 3].set_color,
            edge_BLUE,
            edge_color[2 * 7 + 4].set_color,
            edge_BLUE,
            edge_color[4 * 7 + 3].set_color,
            edge_ORANGE,
            edge_color[2 * 7 + 5].set_color,
            edge_ORANGE,
            variable_visited[3].set_color,
            edge_ORANGE,
            variable_visited[2].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # j=4 [1][4] 不产生内循环
        variable_j_num_tmp = Text("4", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[4 * 7 + 3].set_color,
            edge_RED,
            edge_color[2 * 7 + 5].set_color,
            edge_RED,
            edge_color[5 * 7 + 3].set_color,
            edge_ORANGE,
            edge_color[2 * 7 + 6].set_color,
            edge_ORANGE,
            variable_visited[4].set_color,
            edge_ORANGE,
            variable_visited[3].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # ~~~~~ 开始内部 if 语句 ~~~~~
        what_is_j = 4
        adjvex_to = "1"
        lowcost_to = "3"
        # 一轮
        code_move(21)
        # 二轮（过了才可以添加下面的代码）
        code_move(23)
        variable_lowcost_num_tmp = Text(lowcost_to,
                                        font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_lowcost_num_tmp.next_to(variable_lowcost[what_is_j],
                                         RIGHT,
                                         buff=0.1)
        self.play(
            Transform(variable_lowcost_num[what_is_j],
                      variable_lowcost_num_tmp.copy()))
        self.wait()
        code_move(24)
        variable_adjvex_num_tmp = Text(adjvex_to,
                                       font="思源宋体 Heavy",
                                       color=BLACK).scale(0.45)
        variable_adjvex_num_tmp.next_to(variable_adjvex[what_is_j],
                                        RIGHT,
                                        buff=0.1)
        self.play(
            Transform(variable_adjvex_num[what_is_j],
                      variable_adjvex_num_tmp.copy()))  # 出现过
        self.wait()
        # ~~~~~ 结束内部 if 语句 ~~~~~
        # j=5 [1][5] 不产生内循环
        variable_j_num_tmp = Text("5", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[5 * 7 + 3].set_color,
            edge_BLUE,
            edge_color[2 * 7 + 6].set_color,
            edge_BLUE,
            edge_color[6 * 7 + 3].set_color,
            edge_ORANGE,
            edge_color[2 * 7 + 7].set_color,
            edge_ORANGE,
            variable_visited[5].set_color,
            edge_ORANGE,
            variable_visited[4].set_color,
            BLACK,
        )  # 下一个 visit 变橙色 + 上一个 visit 颜色褪回本色，对应 edge 变橙色 + 上一个颜色褪回本色
        self.wait()
        code_move(19)
        # j=6 略过，全部颜色复原
        variable_j_num_tmp = Text("6", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(18)
        self.play(
            Transform(variable_j_num, variable_j_num_tmp),
            edge_color[6 * 7 + 3].set_color,
            edge_RED,
            edge_color[2 * 7 + 7].set_color,
            edge_RED,
            variable_visited[5].set_color,
            BLACK,
        )  # 上一个 visit 颜色褪回本色，上一个颜色褪回本色
        self.wait()
        code_move(27)
        variable_mincost_num_tmp = Text("INF", font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_mincost_num_tmp.next_to(variable_mincost, RIGHT, buff=0.1)
        self.play(
            Transform(variable_mincost_num, variable_mincost_num_tmp.copy()))
        self.wait()
        # 内部第二个循环（结点 1）
        # j=0
        variable_j_num_tmp = Text("0", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=1
        variable_j_num_tmp = Text("1", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=2
        variable_j_num_tmp = Text("2", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=3
        variable_j_num_tmp = Text("3", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=4
        variable_j_num_tmp = Text("4", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # ~~~~~ 满足内部 if 语句 ~~~~~
        what_is_u = "4"
        mincost_to = "3"
        code_move(31)
        variable_mincost_num_tmp = Text(mincost_to,
                                        font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_mincost_num_tmp.next_to(variable_mincost, RIGHT, buff=0.1)
        self.play(
            Transform(variable_mincost_num, variable_mincost_num_tmp.copy()))
        self.wait()
        code_move(32)
        variable_u_num_tmp = Text(what_is_u, font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_u_num_tmp.next_to(variable_u, RIGHT, buff=0.1)
        self.play(Transform(variable_u_num, variable_u_num_tmp.copy()))
        self.wait()
        # ~~~~~ 结束内部 if 语句 ~~~~~
        # j=5
        variable_j_num_tmp = Text("5", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        code_move(29)
        # j=6
        variable_j_num_tmp = Text("6", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_j_num_tmp.next_to(variable_j, RIGHT, buff=0.1)
        code_move(28)
        self.play(Transform(variable_j_num, variable_j_num_tmp))
        self.wait()
        # 内部结尾（转向右侧）
        self.play(Camera_left.shift, LEFT * 4)
        self.wait(2)
        code_move(34)
        self.play(variable_vex1_num[4].set_opacity, 1)
        self.wait()
        code_move(35)
        self.play(variable_vex2_num[4].set_opacity, 1)
        self.wait()
        code_move(36)
        variable_count_num_tmp = Text("5", font="思源宋体 Heavy",
                                      color=BLACK).scale(0.4)
        variable_count_num_tmp.next_to(variable_count, RIGHT, buff=0.1)
        self.play(Transform(variable_count_num, variable_count_num_tmp),
                  circles_second[4].set_opacity, 1,
                  nodes_second[4].set_opacity, 1, lines_second[4].set_opacity,
                  1, fires_second[4].set_opacity, 1)
        self.wait()
        # 转向左侧
        self.play(Camera_left.shift, RIGHT * 4)
        self.wait(2)
        code_move(37)
        variable_lowcost_num_tmp = Text("INF", font="思源宋体 Heavy",
                                        color=BLACK).scale(0.45)
        variable_lowcost_num_tmp.next_to(variable_lowcost[4], RIGHT, buff=0.1)
        self.play(Transform(variable_lowcost_num[4], variable_lowcost_num_tmp))
        self.wait()
        code_move(38)
        bool = Text("true", font="思源宋体 Heavy", color=BLACK).scale(0.45)
        bool.next_to(variable_visited[4], RIGHT, buff=0.1)
        # 圈圈变红，线条变橙色
        self.play(Transform(variable_visited_bool[4], bool),
                  circles[4].set_color, RED, line14.set_color, ORANGE)
        self.wait()
        # -------------------- 最后结尾 --------------------
        variable_i_num_tmp = Text("6", font="思源宋体 Heavy",
                                  color=BLACK).scale(0.45)
        variable_i_num_tmp.next_to(variable_i, RIGHT, buff=0.1)
        code_move(16)
        self.play(Transform(variable_i_num, variable_i_num_tmp))  # i 变成 6
        self.wait()
        # 最后一行代码
        code_move(40)
        self.play(Camera_left.shift, LEFT * 4)
        self.wait(2)
        self.play(FadeOut(move_frame), FadeOut(arrow), line01.set_opacity, 0,
                  line03.set_opacity, 0, line23.set_opacity, 0,
                  line24.set_opacity, 0, line45.set_opacity, 0,
                  fire01.set_opacity, 0, fire03.set_opacity, 0,
                  fire23.set_opacity, 0, fire24.set_opacity, 0,
                  fire45.set_opacity, 0)
        self.wait(2)
