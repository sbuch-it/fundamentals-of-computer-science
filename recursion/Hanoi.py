def Hanoi(n, T1, T2, T3):
    if n == 0: return  # Nessun disco da spostare: facile!
    global contatore
    contatore += 1
    #
    # muovi n-1 dischi da T1 a T2 usando la torre intermedia T3
    #
    Hanoi(n-1, T1, T3, T2)
    #
    # muovi il disco rimanente in T1 a T3
    #
    T3.append(T1.pop())
    #
    print(A, B, C) # visualizza il contenuto delle torri
    #
    # muovi n-1 dischi da T2 a T3 usando la torre intermedia T1
    #
    Hanoi(n-1, T2, T1, T3)
    #
##############################################
# Muovi n dischi dalla torre T1 alla torre T3
# usando la torre intermedia T2.
##############################################
#
# Inizializza le torri:tutti gli n dischi sono sulla torre A.
#
n = 6
A = list(range(n,0,-1))
B, C = [], []
#
print(A, B, C)
contatore = 0
Hanoi(n, A, B, C)
print(contatore)
