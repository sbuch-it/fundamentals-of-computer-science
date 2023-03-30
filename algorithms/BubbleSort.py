def BubbleSort(L):
    for k in range(len(L)-1,0,-1):
        for i in range(k):
            if L[i]>L[i+1]:
                L[i],L[i+1]=L[i+1],L[i]

Lista = [541,261,9,117,177,431,554,551,201,65]
BubbleSort(Lista)
print(Lista)
