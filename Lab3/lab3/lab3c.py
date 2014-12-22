'''
lab3b.py
Simple L-system simulator.
'''

# References: 
#   http://en.wikipedia.org/wiki/L-systems
#   http://www.kevs3d.co.uk/dev/lsystems/
# N.B. http://en.wikipedia.org/wiki/MU_puzzle for midterm?

import math

# ---------------------------------------------------------------------- 
# Example L-systems.
# ---------------------------------------------------------------------- 

#plant
plant = { 'start' : 'X',
          'X' : 'F-[[X]+X]+F[+FX]-X',
          'F' : 'FF' }
plant_draw = { 'F' : 'F 1',
               '-' : 'L 25',
               '+' : 'R 25' }

# Koch snowflake.
koch = { 'start' : 'F++F++F', 
         'F'     : 'F-F++F-F' }
koch_draw = { 'F' : 'F 1', 
              '+' : 'R 60', 
              '-' : 'L 60' }

# Hilbert curve.
hilbert  = { 'start' : 'A', 
             'A'     : '-BF+AFA+FB-' , 
             'B'     : '+AF-BFB-FA+' }
hilbert_draw = { 'F' : 'F 1', 
                 '-' : 'L 90', 
                 '+' : 'R 90' }

# Sierpinski triangle.
sierpinski = { 'start' : 'F-G-G', 
               'F'     : 'F-G+F+G-F', 
               'G'     : 'GG' }
sierpinski_draw = { 'F' : 'F 1', 
                    'G' : 'F 1', 
                    '+' : 'L 120', 
                    '-' : 'R 120' }

# ---------------------------------------------------------------------- 
# L-systems functions.
# ---------------------------------------------------------------------- 
def update(dictionary, lsys):
    '''Updates an L-system string as per the rules of an inputted dictionary.
    '''
    for key in dictionary:
        if key in lsys:
            lsys = lsys.replace(key, dictionary[key])
    return lsys

def iterate(lsys, n):
    '''Returns the string which results from starting with the starting 
    string for that L-system and updating n times.'''
    Lstring = lsys['start']
    for i in range(n):
        Lstring = update(lsys, Lstring)
    return Lstring

def lsystemToDrawingCommands(draw, s):
    '''Returns the list of drawing commands needed to draw the figure
    corresponding to the L-system string.'''
    lst = []
    for i in s:
        if i in draw:
            lst.append(draw[i])
        else:
            if i == '[':
                lst.append('[')
            elif i == ']':
                lst.append(']')

    return lst

import math
def nextLocation(x, y, angle, cmd):
    '''Generates the next location and direction of the turtle after the 
    drawing command has executed. It returns a tuple of three values, the 
    next x coordinate, the next y coordinate and the next angle.'''
    angle_rad = angle * (math.pi/180)
    locLst = []
    cmdlst = cmd.split(' ')
    if cmdlst[0] == 'R':
        angle = (angle - int(cmdlst[1])) % 360
    elif cmdlst[0] == 'L':
        angle = (angle + int(cmdlst[1])) % 360
    elif cmdlst[0] == 'F':
        x += float(cmdlst[1]) * math.cos(angle_rad)
        y += float(cmdlst[1]) * math.sin(angle_rad)
    elif cmdlst[0] == '[':
        locLst.append((x,y))
    elif cmdlst[0] == ']':
        (x, y) = locLst.pop()
        print 'G %f %f %d' %(x, y, angle)
    return (x, y, angle)


def bounds(cmds):
    '''Returns a tuple of the (xmin, xmax, ymin, ymax) coordinates, where 
    each coordinate is a float.'''
    xmin, xmax, ymin, ymax, x, y, angle = (0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0)
    for i in cmds:
        x, y, angle = nextLocation(x, y, angle, i)
        if x < xmin:
            xmin = x
        elif x > xmax:
            xmax = x
        if y < ymin:
            ymin = y
        elif y > ymax:
            ymax = y
    tup = (xmin, xmax, ymin, ymax)
    return tup


def saveDrawing(filename, bounds, cmds):
    '''This function writes the information to the file corresponding the 
    given filename, by writing the bounds information on a single line.'''
    file = open(filename, 'w')
    for i in bounds:
      file.write(str(i) + ' ')
    file.write('\n')
    for x in cmds:
      file.write(x + '\n')
    file.close()

def makeDrawings(name, lsys, ldraw, imin, imax):
    '''Make a series of L-system drawings.'''
    print 'Making drawings for %s...' % name
    for i in range(imin, imax):
        l = iterate(lsys, i)
        cmds = lsystemToDrawingCommands(ldraw, l)
        b = bounds(cmds)
        saveDrawing('%s_%d' % (name, i), b, cmds)

def main():
    makeDrawings('koch', koch, koch_draw, 0, 6)
    makeDrawings('hilbert', hilbert, hilbert_draw, 1, 6)
    makeDrawings('sierpinski', sierpinski, sierpinski_draw, 0, 10)

