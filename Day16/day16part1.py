import pdb
import copy

def traverse_node(currnode,pathsthis,pathlistthis,visited):
    pathlistthis.append(currnode)
    for node in pathsthis[currnode]:
        visited[node] += 1
        if len(pathlistthis) > 30 or visited[node] > 4:
            break
        currnode = node
        traverse_node(currnode,pathsthis.copy(),pathlistthis.copy(),visited.copy())
    pathlist.append(pathlistthis)
        
def traverse_path(paths, time, flowrate,totalflowlist, opened):
    if isinstance(paths,str):
        paths = [paths]
    time += 1
    while len(paths) > 0:
        if time == 30:
            break
        currnode = paths.pop(0)
        if flowrate[currnode] > 0 and currnode not in opened:
            time += 1
            opened.append(currnode)
            totalflowlist.append((30-time)*flowrate[currnode])
            traverse_path(paths.copy(), time, flowrate, totalflowlist.copy(),opened.copy())
        traverse_path(paths.copy(), time, flowrate, totalflowlist.copy(),opened.copy())
            
flowrate = {}
paths = {}
visited = {}
with open('testinput.txt','r') as f:
    for line in f:
        linelist = line.strip().split(' ')
        node = linelist[1]
        flowrate[node] = int(linelist[4].split('=')[1].strip(';'))
        paths[node] = [x.strip(',') for x in linelist[9:]]
        visited[node] = 0


startnode = 'AA'
pathlist = []
traverse_node(startnode, paths, pathlist, visited.copy())
pathtest = ['AA','DD','CC','BB','AA','II','JJ','II','AA','DD','EE','FF','GG','HH','GG','FF','EE','DD','CC']
pdb.set_trace()
opened = []
maxflow = 0
totalflowlist = []
traverse_path(pathlist, 0, flowrate, [], opened)
pdb.set_trace()
for ix, paths in enumerate(pathlist[:-1]):
    print(ix)
    traverse_path(paths, 0, flowrate, 0, maxflow)
pdb.set_trace()

        
