import numpy as np
import matplotlib.pyplot as plt
import copy
import pdb

def drop_sand(pos,grid,sandstart):
    # Return new position, updated grid (if sand comes to rest), sand came to rest flag, sand dropped off grid flag
    if grid[sandstart[0],sandstart[1]] == 2:
        return pos,grid,True,True
    elif grid[pos[0]+1,pos[1]] == 0:
        pos[0] += 1
        return pos,grid,False,False
    elif grid[pos[0]+1,pos[1]-1] == 0:
        pos[0] += 1
        pos[1] -= 1
        return pos,grid,False,False
    elif grid[pos[0]+1,pos[1]+1] == 0:
        pos[0] += 1
        pos[1] += 1
        return pos,grid,False,False
    else:
        grid[pos[0],pos[1]] = 2
        return pos,grid,True,False

testinput = ['498,4 -> 498,6 -> 496,6\n',
             '503,4 -> 502,4 -> 502,9 -> 494,9\n']

grid = np.zeros((200,1000))
highesti = 0
with open('input.txt','r') as f:
    for line in f:
        nodes = line.strip().split(' -> ')
        startnode = [int(x) for x in nodes.pop(0).split(',')]
        while len(nodes) > 0:
            endnode = [int(x) for x in nodes.pop(0).split(',')]
            if startnode[0] == endnode[0]:
                j = startnode[0]
                i = range(min(startnode[1],endnode[1]),max(startnode[1],endnode[1])+1)
                if max(startnode[1],endnode[1]) > highesti:
                    highesti = max(startnode[1],endnode[1])

            else:
                i = startnode[1]
                if i > highesti:
                    highesti = i
                j = range(min(startnode[0],endnode[0]),max(startnode[0],endnode[0])+1)
            grid[i,j] = 1
            startnode = endnode

grid[highesti+2,:] = 1
            
sandstart = [0,500]
hit_start_flag = False
count = 1

while not hit_start_flag:
    pos = copy.deepcopy(sandstart)
    sand_came_to_rest_flag = False
    while not sand_came_to_rest_flag:
        pos, grid, sand_came_to_rest_flag, hit_start_flag = drop_sand(pos, grid, sandstart)
    count += 1

    
print(np.sum(grid == 2))
plt.matshow(grid)
plt.show()





        
