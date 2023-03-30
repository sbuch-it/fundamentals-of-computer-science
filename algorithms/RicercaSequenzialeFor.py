import numpy as np

def RicercaSequenziale(T,c):
   idx = T.shape[0]  # metto l'indice in posizione irraggiungibile
   for i in range(T.shape[0]):
       if c == T[i]:
          idx=i
          break
   return(idx)
   
Tabella=np.array([2,-3,5,-22,6,12,-4,123])
chiave = int(input("Ingresso della chiave "))
indice=RicercaSequenziale(Tabella,chiave)
if indice == Tabella.shape[0]:
   print("Chiave non presente nella tabella")
else:
   print("Chiave presente nella tabella nella posizione ",1+indice)

