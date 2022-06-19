import colorgram
import turtle as t
from t import Turtle, Screen
import random


#using the image to extract the colors
colors = colorgram.extract('/Users/aryansaini/Documents/Visual Studio Code/100 days of code/Day 18/image.jpg', 15)
#print(colors[0])
#first_color = colors[0]
#rgb = first_color.rgb # e.g. (255, 151, 210)
rgb_color=[]
for i in range(15):
    r= colors[i].rgb.r
    g= colors[i].rgb.g
    b= colors[i].rgb.b
    new_color = (r,g,b)
    rgb_color.append(new_color)

print(rgb_color)

#Now we are going to draw our hirst painting 
#changing the color mode of the turtle 
t.colormode(255)


tim = Turtle()
for i in range(20):
    tim.dot(20,random.choice(rgb_color))


screen = Screen()
screen.exitonclick()