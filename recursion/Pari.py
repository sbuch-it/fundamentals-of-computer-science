#
# Generazione dei numeri pari: versione ricorsiva
#
def Pari(n):
    if n==0: P=[0]
    else:
        P=Pari(n-1)
        if (n % 2==0): P.append(n)
    return(P)
#
n = int(input("Ingresso del numero:"))
print("Insieme dei numeri pari ",Pari(n))
