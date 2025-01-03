# import colorgram
#
# colors = colorgram.extract('image.jpg', 30)
#
# list_of_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     list_of_colors.append((r,g,b))

import turtle as t
import random as rd

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")

list_of_colors = [(1, 9, 30), (121, 95, 41), (72, 32, 21), (238, 212, 72), (220, 81, 59), (226, 117, 100), (93, 1, 21), (178, 140, 170), (151, 92, 115), (35, 90, 26), (6, 154, 73), (205, 63, 91), (168, 129, 78), (3, 78, 28), (1, 64, 147), (221, 179, 218), (4, 220, 218), (80, 135, 179), (130, 157, 177), (81, 110, 135), (120, 187, 164), (11, 213, 220), (118, 18, 36), (243, 205, 7), (132, 223, 209), (229, 173, 165)]

tim.hideturtle()
tim.setheading(220)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.penup()

num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, rd.choice(list_of_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = t.Screen()
screen.exitonclick()