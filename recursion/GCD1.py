# 
# Massimo Comun Divisore (versione differenze)
#
def mcd(m,n):
    if (n==0): return m
    else:
        if (m<n):
            m,n=n,m  # scambia m con n
        return mcd(m-n,n)
#
a = int(input("Ingresso del primo numero:"))
b = int(input("Ingresso del secondo numero:"))
print("Massimo Comun Divisore:", mcd(a,b))



