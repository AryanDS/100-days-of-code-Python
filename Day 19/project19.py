"""
Turtle race bet project!
"""
from turtle import Turtle, Screen, color
import random
#creating object
screen = Screen()

#setting the dimension of the screen, width and height!
screen.setup(width= 500,height= 400)
#Calling the textinput() which will ask the user for the input on the bet!
user_bet = screen.textinput(title="Make your Bet!", prompt="Which turtle do you think will win the race? Enter the color: ")

colors=['red','green','blue','orange','purple','yellow']
is_race_on = False

#Creating a list of turtles, this will hold all the turtle instances!
all_turtles=[]

#using a loop to do the same thing above!
y=60
for turtle_idx in range(6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[turtle_idx])
    tim.goto(x= -230, y=y)
    y-=30
    all_turtles.append(tim)

if user_bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        #Condition which will check whether the turtle has finished the race or not!
        if turtle.xcor()>230:
            is_race_on= False
            winning_turtle = turtle.pencolor()    
            if winning_turtle == user_bet:
                print(f"You've WON!, The winning turtle is {winning_turtle}!")
            else:
                 print(f"You've LOST!, The winning turtle is {winning_turtle}!")
        rand_dist= random.randint(0,10)
        turtle.forward(rand_dist)

screen.exitonclick()