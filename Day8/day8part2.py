import numpy as np
import pdb

def count(directionlist,height):
    c = 1
    while directionlist.pop() < height:
        if len(directionlist) == 0:
            return c
        c += 1
    return c

grid = []
with open('input.txt','r') as f:
    for line in f:
        grid.append([int(x) for x in list(line.strip())])

grid = np.array(grid)

scenic = np.zeros_like(grid)
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if i==0 or j==0 or i==grid.shape[0]-1 or j==grid.shape[1]-1:
            scenic[i,j]=0
        else:
#            pdb.set_trace()
            height = grid[i,j]
            up = grid[:i,j].tolist()
            down = grid[i+1:,j].tolist()
            down.reverse() # So pop() takes the closest first
            left = grid[i,:j].tolist()
            right = grid[i,j+1:].tolist()
            right.reverse()
            scenic[i,j] = count(up,height) * count(down,height) * count(left,height) * count(right,height)

print(np.max(scenic.ravel()))
                    
