def mergeSort(lista):
    #print("Splitting ",lista)
    if len(lista)>1:
        mezzo = len(lista)//2
        ParteSinistra = lista[:mezzo]
        ParteDestra = lista[mezzo:]
        mergeSort(ParteSinistra)
        mergeSort(ParteDestra)
        #
        i=0; j=0; k=0
        while i < len(ParteSinistra) and j < len(ParteDestra):
            if ParteSinistra[i] <= ParteDestra[j]:
                lista[k]=ParteSinistra[i]
                i=i+1
            else:
                lista[k]=ParteDestra[j]
                j=j+1
            k=k+1
        #
        while i < len(ParteSinistra):
            lista[k]=ParteSinistra[i]
            i=i+1; k=k+1
        while j < len(ParteDestra):
            lista[k]=ParteDestra[j]
            j=j+1; k=k+1
    #print("Merging ",alist)
#
lista = [514,126,93,117,7,314,434,55,20,1,-12,123]
print(lista)
mergeSort(lista)
print(lista)
