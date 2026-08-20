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
        
