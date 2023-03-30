#
# Fattoriale: versione ricersiva
#
def fattoriale(n):
    if(n <= 0):
        return 1
    else:
        return(n*fattoriale(n-1))
#
n = int(input("Ingresso numero:"))
print("Fattoriale:",fattoriale(n))

