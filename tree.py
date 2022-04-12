from manimlib.imports import *
from manim_tuan import *
import math

"""
TODO
0: 代码加颜色 | 不同 base_stack 改颜色
1: 选择性补充 levelOrderCreate 函数的代码(因为书本没有加入 层次创建二叉树 的函数)
2: 理清逻辑, 由于使用变量的数量太多了, 且很多顺序都不能轻易更改(如 stack_i 、count 与 mod 等变量), 画一棵清晰的逻辑树用于解释
"""

"""
BUG
1: 全部函数仅适合满二叉树的情况
"""

# preOrder
# inOrder
# postOrder
# levelOrderTraverse
# preOrderCreate
# levelOrderCreate

# 自定义结点信息(结点个数必须 大于 1 小于 15 )
# 因为层次(遍历 | 创建)所用的是非递归代码, 其他(遍历 | 创建)所用的是递归代码, 二者各框架占用空间与内容不一致, 因此分区为两个类
# tree 类        1: 前序顺序建立二叉树  2: 前序遍历二叉树  3: 中序遍历二叉树  4: 后序遍历二叉树
# tree_level 类  1: 层次建立二叉树   2: 层次遍历二叉树
chose = 2
flag = "*"  # 空结点的表示方法
# nodeList = "ABD**E**CF**G**"  # 前序顺序建立二叉树满结点
# biTree = BiTree(['A', 'B', 'D', '*', '*', 'E', '*', '*', 'C', 'F', '*', '*', 'G', '*', '*'])
nodeList = "ABCDEFG*"  # 层次建立二叉树满结点
# biTree = BiTree(['A', 'B', 'C', 'D', 'E', 'F', 'G', '*'])


# 预处理
def Pretreatment():
    noed_nums = 0  # 结点数
    node_full = 0  # 树的类型:  1: 满结点为 3   2: 满结点为 7   3: 满结点为 15
    for node in nodeList:
        if node != flag:
            noed_nums += 1
    if noed_nums <= 3:
        node_full = 3
    elif noed_nums <= 7:
        node_full = 7
    elif noed_nums <= 15:
        node_full = 15
    return noed_nums, node_full


# 结点数 树的类型
noed_nums, node_full = Pretreatment()
# 结点层数
node_layers = math.log((node_full + 1), 2)
node_layers = (int)(float(node_layers))
# 所有结点 当前结点 当前结点元素 当前nodeList[i]的元素 表示第 i 层堆栈长方块  move_frame 是否已经出现
nodeList_unzip = [*nodeList]
pre_list = nodeList_unzip
count = 1
index_tmp = 0
num_index = 0
stack_i = 0
turn_on = False

# 自定义函数代码(若需更改代码，其行数与格式必须保持一致)
preOrder_codes = [
    # "void BinaryLinkList<elemType>::preOrder(Node *t) const",
    "void preOrder(Node *t) const",
    "{",
    "   if (t)",
    "   {",
    "      cout << t->data << ' ';",
    "      preOrder(t->left);",
    "      preOrder(t->right);",
    "   }",
    "}",
]
inOrder_codes = [
    # "void BinaryLinkList<elemType>::inOrder(Node *t) const",
    "void inOrder(Node *t) const",
    "{",
    "   if (t)",
    "   {",
    "      inOrder(t->left);",
    "      cout << t->data << ' ';",
    "      inOrder(t->right);",
    "   }",
    "}",
]
postOrder_codes = [
    # "void BinaryLinkList<elemType>::postOrder(Node *t) const",
    "void postOrder(Node *t) const",
    "{",
    "   if (t)",
    "   {",
    "      postOrder(t->left);",
    "      postOrder(t->right);",
    "      cout << t->data << ' ';",
    "   }",
    "}",
]
levelOrderTraverse_codes = [
    # "void BinaryLinkList<elemType>::levelOrderTraverse() const",
    "void levelOrderTraverse() const",
    "{",
    "   queue<Node*> que;",
    "   Node* p = root;",
    "   if (p)",
    "      que.push(p);",
    "   while (!que.empty())",
    "   {",
    "      p = que.front();",
    "      que.pop();",
    "      cout << p->data << ' ';",
    "      if (p->left != NULL)",
    "         que.push(p->left);",
    "      if (p->right!= NULL)",
    "         que.push(p->right);",
    "   }",
    "}",
]
preOrderCreate_codes = [
    # "void BinaryLinkList<elemType>::preOrderCreate(elemType flag, Node *&t)",
    "void preOrderCreate(elemType flag, Node *&t)",
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
levelOrderCreate_codes = [
    # "void BinaryLinkList<elemType>::levelOrderCreate(elemType flag)"
    "void levelOrderCreate(elemType flag)"
    "{"
    "   queue<Node *> que;"
    "   Node *p;"
    "   elemType value, ldata, rdata;"
    "   cin >> value;"
    "   if (value != flag)"
    "      root = new Node(value);"
    "   que.push(root);"
    "   while (!que.empty())"
    "   {"
    "      p = que.front();"
    "      que.pop();"
    "      cin >> ldata >> rdata;"
    "      if (ldata != flag)"
    "         que.push(p->left = new Node(ldata));"
    "      if (rdata != flag)"
    "         que.push(p->right = new Node(rdata));"
    "   }"
    "}"
]


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.leftChild = None
        self.rightChild = None


class BiTree:
    def __init__(self, pre_list, chose, play):
        """
        1: 前序顺序建立二叉树
        2: 层次建立二叉树
        3: pre_list 按照规定顺序且 pre_list[0] 不能为 '*'(flag)
        """
        self.treeNode = TreeNode(None)
        self.pre_list = pre_list
        if flag == 1:
            self.treeNode = self.__preOrderCreate(self.treeNode)
        elif flag == 2:
            self.treeNode = self.__levelOrderCreate(self.treeNode)
        # self.count = 0

    def __preOrderCreate(self, node):
        value = self.pre_list[0]
        if len(self.pre_list) > 1:
            self.pre_list = self.pre_list[1:]

        if value == flag:  # 当遇到 flag 时，令树的根节点为 None，从而结束该分支的递归
            node = None
        else:
            node = TreeNode(value)
            node.leftChild = self.__preOrderCreate(node.leftChild)
            node.rightChild = self.__preOrderCreate(node.rightChild)
        return node

    def __levelOrderCreate(self, node):
        data = self.pre_list[0]
        node = TreeNode(data)
        Nodes = [node]
        i = 1
        for data in Nodes:
            if data != None:
                data.leftChild = (
                    TreeNode(self.pre_list[i]) if self.pre_list[i] != flag else None
                )
                Nodes.append(data.leftChild)
                i += 1
                if i == len(self.pre_list):
                    return node
                data.rightChild = (
                    TreeNode(self.pre_list[i]) if self.pre_list[i] != flag else None
                )
                i += 1
                Nodes.append(data.rightChild)
                if i == len(self.pre_list):
                    return node

    def preTraverse(self):
        """
        前序遍历
        """
        self.__preTraverse(self.treeNode)

    def __preTraverse(self, node):
        if node != None:
            print(node.value, end="")
            self.__preTraverse(node.leftChild)
            self.__preTraverse(node.rightChild)

    def midTraverse(self):
        """
        中序遍历
        """
        self.__midTraverse(self.treeNode)

    def __midTraverse(self, node):
        if node != None:
            self.__midTraverse(node.leftChild)
            print(node.value, end="")
            self.__midTraverse(node.rightChild)

    def postTraverse(self):
        """
        后序遍历
        """
        self.__postTraverse(self.treeNode)

    def __postTraverse(self, node):
        if node != None:
            self.__postTraverse(node.leftChild)
            self.__postTraverse(node.rightChild)
            print(node.value, end="")

    def levelOrderTraverse(self):
        """
        层次遍历
        """
        self.__levelOrderTraverse(self.treeNode)

    def __levelOrderTraverse(self, node):
        if node != None:
            pass
        queue = []
        queue.append(node)
        last = node
        level = 1
        print("Level " + str(level) + ":", end=" ")
        while queue:
            node = queue.pop(0)
            print(node.value, end=" ")
            if node.leftChild:
                nlast = node.leftChild
                queue.append(node.leftChild)
            if node.rightChild:
                nlast = node.rightChild
                queue.append(node.rightChild)
            if node == last and queue:
                last = nlast
                print()
                level += 1
                print("Level " + str(level) + ":", end=" ")


class Scene_White(Scene):
    CONFIG = {"camera_config": {"background_color": WHITE, "use_plot_depth": True,}}


class tree(Scene_White):
    def construct(self):
        global count, pre_list, index_tmp, num_index, stack_i
        # Frame 整体框架
        # height: 8  *  width: 14.2
        frame_code = Rectangle(
            color=BLUE, stroke_opacity=0, height=4, width=7.1,
        ).to_corner(UR, buff=0)
        frame_variable = Rectangle(
            color=RED, stroke_opacity=0, height=4, width=7.1,
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
        # 基准圆形
        circle_base = Circle(
            radius=0.6, stroke_width=8, stroke_color=BLACK, stroke_opacity=1
        )
        # 基准大小
        narrow_multiple = circle_base.get_width()  # 直径
        # assert circle_base.get_width() * 2 == 1
        # 结点集合
        base_all = VGroup()
        for i in range(node_full):
            base_tmp = circle_base.copy()
            base_all.add(base_tmp)
        # 结点元素集合
        element_all = VGroup()
        for i in range(len(pre_list)):
            element_tmp = Text(pre_list[i], font="江西拙楷", color=BLACK).scale(1.5).copy()
            if pre_list[i] != flag:
                element_all.add(element_tmp)
        # 结点连线集合
        line_all = VGroup()

        # 各结点的位置
        if node_full == 3:
            pass
        elif node_full == 7:
            # 结点 0 的位置
            base_all[0].move_to(frame_animation).align_to(frame_animation, UP).shift(
                DOWN * 0.8
            )
            # 结点 1 结点 2 的位置
            base_all[1].next_to(base_all[0], DOWN, buff=1).shift(LEFT * 1.5)
            # 结点 0 1 连线
            base_0 = base_all[0].point_at_angle(250 * DEGREES)
            base_1 = base_all[1].point_at_angle(90 * DEGREES)
            line_0_1 = Line(
                np.array(base_0), np.array(base_1), color=BLACK, stroke_width=5
            )
            base_all[2].next_to(base_all[0], DOWN, buff=1).shift(RIGHT * 1.5)
            # 结点 0 2 连线
            base_0 = base_all[0].point_at_angle(290 * DEGREES)
            base_2 = base_all[2].point_at_angle(90 * DEGREES)
            line_0_2 = Line(
                np.array(base_0), np.array(base_2), color=BLACK, stroke_width=5
            )
            # 结点 3 结点 4 的位置
            base_all[3].next_to(base_all[1], DOWN, buff=1).shift(LEFT * 1.2)
            # 结点 1 3 连线
            base_1 = base_all[1].point_at_angle(240 * DEGREES)
            base_3 = base_all[3].point_at_angle(90 * DEGREES)
            line_1_3 = Line(
                np.array(base_1), np.array(base_3), color=BLACK, stroke_width=5
            )
            base_all[4].next_to(base_all[1], DOWN, buff=1).shift(RIGHT * 0.7)
            # 结点 1 4 连线
            base_1 = base_all[1].point_at_angle(290 * DEGREES)
            base_4 = base_all[4].point_at_angle(90 * DEGREES)
            line_1_4 = Line(
                np.array(base_1), np.array(base_4), color=BLACK, stroke_width=5
            )
            # 结点 5 结点 6 的位置
            base_all[5].next_to(base_all[2], DOWN, buff=1).shift(LEFT * 0.7)
            # 结点 2 5 连线
            base_2 = base_all[2].point_at_angle(250 * DEGREES)
            base_5 = base_all[5].point_at_angle(90 * DEGREES)
            line_2_5 = Line(
                np.array(base_2), np.array(base_5), color=BLACK, stroke_width=5
            )
            base_all[6].next_to(base_all[2], DOWN, buff=1).shift(RIGHT * 1.2)
            # 结点 2 6 连线
            base_2 = base_all[2].point_at_angle(300 * DEGREES)
            base_6 = base_all[6].point_at_angle(90 * DEGREES)
            line_2_6 = Line(
                np.array(base_2), np.array(base_6), color=BLACK, stroke_width=5
            )
            # 集合
            line_all = VGroup(
                line_0_1, line_0_2, line_1_3, line_1_4, line_2_5, line_2_6
            )
        elif node_full == 15:
            pass

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
        background.set_height(3.5, stretch=True).set_width(6.5, stretch=True)
        background.move_to(frame_code)

        # frame_code 背景 + 代码 + 移动框
        class codeline_preOrderCreate(Text):
            CONFIG = {
                "t2c": {".": WHITE, "t.": BLACK},  # t. 需要和 . 区分开
                "size": 0.50,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        class codeline_preOrder(Text):
            CONFIG = {
                "t2c": {".": WHITE, "t.": BLACK},
                "size": 0.65,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        class codeline_inOrder(Text):
            CONFIG = {
                "t2c": {".": WHITE, "t.": BLACK},
                "size": 0.65,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        class codeline_postOrder(Text):
            CONFIG = {
                "t2c": {".": WHITE, "t.": BLACK},
                "size": 0.65,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        def ignore_space_len(code, str, num):
            origin_len = len(code)
            begin = origin_len - 1
            record = 0
            if str == "pr":
                temp_codes = preOrder_codes
            elif str == "in":
                temp_codes = inOrder_codes
            elif str == "po":
                temp_codes = postOrder_codes
            elif str == "prC":
                temp_codes = preOrderCreate_codes
            for index in range(begin, 0, -1):
                if temp_codes[num][index] == " " and record == 1:
                    if str == "pr":
                        return (origin_len - index - 2) * 0.19
                    elif str == "in":
                        return (origin_len - index - 2) * 0.19
                    elif str == "po":
                        return (origin_len - index - 2) * 0.19
                    else:
                        return (origin_len - index - 2) * 0.14
                elif temp_codes[num][index] == " " and record == 0:
                    record = 1
                elif temp_codes[num][index] != " ":
                    record = 0
            if str == "pr":
                return origin_len * 0.19
            elif str == "in":
                return origin_len * 0.19
            elif str == "po":
                return origin_len * 0.19
            else:
                return origin_len * 0.14

        codes_preOrderCreate = (
            VGroup(*[codeline_preOrderCreate(code) for code in preOrderCreate_codes])
            .arrange(DOWN, aligned_edge=LEFT, buff=0.05)
            .next_to(background.get_top(), DOWN, buff=0)
            .shift(LEFT * 0.05 + DOWN * 0.2)
        )

        codes_preOrder = (
            VGroup(*[codeline_preOrder(code) for code in preOrder_codes])
            .arrange(DOWN, aligned_edge=LEFT, buff=0.05)
            .next_to(background.get_top(), DOWN, buff=0)
            .shift(DOWN * 0.2)
        )

        codes_inOrder = (
            VGroup(*[codeline_inOrder(code) for code in inOrder_codes])
            .arrange(DOWN, aligned_edge=LEFT, buff=0.05)
            .next_to(background.get_top(), DOWN, buff=0)
            .shift(DOWN * 0.2)
        )

        codes_postOrder = (
            VGroup(*[codeline_postOrder(code) for code in postOrder_codes])
            .arrange(DOWN, aligned_edge=LEFT, buff=0.05)
            .next_to(background.get_top(), DOWN, buff=0)
            .shift(DOWN * 0.2)
        )

        # 代码框
        # codes_preOrderCreate   height: 0.28  *  width: 0.1 * x
        # codes_preOrder         height: 0.35  *  width: 0.1 * x
        # codes_inOrder          height: 0.35  *  width: 0.1 * x
        # codes_postOrder        height: 0.35  *  width: 0.1 * x
        move_frame = RoundedRectangle(
            stroke_width=2.5, stroke_color=BLUE, corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1, fill_color=RED).rotate(
            90 * DEGREES, axis=IN
        )
        if chose == 1:
            arrow.scale(0.11)
        else:
            arrow.scale(0.13)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))

        # 移动圆环
        move_circle = Circle(
            radius=0.48, stroke_width=20, stroke_color=BLUE, stroke_opacity=1
        ).shift(
            LEFT * 10
        )  # 让它换地方消失

        self.add(background)
        if chose == 1:
            self.add(codes_preOrderCreate)
        elif chose == 2:
            self.add(codes_preOrder)
        elif chose == 3:
            self.add(codes_inOrder)
        elif chose == 4:
            self.add(codes_postOrder)

        # frame_variable
        stack_frame = RoundedRectangle(
            stroke_width=8,
            stroke_color=GREEN_B,
            fill_color="#EBEBEB",
            fill_opacity=0,
            plot_depth=-1,
            corner_radius=0.05,
            sheen_factor=0.1,
            sheen_direction=UR,
        )
        stack_frame.set_height(3, stretch=True).set_width(6.5, stretch=True)
        stack_frame.move_to(frame_variable).align_to(frame_variable, UP)
        stack_location = Text("结点位置", font="思源宋体 Heavy", color=PURPLE).scale(0.7)
        stack_father = Text("父结点", font="思源宋体 Heavy", color=ORANGE).scale(0.7)
        stack_location.next_to(stack_frame, DOWN, buff=0.1).shift(LEFT * 1.5)
        stack_father.next_to(stack_frame, DOWN, buff=0.1).shift(RIGHT * 1.5)
        stack_level = Text("结点层数", font="思源宋体 Heavy", color=PURPLE).scale(0.7)
        stack_value = Text("结点值", font="思源宋体 Heavy", color=ORANGE).scale(0.7)
        stack_level.next_to(stack_frame, DOWN, buff=0.1).shift(LEFT * 1.5)
        stack_value.next_to(stack_frame, DOWN, buff=0.1).shift(RIGHT * 1.5)
        self.add(stack_frame)

        # 堆栈长方块
        base_stack = RoundedRectangle(
            stroke_width=5.5,
            stroke_color="FF5900",
            fill_color=BLUE,
            fill_opacity=0.95,
            plot_depth=-1,
            corner_radius=0.05,
            sheen_factor=0.15,
            sheen_direction=UR,
        )
        base_stack.set_height(0.6, stretch=True).set_width(6.36, stretch=True)

        # 堆栈长方块中的 方向 和 父结点
        left_direction = (
            Text("左", font="思源宋体 Heavy", color=BLACK)
            .scale(0.7)
            .move_to(base_stack)
            .align_to(base_stack)
            .shift(LEFT * 1.5)
        )
        right_direction = (
            Text("右", font="思源宋体 Heavy", color=BLACK)
            .scale(0.7)
            .move_to(base_stack)
            .align_to(base_stack)
            .shift(LEFT * 1.5)
        )
        origin_direction = (
            Text("中", font="思源宋体 Heavy", color=BLACK)
            .scale(0.7)
            .move_to(base_stack)
            .align_to(base_stack)
            .shift(LEFT * 1.5)
        )
        bottom_father = (
            Text("NULL", font="思源宋体 Heavy", color=BLACK)
            .scale(0.7)
            .move_to(base_stack)
            .align_to(base_stack)
            .shift(RIGHT * 1.5)
        )
        tmp_father = (
            Text("A", font="思源宋体 Heavy", color=BLACK)
            .scale(0.7)
            .move_to(base_stack)
            .align_to(base_stack)
            .shift(RIGHT * 1.5)
        )

        # 堆栈长方块整体
        base_stack_all = VGroup(base_stack, left_direction, tmp_father)

        # 堆栈长方块(bottom)
        stack_bottom = VGroup(base_stack, origin_direction, bottom_father)

        # 堆栈长方块(top)
        stack_top = RoundedRectangle(
            stroke_opacity=0,
            fill_color=YELLOW_D,
            fill_opacity=0.95,
            corner_radius=0.05,
            sheen_factor=0.1,
            sheen_direction=UR,
        )
        stack_top.set_height(0.315, stretch=True).set_width(6.42, stretch=True)

        # 堆栈长方块(top)里面的小三角
        arrow_in = (
            Triangle(stroke_opacity=0, fill_opacity=1, fill_color=GREEN_E)
            .scale(0.1)
            .rotate(180 * DEGREES, axis=IN)
        )

        # 堆栈长方块集合
        """  前序顺序建立二叉树 专属
        stack_all -> 除外 bottom 和 top 外的其他全部堆栈长方块
        |
        ├─ stack_layers -> 每一层的堆栈长方块
        |        |_ tmp_stack_all -> 一层中的一种类型的堆栈长方块
        |               ├─ base_stack -> 堆栈长方块的外型
        |               ├─ left_direction -> 堆栈长方块的方向(左)变量
        |               |_ tmp_father -> 堆栈长方块的父结点值(右)变量
        |
        ├─ stack_layers
        |        |_ tmp_stack_all X 2
        |
        |_ stack_layers
                 |_ tmp_stack_all X 4
        """
        if chose == 1:
            stack_all = VGroup()
            for layer in range(node_layers):
                stack_layers = VGroup()
                stack_all.add(stack_layers)

            def prC(self):
                global pre_list, stack_i
                value = pre_list[0]
                if len(pre_list) > 1:
                    pre_list = pre_list[1:]

                if value == flag:  # 当遇到 flag 时，令树的根节点为 None，从而结束该分支的递归
                    return
                else:
                    tmp_father = (
                        Text(value, font="思源宋体 Heavy", color=BLACK)
                        .scale(0.7)
                        .move_to(base_stack)
                        .align_to(base_stack)
                        .shift(RIGHT * 1.5)
                    )
                    tmp_stack_all = VGroup(base_stack, left_direction, tmp_father)
                    stack_all[stack_i].add(tmp_stack_all.copy())
                    stack_i += 1
                    prC(self)
                    prC(self)
                    stack_i -= 1

            prC(self)
            pre_list = nodeList_unzip  # 恢复 pre_list
            stack_i = 0  # 恢复 stack_i
        """  前序遍历二叉树 | 中序遍历二叉树 | 后序遍历二叉树 专属
        string_Traverse -> 遍历的字符串
        stack_all -> 除外 bottom 和 top 外的其他全部堆栈长方块
        |
        ├─ stack_layers -> 每一层的堆栈长方块
        |        |_ tmp_stack_all -> 一层中的一种类型的堆栈长方块
        |               ├─ base_stack -> 堆栈长方块的外型
        |               ├─ tmp_layer -> 堆栈长方块的层数(左)变量
        |               |_ tmp_value -> 堆栈长方块的结点值(右)变量
        |
        ├─ stack_layers
        |        |_ tmp_stack_all X 2
        |
        |_ stack_layers
        |        |_ tmp_stack_all X 4
        |
        |_ stack_layers
                 |_ tmp_stack_all X 8 -> 特殊(结点值为 NULL)的一层中的堆栈长方块
        """
        if chose == 2 or chose == 3 or chose == 4:
            stack_all = VGroup()
            string_Traverse = ""
            for layer in range(node_layers + 1):
                stack_layers = VGroup()
                stack_all.add(stack_layers)

            class T_N:
                def __init__(self, value):
                    self.value = value
                    self.leftChild = None
                    self.rightChild = None

            def prC(node):
                global pre_list
                value = pre_list[0]
                if len(pre_list) > 1:
                    pre_list = pre_list[1:]

                if value == flag:  # 当遇到 flag 时，令树的根节点为 None，从而结束该分支的递归
                    node = None
                else:
                    node = T_N(value)
                    node.leftChild = prC(node.leftChild)
                    node.rightChild = prC(node.rightChild)
                return node

            def pr(node):
                nonlocal string_Traverse
                global stack_i
                if node != None:
                    # 结点层数 stack_i+1  结点值 node.value
                    string_Traverse += node.value
                    tmp_layer = (
                        Text(str(stack_i + 1), font="思源宋体 Heavy", color=BLACK)
                        .scale(0.7)
                        .move_to(base_stack)
                        .align_to(base_stack)
                        .shift(LEFT * 1.5)
                    )
                    tmp_value = (
                        Text(node.value, font="思源宋体 Heavy", color=BLACK)
                        .scale(0.7)
                        .move_to(base_stack)
                        .align_to(base_stack)
                        .shift(RIGHT * 1.5)
                    )
                    tmp_stack_all = VGroup(base_stack, tmp_layer, tmp_value)
                    stack_all[stack_i].add(tmp_stack_all.copy())
                    stack_i += 1
                    pr(node.leftChild)
                    pr(node.rightChild)
                    stack_i -= 1
                else:
                    tmp_layer = (
                        Text(str(stack_i + 1), font="思源宋体 Heavy", color=BLACK)
                        .scale(0.7)
                        .move_to(base_stack)
                        .align_to(base_stack)
                        .shift(LEFT * 1.5)
                    )
                    tmp_value = (
                        Text("NULL", font="思源宋体 Heavy", color=BLACK)
                        .scale(0.7)
                        .move_to(base_stack)
                        .align_to(base_stack)
                        .shift(RIGHT * 1.5)
                    )
                    tmp_stack_all = VGroup(base_stack, tmp_layer, tmp_value)
                    stack_all[stack_i].add(tmp_stack_all.copy())

            def In(node):
                nonlocal string_Traverse
                global stack_i
                if node != None:
                    # 结点层数 stack_i+1  结点值 node.value
                    tmp_layer = (
                        Text(str(stack_i + 1), font="思源宋体 Heavy", color=BLACK)
                        .scale(0.7)
                        .move_to(base_stack)
                        .align_to(base_stack)
                        .shift(LEFT * 1.5)
                    )
                    tmp_value = (
                        Text(node.value, font="思源宋体 Heavy", color=BLACK)
                        .scale(0.7)
                        .move_to(base_stack)
                        .align_to(base_stack)
                        .shift(RIGHT * 1.5)
                    )
                    tmp_stack_all = VGroup(base_stack, tmp_layer, tmp_value)
                    stack_all[stack_i].add(tmp_stack_all.copy())
                    stack_i += 1
                    In(node.leftChild)
                    string_Traverse += node.value
                    In(node.rightChild)
                    stack_i -= 1
                else:
                    tmp_layer = (
                        Text(str(stack_i + 1), font="思源宋体 Heavy", color=BLACK)
                        .scale(0.7)
                        .move_to(base_stack)
                        .align_to(base_stack)
                        .shift(LEFT * 1.5)
                    )
                    tmp_value = (
                        Text("NULL", font="思源宋体 Heavy", color=BLACK)
                        .scale(0.7)
                        .move_to(base_stack)
                        .align_to(base_stack)
                        .shift(RIGHT * 1.5)
                    )
                    tmp_stack_all = VGroup(base_stack, tmp_layer, tmp_value)
                    stack_all[stack_i].add(tmp_stack_all.copy())

            def po(node):
                nonlocal string_Traverse
                global stack_i
                if node != None:
                    # 结点层数 stack_i+1  结点值 node.value
                    tmp_layer = (
                        Text(str(stack_i + 1), font="思源宋体 Heavy", color=BLACK)
                        .scale(0.7)
                        .move_to(base_stack)
                        .align_to(base_stack)
                        .shift(LEFT * 1.5)
                    )
                    tmp_value = (
                        Text(node.value, font="思源宋体 Heavy", color=BLACK)
                        .scale(0.7)
                        .move_to(base_stack)
                        .align_to(base_stack)
                        .shift(RIGHT * 1.5)
                    )
                    tmp_stack_all = VGroup(base_stack, tmp_layer, tmp_value)
                    stack_all[stack_i].add(tmp_stack_all.copy())
                    stack_i += 1
                    po(node.leftChild)
                    po(node.rightChild)
                    string_Traverse += node.value
                    stack_i -= 1
                else:
                    tmp_layer = (
                        Text(str(stack_i + 1), font="思源宋体 Heavy", color=BLACK)
                        .scale(0.7)
                        .move_to(base_stack)
                        .align_to(base_stack)
                        .shift(LEFT * 1.5)
                    )
                    tmp_value = (
                        Text("NULL", font="思源宋体 Heavy", color=BLACK)
                        .scale(0.7)
                        .move_to(base_stack)
                        .align_to(base_stack)
                        .shift(RIGHT * 1.5)
                    )
                    tmp_stack_all = VGroup(base_stack, tmp_layer, tmp_value)
                    stack_all[stack_i].add(tmp_stack_all.copy())

            tmp_treeNode = T_N(None)
            treeNode = prC(tmp_treeNode)
            if chose == 2:
                pr(treeNode)
            elif chose == 3:
                In(treeNode)
            elif chose == 4:
                po(treeNode)
            pre_list = nodeList_unzip  # 恢复 pre_list
            stack_i = 0  # 恢复 stack_i

        # 各堆栈长方块的位置
        sort_stack_all = VGroup()
        for sort_stack in stack_all:
            sort_stack_all.add(sort_stack[0])
        sort_stack_all.arrange(UP, aligned_edge=LEFT, buff=0.05)
        if chose == 1:
            stack_bottom.move_to(stack_frame).align_to(stack_frame, DOWN).shift(
                UP * 0.065
            )
            sort_stack_all.move_to(stack_bottom).next_to(
                stack_bottom, UP, buff=0
            ).shift(UP * 0.05)
        else:
            sort_stack_all.move_to(stack_frame).align_to(stack_frame, DOWN).shift(
                UP * 0.065
            )
        for sort_stacks in stack_all:
            for sort_stack in sort_stacks:
                if sort_stack != sort_stacks[0]:
                    sort_stack.move_to(sort_stacks[0])
        stack_top.move_to(stack_frame).align_to(stack_frame, DOWN).shift(
            UP * 0.04
        )  # .shift(UP*0.65*4)
        # 保存小三角和堆栈长方块(top)的相对位置不变
        arrow_in.add_updater(lambda a: a.move_to(stack_top))
        # self.add(sort_stack_all, stack_bottom, stack_top, arrow_in)

        # frame_animation
        # 位于框架下面的 Value 和 剩余串(前序顺序建立二叉树 专属)
        """
        animation_value_string -> 原字符串

        animation_value -> Value 整体
        |
        ├─ animation_value_reveal -> Value 左边部分(显示的 Value)
        |_ animation_value_value -> Value 右边部分(Value 的结点值)

        animation_string -> 剩余串 整体
        |
        ├─ animation_string_reveal -> 剩余串 左边部分(显示的 剩余串)
        |_ animation_string_value -> 剩余串 右边部分(剩余串 的字符串)
        """
        animation_value_string = nodeList
        animation_value_reveal = Text("Value:", font="思源宋体 Heavy", color=GOLD).scale(
            0.7
        )
        animation_string_reveal = Text("剩余串:", font="思源宋体 Heavy", color=BLUE).scale(0.7)
        animation_value_value = Text(".", font="思源宋体 Heavy", color=WHITE).scale(0.7)
        animation_string_value = Text(
            animation_value_string, font="思源宋体 Heavy", color=BLACK
        ).scale(0.7)
        animation_value_reveal.align_to(frame_animation, LEFT).align_to(
            frame_animation, DOWN
        ).shift(UP * 0.6 + RIGHT * 0.4)
        animation_value_value.next_to(animation_value_reveal, RIGHT, buff=0.15)
        animation_string_reveal.align_to(frame_animation, DOWN).next_to(
            animation_value_reveal, RIGHT, buff=0.8
        )
        animation_string_value.next_to(animation_string_reveal, RIGHT, buff=0.15)
        animation_value = VGroup(animation_value_reveal, animation_value_value)
        animation_string = VGroup(animation_string_reveal, animation_string_value)
        # 位于框架下面的 遍历结点 (前序遍历二叉树 | 中序遍历二叉树 | 后序遍历二叉树 专属)
        """
        animation_value_stringTraverse -> 遍历的字符串

        animation_stringTraverse -> 遍历结点 整体
        |
        ├─ animation_stringTraverse_reveal -> 遍历结点 左边部分(显示的 遍历结点)
        |_ animation_stringTraverse_value -> 遍历结点 右边部分(遍历结点 的各个结点值)
        """
        animation_value_stringTraverse = (
            string_Traverse if chose != 1 else nodeList
        )  # 为了防止被 chose==1 的情况影响
        animation_stringTraverse_reveal = Text(
            "遍历结果:", font="思源宋体 Heavy", color=GOLD
        ).scale(0.7)
        animation_stringTraverse_reveal.align_to(frame_animation, LEFT).align_to(
            frame_animation, DOWN
        ).shift(UP * 0.6 + RIGHT * 1)
        animation_stringTraverse_value = VGroup()
        index_Traverse = 0
        for stringTraverse_value in animation_value_stringTraverse:
            stringTraverse_reveal_tmp = Text(
                stringTraverse_value, font="思源宋体 Heavy", color=BLACK
            ).scale(0.7)
            if stringTraverse_value == animation_value_stringTraverse[0]:
                stringTraverse_reveal_tmp.next_to(
                    animation_stringTraverse_reveal, RIGHT, buff=0.25
                )
            else:
                stringTraverse_reveal_tmp.move_to(
                    animation_stringTraverse_value[index_Traverse]
                )
                index_Traverse += 1
                stringTraverse_reveal_tmp.shift(RIGHT * 0.5)
            animation_stringTraverse_value.add(stringTraverse_reveal_tmp)
        animation_stringTraverse = VGroup(
            animation_stringTraverse_reveal, animation_stringTraverse_value
        )

        # 二叉树结点
        class TreeNode:
            def __init__(self, value):
                self.value = value
                self.leftChild = None
                self.rightChild = None

        # 前序顺序建立二叉树
        def __preOrderCreate(node):
            global count, pre_list, index_tmp, num_index, stack_i
            value = pre_list[0]
            if len(pre_list) > 1:
                pre_list = pre_list[1:]
            if value == nodeList_unzip[0]:
                move_frame.set_width(
                    ignore_space_len(codes_preOrderCreate[2], "prC", 2), stretch=True
                ).set_height(0.28, stretch=True).move_to(
                    codes_preOrderCreate[2]
                ).align_to(
                    codes_preOrderCreate[2], RIGHT
                ).shift(
                    RIGHT * 0.05
                )
                self.play(ShowCreation(move_frame), Write(arrow))
                self.wait()
            else:
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_preOrderCreate[2], "prC", 2),
                    move_frame.move_to,
                    codes_preOrderCreate[2],
                    move_frame.align_to,
                    codes_preOrderCreate[2],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.28, "stretch": True},
                    run_time=1.5,
                )
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_preOrderCreate[3], "prC", 3),
                move_frame.move_to,
                codes_preOrderCreate[3],
                move_frame.align_to,
                codes_preOrderCreate[3],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.28, "stretch": True},
                run_time=1.5,
            )
            self.wait(0.5)
            animation_value_value_tmp = (
                Text(animation_value_string[num_index], font="思源宋体 Heavy", color=BLACK)
                .scale(0.7)
                .next_to(animation_value[0], RIGHT, buff=0.15)
            )
            # 剩余串临时移动组
            move_animation_string_value = VGroup()
            for move_element in range(num_index + 1, len(animation_value_string)):
                move_animation_string_value.add(animation_string[1][move_element])
            self.play(
                FadeOut(animation_string[1][num_index]),
                Transform(animation_value[1], animation_value_value_tmp),
                move_animation_string_value.shift,
                LEFT * 0.21,
            )
            num_index += 1
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_preOrderCreate[4], "prC", 4),
                move_frame.move_to,
                codes_preOrderCreate[4],
                move_frame.align_to,
                codes_preOrderCreate[4],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.28, "stretch": True},
                run_time=1.5,
            )

            if value == flag:  # 当遇到 flag 时，令树的根节点为 None，从而结束该分支的递归
                node = None
            else:
                # print(count-1)  # 出现结点
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_preOrderCreate[6], "prC", 6),
                    move_frame.move_to,
                    codes_preOrderCreate[6],
                    move_frame.align_to,
                    codes_preOrderCreate[6],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.28, "stretch": True},
                    run_time=1.5,
                )
                if count >= 2:
                    self.play(ShowCreation(line_all[count - 2]))
                self.play(GrowFromCenter(base_all[count - 1]))
                element_all[index_tmp].move_to(base_all[count - 1])
                self.play(FadeIn(element_all[index_tmp]))
                index_tmp += 1
                self.wait(0.5)
                node = TreeNode(value)
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_preOrderCreate[7], "prC", 7),
                    move_frame.move_to,
                    codes_preOrderCreate[7],
                    move_frame.align_to,
                    codes_preOrderCreate[7],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.28, "stretch": True},
                    run_time=1.5,
                )
                self.wait(0.5)
                mod = 2 ** (stack_i)
                stack_num = (int)(count % mod)
                # print("appear:  mod: "+str(mod)+" "+"stack_i: " +str(stack_i)+" "+"count: "+str(count)+" "+"stack_num: "+str(stack_num))
                self.play(
                    FadeInFrom(stack_all[stack_i][stack_num], UP),
                    stack_top.shift,
                    UP * 0.65,
                )
                self.wait()
                stack_i += 1
                count *= 2
                node.leftChild = __preOrderCreate(node.leftChild)
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_preOrderCreate[8], "prC", 8),
                    move_frame.move_to,
                    codes_preOrderCreate[8],
                    move_frame.align_to,
                    codes_preOrderCreate[8],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.28, "stretch": True},
                    run_time=1.5,
                )
                self.wait(0.5)
                # 极其重要，mod 和 stack_num 要取父结点值，不然会越界
                mod = 2 ** (stack_i - 1)
                stack_num = (int)((count // 2) % mod)
                # print("change:  mod: "+str(mod)+" "+"stack_i-1: "+str(stack_i-1)+" "+"count: "+str(count)+" "+"stack_num: "+str(stack_num))
                transform_stack_direction = (
                    right_direction.copy()
                    .move_to(stack_all[stack_i - 1][stack_num][0])
                    .align_to(stack_all[stack_i - 1][stack_num][0])
                    .shift(LEFT * 1.5)
                )
                self.play(
                    Transform(
                        stack_all[stack_i - 1][stack_num][1],
                        transform_stack_direction.copy(),
                    )
                )
                self.wait()
                count += 1
                node.rightChild = __preOrderCreate(node.rightChild)
                stack_i -= 1
                count //= 2
                mod = 2 ** (stack_i)
                stack_num = (int)(count % mod)
                # print("disappear:  mod: "+str(mod)+" "+"stack_i: " +str(stack_i)+" "+"count: "+str(count)+" "+"stack_num: "+str(stack_num))
                self.play(
                    FadeOutAndShift(stack_all[stack_i][stack_num], UP),
                    stack_top.shift,
                    DOWN * 0.65,
                )
                self.wait()
            return node

        # 前序顺序建立二叉树(非动画演示)
        def __preOrderCreate_forTraverse(node):
            global pre_list, count, index_tmp
            value = pre_list[0]
            if len(pre_list) > 1:
                pre_list = pre_list[1:]
            if value == flag:
                node = None
            else:
                element_all[index_tmp].move_to(base_all[count - 1])
                node = TreeNode(value)
                index_tmp += 1
                count *= 2
                node.leftChild = __preOrderCreate_forTraverse(node.leftChild)
                count += 1
                node.rightChild = __preOrderCreate_forTraverse(node.rightChild)
                count //= 2
            return node

        # 前序遍历二叉树
        def __preTraverse(node):
            nonlocal move_circle
            global turn_on, stack_i, index_tmp, count
            mod = 2 ** (stack_i)
            stack_num = (int)(count % mod)
            # print("appear:  mod: "+str(mod)+" "+"stack_i: " +str(stack_i)+" "+"count: "+str(count)+" "+"stack_num: "+str(stack_num))
            if stack_i < 3:
                move_circle_new_position = move_circle.copy()
                move_circle_new_position.move_to(base_all[count - 1])
                self.play(
                    FadeInFrom(stack_all[stack_i][stack_num], UP),
                    stack_top.shift,
                    UP * 0.65,
                    FadeIn(move_circle_new_position),
                    FadeOut(move_circle),
                )
                move_circle = move_circle_new_position
            else:
                self.play(
                    FadeInFrom(stack_all[stack_i][stack_num], UP),
                    stack_top.shift,
                    UP * 0.65,
                    FadeOut(move_circle),
                )
                move_circle.shift(LEFT * 10)  # 让它换地方消失
            self.wait(0.5)
            stack_i += 1
            count *= 2
            if turn_on == False:
                turn_on = True
                move_frame.set_width(
                    ignore_space_len(codes_preOrder[2], "pr", 2), stretch=True
                ).set_height(0.35, stretch=True).move_to(codes_preOrder[2]).align_to(
                    codes_preOrder[2], RIGHT
                ).shift(
                    RIGHT * 0.05
                )
                self.play(ShowCreation(move_frame), Write(arrow))
                self.wait()
            else:
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_preOrder[2], "pr", 2),
                    move_frame.move_to,
                    codes_preOrder[2],
                    move_frame.align_to,
                    codes_preOrder[2],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.35, "stretch": True},
                    run_time=1.5,
                )
                self.wait(0.5)
            if node != None:
                # print(node.value, end='')  # 打印结点
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_preOrder[4], "pr", 4),
                    move_frame.move_to,
                    codes_preOrder[4],
                    move_frame.align_to,
                    codes_preOrder[4],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.35, "stretch": True},
                    run_time=1.5,
                )
                self.wait(0.5)
                self.play(FadeIn(animation_stringTraverse[1][index_tmp]))
                index_tmp += 1
                self.wait()
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_preOrder[5], "pr", 5),
                    move_frame.move_to,
                    codes_preOrder[5],
                    move_frame.align_to,
                    codes_preOrder[5],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.35, "stretch": True},
                    run_time=1.5,
                )
                self.wait(0.5)
                __preTraverse(node.leftChild)
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_preOrder[6], "pr", 6),
                    move_frame.move_to,
                    codes_preOrder[6],
                    move_frame.align_to,
                    codes_preOrder[6],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.35, "stretch": True},
                    run_time=1.5,
                )
                count += 1
                self.wait(0.5)
                __preTraverse(node.rightChild)
                stack_i -= 1
                count //= 2
                mod = 2 ** (stack_i)
                stack_num = (int)(count % mod)
                # print("disappear:  mod: "+str(mod)+" "+"stack_i: " +str(stack_i)+" "+"count: "+str(count)+" "+"stack_num: "+str(stack_num))
                if stack_i > 0:
                    move_circle_new_position = move_circle.copy()
                    move_circle_new_position.move_to(base_all[count // 2 - 1])
                    self.play(
                        FadeOutAndShift(stack_all[stack_i][stack_num], UP),
                        stack_top.shift,
                        DOWN * 0.65,
                        FadeIn(move_circle_new_position),
                        FadeOut(move_circle),
                    )
                    move_circle = move_circle_new_position
                else:
                    self.play(
                        FadeOutAndShift(stack_all[stack_i][stack_num], UP),
                        stack_top.shift,
                        DOWN * 0.65,
                        FadeOut(move_circle),
                    )
                    move_circle.shift(LEFT * 10)  # 让它换地方消失
                self.wait(0.5)
            else:
                stack_i -= 1
                count //= 2
                mod = 2 ** (stack_i)
                stack_num = (int)(count % mod)
                # print("disappear:  mod: "+str(mod)+" "+"stack_i: " +str(stack_i)+" "+"count: "+str(count)+" "+"stack_num: "+str(stack_num))
                move_circle_new_position = move_circle.copy()
                move_circle_new_position.move_to(base_all[count // 2 - 1])
                self.play(
                    FadeOutAndShift(stack_all[stack_i][stack_num], UP),
                    stack_top.shift,
                    DOWN * 0.65,
                    FadeIn(move_circle_new_position),
                    FadeOut(move_circle),
                )
                move_circle = move_circle_new_position
                self.wait(0.5)

        # 中序遍历二叉树
        def __midTraverse(node):
            nonlocal move_circle
            global turn_on, stack_i, index_tmp, count
            mod = 2 ** (stack_i)
            stack_num = (int)(count % mod)
            # print("appear:  mod: "+str(mod)+" "+"stack_i: " +str(stack_i)+" "+"count: "+str(count)+" "+"stack_num: "+str(stack_num))
            if stack_i < 3:
                move_circle_new_position = move_circle.copy()
                move_circle_new_position.move_to(base_all[count - 1])
                self.play(
                    FadeInFrom(stack_all[stack_i][stack_num], UP),
                    stack_top.shift,
                    UP * 0.65,
                    FadeIn(move_circle_new_position),
                    FadeOut(move_circle),
                )
                move_circle = move_circle_new_position
            else:
                self.play(
                    FadeInFrom(stack_all[stack_i][stack_num], UP),
                    stack_top.shift,
                    UP * 0.65,
                    FadeOut(move_circle),
                )
                move_circle.shift(LEFT * 10)  # 让它换地方消失
            self.wait(0.5)
            stack_i += 1
            count *= 2
            if turn_on == False:
                turn_on = True
                move_frame.set_width(
                    ignore_space_len(codes_inOrder[2], "in", 2), stretch=True
                ).set_height(0.35, stretch=True).move_to(codes_inOrder[2]).align_to(
                    codes_inOrder[2], RIGHT
                ).shift(
                    RIGHT * 0.05
                )
                self.play(ShowCreation(move_frame), Write(arrow))
                self.wait()
            else:
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_inOrder[2], "in", 2),
                    move_frame.move_to,
                    codes_inOrder[2],
                    move_frame.align_to,
                    codes_inOrder[2],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.35, "stretch": True},
                    run_time=1.5,
                )
                self.wait(0.5)
            if node != None:
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_inOrder[4], "in", 4),
                    move_frame.move_to,
                    codes_inOrder[4],
                    move_frame.align_to,
                    codes_inOrder[4],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.35, "stretch": True},
                    run_time=1.5,
                )
                self.wait(0.5)
                __midTraverse(node.leftChild)
                # print(node.value, end='')  # 打印结点
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_inOrder[5], "in", 5),
                    move_frame.move_to,
                    codes_inOrder[5],
                    move_frame.align_to,
                    codes_inOrder[5],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.35, "stretch": True},
                    run_time=1.5,
                )
                self.wait(0.5)
                self.play(FadeIn(animation_stringTraverse[1][index_tmp]))
                index_tmp += 1
                self.wait()
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_inOrder[6], "in", 6),
                    move_frame.move_to,
                    codes_inOrder[6],
                    move_frame.align_to,
                    codes_inOrder[6],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.35, "stretch": True},
                    run_time=1.5,
                )
                count += 1
                self.wait(0.5)
                __midTraverse(node.rightChild)
                stack_i -= 1
                count //= 2
                mod = 2 ** (stack_i)
                stack_num = (int)(count % mod)
                # print("disappear:  mod: "+str(mod)+" "+"stack_i: " +str(stack_i)+" "+"count: "+str(count)+" "+"stack_num: "+str(stack_num))
                if stack_i > 0:
                    move_circle_new_position = move_circle.copy()
                    move_circle_new_position.move_to(base_all[count // 2 - 1])
                    self.play(
                        FadeOutAndShift(stack_all[stack_i][stack_num], UP),
                        stack_top.shift,
                        DOWN * 0.65,
                        FadeIn(move_circle_new_position),
                        FadeOut(move_circle),
                    )
                    move_circle = move_circle_new_position
                else:
                    self.play(
                        FadeOutAndShift(stack_all[stack_i][stack_num], UP),
                        stack_top.shift,
                        DOWN * 0.65,
                        FadeOut(move_circle),
                    )
                    move_circle.shift(LEFT * 10)  # 让它换地方消失
                self.wait(0.5)
            else:
                stack_i -= 1
                count //= 2
                mod = 2 ** (stack_i)
                stack_num = (int)(count % mod)
                # print("disappear:  mod: "+str(mod)+" "+"stack_i: " +str(stack_i)+" "+"count: "+str(count)+" "+"stack_num: "+str(stack_num))
                move_circle_new_position = move_circle.copy()
                move_circle_new_position.move_to(base_all[count // 2 - 1])
                self.play(
                    FadeOutAndShift(stack_all[stack_i][stack_num], UP),
                    stack_top.shift,
                    DOWN * 0.65,
                    FadeIn(move_circle_new_position),
                    FadeOut(move_circle),
                )
                move_circle = move_circle_new_position
                self.wait(0.5)

        # 后序遍历二叉树
        def __postTraverse(node):
            nonlocal move_circle
            global turn_on, stack_i, index_tmp, count
            mod = 2 ** (stack_i)
            stack_num = (int)(count % mod)
            # print("appear:  mod: "+str(mod)+" "+"stack_i: " +str(stack_i)+" "+"count: "+str(count)+" "+"stack_num: "+str(stack_num))
            if stack_i < 3:
                move_circle_new_position = move_circle.copy()
                move_circle_new_position.move_to(base_all[count - 1])
                self.play(
                    FadeInFrom(stack_all[stack_i][stack_num], UP),
                    stack_top.shift,
                    UP * 0.65,
                    FadeIn(move_circle_new_position),
                    FadeOut(move_circle),
                )
                move_circle = move_circle_new_position
            else:
                self.play(
                    FadeInFrom(stack_all[stack_i][stack_num], UP),
                    stack_top.shift,
                    UP * 0.65,
                    FadeOut(move_circle),
                )
                move_circle.shift(LEFT * 10)  # 让它换地方消失
            self.wait(0.5)
            stack_i += 1
            count *= 2
            if turn_on == False:
                turn_on = True
                move_frame.set_width(
                    ignore_space_len(codes_postOrder[2], "po", 2), stretch=True
                ).set_height(0.35, stretch=True).move_to(codes_postOrder[2]).align_to(
                    codes_postOrder[2], RIGHT
                ).shift(
                    RIGHT * 0.05
                )
                self.play(ShowCreation(move_frame), Write(arrow))
                self.wait()
            else:
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_postOrder[2], "po", 2),
                    move_frame.move_to,
                    codes_postOrder[2],
                    move_frame.align_to,
                    codes_postOrder[2],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.35, "stretch": True},
                    run_time=1.5,
                )
                self.wait(0.5)
            if node != None:
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_postOrder[4], "po", 4),
                    move_frame.move_to,
                    codes_postOrder[4],
                    move_frame.align_to,
                    codes_postOrder[4],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.35, "stretch": True},
                    run_time=1.5,
                )
                self.wait(0.5)
                __postTraverse(node.leftChild)
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_postOrder[5], "po", 5),
                    move_frame.move_to,
                    codes_postOrder[5],
                    move_frame.align_to,
                    codes_postOrder[5],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.35, "stretch": True},
                    run_time=1.5,
                )
                count += 1
                self.wait(0.5)
                __postTraverse(node.rightChild)
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_postOrder[6], "po", 6),
                    move_frame.move_to,
                    codes_postOrder[6],
                    move_frame.align_to,
                    codes_postOrder[6],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.35, "stretch": True},
                    run_time=1.5,
                )
                self.wait(0.5)
                # print(node.value, end='')  # 打印结点
                self.play(FadeIn(animation_stringTraverse[1][index_tmp]))
                index_tmp += 1
                self.wait()
                stack_i -= 1
                count //= 2
                mod = 2 ** (stack_i)
                stack_num = (int)(count % mod)
                # print("disappear:  mod: "+str(mod)+" "+"stack_i: " +str(stack_i)+" "+"count: "+str(count)+" "+"stack_num: "+str(stack_num))
                if stack_i > 0:
                    move_circle_new_position = move_circle.copy()
                    move_circle_new_position.move_to(base_all[count // 2 - 1])
                    self.play(
                        FadeOutAndShift(stack_all[stack_i][stack_num], UP),
                        stack_top.shift,
                        DOWN * 0.65,
                        FadeIn(move_circle_new_position),
                        FadeOut(move_circle),
                    )
                    move_circle = move_circle_new_position
                else:
                    self.play(
                        FadeOutAndShift(stack_all[stack_i][stack_num], UP),
                        stack_top.shift,
                        DOWN * 0.65,
                        FadeOut(move_circle),
                    )
                    move_circle.shift(LEFT * 10)  # 让它换地方消失
                self.wait(0.5)
            else:
                stack_i -= 1
                count //= 2
                mod = 2 ** (stack_i)
                stack_num = (int)(count % mod)
                # print("disappear:  mod: "+str(mod)+" "+"stack_i: " +str(stack_i)+" "+"count: "+str(count)+" "+"stack_num: "+str(stack_num))
                move_circle_new_position = move_circle.copy()
                move_circle_new_position.move_to(base_all[count // 2 - 1])
                self.play(
                    FadeOutAndShift(stack_all[stack_i][stack_num], UP),
                    stack_top.shift,
                    DOWN * 0.65,
                    FadeIn(move_circle_new_position),
                    FadeOut(move_circle),
                )
                move_circle = move_circle_new_position
                self.wait(0.5)

        # ------------------------------ 动画演示 ------------------------------
        #  1: 前序顺序建立二叉树  2: 前序遍历二叉树  3: 中序遍历二叉树  4: 后序遍历二叉树
        if chose == 1:
            treeNode_tmp = TreeNode(None)
            self.add(stack_top, arrow_in)
            self.add(animation_value, animation_string)
            self.add(stack_location, stack_father)
            self.wait(0.5)
            self.play(FadeInFrom(stack_bottom, UP), stack_top.shift, UP * 0.65)
            self.wait(0.5)
            treeNode = __preOrderCreate(treeNode_tmp)
            self.play(FadeOutAndShift(stack_bottom, UP), stack_top.shift, DOWN * 0.65)
            self.play(FadeOut(move_frame), FadeOut(arrow))
        elif chose == 2:
            treeNode_tmp = TreeNode(None)
            treeNode = __preOrderCreate_forTraverse(treeNode_tmp)
            pre_list = nodeList_unzip  # 恢复 pre_list
            count = 1  # 恢复 count
            index_tmp = 0  # 恢复 index_tmp
            self.add(stack_top, arrow_in)
            self.add(animation_stringTraverse[0])
            self.add(base_all, line_all, element_all)
            self.add(stack_level, stack_value)
            self.wait(0.5)
            treeNodeTraverse = __preTraverse(treeNode)
            self.play(FadeOut(move_frame), FadeOut(arrow))
        elif chose == 3:
            treeNode_tmp = TreeNode(None)
            treeNode = __preOrderCreate_forTraverse(treeNode_tmp)
            pre_list = nodeList_unzip  # 恢复 pre_list
            count = 1  # 恢复 count
            index_tmp = 0  # 恢复 index_tmp
            self.add(stack_top, arrow_in)
            self.add(animation_stringTraverse[0])
            self.add(base_all, line_all, element_all)
            self.add(stack_level, stack_value)
            self.wait(0.5)
            treeNodeTraverse = __midTraverse(treeNode)
            self.play(FadeOut(move_frame), FadeOut(arrow))
        elif chose == 4:
            treeNode_tmp = TreeNode(None)
            treeNode = __preOrderCreate_forTraverse(treeNode_tmp)
            pre_list = nodeList_unzip  # 恢复 pre_list
            count = 1  # 恢复 count
            index_tmp = 0  # 恢复 index_tmp
            self.add(stack_top, arrow_in)
            self.add(animation_stringTraverse[0])
            self.add(base_all, line_all, element_all)
            self.add(stack_level, stack_value)
            self.wait(0.5)
            treeNodeTraverse = __postTraverse(treeNode)
            self.play(FadeOut(move_frame), FadeOut(arrow))


class tree_traverse(Scene_White):
    def construct(self):
        global pre_list
        # Frame 整体框架
        # height: 8  *  width: 14.2
        frame_code = Rectangle(
            color=BLUE, stroke_opacity=0, height=5, width=7.1,
        ).to_corner(UR, buff=0)
        frame_variable = Rectangle(
            color=RED, stroke_opacity=0, height=3, width=7.1,
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
        # 基准圆形
        circle_base = Circle(
            radius=0.6, stroke_width=8, stroke_color=BLACK, stroke_opacity=1
        )
        # 基准大小
        narrow_multiple = circle_base.get_width()  # 直径
        # assert circle_base.get_width() * 2 == 1
        # 结点集合
        base_all = VGroup()
        for i in range(node_full):
            base_tmp = circle_base.copy()
            base_all.add(base_tmp)
        # 结点元素集合
        element_all = VGroup()
        for i in range(len(pre_list)):
            element_tmp = Text(pre_list[i], font="江西拙楷", color=BLACK).scale(1.5).copy()
            if pre_list[i] != flag:
                element_all.add(element_tmp)
        # 结点连线集合
        line_all = VGroup()

        # 各结点的位置
        if node_full == 3:
            pass
        elif node_full == 7:
            # 结点 0 的位置
            base_all[0].move_to(frame_animation).align_to(frame_animation, UP).shift(
                DOWN * 0.8
            )
            # 结点 1 结点 2 的位置
            base_all[1].next_to(base_all[0], DOWN, buff=1).shift(LEFT * 1.5)
            # 结点 0 1 连线
            base_0 = base_all[0].point_at_angle(250 * DEGREES)
            base_1 = base_all[1].point_at_angle(90 * DEGREES)
            line_0_1 = Line(
                np.array(base_0), np.array(base_1), color=BLACK, stroke_width=5
            )
            base_all[2].next_to(base_all[0], DOWN, buff=1).shift(RIGHT * 1.5)
            # 结点 0 2 连线
            base_0 = base_all[0].point_at_angle(290 * DEGREES)
            base_2 = base_all[2].point_at_angle(90 * DEGREES)
            line_0_2 = Line(
                np.array(base_0), np.array(base_2), color=BLACK, stroke_width=5
            )
            # 结点 3 结点 4 的位置
            base_all[3].next_to(base_all[1], DOWN, buff=1).shift(LEFT * 1.2)
            # 结点 1 3 连线
            base_1 = base_all[1].point_at_angle(240 * DEGREES)
            base_3 = base_all[3].point_at_angle(90 * DEGREES)
            line_1_3 = Line(
                np.array(base_1), np.array(base_3), color=BLACK, stroke_width=5
            )
            base_all[4].next_to(base_all[1], DOWN, buff=1).shift(RIGHT * 0.7)
            # 结点 1 4 连线
            base_1 = base_all[1].point_at_angle(290 * DEGREES)
            base_4 = base_all[4].point_at_angle(90 * DEGREES)
            line_1_4 = Line(
                np.array(base_1), np.array(base_4), color=BLACK, stroke_width=5
            )
            # 结点 5 结点 6 的位置
            base_all[5].next_to(base_all[2], DOWN, buff=1).shift(LEFT * 0.7)
            # 结点 2 5 连线
            base_2 = base_all[2].point_at_angle(250 * DEGREES)
            base_5 = base_all[5].point_at_angle(90 * DEGREES)
            line_2_5 = Line(
                np.array(base_2), np.array(base_5), color=BLACK, stroke_width=5
            )
            base_all[6].next_to(base_all[2], DOWN, buff=1).shift(RIGHT * 1.2)
            # 结点 2 6 连线
            base_2 = base_all[2].point_at_angle(300 * DEGREES)
            base_6 = base_all[6].point_at_angle(90 * DEGREES)
            line_2_6 = Line(
                np.array(base_2), np.array(base_6), color=BLACK, stroke_width=5
            )
            # 集合
            line_all = VGroup(
                line_0_1, line_0_2, line_1_3, line_1_4, line_2_5, line_2_6
            )
        elif node_full == 15:
            pass

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
        background.set_height(4.5, stretch=True).set_width(6.5, stretch=True)
        background.move_to(frame_code)

        # frame_code 背景 + 代码 + 移动框
        class codeline_levelOrderTraverse(Text):
            CONFIG = {
                # "t2c": {".": WHITE, "t.": BLACK},  # t. 需要和 . 区分开
                "size": 0.45,
                "color": BLACK,
                "font": "Consolas",
            }

            def __init__(self, text, **kwargs):
                Text.__init__(self, text, **kwargs)

        def ignore_space_len(code, str, num):
            origin_len = len(code)
            begin = origin_len - 1
            record = 0
            if str == "lo":
                temp_codes = levelOrderTraverse_codes
            elif str == "loC":
                temp_codes = levelOrderCreate_codes
            for index in range(begin, 0, -1):
                if temp_codes[num][index] == " " and record == 1:
                    if str == "lo":
                        return (origin_len - index - 2) * 0.13
                    else:
                        return (origin_len - index - 2) * 0.13
                elif temp_codes[num][index] == " " and record == 0:
                    record = 1
                elif temp_codes[num][index] != " ":
                    record = 0
            if str == "lo":
                return origin_len * 0.13
            else:
                return origin_len * 0.13

        codes_levelOrderTraverse = (
            VGroup(
                *[
                    codeline_levelOrderTraverse(code)
                    for code in levelOrderTraverse_codes
                ]
            )
            .arrange(DOWN, aligned_edge=LEFT, buff=0.05)
            .next_to(background.get_top(), DOWN, buff=0)
            .shift(LEFT * 0.2 + DOWN * 0.1)
        )

        # 代码框
        # codes_levelOrderTraverse   height: 0.30  *  width: 0.1 * x
        move_frame = RoundedRectangle(
            stroke_width=2.5, stroke_color=BLUE, corner_radius=0.05,
        )

        # 代码框左边的小三角
        arrow = Triangle(stroke_opacity=0, fill_opacity=1, fill_color=RED).rotate(
            90 * DEGREES, axis=IN
        )
        if chose == 1:
            arrow.scale(0.11)
        else:
            arrow.scale(0.09)
        # 保存小三角和代码框的相对位置不变
        arrow.add_updater(lambda a: a.next_to(move_frame, LEFT, buff=0.1))

        # 移动圆环
        move_circle = Circle(
            radius=0.48, stroke_width=20, stroke_color=BLUE, stroke_opacity=1
        ).shift(
            LEFT * 10
        )  # 让它换地方消失

        self.add(background)
        if chose == 1:
            pass
        elif chose == 2:
            self.add(codes_levelOrderTraverse)

        # frame_variable
        stack_frame = RoundedRectangle(
            stroke_width=8,
            stroke_color=GREEN_B,
            fill_color="#EBEBEB",
            fill_opacity=0,
            plot_depth=-1,
            corner_radius=0.05,
            sheen_factor=0.1,
            sheen_direction=UR,
        )
        stack_frame.set_height(2, stretch=True).set_width(5.5, stretch=True)
        stack_frame.move_to(frame_variable).align_to(background, LEFT).shift(
            RIGHT * 0.4 + UP * 0.2
        )
        stack_current = VGroup()
        stack_current_1 = Text("当", font="思源宋体 Heavy", color=PURPLE).scale(0.7)
        stack_current_2 = Text("前", font="思源宋体 Heavy", color=PURPLE).scale(0.7)
        stack_current_3 = Text("结", font="思源宋体 Heavy", color=PURPLE).scale(0.7)
        stack_current_4 = Text("点", font="思源宋体 Heavy", color=PURPLE).scale(0.7)
        stack_current.add(
            stack_current_1, stack_current_2, stack_current_3, stack_current_4
        )
        stack_current.arrange(DOWN, aligned_edge=LEFT, buff=0.05).next_to(
            stack_frame, RIGHT
        )

        # 堆栈长方块
        base_stack = RoundedRectangle(
            stroke_width=5.5,
            stroke_color="FF5900",
            fill_color=BLUE,
            fill_opacity=0.95,
            plot_depth=-1,
            corner_radius=0.05,
            sheen_factor=0.15,
            sheen_direction=UR,
        )
        base_stack.set_height(1.87, stretch=True).set_width(1.1, stretch=True)

        # 堆栈圆形
        base_circle = (
            Circle(
                radius=0.2,
                stroke_width=3.5,
                stroke_color=ORANGE,
                stroke_opacity=1,
                fill_color=WHITE,
                fill_opacity=0,
            )
            .align_to(base_stack, UR)
            .shift(LEFT * 0.08 + DOWN * 0.08)
        )

        # 堆栈长方块中的 结点 和 父结点
        tmp_current = (
            Text("A", font="思源宋体 Heavy", color=BLACK).scale(1.0).move_to(base_stack)
        )
        tmp_father = (
            Text("A", font="思源宋体 Heavy", color=BLACK).scale(0.5).move_to(base_circle)
        )

        # 堆栈长方块整体
        base_stack_all = VGroup(base_stack, base_circle, tmp_current, tmp_father)

        # 堆栈长方块(left or right)
        stack_left = RoundedRectangle(
            stroke_opacity=0,
            fill_color=YELLOW_D,
            fill_opacity=0.95,
            corner_radius=0.05,
            sheen_factor=0.1,
            sheen_direction=UR,
        )
        stack_left.set_height(1.92, stretch=True).set_width(0.4, stretch=True)
        stack_right = stack_left.copy()
        stack_left.move_to(stack_frame).align_to(stack_frame, LEFT).shift(RIGHT * 0.04)
        stack_right.move_to(stack_frame).align_to(stack_frame, RIGHT).shift(LEFT * 0.04)

        # 堆栈长方块(left or right)里面的小三角
        arrow_in_left = (
            Triangle(stroke_opacity=0, fill_opacity=1, fill_color=GREEN_E)
            .scale(0.14)
            .rotate(270 * DEGREES, axis=IN)
        )
        arrow_in_right = arrow_in_left.copy()
        arrow_in_left.move_to(stack_left)
        arrow_in_right.move_to(stack_right)

        # 伪集合
        # ---------------- test ----------------
        stack_all = VGroup()
        for i in range(4):
            tmp = base_stack_all.copy()
            if i == 1:
                tmp[0].set_style(
                    fill_color=RED_B, sheen_factor=0.15, sheen_direction=UR
                )
            elif i == 2:
                tmp[0].set_style(
                    fill_color="#ffb61e", sheen_factor=0.15, sheen_direction=UR
                )
            elif i == 3:
                tmp[0].set_style(
                    fill_color=PURPLE_B, sheen_factor=0.15, sheen_direction=UR
                )
            stack_all.add(tmp)
        stack_all.arrange(RIGHT, aligned_edge=UP, buff=0.055).move_to(
            stack_frame
        ).next_to(stack_left, RIGHT, buff=0.03)
        # self.add(stack_all)
        # ---------------- test ----------------

        # frame_animation
        # 位于框架下面的 遍历结点 (层次遍历二叉树 专属)
        """
        animation_value_stringTraverse -> 遍历的字符串

        animation_stringTraverse -> 遍历结点 整体
        |
        ├─ animation_stringTraverse_reveal -> 遍历结点 左边部分(显示的 遍历结点)
        |_ animation_stringTraverse_value -> 遍历结点 右边部分(遍历结点 的各个结点值)
        """
        string_Traverse = ""
        queue_all = VGroup()

        class T_N:
            def __init__(self, value):
                self.value = value
                self.leftChild = None
                self.rightChild = None

        def loC(node):
            nonlocal queue_all
            global pre_list
            data = pre_list[0]
            node = T_N(data)
            Nodes = [node]
            i = 1
            pop_father = 0
            change_color_count = 1
            tmp_current = (
                Text(pre_list[i - 1], font="思源宋体 Heavy", color=BLACK)
                .scale(1.0)
                .move_to(base_stack)
            )
            tmp_queue = VGroup(base_stack.copy(), tmp_current.copy())
            queue_all.add(tmp_queue)
            for data in Nodes:
                if data != None:
                    data.leftChild = T_N(pre_list[i]) if pre_list[i] != flag else None
                    Nodes.append(data.leftChild)
                    i += 1
                    tmp_current = (
                        Text(pre_list[i - 1], font="思源宋体 Heavy", color=BLACK)
                        .scale(1.0)
                        .move_to(base_stack)
                    )
                    tmp_father = (
                        Text(pre_list[pop_father], font="思源宋体 Heavy", color=BLACK)
                        .scale(0.5)
                        .move_to(base_circle)
                    )
                    tmp_queue = VGroup(
                        base_stack.copy(),
                        base_circle.copy(),
                        tmp_current.copy(),
                        tmp_father.copy(),
                    )
                    if change_color_count == 1:
                        tmp_queue[0].set_style(
                            fill_color=RED_B, sheen_factor=0.15, sheen_direction=UR
                        )
                    elif change_color_count == 2:
                        tmp_queue[0].set_style(
                            fill_color="#ffb61e", sheen_factor=0.15, sheen_direction=UR
                        )
                    elif change_color_count == 3:
                        tmp_queue[0].set_style(
                            fill_color=PURPLE_B, sheen_factor=0.15, sheen_direction=UR
                        )
                    queue_all.add(tmp_queue)
                    if i == len(pre_list):
                        return node
                    data.rightChild = T_N(pre_list[i]) if pre_list[i] != flag else None
                    Nodes.append(data.rightChild)
                    i += 1
                    tmp_current = (
                        Text(pre_list[i - 1], font="思源宋体 Heavy", color=BLACK)
                        .scale(1.0)
                        .move_to(base_stack)
                    )
                    tmp_father = (
                        Text(pre_list[pop_father], font="思源宋体 Heavy", color=BLACK)
                        .scale(0.5)
                        .move_to(base_circle)
                    )
                    tmp_queue = VGroup(
                        base_stack.copy(),
                        base_circle.copy(),
                        tmp_current.copy(),
                        tmp_father.copy(),
                    )
                    if change_color_count == 1:
                        tmp_queue[0].set_style(
                            fill_color=RED_B, sheen_factor=0.15, sheen_direction=UR
                        )
                    elif change_color_count == 2:
                        tmp_queue[0].set_style(
                            fill_color="#ffb61e", sheen_factor=0.15, sheen_direction=UR
                        )
                    elif change_color_count == 3:
                        tmp_queue[0].set_style(
                            fill_color=PURPLE_B, sheen_factor=0.15, sheen_direction=UR
                        )
                    queue_all.add(tmp_queue)
                    if i == len(pre_list):
                        return node
                    pop_father += 1
                    change_color_count += 1

        def lo(node):
            nonlocal string_Traverse
            if node != None:
                pass
            queue = []
            queue.append(node)
            last = node
            level = 1
            while queue:
                node = queue.pop(0)
                string_Traverse += node.value
                if node.leftChild:
                    nlast = node.leftChild
                    queue.append(node.leftChild)
                if node.rightChild:
                    nlast = node.rightChild
                    queue.append(node.rightChild)
                if node == last and queue:
                    last = nlast
                    level += 1

        tmp_treeNode = T_N(None)
        treeNode = loC(tmp_treeNode)
        if chose == 2:
            lo(treeNode)
        pre_list = nodeList_unzip  # 恢复 pre_list

        animation_value_stringTraverse = string_Traverse
        animation_stringTraverse_reveal = Text(
            "遍历结果:", font="思源宋体 Heavy", color=GOLD
        ).scale(0.7)
        animation_stringTraverse_reveal.align_to(frame_animation, LEFT).align_to(
            frame_animation, DOWN
        ).shift(UP * 0.6 + RIGHT * 1)
        animation_stringTraverse_value = VGroup()
        index_Traverse = 0
        for stringTraverse_value in animation_value_stringTraverse:
            stringTraverse_reveal_tmp = Text(
                stringTraverse_value, font="思源宋体 Heavy", color=BLACK
            ).scale(0.7)
            if stringTraverse_value == animation_value_stringTraverse[0]:
                stringTraverse_reveal_tmp.next_to(
                    animation_stringTraverse_reveal, RIGHT, buff=0.25
                )
            else:
                stringTraverse_reveal_tmp.move_to(
                    animation_stringTraverse_value[index_Traverse]
                )
                index_Traverse += 1
                stringTraverse_reveal_tmp.shift(RIGHT * 0.5)
            animation_stringTraverse_value.add(stringTraverse_reveal_tmp)
        animation_stringTraverse = VGroup(
            animation_stringTraverse_reveal, animation_stringTraverse_value
        )

        # 二叉树结点
        class TreeNode:
            def __init__(self, value):
                self.value = value
                self.leftChild = None
                self.rightChild = None

        # 层次建立二叉树(非动画演示)
        def __levelOrderCreate_forTraverse(node):
            global pre_list
            data = pre_list[0]
            node = TreeNode(data)
            Nodes = [node]
            i = 1
            element_all[i - 1].move_to(base_all[i - 1])
            for data in Nodes:
                if data != None:
                    data.leftChild = (
                        TreeNode(pre_list[i]) if pre_list[i] != flag else None
                    )
                    Nodes.append(data.leftChild)
                    element_all[i - 1].move_to(base_all[i - 1])
                    i += 1
                    if i == len(pre_list):
                        return node
                    data.rightChild = (
                        TreeNode(pre_list[i]) if pre_list[i] != flag else None
                    )
                    element_all[i - 1].move_to(base_all[i - 1])
                    i += 1
                    Nodes.append(data.rightChild)
                    if i == len(pre_list):
                        return node

        # 层次遍历二叉树
        def __levelOrderTraverse(node):
            nonlocal move_circle, queue_all
            global turn_on, count
            if node != None:
                pass
            queue = []
            queue.append(node)
            last = node
            level = 1
            i = 1
            move_count = 0
            last_queue = queue_all[i - 1]
            move_frame.set_width(
                ignore_space_len(codes_levelOrderTraverse[2], "lo", 2), stretch=True
            ).set_height(0.25, stretch=True).move_to(
                codes_levelOrderTraverse[2]
            ).align_to(
                codes_levelOrderTraverse[2], RIGHT
            ).shift(
                RIGHT * 0.05
            )
            self.play(ShowCreation(move_frame), Write(arrow))
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_levelOrderTraverse[3], "lo", 3),
                move_frame.move_to,
                codes_levelOrderTraverse[3],
                move_frame.align_to,
                codes_levelOrderTraverse[3],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.25, "stretch": True},
                run_time=1.5,
            )
            self.wait()
            move_circle_new_position = move_circle.copy()
            move_circle_new_position.move_to(base_all[i - 1])
            self.play(FadeIn(move_circle_new_position), FadeOut(move_circle))
            move_circle = move_circle_new_position
            self.wait()
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_levelOrderTraverse[4], "lo", 4),
                move_frame.move_to,
                codes_levelOrderTraverse[4],
                move_frame.align_to,
                codes_levelOrderTraverse[4],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.25, "stretch": True},
                run_time=1.5,
            )
            self.wait(0.5)
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_levelOrderTraverse[5], "lo", 5),
                move_frame.move_to,
                codes_levelOrderTraverse[5],
                move_frame.align_to,
                codes_levelOrderTraverse[5],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.25, "stretch": True},
                run_time=1.5,
            )
            self.wait()
            queue_all[i - 1].move_to(stack_frame).next_to(stack_left, RIGHT, buff=0.03)
            self.play(FadeInFrom(queue_all[i - 1], RIGHT))
            self.wait()
            # print("Level " + str(level) + ':', end=' ')  # 打印结点
            while queue:
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_levelOrderTraverse[6], "lo", 6),
                    move_frame.move_to,
                    codes_levelOrderTraverse[6],
                    move_frame.align_to,
                    codes_levelOrderTraverse[6],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.25, "stretch": True},
                    run_time=1.5,
                )
                self.wait(0.5)
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_levelOrderTraverse[8], "lo", 8),
                    move_frame.move_to,
                    codes_levelOrderTraverse[8],
                    move_frame.align_to,
                    codes_levelOrderTraverse[8],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.25, "stretch": True},
                    run_time=1.5,
                )
                self.wait()
                if turn_on == False:
                    turn_on = True
                    count += 1
                else:
                    move_circle_new_position = move_circle.copy()
                    move_circle_new_position.move_to(base_all[count - 1])
                    self.play(FadeIn(move_circle_new_position), FadeOut(move_circle))
                    move_circle = move_circle_new_position
                    count += 1
                    self.wait()
                node = queue.pop(0)
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_levelOrderTraverse[9], "lo", 9),
                    move_frame.move_to,
                    codes_levelOrderTraverse[9],
                    move_frame.align_to,
                    codes_levelOrderTraverse[9],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.25, "stretch": True},
                    run_time=1.5,
                )
                self.wait()
                move_queues = VGroup()
                if 2 * move_count <= 7:
                    for index_queue in range(move_count, 2 * move_count + 1):
                        move_queues.add(queue_all[index_queue])
                else:
                    for index_queue in range(move_count, 7):
                        move_queues.add(queue_all[index_queue])
                self.play(
                    move_queues.shift, LEFT * 1.155, FadeOutAndShift(move_queues[0], LEFT)
                )
                self.wait()
                # print(node.value, end=' ')  # 打印结点
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_levelOrderTraverse[10], "lo", 10),
                    move_frame.move_to,
                    codes_levelOrderTraverse[10],
                    move_frame.align_to,
                    codes_levelOrderTraverse[10],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.25, "stretch": True},
                    run_time=1.5,
                )
                self.wait()
                self.play(FadeIn(animation_stringTraverse[1][move_count]))
                self.wait()
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_levelOrderTraverse[11], "lo", 11),
                    move_frame.move_to,
                    codes_levelOrderTraverse[11],
                    move_frame.align_to,
                    codes_levelOrderTraverse[11],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.25, "stretch": True},
                    run_time=1.5,
                )
                self.wait()
                if node.leftChild:
                    nlast = node.leftChild
                    queue.append(node.leftChild)
                    i += 1
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(codes_levelOrderTraverse[12], "lo", 12),
                        move_frame.move_to,
                        codes_levelOrderTraverse[12],
                        move_frame.align_to,
                        codes_levelOrderTraverse[12],
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.25, "stretch": True},
                        run_time=1.5,
                    )
                    self.wait()
                    if i == 2:
                        queue_all[i - 1].move_to(stack_frame).next_to(
                            stack_left, RIGHT, buff=0.03
                        )
                    else:
                        queue_all[i - 1].next_to(last_queue, buff=0.055)
                    self.play(FadeInFrom(queue_all[i - 1], RIGHT))
                    last_queue = queue_all[i - 1]
                    self.wait()
                self.play(
                    move_frame.set_width,
                    ignore_space_len(codes_levelOrderTraverse[13], "lo", 13),
                    move_frame.move_to,
                    codes_levelOrderTraverse[13],
                    move_frame.align_to,
                    codes_levelOrderTraverse[13],
                    RIGHT,
                    move_frame.shift,
                    RIGHT * 0.05,
                    move_frame.set_height,
                    {"height": 0.25, "stretch": True},
                    run_time=1.5,
                )
                self.wait()
                if node.rightChild:
                    nlast = node.rightChild
                    queue.append(node.rightChild)
                    i += 1
                    self.play(
                        move_frame.set_width,
                        ignore_space_len(codes_levelOrderTraverse[14], "lo", 14),
                        move_frame.move_to,
                        codes_levelOrderTraverse[14],
                        move_frame.align_to,
                        codes_levelOrderTraverse[14],
                        RIGHT,
                        move_frame.shift,
                        RIGHT * 0.05,
                        move_frame.set_height,
                        {"height": 0.25, "stretch": True},
                        run_time=1.5,
                    )
                    self.wait()
                    queue_all[i - 1].next_to(last_queue, buff=0.055)
                    self.play(FadeInFrom(queue_all[i - 1], RIGHT))
                    last_queue = queue_all[i - 1]
                    self.wait()
                if node == last and queue:
                    last = nlast
                    # print()  # 打印结点
                    level += 1
                    # print("Level " + str(level) + ":", end=' ')  # 打印结点
                move_count += 1
            self.play(
                move_frame.set_width,
                ignore_space_len(codes_levelOrderTraverse[6], "lo", 6),
                move_frame.move_to,
                codes_levelOrderTraverse[6],
                move_frame.align_to,
                codes_levelOrderTraverse[6],
                RIGHT,
                move_frame.shift,
                RIGHT * 0.05,
                move_frame.set_height,
                {"height": 0.25, "stretch": True},
                run_time=1.5,
            )
            self.wait()

        # ------------------------------ 动画演示 ------------------------------
        #  1: 层次建立二叉树   2: 层次遍历二叉树
        if chose == 1:
            pass
        elif chose == 2:
            treeNode_tmp = TreeNode(None)
            treeNode = __levelOrderCreate_forTraverse(treeNode_tmp)
            pre_list = nodeList_unzip  # 恢复 pre_list
            self.add(stack_left, stack_right, arrow_in_left, arrow_in_right)
            self.add(animation_stringTraverse[0])
            self.add(base_all, line_all, element_all)
            self.add(stack_frame, stack_current)
            self.wait(0.5)
            treeNodeTraverse = __levelOrderTraverse(treeNode)
            self.play(FadeOut(move_frame), FadeOut(arrow), FadeOut(move_circle))
            self.wait()
