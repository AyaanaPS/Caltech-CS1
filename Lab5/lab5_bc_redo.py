import math

# B.1
class Point:
	def __init__(self, x, y, z):
		'''Initializes new point object.'''
		self.x = x
		self.y = y
		self.z = z

	def distanceTo(self, p2):
		'''Calculates the distance from the current point to an 
		inputted point using the distance formula.'''
		distance = math.sqrt((self.x-p2.x)**2 + (self.y-p2.y)**2 + \
		                     (self.z-p2.z)**2)
		return distance

# B.2
class Triangle:
	def __init__(self, point1, point2, point3):
		'''Initializes new triangle object.'''
		self.p1 = point1
		self.p2 = point2
		self.p3 = point3
	
	def area(self):
		'''Calculates the area of the current triangle object.'''
		a = (self.p1).distanceTo(self.p2)
		b = (self.p2).distanceTo(self.p3)
		c = (self.p3).distanceTo(self.p1)
		s = (a + b + c) / 2
		area = math.sqrt(s * (s - a) * (s - b) * (s - c))
		return area
	
# B.3
class Averager:

	def __init__(self):
		'''Initializes new averager list object.'''
		self.nums = []
		self.total = 0
		self.n = 0.0

	def getNums(self):
		'''Returns a copy of the current list.'''
		return self.nums[:]
		# self.total and self.n do not have to be updated as this
		# is an accessor method, not a mutator method.

	def append(self, n):
		'''Appends an inputted value to the current list.'''
		self.nums.append(n)
		self.total += n
		self.n += 1

	def extend(self, lst2):
		'''Extends the current list by some new list.'''
		self.nums.extend(lst2)
		for i in lst2:
			self.total += i
		self.n += len(lst2)

	def average(self):
		'''Returns the average of the values in list.'''
		if self.n == 0:
			average = 0
		else:
			average = self.total/self.n
		return average
		# self.nums self.total and self.n are not being updated here.

	def limits(self):
		'''Returns the limits of a list.'''
		if len(self.nums) > 0:
			return (min(self.nums), max(self.nums))
		else:
			return (0, 0)
		# self.nums, self.total, & self.n are not being updated here.

# C.1
# This function contains unnecessary code. The else statement is not needed.

def is_positive(x):
	'''Test if x is positive.'''
	return x > 0


# C.2
# This function contains excessively complex code and  unnecessarily 
# inefficient code. There is no need for the use of booleans. Furthermore,
# the use of the else is unnecessary because a return statement breaks out
# of the function.

def find(x, lst):
	'''Returns the index into a list where x is found, or -1 otherwise.
	Assume that x is found at most once in the list.'''
	for i in range(len(lst)):
		if lst[i] == x:
			return i
	return -1

# C.3
# This function contains unnecessarily inefficient code. The use of multiple
# if statments without any else if's or else statements is a design flaw.

def categorize(x):
	'''Return a string categorizing the number 'x', which should be
	an integer.'''
	if x < 0:
		category = 'negative'
	elif x == 0:
		category = 'zero'
	elif x > 0 and x < 10:
		category = 'small'
	else:
		category = 'large'
	return category

# C.4
# This function contains unnecessarily inefficient code. It doesn't need to
# see how many elements there are in the list to calculate the sum. 

def sum_list(lst):
	'''Returns the sum of the elements of a list of numbers.'''
	sumlst = 0
	for i in lst:
		sumlst += i
	return sumlst



