import pdb
test = ['2-4,6-8',
	'2-3,4-5',
        '5-7,7-9',
        '2-8,3-7',
        '6-6,4-6',
        '2-6,4-8']

result = 0
with open('input.txt','r') as f:
    for l in f:
        elf1, elf2 = l.strip().split(',')
        
        result += (int(elf1.split('-')[0]) in range(int(elf2.split('-')[0]),int(elf2.split('-')[1])+1) or
                   int(elf1.split('-')[1]) in range(int(elf2.split('-')[0]),int(elf2.split('-')[1])+1) or
                   int(elf2.split('-')[0]) in range(int(elf1.split('-')[0]),int(elf1.split('-')[1])+1) or
                   int(elf2.split('-')[1]) in range(int(elf1.split('-')[0]),int(elf1.split('-')[1])+1))
 
print(result)
