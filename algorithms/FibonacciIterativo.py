#
# Calcolo di Fn
#
import math

def Fibonacci(n):
    Fn2=0; Fn1=1
    if n==0: Fn=Fn2
    elif n==1: Fn=Fn1
    else:
        for i in range(0,n-1):
            Fn=Fn1+Fn2
            Fn2=Fn1
            Fn1=Fn
    return(Fn)

def FibonacciReal(n):
    phi1=(1+math.sqrt(5))/2
    phi2=(1-math.sqrt(5))/2
    c=(math.sqrt(5))/5
    Fn=c * (math.pow(phi1,n) - math.pow(phi2,n))
    return(Fn)

print("Calcolo del numero di Fibonacci Fn \n")
n=int(input("Ingresso del numero n per calcolo di Fn " ))
print("Fn = ",Fibonacci(n),"\n")
print("Fn = ",FibonacciReal(n))
