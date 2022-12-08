import numpy as np
import pdb

grid = []
with open('input.txt','r') as f:
    for line in f:
        grid.append([int(x) for x in list(line.strip())])

grid = np.array(grid)

visible = np.zeros_like(grid)
for i in range(grid.shape[0]):
    for j in range(grid.shape[1]):
        if i==0 or j==0 or i==grid.shape[0]-1 or j==grid.shape[1]-1:
            visible[i,j]=1
        else:
            height = grid[i,j]
            if (max(grid[:i,j]) < height or max(grid[i+1:,j]) < height or
                max(grid[i,:j]) < height or max(grid[i,j+1:]) < height):
                visible[i,j] = 1

print(sum(visible.ravel()))
        
                    
