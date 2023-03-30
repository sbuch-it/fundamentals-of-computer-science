#############################################
#
# Genera tuple di interi a somma definita
#
#############################################

def GeneraSommaDefinita(L,s):
    Lk=[[]]
    if s==1: L=[[1]]
    else:
        for k in range(1,s):
            GeneraSommaDefinita(Lk,k)
            [lk.append(s-k) for lk in Lk]
            L.extend(Lk)
    
#  
#############################################
#
X=[[]]
n = int(input("Somma pari a "))
GeneraSommaDefinita(X,n)
print(X)


