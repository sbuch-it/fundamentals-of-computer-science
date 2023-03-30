import random

n=1000; C=0; 
for i in range(n):
    x=random.uniform(-1,1)
    y=random.uniform(-1,1)
    if (x**2+y**2-1) <= 0: C+=1

print(4*C/n)

