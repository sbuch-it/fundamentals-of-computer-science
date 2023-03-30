import turtle
SogliaLunghezza = 5
def CostruisciAlbero(t, lunghezza_ramo, riduci_di, angolo):
  if lunghezza_ramo > SogliaLunghezza:
    t.forward(lunghezza_ramo)
    nuova_lunghezza = lunghezza_ramo - riduci_di
    t.left(angolo)
    CostruisciAlbero(t, nuova_lunghezza, riduci_di, angolo)
    t.right(angolo * 2)
    CostruisciAlbero(t, nuova_lunghezza, riduci_di, angolo)
    t.left(angolo)
    t.backward(lunghezza_ramo)
albero = turtle.Turtle()
albero.hideturtle()
albero.setheading(90)
albero.color('green')
CostruisciAlbero(albero, 50, 5, 30)
