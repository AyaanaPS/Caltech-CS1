from Tkinter import *

def draw_square(canvas, color, length, center):
	'''Constructs a square of the given length and color, so that
	its center is at the given position on the canvas passed to it.'''
	xc, yc = center
	rect = c.create_rectangle((xc-length/2), (yc-length/2), \
		(xc+length/2), (yc+length/2), \
		fill = color, outline = color)
	

if __name__ == '__main__':
	root = Tk()
	root.geometry('800x800')
	c = Canvas(root, width = 800, height = 800)
	c.pack()
	draw_square(c, 'red', 100, (50, 50))
	draw_square(c, 'green', 100, (750, 50))
	draw_square(c, 'blue', 100, (50, 750))
	draw_square(c, 'yellow', 100, (750, 750))
	root.mainloop()