import numpy as np

#
# Controlla se una matrice risulta diagonale
#

A = np.array([[3,0,0],[0,3,0],[0,1,2]])

n= A.shape[0]
D=True
for i in range(n):
    for j in range(n):
        if i!=j:
             if A[i,j]!=0: D=False
if D: print("La matrice risulta diagonale")
else: print("La matrice non risulta diagonale")
