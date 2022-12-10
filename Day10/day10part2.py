import pdb
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

cyclenumber = 0
X = 1
signal_strength = 0
CRT = []

with open('input.txt','r') as f:
    for line in f:
        sprite = range(X-1,X+2)
        if cyclenumber%40 in sprite:
            CRT.append(0)
        else:
            CRT.append(1)
        if line.strip() == 'noop':
            cyclenumber += 1
        else:
            cyclenumber += 1
            sprite = range(X-1,X+2)
            if cyclenumber%40 in sprite:
                CRT.append(0)
            else:
                CRT.append(1)
            cyclenumber += 1
            X += int(line.strip().split(' ')[1])

CRT = np.reshape(np.array(CRT),(6,40))
plt.matshow(CRT,cmap=cm.gray)
plt.show()

            
