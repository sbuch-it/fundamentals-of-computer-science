#############################################
# Calcolo della potenza: soluzione iterativa
# Calcola x^y 
#############################################
def potenza(x, y):
    p=1
    for i in range(y):
        p = p*x
    return(p)
#  
#############################################
#
x = float(input("Base= "))
y = int(input("Esponente= "))
print(potenza(x, y)) 

