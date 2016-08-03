'''
final_tests.py: Tests of the dots-and-boxes game implemented in Python.

NOTE: This is a _partial_ test script.  If your code passes this script, it
does not mean that it is correct.  You will also need to test your code
interactively and/or write some more tests of your own.
'''

import nose
from nose.tools import *   # for "assert_raises"
import random
from final import *

ntests = 10

def isPoint(p, nrows, ncols):
     '''
     Test if 'p' is a point on a grid of 'nrows' rows and 'ncols' columns.
     Arguments:
       p: a putative point
       nrows: positive integer
       ncols: positive integer
     Return value: 
       True if p is a point on the grid, otherwise False
     '''
     if type(p) is not tuple or len(p) != 2:
          return False
     (row, col) = p
     if type(row) is not int or type(col) is not int:
         return False
     if row < 0 or col < 0:
         return False
     if row >= nrows or col >= ncols:
         return False
     return True

def areAdjacentPoints(p1, p2, nrows, ncols):
    '''
    Return True if point 'p1' is adjacent to point 'p2' on the grid.
    Arguments:
      p1, p2: points
      nrows: positive integer
      ncols: positive integer
    Return value: 
      True if p1 and p2 are adjacent, otherwise False
    '''
    if not (isPoint(p1, nrows, ncols) and isPoint(p2, nrows, ncols)):
        return False
    (r1, c1) = p1
    (r2, c2) = p2
    if r1 == r2:
        return abs(c1 - c2) == 1
    elif c1 == c2:
        return abs(r1 - r2) == 1
    else:
        return False

def isEdge(e, nrows, ncols):
    '''
    Arguments:
      e: an edge
      nrows: positive integer
      ncols: positive integer
    Return value: 
      True if 'e' is a valid edge on the grid.
    '''
    if type(e) is not frozenset or len(e) != 2:
        return False
    (p1, p2) = tuple(e)  # or just: (p1, p2) = e
    return isPoint(p1, nrows, ncols) \
           and isPoint(p2, nrows, ncols) \
           and areAdjacentPoints(p1, p2, nrows, ncols)

def isBox(box, nrows, ncols):
    '''
    Arguments:
      box: a box
      nrows: positive integer
      ncols: positive integer
    Return value: 
      True if 'box' is a valid box on the grid.
    '''
    if type(box) is not tuple or len(box) != 2:
        return False
    if not (isPoint(box, nrows, ncols)):
        return False
    (r, c) = box
    return True

def test_getEdgesFromBox():
    nrows = 5
    ncols = 6
    boxes = [(i, j) for i in range(nrows-1) for j in range(ncols-1)]
    for box in boxes:
        es = getEdgesFromBox(box)
        assert type(es) is list
        assert len(es) == 4
        for edge in es:
            assert isEdge(edge, nrows, ncols)

def test_constructor():
    # Test bad constructor inputs.
    assert_raises(TypeError, DotsAndBoxes, "ten", 10)
    assert_raises(TypeError, DotsAndBoxes, 10, "ten")
    assert_raises(TypeError, DotsAndBoxes, 1.2, 10)
    assert_raises(TypeError, DotsAndBoxes, 10, 3.4)
    assert_raises(ValueError, DotsAndBoxes, -1, 10)
    assert_raises(ValueError, DotsAndBoxes, 0, 10)
    assert_raises(ValueError, DotsAndBoxes, 8, -4)
    assert_raises(ValueError, DotsAndBoxes, 9, 0)
    
    for i in range(ntests):
        nrows = random.randrange(3, 8)
        ncols = random.randrange(3, 8)
        db = DotsAndBoxes(nrows, ncols)
        # Check that the expected fields are there.
        assert hasattr(db, 'nrows')
        assert hasattr(db, 'ncols')
        assert hasattr(db, 'allEdges')
        assert hasattr(db, 'allBoxes')
        assert hasattr(db, 'edgeBoxes')
        assert hasattr(db, 'filledEdges')
        assert hasattr(db, 'filledBoxes')
        assert hasattr(db, 'toMove')

        # Check field values and types.
        assert db.nrows == nrows
        assert db.ncols == ncols
        assert db.toMove in [1, 2]
        assert type(db.allEdges) is set
        assert type(db.allBoxes) is set
        assert type(db.edgeBoxes) is dict
        assert type(db.filledEdges) is set
        assert type(db.filledBoxes) is dict

def test_makeAllEdges():
    for i in range(ntests):
        nrows = random.randrange(3, 8)
        ncols = random.randrange(3, 8)
        db = DotsAndBoxes(nrows, ncols)
        edges = db.makeAllEdges()
        assert type(edges) is set
        for edge in edges:
            assert isEdge(edge, nrows, ncols)
        assert len(edges) == 2 * nrows * ncols - nrows - ncols

def test_makeAllBoxes():
    for i in range(ntests):
        nrows = random.randrange(3, 8)
        ncols = random.randrange(3, 8)
        db = DotsAndBoxes(nrows, ncols)
        boxes = db.makeAllBoxes()
        assert type(boxes) is set
        for box in boxes:
            assert isBox(box, nrows, ncols)
        assert len(boxes) == nrows * ncols - nrows - ncols + 1

def test_makeEdgeBoxes():
    for i in range(ntests):
        nrows = random.randrange(3, 8)
        ncols = random.randrange(3, 8)
        db = DotsAndBoxes(nrows, ncols)
        edges = db.makeAllEdges()
        boxes = db.makeAllBoxes()
        edgeboxes = db.makeEdgeBoxes()
        assert type(edgeboxes) is dict
        for edge in edgeboxes:
            assert isEdge(edge, nrows, ncols)
            bs = edgeboxes[edge]
            assert len(bs) in [1, 2]
            for box in bs:
                assert isBox(box, nrows, ncols)
                assert box in boxes
        assert len(edgeboxes) == len(edges)


if __name__ == '__main__':
    nose.runmodule()

