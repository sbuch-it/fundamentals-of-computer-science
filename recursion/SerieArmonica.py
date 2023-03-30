#
# Generazione ricorsiva della serie armonica
#
def H(n):
    if n==1: Armonica=1
    else: Armonica = H(n-1) + 1/n
    return(Armonica)
#
n = int(input("Ingresso del numero:"))
print("Calcolo di H(n) ", H(n))
