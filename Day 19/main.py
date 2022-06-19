"""
Using Turtle module we would be exploring the high order functions and event listeners"""

# from turtle import Turtle, Screen

# #creating objects
# tim = Turtle()
# screen = Screen()

# def move_forward():
#     tim.forward(10)


# #In order to start listening to screen events we need to get hold of the screen object and tell it to listen
# screen.listen()

# #below is an example of higher order functions
# screen.onkey(key ="space", fun=move_forward)

# screen.exitonclick()

#checking 
""""
Etch a Sketch program
"""


from turtle import Turtle, Screen


tim = Turtle()
screen= Screen()


def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def move_counter_clockwise():
    tim.left(angle=10)

def move_clockwise():
    tim.right(angle = 10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


    
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=move_counter_clockwise)
screen.onkey(key="d", fun=move_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()