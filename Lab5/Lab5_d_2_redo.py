from Tkinter import *
import random
import math

# Graphics Commands

def random_color():
	'''Returns a random color in the hexadecimal format.'''
	options = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	options.extend(['a', 'b', 'c', 'd', 'e', 'f'])
	x = 0
	color = '#'
	while (x < 6):
		color += random.choice(options)
		x += 1
	return color

def draw_line(canvas, pt1, pt2):
	'''This function draws a line from pt1 to pt2 on a given canvas.'''
	x1, y1 = pt1
	x2, y2 = pt2
	line = canvas.create_line(x1, y1, x2, y2, fill = color)
	return line

def draw_star(canvas, xc, yc):
	'''This function draws a star using the draw_line function. The star
	is drawn on the given campus about the inputted center points.'''
	radius = random.randrange(50,101)
	theta = 2*math.pi/N
	points = []
	star = []
	for i in range(N):
		x = radius*math.cos(theta*i)
		y = radius*math.sin(theta*i)
		point = (xc + y, yc - x)
		points.append(point)
	for i, pt in enumerate(points):
		nextI = (i + (N-1)/2)%N
		line = draw_line(canvas, pt, points[nextI])
		star.append(line)
	return star

# Event Handlers

def key_handler(event):
	'''This function handles key presses.'''
	global stars
	global color
	global N
	key = event.keysym
	if key == 'q':
		quit()
	elif key == 'c':
		color = random_color()
	elif key == 'plus':
		N = N + 2
	elif key == 'minus':
		if ((N-2) < 5):
			N = 5
		else:
			N = N - 2
	elif key == 'x':
		for star in stars:
			for line in star:
				canvas.delete(line)
		stars = []

def button_handler(event):
	'''This function handles button presses.'''
	star = draw_star(canvas, event.x, event.y)
	stars.append(star)


if __name__ == '__main__':
	root = Tk()
	root.geometry('800x800')
	canvas = Canvas(root, width = 800, height = 800)
	canvas.pack()
	stars = []
	color = random_color()
	N = 5
	# Bind events to handlers.
	root.bind('<Key>', key_handler)
	canvas.bind('<Button-1>', button_handler)
	# Start it up.
	root.mainloop()


