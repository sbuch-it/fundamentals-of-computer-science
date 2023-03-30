#
# Controllo di palindromia di una stringa
#
def Palindroma(X):
    PalChk=True
    NumeroCicli=0
    n=len(X)
    for i in range(int(n/2)):
        NumeroCicli+=1
        if X[i] != X[n-i-1]:
            PalChk=False
            break
    return(PalChk,NumeroCicli)

V=input("Ingresso della stringa ")
print(Palindroma(V))

