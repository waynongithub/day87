from turtle import Turtle


class Score(Turtle):
    def __init__(self, level, bricks_destroyed):
        super().__init__()
        self.hideturtle()
        self.destroyed_bricks_count = 0
        self.balls_left = 5
        self.level = 1
        self.penup()
        self.color('orange')
        self.goto(140, 0)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"LEVEL: {self.level}\nSCORE: {self.destroyed_bricks_count}\nBALLS LEFT: {self.balls_left}",
                   font=('Courier', 15, 'normal'))

    def brick_destroyed(self):
        print(f"in brick_destroyed, count={self.destroyed_bricks_count}")
        self.destroyed_bricks_count += 1
        self.update_score()

    def next_level(self):
        self.level += 1
        self.update_score()

    def new_ball(self):
        self.balls_left -= 1
        self.update_score()

    def game_over(self):
        self.goto(0, -100)
        self.color('yellow')
        self.write(f"GAME OVER", align='center', font=('Courier', 45, 'bold'))