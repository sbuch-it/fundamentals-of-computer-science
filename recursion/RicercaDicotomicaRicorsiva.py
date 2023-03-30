def RicercaDicotomica(Tabella, a, b, c):  
    if b >= a: 
        mezzo = (a + b) // 2
        if Tabella[mezzo] == c:
            return mezzo
        elif Tabella[mezzo] > c:
            return RicercaDicotomica(Tabella, a, mezzo-1, c)  
        else:
            return RicercaDicotomica(Tabella, mezzo+1, b, c) 
    else: 
        return -1

#Tabella = [ 2, 3, 4, 10, 40, 123, 200 ] 
Tabella = [1]
chiave = int(input("Ingresso della chiave "))
risultato = RicercaDicotomica(Tabella, 0, len(Tabella)-1, chiave) 
if risultato != -1:
    print("Chiave presente nella posizione ", str(risultato)) 
else: print("Chiave non presente nella tabella") 
