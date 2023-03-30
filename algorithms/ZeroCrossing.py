import numpy as np

def ZeroCrossing(V):
   Z=0
   for i in range(V.shape[0]-1):
       if V[i]*V[i+1]<0: Z+=1
   return(Z)   

F=np.array([-1,3,-5,22,-6,12,-4,123])

print(ZeroCrossing(F))

