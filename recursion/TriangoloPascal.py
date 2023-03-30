#################################################
# Triangolo di Pascal
#################################################
def Binomiale(n, k) : # soluzione iterativa
    r = 1
    if (k > n - k) : k = n - k 
    for i in range(0 , k) : 
        r = r * (n - i) 
        r = r // (i + 1) 
    return r
#
def BinRic(n, k): # soluzione ricorsiva
    if (k==0) or (k==n): r=1
    else: r = BinRic(n-1, k-1)+BinRic(n-1, k)
    return r
#
def StampaTriangolo(n) : 
    for line in range(0, n) : 
        for i in range(0, line + 1) : 
            print(BinRic(line, i), 
                " ", end = "") # "end =" aggiunge uno spazio invece di \n
        print()
#
DimensioneTriangolo = int(input('Dimensione Triangolo = '))
StampaTriangolo(DimensioneTriangolo)
