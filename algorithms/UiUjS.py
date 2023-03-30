import numpy as np

###################################################
# E' vero che u_i + u_j = x ? Si assume che i neq j
###################################################

U = np.array([3,2,4,-7,67,3,2,45])
x = int(input("ingresso numero somma "))

Flag=False
for i in range(U.shape[0]):
    for j in range(U.shape[0]):
        if (U[i]+U[j] == x) and (i!=j):
            Flag=True
            break
if Flag: print("La proprieta vale")
else: print("La proprieta non vale")
    
    
