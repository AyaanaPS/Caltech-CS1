# Ex B.1
def complement(DNA):
	''' Returns the complement of the inputted DNA molecule.
	Input: A DNA sequence with only A, C, G, or T bases.
	Output: A DNA sequence with only A, C, G, or T bases. '''
	DNAcomplement = ''
	for i in DNA:
		if (i == 'A'):
			DNAcomplement += 'T'
		elif (i == 'T'):
			DNAcomplement += 'A'
		elif (i == 'G'):
			DNAcomplement += 'C'
		elif (i == 'C'):
			DNAcomplement += 'G'
	return DNAcomplement

# Ex B.2
def list_complement(DNA):
	''' Returns the complement of the inputted DNA molecule.
	Input: A DNA sequence with only A, C, G, or T bases in the form of a 
	list. No Output. The list is modified. '''
	for i in range(len(DNA)):
		if(DNA[i] == 'A'):
			DNA[i] = 'T'
		elif (DNA[i] == 'T'):
			DNA[i] = 'A'
		elif (DNA[i] == 'G'):
			DNA[i] = 'C'
		elif (DNA[i] == 'C'):
			DNA[i] = 'G'

# Ex B.3
def product(list):
	''' Returns the product of the elements in a list of integers. 
	Input: A list of integers.
	Output: The product of said integers.'''
	product = 1
	for i in list:
		product *= i
	return product

# Ex B.4
def factorial(n):
	''' Returns the factorial of an inputted integer n. 
	Input: An integer.
	Output: The factorial of the integer.'''
	lst = range(1, n+1)
	productn = 1
	productn = product(lst)
	return productn


# Ex B.5
import random

def dice(m,n):
	''' This function simulates a game of Dungeons and Dragons.
	Input: The first parameter is how many sides the dice has, the second 
	parameter is the number of dice rolled.
	Output: The sum of rolls. '''
	possibilities = range(1, m+1)
	sum = 0
	for i in range(1, n+1):
		sum += random.choice(possibilities)
	return sum

# Ex B.6
# while(lst.count(val)>0)
def remove_all(lst, val):
	''' This function removes all instances of an inputted value from an 
	inputted list. 
	Input: A list to consider and the value to remove. '''
	while(lst.count(val) > 0):
		lst.remove(val)
	

# Ex B.7
def remove_all2(lst, val):
	''' This function removes all instances of an inputted value from an 
	inputted list.
	Input: A list to consider and the value to remove. '''
	for i in range(lst.count(val)):
		lst.remove(val)
		
def remove_all3(lst, val):
	''' This function removes all instances of an inputted value from an 
	inputted list. 
	Input: A list to consider and the value to remove.'''
	while (val in lst):
		lst.remove(val)

# Ex B.8
def any_in(lst1, lst2):
	''' This function checks if any elements in the first list equal any 
	elements in the second list. 
	Input: Two lists to compare.
	Output: A boolean. '''
	for i in lst1:
		if i in lst2:
			return True
	return False


# Ex C.1.a
# The '=' should actually be '=='. == tests for equivalence, while = is an 
# assignment operator.

a = 20
# ... later in the program, test to see if a has become 0.
if (a == 0):
	print 'a is zero!' 

# Ex C.1.b
# The parameter of the function shouldn't have quotes around it, because a 
# parameter representing a string is not a string itself. The parameter being
# a string means that it doesn't store the value passed into the function.

def add_suffix(s):
	'''This function adds the suffix '-Caltech' to the string s.'''
	return s + '-Caltech'

# Ex C.1.c
# The s in the return statement should not have quotes around it. The s is 
# meant to represent the string passed into the function. However, 's' is a 
# string itself and python will not replace it with s.

def add_suffix(s):
	'''This function adds the suffix '-Caltech' to the string s.'''
	return s + '-Caltech'

# Ex C.1.d
# We have to use the list method, append. Python does not allow addition of 
# lists and strings. Furthermore, you do not have to reassign lst to 
# lst.append.

# We want to add the string 'bam' to a list of strings, changing the original
# list.
lst = ['foo', 'bar', 'baz']
lst.append('bam')

# Ex C.1.e
# Defining a new lst2 within the function does not work. Instead, we can just 
# modify the lst itself.

def reverse_and_append_zero(lst):
	'''This function reverses a list of numbers and then
	appends the number 0 to the end of the list.'''
	lst.reverse()
	lst.append(0)

# Ex C.1.f
# This code would append letters to list in the form ['A', 'B']. List would 
# then
# look like ['Z', 'Y', ['A', 'B']]. To fix this, you could use a for loop
# to separately append each letter in letters to list. Also, list is a 
# keyword and shouldn't be used as a variable.

def append_string_letters_to_list(lst, str):
	'''This function converts a string 'str' to a list and appends
	the letters of the string to the list 'list'.'''
	letters = list(str)
	lst.extend(letters)

# Ex C.2
# Python follows its instructions in the order it gets them. Therefore,
# when it evaluates c = b + a, it is using the values a = 10 and b =20. 
# Thus, c = 30. After this, a's value becomes 30. However, this does not
# change the value of c, which has already been set.

# Ex C.3
# Print simply prints the value for the user to see. However, return is much 
# more valuable as it can give the value back for use later. When there is a 
# print in the function instead of return, the function can not be used as a 
# value. Return fetches the value, print doesn't. In a function, print 
# returns nothing. It simply outputs a value that cannot be used again.

# Ex C.4
# The second statement will not work because sum_of_squares_2 does not take 
# any parameters. Passing in parameters happens when calling the function. 
# Meanwhile, taking in values using raw_input interactively prompts the user 
# and collects an answer (value). sum_of_squares_2 takes raw_input, which
# means that while the program is running, it collects values from the user.

# Ex C.5
# The function upper returns a copy of the string with all characters
# converted to upper case. The fact that strings are immutable means you 
# can't change one letter. A new string would have to be created to do this.

# Ex C.6
# This does not work because the lst is not being permanently modified. In 
# order to actually modify it, you would have to loop over the range of its 
# length and change the element at each index.

def double_list(lst):
	for i in range(len(lst)):
		lst[i] = lst[i] * 2
		
