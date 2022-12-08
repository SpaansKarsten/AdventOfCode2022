import pdb
dirdict = {}

currdir = []
contentlist = []
with open('input.txt','r') as f:
    for l in f:
        if l[0] == '$':
            # Command
            if contentlist:
                # There's and unparsed ls result, parse it
                for c in contentlist:
                    if c.split()[0] != 'dir':
                        # file, needs to be added to current and all parent dir totals
                        thisdir = ''
                        for cd in currdir:
                            # Loop through parent dirs
                            thisdir += cd+'-'
                            dirdict[thisdir[:-1]] += int(c.split()[0])
                contentlist = []
            if l.split()[1] == 'cd':
                if l.split()[2] == '..':
                    # Up one level
                    currdir.pop()
                else:
                    # Down one level
                    currdir.append(l.split()[2])
                    dirdict['-'.join(currdir)] = 0
            elif l.split()[1] == 'ls':
                # Not strictly required
                contentlist = []
        else:
            # Not a command, so part of an ls contents
            contentlist.append(l.strip())

# Handle the final ls contents
for c in contentlist:
    if c.split()[0] != 'dir':
        thisdir = ''
        for cd in currdir:
            thisdir += cd+'-'
            dirdict[thisdir[:-1]] += int(c.split()[0])

valuesum = 0
for value in dirdict.values():
    if value < 100000:
        valuesum += value

print(valuesum)
