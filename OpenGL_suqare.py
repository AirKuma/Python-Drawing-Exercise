# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 15:04:58 2015

@author: user
"""

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from random import *

r = g = b = 1

def display():
    glClearColor(0,0,0,0) #black
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(r,g,b)  #default(1,1,1)white
    glRectf(0,0,1,1)
    glFlush()
    
def reshape(w,h):
     glViewport(0,0,w,h)
     glMatrixMode(GL_PROJECTION)
     gluOrtho2D(-1.2,1.2,-1.2,1.2)
     glMatrixMode(GL_MODELVIEW)
     
def keyboard(key,x,y):
    if ord(key) ==27:
        sys.exit(0)

def mouse(button,state,x,y):
    if button == GLUT_RIGHT_BUTTON:
        sys.exit(0)     
        
    global r,g,b
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        r = random()
        g = random()
        b = random()
        display()
   
glutInit(sys.argv)
glutCreateWindow(b'square')
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse)
glutMainLoop()    