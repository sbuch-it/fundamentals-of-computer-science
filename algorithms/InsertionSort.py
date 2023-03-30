def InsertionSort(L):
   for i in range(1,len(L)):
     currentvalue = L[i]
     position = i
     while position>0 and L[position-1]>currentvalue:
         L[position]=L[position-1]
         position = position-1
     L[position]=currentvalue

Lista = [54,26,93,17,77,31,44,55,20]
InsertionSort(Lista)
print(Lista)
