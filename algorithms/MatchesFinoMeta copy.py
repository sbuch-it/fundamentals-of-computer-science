#
# Nim-like
#
# Due giocatori giocano alternativamente
# Possono prendere fino alla meta' dei fiammiferi rimanenti
# Perde chi raccoglie l'ultimo fiammifero
#
import random
import math 
n=int(input("Quanti fiammiferi sono sul tavolo all'inizio? "))
win=False; m=n
PlayFirst=input("Vuoi giocare per primo? (s/n) ")
if PlayFirst=='s':
    a=int(input("Quanti fiammiferi prendi? " ))
    n=n-a
while (n>1):
   m=m//2 
   if  ((n-1)%m == 0) and (int(math.log((n-1),2))%2 ==1):
        c=random.randint(1,m-1)  # Il gioco e' nelle mani dell'avversario
   else:
       c=max((n-1)%m,m-1) # Strategia ottima
       win=True
   n=n-c # Nota che, dopo questo aggiornamento, n-1 >=0 
   print("Io prendo %d fiammiferi" % c)
   if (n>1):  # chiaramente, non devo procedere se n=1
       a=int(input("Quanti fiammiferi prendi? " ))
       n=n-a
if (n==1) and (PlayFirst=='s'): win=True
if win: print("Ho vinto!");
else: print("Questa volta ho perso ...")
