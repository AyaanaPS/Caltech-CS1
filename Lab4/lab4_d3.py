from Tkinter import *
import random

def draw_square(canvas, color, length, center):
	'''Constructs a square of the given length and color, so that
	its center is at the given position on the canvas passed to it.'''	
	xc, yc = center
	rect = c.create_rectangle((xc-length/2), (yc-length/2), \
		(xc+length/2), (yc+length/2), \
		fill = color, outline = color)

def random_color():
	'''This function returns a random color in the hexadecimal form.'''
	options = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
	options.extend(['a', 'b', 'c', 'd', 'e', 'f']) 
	x = 0
	color = '#'
	while (x < 6):
		color += random.choice(options)
		x += 1
	return color

def random_size(int1, int2):
	''' This function returns random integer that is >= int1 and <= int2.
	Input: First non-negative even int must be smaller than the second.'''
	assert int2 > int1 >= 0	
	assert int2 > int1 >= 0
	assert ((int2 % 2) == 0) and ((int1 % 2) == 0)
	number = random.randint(int1, int2)
	while (number % 2 != 0):
		number = random.randint(int1, int2)
	return number

def random_position(max_x, max_y):
	'''This function returns a random (x, y) pair with x and y between 0
	and the inputted max value.
	Input: The max value of x and y as an integer. '''	
	assert max_x >= 0 and max_y >= 0
	x = random.randint(0, max_x)
	y = random.randint(0, max_y)
	return (x, y)

if __name__ == '__main__':
	root = Tk()
	root.geometry('800x800')
	c = Canvas(root, width = 800, height = 800)
	c.pack()
	x = 0
	while (x < 50):
		draw_square(c, random_color(), random_size(20, 150), \
			random_position(800, 800))
		x = x + 1
	root.bind('<q>', quit)
	root.mainloop()