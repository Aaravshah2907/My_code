from manim import *


# Manim LOGO Demo
class ManimCELogo(Scene):
    def construct(self):
        self.camera.background_color = "#ece6e2"
        logo_green = "#87c2a5"
        logo_blue = "#525893"
        logo_red = "#e07a5f"
        logo_black = "#343434"
        ds_m = MathTex(r"\mathbb{M}", fill_color=logo_black).scale(7)
        ds_m.shift(2.25 * LEFT + 1.5 * UP)
        circle = Circle(color=logo_green, fill_opacity=1).shift(LEFT)
        square = Square(color=logo_blue, fill_opacity=1).shift(UP)
        triangle = Triangle(color=logo_red, fill_opacity=1).shift(RIGHT)
        logo = VGroup(triangle, square, circle, ds_m)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)


class MyNameInLatex(Scene):
    def construct(self):
        logo_black = "#343434"
        a1 = MathTex(r"\mathbb{A}", fill_color=logo_black).scale(7)
        a2 = MathTex(r"\mathbb{A}", fill_color=logo_black).scale(7).next_to(a1).shift(LEFT)
        r1 = MathTex(r"\mathbb{R}", fill_color=logo_black).scale(7).next_to(a2).shift(LEFT)
        a3 = MathTex(r"\mathbb{A}", fill_color=logo_black).scale(7).next_to(r1).shift(LEFT)
        v1 = MathTex(r"\mathbb{V}", fill_color=logo_black).scale(7).next_to(a3).shift(LEFT).shift(LEFT).shift(DOWN)
        Name_Latex = VGroup(a1, a2, r1, a3, v1)
        Name_Latex.move_to(ORIGIN)
        self.add(Name_Latex)
