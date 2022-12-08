import pdb
dirdict = {}

currdir = []
contentlist = []
with open('input.txt','r') as f:
    for l in f:
        if l[0] == '$':
            if contentlist:
                for c in contentlist:
                    if c.split()[0] != 'dir':
                        thisdir = ''
                        for cd in currdir:
                            thisdir += cd+'-'
                            dirdict[thisdir[:-1]] += int(c.split()[0])
                contentlist = []
            if l.split()[1] == 'cd':
                if l.split()[2] == '..':
                    currdir.pop()
                else:
                    currdir.append(l.split()[2])
                    dirdict['-'.join(currdir)] = 0
            elif l.split()[1] == 'ls':
                contentlist = []
        else:
            contentlist.append(l.strip())

for c in contentlist:
    if c.split()[0] != 'dir':
        thisdir = ''
        for cd in currdir:
            thisdir += cd+'-'
            dirdict[thisdir[:-1]] += int(c.split()[0])

spacerequired = 30000000 - 70000000 + dirdict['/']

print(sorted([x for x in dirdict.values() if x > spacerequired])[0])



