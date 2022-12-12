import pdb

class Monkey:
    def __init__(self,items,operation,testvalue,throwtrue,throwfalse):
        self.items = items
        self.operation = operation
        self.testvalue = testvalue
        self.throwtrue = throwtrue
        self.throwfalse = throwfalse
        self.inspectedcount = 0

    def get_next_item(self):
        return self.items.pop(0)
        
    def throw(self,item,receivemonkey):
        receivemonkey.items.append(item)

    def do_operation(self, old):
        return eval(self.operation)

monkeys = []
with open('input.txt','r') as f:
    for line in f:
        if 'Monkey' in line:
            pass
        elif 'Starting' in line:
            items = [int(x) for x in line.split(':')[1].strip().split(',')]
        elif 'Operation' in line:
            operation = line.split('=')[1].strip()
        elif 'Test' in line:
            testvalue = int(line.strip().split(' ')[-1])
        elif 'true' in line:
            throwtrue = int(line.strip().split(' ')[-1])
        elif 'false' in line:
            throwfalse = int(line.strip().split(' ')[-1])
        else:
            monkeys.append(Monkey(items, operation, testvalue, throwtrue, throwfalse))
monkeys.append(Monkey(items, operation, testvalue, throwtrue, throwfalse))

testvalues = [x.testvalue for x in monkeys]

#(a+b)%n = (a%n+b)%n -> (a%M+b)%n if n | M
#(a*b)%n = [(a%n)*b]%n -> [(a%M)*b]%n if n | M
#simplest M that works for all testvalues is the product of all testvalues
common_multiplier=1
for tv in testvalues:
    common_multiplier *= tv
    
for monkey in monkeys:
    items = [item % M for item in monkey.items]
    monkey.items = items

for x in range(10000):
    for ix,monkey in enumerate(monkeys):
        while len(monkey.items) > 0:
            monkey.inspectedcount += 1
            item = monkey.get_next_item()
            item = monkey.do_operation(item)
            item = item % common_multiplier
            if item % monkey.testvalue == 0:
                monkey.throw(item,monkeys[monkey.throwtrue])
            else:
                monkey.throw(item,monkeys[monkey.throwfalse])
inspectcount = []
for monkey in monkeys:
    inspectcount.append(monkey.inspectedcount)

high1 = max(inspectcount)
inspectcount.remove(high1)
high2 = max(inspectcount)

print(high1 * high2)
                        
        
            
        


    
    
