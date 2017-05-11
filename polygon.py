from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import math, sys

//used for platonic solids
phi = (1.0+math.sqrt(5))/2.0

def prism(sides):
    angle = (360.0/sides) * (math.pi/180)
    faces, lines, vertexes = [], [], []
    
    #init
    for i in range(0, sides):
        vertexes.append((1*math.cos(i*angle) - 0*math.sin(i*angle), -1, 1*math.sin(i*angle) + 0*math.cos(i*angle)))
        vertexes.append((1*math.cos(i*angle) - 0*math.sin(i*angle), 1, 1*math.sin(i*angle) + 0*math.cos(i*angle)))
    v_count = len(vertexes)
    #print(v_count)
    
    i = 0
    while i < v_count:
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

    #lateral faces
    glBegin(GL_QUADS)
    glColor3fv((1, 1, 1))
    for face in faces:
        for vertex in face:
            glVertex3fv(vertexes[vertex])
    glEnd()
    
    #top face
    glBegin(GL_POLYGON)
    glColor3fv((1, 1, 1))
    vertex = 0
    for do_not_mind_me in range(sides):
        glVertex3fv(vertexes[vertex])
        vertex+=2
    glEnd()
    
    #bottom face
    glBegin(GL_POLYGON)
    glColor3fv((1, 1, 1))
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
    angle = 360.0/sides * (math.pi/180)
    faces, lines, vertexes = [], [], []
    colors = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    
    #init
    #vertexes
    vertexes.append((0, 1, 0))
    for i in range(0, sides):
        vertexes.append((1*math.cos(i*angle) - 0*math.sin(i*angle), -1, 1*math.sin(i*angle) + 0*math.cos(i*angle)))
    c_count = len(vertexes)
    
    #lines and faces
    for i in range (1, c_count):
        a, b = i, i+1
        if a >= c_count:
            a -= c_count-1
        if b >= c_count:
            b -= c_count-1
        lines.append((a,b))
        lines.append((a,0))
        lines.append((b,0))
        faces.append((a, b, 0))
    #print(lines)
    #print(faces)
    
    #lateral faces
    glBegin(GL_TRIANGLE_FAN)
    glColor3fv((1, 1, 1))
    for vertex in range(0, c_count):
        #glColor3fv(colors[vertex%len(colors)])
        glVertex3fv(vertexes[vertex])
    glVertex3fv(vertexes[1])
    glEnd()
    
    
    #polygon base
    glBegin(GL_POLYGON)
    glColor3fv((1, 1, 1))
    for vertex in range(1, c_count):
        glVertex3fv(vertexes[vertex])
    glEnd()
    
    
    #lines
    glColor3fv((0, 0, 0))
    glBegin(GL_LINES)
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
        glColor3fv(colors[vertex%4])
        glVertex3fv(vertexes[vertex])
    glEnd()
    '''
'''
Reference:
	Octant  number				X	Y	Z	Octal (+=0,zyx)	Octal (+=1,zyx)
	I	    top-front-right	    +	+	+			0				7
	II	    top-back-right	    −	+	+			1				6
	III	    top-back-left	    −   −   +			3				4
	IV	    top-front-left	    +   −	+			2				5
	V	    bottom-front-right	+	+	−			4				3
	VI	    bottom-back-right	−	+	−			5				2
	VII	    bottom-back-left	−	−	−			7				0
	VIII	bottom-front-left	+	−	−			6				1

icosahedron

(0, ±1, ±φ)
(±1, ±φ, 0)
(±φ, 0, ±1) 

(0, ±φ, ±1)
(±φ, ±1, 0)
(±1, 0, ±φ)

Dodecahedron

(±1, ±1, ±1)
(0, ±1/φ, ±φ)
(±1/φ, ±φ, 0)
(±φ, 0, ±1/φ)

(±1, ±1, ±1)
(0, ±φ, ±1/φ)
(±φ, ±1/φ, 0)
(±1/φ, 0, ±φ)
'''

def icosahedron():
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
	

def dodecahedron():
	global phi
    vertexes = [
        ( 0,  1,  phi), ( 1,  phi,  0), ( phi,  0,  1), ( 0,  phi,  1), ( phi,  1,  0), ( 1,  0,  phi)
    ]
    edges = []
    faces = []
    

def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    polygon(sides)
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def key_pressed(k, x, y):
    global sides, polygon
    #print(k)
    
    #if spacebar is pressed
    if k == b' ':
        if polygon == pyramid:
            polygon = prism
        else:
            polygon = pyramid
        return
    
    #if any number from 3 to 9 is pressed
    try:
        key = int(k)
        if key <= 9 and key >= 3:
            sides = key
    except:
        return

def usage():
    print('\nUsage:')
    print('\n  polygon.py [polygon] [sides]')
    
    print('\nOptions:')
    print('  [polygon] - prism or pyramid')
    print('  [sides] - 3 or higher')
    
    print('\nInteractions:')
    print('  Keys 3 to 9 - changes polygon\'s number of sides')
    print('  Spacebar - alternate between prism and pyramid')
    
    print('')
    sys.exit()
    
def validate_parameters():
    #argv size
    if len(sys.argv) != 3:
        print('Invalid parameters')
        usage()

    global polygon
    global sides
    
    #polygon
    if sys.argv[1] == "pyramid":
        polygon = pyramid
    elif sys.argv[1] == "prism":
        polygon = prism
    else:
        print('Invalid parameter [polygon]')
        usage()
    
    #sides
    try:
        sides = int(sys.argv[2])
        if sides < 3:
            print('Invalid parameter [sides]')
            usage()
    except ValueError:
        print('Invalid parameter [sides]')
        usage()

# PROGRAMA PRINCIPAL
validate_parameters()
glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow(b"Interactive polygon")
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


