import numpy as np

# Un esempio
A = np.matrix([[0, 3, 3,0], [-8, 0, 0,4], [-1, 0, 0 ,6],[0, 9, -9 ,0]]) 

# Scrivi l'ingresso
print('A matrix :\n', A)
#
n=A.shape[0]; i=0
DiagonaliNulle = True
while  ((i in range(n)) and (A[i,i])==0) and ((A[i,n-1-i]==0)): i+=1
if (i<n): DiagonaliNulle = False
if DiagonaliNulle: print("La proprieta e' vera")
else: print("La proprieta e' falsa")
        
