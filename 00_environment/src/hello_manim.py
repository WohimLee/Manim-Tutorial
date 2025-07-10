from manim import *

class HelloWorld(Scene):
    def construct(self):
        # 创建文字对象
        text = Text("Hello, Manim!")
        
        # 显示文字
        self.play(Write(text))
        self.wait(1)

        # 向右移动文字
        self.play(text.animate.shift(RIGHT * 2))
        self.wait(1)

        # 文字渐变消失
        self.play(FadeOut(text))
