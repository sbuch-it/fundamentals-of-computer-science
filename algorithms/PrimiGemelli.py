#
# Calcolo dei numeri primi gemelli fino ad un dato intero n>2
#
import math
n=int(input("Numeri primi gemelli fino a "))
p=1; print(1,3)
for i in range(2,n+1):
   Primality=True
   m=int(math.sqrt(i))
   for j in range(2,m+1):
      if i%j==0:
         Primality=False
         break
   if ((i==p+2) and Primality): print(p,i);
   if Primality: p=i
     
