
from Tkinter import *
import random

# Graphics Commands

def random_color():
	'''Returns a random color in hexadecimal format.'''
	options = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	options.extend(['a', 'b', 'c', 'd', 'e', 'f'])
	x = 0
	color = '#'
	while (x < 6):
		color += random.choice(options)
		x += 1
	return color

def draw_circle(canvas, x, y):
	'''This function draws a circle on a given canvas about the inputted
	center.'''
	diameter = random.randrange(10, 51)
	circle = canvas.create_oval((x-diameter/2), (y-diameter/2), \
		(x+diameter/2), (y+diameter/2), fill = color, outline = color)
	return circle

# Event Handlers.

def key_handler(event):
	'''This function handles key presses.'''
	global circles
	global color
	key = event.keysym
	if key == 'q':
		quit()
	elif key == 'c':
		color = random_color()
	elif key == 'x':
		for circle in circles:
			canvas.delete(circle)
		circles = []

def button_handler(event):
	'''This function handles button presses.'''
	global circles
	circle = draw_circle(canvas, event.x, event.y)
	circles.append(circle)

if __name__ == '__main__':
	root = Tk()
	root.geometry('800x800')
	canvas = Canvas(root, width = 800, height = 800)
	canvas.pack()
	circles = []
	color = random_color()
	# Bind events to handlers.
	root.bind('<Key>', key_handler)
	canvas.bind('<Button-1>', button_handler)
	# Start it up.
	root.mainloop()