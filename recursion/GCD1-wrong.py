# Exercise: why is this wrong?
def GCD(m,n):
    if(m==n):
        return m
    elif (m>n):
        return(GCD(m,m-n))
    else:
        return(GCD(n,n-m))
    
a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
print("Great Common Divisor:")
print(GCD(a,b))
