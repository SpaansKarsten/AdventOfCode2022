import pdb
foodlist = []
with open('input.txt','r') as f:
    elftotal = 0
    for l in f:
        if l.strip() == '':
            foodlist.append(elftotal)
            elftotal = 0
        else:
            elftotal += int(l.strip())

maxtotal = 0
for i in range(3):
    maxtotal += max(foodlist)
    foodlist.pop(foodlist.index(max(foodlist)))

print(maxtotal)
