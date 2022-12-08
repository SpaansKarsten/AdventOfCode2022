gamescore = {'A': {'X': 3, 'Y': 6, 'Z': 0},
             'B': {'X': 0, 'Y': 3, 'Z': 6} ,
             'C': {'X': 6, 'Y': 0, 'Z': 3}}

choicescore = {'X': 1, 'Y': 2, 'Z': 3}

totalscore = 0
with open('input.txt','r') as f:
    for s in f:
        them, me = [x.strip() for x in s.split(' ')]
        totalscore += gamescore[them][me] + choicescore[me]

print(totalscore)
