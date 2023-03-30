import numpy as np

# Un esempio
S = np.matrix([[1, 0, 1, 0, 1, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1],
               [1, 0, 1, 0, 1, 0, 1, 0],
               [0, 1, 0, 1, 0, 1, 0, 1]]) 

# Scrivi l'ingresso
print("La matrice candidata scacchiera e' \n", S)
#
n=S.shape[0]
ScacchieraFlag=True
for i in range(n):
    for j in range(n):
        if not((i+j)%2==0 and S[i,j]==1
               or (i+j)%2==1 and S[i,j]==0):
            ScacchieraFlag=False
if ScacchieraFlag: print("La proprieta e' vera")
else: print("La proprieta e' falsa")
        
