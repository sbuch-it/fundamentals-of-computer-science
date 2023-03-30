import random
import matplotlib.pyplot as plt

Max=5000; C=0; Y=[]
for i in range(1,Max):
    C=0
    for k in range(i):
        x=random.uniform(-1,1)
        y=random.uniform(-1,1)
        if (x**2+y**2-1) <= 0: C+=1
    Y.append(4*C/i)

plt.plot(Y)
plt.ylabel('Stima di Pi')
plt.show()
