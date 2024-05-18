import turtle

turtle.shape("turtle")
turtle.speed(0)

def fractal(length, niveles):
    if niveles == 0:
        turtle.forward(length)
        return
    
    length /= 3.0
    fractal(length, niveles - 1)
    turtle.left(60)
    fractal(length, niveles - 1)
    turtle.right(120)
    fractal(length, niveles - 1)
    turtle.left(60)
    fractal(length, niveles - 1)

def Dibujar_Copo(lados, length, niveles):
    angle = 360.0 / lados
    for _ in range(lados):
        fractal(length, niveles)
        turtle.right(angle)

LADOS = 6
LONGITUD = 300
NIVELES = 4

Dibujar_Copo(LADOS, LONGITUD, NIVELES)

turtle.mainloop()