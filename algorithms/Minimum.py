import numpy as np

def VectorMinimum(V):
   Min = V[0]
   for i in range(V.shape[0]):
       if V[i] < Min: Min=V[i]
   return(Min)   

V=np.array([2,-3,5,-22,6,12,-4,123])

print(VectorMinimum(V))

