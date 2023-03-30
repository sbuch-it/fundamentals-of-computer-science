import matplotlib.pyplot as plt 
from random import randint    
x = []; y = [] # Inizializza la lista dei punti che si generano
x.append(0); y.append(0) #  appendi alla lista (0,0)
m=150000
#
for i in range(0,m):  # ogni punto generato ha indice i
    z = randint(1, 100) # genera numeri random tra 1 e 100
    #
    if z == 1: # Con probabilitita' 0.01 - stelo
        x.append(0) 
        y.append(0.16*(y[i])) 
    #       
    if z>= 2 and z<= 86:  # con probabilta' 0.85 - foglioline
        x.append(0.85*(x[i]) + 0.04*(y[i])) 
        y.append(-0.04*(x[i]) + 0.85*(y[i])+1.6)      
    #
    if z>= 87 and z<= 93: # con probabilita' 0.07 - foglie sinistra
        x.append(0.2*(x[i]) - 0.26*(y[i])) 
        y.append(0.23*(x[i]) + 0.22*(y[i])+1.6)    
    #
    if z>= 94 and z<= 100:  # con probabilita' 0.07 -foglie destra
        x.append(-0.15*(x[i]) + 0.28*(y[i])) 
        y.append(0.26*(x[i]) + 0.24*(y[i])+0.44) 
    #      
################################################
# Visualizzazione della felce
################################################
plt.scatter(x, y, s = 0.2, edgecolor ='green') 
plt.show() 
