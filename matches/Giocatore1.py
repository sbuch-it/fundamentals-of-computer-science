#
# Nim-like
#
import random
#
m=4
f = open("Sincronizzazione.txt", "r")
Stato=f.read().split()
n=int(Stato[1])
f.close()
while n>0:
    f = open("Sincronizzazione.txt", "r")
    Stato=f.read().split()
    n=int(Stato[1])
    if (Stato[0]==str(1)) and (Stato[3]==str(0)):
        if ((n-1) % m == 0):
            c=min(n,random.randint(1,m-1))  # Il gioco e' nelle mani dell'avversario
        else:
            c=(n-1) % m # Strategia ottima
        #
        print(Stato[0],c)
        Stato[2]=str(c)
        Stato[3]="1"
        StatoFile=Stato[0]+" "+Stato[1]+" "+Stato[2]+" "+Stato[3]
        f = open("Sincronizzazione.txt", "w")
        f.write(StatoFile)
f.close()

