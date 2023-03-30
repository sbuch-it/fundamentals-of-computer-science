# importing necessary modules 
import matplotlib.pyplot as plt 
from random import randint
import time
  
# initializing the list 
x = [] 
y = [] 
  
# setting first element to 0 
x.append(0) 
y.append(0) 
  
n = 0
m_init=60

for m in range(10):
    m=m_init+m
    for i in range(1, 150000): 
  
        # generates a random integer between 1 and 100 
        z = randint(1, 100) 
  
        # the x and y coordinates of the equations 
        # are appended in the lists respectively. 
      
        # for the probability 0.01 
        if z == 1: 
            x.append(0) 
            y.append(0.16*(y[n])) 
      
        # for the probability 0.85     
        if z>= 2 and z<= m: 
            x.append(0.85*(x[n]) + 0.04*(y[n])) 
            y.append(-0.04*(x[n]) + 0.85*(y[n])+1.6) 
      
        # for the probability 0.07     
        if z>= m+1 and z<= 93: 
            x.append(0.2*(x[n]) - 0.26*(y[n])) 
            y.append(0.23*(x[n]) + 0.22*(y[n])+1.6) 
      
        # for the probability 0.07     
        if z>= 94 and z<= 100: 
            x.append(-0.15*(x[n]) + 0.28*(y[n])) 
            y.append(0.26*(x[n]) + 0.24*(y[n])+0.44) 
          
        n = n + 1
    time.sleep(5)
    plt.scatter(x, y, s = 0.2, edgecolor ='green') 

    plt.show()
    #plt.show(block=False)
    # usa la stessa g update usata nella curva ml
