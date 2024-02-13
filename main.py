from turtle import Screen
from ball import Ball
from player import Player
from brick import Brick
from score import Score
import time

screen = Screen()
screen.setup(800, 600)
screen.bgcolor('black')
screen.tracer(0) # speeds up setting up the board
screen.listen()


def end_game():
    screen.bgcolor('coral')


ball = Ball()
player = Player()
score = Score(level=1, bricks_destroyed=0)
bricks = []


def place_bricks():
    for y in (270, 240, 210, 180):
        for x in range(-330, 350, 110):
            # print(f"brick {x}, {y}")
            bricks.append(Brick((x, y)))
# screen.tracer(3)

place_bricks()

screen.onkey(key="z", fun=end_game)
screen.onkey(key="Left", fun=player.move_left)
screen.onkey(key="Right", fun=player.move_right)

# screen.exitonclick()
while score.balls_left > 0:
    screen.update()
    ball.move()

    if ball.ycor() <= -260 and (player.left_edge < ball.xcor() < player.right_edge):
        ball.bounce_y()

    if ball.ycor() < -280:
        print("ball is lost")
        score.new_ball()
        ball.goto(0, -400)
        ball.reset()
        ball = Ball()
        ball.reset_position()

    if ball.ycor() > 160:
        for brick in bricks:
            if ((brick.ycor - 20) <= ball.ycor() <= (brick.ycor + 20)) and (
                    brick.xcor - 60 < ball.xcor() < brick.xcor + 60) and ball.y_move > 0:
                brick.goto(1000, 1000)
                ball.y_move *= -1
                bricks.remove(brick)
                score.brick_destroyed()
                if len(bricks) == 0:
                    score.next_level()
                    ball.x_move += 3
                    ball.y_move += 3
                    place_bricks()
    time.sleep(0.017)

    if score.balls_left == 0:
        score.game_over()

screen.exitonclick()
print(f"after the while loop")