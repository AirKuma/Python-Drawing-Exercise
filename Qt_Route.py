import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt4.QtGui import *
from PyQt4.QtOpenGL import *
from PyQt4.QtCore import *
from random import *

FPS = 60
theta = 0 
delta = 12/FPS

class Window(QGLWidget):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowTitle("square")
        self.resize(360,360)
        
        timer = QTimer(self)
        timer.timeout.connect(self.animate)
        timer.start(1000/FPS)
        #timer.start(0)
        self.setAutoBufferSwap(True)
        
        
    def paintGL(self):
        global theta
        glClearColor(0,0,0,0)    #black
        glClear(GL_COLOR_BUFFER_BIT)
        
        glPushMatrix()  
        glRotatef(theta,0,0,1)
        glScalef(0.5,0.5,1)
        
        glBegin(GL_POLYGON)
        glColor3f(1,0,0)       #正方形
        glVertex3f(-1,-1,0)
        glColor3f(0,1,0)   
        glVertex3f(1,-1,0)
        glColor3f(0,0,1)   
        glVertex3f(1,1,0)
        glColor3f(1,1,0)   
        glVertex3f(-1,1,0)
        glEnd()
              
        #glRectf(-1,-1,1,1)
        glRectf(-1.3,-1.3,-1.1,-1.1)   #多一個小方塊
        glColor3f(1,1,1)           #與其顏色
   
        glTranslatef(1.5,0,0)        #另一個白色小方塊移出
        glRotatef(theta*6,0,0,1)
        glScalef(0.2,0.2,1)
        glRectf(-1,-1,1,1)
        
        glTranslatef(3,0,0)               #跟在上一個後面的小方塊
        glRotatef(theta*6,0,0,1)
        glScalef(0.5,0.5,1)
        glColor3f(0,0,1) 
        glRectf(-1,-1,1,1)     
        
        glPopMatrix()
        
              
        theta += delta
        theta %= 360.0
    
    def resizeGL(self,w,h):
        glViewport(0,0,w,h)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()     #單位矩陣
        #gluOrtho2D(-0.2,1.2,-0.2,1.2)    #平行投影
        
        if w > h:
            gluOrtho2D(-w/h,w/h,-1,1)
        else:    
            gluOrtho2D(-1,1,-h/w,h/w)
        
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        
    def keyPressEvent(self,event):
        if event.key() == Qt.Key_Escape:
            self.close()
            
    def mousePressEvent(self,event):
        if event.button() == Qt.RightButton:
            self.close()        
        '''    
        global r,g,b
        if event.buttons() == Qt.LeftButton   按滑鼠左鍵隨機換顏色
            r = random()
            g = random()
            b = random()
            self.update()  
        '''     

    def animate(self):
        global r,g,b
        r = random()
        g = random()
        b = random()
        self.update()
        
#========================================================
if __name__ == '__main__':
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    window = Window()
    window.show()
    app.exec_()        