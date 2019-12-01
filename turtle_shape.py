# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 13:26:30 2015

@author: user
"""

from turtle import *

color("green")
bgcolor("yellow")

pensize(5)
turtlesize(2)

turtle_shapes = ("arrow","turtle","circle","square","triangle","classic")
shape("turtle")

for _ in range(4):
   forward(100)
   left(90)

print("Done!")
mainloop()