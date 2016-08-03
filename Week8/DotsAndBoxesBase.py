'''
DotsAndBoxesBase.py: 
  Base class for the dots-and-boxes game implemented in Python.
'''

import sys, random

#
# Helper functions.
#

def makeEdge(p1, p2):
    '''
    Make an edge from two adjacent points.
    An edge is a frozenset of two adjacent points on the grid.

    Arguments:
      p1, p2: points
    Return value: 
      the edge
    '''
    return frozenset([p1, p2])

#
# Exception classes.
#

class InvalidMoveError(Exception):
    '''
    Objects of this exception class are raised when the user
    attempts to make an invalid move.
    '''
    pass

class InvalidPlayerError(Exception):
    '''
    Objects of this exception class are raised when an invalid
    computer player has been selected.
    '''
    pass

class DotsAndBoxesBase:
    '''Base class for dots and boxes game.'''

    def makeComputerMove(self, computerPlayer):
        '''
        Make a move using one of the computer players.

        Argument:
          computerPlayer: a string; either 'C1', 'C2', or 'C3'
          which identifies which computer player will be selected
        Return value:
          True if the same player gets another move, else False
        '''
        move = None
        if computerPlayer == 'C1':
            move = self.getComputerMove1()
        elif computerPlayer == 'C2':
            move = self.getComputerMove2()
        elif computerPlayer == 'C3':
            move = self.getComputerMove3()
        else:
            msg = 'Unknown player: %s' % computerPlayer
            raise InvalidPlayer('Unknown player: %s' % msg)
        (p1, p2) = move
        return self.makeMove(p1, p2)

    def autoPlay(self, player1, player2, verbose=False):
        '''
        Play a game between two computer players.

        Arguments:
          player1: string identifying computer player 1
          player2: string identifying computer player 2
          verbose: boolean; if True, print game output during game
        Return value:
          A two-tuple of the final count of boxes of each player.
        '''
        self.reset()
        while len(self.filledEdges) < len(self.allEdges):
            if self.toMove == 1:
                if verbose:
                    print 'Player to move: %s' % player1
                repeat = self.makeComputerMove(player1)
            else:
                if verbose:
                    print 'Player to move: %s' % player2
                repeat = self.makeComputerMove(player2)
            if not repeat:
                self.changePlayers()
            if verbose:
                self.show()
                print 'player 1: %d boxes; player 2: %d boxes' % \
                  self.countBoxes()

        assert len(self.filledEdges) == len(self.allEdges)
        # No more unfilled edges; the game is over.
        (count1, count2) = self.countBoxes()
        if verbose:
            print 'Game over.'
            if count1 > count2:
                print 'Player %s wins!' % player1
            elif count2 > count1:
                print 'Player %s wins!' % player2
            else:
                print 'Draw!'
        return (count1, count2)

    def play(self, computerPlayer):
        '''
        Play the game interactively between a human player and a computer
        player.  The human player is player 1 and the computer player is player
        2.

        Arguments:
          computerPlayer: a string identifying the computer player
        Return value: none.
        '''

        self.reset()
        print 'Dots and boxes game'
        print '-------------------'
        print
        while len(self.filledEdges) < len(self.allEdges):
            try:
                    if self.toMove == 2:
                        print 'Player to move: computer'
                        repeat = self.makeComputerMove(computerPlayer)
                    else:
                        print 'Player to move: you'
                        raw_move = raw_input('Enter move (r1 c1 r2 c2): ')
                        move = raw_move.strip().split()
                        if raw_move == 'quit':
                            print 'Exiting game...'
                            return
                        elif len(move) != 4:
                            raise InvalidMoveError('bad input')
                        else:
                            r1 = int(move[0])
                            c1 = int(move[1])
                            r2 = int(move[2])
                            c2 = int(move[3])
                            repeat = self.makeMove((r1, c1), (r2, c2))
                    if not repeat:
                        self.changePlayers()
                    self.show()
                    print 'player 1: %d boxes; player 2: %d boxes' % \
                      self.countBoxes()
            except InvalidMoveError as e:
                print 'invalid move: %s' % e.message
            except ValueError as e:
                print 'invalid move: %s' % e.message

        assert len(self.filledEdges) == len(self.allEdges)
        # No more unfilled edges; the game is over.
        (count1, count2) = self.countBoxes()
        print 'Game over.'
        if count1 > count2:
            print 'Player wins!'
        elif count2 > count1:
            print 'Computer wins!'
        else:
            print 'Draw!'
        
    def show(self):
        '''
        Display a representation of the game to the terminal.

        Arguments: none
        Return value: none
        '''
        write = sys.stdout.write
        print
        write('  ')
        for c in range(self.ncols):
            write(str(c) + ' ')
        write('\n')
        for r in range(self.nrows):
            write(str(r) + ' ')
            # Write out a row of dots and horizontal lines.
            for c in range(self.ncols):
                write('.')
                e = makeEdge((r, c), (r, c + 1))
                if e in self.filledEdges:
                    write('-')
                else:
                    write(' ')
            write('\n')
            if r < self.nrows - 1:
                # Write out a row of vertical lines and box names.
                write('  ')
                for c in range(self.ncols):
                    e = makeEdge((r, c), (r + 1, c))
                    if e in self.filledEdges:
                         write('|')
                    else:
                         write(' ')
                    if c < self.ncols - 1:
                        if (r, c) in self.filledBoxes:
                            write(str(self.filledBoxes[(r, c)]))
                        else:
                            write(' ')
                write('\n')
        print

# end class DotsAndBoxesBase

def usage():
    '''Print a usage message and exit.'''

    usagestr = '''usage: python %s <arguments>
  where <arguments> is either:
    nrows ncols computer_player
    nrows ncols computer_player computer_player nrepeats
  where:
    nrows, ncols: integers >= 3
    nrepeats: integer > 0
    computer player: one of C1, C2, or C3

  If two computer players are given, the game plays itself.
  If nrepeats > 1, the game plays itself silently and the
  aggregate results are printed.''' % sys.argv[0]

    print >> sys.stderr, usagestr
    sys.exit(1)

