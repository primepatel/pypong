from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from score import Scoreboard

screen = Screen()

screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0) # turn off the animation

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_over = False
while not game_over:
    sleep(0.1)
    screen.update()
    ball.move()
    # ball's collision with top or bottom wall
    if abs(ball.ycor()) > 280:
        ball.bounce_y()
        
    # detect collision with r paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() >330:
        ball.bounce_x()
    
    if ball.distance(l_paddle) < 50 and ball.xcor() <-330:
        ball.bounce_x()
    
    # detext r paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.add_lscore()
        scoreboard.update_score()
    
    # detext l paddle misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.add_rscore()
        scoreboard.update_score()

screen.exitonclick()