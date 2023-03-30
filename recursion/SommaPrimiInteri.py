#
# Summa degli interi fino a n  k
#
def SommaRicorsiva(k):
  if(k>0):
    risultato = k+SommaRicorsiva(k-1)
  else:
    risultato = 0
  return risultato

n=int(input("Somma fino a: "))
print("La somma risulta: ",SommaRicorsiva(n))

