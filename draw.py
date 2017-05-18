from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math, sys, random

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    draw()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def f(x, y):
    return x**2 - y**2

def abstract_draw():
    vertices = []
    glBegin(GL_TRIANGLE_STRIP)
    glColor3fv((0.2, 0.2, 0.2))
    x = 0
    while x < 1:
        y = 0        
        while y < 1:
            vertices.append((x, y, f(x,y)))
            if len(vertices) > 2:
                glVertex3fv(vertices[-1])
            elif len(vertices) == 2:
                glVertex3fv(vertices[0])
                glVertex3fv(vertices[1])
            y += 0.1
        x += 0.1
    glVertex3fv(vertices[-1])
    glVertex3fv(vertices[0])    
    glEnd()
    
def draw():
    vertices = []
    dx = 0.1
    dy = 0.1
    x = -1
    while x < 1:
        y = -1
        glColor3fv((1, 1, 1))
        glBegin(GL_TRIANGLE_STRIP)
        while y < 1:
            vertices.append((x, y, f(x,y)))
            vertices.append((x+dx, y, f(x+dx,y)))
            glVertex3fv(vertices[-2])
            glVertex3fv(vertices[-1])
            y += dy
        x += dx
        glEnd()
        

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow(b"f(x,y)")
glutDisplayFunc(display)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(0,0,0,0)
glutTimerFunc(50,timer,1)
#glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
glutMainLoop()
