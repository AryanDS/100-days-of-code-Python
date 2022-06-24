from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time 
from scoreboard import Scoreboard

screen = Screen()
tim = Turtle()


screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)


l_paddle = Paddle(-350,0)
r_paddle = Paddle(350,0)
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")



is_game_on=True

while is_game_on:
    
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    #detecting collision with the top or bottom screen
    if ball.ycor() >280 or ball.ycor() < -280:
        #collision
        ball.bounce_y()

    #detecting collision with the rpaddle and lpaddle 
    if ball.distance(r_paddle)  <50 and ball.xcor() >320 or ball.distance(l_paddle)  <50 and ball.xcor() < -320:
        ball.bounce_x()

    #detecting whether the ball has missed the paddle
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
        

    if  ball.xcor() < -350:
        ball.reset_position()
        scoreboard.r_point()
       

screen.exitonclick()


