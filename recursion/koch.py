import turtle

def koch(t, ordine, lunghezza):
    # Frattale di Koch di un certo ordine.

    if ordine == 0:                    # Passo base
        t.forward(lunghezza)
    else:
        koch(t,ordine-1,lunghezza/3)   # Induzione
        t.left(60)                     
        koch(t,ordine-1,lunghezza/3)   
        t.right(120)                   
        koch(t,ordine-1,lunghezza/3)   
        t.left(60)                     
        koch(t,ordine-1,lunghezza/3)   
#
tartaruga = turtle.Turtle()
#tartaruga.hideturtle()
koch(tartaruga,4,250)

