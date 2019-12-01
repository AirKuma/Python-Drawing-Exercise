# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:55:33 2015

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
    glPushMatrix()
    glColor3f(r,g,b)  #default(1,1,1)white
    glScalef(0.8,0.8,1)  
    glRectf(-1,-1,1,1)
    glPopMatrix()
    glFlush()
    
def reshape(w,h):
     glViewport(0,0,w,h)
     glMatrixMode(GL_PROJECTION)
     glLoadIdentity()
     
     if w <= 0:  w = 1
     if h <= 0:  h = 1
     if w > h:
         gluOrtho2D(-w/h,w/h,-1,1)
     else:    
         gluOrtho2D(-1,1,-h/w,h/w)
        
     glMatrixMode(GL_MODELVIEW)
     glLoadIdentity()
          
def keyboard(key,x,y):
    if ord(key) ==27:
        sys.exit(0)

def mouse(button,state,x,y):
    if button == GLUT_RIGHT_BUTTON:
        sys.exit(0)     
        
#def idle():
    #return
        
def timer(v):    
    global r,g,b
    FPS = 2
    r = random()
    g = random()
    b = random()
    glutPostRedisplay()
    glutTimerFunc(1000//FPS,timer,0)
    
    
   
glutInit(sys.argv)
glutCreateWindow(b'square')
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse)
#glutIdleFunc(idle)
glutTimerFunc(0,timer,0)
glutMainLoop()    