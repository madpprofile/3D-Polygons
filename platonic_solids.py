from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math, sys

#Global variables
phi = (1.0+math.sqrt(5))/2.0 #Divine proportion
isWireframe = False
polygon = None

#Fire
def tetrahedron():
    global isWireframe
    color = (1, 0, 0)
    vertexes = [(1, 1, 1), (1, -1, -1), (-1, 1, -1), (-1, -1, 1)]
    edges = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]
    faces = [(0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3)]
    
    glColor3fv(color)
    if isWireframe == False:
        glBegin(GL_TRIANGLES)
        for face in faces:
            for vertex in face:
                glVertex3fv(vertexes[vertex])
        glEnd()
        #change line colors if it's not wireframe mode
        glColor3fv((0, 0, 0))

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertexes[vertex])
    glEnd()

#Earth
def cube():
    global isWireframe
    color = (112.0/255, 56.0/255, 0)
    vertexes = [
        ( 1,-1,-1), ( 1, 1,-1), (-1, 1,-1), (-1,-1,-1),
        ( 1,-1, 1), ( 1, 1, 1), (-1,-1, 1), (-1, 1, 1)
    ]
    edges = [
        (0,1), (0,3), (0,4), (2,1), (2,3), (2,7),
        (6,3), (6,4), (6,7), (5,1), (5,4), (5,7),
    ]
    faces = [
        (0,1,2,3), (3,2,7,6), (6,7,5,4),
        (4,5,1,0), (1,5,7,2), (4,0,3,6)
    ]
    
    glColor3fv(color)
    if isWireframe == False:
        glBegin(GL_QUADS)
        for face in faces:
            for vertex in face:
                glVertex3fv(vertexes[vertex])
        glEnd()
        #change line colors if it's not wireframe mode
        glColor3fv((0, 0, 0))

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertexes[vertex])
    glEnd()

#Air
def octahedron():
    global isWireframe
    color = (152.0/255, 251.0/255, 152.0/255)
    vertexes = [
        (1, 0, 0), (0, 1, 0), (0, 0, 1),
        (-1, 0, 0), (0, -1, 0), (0, 0, -1)        
    ]
    edges = [
        (0, 1), (0, 2), (0, 4), (0, 5),
        (1, 2), (2, 4), (4, 5), (1, 5),
        (1, 3), (2, 3), (3, 4), (3, 5)
    ]
    faces = [
        (0, 1, 2), (0, 2, 4), (0, 4, 5), (0, 1, 5),
        (1, 2, 3), (2, 3, 4), (3, 4, 5), (1, 3, 5)
    ]
    
    glColor3fv(color)
    if isWireframe == False:
        glBegin(GL_TRIANGLES)
        for face in faces:
            for vertex in face:
                glVertex3fv(vertexes[vertex])
        glEnd()
        #change line colors if it's not wireframe mode
        glColor3fv((0, 0, 0))

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertexes[vertex])
    glEnd()

#Aether (dark matter?)
def dodecahedron():
    global isWireframe
    global phi
    vertexes = [
        (1, 1, 1), (0, 1/phi, phi), (1/phi, phi, 0), (phi, 0, 1/phi),
        (1, 1, 1), (0, phi, 1/phi), (phi, 1/phi, 0), (1/phi, 0, phi),

        (1, 1, 1), (0, 1/phi, phi), (1/phi, phi, 0), (phi, 0, 1/phi),
        (1, 1, 1), (0, phi, 1/phi), (phi, 1/phi, 0), (1/phi, 0, phi),

        (1, 1, 1), (0, 1/phi, phi), (1/phi, phi, 0), (phi, 0, 1/phi),
        (1, 1, 1), (0, phi, 1/phi), (phi, 1/phi, 0), (1/phi, 0, phi),        
    ]
    edges = []
    faces = []
    
    glBegin(GL_TRIANGLES)
    glColor3fv((255, 215.0/255, 0))
    for face in faces:
        for vertex in face:
            glVertex3fv(vertexes[vertex])
    glEnd()
    #change line colors if it's not wireframe mode
    glColor3fv((0, 0, 0))
    
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertexes[vertex])
    glEnd()

#Water
def icosahedron():
    global isWireframe
    global phi
    color = (0, 159.0/255, 255)
    vertexes = [
        (phi, 1, 0), (phi, -1, 0), (1, 0, phi), (1, 0, -phi),
        (0, phi, 1), (0, phi, -1), (0, -phi, 1), (0, -phi, -1),
        (-1, 0, phi), (-1, 0, -phi), (-phi, 1, 0), (-phi, -1, 0)
    ]
    edges = [
        (0, 1), (0, 2), (0, 3), (0, 4), (0, 5),
        (1, 2), (1, 3), (1, 6), (1, 7),
        (2, 4), (2, 6), (2, 8),
        (3, 5), (3, 7), (3, 9),
        (4, 5), (4, 8), (4, 10),
        (5, 9), (5, 10),
        (6, 7), (6, 8), (6, 11),
        (7, 9), (7, 11),
        (8, 10), (8, 11),
        (9, 10), (9, 11),
        (10, 11)
    ]
    faces = [
        (0, 1, 2), (0, 1, 3),
        (0, 2, 4), (0, 4, 5), (0, 3, 5),
        (1, 2, 6), (1, 6, 7), (1, 3, 7),
        (2, 4, 8), (2, 6, 8),
        (3, 5, 9), (3, 7, 9),
        (4, 8, 10), (4, 5, 10), (5, 9, 10),
        (6, 8, 11), (6, 7, 11), (7, 9, 11),
        (8, 10, 11), (9, 10, 11)
    ]
    
    glColor3fv(color)
    if isWireframe == False:
        glBegin(GL_TRIANGLES)
        for face in faces:
            for vertex in face:
                glVertex3fv(vertexes[vertex])
        glEnd()
        #change line colors if it's not wireframe mode
        glColor3fv((0, 0, 0))
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertexes[vertex])
    glEnd()    

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    polygon()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def key_pressed(k, x, y):
    global polygon, isWireframe
    #print(k)
    
    #if spacebar is pressed
    if k == b' ':
        if isWireframe == False:
            isWireframe = True
        else:
            isWireframe = False
        return
    elif k == b'1':
        polygon = tetrahedron
    elif k == b'2':
        polygon = cube
    elif k == b'3':
        polygon = octahedron
    elif k == b'4':
        polygon = icosahedron
    elif k == b'5':
        polygon = dodecahedron

#MAIN PROGRAM
polygon = tetrahedron
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow(b"Platonic solids")
glutDisplayFunc(display)
glutKeyboardFunc(key_pressed)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(0,0,0,0)
glutTimerFunc(50,timer,1)
glutMainLoop()


