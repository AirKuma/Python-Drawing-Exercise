import math
import random

import sys
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

FPS = 120
quadratic = gluNewQuadric()

def circle(x = 0,y = 0,r = 1,n = 36):
    glPushMatrix()
    glTranslatef(x,y,0)
    gluDisk(quadratic,0,r,n,1)    #產生圓   r = 半徑
    glPopMatrix()

def display():
    glClearColor(0,0,0,0) #black
    r = random.random()
    g = random.random()
    b = random.random()
    
    x = random.random()
    y = random.random()
    radius = random.random()/10
       
    glPushMatrix()           
    glColor4f(0,0,0,0.06) 
    glRectf(0,0,1,1)
    
    glColor3f(r,g,b)
    circle(x,y,radius)   
    glPopMatrix()
    glFlush()
  
def reshape(w,h):
    glViewport(0,0,w,h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
     
    gluOrtho2D(0,1,0,1)
    glMatrixMode(GL_MODELVIEW)
     
    glShadeModel(GL_FLAT)
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA,GL_ONE_MINUS_SRC_ALPHA)    
          
def keyboard(key,x,y):
    if ord(key) ==27:
        sys.exit(0)

def mouse(button,state,x,y):
    if button == GLUT_RIGHT_BUTTON:
        sys.exit(0)     
        
def idle():
    glutPostRedisplat()
        
def timer(v):    
    glutPostRedisplay()
    glutTimerFunc(1000//FPS,timer,0)
    
    
   
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGB | GLUT_SINGLE | GLUT_DEPTH)   
glutInitWindowSize(600,600)
glutCreateWindow(b'circles_fade')   #視窗上面顯示的名稱
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse)
#glutIdleFunc(idle)
glutTimerFunc(0,timer,0)
glutMainLoop()    