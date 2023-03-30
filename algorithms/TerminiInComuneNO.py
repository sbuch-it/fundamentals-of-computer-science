import numpy as np
#
# Troava il numero di elementi comuni in U,V - senza ordinamento
#

U = np.array([1, 2, 3])   # Primo vettore
print(U)                  # Stampa primo
V = np.array([3, 2, 1])   # Secondo vettore
print(V)                  # Stampa secondo

m=0
for i in range(U.shape[0]):
    for j in range(V.shape[0]):
        if U[i]==V[j]: m=m+1
print(m)
