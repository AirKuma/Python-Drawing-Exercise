from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

FPS = 60
theta = 0

def display():
    global theta
    glClearColor(0,0,0,0) #black
    glClear(GL_COLOR_BUFFER_BIT)
    
    delta = 12/FPS
    glPushMatrix()
    glRotatef(theta,0,0,1)
    glScalef(0.5,0.5,1)
    glColor3f(1,1,1)  #default(1,1,1)white
    glRectf(-1,-1,1,1)
    glPopMatrix()
    
    glFlush()
    glutSwapBuffers()
    
    theta += delta
    theta %= 360.0
    
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
    glutPostRedisplay()
    glutTimerFunc(1000//FPS,timer,0)
    
    
   
glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE)
glutInitWindowSize(360,360)
glutCreateWindow(b'square')
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutKeyboardFunc(keyboard)
glutMouseFunc(mouse)
#glutIdleFunc(idle)
glutTimerFunc(0,timer,0)
glutMainLoop()    