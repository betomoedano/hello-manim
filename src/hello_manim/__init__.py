from manim import *

BLUE = "#0A84FF"

class CreateCircle(Scene):
    def construct(self):
        circle = Circle(
            color=WHITE,
            fill_color=WHITE,
            fill_opacity=1
        )  # create a circle
        square = Square(
            color=BLUE,
            fill_color=BLUE,
            fill_opacity=1
        )  # create a square

        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.next_to(circle)  # position next to the circle
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle(
            color=WHITE
        )
        square = Square()

        self.play(Create(square))
        self.play(square.animate.rotate(PI / 4)) # rotate the square
        self.play(Transform(square, circle))
        self.play(square.animate.set_fill(BLUE, opacity=1))

        newSquare = Square()
        newSquare.set_fill(BLUE, opacity=1)

        self.play(Transform(square, newSquare)) # square is a square again
        
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


class Shapes(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        triangle = Triangle()

        circle.shift(LEFT)
        square.shift(UP)
        triangle.shift(RIGHT)

        self.add(circle, square, triangle)
        self.wait(1)


class MobjectStyling(Scene):
    def construct(self):
        circle = Circle().shift(LEFT)
        square = Square().shift(UP)
        triangle = Triangle().shift(RIGHT)

        circle.set_stroke(color=GREEN, width=20)
        square.set_fill(YELLOW, opacity=1.0)
        triangle.set_fill(PINK, opacity=0.5)

        self.add(circle, square, triangle)
        self.wait(1)


class ExampleTransform(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1 = Square().set_color(RED)
        m2 = Rectangle().set_color(RED).rotate(0.2)
        self.play(Transform(m1,m2))


class ExampleRotation(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        m1a = Square().set_color(RED).shift(LEFT)
        m1b = Circle().set_color(RED).shift(LEFT)
        m2a = Square().set_color(BLUE).shift(RIGHT)
        m2b = Circle().set_color(BLUE).shift(RIGHT)

        points = m2a.points
        points = np.roll(points, int(len(points)/4), axis=0)
        m2a.points = points

        self.play(Transform(m1a,m1b),Transform(m2a,m2b), run_time=1)

def subtle_bounce(t):
      normal = smooth(t)
      bounce = rate_functions.ease_out_back(t)

      return 0.3 * normal + 0.7 * bounce

class CodeWithBeto(Scene):
    def construct(self):
        logo = ImageMobject("logo-white-transparent.png")
        logo.width = .7

        self.play(
            SpinInFromNothing(
                logo,
                angle=PI / 4,
                run_time=0.8,
                rate_func=subtle_bounce,
            )
        )

        label = Text("cwb.sh", font="SF Pro Rounded", weight=BOLD)

        # Calculate the final centered layout without moving the visible logo yet.
        final_logo = logo.copy()
        final_layout = Group(final_logo, label)
        final_layout.arrange(RIGHT, buff=0.25)
        final_layout.move_to(ORIGIN)

        launch_point = final_logo.get_right() + RIGHT * 0.05

        for character in label:
            character.save_state()
            character.move_to(launch_point)
            character.scale(0.6)
            character.set_opacity(0)

        self.add(label)

        self.play(
            AnimationGroup(
                logo.animate(
                    run_time=0.7,
                    rate_func=rate_functions.ease_out_cubic,
                ).move_to(final_logo),
                Succession(
                    Wait(0.10),
                    LaggedStart(
                        *[
                            Restore(
                                character,
                                rate_func=rate_functions.ease_out_cubic,
                            )
                            for character in label
                        ],
                        lag_ratio=0.08,
                        run_time=.5,
                    ),
                ),
                lag_ratio=0,
            ),
        )
        self.wait(.5)
