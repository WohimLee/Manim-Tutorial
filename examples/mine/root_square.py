from manim import *

class SqrtRootScene(Scene):
    def construct(self):
        # 1. Title: Solving Square Roots
        title = Text("Solving Square Roots")
        self.play(FadeIn(title))
        self.wait(1)

        # 2. Goal
        target1 = Tex(r"We want to find the value of $\sqrt{a}$, which is the square root of $a$")
        target2 = Tex(r"which is the square root of $a$")

        target1.next_to(title, DOWN)
        target2.next_to(target1, DOWN)

        
        self.play(Write(target1))
        self.play(Write(target2))

        self.wait(2)

        self.play(FadeOut(target1), FadeOut(target2))

        # 3. Turn into an equation
        step1 = Tex(r"Assume $\sqrt{a} = x$, then:", r"$x = \sqrt{a}$")
        step1.arrange(DOWN, aligned_edge=ORIGIN)
        step1.next_to(title, DOWN)
        self.play(Write(step1))
        self.wait(2)
        self.play(FadeOut(step1))


        # 4. Mathematical manipulation
        equations = VGroup(
            Tex(r"$x^2 = a$"),
            Tex(r"$x^2 - a = 0$"),
            Tex(r"$(x^2 - a)^2 = 0$"),
            Tex(r"$\frac{1}{2}(x^2 - a)^2 = 0$\quad\text{(constant can be changed)}")
        ).arrange(DOWN, aligned_edge=ORIGIN, buff=0.5)
        equations.next_to(title, DOWN)
        self.play(LaggedStartMap(Write, equations, lag_ratio=0.6))
        self.wait(2)

        self.play(FadeOut(equations))

        # 5. Define new function
        func_def = Tex(r"Define: $f(x) = \frac{1}{2}(x^2 - a)^2$")
        domain_info1 = Tex(r"$f(x) \geq 0$, so the problem becomes:")
        domain_info2 = Tex(r"find the minimum value of $f(x)$")

        func_def.next_to(title, DOWN)
        domain_info1.next_to(func_def, DOWN)
        domain_info2.next_to(domain_info1, DOWN)

        self.play(Write(func_def))
        self.play(Write(domain_info1))
        self.play(Write(domain_info2))

        self.wait(2)

        # 6. Derivative derivation
        derivative = Tex(r"$f'(x) = 2x(x^2 - a)$")
        derivative.next_to(domain_info2, DOWN, buff=0.8)
        self.play(Write(derivative))
        self.wait(3)

        # Ending
        self.play(
            FadeOut(func_def), 
            FadeOut(domain_info1), 
            FadeOut(domain_info2), 
            FadeOut(derivative), 
            FadeOut(title)
        )
        final_note = Tex(r"Therefore, $\sqrt{a}$ can be found by minimizing $f(x)$!")
        self.play(Write(final_note))
        self.wait(3)
