#
# Nim-like - Arbitro
# 
# Numero Giocatore: 1,2
# Numero fiammiferi rimasti sul tavolo
# [Ultima] Mossa
# Semaforo (Semaforo=1 l'arbitro alloca il gioco)
#
while True:
    f = open("Sincronizzazione.txt", "r")
    Stato=f.read().split()
    Semaforo=Stato[3]
    Mossa=Stato[2]
    NumeroFiammiferi=Stato[1]
    Giocatore=Stato[0]
    if (Semaforo=="1") and (NumeroFiammiferi!="0"): 
        NumeroFiammiferi = int(NumeroFiammiferi) - int(Mossa)
        Giocatore = 1+int(Giocatore)%2
        Semaforo = "0"
        Stato=str(Giocatore)+" "+str(NumeroFiammiferi)+" "+str(Mossa) +" "+str(Semaforo)
        f = open("Sincronizzazione.txt", "w")
        f.write(Stato)
    f.close()
    #
    if (NumeroFiammiferi==0):
        print("Ha vinto il giocatore no. ", 1+int(Giocatore)%2)
        break



