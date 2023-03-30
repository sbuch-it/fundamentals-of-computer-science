#
# Nim-like
# Due giocatori giocano alternativamente
# Possono prendere fino alla meta' dei fiammiferi rimanenti
# Perde chi raccoglie l'ultimo fiammifero
#
import random
n=int(input("Quanti fiammiferi sono sul tavolo all'inizio? "))
PlayFirst=input("Vuoi giocare per primo? (s/n) ")
if PlayFirst=='s':
    a=int(input("Quanti fiammiferi prendi? " ))
    n=n-a
if (n==0) and (PlayFirst=='s'):
    win=True
else: win=False
m=1+n//2
#
while n>1:
    if ((n-1) % m == 0):
        c=min(1,random.randint(1,m-1))  # Il gioco e' nelle mani dell'avversario
    else:
        c=(n-1) % m # Strategia ottima
        win=True
    n=n-c
    print("Io prendo %d fiammiferi" %c)
    if (n>1):  # chiaramente, non devo procedere se n=1
        a=int(input("Quanti fiammiferi prendi? " ))
        n=n-a
    m=1+n//2
if win: print("Ho vinto!");
else: print("Questa volta ho perso ...")
