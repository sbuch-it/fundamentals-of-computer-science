import numpy as np

# Un esempio
S = np.matrix([[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1 ,0],[0, 1, 0 ,0]]) 

# Scrivi l'ingresso
print("La matrice candidata scacchiera e' \n", S)
#
n=S.shape[0]
ScacchieraFlag=True
for i in range(n-1):
    for j in range(n-1):
        if (2* S[i,j] +S[i,j+1]+ S[i+1,j] - 2 != 0):
            ScacchieraFlag=False
            break
if ScacchieraFlag: print("La proprieta e' vera")
else: print("La proprieta e' falsa")
        
