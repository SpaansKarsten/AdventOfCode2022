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
    for s in f:
        s = s.strip()
        rs1 = s[:int(len(s)/2)]
        rs2 = s[int(len(s)/2):]
        for r1 in rs1:
            if r1 in rs2:
                print(r1)
                priority_sum += alphabet.index(r1)+1
                break

print(priority_sum)



        
