# Ex B.1
def list_reverse(lst):
	'''Returns the inverse of a list without changing the original list.
	'''
	lst2 = lst[:]
	lst2.reverse()
	return lst2

# Ex B.2
def list_reverse2(lst):
	'''Returns the inverse of a list without changing the original list.
	'''
	lst2 = []
	for j in range(len(lst)-1, -1, -1):
		lst2.append(lst[j])
	return lst2

# Ex B.3
def file_info(text_name):
	'''Returns the number of lines, words and characters in an inputted
	text file.'''
	file = open(text_name, 'r')
	numLines, numWords, numChars = (0, 0, 0)
	while True:
		line = file.readline()
		if line == '':
			break
		numLines += 1
		for i in line.split():
			numWords += 1
		for x in list(line):
			numChars += 1
	file.close()
	return (numLines, numWords, numChars)

# Ex B.4
def file_info2(text_name):
	'''Returns a dictionary of the lines, characters and words.'''
	lines, words, characters = file_info(text_name)
	dict = {
		'lines' : lines,
	        'characters' : characters,
		'words' : words
		 }
	return dict

# Ex B.5
def longest_line(text_name):
	'''Returns the longest line and line length in an inputted text file.
	'''
	file = open(text_name, 'r')
	lineLength = 0
	longestLine = ''
	for line in file:
		if len(line) > lineLength:
			lineLength = len(line)
			longestLine = line
	return(lineLength, longestLine)
	file.close()

# Ex B.6
def sort_words(str):
	'''Sorts the words in a string. Returns the sorted words as a list.
	'''
	wordLst = str.split()
	wordLst.sort()
	return wordLst

# Ex B.7
# Compare 11011010 to the sequence 128 64 32 16 8 4 2 1. The decimal 
# number will be the sum of all of the sequence numbers that have 
# a 1 in the same position for the binary number.
# Therefore, decimal = 128 + 64 + 16 + 8 + 2 = 218
# The largest number you can get is 255 [11111111]

# Ex B.8
def binaryToDecimal(lst):
	'''Takes a binary number in the form of a list and returns the 
	decimal number it represents.'''
	decimalSum = 0
	lst.reverse()
	for i in range(len(lst)):
		if (lst[i]==1):
			decimalSum += 2**i
	return decimalSum

# Ex B.9
def decimalToBinary(n):
	binary = []
	while (n > 0):
		binary.append(n % 2)
		n /= 2
	binary.reverse()
	return binary


# Ex C.2.1
# Error1: Bad Name: sc is not descriptive enough.
# Error2: Operator Space: This is hard to read. It should
#				say a * a * a + b * b * b + c * c * c
# Error3: Comma Space: There should always be commas after 
#				spaces.

# Correct Code:
def sumOfCubes(a, b, c):
	return a * a * a + b * b * b + c * c * c

# Ex C.2.2
# Error1: Bad Name: You can't see the boundaries of words 
#				in sumofcubes. Should be sumOfCubes.
# Error2: Comment_Grammatical: There are multiple spelling
#				errors in the comment
# Error3: Comment_Space: There should always be a space
#				after the open-comment sign. 
# Error4: Line_Length: The return line exceeds 80
#				characters.

# Correct Code:
def sumOfCubes(arga, argb, argc, argd):
	# return sum of cubes of args a, b, c & d.
	return arga * arga * arga + argb * argb * argb + \
		argc * argc * argc + argd * argd * argd		

# Ex C.2.3
# Error1: Blank_Lines: There should be line between the two
#				functions.
# Error2: Indent_Consistent: The first method's body is indented
#				too much. The second method's body is indented
#				too little.

# Correct Code:
def sum_of_squares(x, y):
	return x * x + y * y

def sum_of_three_cubes(x, y, z):
	return x * x * x + y * y * y + z * z * z
