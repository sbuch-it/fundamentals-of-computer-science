import numpy as np

#
# Conta il numero delle doppie in una stringa
#
S = "abborracciasse"
C=0
for i in range(len(S)-1):
    if S[i]==S[i+1]: C+=1
print("Ci sono ",C," doppie")
