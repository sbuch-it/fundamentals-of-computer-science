#
# Algoritmo di Euclide: versione ricorsiva 
# inversione degli argomenti.
#
def mcd(a, b):
    if b == 0:
        return a
    else:
        return mcd(a % b,b)
#
m = int(input("Ingresso del primo numero:"))
n = int(input("Ingresso del secondo numero:"))
print("Massimo Comun Divisore:", mcd(m,n))
