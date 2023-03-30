#################################################
# Controllo di sottostringa: versione ricorsiva
#################################################
def SottoStringa(S1,S2,n):
    C=False
    if n==0: C=True
    else:
        m=len(S1) - len(S2)
        for k in range(m):
            if (SottoStringa(S1[k:],S2,n-1) and
                (S2[n-1]==S1[k+n-1])): C=True
    return(C)
#
Stringa1 = input("Ingresso prima stringa ")
Stringa2 = input("Ingresso seconda stringa ")
print(SottoStringa(Stringa1,Stringa2,len(Stringa2)))
