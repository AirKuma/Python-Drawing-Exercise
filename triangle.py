# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 14:28:24 2015

@author: user
"""
from turtle import *

def curve(order,r):
    if order > 0:
        for _ in range(3):
            curve(order-1,r/2)
            forward(r)
            left(120)
            
