import numpy as np

# Un esempio
A = np.matrix([[4, 3, 3,2], [-8, 0, 0,4], [-1, 0, 0 ,6],[1, 9, -9 ,2]]) 
#
P=0; S=0; n=A.shape[0]
for i in range(n):
    P+=A[i,i]; S+=A[i,n-1-i]
if P==2*S: print("La proprieta e' vera")
else: print("La proprieta e' falsa")
        
