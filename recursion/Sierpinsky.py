import turtle

def DisegnaTriangolo(points,color,myTurtle):
    myTurtle.fillcolor(color)
    myTurtle.up()
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.down()
    myTurtle.begin_fill()
    myTurtle.goto(points[1][0],points[1][1])
    myTurtle.goto(points[2][0],points[2][1])
    myTurtle.goto(points[0][0],points[0][1])
    myTurtle.end_fill()

def PuntoMezzo(p1,p2):
    return ( (p1[0]+p2[0]) / 2, (p1[1] + p2[1]) / 2)

def Sierpinski(points,degree,myTurtle):
    colormap = ['blue','red','green','white','yellow',
                'violet','orange']
    DisegnaTriangolo(points,colormap[degree],myTurtle)
    if degree > 0:
        Sierpinski([points[0],
                        PuntoMezzo(points[0], points[1]),
                        PuntoMezzo(points[0], points[2])],
                   degree-1, myTurtle)
        Sierpinski([points[1],
                        PuntoMezzo(points[0], points[1]),
                        PuntoMezzo(points[1], points[2])],
                   degree-1, myTurtle)
        Sierpinski([points[2],
                        PuntoMezzo(points[2], points[1]),
                        PuntoMezzo(points[0], points[2])],
                   degree-1, myTurtle)

def main():
   myTurtle = turtle.Turtle()
   myWin = turtle.Screen()
   myPoints = [[-300,-150],[0,300],[300,-150]]
   Sierpinski(myPoints,3,myTurtle)
   myWin.exitonclick()

main()
