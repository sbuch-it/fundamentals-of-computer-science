import numpy as np

def RicercaSequenziale(T,c):
   i=0; T[T.shape[0]-1]=c
   while  c!=T[i]:i+=1
   return(i)

Dummy=0
Tabella=np.array([2,-3,5,-22,6,12,-4,123,Dummy])
chiave = int(input("Ingresso della chiave "))
indice=RicercaSequenziale(Tabella,chiave)
if indice == Tabella.shape[0]-1:
   print("Chiave non presente nella tabella")
else:
   print("Chiave presente nella tabella nella posizione ",1+indice)

