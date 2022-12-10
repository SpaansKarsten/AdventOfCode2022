import numpy as np
import pdb
class Knot:
    def __init__(self,i,j):
        self.i = i
        self.j = j

    def move(self,direction):
        if direction == 'R':
            self.j += 1
        elif direction == 'L':
            self.j -= 1
        elif direction == 'U':
            self.i -= 1
        elif direction == 'D':
            self.i += 1
            
    def follow(self,leader):
        idiff = leader.i - self.i
        jdiff = leader.j - self.j

        if idiff == 2:
            self.move('D')
            if jdiff == -1:
                self.move('L')
            elif jdiff == 1:
                self.move('R')
        elif idiff == -2:
            self.move('U')
            if jdiff == -1:
                self.move('L')
            elif jdiff == 1:
                self.move('R')
        elif jdiff == 2:
            self.move('R')
            if idiff == -1:
                self.move('U')
            elif idiff == 1:
                self.move('D')
        elif jdiff == -2:
            self.move('L')
            if idiff == -1:
                self.move('U')
            elif idiff == 1:
                self.move('D')

testinput = ['R 4',
             'U 4',
             'L 3',
             'D 1',
             'R 4',
             'D 1',
             'L 5',
             'R 2']

H = Knot(500,500)
T = Knot(500,500)
grid = np.zeros((1000,1000),dtype=bool)
grid[T.i,T.j] = True

with open('input.txt','r') as f:
    for line in f:
        direction = line.split(' ')[0]
        steps = int(line.split(' ')[1])
        for step in range(steps):
            H.move(direction)
            T.follow(H)
            grid[T.i,T.j] = True

print(sum(grid.ravel()))
