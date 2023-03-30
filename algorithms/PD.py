#
# Controllo di vettore con "Prevalenza Pari"
#

def PrevalenzaPari(X):
    ContatorePari=0
    Pari=False
    n= len(X)
    for i in range(n):
        if X[i]%2 == 0:
            ContatorePari+=1
        if ContatorePari>int(n/2):
            Pari= True
            break
    return(Pari)

print("Controllo di Prevalenza Pari di un vettore \n")
V=[]  
for i in range(int(input("Quanti elementi sono nella lista? "))):  
    V.append(int(input())) 
print(V,"\n") 

print("La Prevalenza Pari risulta ", PrevalenzaPari(V))

