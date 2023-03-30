import numpy as np
#
# Trova il numero di elementi comunti a U,V - i vettori sono ordinati
# 

U = np.array([1, 3, 6, 9, 10, 91, 207, 323, 344, 450, 1025, 2048, 2049, 3000])   # primo vettore
print(U)                  # Stampa del primo
V = np.array([3,10, 91, 110, 207, 450, 1024, 1025, 2049, 3000, 3600])   # secondo vettore
print(V)                  # Stampa il secondo


m=0; i=0; j=0
while (i in range(U.shape[0])) and (j in range(V.shape[0])):
    if (U[i]==V[j]):m=m+1; i=i+1; j=j+1
    elif (U[i]<V[j]): i=i+1
    else: j=j+1
print(m)
