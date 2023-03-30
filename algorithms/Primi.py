#
# Calcolo dei numeri primi fino ad un dato intero n
#
import math
n=int(input("Numeri primi fino a "))
for i in range(1,n+1):
   Primality=True
   m=int(math.sqrt(i))
   for j in range(2,m+1):
      if i%j==0:
         Primality=False
         break
   if Primality: print(i)
