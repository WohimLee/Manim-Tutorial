from manim import *

class LossFunctionIntro(Scene):
    def construct(self):
        title = Title("什么是损失函数 (Loss Function)")
        self.play(Write(title))
        self.wait(1)

        # 简单定义
        definition = Text("损失函数 = 告诉模型“你错了多少！”", font_size=36)
        self.play(Write(definition))
        self.wait(2)
        self.play(definition.animate.shift(UP * 2))

        # 投篮比喻
        analogy = Text("🎯 类比：投篮练习", font_size=32)
        bullet_points = BulletedList(
            "你向篮筐投球",
            "偏差越大 = 损失越大",
            "不断调整投篮角度 → 损失减小",
            font_size=30
        ).next_to(analogy, DOWN)

        self.play(Write(analogy))
        self.play(FadeIn(bullet_points, shift=UP))
        self.wait(2)

        # 模拟投篮动画
        ball = Dot(radius=0.15, color=RED).move_to(LEFT * 4 + DOWN * 2)
        hoop = Circle(radius=0.3, color=BLUE).move_to(RIGHT * 3 + DOWN * 1.5)
        self.play(FadeIn(ball), FadeIn(hoop))
        self.wait(0.5)

        # 投篮轨迹（偏离）
        bad_trajectory = ArcBetweenPoints(ball.get_center(), hoop.get_center() + LEFT * 1, angle=PI/4)
        self.play(MoveAlongPath(ball, bad_trajectory), run_time=2)
        self.wait(0.5)

        # 显示偏差距离
        error_arrow = Arrow(start=ball.get_center(), end=hoop.get_center(), color=YELLOW)
        error_text = Text("偏差距离 = 损失", font_size=28).next_to(error_arrow, UP)
        self.play(GrowArrow(error_arrow), Write(error_text))
        self.wait(2)

        self.play(FadeOut(ball), FadeOut(hoop), FadeOut(error_arrow), FadeOut(error_text), FadeOut(analogy), FadeOut(bullet_points))

        # 模型训练流程
        train_steps = BulletedList(
            "模型预测：比如房价预测 100 万",
            "计算损失：真实值是 120 万，损失 = 20 万",
            "调整模型参数",
            "重复训练直到损失最小",
            font_size=30
        )
        self.play(Write(train_steps))
        self.wait(3)
        self.play(FadeOut(train_steps), FadeOut(definition), FadeOut(title))
