from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("arrow")
timmy.color("red")

# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# for i in range(500):
#     timmy.pencolor("gold1")
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
# #     timmy.pendown()

# def draw(num_sides):
#     angle = 360/num_sides
#     for i in range(num_sides):
#         timmy.forward(120)
#         timmy.right(angle) 


# for i in range(3,11):
#     draw(i)

#random walk

# direction=[0,90,180,270]
# timmy.pensize(10)
# for i in range(200):
#     timmy.forward(10)
#     timmy.setheading(random.choice(direction))


#sipral circle
for i in range(200):
    timmy.circle(20)
    timmy.forward(2)
    timmy.circle(20)
screen = Screen()
screen.exitonclick()