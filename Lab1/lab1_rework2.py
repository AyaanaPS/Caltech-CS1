# Tracking with git.

# Ex C.1
# C.1.1 --> 9 - 3 = 6
# C.1.2 --> 8 * 2.5 = 20.0
# C.1.3 --> 9 / 2 = 4
# C.1.4 --> 9 / -2 = -5
# C.1.5 --> 9 % 2 = 1
# C.1.6 --> 9 % -2 = -1
# C.1.7 --> -9 % 2 = 1
# C.1.8 --> 9 / -2.0 = -4.5
# C.1.9 --> 4 + 3 * 5 = 19
# C.1.10 --> (4 + 3) * 5 = 35

# Ex C.2
# C.2.1 --> 100
# C.2.2 --> 110
# C.2.3 --> 130
# C.2.4 --> 90
# C.2.5 --> 40
# C.2.6 --> 120
# C.2.7 --> 24
# C.2.8 --> 0

# Ex C.3
# First, Python evaluates x - x. It then adds (x-x) to x.
# When x has the initial value of 3, the final value of x is 3.

# Ex C.4
# C.4.1--> 1j + 2.4j = 3.4j
# C.4.2--> 4j * 4j = (-16 + 0j)
# C.4.3--> (1 + 2j) / (3 + 4j) = (0.44 + 0.08j)

# C.4.1--> (1 + 2j) * (1 + 2j) = (-3 + 4j)
# C.4.2--> 1 + 2j * 1 + 2j = (1 + 4j)

# The two expressions are different because of the order of operations.
# Python calculates multiplication before addition. Therefore, it begins by
# multiplying 1 and 2j and then it performs the addition. This tells me that
# Python does not give complex numbers higher precendence in the order of 
# operations. Furthermore, complex numbers are stored in their two parts - 
# real and imaginary. Complex numbers are treated sort of like variables.  

# Ex C.5
# C.5.1--> cmath.sin(-1.0 + 2.0j) = (-3.165778513216168 + 1.959601041421606j)
# C.5.2--> cmath.log(-1.0 + 3.4j) = (1.2652585805200263 + 1.856847768512215j)
# C.5.3--> cmath.exp(-cmath.pi * 1.0j) = (-1-1.2246467991473532e-16j)

# There could be many functions that have the same name in both math and 
# cmath. However, only one definition of a function can exist at any given 
# point in a program. The most recently imported function (of the method 
# you're trying to reach) will be used. (This is called 'Name clash'). This 
# could cause serious issues in the code because the programmer is using the 
# wrong function. Meanwhile, import math and import cmath are fine because in
# the function you would call methods using math.method or cmath.method, 
# which stops name clashes from occuring. 

# Ex C.6
# C.6.1--> "foo" + 'bar' = 'foobar'
# C.6.2--> "foo" 'bar' = 'foobar'
# C.6.3--> a = 'foo'
#	       b = "bar"
#	       a + b = 'foobar'
# C.6.4--> a = 'foo'
#	       b = "bar"
#	       a b = SyntaxError: invalid syntax

# Ex C.7
# 'A\nB\nC'

# Ex C.8
# print '-' * 80

# Ex C.9
# prin 'first line\nsecond line\nthird line' 

# Ex C.10
x = 3
y = 12.5
print 'The rabbit is %d.' %x
print 'The rabbit is %d years old.' %x
print '%.1f is average.' %y
print '%.1f * %d' %(y, x)
print '%.1f * %d is %.1f.' %(y, x, x*y)

# Ex C.11
num = raw_input('Enter a number: ')
print num

# Ex C.12
def quadratic(a, b, c, x):
	value = a*(x*x) + b*x + c
	return value


# Ex C.13
def GC_content(DNA):
	'''Returns the proportion of C/G bases in a DNA molecule. 
	Input Argument: A DNA sequence with only A, C, G, or T bases. 
	Output: A single float. '''
	subG = 'G'
	subC = 'C'
	GCnumber = float(DNA.count(subG) + DNA.count(subC))
	lengthDNA = float(len(DNA))
	proportion = GCnumber/lengthDNA
	return proportion
