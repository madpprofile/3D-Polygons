import sys, math

def pyramid(sides):
    angle = 360.0/sides * (math.pi/180)
    faces, vertexes = [], []
    
    #init
    #vertexes
    vertexes.append((0, 1, 0))
    for i in range(0, sides):
        vertexes.append((1*math.cos(i*angle) - 0*math.sin(i*angle), -1, 1*math.sin(i*angle) + 0*math.cos(i*angle)))
    c_count = len(vertexes)
    
    #faces
    for i in range (1, c_count):
        a, b = i, i+1
        if a >= c_count:
            a -= c_count-1
        if b >= c_count:
            b -= c_count-1
        faces.append((a, b, 0))
    base = []
    for vertex in range(1, c_count):
        base.append(vertex)
    faces.append(tuple(base))
    return vertexes, faces

def to_string(l):
    out = ""
    for vertex in l:
        out += " " + str(vertex)
    return out

def drawOBJ(filepath):
        vertexes, faces =  pyramid(int(sys.argv[1]))
        file = open(filepath, "w")
        file.write("mtllib ./vp.mtl\n")
        file.write("g\n")
        for vertex in vertexes:
            file.write("v " + "%0.6F"%(vertex[0]) + " " + "%0.6F"%(vertex[1])  + " " + "%0.6F"%(vertex[2]) + "\n")
        for face in faces:
            file.write("f" + to_string(face) + "\n")
        file.close()

def main():
    if len(sys.argv) == 3:
        drawOBJ(sys.argv[2])
    else:
        print("Invalid parameter")
    
if __name__ == "__main__":
    main()
