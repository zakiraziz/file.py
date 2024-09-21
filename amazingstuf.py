from turtle import *
import colorsys
tracer(10)
bgcolor('black')
h=0.1
for i in range(500):
    c=colorsys.hls_to_rgb(h,1,1)
    fillcolor(c)
    h+=0.005
    begin_fill()
    circle(170,170)
    lt(91)
    lt(10)
    circle(20,20)
    end_fill()
done()