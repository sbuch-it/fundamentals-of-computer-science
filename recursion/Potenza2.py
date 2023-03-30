#############################################
# Calcolo della potenza: soluzione ricorsiva
# Base reale, esponente intero
# Calcola x^y
#############################################
#
def potenza2(x, y):  
    if(y == 0): return 1
    temp = potenza2(x, int(y / 2))  
    if (y % 2 == 0): 
        return temp * temp 
    else: 
        if(y > 0): return x * temp * temp 
        else: return (temp * temp) / x      
#  
#############################################
#
x = float(input("Base= "))
y = int(input("Esponente= "))
print(potenza2(x, y)) 
  

