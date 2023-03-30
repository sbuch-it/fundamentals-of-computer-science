import numpy as np
#
# Ricerca dicotomica con interpolazione lineare
#
def RicercaDicotomica(T,c):
   inferiore=0; superiore=T.shape[0]-1;
   if (inferiore == superiore) or (c<T[inferiore]) or (c>T[superiore]):
      predizione=inferiore
   else:
      predizione = inferiore+ int((superiore-inferiore)*(c -T[inferiore])/(T[superiore]-T[inferiore])) 
      while (c != T[predizione]) and (inferiore < superiore):
         if (c > T[predizione]):
            inferiore=predizione+1
         else: superiore=predizione-1
         if inferiore!=superiore:
            predizione = inferiore+int((superiore-inferiore)*(c -T[inferiore])/(T[superiore]-T[inferiore]))
   if (c != T[predizione]): 
      idx=T.shape[0]
   else: idx=predizione
   return(idx)
# 
Tabella=np.array([1,10,20,33,256,1024,2056])
chiave = int(input("Ingresso della chiave "))
indice=RicercaDicotomica(Tabella,chiave)
if indice == Tabella.shape[0]:
   print("Chiave non presente nella tabella")
else:
   print("Chiave presente nella tabella nella posizione ",1+indice)

