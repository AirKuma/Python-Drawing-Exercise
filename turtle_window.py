# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:47:28 2015

@author: user
"""

from turtle import *

turtle_modes = ("standard","logo","world")
mode("standard")

#title("square")

#setup(640,480)

setworldcoordinates(-2,-2,2,2)


#"fastest":0
#"fast":10
#"normal":6
#"slow":3
#"slowest":1

speed("slowest")

color("green")
#bgcolor("yellow")

pensize(3)
#turtlesize(2)

turtle_shapes = ("arrow","turtle","circle","square","triangle","classic")
shape("turtle")

colors = ("Salmon","Purple","DeepPink","GreenYellow","RoyalBlue","Goldenrod","Lime")
home()
left(45)
n = len(colors)
for i in range(n):
    color(colors[i])
    for _ in range(4):
        forward(1)
        left(90)
    left(360/n)

#for _ in range(4):
#    forward(1)
#    left(90)

#forward(1)
#left(90)
#
#forward(1)
#left(90)
#
#forward(1)
#left(90)
#
#forward(1)
#left(90)

print("Done!")
mainloop()