from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math, sys

vertices = (
    ( 1, 0, -1),
    ( -1, 0, -1),
    (-1, 0, 1),
    (1, 0, 1),
    (0, 1, 0),
    )

linhas = (
    (0, 1),
    (1, 2),
    (2, 3),
    (3, 0),
    (0, 4),
    (1, 4),
    (2, 4),
    (3, 4),
    )

faces = (
    (0,1,4),
    (1,2,4),
    (2,3,4),
    (3,0,4),
    (0,1,2),
    (2,3,0),
    )

cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

def Cubo():
    glBegin(GL_TRIANGLE_STRIP)
    i = 0
    for face in faces:
#        glColor3fv(cores[i])
        for vertex in face:
            glColor3fv(cores[vertex])
            glVertex3fv(vertices[vertex])
        i = i+1
    glEnd()

    glColor3fv((0,0.5,0))
    glBegin(GL_LINES)
    for linha in linhas:
        for vertice in linha:
            glVertex3fv(vertices[vertice])
    glEnd()
    
def prism(sides):
    angle = (360.0/sides) * (math.pi/180)
    faces, lines, vertexes = [], [], []
    
    #init
    i = 0
    for i in range(0, sides):
        vertexes.append((1*math.cos(i*angle) - 0*math.sin(i*angle), -1, 1*math.sin(i*angle) + 0*math.cos(i*angle)))
        vertexes.append((1*math.cos(i*angle) - 0*math.sin(i*angle), 1, 1*math.sin(i*angle) + 0*math.cos(i*angle)))
        #i+=1
    v_count = len(vertexes)
    #print(v_count)
    
    i = 0
    for do_not_mind_me in range(0, v_count/2):
        a, b, c, d = i, i+1, i+2, i+3
        if a >= v_count:
            a -= v_count
        if b >= v_count:
            b -= v_count
        if c >= v_count:
            c -= v_count
        if d >= v_count:
            d -= v_count
        lines.append((a,b))
        lines.append((a,c))
        lines.append((b,d))
        lines.append((c,d))
        faces.append((a, b, d, c))
        i+=2
    
#    print('vertexes')
#    print(vertexes)
#    print('lines')
#    print(lines)
#    print('faces')
#    print(faces)
    
    #lateral_faces
    glBegin(GL_QUADS)
    glColor3fv((1, 1, 1))
    for face in faces:
        for vertex in face:
            glVertex3fv(vertexes[vertex])
    glEnd()
    
    #top face
    glBegin(GL_POLYGON)
    glColor3fv((1, 0, 0))
    vertex = 0
    for do_not_mind_me in range(sides):
        glVertex3fv(vertexes[vertex])
        vertex+=2
    glEnd()
    
    #bottom face
    glBegin(GL_POLYGON)
    glColor3fv((0, 0, 1))
    vertex = 1
    for do_not_mind_me in range(sides):
        glVertex3fv(vertexes[vertex])
        vertex+=2
    glEnd()
    
    #lines
    glBegin(GL_LINES)
    glColor3fv((0, 0, 0))
    for line in lines:
        for vertex in line:
            glVertex3fv(vertexes[vertex])
    glEnd()
        
    
    '''
    #Draw vertexes
    colors =[(i, 0, 0), (0, i, 0), (0, 0, i), (i, i, i)]
    glBegin(GL_POINTS)
    i = 0
    for vertex in range(0,len(vertexes)):
        if i == 4:
            i = 0
        glColor3fv(colors[i])
        glVertex3fv(vertexes[vertex])
        i+=1
    glEnd()
    '''

def pyramid(sides):
    angle = 360.0/sides
    faces, lines, vertexes = [], [], []
    
    #init
    i = 0
    for i in range(0, sides):
        vertexes.append((math.cos(i*angle) - math.sin(i*angle), -1, math.sin(i*angle) + math.cos(i*angle)))
        i+=1
    #vertexes.append((0, 1, 0))
    c_count = len(vertexes)
    
    i = 0
    for i in range (0, c_count-1):
        a, b = i, i+1
        if a >= c_count:
            a -= c_count
        if b >= c_count:
            b -= c_count
        lines.append((a,b))
        lines.append((a,c_count-1))
        lines.append((b,c_count-1))
        faces.append((a, b, c_count-1))
        i+=1
    lines.append((i,0))
    lines.append((i,c_count-1))
    lines.append((0,c_count-1))
    faces.append((i, 0, c_count-1))
    
    glBegin(GL_TRIANGLE_FAN)
    glColor3fv((1, 1, 1))
    glVertex3fv((0, 1, 0))
    for vertex in range(0, c_count):
        glVertex3fv(vertexes[vertex])
    glEnd()        
    
    '''
    #Draw vertexes
    colors =[(i, 0, 0), (0, i, 0), (0, 0, i), (i, i, i)]
    glBegin(GL_POINTS)
    i = 0
    for vertex in range(0,len(vertexes)):
        if i == 3:
            i = 0
        glColor3fv(colors[i])
        glVertex3fv(vertexes[vertex])
        i+=1
    glEnd()
    '''
    

def display():
    global polygon
    global sides
    sides = 3
    if len(sys.argv) == 3:
        sides = int(sys.argv[2])
    if sys.argv[1] == "pyramid":
        polygon = pyramid
    elif sys.argv[1] == "prism":
        polygon = prism
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    #Cubo()
    polygon(sides)
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

# PROGRAMA PRINCIPAL
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)

if sys.argv[1] == "pyramid":
    glutCreateWindow(b"Pyramid")
else:
    glutCreateWindow(b"Prism")
glutDisplayFunc(display)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-10)
glRotatef(0,0,0,0)
glutTimerFunc(50,timer,1)
glutMainLoop()


