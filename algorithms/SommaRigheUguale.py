import numpy as np

# Un esempio
A = np.matrix([[-1, 13, 3,0], [-8, 0, 0,23], [-1, -1, 10 ,7]]) 

# Scrivi l'ingresso
print('A matrix :\n', A)
#
SommaUguale=True
m=A.shape[0]; n=A.shape[1]
for i in range(m):
    q=0
    for j in range(n):
        q+=A[i,j]
    if (i>0):
        if (p!=q):
            SommaUguale=False
            break
    p=q

if SommaUguale: print("Matrice con somma righe costante")
else: print("Matrice con somma righe variabile")
    
   
