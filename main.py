import colorgram
import turtle
from turtle import Turtle, Screen
import random

rgb=[]
colors=colorgram.extract('test.jpg',15)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new=(r,g,b)
    rgb.append(new)

colorlist = [(253, 251, 247), (254, 249, 252), (234, 251, 243), (197, 13, 32), (249, 237, 21), (39, 77, 188),
(238, 227, 5), (39, 216, 68), (228, 160, 47), (243, 247, 253), (28, 40, 155), (214, 75, 14), (16, 153, 17),
(199, 15, 11), (242, 34, 164)]
turtle.colormode(255)
tim = Turtle()
tim.speed("fastest")

tim.shape("arrow")
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
number_dots=101

for i in range(1,number_dots):
    tim.pendown()
    tim.dot(20,random.choice(colorlist))
    tim.penup()
    tim.forward(50)
    if i % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = Screen()
screen.exitonclick()


