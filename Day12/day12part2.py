import numpy as np
import string
import pdb

def get_paths(shape):
    paths = {}
    vertices = []
    for y in range(shape[0]):
        for x in range(shape[1]):
            paths[f'{y},{x}'] = []
            if y-1 >= 0:
                paths[f'{y},{x}'].append((y-1,x))
            if y+1 < shape[0]:
                paths[f'{y},{x}'].append((y+1,x))
            if x-1 >= 0:
                paths[f'{y},{x}'].append((y,x-1))
            if x+1 < shape[1]:
                paths[f'{y},{x}'].append((y,x+1))
            vertices.append((y,x))
    return paths, vertices

def get_min_vertex(cost, vertices):
    min_cost = np.inf
    
    for vertex in vertices:
        if cost[vertex[0],vertex[1]] < min_cost: 
            min_cost = cost[vertex[0],vertex[1]]
            min_vertex = vertex
    return min_vertex
            
def Dijkstra(start,heights):
    paths, vertices = get_paths(heights.shape)
    cum_cost = np.ones_like(heights)*np.inf
    cum_cost[start[0],start[1]] = 0
    while len(vertices) > 0:
        min_vertex = get_min_vertex(cum_cost,vertices)
        vertices.remove(min_vertex)
        cum_cost_this = cum_cost[min_vertex[0],min_vertex[1]]
        for path in paths[f'{min_vertex[0]},{min_vertex[1]}']:
            if path in vertices:
                if heights[min_vertex] - heights[path] <= 1: # We're walking in "reverse", so flip cost
                    costthis = cum_cost_this + 1
                else:
                    costthis = 999999999
                if costthis < cum_cost[path[0],path[1]]:
                    cum_cost[path[0],path[1]] = costthis
    return cum_cost

testinput = ['Sabqponm',
             'abcryxxl',
             'accszExk',
             'acctuvwj',
             'abdefghi']

alphabet = list(string.ascii_letters)

grid = []
with open('input.txt','r') as f:
    for line in f:
        grid.append([alphabet.index(x) for x in line.strip()])

grid = np.array(grid)
start = np.where(grid == 30)
grid[start[0], start[1]] = 25
pathlengths = Dijkstra(start,grid)
alengths = pathlengths[grid == 0]
print(min(alengths))


