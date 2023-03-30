#
################################################
# Generazione delle permutazioni di una stringa
################################################
#
def Permutazioni(parola):
    risultato = []
    #
    if len(parola) == 0:
        risultato.append(parola)
        return risultato
    else:
        for i in range(len(parola)):
            StringaRidotta=parola[:i]+parola[i+1:]
            PermutazioniRidotte= Permutazioni(StringaRidotta)
            for stringa in PermutazioniRidotte:
                risultato.append(parola[i]+stringa)
    return risultato

print(Permutazioni('roma'))
