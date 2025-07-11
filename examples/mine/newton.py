# 从 Manim 中导入所有类和函数
from manim import *

# 定义一个继承自 Scene 的类，用于创建动画
class NewtonsMethod(Scene):
    def construct(self):
        # 定义目标函数 f(x) = x^3 - x - 2
        def f(x): return 0.5*(x**2-2)**2
        
        # 定义 f(x) 的导数 f'(x) = 2(x^2 - 2)，用于牛顿法
        def df(x): return 2 * x * (x**2 - 2)

        # 创建坐标轴对象，设置 x 和 y 范围，不显示箭头尖
        axes = Axes(
            x_range=[-2, 5],               # x轴范围
            y_range=[-10, 10],               # y轴范围
            axis_config={"include_tip": False}  # 不显示轴的箭头尖
        )

        graph = axes.plot(f, color=BLUE)

        formula = MathTex(r"f(x)=\frac{1}{2}(x^2 - 2)^2")

        # 给函数图像添加一个标签“f(x)”放在右上方
        label = axes.get_graph_label(
            graph, 
            label=formula, 
            x_val=3, 
            direction=UR
        )

        self.play(Create(axes), Create(graph), Write(label))
        self.wait(1)

        # 设置牛顿法的初始点 x₀ = 2.0
        x = 2.5

        # 在图像上的 f(x₀) 位置放一个红点，表示起始点
        dot = Dot(axes.coords_to_point(x, f(x)), color=RED)
        self.play(FadeIn(dot))

        # # 进行 3 次牛顿迭代
        # for _ in range(3):
        #     x_old = x              # 保存上一次的 x 值
        #     y = f(x)               # 计算 f(x)
        #     slope = df(x)          # 计算导数 f'(x)
        #     x = x - y / slope      # 应用牛顿迭代公式更新 x 值

        #     # 在 x_old 处画出函数图像的切线
        #     tangent = graph.get_secant_slope_group(
        #         x_old,             # 切线起点 x
        #         f_graph,           # 传入图像对象（注意不能是函数）
        #         dx=0.01,           # 小的增量，用于近似切线
        #         secant_line_color=YELLOW  # 切线颜色为黄色
        #     )

        #     # 播放动画：画出切线
        #     self.play(Create(tangent))

        #     # 在切线与 x 轴的交点处放一个绿点，表示下一步的 x₁
        #     next_dot = Dot(graph.coords_to_point(x, 0), color=GREEN)

        #     # 播放动画：绿点出现，红点移动到新的 (x₁, f(x₁)) 位置
        #     self.play(FadeIn(next_dot), dot.animate.move_to(graph.coords_to_point(x, f(x))))

        #     # 暂停 0.5 秒以便观看
        #     self.wait(0.5)

        # # 动画结束前再停留 2 秒
        # self.wait(2)
