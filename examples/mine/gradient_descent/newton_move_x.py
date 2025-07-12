from manim import *

class NewtonsMethod(MovingCameraScene):
    def construct(self):
        # 定义目标函数 f(x) = 0.5*(x^2 - 2)^2
        def f(x): return 0.5 * (x**2 - 2)**2
        def df(x): return 2 * x * (x**2 - 2)

        # 创建坐标轴
        axes = Axes(
            x_range=[-2, 5, 1],
            y_range=[-1, 10, 2],
            axis_config={
                "include_tip": False,
                "include_numbers": True,
            },
            x_axis_config={
                "numbers_to_include": [i for i in range(-2, 6) if i != 0],
                "label_direction": DOWN,
            },
            y_axis_config={
                "numbers_to_include": [i for i in range(2, 11, 2)],
                "label_direction": LEFT,
            }
        )

        # 原点标记“O”
        origin_label = MathTex("O").next_to(axes.c2p(0, 0), DOWN + LEFT, buff=0.2)
        origin_dot = Dot(axes.c2p(0, 0), color=WHITE)

        # 绘制函数图像
        graph = axes.plot(f, color=BLUE)
        formula = MathTex(r"f(x)=\frac{1}{2}(x^2 - 2)^2")
        label = axes.get_graph_label(graph, label=formula, x_val=3, direction=UR)

        # 初始绘制
        self.play(FadeIn(axes), FadeIn(origin_label), FadeIn(origin_dot))
        self.play(Create(graph), Write(label), run_time=2, rate_func=linear)
        self.wait(0.5)

        # 设置牛顿法的初始点
        x_cur = 2.5
        moving_dot = Dot(axes.c2p(x_cur, 0), color=GREEN)
        self.play(FadeIn(moving_dot))
        
        # 进行多次牛顿迭代
        self.camera.frame.save_state() # 保存相机初始状态，Restore 使用
        for _ in range(3):
            
            # 从 x 轴的点画一条虚线连接到函数图像上
            v_line = DashedLine(
                start=axes.c2p(x_cur, 0),
                end=axes.c2p(x_cur, f(x_cur)),
                color=GRAY,
                dashed_ratio=0.5
            )
            self.play(Create(v_line))

            intersection = Dot(axes.c2p(x_cur, f(x_cur)), color=RED)
            self.play(FadeIn(intersection))

            x_old = x_cur
            y_old = f(x_old)
            slope = df(x_old)

            # 牛顿法公式：x_new = x_old - f(x)/f'(x)
            x_new = x_old - y_old / slope
            y_new = 0  # x 轴交点

            # 切线表达式
            tangent = axes.plot(
                lambda x_val: y_old + slope * (x_val - x_old),
                x_range=[x_old - 1.5, x_old + 1.5],
                color=YELLOW
            )
            self.play(Create(tangent), run_time=2, rate_func=linear)
            self.wait(1)

            # 新交点（x_new, 0）
            next_x_dot = Dot(axes.c2p(x_new, y_new), color=GREEN)

            # 镜头放大到新交点（x_new, 0）
            self.play(self.camera.frame.animate.scale(0.5).move_to(next_x_dot))

            # 移动到新交点（x_new, 0）
            self.play(moving_dot.animate.move_to(axes.c2p(x_new, 0)))
            self.wait(1)
            
            # 恢复画面大小
            self.play(Restore(self.camera.frame))

            self.wait(0.5)

            # 更新 x 值
            x_cur = x_new

            # 移除辅助图形（可选）
            self.play(FadeOut(tangent, intersection, v_line))
            # self.remove(tangent, intersection, v_line)

        self.wait(2)
