# Arrow

在 Manim 中，你可以通过以下参数来自定义 箭头大小、颜色、粗细、透明度等属性，无论是 Arrow 还是 CurvedArrow：

| 参数                               | 说明              | 示例                                   |
| -------------------------------- | --------------- | ------------------------------------ |
| `color`                          | 箭头颜色            | `color=RED`                          |
| `stroke_width`                   | 箭头线条粗细（默认 2）    | `stroke_width=4`                     |
| `max_tip_length_to_length_ratio` | 控制箭头头部占比（缩短箭头尖） | `max_tip_length_to_length_ratio=0.1` |
| `buff`                           | 箭头起止点与对象之间的间隔   | `buff=0.1`（默认）                       |
| `opacity`                        | 箭头整体透明度         | `opacity=0.8`                        |
| `tip_length`                     | 箭头尖长度           | `tip_length=0.2`                     |


>Example
```py
arrow = Arrow(
    start=equation.get_bottom(),
    end=new_equation.get_top(),
    buff=0.1,
    color=BLUE,            # 颜色设置
    stroke_width=5,        # 粗一点
    opacity=1.0,           # 不透明
    tip_length=0.25        # 箭头尖更明显
)
```