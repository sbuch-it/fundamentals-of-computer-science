import numpy as np

# Matrici compatibili con prodotto righe-colonne
A = np.matrix([[-1, 3, 0], [1, 0, 2]])  # prima matrice
B = np.matrix([[5, 2], [7, 1], [1, 2]])  # second matrice
C = np.matrix(np.zeros((2,2)))  # inizializzazione  

# Scrivi le matrici
print('A matrix :\n', A)
print('\nB matrix :\n', B)

# calcolo del prodotto
for i in range(C.shape[0]):
    for j in range(C.shape[1]):
        for k in range(A.shape[1]):
            C[i,j] += A[i,k] * B[k,j]

print('\nCalcolo basato su singole coordinate :\n', C)

# Calcolo matriciale diretto gia' presente in Python
DirectC = A * B
print('\nCalcolo diretto con Python :\n', DirectC)
