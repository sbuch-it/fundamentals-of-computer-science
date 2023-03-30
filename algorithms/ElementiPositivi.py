import numpy as np

#
# Dati U,V della stessa lunghezza, quali dei due ha piu' elementi positivi - oppure lo stesso numero
#

U = np.array([3,-12,4,-5,-9,0,1])
V = np.array([31,1,-4,-5,0,12,45])
#
n= U.shape[0]
CU=0; CV=0
for i in range(n):
    if U[i]>0: CU+=1
    if V[i]>0: CV+=1
if CU>CV: print("U contiene un maggior numero di positivi")
elif CV>CU: print("V contiene un maggior numero di positivi")
else: print("U e V hanno lo stesso numero di positivi") 
