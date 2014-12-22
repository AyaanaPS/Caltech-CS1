'''
This module simulates balls bouncing around a canvas.
'''

import math
import random
from Tkinter import *

class BouncingBall:
    '''Objects of this class represent balls which bounce on a canvas.'''
    def __init__(self, canvas, center, radius, color, direction, speed):
        '''Create a new ball at center of the given radius and color, 
        moving at a given direction and speed.'''

        x, y = center
        x1 = x - radius
        y1 = y - radius
        x2 = x + radius
        y2 = y + radius
        self.handle = canvas.create_oval(x1, y1, x2, y2,
                        fill=color, outline=color)
        self.canvas = canvas
        self.xmax   = int(canvas.cget('width')) - 1
        self.ymax   = int(canvas.cget('height')) - 1
        self.center = center
        self.radius = radius
        self.color  = color

        # The direction is represented as an angle in degrees
        # (range 0-360), which we convert to radians here.
        # The angle is with respect to the positive x axis,
        # going clockwise around the origin.
        if direction < 0.0 or direction > 360.0:
            raise ValueError('Invalid direction; must be in range [0.0, 360.0]')
        dir_radians = direction * math.pi / 180.0

        # Separate the direction into its x and y coordinates.
        # Flip the sign of the y coordinate because the y coordinate
        # grows downward, not upward.
        self.dirx = math.cos(dir_radians)
        self.diry = -math.sin(dir_radians)

        # Speed is represented as a single non-negative float.
        # Note that non-float speeds will behave poorly.
        if speed < 0.0: 
            raise ValueError('Invalid speed; must be positive')
        self.speed = speed

    def step(self):
        '''Move this ball in its current direction with its
        current speed.  Change direction if the edge of the
        canvas is reached.'''

        vx = int(self.speed * self.dirx)
        vy = int(self.speed * self.diry)
        xc, yc = self.center
        dx = self.displacement(xc, vx, self.xmax)
        dy = self.displacement(yc, vy, self.ymax)
        
        canvas.move(self.handle, dx, dy)
        self.center = (xc + dx, yc + dy)
        if vx != dx:
            self.dirx = self.dirx * -1
            
        if vy != dy:
            self.diry = self.diry * -1


    def displacement(self, c, d, cmax):
        '''Compute the actual displacement along the x or y dimension,
        taking reflections off the edge into account.  'c' is the
        center of the ball (x or y coordinate); 'cmax' is the largest 
        value in that direction, and 'd' is the desired displacement
        in that direction.'''
        
        movement = c + d
        displacement = 0
        if movement + self.radius > cmax:
            displacement = cmax - (c + self.radius)
            displacement -= d - displacement
            return displacement
        elif movement - self.radius < 0:
            displacement = (d - c - self.radius) * -1
            return displacement - 2 * self.radius
        else:
            return d
        
        

    def scale_speed(self, scale):
        '''Scale the speed of this object by a factor 'scale'.'''

        self.speed = self.speed + (self.speed * scale)
            
    def delete(self):
        '''Remove this object from the canvas.'''
        self.canvas.delete(self.handle)


def random_ball(canvas, rmin, rmax, smin, smax, xmax, ymax):
    '''
    Create and return a ball with a random color, starting position,
    size, direction, and velocity.
    rmin: minimum radius (pixels)
    rmax: maximum radius (pixels)
    smin: minimum speed
    smax: maximum speed
    xmax: maximum x dimension of canvas
    ymax: maximum y dimension of canvas
    '''

    radius = random.randrange(rmin, rmax + 1)
    speed = random.uniform(smin, smax + 1)
    cx = random.randrange(0 + radius, xmax - radius + 1)
    cy = random.randrange(0 + radius, ymax - radius + 1)
    options = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    options.extend(['a', 'b', 'c', 'd', 'e', 'f'])    
    x = 0
    color = '#'
    while (x < 6):
        color += random.choice(options)
        x += 1    
    direction = random.randrange(0.0, 360.0 + 1)
    return BouncingBall(canvas, (cx, cy), radius, color, direction, speed)

def key_handler(event):
    '''Handle key presses.'''
    global bouncing_balls
    global done
    key = event.keysym
    if key == 'q': 
        done = True
    elif key == 'plus':  # add a ball at a random location
        ball = random_ball(canvas, 10, 60, 5.0, 15.0, 800, 600)
        bouncing_balls.append(ball)
    elif key == 'minus':  # remove a ball from the canvas if there are any
        x = bouncing_balls.pop()
        x.delete()
    elif key == 'u':  # speed (u)p all bouncing_balls by factor of 1.2
        for balls in bouncing_balls:
            balls.scale_speed(1.2)
    elif key == 'd':  # slow (d)own all bouncing_balls by factor of 1.2
        for balls in bouncing_balls:
            balls.scale_speed(-1.2)
    elif key == 'x':  # delete all bouncing_balls
        for balls in bouncing_balls:
            balls.delete()
            bouncing_balls = []

if __name__ == '__main__':
    root = Tk()
    root.geometry('800x600')
    canvas = Canvas(root, width=800, height=600)
    canvas.pack()
    done = False

    # Bind events to handlers.
    root.bind('<Key>', key_handler)
    
    # Set up some bouncing balls.
    bouncing_balls = []
    for i in range(5):
        bouncing_balls.append(random_ball(canvas, 10, 60, 5.0, 15.0, 800, 600))

    # Start the event loop.
    while not done:
        for ball in bouncing_balls:
            ball.step()
        root.update()

