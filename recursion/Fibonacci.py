#
# Fibonacci: versione ricorsiva
#
def fibonacci(n):
    if (n == 0):return 0
    elif (n==1): return 1
    else: return(fibonacci(n-1)+fibonacci(n-2))
#
n = int(input("Ingresso del numero:"))
print("Il corrispondente di Fibonacci:",fibonacci(n))
