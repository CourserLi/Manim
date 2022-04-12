```python
'''
map地址：rec_map、num_map
固定长条：rec_base_position == rec_fix
长条：rec_base
数字：rec_coordinate
原数组：rec_height_chaos == R
'''
# 移动1
self.play(rec_map[j].move_to, rec_base_position[j+1],
                          rec_map[j].align_to, rec_base_position[j+1], DOWN,
                          num_map[j].shift, RIGHT*1.3)
# map交换1
rec_map[j+1] = rec_map[j]
num_map[j+1] = num_map[j]
# 移动2
self.play(FadeOut(rec_base[pos]), FadeOut(rec_coordinate[pos])) # tmp的长条和数字消失
rec_base[pos].move_to(rec_base_position[int(low)]).align_to(rec_base_position[int(low)], DOWN) # tmp的长条移动到顺序空位
rec_coordinate[pos].move_to(rec_map[int(low)]) # tmp的数字移动到顺序空位
self.play(FadeIn(rec_base[pos]), FadeIn(rec_coordinate[pos])) # tmp的长条和数字出现
# map交换2
rec_map[int(low)] = rec_base[pos]
num_map[int(low)] = rec_coordinate[pos]

```

目前缺少代码框移动 与 变量框变换

```python
'''
all_num = VGroup(Rm_num, high_num, mid_num, low_num, pos_num, j_num)
all_num[0]: R[mid]
all_num[1]: high
all_num[2]: mid
all_num[3]: low
all_num[4]: pos
all_num[5]: j
'''

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
```

最后一步是代码框重新回大的 for 循环，且指针 pos 向右移动伴随消失

```python
# 额外的 -1 下标
extra_subscript = (
    Text(str(-1), font="思源宋体 Heavy", color=BLACK)
    .scale(0.4)
    .move_to(rec_subscript[0])
    .shift(LEFT*0.6)
)

FadeIn(extra_subscript)
FadeOut(extra_subscript)

self.play(FadeOut(extra_subscript) if 1 == -1 else FadeIn(NULL))
```

`while(low<=high)` 转 `for(j=pos-1;;)` 时 三个指针同时消失，即 `code_move(i,j,st)`【√】

`for(j=pos-1;;)` 转 `R[low]=tmp` 时 `extra_subscript` 和 指针 j 同时消失【√】

改函数 `FadeIn()` 和 `FadeOut()` 末尾添加 `self.wait()`【参数包括多个出现的（消失的） + `run_time` + `self.wait`】【√】

第一个用面向过程直接写（目的包括使变量框值逐渐出现）【√】

```python
for pos in range(2,8):
    code_move(0, 2)
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
    high = pos-1
    vec_high_all.next_to(rec_fix[high], DOWN, buff=0.35)
    self.play(FadeIn(vec_high_all), renew_variable('high', high))
    self.wait()
    # 指针 pos 消失
    self.play(FadeOut(vec_pos_all))
    self.wait()
    # 面向对象二 (low | high | mid 的变化)
    low, high = while_OOP(low, high, tmp)
    # 面向对象三 (元素长条的移动)
    for_OOP(pos, low, high, tmp)
    self.wait()
```

下一个动画开始，整体布局，采用伪面向对象(OOP)模式

```python
def FadeIO(*method, run_time=1, wait_time=1):
    self.play(*method, run_time=run_time)
    self.wait(wait_time)
# 举例
FadeIO(FadeIn(vec_high_all), FadeIn(vec_low_all), run_time=1.5, wait_time=2)
```

参考 impromptu.md 上的建议
