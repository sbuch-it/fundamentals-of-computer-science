def SommaPrimi_n_Elemeni(n):
   Somma = 0
   for i in range(1,n+1):
       Somma = Somma + i
   return Somma

def Idea_di_Gauss(n):
    return n*(n+1)/2  

print("Somma dei primi n interi")
n=int(input("Fino a che intero vuoi fare la somma? "))
print(SommaPrimi_n_Elemeni(n))
print("Modo alternativo di calcolare la somma")
print(Idea_di_Gauss(n))
