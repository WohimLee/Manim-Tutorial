
from manim import *

class SqrtRootScene(Scene):
    def construct(self):
        self.show_title()
        self.show_goal()
        self.solution_process()
        # self.derive_derivative()
        # self.show_final_note()

    def show_title(self):
        title = Text("Solving Square Roots", font_size=60)

        self.play(FadeIn(title))
        self.wait(1)
        self.play(FadeOut(title))

    def show_goal(self):
        texts = VGroup(
            Tex(r"We want to find the value of $\sqrt{a}$"),
            Tex(r"which is the square root of $a$")
        ).arrange(DOWN, aligned_edge=ORIGIN, buff=0.4).shift(UP * 0.5)

        # # 一行一行显示（推荐方式 1）
        # for line in texts:
        #     self.play(Write(line))
        #     self.wait(0.5)

        # 或者使用 LaggedStart（推荐方式 2）
        self.play(LaggedStart(*[Write(line) for line in texts], lag_ratio=0.9))
        self.wait(1)
        self.play(FadeOut(texts))

    def solution_process(self):
        # Step 1: 显示假设与初始等式
        assume = Tex(r"Assume $\sqrt{a} = x$, then:")
        equation = Tex(r"$x = \sqrt{a}$")

        step_group = VGroup(assume, equation).arrange(DOWN, aligned_edge=ORIGIN).shift(UP*0.5)
        
        self.play(Write(step_group))
        self.wait()

        # Step 2: 移除假设语句，保留公式并上移
        self.play(FadeOut(assume, shift=UP))
        self.play(equation.animate.shift(UP*2.5))
        self.wait()

        new_equation = self.math_manipulation(equation)

    def math_manipulation(self, extra_mobjects=None):

        steps = [
            ("First, square both sides.", [r"x^2", "=", "a"]),
            ("Rearrange the equation.", [r"x^2 - a", "=", "0"]),
            ("Square both sides again.", [r"(x^2 - a)^2", "=", "0"]),
            ("Multiply both sides by 1/2.", [r"\frac{1}{2}(x^2 - a)^2", "=", "0"]),
        ]

        explanations = []
        equations = []

        # 用于统一管理所有展示的元素
        all_mobjects = VGroup()

        for text, eq in steps:
            explanations.append(Text(text, font_size=32))
            equations.append(MathTex(*eq, font_size=45))

        # Arrange them step by step vertically
        for i in range(len(steps)):
            explanations[i].to_edge(LEFT*6).shift(UP * (1.5 - i*1))
            equations[i].next_to(explanations[i], RIGHT, buff=0.8)
            all_mobjects.add(explanations[i], equations[i])

        # Animate them one by one
        for i in range(len(steps)):
            self.play(Write(explanations[i]))
            self.play(Write(equations[i]))
            self.wait(1)

        # Add note at the end
        note = Tex(
            r"Note: We use",r" $\frac{1}{2}$", r" for convenience — any constant works, since the derivative removes constants.",
            font_size=30
        )
        note.to_edge(DOWN)
        self.play(FadeIn(note))
        self.wait(1)

        all_mobjects.add(note)
        if extra_mobjects:
            all_mobjects.add(*extra_mobjects)

        self.play(Indicate(equations[3], scale_factor=1.5))

        # 清屏
        all_mobjects.remove(equations[3])
        self.play(
            FadeOut(all_mobjects),
            equations[3].animate.move_to(UP*2)
            )
        self.wait(1)
        
        ### === 开始转换公式 === ###

        # 移除 "= 0"
        self.play(FadeOut(equations[3][1]), FadeOut(equations[3][2]))
        self.wait(0.3)

        # 创建新公式前缀
        new_eq = MathTex(r"\text{Define: } f(x) =", r"\frac{1}{2}(x^2 - a)^2", font_size=45)
        new_eq.move_to(equations[3].get_center())

        # 动画替换核心部分，写入前缀
        self.play(
            Transform(equations[3][0], new_eq[1]),  # 替换主体部分
            Write(new_eq[0])                 # 写入 Define: f(x) =
        )
        self.wait(1)

        # === 添加 f(x) 的分析步骤 === #
        # 提前对其位置设置（靠下）
        steps = VGroup(
            Tex(r"Then the range of $f(x)$ is: $f(x) \geq 0$", font_size=45),
            Tex(r"So the problem becomes:", font_size=45),
            Tex(r"Find the minimum value of $f(x)$", font_size=45)
        ).arrange(DOWN, buff=0.6)
        steps.next_to(new_eq, DOWN, buff=1.2)

        # 动画逐条展示
        for step in steps:
            self.play(Write(step))
            self.wait(1)

        self.wait(2)


    def derive_derivative(self):
        derivative = Tex(r"$f'(x) = 2x(x^2 - a)$")
        self.play(Write(derivative))
        self.wait(3)

    def show_final_note(self):
        final_note = Tex(r"Therefore, $\sqrt{a}$ can be found by minimizing $f(x)$!")
        self.play(Write(final_note))
        self.wait(3)
