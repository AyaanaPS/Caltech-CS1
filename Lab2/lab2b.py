import random

# Ex D.1
def make_random_code():
	''' Generates a random 4 letter code. '''
	possibilities = ['R', 'G', 'B', 'Y', 'O', 'W']
	code = ''
	n = 0
	while (n<4):
		code += random.choice(possibilities)
		n += 1
	return code

# Ex D.2
def count_exact_matches(string1, string2):
	''' Counts the amount of times two strings have the exact same 
	letters in the same locations. '''
	count = 0
	for i in range(4):
		if (string1[i] == string2[i]):
			count += 1
	return count

# Ex D.3
def count_letter_matches(string1, string2):
	''' Counts the amount of letters that appear in both strings. '''
	list1 = list(string1)
	list2 = list(string2)
	count = 0
	for i in list1:
		if i in list2:
			count += 1
			list2.remove(i)
	return count

# Ex D.4
def compare_codes(code, guess):
	''' Uses count_letter_matches and count_exact_matches to generate a 
	comparison string. '''
	blackpegs = count_exact_matches(code, guess)
	whitepegs = count_letter_matches(code, guess) - blackpegs
	blankpegs = 4 - (blackpegs + whitepegs)
	comparison = 'b'*blackpegs + 'w'*whitepegs + '-'*blankpegs
	return comparison

# Ex D.5
def run_game():
	''' Uses compare_codes function to actually run the game simulation. 
	'''
	print 'New Game'
	count = 0
	code = make_random_code()
	result = ''
	while (result != 'bbbb'):
		guess = raw_input('Enter your guess: ')
		result = compare_codes(code, guess)
		print 'Result: ' + result
		count += 1
	if (result == 'bbbb'):
		print 'Congrats! You cracked the code in %d moves!' % count
