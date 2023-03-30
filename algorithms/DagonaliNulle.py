import numpy as np

# Un esempio
A = np.matrix([[0, 3, 3,0], [-8, 0, 0,4], [-1, 0, 0 ,6],[0, 9, -9 ,0]]) 

# Scrivi l'ingresso
print('A matrix :\n', A)
#
n=A.shape[0]
DiagonaliNulle = True
for i in range(n):
    if (A[i,i]!=0) or (A[i,n-1-i]!=0):
        DiagonaliNulle = False
        break
if DiagonaliNulle: print("La proprieta e' vera")
else: print("La proprieta e' falsa")
        
