#Snake Game 
from turtle import Turtle, Screen
import time 
from snake import Snake

screen = Screen()
#Declaring dimensions of the screen
screen.setup(width=600, height=600)

#Declaring the background color of the screen
screen.bgcolor("black")

#declaring title of the screen
screen.title("My Snake Game!")

#from the snake class creating a snake object!
snake=  Snake()


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

screen.exitonclick()