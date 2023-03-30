import numpy as np

def RicercaDicotomica(T,c):
   inferiore=0; superiore=T.shape[0]-1; mezzo=int((inferiore+superiore)/2) 
   while (c != T[mezzo]) and (inferiore < superiore):
      if (c > T[mezzo]):
         inferiore=mezzo+1
      else: superiore=mezzo-1
      mezzo=int((inferiore+superiore)/2)
   if c != T[mezzo]:
      idx=T.shape[0]
   else: idx=mezzo
   return(idx)
   
Tabella=np.array([-22,-4,10,12,44])
chiave = int(input("Ingresso della chiave "))
indice=RicercaDicotomica(Tabella,chiave)
if indice == Tabella.shape[0]:
   print("Chiave non presente nella tabella")
else:
   print("Chiave presente nella tabella nella posizione ",1+indice)

