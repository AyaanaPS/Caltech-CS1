# Ex B.1
import random
def random_size(int1, int2):
	''' This function returns random integer that is >= int1 and <= int2.
	Input: First non-negative even int must be smaller than the second.'''
	assert int2 > int1 >= 0
	assert ((int2 % 2) == 0) and ((int1 % 2) == 0)
	number = random.randint(int1, int2)
	while (number % 2 != 0):
		number = random.randint(int1, int2)
	return number

# Ex B.2
def random_position(max_x, max_y):
	'''This function returns a random (x, y) pair with x and y between 0
	and the inputted max value.
	Input: The max value of x and y as an integer. '''
	assert max_x >= 0 and max_y >= 0
	x = random.randint(0, max_x)
	y = random.randint(0, max_y)
	return (x, y)

# Ex B.3
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

# Ex B.4
def count_values(dictionary):
	'''Count the amount of distinct values in a dictionary. 
	Input: A dictionary. '''
	lst = dictionary.values()
	for i in lst:
		while (lst.count(i) > 1):
			lst.remove(i)
	count = len(lst)
	return count
		
# Ex B.5
def remove_value(dictionary, value):
	'''Removes all key/value pairs from the dictionary that equal the 
	inputted value.'''
	lst = []
	for key in dictionary:
		if dictionary[key] == value:
			lst.append(key)
	for i in lst:
		del dictionary[i]
	return dictionary

# Ex B.6
def split_dict(dictionary):
	'''Splits the inputted dictionary into two - d1 contains keys that 
	start with letters a-m and d2 contains keys that start with letters
	n-z.'''
	d1 = {}
	d2 = {}
	for key in dictionary:
		if key.lower() < 'n' and key.lower() >= 'a':
			d1[key] = dictionary[key]
		elif key.lower() <= 'z' and key.lower() > 'm':
			d2[key] = dictionary[key]
	return (d1, d2)

# Ex B.7
def count_duplicates(dictionary):
	'''Takes a dictionary and returns the number of values that appear 
	two or more times.'''
	lst = dictionary.values()
	duplicates = 0
	for i in lst:
		if lst.count(i) > 1:
			while lst.count(i) > 1:
				lst.remove(i)
			duplicates += 1
	return duplicates
		