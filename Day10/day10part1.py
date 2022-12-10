import pdb
cyclenumber = 1
X = 1
signal_strength = 0

with open('input.txt','r') as f:
    for line in f:
        if line.strip() == 'noop':
            cyclenumber += 1
            if (cyclenumber-20) % 40 == 0:
                print(cyclenumber, X, cyclenumber * X)
                signal_strength += X * cyclenumber
        else:
            cyclenumber += 1
            if (cyclenumber-20) % 40 == 0:
                print(cyclenumber, X, cyclenumber * X)
                signal_strength += X * cyclenumber
            cyclenumber += 1
            X += int(line.strip().split(' ')[1])
            if (cyclenumber-20) % 40 == 0:
                print(cyclenumber, X, cyclenumber * X)
                signal_strength += X * cyclenumber

print(signal_strength)

            
