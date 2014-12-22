# student name: Ayaana Sikora
# student login: asikora

import sys, random
from DotsAndBoxesBase import *

#
# Helper functions.
#

def getEdgesFromBox(box):
    '''
    Get all the edges from a box.  A box is represented as a
    (row, column) tuple where the row and column coordinates
    are from the corner of the box having the lowest row and
    column coordinates.

    Arguments:
      box: a box
    Return value:
      All the edges from a box as a list.
    '''
    pt1, pt2 = box
    boxEdges = []
    boxEdges.append(makeEdge(box, (pt1 + 1, pt2)))
    boxEdges.append(makeEdge(box, (pt1, pt2 + 1)))
    boxEdges.append(makeEdge((pt1 + 1, pt2), (pt1 + 1, pt2 + 1)))
    boxEdges.append(makeEdge((pt1 + 1, pt2 + 1), (pt1, pt2 + 1)))
    return boxEdges
    

class DotsAndBoxes(DotsAndBoxesBase):
    '''
    Instances of this class allow a user to play a game of "dots and boxes"
    against the computer.
    '''

    def __init__(self, nrows, ncols):
        '''
        Initialize the object.
        Arguments:
          nrows: integer >= 3; the number of rows in a grid of points
          ncols: integer >= 3; the number of columns in a grid of points
        '''
        if type(nrows) != int or type(ncols) != int:
            raise TypeError('Rows and Columns must be ints.')
        if nrows < 3 or ncols < 3:
            raise ValueError('Rows and Columns should be >= to 3!')     
        self.nrows = nrows
        self.ncols = ncols
        self.allEdges = self.makeAllEdges()
        self.allBoxes = self.makeAllBoxes()
        self.edgeBoxes = self.makeEdgeBoxes()
        self.filledEdges = set([])
        self.filledBoxes ={}
        self.toMove = random.randint(1, 2)

    def reset(self):
        '''
        Reset the game to the initial state.
        Arguments: none
        Return value: none
        '''
        self.filledEdges = set([])
        self.filledBoxes = {}
        self.toMove = random.randint(1, 2)

    def makeAllEdges(self):
        '''
        Arguments: none
        Return value: a set containing all valid edges on the board
        '''
        allEdges = set([])
        for i in range(self.nrows):
            for x in range(self.ncols):
                if i == self.nrows - 1:
                    if x != self.ncols - 1:
                        allEdges.add(makeEdge((i, x), (i, x+1)))
                else:
                    if x == self.ncols - 1:
                        allEdges.add(makeEdge((i, x), (i+1, x)))
                    else:
                        allEdges.add(makeEdge((i, x), (i+1, x)))
                        allEdges.add(makeEdge((i, x), (i, x+1)))
        return allEdges

    def makeAllBoxes(self):
        '''
        Arguments: none
        Return value: 
          a set containing all valid boxes (of side length 1) on the board
        '''
        allBoxes = set([])
        for i in range(self.nrows - 1):
            for x in range(self.ncols - 1):
                allBoxes.add((i, x))
        return allBoxes

    def makeEdgeBoxes(self):
        '''
        Arguments: none
        Return value: 
          a dictionary mapping each edge to a list of the boxes adjacent
          to that edge
        '''
        edgeBoxes = {}
        for i in self.allBoxes:
            for x in getEdgesFromBox(i):
                for z in self.allEdges:
                    if x == z:
                        if x in edgeBoxes:
                            edgeBoxes[x].append(i)
                        else:
                            edgeBoxes[x] = [i]
        return edgeBoxes
                
    def isFilled(self, box):
        '''
        Arguments: 
          box: a box
        Return value:
          True if the box 'box' is filled i.e. if all its edges are filled
        '''
        filled = True
        for i in getEdgesFromBox(box):
            if i not in self.filledEdges:
                filled = False
        return filled

    def makesABox(self, edge):
        '''
        Arguments:
          edge: an edge
        Return value:
          True if playing the edge 'edge' would make a box.
        '''
    
        if edge in self.filledEdges:
            raise ValueError('Edge is already filled.')
        self.filledEdges.add(edge)
    
        for x in self.edgeBoxes[edge]:
            if self.isFilled(x) == True:
                completed = True
                break
            else:
                completed = False
                
        self.filledEdges.remove(edge)

        return completed

    def getComputerMove1(self):
        '''
        Select a move for the computer to make on the current board.
        Choose a random (legal) move.

        Arguments: none
        Return value: the move chosen
        '''
        edge = random.sample(self.allEdges, 1)
        while edge[0] in self.filledEdges:
            edge = random.sample(self.allEdges, 1)
        return edge[0]

    def getComputerMove2(self):
        '''
        Select a move for the computer to make on the current board.
        If there are one or more moves which will make a box, select one
        such move at random.
        Otherwise, choose a random (legal) move.

        Arguments: none
        Return value: the move chosen
        '''
        goodMoves = []
        for edge in self.allEdges:
            if edge not in self.filledEdges and self.makesABox(edge) == True:
                    goodMoves.append(edge)
    
        if len(goodMoves) != 0:
            edge = random.choice(goodMoves)
            
        else:
            x = random.sample(self.allEdges, 1)
            while x[0] in self.filledEdges:
                x = random.sample(self.allEdges, 1)
                edge = x[0]
        
        print edge
        print 'Checking: '
        if edge in self.filledEdges:
            print 'Yes'
        else:
            print 'No'
        return edge
             
    
    def getComputerMove3(self):
        '''
        Select a move for the computer to make on the current board.
        If there are one or more moves which will make a box, select one
        such move at random.
        Otherwise randomly pick any move that will not allow the other player
        to make a box on his next move.
        Otherwise, choose a random legal move.

        Arguments: none
        Return value: the move chosen
        '''
        goodMoves = []
        safeMoves = []
        for i in self.allEdges:
            
            if i not in self.filledEdges:
                if self.makesABox(i) == True:
                    goodMoves.append(i)
                else:
                    safeMoves.append(i)
                            
        if len(goodMoves) == 0:
            edge = random.choice(safeMoves)
        
        else:
            edge = random.choice(goodMoves)
                    
        
        return edge        

    def makeMove(self, p1, p2):
        '''
        Make a move on the board by connecting two adjacent points.
        Raises 'InvalidMoveError' if the points don't constitute
        a valid move.  If the move creates a box, record that in 
        the 'filledBoxes' field of the object and give the player
        another move.

        Arguments:
          p1, p2: points
        Return value:
          True if the same player gets another move, else False
        '''
        
        edge = makeEdge(p1, p2) 
        if edge not in self.allEdges:
            raise InvalidMoveError('Points are not adjacent.')
        if edge not in self.allEdges:
            raise InvalidMoveError('Points are not on the board.')
        if edge in self.filledEdges:
            raise InvalidMoveError('Edge is already filled')
        
        if self.makesABox(edge) == True:
            self.filledEdges.add(edge)
            for x in self.edgeBoxes[edge]:
                if self.isFilled(x) == True:
                    self.filledBoxes[x] = self.toMove
            return True
        else:
            self.filledEdges.add(edge)
            return False
        
        
    def countBoxes(self):
        '''
        Arguments: none
        Return value:
          a tuple of the count of boxes filled by the players,
          with player 1's count coming first
        '''
        player1, player2 = 0, 0
        for key in self.filledBoxes:
            if self.filledBoxes[key] == 1:
                player1 += 1
            else:
                player2 += 1
        return (player1, player2)

    def changePlayers(self):
        '''
        Change the next player to play.

        Arguments: none
        Return value: none
        '''
        if self.toMove == 1:
            self.toMove = 2
        else:
            self.toMove = 1

    def comparePlayers(self, player1, player2, nrepeats):
        '''
        Play computer players 'player1' and 'player2' against each other
        'nrepeats' times and add up the total number of boxes marked by
        both players.  Return the average number of boxes scored per player
        per game.

        Arguments:
          player1: string representing a computer player
          player2: string representing a computer player
          nrepeats: integer > 0
        Return value:
          A 2-tuple of floating-point numbers, representing the average
          number of boxes scored per game for player1, player2 respectively.
        '''
        possible = ['C1', 'C2', 'C3']
        assert player1 in possible or player2 in possible
        x = 0
        boxes1, boxes2 = 0, 0
        while x < nrepeats:
            a, b = self.allPlay(player1, player2, True)
            boxes1 += a
            boxes2 += b
        average1 = boxes1/nrepeats
        average2 = boxes2/nrepeats
        return (average1, average2)


if __name__ == '__main__':
    computerPlayers = ['C1', 'C2', 'C3']
    args = sys.argv
    try:
        if len(args) != 4 and len(args) != 6:
            usage()

        nrows = int(args[1])
        ncols = int(args[2])
        if nrows < 3 or ncols < 3:
            usage()
        db = DotsAndBoxes(nrows, ncols)
        computerPlayer1 = args[3]
        if computerPlayer1 not in computerPlayers:
            usage()

        if len(args) == 4:
            db.play(computerPlayer1)
        else:  # len(args) == 6
            computerPlayer2 = args[4]
            if computerPlayer2 not in computerPlayers:
                usage()
            # Note that it's perfectly legal to have 
            #   computerPlayer1 == computerPlayer2
            nrepeats = int(args[5])
            if nrepeats == 1:
                db.autoPlay(computerPlayer1, computerPlayer2, True)
            else:
                print 'Comparing computer players %s and %s' % \
                  (computerPlayer1, computerPlayer2)
                (score1, score2) = \
                  db.comparePlayers(computerPlayer1, computerPlayer2, nrepeats)
                print '%d games played.' % nrepeats
                print 'Computer player 1: %g boxes per game' % score1
                print 'Computer player 2: %g boxes per game' % score2
    except ValueError:   # non-integer values for nrows, ncols, nrepeats
        usage()

