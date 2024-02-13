from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.width = 5
        self.shapesize(1, self.width)
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, -280)
        self.left_edge = 0
        self.right_edge = 0
        self.recalculate_edges()
        self.showturtle()


    def move_left(self):
        newx = self.xcor() - 50
        self.goto(newx, -280)
        self.recalculate_edges()

    def move_right(self):
        newx = self.xcor() + 50
        self.goto(newx, -280)
        self.recalculate_edges()

    def recalculate_edges(self):
        x, y = self.pos()
        self.left_edge = x - (20 * self.width)
        self.right_edge = x + (20 * self.width)
        print(f"pos={x}, edges are {self.left_edge}, {self.right_edge}, y={y}")

