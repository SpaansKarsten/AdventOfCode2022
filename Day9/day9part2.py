import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
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
            if jdiff == -1 or jdiff == -2:
                self.move('L')
            elif jdiff == 1 or jdiff == 2:
                self.move('R')
        elif idiff == -2:
            self.move('U')
            if jdiff == -1 or jdiff == -2:
                self.move('L')
            elif jdiff == 1 or jdiff == 2:
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
                
    def position(self):
        print(self.i,self.j)


def plot_positions(knots):
    grid = np.zeros((30,30))
    for knot in knots:
        grid[knot.i,knot.j] = 1
    plt.matshow(grid,cmap=cm.gray)
    plt.show()
    
testinput = ['R 5',
             'U 8',
             'L 8',
             'D 3',
             'R 17',
             'D 10',
             'L 25',
             'U 20']

knotlist = [Knot(500,500) for x in range(10)]
            
grid = np.zeros((1000,1000),dtype=bool)
grid[500,500] = True

with open('input.txt','r') as f:
    for line in f:
        direction = line.split(' ')[0]
        steps = int(line.split(' ')[1])
        for step in range(steps):
            knotlist[0].move(direction)
            for ix in range(1,10):
                knotlist[ix].follow(knotlist[ix-1])
            grid[knotlist[-1].i,knotlist[-1].j] = True
#        plot_positions(knotlist)
print(sum(grid.ravel()))
