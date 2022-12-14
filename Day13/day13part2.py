import pdb
import copy

def compare(leftthis, rightthis):
    if isinstance(leftthis,int) and isinstance(rightthis,int):
        if leftthis < rightthis:
            return True
        elif leftthis > rightthis:
            return False
        else:
            return None
    elif isinstance(leftthis,list) and isinstance(rightthis,list):
        if len(leftthis) == 0:
            return True
        elif len(rightthis) == 0:
            return False
        else:
            firstleft = leftthis.pop(0)
            firstright = rightthis.pop(0)
            result = compare(firstleft,firstright)
    elif isinstance(leftthis,int):
        leftthis = [leftthis]
        result = compare(leftthis, rightthis)
    else:
        rightthis = [rightthis]
        result = compare(leftthis, rightthis)

    # This handles if current comparison is inconclusive, i.e. both left and right the same
    if result == None:
        if isinstance(leftthis,list) and isinstance(rightthis,list):
            if len(leftthis) > 0 and len(rightthis) > 0:
                result = compare(leftthis,rightthis)
            elif len(leftthis) > 0:
                result = False
            elif len(rightthis) > 0:
                result = True
            else:
                result = None
        elif isinstance(leftthis,list):
            if len(leftthis) > 0:
                result = compare(leftthis,rightthis)
            else:
                result = True
        elif isinstance(rightthis,list):
            if len(rightthis) > 0:
                result = compare(leftthis,rightthis)
            else:
                result = False

    return result
    
    

ainputlist = [ '[1,1,3,1,1]',
              '[1,1,5,1,1]',
              '[[1],[2,3,4]]',
              '[[1],4]',
              '[9]',
              '[[8,7,6]]',
              '[[4,4],4,4]',
              '[[4,4],4,4,4]',
              '[7,7,7,7]',
              '[7,7,7]',
              '[]',
              '[3]',
              '[[[]]]',
              '[[]]',
              '[1,[2,[3,[4,[5,6,7]]]],8,9]',
              '[1,[2,[3,[4,[5,6,0]]]],8,9]']

inputlist = []
with open('input.txt','r') as f:
    for line in f:
        if line.strip() != '':
            inputlist.append(line)

inputlist.append('[[2]]')
inputlist.append('[[6]]')

test = compare([[1],4],[1,1,5,1,1])
sortedlist = [eval(inputlist.pop(0).strip())]
while len(inputlist) > 0:
    nextentry = eval(inputlist.pop(0).strip())
    sortlistthis = copy.deepcopy(sortedlist)
    for ix in range(len(sortlistthis)):
        result = compare(copy.deepcopy(nextentry),copy.deepcopy(sortedlist[ix]))
        if result:
            sortedlist.insert(ix, nextentry)
            break
        elif ix == len(sortlistthis)-1:
            sortedlist.append(nextentry)

ix1 = sortedlist.index([[2]])+1
ix2 = sortedlist.index([[6]])+1
print(ix1*ix2)
