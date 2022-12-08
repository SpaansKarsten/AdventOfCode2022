import string
import pdb

test = ['vJrwpWtwJgWrhcsFMMfFFhFp',
        'jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL',
        'PmmdzqPrVvPwwTWBwg',
        'wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn',
        'ttgJtRGJQctTZtZT',
        'CrZsJsPPZsGzwwsLwLmpwMDw']

alphabet = list(string.ascii_letters)

priority_sum = 0
with open('input.txt','r') as f:
    group = []
    for s in f:
        group.append(s.strip())
        if len(group) == 3:    
            for item in group[0]:
                if (item in group[1] and item in group[2]):
                    print(item)
                    priority_sum += alphabet.index(item)+1
                    group = []
                    break


print(priority_sum)



        
