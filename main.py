from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("ping pong the game")
screen.tracer(0)
screen.bgpic("BG.png")


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down, "s")


game = True
while game:
    time.sleep(ball.level)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle)< 50 and ball.xcor() > 340 or ball.distance(l_paddle)<50 and ball.xcor()<-340:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()


screen.exitonclick()
