#
# Calcolo del Fattoriale (versione iterativa)
#

def Fattoriale(n):
    Fatt=1
    for i in range(1,n+1):
        Fatt = Fatt*i
    return(Fatt)

print("Calcolo del Fattoriale di un numero \n")
n=int(input("Ingresso del numero n per calcolo del Fattoriale: " ))
print("Fn = ",Fattoriale(n))

