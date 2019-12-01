import sys

from OpenGL.GL import *
from OpenGL.GLU import *
from PyQt4.QtGui import *
from PyQt4.QtOpenGL import *
from PyQt4.QtCore import *
from random import *

FPS = 1
r = g = b = 1

class Window(QGLWidget):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowTitle("square")
        self.resize(360,360)
        
        timer = QTimer(self)
        timer.timeout.connect(self.animate)
        timer.start(1000/FPS)
        #timer.start(0)
        
        glPushMatrix()  
        glScalef(0.8,0.8,1)
        glColor3f(r,g,b)
        
        
    def paintGL(self):
        glClearColor(0,0,0,0)    #black
        glClear(GL_COLOR_BUFFER_BIT)
        
        glPushMatrix()  
        glScalef(0.8,0.8,1)
        glColor3f(r,g,b)    
        glRectf(-1,-1,1,1)
        glPopMatrix()
    
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