#
# Mim-like con tre persone
# Ogni persona raccoglie (1,2,3,4) e gioca secondo ordine stabilito, con il
# computer che opera per ultimo.  Vince chi raccoglie l'ultimo fiammifero
#
n=27 
while n>0:
   a1=int(input("Primo Giocatore " ))
   a2=int(input("Secondo Giocatore " ))
   a=a1+a2
   n=n-a
   if a<3: c=3-a
   elif a<6: c=6-a
   else: c=9-a
   n=n-c # Notice that, after this update, n-1 >=0 
   print("I prendo %d fiammieri" % c)
   if n>0: print("Sulla tavola sono rimasti,", n, "fiammiferi \n")
   else: print("Ho vinto - come al solito!")
