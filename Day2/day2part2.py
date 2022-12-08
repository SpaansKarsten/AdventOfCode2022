gamescore = {'X': 0, 'Y': 3, 'Z': 6}

choicescore = {'A': {'X': 3, 'Y': 1, 'Z': 2},
               'B': {'X': 1, 'Y': 2, 'Z': 3},
               'C': {'X': 2, 'Y': 3, 'Z': 1}}

totalscore = 0
with open('input.txt','r') as f:
    for s in f:
        them, me = [x.strip() for x in s.split(' ')]
        totalscore += gamescore[me] + choicescore[them][me]

print(totalscore)
