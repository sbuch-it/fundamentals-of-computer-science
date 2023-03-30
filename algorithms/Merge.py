def Merge(U,V):
    i=0;j=0;m=len(U);n=len(V);W=[]
    while (i<m) and (j<n):
        if (U[i]<V[j]):
            W.append(U[i])
            i+=1
        else:
            W.append(V[j])
            j+=1
    # 
    if (i==m):
        while (j<n):
            W.append(V[j])
            j+=1
    else:
        while (i<m):
            W.append(U[i])
            i+=1
    print(W)

#Primo = [1,3,6,9,14,21]
#Secondo = [-4,10,11,17,35]
Primo = [1,3,6,9,14,21]
Secondo = [4,100,110,170,350]
Merge(Primo,Secondo)
