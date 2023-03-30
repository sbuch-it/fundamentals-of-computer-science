import numpy as np
#
# Simulazione cicli ricerca dicotomica classica e ricerca dicotomica con predizione lineare
#
def RicercaDicotomica(T,c):
   inferiore=0; superiore=T.shape[0]-1; mezzo=int((inferiore+superiore)/2)
   nc=0
   while (c != T[mezzo]) and (inferiore < superiore):
      nc+=1
      if (c > T[mezzo]):
         inferiore=mezzo+1
      else: superiore=mezzo-1
      mezzo=int((inferiore+superiore)/2)
   if c != T[mezzo]:
      idx=T.shape[0]
   else: idx=mezzo
   return(idx,nc)
#
# Ricerca dicotomica con interpolazione lineare
#
def RicercaDicotomicaL(T,c):
   inferiore=0; superiore=T.shape[0]-1;
   nc=0
   if (inferiore == superiore) or (c<T[inferiore]) or (c>T[superiore]):
      predizione=inferiore
   else:
      predizione = inferiore+ int((superiore-inferiore)*(c -T[inferiore])/(T[superiore]-T[inferiore])) 
      while (c != T[predizione]) and (inferiore < superiore):
         nc+=1
         if (c > T[predizione]):
            inferiore=predizione+1
         else: superiore=predizione-1
         if inferiore!=superiore:
            predizione = inferiore+int((superiore-inferiore)*(c -T[inferiore])/(T[superiore]-T[inferiore]))
   if (c != T[predizione]): 
      idx=T.shape[0]
   else: idx=predizione
   return(idx,nc)

n=200

chiave = int(input("Ingresso della chiave "))
Tabella=np.array([])
for i in range(n):   
   Tabella=np.append(Tabella,[2*(i**2)])
   indice,NumeroCicli=RicercaDicotomica(Tabella,chiave)
   indiceL,NumeroCicliL=RicercaDicotomicaL(Tabella,chiave)
   print("Numero cicli: ",NumeroCicli,NumeroCicliL)

