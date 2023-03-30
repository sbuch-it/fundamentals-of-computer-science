import numpy as np

#
# Controlla se i tre interi assegnati corrispondono alla
# misura dei lati di un triangolo rettangolo
#

a = int(input("primo numero: "))
b = int(input("secondo numero: "))
c = int(input("terzo3 numero: "))

if ((a**2-b**2-c**2==0) or (b**2-a**2-c**2==0) or
    (c**2-a**2-b**2==0)):
    print("Proprieta' Pitagorica")
else: print("Proprita' Pitagorica assente")
    
