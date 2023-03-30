import numpy as np

#
# Controlla se una coordinata di un vettore risulta dominante
#

U = np.array([3,1,18,8,1,2,2])

n= U.shape[0]
for i in range(n):
    s=0
    for j in range(n):
        if i!=j: s+=U[j]
    if U[i]>s:
        print("La dominanza si verifica per i = ",i)
        break
if i==n-1: print("Dominanza non assente")
