import pdb
stacks = [ ['H','C','R'],
           ['B','J','H','L','S','F'],
           ['R','M','D','H','J','T','Q'],
           ['S','G','R','H','Z','B','J'],
           ['R','P','F','Z','T','D','C','B'],
           ['T','H','C','G'],
           ['S','N','V','Z','B','P','W','L'],
           ['R','J','Q','G','C'],
           ['L','D','T','R','H','P','F','S']]

moves = ['move 1 from 2 to 1',
         'move 3 from 1 to 3',
         'move 2 from 2 to 1',
         'move 1 from 1 to 2']

with open('input.txt','r') as f:
    for move in f:
        number = int(move.split()[1])
        source = int(move.split()[3])-1
        target = int(move.split()[5])-1
        move_crates = stacks[source][-1*number:]
        for x in range(number):
            stacks[source].pop()
        for crate in move_crates:
            stacks[target].append(crate)

for stack in stacks:
    print(stack[-1])
