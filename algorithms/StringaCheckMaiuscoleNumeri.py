################################################
# Ci sono piu' numeri o maiuscole?
################################################
import sys

ContatoreMaiuscole=0; ContatoreNumeri=0
Stringa=input("Ingresso stringa ")
for i in range(0,len(Stringa)):
   if ord(Stringa[i]) >= 48 and ord(Stringa[i]) <=57:
      ContatoreNumeri+=1
   elif ord(Stringa[i]) >=65 and ord(Stringa[i]) <=90:
      ContatoreMaiuscole+=1
if ContatoreNumeri > ContatoreMaiuscole:
   print("Ci sono piu' numeri di maiuscole")
elif ContatoreNumeri == ContatoreMaiuscole:
   print("Ci sono tanti numeri quante maiuscole")
else:
   print("Ci sono piu'  maiuscole di numeri")

   
