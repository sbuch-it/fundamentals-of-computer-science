#############################################
# Calcolo della potenza: soluzione ricorsiva
# Base reale, esponente intero
# Calcola x^y 
#############################################
def potenza(x, y): 
    if (y == 0): return 1
    elif (int(y % 2) == 0): 
        return (potenza(x, int(y / 2)) *
               potenza(x, int(y / 2))) 
    else: 
        return (x * potenza(x, int(y / 2)) *
                   potenza(x, int(y / 2))) 
#  
#############################################
#
x = float(input("Base= "))
y = int(input("Esponente= "))
print(potenza(x, y)) 

