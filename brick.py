from turtle import Turtle
from random import randint, choice


class Brick(Turtle):
    def __init__(self, position):
        super().__init__()
        colors = ['red', 'blue', 'yellow', 'purple', 'green', 'orange']
        self.color(choice(colors))
        self.hideturtle()
        self.shape('square')
        self.speed('fastest')
        self.width = 5
        self.shapesize(1, self.width)
        self.penup()
        self.xcor, self.ycor = position
        self.goto(self.xcor, self.ycor)
        self.bottom_edge = self.ycor - 20
        self.top_edge = self.ycor + 20
        self.right_edge = self.xcor + (20 * self.width)
        self.left_edge = self.xcor - (20 * self.width)
        # print(f"xcor={self.xcor}, ycor={self.ycor}")
        self.showturtle()