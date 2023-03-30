from math import *

def Karatsuba(x,y):
    # Definisci la base B = 10
    B = 10
    
    # Passo base: entrambi i numeri sono singole cifre
    if x < 10 and y < 10:
        return x*y    
    #
    # m e' posto come il massimo della lunghezza di x o y
    # Si puo' calcolare con log in base 10,
    # oppure com m = max(len(str(x)), len(str(y)))
    # E' meglio il primo metodo per grossi n
    #
    m = max(int(log10(x)+1), int(log10(y)+1))
    #
    # Controllo m pari/dispari:
    #
    if m % 2 != 0:
        m -= 1
    m2 = int(m/2)
    #
    a, b = divmod(x, B**m2)
    c, d = divmod(y, B**m2)
    #
    ac = Karatsuba(a,c)
    bd = Karatsuba(b,d)
    ad_bc = Karatsuba((a+b),(c+d)) - ac - bd
    #
    return ((ac*(10**m)) + bd + ((ad_bc)*(10**m2)))
    #
###################################
#   Esempio di calcolo
###################################
x = int(input('Primo fattore: '))
y = int(input('Secondo fattore: ')) 
s = str(Karatsuba(x,y))
print (s)
