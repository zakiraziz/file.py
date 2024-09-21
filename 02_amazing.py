from turtle import *
from colorsys import *
bgcolor('black')
tracer(30)
setpos (0, -230)
width(20)
h = 0

for i in range (200):
    c = hsv_to_rgb(h,1,1)
    h += 0.1
    fillcolor(c)
    begin_fill()
    circle(i, 120)
    circle(90,90)
    circle(i, 120)
    end_fill()
