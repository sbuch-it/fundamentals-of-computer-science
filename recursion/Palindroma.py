########################################################
# Determinazione ricorsiva della Palindromia
########################################################
def Palindroma(x, n):
    P=False
    if ((n==2) and (x[0]==x[1])) or (n==1): P=True
    elif (x[0] == x[n-1]) and Palindroma(x[1:n-1],n-2):
        P=True
    return(P)
#
Parola = input("Stringa ")
print(Palindroma(Parola,len(Parola)))
