#
# Calcolo del MCD - Algoritmo Euclide versione somma
# Hp: m<n
from copy import copy
#
m=int(input("Ingresso primo numero m= "))
n=int(input("Ingresso secondo numero n= "))
while n>0:
      d=m-n; m=n; n=d
      if m<n: temp=m; m=n; n=temp
print("Il MCD e' ",m)


