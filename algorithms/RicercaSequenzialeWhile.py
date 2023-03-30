import numpy as np

def RicercaSequenziale(T,c):
   i=0
   while (i<T.shape[0]) and (c!=T[i]):i+=1
   return(i)
   
Tabella=np.array([2,-3,5,-22,6,12,-4,123])
chiave = int(input("Ingresso della chiave "))
indice=RicercaSequenziale(Tabella,chiave)
if indice == Tabella.shape[0]:
   print("Chiave non presente nella tabella")
else:
   print("Chiave presente nella tabella nella posizione ",1+indice)

