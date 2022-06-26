#Snake Game 
from turtle import Turtle , Screen
import time 
from snake import Snake
from food import Food
from scoreboard import Score

screen = Screen()
#Declaring dimensions of the screen
screen.setup(width=600, height=600)

#Declaring the background color of the screen
screen.bgcolor("black")

#declaring title of the screen
screen.title("My Snake Game!")

#from the snake class creating a snake object!
snake=  Snake()
food = Food()
scoreboard = Score()

#calling screen event listener methods!
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    
    snake.move()

    #detecting the collision between the snake and the food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()

    #detecting whether the snake hits the wall or not 
    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or  snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    #detecting tail collision within the snake
    for seg in snake.segment[1:]:
        if  snake.head.distance(seg) <10:
            scoreboard.reset()
            snake.reset()
            
screen.exitonclick()