# Ayaana Patel Sikora
# CMS Cluster Login: asikora
import random
# 
# Part One: Pitfalls
#
# Problem 1.1
#
# Error 1: Docstring should be ''' not ''
# Error 2: Variable chars should not have quotes around it.
# Error 3: There should be a ':' at the end of the for line.
# Error 4: Should be == not - in the if statement.
# Error 5: Should be lst(s) not list(s)

# Problem 1.2
# 
# Error 1: A new variable should be created and set to name.split().
# 	Setting name to name.split() is confusing.
# Error 2: val, first and last haven't been defined yet. 
# 	They need to be created before the for loop.
# Error 3: dict[key] = val is unnecessary because dict[key] already
# 	equals val.
# Error 4: Strings are immutable. Thus, first[position] = new_char 
# 	will not work. 
# Error 5: [key[0], key[1]] is incorrect. It should be (key[0], key[1]) 
# 	because tuples are initialized that way. 
#
# Problem 1.3
# 
# Wasn't sure if you wanted me to list the errors for each function 
# togehter or separately, so I just did this.
#
# Errors for def ce(): 
#
# Error 1: Operator_Space: There should be a space around the = sign.
#	Should be s = 1, f = 1 ...
# Error 2: Comma_Space: There should be a space after every comma.
#	Should be (1, 20)
# Error 3: Bad_Names: ce is not descriptive enough.
# Error 4: Indent_Consistent: Indentation levels are not consistent.
# 	The indent in the for loop body is too much.
# Error 5: Magic_Number: 20 appears to be an arbitrary limit for the range.
#
# Errors for def ip(s):
#
# Error 1: Comment_Space: There should always be a space after the # sign.
#	Should be # xxx and # grr.
# Error 2: Bad_Names: ip is not desciptive enough.
# Error 3: Indent_Consistent: Indentation levels are not consistent.
# 	The indent in the if statement is too little.
# Error 4: Comment_Full_Sentences: The comments # xxx and # grr are not 
#	sentences.
# Error 5: Comment_Meaningless: The comments # xxx and # grr appear to be
#	meaningless. 
# Error 6: Operator_Space: There should be spaces around opeartors.
#	Should be b != s[q - 1 - a]


# Part Two: Writing Simple Functions

# Problem 2.1
def top_two(int1, int2, int3):
	'''Returns the top two integers of the three integer arguments.'''
	if int1 > int2 and int1 > int3:
		if int2 > int3:
			return (int1, int2)
		else:
			return (int1, int3)
	elif int2 > int1 and int2 > int3:
		if int1 > int3:
			return (int2, int1)
		else:
			return (int2, int3)
	else:
		if int2 > int1:
			return (int3, int2)
		else:
			return (int3, int1)

# Problem 2.1
# Honor Roll Version:
def top_two(int1, int2, int3):
	'''Returns the top two integers of the three integer arguments.'''
	return(max(int1, int2, int3), max(min(int1, int2), min(int1, int3), \
	                                  min(int2, int3)))

# Problem 2.2
def print_squares(n):
	'''Takes a positive odd integer n which is at least 1 as input. 
	Outputs a sequence of square-shaped patterns of asterisk characters. 
	Each square has an odd side length and is separated by a space.'''
	assert n >= 1
	assert n % 2 != 0
	pad = ''
	while (n >= 1):
		for i in range(n):
			if (i != 0 and i != (n-1)):
				print pad + '*' + (' ' * (n-2)) + '*'
			else:
				print pad + '*' * n
		print '\n'
		n -= 2
		pad += ' '

# Problem 2.3
def monte_carlo(a, b, n):
	'''Takes the lower x value, upper x value and number of random points 
	as input. Finds the monte carlo approximation and returns it as a 
	floating point number.'''
	assert n > 0 and a >= 0 and b >= a
	length = b - a
	count, ymax = 0, 0
	divisions = n
	for i in range(int(a), int(b+1)):
		if i**2 > ymax:
			ymax = i**2
	boundingArea = ymax*length
	while(n > 0):
		ypoint = random.random() * ymax
		xpoint = (random.random() * length) + a
		if ypoint <= xpoint**2:
			count += 1
		n -= 1
	return (count/float(divisions)) * boundingArea

def monte_carlo_sequence(a, b, k):
	'''Prints out monte carlo approximations with varying number of 
	random points. The varying points are 10 to the power of the range of 
	k.'''
	x = 0
	while (x < k):
		print (' ' * (k - x)) + str(10**x) + '\t' +  \
		      (('%.' + str(x) + 'f') % monte_carlo(a, b, 10**x))
		x += 1

# Part 3: Microproject: Morse code

morse_code = {
'a' : '.-',
'b' : '-...',
'c' : '-.-.',
'd' : '-..',
'e' : '.',
'f' : '..-.',
'g' : '--.',
'h' : '....',
'i' : '..',
'j' : '.---',
'k' : '-.-',
'l' : '.-..',
'm' : '--',
'n' : '-.',
'o' : '---',
'p' : '.--.',
'q' : '--.-',
'r' : '.-.',
's' : '...',
't' : '-',
'u' : '..-',
'v' : '...-',
'w' : '.--',
'x' : '-..-',
'y' : '-.--',
'z' : '--..'
}

# Problem 3.1
def invert_dict(oldDict):
	'''Switches the keys with the values (and vice versa) in a dictionary. 
	Returns the inverted dictionary.'''
	newDict = {}
	for key in oldDict:
		newDict[oldDict[key]] = key
	return newDict

morse_uncode = invert_dict(morse_code)

# Problem 3.2
def find_substring(string, index, stopChar):
	'''Returns the substring from an inputted string starting from a given
	index and ending at the index of a stopChar. If the stopChar is not
	in the string, the substring goes to the end of the string.'''
	assert index >= 0 and index < len(string)
	substring = ''
	if stopChar not in string:
		substring = string[index:]
	else:
		while (string[index] != stopChar):
			substring += string[index]
			index += 1
	return substring

# Problem 3.3
def to_morse_code(s):
	'''Converts an inputted string to morse code using the morse code 
	dictionary. Returns the converted morse code string.'''
	new_string = ''
	for i in s:
		if i >= 'a' and i <= 'z':
			new_string += '[' + morse_code[i] + ']'
		elif i >= 'A' and i <= 'Z':
			new_string += '{' + morse_code[i.lower()] + '}'
		elif i == '[' or i == ']' or i == '{' or i == '}' or i == '.' \
		     or i == '-' or i == '\\':
			new_string += '\\' + i
		else:
			new_string += i
	return new_string

# Problem 3.4
def from_morse_code(m):
	'''Converts an inputted morse code string from morse code using the 
	morse uncode dictionary. Returns the converted string.'''
	new_string = ''
	i = 0
	while i < len(m):
		if m[i] == '[':
			sub = find_substring(m, i + 1, ']')
			new_string += morse_uncode[sub]
			i += len(sub) + 1
		elif m[i] == '{':
			sub = find_substring(m, i + 1, '}')
			new_string += morse_uncode[sub].upper()
			i += len(sub) + 1
		elif m[i] == '\\':
			new_string += m[i+1]
			i += 1
		else:
			new_string += m[i]
		i += 1
	return new_string

# Problem 3.5.a
def convert_file_to_morse_code(filename_root, ext1, ext2):
	'''Converts the text in a file into morse code and saves it as a new 
	file in the same directory with the extension inputted.'''
	file1 = open(filename_root+ext1, 'r')
	file2 = open(filename_root+ext2, 'w')
	while True:
		line = file1.readline()
		file2.write(to_morse_code(line))
		if (line == ''):
			break
	file1.close()
	file2.close()

# Problem 3.5.b
def convert_file_from_morse_code(filename_root, ext1, ext2):
	'''Converts the text in a file into normal english and saves it as a 
	new file in the same directory with the extension inputted.'''
	file1 = open(filename_root+ext1, 'r')
	file2 = open(filename_root+ext2, 'w')
	while True:
		line = file1.readline()
		file2.write(from_morse_code(line))
		if(line == ''):
			break
	file1.close()
	file2.close()
