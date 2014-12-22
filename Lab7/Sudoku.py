'''
This program allows the user to interactively play the game of Sudoku.
'''

import sys

class SudokuError(Exception):
    pass

class SudokuMoveError(SudokuError):
    pass

class SudokuCommandError(SudokuError):
    pass

class Sudoku:
    '''Interactively play the game of Sudoku.'''

    def __init__(self):
        '''Initializes the game board with a 9x9 grid filled with 0's.'''
        self.board = []
        i = 0
        while i < 9:
            self.board.append([0, 0, 0, 0, 0, 0, 0, 0, 0])
            i += 1
        self.moves = []

    def load(self, filename):
        '''Loads the file inputted into the game board.'''
        okay = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        file = open(filename, 'r')
        lines = file.readlines()
        if len(lines) != 9:
            raise IOError('File should only have 9 lines.')
        lineNum, charNum = (0, 0)
        for line in lines:
            line = line[:-1]
            if len(line) != 9:
                raise IOError('Each line should only have 9 numbers.')
            for char in line:
                if char != okay:   
                    self.board[lineNum][charNum] = int(char)
                else:
                    raise IOError('File contains inputs not 1-9 integers.')
                charNum += 1
            lineNum += 1
            charNum = 0
        self.moves = []
        file.close()
        return self.board

    def save(self, filename):
        '''Saves the current state of the game board to a new file.'''
        file = open(filename, 'w')
        lst2 = []
        for lst in self.board:
            for i in lst:
                lst2.append(str(i))
            string = ''.join(lst2)
            file.write(string + '\n')
            lst2 = []
        file.close()

    def show(self):
        '''Pretty-print the current board representation.'''
        print
        print '   1 2 3 4 5 6 7 8 9 '
        for i in range(9):
            if i % 3 == 0:
                print '  +-----+-----+-----+'
            sys.stdout.write('%d |' % (i + 1))
            for j in range(9):
                if self.board[i][j] == 0:
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('%d' % self.board[i][j])
                if j % 3 != 2 :
                    sys.stdout.write(' ')
                else:
                    sys.stdout.write('|')
            print 
        print '  +-----+-----+-----+'
        print

    def move(self, row, col, val):
        '''Checks to see if the inputted value can be added to the box at 
        row and col and then updates the board.'''
        if row <= 0 and col <= 0 and val <= 0 and row > 9 and col > 9 and \
           val > 9:
            raise SudokuMoveError('Inputted values must be between 1 and 9.')
        if self.board[row-1][col-1] != 0:
            raise SudokuMoveError('Position on board is already occupied.')
        for j in range(9):
            if self.board[row-1][j] == val:
                raise SudokuMoveError('Value is already in the row.')
            if self.board[j][col-1] == val:
                raise SudokuMoveError('Value is already in the column.')
        (startr, endr), (startc, endc) = (0, 0), (0, 0)
        x, y = row, col
        while(x%3 != 0):
            x += 1
        startr, endr = (x-2, x)
        while(y%3 != 0):
            y += 1
        startc, endc = (y-2, y)
        for i in range(startr, endr+1):
            for x in range(startc, endc+1):
                if self.board[i-1][x-1] == val:
                    raise SudokuMoveError('Value is already in box.')
        self.board[row-1][col-1] = val
        self.moves.append((row, col, val))


    def undo(self):
        '''Undoes the last move of the user.'''
        row, col, val = self.moves.pop()
        self.board[row-1][col-1] = 0

    def solve(self):
        '''Takes a command and implements it.'''
        completed = False
        while(not completed):
            try:
                s = raw_input('Enter a command: ')
                lst = s.split()
                if lst[0] == 'q':
                    completed = True
                elif lst[0] == 'u':
                    self.undo()
                    self.show()
                elif lst[0] =='s':
                    self.save(lst[1])
                elif s > '111' or s < '999':
                    nums = list(s)
                    self.move(int(nums[0]), int(nums[1]), int(nums[2]))
                    self.show()
                else:
                    raise SudokuCommandError('Command does not exist.')
            except SudokuMoveError as e:
                print e
                self.show()
            except SudokuCommandError as x:
                print x
                self.show()
            

if __name__ == '__main__':
    s = Sudoku()

    while True:
        filename = raw_input('Enter the sudoku filename: ')
        try:
            s.load(filename)
            break
        except IOError, e:
            print e

    s.show()
    s.solve()

