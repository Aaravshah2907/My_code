from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class SquareToCircle(Scene):
    def construct(self):
        square = Square()
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(square))
        self.play(Transform(square, circle))


class AnimatedCircleToSquare(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square
        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(square.animate.set_fill(PINK, opacity=0.5))  # color the circle on screen


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2)
        self.wait()


class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5)  # wait for 0.5 seconds
        self.replacement_transform()


class TransformCycle(Scene):
    def construct(self):
        a = Circle()
        t1 = Square()
        t2 = Triangle()
        self.add(a)
        self.wait()
        for t in [t1, t2]:
            self.play(Transform(a, t))


class ArrowExample(Scene):
    def construct(self):
        left_group = VGroup()
        # As buff increases, the size of the arrow decreases.
        for buff in np.arange(0, 2.2, 0.45):
            left_group += Arrow(buff=buff, start=2 * LEFT, end=2 * RIGHT)
        # Required to arrange arrows.
        left_group.arrange(DOWN)
        left_group.move_to(4 * LEFT)

        middle_group = VGroup()
        # As max_stroke_width_to_length_ratio gets bigger,
        # the width of stroke increases.
        for i in np.arange(0, 5, 0.5):
            middle_group += Arrow(max_stroke_width_to_length_ratio=i)
        middle_group.arrange(DOWN)

        UR_group = VGroup()
        # As max_tip_length_to_length_ratio increases,
        # the length of the tip increases.
        for i in np.arange(0, 0.3, 0.1):
            UR_group += Arrow(max_tip_length_to_length_ratio=i)
        UR_group.arrange(DOWN)
        UR_group.move_to(4 * RIGHT + 2 * UP)

        DR_group = VGroup()
        DR_group += Arrow(start=LEFT, end=RIGHT, color=BLUE, tip_shape=ArrowSquareTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=BLUE, tip_shape=ArrowSquareFilledTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=YELLOW, tip_shape=ArrowCircleTip)
        DR_group += Arrow(start=LEFT, end=RIGHT, color=YELLOW, tip_shape=ArrowCircleFilledTip)
        DR_group.arrange(DOWN)
        DR_group.move_to(4 * RIGHT + 2 * DOWN)

        self.add(left_group, middle_group, UR_group, DR_group)


# This is ManimCELogo
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
        logo = VGroup(triangle, square, circle,ds_m)  # order matters
        logo.move_to(ORIGIN)
        self.add(logo)


class BraceAnnotation(Scene):
    def construct(self):
        dot = Dot([-2, -1, 0])
        dot2 = Dot([2, 1, 0])
        line = Line(dot.get_center(), dot2.get_center()).set_color(ORANGE)
        b1 = Brace(line)
        b1text = b1.get_text("Horizontal distance")
        b2 = Brace(line, direction=line.copy().rotate(PI / 2).get_unit_vector())
        b2text = b2.get_tex("x-x_1")
        self.add(line, dot, dot2, b1, b2, b1text, b2text)


class VectorArrow(Scene):
    def construct(self):
        dot = Dot(ORIGIN)
        arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
        numberplane = NumberPlane()
        origin_text = Text('(0, 0)').next_to(dot, DOWN)
        tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
        self.add(numberplane, dot, arrow, origin_text, tip_text)


class BooleanOperations(Scene):
    def construct(self):
        ellipse1 = Ellipse(
            width=4.0, height=5.0, fill_opacity=0.5, color=BLUE, stroke_width=10
        ).move_to(LEFT)
        ellipse2 = ellipse1.copy().set_color(color=RED).move_to(RIGHT)
        bool_ops_text = MarkupText("<u>Boolean Operation</u>").next_to(ellipse1, UP * 3)
        ellipse_group = Group(bool_ops_text, ellipse1, ellipse2).move_to(LEFT * 3)
        self.play(FadeIn(ellipse_group))

        i = Intersection(ellipse1, ellipse2, color=GREEN, fill_opacity=0.5)
        self.play(i.animate.scale(0.25).move_to(RIGHT * 5 + UP * 2.5))
        intersection_text = Text("Intersection", font_size=23).next_to(i, UP)
        self.play(FadeIn(intersection_text))

        u = Union(ellipse1, ellipse2, color=ORANGE, fill_opacity=0.5)
        union_text = Text("Union", font_size=23)
        self.play(u.animate.scale(0.3).next_to(i, DOWN, buff=union_text.height * 3))
        union_text.next_to(u, UP)
        self.play(FadeIn(union_text))

        e = Exclusion(ellipse1, ellipse2, color=YELLOW, fill_opacity=0.5)
        exclusion_text = Text("Exclusion", font_size=23)
        self.play(e.animate.scale(0.3).next_to(u, DOWN, buff=exclusion_text.height * 3.5))
        exclusion_text.next_to(e, UP)
        self.play(FadeIn(exclusion_text))

        d = Difference(ellipse1, ellipse2, color=PINK, fill_opacity=0.5)
        difference_text = Text("Difference", font_size=23)
        self.play(d.animate.scale(0.3).next_to(u, LEFT, buff=difference_text.height * 3.5))
        difference_text.next_to(d, UP)
        self.play(FadeIn(difference_text))


class GradientImageFromArray(Scene):
    def construct(self):
        n = 256
        imageArray = np.uint8(
            [[i * 256 / n for i in range(0, n)] for _ in range(0, n)]
        )
        image = ImageMobject(imageArray).scale(2)
        image.background_rectangle = SurroundingRectangle(image, GREEN)
        self.add(image, image.background_rectangle)
