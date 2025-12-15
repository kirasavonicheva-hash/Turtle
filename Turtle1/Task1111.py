from turtle import *
from math import sin, cos, pi
tracer(20)
bgcolor("#0a0a1a")
hideturtle()
speed(0)
for angle in range(0, 3600, 5):
    rad = angle * pi / 180
    for r in range(50, 250, 20):
        x = r * cos(rad)
        y = r * sin(rad)
        red = abs(sin(rad * 3))
        green = abs(cos(rad * 2))
        blue = abs(sin(rad * 5))
        up()
        goto(x, y)
        down()
        fillcolor(red, green, blue)
        begin_fill()
        circle(2 + r * 0.02)
        end_fill()
done()